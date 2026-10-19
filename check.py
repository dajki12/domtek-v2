from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse,unquote
root=Path('dist');missing=set();files=list(root.rglob('*.html'))
class P(HTMLParser):
 def handle_starttag(self,t,a):
  d=dict(a)
  for k in ['href','src','poster']:
   u=d.get(k,'').strip()
   if u.startswith('/') and not u.startswith('//'):
    path=unquote(urlparse(u).path);target=root/path.lstrip('/')
    if not target.exists():missing.add(path)
for p in files:P().feed(p.read_text())
print('HTML pages:',len(files),'Missing local targets:',len(missing));print('\n'.join(sorted(missing)))
