import json, re, sys, os, glob
from bs4 import BeautifulSoup, NavigableString
SITE='6702bf4ad824953000041187/'
IMGMAP=json.load(open('/home/claude/portfolio/_export/images.json'))
def local(src):
    if not src or SITE not in src: return None
    k=src.split(SITE,1)[1].split('?')[0]
    return IMGMAP.get(k)
def clean_inline(el):
    # keep strong/em/a/br
    out=''
    for c in el.children:
        if isinstance(c, NavigableString): out+=str(c).replace('<','&lt;')
        elif c.name in ('strong','b'): out+='<strong>'+clean_inline(c)+'</strong>'
        elif c.name in ('em','i'): out+='<em>'+clean_inline(c)+'</em>'
        elif c.name=='a': out+=f'<a href="{c.get("href","")}">'+clean_inline(c)+'</a>'
        elif c.name=='br': out+='<br>'
        else: out+=clean_inline(c)
    return out
def page(fn):
    t=open(fn,encoding='utf-8').read()
    s=BeautifulSoup(t,'html.parser')
    areas={}
    for m in re.finditer(r'\.(fe-block-[0-9a-f]+)\s*\{\s*grid-area:\s*(\d+)/(\d+)/(\d+)/(\d+)', t):
        areas.setdefault(m.group(1), tuple(map(int,m.groups()[1:])))  # first = mobile
    out=[]
    main=s.find('main') or s.find(id='sections') or s
    secs=main.select('section.page-section') or [main]
    for sec in secs:
        bg=sec.select_one('.section-background img')
        if bg and local(bg.get('data-src') or bg.get('src')): out.append({'t':'bg','src':local(bg.get('data-src') or bg.get('src'))})
        bl=[]
        for b in sec.select('.fe-block'):
            cls=[c for c in b['class'] if c.startswith('fe-block-')]
            a=areas.get(cls[0],(999,999,0,0)) if cls else (999,999,0,0)
            bl.append((a[0],a[1],b))
        bl.sort(key=lambda x:(x[0],x[1]))
        sec_out=[]
        for r,c,b in bl:
            items=[]
            html=b.select_one('.sqs-html-content')
            if html:
                for el in html.find_all(['h1','h2','h3','h4','p','ul','ol','blockquote'],recursive=True):
                    if el.find_parent(['ul','ol','blockquote']) : continue
                    if el.name in ('ul','ol'): items.append({'t':el.name,'items':[clean_inline(li).strip() for li in el.find_all('li')]})
                    else:
                        x=clean_inline(el).strip()
                        if x: items.append({'t':el.name,'html':x})
            for im in b.select('img'):
                src=local(im.get('data-src') or im.get('src'))
                if src: items.append({'t':'img','src':src,'alt':im.get('alt',''),'w':im.get('width'),'h':im.get('height')})
            for v in b.select('iframe, video'):
                items.append({'t':'embed','src':v.get('src') or v.get('data-src')})
            btn=b.select_one('a.sqs-block-button-element, .sqs-block-button a')
            if btn: items.append({'t':'button','html':btn.get_text(strip=True),'href':btn.get('href')})
            if items: sec_out.append({'row':r,'col':c,'items':items})
        if not bl:
            items=[]; seen=set()
            for el in sec.find_all(['h1','h2','h3','h4','p','ul','ol','blockquote','img','iframe']):
                if el.find_parent(['ul','ol','blockquote']) and el.name!='img': continue
                if el.find_parent(['noscript']): continue
                if el.name=='img':
                    src=local(el.get('data-src') or el.get('src'))
                    if src and src not in seen and not el.find_parent(class_='section-background'):
                        seen.add(src); items.append({'t':'img','src':src,'alt':el.get('alt',''),'w':el.get('width'),'h':el.get('height')})
                elif el.name=='iframe': items.append({'t':'embed','src':el.get('src') or el.get('data-src')})
                elif el.name in ('ul','ol'): items.append({'t':el.name,'items':[clean_inline(li).strip() for li in el.find_all('li')]})
                else:
                    x=clean_inline(el).strip()
                    if x: items.append({'t':el.name,'html':x})
            if items: sec_out.append({'row':0,'col':0,'items':items})
        if sec_out: out.append({'t':'section','blocks':sec_out})
    return out
if __name__=='__main__':
    res={}
    for fn in sorted(glob.glob('/home/claude/portfolio/_export/html/*__*.html')):
        res[os.path.basename(fn)[:-5]]=page(fn)
    json.dump(res,open('/home/claude/tools/content.json','w'),indent=1,ensure_ascii=False)
    for k,v in res.items():
        n=sum(len(b['items']) for s in v if s['t']=='section' for b in s['blocks'])
        imgs=sum(1 for s in v if s['t']=='section' for b in s['blocks'] for i in b['items'] if i['t']=='img')
        print(k, 'sections',len(v),'items',n,'imgs',imgs)
