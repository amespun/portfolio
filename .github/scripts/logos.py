import os, re, urllib.request
os.makedirs('_misc', exist_ok=True)
UA={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()
for n,u in [('ev-logo.png','https://evpassport.com/wp-content/uploads/2025/07/ev-logo_2-1-scaled-1.png'),('papaya-og.png','https://framerusercontent.com/images/vn4AlVs0TX2Hnag2cP2swOh2gg.png')]:
    try: open('_misc/'+n,'wb').write(get(u))
    except Exception as e: open('_misc/'+n+'.err','w').write(str(e))
h=get('https://papayadash.com/').decode('utf-8','ignore')
open('_misc/papaya.html','w').write(h)
for i,m in enumerate(re.findall(r'<svg[^>]*>.*?</svg>', h, re.S)[:12]):
    open(f'_misc/papaya-svg{i}.svg','w').write(m)
imgs=re.findall(r'https://framerusercontent\.com/images/[A-Za-z0-9]+\.(?:png|svg|jpg|webp)', h)
open('_misc/papaya-imgs.txt','w').write('\n'.join(dict.fromkeys(imgs)))
for i,u in enumerate(list(dict.fromkeys(imgs))[:6]):
    try: open(f'_misc/papaya-img{i}'+u[-4:],'wb').write(get(u))
    except Exception: pass
