"""Bouwt data.json uit een export van de Claude-planning.

Gebruik: python3 -I tools/sync.py <exportmap>
De exportmap bevat per collectie (tasks, milestones, weeks, log, meta) JSON-bestanden.
data.json wordt alleen herschreven als de inhoud echt veranderd is.
"""
import glob, json, os, sys
from datetime import datetime, timezone

src = sys.argv[1]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data.json')

def col(name):
    rows = []
    for f in sorted(glob.glob(os.path.join(src, name, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        body = d.get('data', d) if isinstance(d, dict) else {}
        rows.append({'id': os.path.basename(f)[:-5], **body})
    return rows

meta = {r['id']: r for r in col('meta')}
teller = {k: v for k, v in meta.get('teller', {}).items() if k != 'id'}
new = {
    'tasks': col('tasks'),
    'milestones': col('milestones'),
    'weeks': {r['id']: {k: v for k, v in r.items() if k != 'id'} for r in col('weeks')},
    'log': sorted(col('log'), key=lambda r: r.get('at', 0), reverse=True),
    'reflecties': col('reflecties'),
    'teller': teller,
}
old = {}
if os.path.exists(out):
    old = json.load(open(out, encoding='utf-8'))
    old.pop('updatedAt', None)
if old == new:
    print('geen wijzigingen')
    sys.exit(0)
new['updatedAt'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
with open(out, 'w', encoding='utf-8') as fh:
    json.dump(new, fh, ensure_ascii=False, indent=1)
    fh.write('\n')
print('data.json bijgewerkt')
