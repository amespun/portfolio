import json, os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
m=json.load(open('_export/images.json'))
os.makedirs('assets/img',exist_ok=True)
meta={}
for k,src in m.items():
    base=os.path.splitext(os.path.basename(src))[0]
    ext=os.path.splitext(src)[1].lower()
    if ext in ('.gif','.svg','.mp4'):
        meta[k]={'src':src,'w':None,'h':None,'sizes':{}}; continue
    try:
        im=Image.open(src); im=ImageOps.exif_transpose(im)
    except Exception as e:
        print('bad',src,e); continue
    if im.mode not in ('RGB','RGBA'): im=im.convert('RGBA' if 'A' in im.mode or im.mode=='P' else 'RGB')
    W,H=im.size; sizes={}
    for w in (800,1600):
        if W<w and w!=800: continue
        tw=min(w,W); th=round(H*tw/W)
        out=f'assets/img/{base}-{tw}.webp'
        if not os.path.exists(out):
            im.resize((tw,th),Image.LANCZOS).save(out,'WEBP',quality=82,method=5)
        sizes[tw]=out
    meta[k]={'src':src,'w':W,'h':H,'sizes':sizes}
json.dump(meta,open('_export/imgmeta.json','w'),indent=0)
print(len(meta))
