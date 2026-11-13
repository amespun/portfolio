import re, os, json, urllib.request, urllib.parse
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'}
out='_leo/logos'; os.makedirs(out, exist_ok=True)
def get(u, t=20):
    r=urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t); return r.read(), r.headers.get('content-type','')
SITES={'jzg':'https://www.janzandbergen.nl/','amadeus':'https://amadeus.com/en','safeguard':'https://www.safeguardglobal.com/','ptc':'https://www.ptc.com/en','esendex':'https://www.esendex.com/','bridgestone':'https://www.bridgestone.eu/','degustabox':'https://www.degustabox.com/','ultima':'https://www.ultimadisplays.com/','evernex':'https://www.evernex.com/'}
WIKI={'amadeus':'Amadeus IT Group logo','ptc':'PTC logo','bridgestone':'Bridgestone logo','esendex':'Esendex logo','evernex':'Evernex logo','safeguard':'Safeguard Global logo','degustabox':'Degustabox logo','jzg':'Jan Zandbergen logo','ultima':'Ultima Displays logo'}
log={}
for k,u in SITES.items():
    n=0; log[k]=[]
    try:
        html,_=get(u); html=html.decode('utf-8','ignore')
        for m in re.finditer(r'<svg[^>]*>.*?</svg>', html, re.S|re.I):
            s=m.group(0); head=html[max(0,m.start()-400):m.start()]
            if re.search(r'logo', s[:400]+head[-300:], re.I) and n<3:
                open(f'{out}/{k}-site-{n}.svg','w').write(s); log[k].append('inline svg'); n+=1
        for m in re.finditer(r'<img[^>]+>', html, re.I):
            tag=m.group(0)
            if not re.search(r'logo', tag, re.I): continue
            sm=re.search(r'(?:src|data-src)=["\']([^"\']+)', tag)
            if not sm or sm.group(1).startswith('data:'): continue
            src=urllib.parse.urljoin(u, sm.group(1))
            try:
                b,ct=get(src); ext=os.path.splitext(urllib.parse.urlparse(src).path)[1][:5] or '.img'
                open(f'{out}/{k}-site-{n}{ext}','wb').write(b); log[k].append(src); n+=1
            except Exception as e: log[k].append('ERR '+src+' '+str(e))
            if n>=4: break
    except Exception as e: log[k].append('SITE ERR '+str(e))
    try:
        q=urllib.parse.urlencode({'action':'query','format':'json','generator':'search','gsrnamespace':6,'gsrlimit':3,'gsrsearch':WIKI[k]+' filetype:drawing','prop':'imageinfo','iiprop':'url'})
        d=json.loads(get('https://commons.wikimedia.org/w/api.php?'+q)[0])
        for i,p in enumerate((d.get('query') or {}).get('pages',{}).values()):
            url=p['imageinfo'][0]['url']; b,_=get(url)
            open(f'{out}/{k}-wiki-{i}'+os.path.splitext(url)[1],'wb').write(b); log[k].append('wiki '+p['title'])
    except Exception as e: log[k].append('WIKI ERR '+str(e))
json.dump(log, open(f'{out}/log.json','w'), indent=1)
