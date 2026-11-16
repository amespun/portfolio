import os, urllib.request
os.makedirs('_misc', exist_ok=True)
u='https://redpni.com/wp-content/uploads/2019/10/Logo-RedPNi.svg'
r=urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'}), timeout=25)
open('_misc/redpni.svg','wb').write(r.read())
