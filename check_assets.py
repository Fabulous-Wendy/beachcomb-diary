#!/usr/bin/env python3
"""Fail-closed registered WebP image validation for Beachcomb Diary v0.3."""
import argparse, json, pathlib, re, sys
from PIL import Image, UnidentifiedImageError

ROOT = pathlib.Path(__file__).resolve().parent

def check(root=ROOT):
    errors=[]; rows=[]
    try:
        manifest=json.loads((root/'assets.json').read_text(encoding='utf-8'))
        game=(root/'game.js').read_text(encoding='utf-8')
    except Exception as exc:
        return {'status':'FAIL','errors':[f'Cannot read manifest or game.js: {exc}'],'assets':[]}
    if not isinstance(manifest,dict): errors.append('Manifest must be a JSON object');manifest={}
    if len(manifest)!=52:errors.append(f'Expected 52 registered resources; found {len(manifest)}')
    if len(set(manifest))!=len(manifest):errors.append('Duplicate resource ID')
    # JSON parsing itself discards duplicate keys, so detect via pairs hook before validating.
    def unique_pairs(pairs):
        o={}
        for k,v in pairs:
            if k in o:errors.append(f'Duplicate JSON ID: {k}')
            o[k]=v
        return o
    json.loads((root/'assets.json').read_text(encoding='utf-8'),object_pairs_hook=unique_pairs)
    match=re.search(r'window\.ASSETS\s*=\s*(\{.*?\})\s*;',game,re.S)
    if not match:errors.append('Embedded window.ASSETS mapping not located')
    else:
        try:
            embedded=json.loads(match.group(1))
            if embedded!=manifest:errors.append('game.js window.ASSETS differs from assets.json')
        except Exception as exc:errors.append(f'Embedded mapping parse error: {exc}')
    for key,relative in manifest.items():
        issue=[]
        if not isinstance(relative,str) or not relative.startswith('assets/') or pathlib.PurePosixPath(relative).is_absolute() or '..' in pathlib.PurePosixPath(relative).parts:
            issue.append('Invalid path'); path=None
        else:path=root/relative
        if path is not None:
            if not path.is_file():issue.append('Missing file')
            elif path.stat().st_size==0:issue.append('Zero bytes')
            else:
                try:
                    with Image.open(path) as im:
                        im.load();w,h=im.size;mode=im.mode;fmt=im.format
                        if fmt!='WEBP':issue.append(f'Incorrect format: {fmt}')
                        if w<=0 or h<=0:issue.append('Invalid dimensions')
                        # Preserve transparency where the approved packaging expects it.
                        if key=='trash_food_wrapper' and ('A' not in im.getbands() or im.getchannel('A').getextrema()[0]==255):issue.append('Food wrapper transparency missing')
                except (OSError,ValueError,UnidentifiedImageError) as exc:issue.append(f'Decode failure: {type(exc).__name__}')
        errors += [f'{key}: {x}' for x in issue]
        rows.append({'id':key,'path':relative,'size_bytes':path.stat().st_size if path and path.exists() else None,'status':'PASS' if not issue else 'FAIL','issues':issue})
    return {'status':'PASS' if not errors else 'FAIL','total':len(rows),'passed':sum(x['status']=='PASS' for x in rows),'errors':errors,'assets':rows}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=ROOT);p.add_argument('--output',type=pathlib.Path);args=p.parse_args()
    report=check(args.root)
    payload=json.dumps(report,ensure_ascii=False,indent=2)
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(payload,encoding='utf-8')
    print(f"{report['status']}: {report.get('passed',0)}/{report.get('total',0)} resources")
    for issue in report['errors']:print('ERROR:',issue)
    sys.exit(0 if report['status']=='PASS' else 1)
