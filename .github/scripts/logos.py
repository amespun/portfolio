import re, os, urllib.request, urllib.parse, time
UA={'User-Agent':'LogoFetcher/1.0 (personal portfolio; contact via github) Mozilla/5.0'}
out='_leo/logos2'; os.makedirs(out, exist_ok=True)
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=25); return r.read()
log=[]
for name,u in [('bridgestone-a','https://commons.wikimedia.org/wiki/Special:FilePath/Bridgestone_logo.svg'),
               ('bridgestone-b','https://commons.wikimedia.org/wiki/Special:FilePath/Bridgestone_Logo.svg'),
               ('webfleet','https://commons.wikimedia.org/wiki/Special:FilePath/Webfleet_logo.svg')]:
    try: open(f'{out}/{name}.svg','wb').write(get(u)); log.append('ok '+name)
    except Exception as e: log.append(f'ERR {name} {e}')
    time.sleep(3)
for host in ['https://www.esendex.com/','https://www.esendex.co.uk/','https://www.esendex.fr/','https://www.bridgestone.eu/','https://www.bridgestone.com/']:
    try:
        html=get(host).decode('utf-8','ignore'); n=0
        for m in re.finditer(r'<svg[^>]*>.*?</svg>', html, re.S|re.I):
            if n<6 and len(m.group(0))>300:
                open(f'{out}/{urllib.parse.urlparse(host).netloc}-svg{n}.svg','w').write(m.group(0)); n+=1
        srcs=re.findall(r'(?:src|href)=["\']([^"\']+\.(?:svg|png)[^"\']*)', html)
        log.append(host+' :: '+' | '.join(s for s in srcs if 'logo' in s.lower())[:1500])
        for i,s in enumerate([s for s in srcs if 'logo' in s.lower()][:3]):
            try:
                b=get(urllib.parse.urljoin(host,s)); open(f'{out}/{urllib.parse.urlparse(host).netloc}-img{i}'+os.path.splitext(urllib.parse.urlparse(s).path)[1],'wb').write(b)
            except Exception as e: log.append('ERR '+s)
    except Exception as e: log.append(f'SITE ERR {host} {e}')
open(f'{out}/log.txt','w').write('\n'.join(log))
