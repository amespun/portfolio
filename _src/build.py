#!/usr/bin/env python3
"""Builds the static pages of the portfolio from one content list."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQ = 'https://images.squarespace-cdn.com/content/v1/6702bf4ad824953000041187/'
OLD = 'https://www.amespun.com/work/'


def img(i, w=1500):
    return f'{SQ}{i}?format={w}w'


AVATAR = img('c452157e-0501-4f67-b013-13ce41e854d4/Ellipse+26_.png', 300)
PORTRAIT = img('414dfdcf-4e3c-4d4b-b59a-3cc3c60f750d/IMG_5346.jpeg', 1000)
DEVICES = img('3df60a90-7ab0-4d16-8395-9a4751061c20/Group+112596.png')
COMPANIES = ['EVPassport', 'Haufe Group', 'Badi', 'Papaya Dash', 'Fluendo', 'Tekman Education']
LOGOS = [
    ('EVPassport', '1738611996757-K1F3IY26948QJ2HIKGT3/evpassport-logo.jpg', 'square'),
    ('Haufe Group', '402bd146-9ffe-46b2-bf9f-a40b8e4dcc89/images.png', 'wide'),
    ('Badi', '1738685973446-Y3FZC2U0FR4BDMH98OIJ/Screenshot%252B2025-02-04%252Bat%252B17.17.43.jpg', 'square'),
    ('Papaya Dash', 'dc0cfa25-22fd-4946-8e2a-1ba00c336203/9a161780-a02c-9947-ac23-563a862f1016.png', 'wide'),
    ('Fluendo', '1738611978055-CYA6FSJHOEU3G3I2OTYU/Fluendo_LogoPositive.jpg', 'wide'),
    ('Tekman Education', '35bab9af-58d6-4daa-aed8-30acc6288c11/logo_tekman_noclaim.png', 'wide'),
    ('Airflye', '1738612017208-JNTLSEGB9ZMPW8MO73IJ/asasxax_logo.jpg', 'square'),
]

FEATURED = [
    dict(slug='b2b-saas-ev-charging', who='EVPassport', short='EV charging dashboard',
         title='An EV charging dashboard property managers can run on their own',
         tags=['B2B · IaaS', 'Web dashboard', '2024–25'], role='Sole product designer',
         cover=img('cb837a2f-3f01-4432-8367-4f5210a82400/Mockup+%281%29.jpg'), alt='EV charging dashboard on a laptop',
         kpis=[('−39.8%', 'support tickets'), ('+23.4%', 'engagement'), ('+14%', 'new business owners')]),
    dict(slug='b2c-ev-charging', who='EVPassport', short='App-free EV charging',
         title='Charging an EV without downloading an app',
         tags=['B2C · IaaS', 'iOS · Android · App Clip', '2024–25'], role='Sole product designer',
         cover=img('1739547286663-5W8VCLEAGWGAXLAXQ0AJ/close-up-electric-car-france_%281%29.jpg'), alt='Charging an electric car with a phone',
         kpis=[('+46.6%', 'engagement'), ('+30.3%', 'sessions'), ('+7.4%', 'new users')]),
    dict(slug='saas-team-development', who='Haufe Group', short='Teampact',
         title='Teampact: team retrospectives people actually finish',
         tags=['B2B SaaS', 'Web app', '2021–24'], role='Senior product designer',
         cover=img('fe678532-a447-40b7-8aed-36c0a5a38845/Mockup+%283%29.jpg'), alt='Teampact team health dashboard on a laptop',
         kpis=[('7→3 min', 'onboarding'), ('60→80%', 'survey completion'), ('45→60', 'NPS')]),
    dict(slug='marketplace-growth', who='Badi', short='Badi marketplace growth',
         title='Growth experiments for a rental marketplace',
         tags=['B2C marketplace', 'iOS · Android · Web', '2020–21'], role='Product designer, growth team',
         cover=img('1741965609552-E2KLJCQYO2M889UQQM8W/Mockup+%282%29.jpg'), alt='Badi rental marketplace app screens',
         kpis=[('A/B tests', 'onboarding and search'), ('Interviews', 'with tenants and landlords')], notes=True),
]
EARLIER = [
    dict(slug='ai-fleet-manager', who='Papaya Dash', short='AI fleet copilot', title='An AI copilot for EV and fleet operators',
         tags=['B2B SaaS', 'Web · AI', '2025'], role='Senior product designer · 6-month discovery',
         cover=img('b6360d8e-ed74-455e-b96f-69a1f3dede55/amespun_Close-up_photorealistic_MacBook_Pro_mockup_screen_filli_22854080-d1da-4904-8233-ccfdfb577dc2.jpg', 1000),
         alt='AI fleet manager dashboard on a laptop'),
    dict(slug='design-system', who='Badi', short='Habitat design system', title='Habitat: the first design system at Badi',
         tags=['B2C marketplace', 'Design system', '2020'], role='Product designer',
         cover=img('1728240600202-H45QN2VOYDR7WRLR74MV/Screenshot+2024-10-06+at+20.49.23.png', 1000), alt='Habitat design system components'),
    dict(slug='videogame-platform', who='Fluendo', short='Gaming social network', title='A social network for gamers',
         tags=['B2C', 'Mobile · Web', '2019'], role='Product designer',
         cover=img('1741980242783-N1VOKR3LIJB409AKAYLM/Mockup+%285%29.jpg', 1000), alt='Gaming social network app screens'),
    dict(slug='uxui-kids-learning', who='Tekman Education', short='Kids learning platform', title='A learning platform for kids',
         tags=['B2B2C', 'Web', '2015–18'], role='Product designer',
         cover=img('1731074386961-1X8UOKNI6FFH53YT1KES/WNW.jpg', 1000), alt='Kids learning platform screens'),
]
# Work page order: strongest and most recent first
# Work page order: newest first
PROJECTS = [EARLIER[0], FEATURED[0], FEATURED[1], FEATURED[2], FEATURED[3], EARLIER[1], EARLIER[2], EARLIER[3]]
BEYOND = [
    ('Illustration', 'European-inspired illustrations and watercolour prints that I design and sell on Etsy.', ('Visit the Etsy shop', 'https://www.etsy.com/shop/amespunn')),
    ('ämespun studio', 'Branding and fast no-code websites for small businesses, in four languages.', ('See studio work', 'studio/')),
    ('Mentoring', 'Mentor on ADPList for designers at every stage.', ('Book a session', 'https://adplist.org/mentors/aida-martinez-espun')),
    ('Writing', 'Case studies and process notes on Medium and Prototypr.', ('Read on Medium', 'https://medium.com/@amespun')),
]


import hashlib
CSS_V = hashlib.md5(open(f'{ROOT}/assets/site.css','rb').read()).hexdigest()[:8]


PHOTOS = dict(
    portrait=img('793587e8-8abb-42ed-bd6b-bdae4ff21f79/92e20c21-8f22-4200-a88e-f76f1ee1dc52_SnapseedCopy.jpeg', 1000),
    smile=img('414dfdcf-4e3c-4d4b-b59a-3cc3c60f750d/IMG_5346.jpeg', 1000),
    hike=img('2a2f48c6-6e38-4c9f-9a1f-aba8a4749d2a/IMG_2681.jpeg', 1000),
    beach=img('04701f9a-d4c3-4908-8bf6-2297f7e1483e/IMG_0186.jpg', 1000),
)
FACTS = [('10+', 'years in product design'), ('15+', 'years in design'), ('4', 'languages, Dutch in progress'), ('BCN → NL', 'from Barcelona to the Netherlands')]
EXPERIENCE = [
    ('Skydreams', '', 'B2B2C marketplace', 'Senior Product Designer', '2026 – now', 'nl'),
    ('Papaya Dash', 'UK company', 'B2B2C SaaS · Green tech', 'Senior Product Designer', '2025', 'bcn'),
    ('EVPassport', 'US company', 'B2B2C IaaS · EV green tech', 'Staff Product Designer', '2024 – 2025', 'bcn'),
    ('Haufe Group', 'German company', 'B2B SaaS · IT services', 'Senior Product Designer', '2021 – 2024', 'bcn'),
    ('Badi', '', 'B2C marketplace', 'Product Designer, Growth & Design Systems', '2020 – 2021', 'bcn'),
    ('Airflye', 'US company', 'B2C travel', 'Product Designer', '2019 – 2020', 'bcn'),
    ('Fluendo', '', 'B2C gaming social network', 'Product Designer', '2019', 'bcn'),
    ('Tekman Education', '', 'B2B2C education', 'Product Designer', '2015 – 2018', 'bcn'),
]
SITES = {'Skydreams': 'https://www.skydreams.com/', 'Papaya Dash': 'https://papayadash.com/', 'EVPassport': 'https://www.evpassport.com/',
         'Haufe Group': 'https://www.haufegroup.com/en', 'Badi': 'https://badi.com/', 'Airflye': 'https://airflye.com/',
         'Fluendo': 'https://fluendo.com/', 'Tekman Education': 'https://www.tekmaneducation.com/'}
PLACES = [
    ('nl', 'The Netherlands', 'Since 2026, in-house at a Dutch scale-up.'),
    ('bcn', 'Barcelona, Spain', 'Spanish startups and international companies from the US, Germany and the UK, working from their Barcelona teams.'),
]
EXPERTISE = ['Product vision & roadmapping', 'UX strategy', 'Design systems & style guides', 'End-to-end product design',
             'Growth metric analysis', 'Stakeholder alignment', 'Cross-functional leadership', 'Design operations',
             'Driving UX maturity', 'SaaS conceptualization', 'Research & testing', 'Art direction & branding', 'Mentoring']
FLAGS = {
    'es': '<rect width="30" height="20" fill="#AA151B"/><rect y="5" width="30" height="10" fill="#F1BF00"/>',
    'ca': '<rect width="30" height="20" fill="#FCDD09"/>' + ''.join(f'<rect y="{2.22 * (2 * i + 1):.2f}" width="30" height="2.22" fill="#DA121A"/>' for i in range(4)),
    'en': '<rect width="30" height="20" fill="#012169"/><path d="M0 0L30 20M30 0L0 20" stroke="#fff" stroke-width="4"/><path d="M0 0L30 20M30 0L0 20" stroke="#C8102E" stroke-width="1.6"/><path d="M15 0V20M0 10H30" stroke="#fff" stroke-width="6"/><path d="M15 0V20M0 10H30" stroke="#C8102E" stroke-width="3.6"/>',
    'fr': '<rect width="30" height="20" fill="#fff"/><rect width="10" height="20" fill="#002654"/><rect x="20" width="10" height="20" fill="#CE1126"/>',
    'nl': '<rect width="30" height="20" fill="#21468B"/><rect width="30" height="13.33" fill="#fff"/><rect width="30" height="6.67" fill="#AE1C28"/>',
}
LANGCODE = {'Spanish': 'es', 'Catalan': 'ca', 'English': 'en', 'French': 'fr', 'Dutch': 'nl'}


def flag(code):
    return f'<svg class="flag" viewBox="0 0 30 20" width="24" height="16" aria-hidden="true">{FLAGS[code]}</svg>'


LANGUAGES = [('Hola', 'Spanish', 'Native'), ('Bon dia', 'Catalan', 'Native'), ('Hello', 'English', 'Full professional'), ('Bonjour', 'French', 'C1'), ('Hallo', 'Dutch', 'A1, learning')]
QUOTES = [
    ('It’s hard to find people as proactive and decisive as Aïda. She’s been a key member of the UX/UI team ever since her arrival. She’s a natural leader and a team player.', 'Mercè Delgado', 'CEO, Fluendo'),
    ('Aïda took on the challenge of redesigning the app, transforming it into a much more intuitive and user-friendly experience. Her collaborative approach and openness to iteration fostered a strong dynamic between product and design.', 'Margarida', 'Product Manager, EVPassport'),
    ('Aïda has an exceptional ability to foresee project needs and tackle them efficiently. Her designs stand out for their aesthetic appeal and functionality, reflecting her deep understanding of user experience.', 'Miguel', 'Team Lead & Senior Researcher'),
    ('An innovative thinker who can conceptualize and design aesthetically pleasing and functional products. She is always willing to take on feedback, which she incorporates into her work to ensure the final product meets or exceeds expectations.', 'Raul', 'Senior Product Manager'),
]
ARTICLES = [
    ('How I designed an app in 5 days to plan your team’s vacation', 'https://medium.com/prototypr/how-i-design-an-app-in-5-days-about-planning-your-teams-vacation-3b7c983691be', img('fe761940-f0e6-4077-b0d3-bb66180461e4/Screenshot+2024-10-14+at+22.55.02.png', 1000)),
    ('First Coach: an app for recent graduates to learn job-market basics', 'https://medium.com/prototypr/first-coach-an-app-for-recent-graduates-to-learn-job-market-basics-c014f8cb72cd', img('03bf9d4b-2294-4793-a530-b509d251450a/Screenshot+2024-10-14+at+22.44.21.png', 1000)),
    ('Wallapop: designing a new rent feature', 'https://medium.com/prototypr/wallapop-new-rent-feature-e33a2783d492', img('563ccfa6-44b0-43f2-bb94-ef2b360ffce6/Screenshot+2024-10-15+at+22.40.23.png', 1000)),
]
STUDIO = [
    ('B2B healthcare SaaS', 'UX/UI design', 'b2b-healthcare-saas', 'bbaccdcc-a09f-4d52-b8c0-96a0bba35240/amespun_Close-up_photorealistic_MacBook_Pro_mockup_screen_filli_85d9a0fb-b70c-4cf1-9c21-20e454b06405.jpg'),
    ('Luxury Service Concierge', 'No-code website + branding', 'branding-concierge-luxury', '1739098746554-KHGPYQ6666L33A0MCK2N/Free+MacBook+Pro+on+Table+Mockup+%281%29.jpg'),
    ('Outweb Studio', 'No-code website + branding', 'outweb-studio', '1738665314506-T1FMS84ZFLT0N6U159LN/Mockup.jpg'),
    ('European illustrations', 'Illustration · Etsy shop', 'illustrations', 'f3942949-4c22-41b3-8eee-a1b2b2a66ebe/il_1588xN.6003542903_2rbe.jpg'),
    ('Personal branding', 'Brand identity', 'personal-branding', '1737905645317-RYNOALK7FWQ63LGO9F4R/Free_Businness_Card_Mockup_1+%281%29.jpg'),
    ('Hair salon', 'Branding', 'hairsalon-branding', '1730817533283-W7SNPKZ16P2JUBRXK4UQ/fadfFrame+10.jpg'),
    ('Wedding stationery on Etsy', 'Print design', 'wedding-etsy', '1737394028120-KDPREP0KH25RNVYFR97F/blank-wedding-invitation-top-view.jpg'),
    ('Truffle business', 'Branding', 'branding-truffle', '1728939614178-EOL3GG4KG8O6A2JQR85D/Screenshot+2024-10-14+at+22.59.27.png'),
    ('UI design', 'Concept work', 'ui-design', 'fe761940-f0e6-4077-b0d3-bb66180461e4/Screenshot+2024-10-14+at+22.55.02.png'),
    ('Children’s publishing', 'Editorial design', 'editorial-design', '1731075935697-6ZWCAMRPZ6LLB4T7YMIS/CATALEG+TEKMAN_1.png'),
    ('Interior design', '3D visualisation', 'interior-design', '1731075618383-ZHH0FVDA4JSK35FKO1HG/Captura+de+pantalla+2015-10-28+a+las+0.59.24.png'),
]


def collage(big=False):
    return f'''<div class="collage{' big' if big else ''}" aria-hidden="true">
      <span class="ph a">{pic(PHOTOS["portrait"], "", "320px", w=1000, h=1250)}</span>
      <span class="ph b">{pic(PHOTOS["hike"], "", "260px", w=1000, h=1250)}</span>
    </div>'''


def facts():
    return '<ul class="facts">' + ''.join(f'<li><strong>{n}</strong><span>{l}</span></li>' for n, l in FACTS) + '</ul>'


def quote_html(q):
    return f'<blockquote class="q"><p>“{q[0]}”</p><footer><b>{q[1]}</b> · {q[2]}</footer></blockquote>'


def head(title, desc, base):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#ffffff">
<link rel="icon" type="image/png" sizes="32x32" href="{base}assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{base}assets/favicon-64.png">
<link rel="apple-touch-icon" href="{base}assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SQ}cb837a2f-3f01-4432-8367-4f5210a82400/Mockup+%281%29.jpg?format=1500w">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Hanken+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/site.css?v={CSS_V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


MAIL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m4 7 8 6 8-6"/></svg>'


def nav(base, current):
    items = [('Work', f'{base}work/', 'work'), ('About', f'{base}about/', 'about'),
             ('Studio', f'{base}studio/', 'beyond'), ('Contact', '#contact', 'contact')]
    cur = lambda n: ' aria-current="page"' if n == current else ''
    links = ''.join(f'<a href="{h}"{cur(n)}>{n}</a>' for n, h, _ in items)
    island = ''.join(f'<a href="{h}">{n}</a>' for n, h, _ in items[:3])
    dock = ''.join(f'<a href="{h}" data-spy="{s}"{cur(n)}>{n}</a>' for n, h, s in items)
    return f'''<header class="topbar" data-island>
  <div class="full"><div class="wrap">
    <a class="me" href="{base}"><img src="{AVATAR}" alt="" width="44" height="44"><span class="id"><b>Aïda Martínez Espún</b><small>Senior Product Designer</small></span></a>
    <nav class="links" aria-label="Main">{links}</nav>
    <button class="iconbtn" type="button" data-copy aria-label="Copy email address">{COPY_ICON}</button>
  </div></div>
  <nav class="island" aria-label="Quick navigation"><img src="{AVATAR}" alt="">{island}<button type="button" data-copy>{COPY_ICON}{labels("Copy email")}</button></nav>
</header>
<nav class="dock" aria-label="Sections">{dock}</nav>
'''


ARROW = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_DOWN = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'
EXT = '<svg class="ic ext" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'
CHECK = '<svg class="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path pathLength="1" d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
MAIL_ICON = MAIL_SVG.replace('<svg ', '<svg class="i-mail" ')
COPY_ICON = f'<span class="swap">{MAIL_ICON}{CHECK}</span>'


def labels(idle, done='Copied'):
    return f'<span class="labels"><span class="l-idle">{idle}</span><span class="l-done" data-done>{done}</span></span>'


import json, re
IMETA = json.load(open(f'{ROOT}/_export/imgmeta.json'))
BYSRC = {v['src']: v for v in IMETA.values()}


def meta_of(u):
    """Accepts a Squarespace URL/id or a local assets/sq path; returns image meta."""
    if u in BYSRC: return BYSRC[u]
    k = u.replace(SQ, '').split('?')[0]
    return IMETA.get(k)


def best(u, w=1600):
    m = meta_of(u)
    if not m: return u
    if not m['sizes']: return '@@/' + m['src']
    ks = sorted(int(x) for x in m['sizes'])
    pick = next((k for k in ks if k >= w), ks[-1])
    return '@@/' + m['sizes'][str(pick)]


def pic(url, alt, sizes, eager=False, w=None, h=None):
    m = meta_of(url)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    if not m or not m['sizes']:
        src = '@@/' + m['src'] if m else url
        return f'<img src="{src}" alt="{alt}" {load}>'
    srcset = ', '.join(f'@@/{p} {k}w' for k, p in sorted(m['sizes'].items(), key=lambda x: int(x[0])))
    W, H = m['w'], m['h']
    return f'<img src="{best(url, 800)}" srcset="{srcset}" sizes="{sizes}" width="{W}" height="{H}" alt="{alt}" {load}>'


def tags(t):
    return '<div class="tags">' + ''.join(f'<span>{x}</span>' for x in t) + '</div>'


def card(p, lead=False):
    k = ''
    if p.get('kpis'):
        k = f'<div class="kpis{" notes" if p.get("notes") else ""}">' + ''.join(
            f'<div class="kpi"><strong>{v}</strong>{l}</div>' for v, l in p['kpis']) + '</div>'
    who = f' <span class="who">· {p["who"]}</span>' if p.get('who') else ''
    sizes = '(max-width: 900px) 100vw, 720px' if lead else '(max-width: 900px) 100vw, 600px'
    return f'''<a class="card{' lead' if lead else ''}" href="@@/work/{p["slug"]}/">
  <div class="media" style="view-transition-name:cover-{p["slug"]}">{pic(p["cover"], p["alt"], sizes)}</div>
  <div class="body">
    {tags(p["tags"])}
    <h3>{p["title"]}{who}</h3>
    <p class="role">{p["role"]}</p>
    {k}
    <span class="more">Read case study {ARROW}</span>
  </div>
</a>'''


def small(e):
    return f'''<a class="small" href="@@/work/{e["slug"]}/">
  <div class="media">{pic(e["cover"], e["alt"], "(max-width: 600px) 100vw, (max-width: 900px) 50vw, 380px", w=1600, h=1000)}</div>
  <b>{e["title"]} {ARROW}</b><span>{e["meta"]}</span>
</a>'''


def contact(base=''):
    pages = [('Work', f'{base}work/'), ('About', f'{base}about/'), ('Studio', f'{base}studio/')]
    work = [(p['short'], f'{base}work/' + p['slug'] + '/') for p in FEATURED]
    social = [('LinkedIn', 'https://www.linkedin.com/in/amespun/'), ('Behance', 'https://www.behance.net/amespun'),
              ('Dribbble', 'https://dribbble.com/amespun'), ('Medium', 'https://medium.com/@amespun'),
              ('ADPList', 'https://adplist.org/mentors/aida-martinez-espun')]
    li = lambda xs: ''.join(f'<li><a href="{h}">{n}</a></li>' for n, h in xs)
    return f'''<footer class="footer" id="contact"><div class="card-dark">
  <p class="greet"><span data-greet>Hola</span>, let’s talk.</p>
  <p class="sub">Spanish, Catalan, English and French at work. Dutch in progress.</p>
  <button class="mail" type="button" data-copy>amespun@gmail.com <em>{COPY_ICON}{labels("Copy")}</em></button>
  <div class="cols">
    <div><h2>Pages</h2><ul>{li(pages)}</ul></div>
    <div><h2>Selected work</h2><ul>{li(work)}</ul></div>
    <div><h2>Elsewhere</h2><ul>{li(social)}</ul></div>
    <div><h2>Based in</h2><ul><li>The Netherlands</li><li>Senior Product Designer at Skydreams</li></ul></div>
  </div>
  <div class="colophon"><span>© 2026 Aïda Martínez Espún</span><span>Designed and built by me.</span></div>
</div></footer>
'''


def foot():
    return '''</main>
<script>
// Copy email: the mail icon cross-fades into a check that draws itself, the label slides to "Copied"
document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
  const done = b.querySelector('[data-done]');
  try {
    await navigator.clipboard.writeText('amespun@gmail.com');
    if (done) done.textContent = 'Copied';
    if (b.classList.contains('iconbtn')) b.setAttribute('aria-label', 'Email copied');
  } catch {
    if (done) done.textContent = 'amespun@gmail.com';
  }
  b.classList.add('copied');
  clearTimeout(b._t);
  b._t = setTimeout(() => {
    b.classList.remove('copied');
    if (b.classList.contains('iconbtn')) b.setAttribute('aria-label', 'Copy email address');
  }, 2000);
}));

// Header collapses into the island after the first screen
const bar = document.querySelector('[data-island]');
const onScroll = () => bar.classList.toggle('scrolled', window.scrollY > 120);
window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

// Greeting in my languages
const words = ['Hola', 'Bon dia', 'Hello', 'Bonjour', 'Hallo'];
const greet = document.querySelector('[data-greet]');
if (greet && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  let i = 0;
  setInterval(() => {
    greet.classList.add('out');
    setTimeout(() => { i = (i + 1) % words.length; greet.textContent = words[i]; greet.classList.remove('out'); }, 250);
  }, 2400);
}

// Highlight the current section in the phone dock
const spy = [...document.querySelectorAll('#about,#beyond,#contact')];
if (spy.length > 1) {
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) document.querySelectorAll('[data-spy]').forEach(a => a.dataset.spy === e.target.id ? a.setAttribute('aria-current', 'true') : a.removeAttribute('aria-current'));
  }), { rootMargin: '-45% 0px -50% 0px' });
  spy.forEach(s => io.observe(s));
}
</script>
</body>
</html>
'''


def more_work(base=''):
    rest = [p for p in PROJECTS if p not in FEATURED[:2]]
    thumbs = ''.join(f'<span style="--i:{n}">{pic(p["cover"], "", "96px")}</span>' for n, p in enumerate(rest[:5]))
    names = ' · '.join(p['short'] for p in rest[:3]) + ' and more'
    return f'''<a class="more-work" href="{base}work/">
      <span class="stack" aria-hidden="true">{thumbs}</span>
      <span class="text"><b>{len(rest)} more projects</b><span>{names}</span></span>
      <span class="btn primary">See all work {ARROW}</span>
    </a>'''


def home():
    beyond = ''.join(
        f'<li><b>{t}</b><p>{d}</p>' + (f'<a class="ext-link" href="{l[1]}">{l[0]} {EXT if l[1].startswith("http") else ARROW}</a>' if l else '') + '</li>' for t, d, l in BEYOND)
    return head('Aïda Martínez Espún · Senior Product Designer',
                'Senior Product Designer in the Netherlands with 10+ years in product design, across B2B and B2C SaaS, marketplaces and green tech.', '') + nav('', None) + f'''
<main class="wrap" id="main">
  <section class="hero">
    <div>
      <h1>I design B2B and B2C products people stick with.</h1>
      <p class="lede">Senior Product Designer with 10+ years in product design across SaaS, marketplaces and green tech, from discovery to measurable results.</p>
      <div class="hero-actions">
        <a class="btn primary" href="#work">View selected work {ARROW_DOWN}</a>
        <button class="btn secondary" type="button" data-copy>{COPY_ICON}{labels("Copy email")}</button>
      </div>
    </div>
    <div class="art">{pic(DEVICES, "Product screens from recent projects", "(max-width: 900px) 100vw, 520px", eager=True, w=1500, h=1060)}</div>
  </section>
  <div class="worked"><p>Worked with</p><ul class="logos" aria-label="Companies I’ve worked with">{''.join(f'<li class="{k}"><img src="{SQ}{u}?format=300w" alt="{n}" loading="lazy" decoding="async"></li>' for n, u, k in LOGOS)}</ul></div>

  <section class="section" id="work">
    <div class="section-head"><h2>Selected work</h2><a class="more-link" href="work/">All {len(PROJECTS)} projects {ARROW}</a></div>
    <div class="grid featured">{card(FEATURED[0], lead=True)}{card(FEATURED[1], lead=True)}</div>
    {more_work()}
  </section>

  <section class="section about-home" id="about">
    {collage()}
    <div class="about-copy">
      <h2 class="h2">Hi, I’m Aïda.</h2>
      <p>I spent ten years in Barcelona designing B2B and B2C products for Spanish startups and for US, German and UK companies with teams there. Now I’m in the Netherlands. I like the messy part: aligning product, engineering and sales on what to build, then proving it with research and numbers.</p>
      {facts()}
      {quote_html(QUOTES[0])}
      <a class="more-link" href="about/">More about me {ARROW}</a>
    </div>
  </section>

  <section class="section beyond" id="beyond">
    <div class="intro"><h2 class="h2">Beyond the day job</h2><p>What I design when nobody asks me to.</p></div>
    <ul>{beyond}</ul>
  </section>
''' + contact() + foot()


def work():
    return head('Work · Aïda Martínez Espún', 'Product design case studies by Aïda Martínez Espún: EV charging, B2B SaaS, marketplaces and more.', '../') + nav('../', 'Work') + f'''
<main class="wrap" id="main">
  <section class="page-head">
    <h1>Work</h1>
    <p>All {len(PROJECTS)} projects from my full-time roles, with the problem, my role and what changed. Freelance branding and websites live in the <a href="../studio/">studio</a>.</p>
  </section>
  <section class="section work-all" style="margin-top:48px" aria-label="All projects">
    <div class="grid">{''.join(card(p) for p in PROJECTS)}</div>
  </section>
''' + contact('../') + foot()


def about():
    logo_of = {n: (u, k) for n, u, k in LOGOS}
    def mark(c):
        u, k = logo_of.get(c, (None, ''))
        z = {'EVPassport': 2.0, 'Badi': 1.75, 'Airflye': 1.2}.get(c)
        st = f' style="--z:{z}"' if z else ''
        return f'<span class="logo {k}" aria-hidden="true"><img src="{SQ}{u}?format=300w" alt="" loading="lazy" decoding="async"{st}></span>' if u else '<span class="logo" aria-hidden="true"></span>'
    def row(c, cc, k, r, y):
        tag = f' <em>{cc}</em>' if cc else ''
        return f'''<li>{mark(c)}<div><b><a class="co" href="{SITES[c]}" target="_blank" rel="noopener">{c}<span class="sr"> (opens in a new tab)</span><i class="ext" aria-hidden="true">{EXT}</i></a>{tag}</b><span>{r}</span></div><div class="meta">{f'<span class="yr">{y}</span>' if y else ''}<span class="kind">{k}</span></div></li>'''
    exp = ''.join(f'''<div class="place"><p class="where"><b>{name}</b><span>{note}</span></p><ol class="timeline">{''.join(row(*e[:5]) for e in EXPERIENCE if e[5] == key)}</ol></div>''' for key, name, note in PLACES)
    langs = ''.join(f'<li><span class="hi">{flag(LANGCODE[n])}<span lang="{LANGCODE[n]}">{g}</span></span><b>{n}</b><span>{l}</span></li>' for g, n, l in LANGUAGES)
    arts = ''.join(f'''<a class="small" href="{u}"><div class="media">{pic(im, "", "(max-width: 600px) 100vw, 380px", w=1600, h=1000)}</div><b>{tt} {EXT}</b><span>Prototypr · Medium</span></a>''' for tt, u, im in ARTICLES)
    return head('About · Aïda Martínez Espún', 'About Aïda Martínez Espún, Senior Product Designer in the Netherlands: experience, expertise, languages and recommendations.', '../') + nav('../', 'About') + f'''
<main class="wrap" id="main">
  <section class="about-hero">
    <div>
      <h1>Senior Product Designer, specialised in Business UX Strategy, B2B2C SaaS</h1>
      <p class="lede"><strong>10+ years</strong> of experience in <strong>startups</strong> and <strong>scale-ups</strong>, and <strong>15+ years</strong> in the <strong>design</strong> field. I specialise in <strong>UX strategy</strong>, <strong>design systems</strong>, and aligning user experience with <strong>business impact</strong>, particularly in <strong>B2B2C SaaS</strong>.</p>
      <p class="lede">I thrive on solving <strong>complex problems</strong>, <strong>strategic thinking</strong>, <strong>scaling</strong> design processes, and <strong>collaborating</strong> across <strong>product</strong>, <strong>engineering</strong> and <strong>leadership</strong> teams. I’ve also been a <strong>mentor</strong> on <strong>ADPList</strong>, supporting the next generation of designers. I’m a <strong>people person</strong>: I do my best work <strong>face to face</strong>, so I enjoy going to the office and working side by side with my team, not 100% remote.</p>
      <p class="lede">As a side project, I also create <strong>no-code websites</strong>, help <strong>small businesses scale</strong>, do <strong>branding</strong> and design <strong>European-inspired illustrations</strong> that I sell on <strong>Etsy</strong>, blending tech and creativity in hands-on projects.</p>
      {facts()}
    </div>
    {collage(big=True)}
  </section>

  <section class="section split">
    <h2 class="h2">Experience</h2>
    <div class="places">{exp}</div>
  </section>

  <section class="section split">
    <h2 class="h2">What I bring</h2>
    <ul class="chips">{''.join(f'<li>{e}</li>' for e in EXPERTISE)}</ul>
  </section>

  <section class="section split">
    <h2 class="h2">Languages</h2>
    <ul class="langs">{langs}</ul>
  </section>

  <section class="section split">
    <h2 class="h2">Outside work</h2>
    <ul class="hobbies">
      <li><b>Ice skating</b><span>My favourite way to switch off. I’m on the rink whenever I can.</span></li>
      <li><b>Baking sourdough</b><span>Patience, testing and iterating, one loaf at a time. Not so different from design.</span></li>
      <li><b>Learning Dutch</b><span>Ik leer Nederlands. A little better every week.</span></li>
    </ul>
  </section>

  <section class="section">
    <div class="section-head"><h2>What people say</h2></div>
    <div class="quotes">{''.join(quote_html(q) for q in QUOTES)}</div>
  </section>

  <section class="section">
    <div class="section-head"><h2>Writing</h2><a class="more-link" href="https://medium.com/@amespun">All articles {EXT}</a></div>
    <div class="earlier">{arts}</div>
  </section>
''' + contact('../') + foot()


def studio():
    items = ''.join(f'''<a class="small" href="@@/studio/{s}/"><div class="media">{pic(SQ + u, "", "(max-width: 600px) 100vw, (max-width: 900px) 50vw, 380px", w=1600, h=1000)}</div><b>{n} {ARROW}</b><span>{k}</span></a>''' for n, k, s, u in STUDIO)
    return head('Studio · Aïda Martínez Espún', 'ämespun studio: freelance UX/UI, no-code websites, branding and illustration by Aïda Martínez Espún.', '../') + nav('../', 'Studio') + f'''
<main class="wrap" id="main">
  <section class="page-head">
    <h1>ämespun studio</h1>
    <p>Beyond my full-time work, I take on selected freelance projects: UX/UI design, no-code websites, branding and illustration. It’s where I keep my hands on every part of design, from a logo to a launch.</p>
  </section>
  <section class="section services" style="margin-top:48px">
    <div><b>UX/UI design</b><p>Product and interface design for startups and small teams, from flows to a ready-to-build UI.</p></div>
    <div><b>No-code websites</b><p>Fast, polished websites for small businesses, built to be easy to update yourself.</p></div>
    <div><b>Branding & illustration</b><p>Identities, print and illustration with a hand-made touch.</p></div>
  </section>
  <section class="section" style="margin-top:72px">
    <div class="section-head"><h2>Selected studio work</h2></div>
    <div class="earlier">{items}</div>
  </section>
''' + contact('../') + foot()



# ---------- Case studies and studio pages, rebuilt from the Squarespace export ----------
# Three-line overview per case study, written from the case study's own text.
SUMMARY = {
    'b2b-saas-ev-charging': ('Operators and businesses had no central, reliable place to manage their EV charging networks, monitor stations and handle their users.',
                             '<strong>Sole product designer.</strong> Led the UX strategy, built the first design system, ran research and aligned product, engineering, sales and support.',
                             '<strong>39.8% fewer</strong> support tickets, <strong>23.4% more</strong> engagement, <strong>14% more</strong> new business owners and <strong>60% more</strong> role-management sessions.'),
    'b2c-ev-charging': ('Drivers struggled with navigation and unclear charger screens across the web, the native app and the App Clip, so many ended up calling support.',
                        '<strong>Sole product designer</strong> across iOS, Android and web: UX strategy, design system, research and roadmap with product and engineering.',
                        '<strong>46.6% more</strong> engagement, <strong>7.4% more</strong> new users and <strong>39.8% fewer</strong> support tickets.'),
    'saas-team-development': ('Teampact helps teams improve collaboration through performance metrics, but people found it too complex and time-consuming to use.',
                              '<strong>Senior product designer.</strong> Defined the product strategy with PMs, led design end to end from research to usability testing, and mentored designers.',
                              'Onboarding from <strong>7 to 3 minutes</strong>, survey completion from <strong>60% to 80%</strong>, NPS from <strong>45 to 60</strong>, <strong>+20%</strong> retention and <strong>+15%</strong> subscriptions.'),
    'ai-fleet-manager': ('Fleet operators lose uptime and money because mechanical issues go undetected until something fails.',
                         '<strong>Senior product designer</strong> in a small team: UX strategy, experimenting with AI and designing the platform from scratch.',
                         'A <strong>6-month discovery</strong>: market and user research, the first MVP designs and a landing page.'),
    'marketplace-growth': ('Make renting a room in a big city simple, and keep people coming back to the app, by understanding tenants’ and landlords’ pain points.',
                           '<strong>Product designer on the growth team</strong>, with two PMs and two development teams: interviews, UX and visual decisions, fast iteration and data analysis.',
                           'Growth experiments shaped by <strong>interviews, prototypes and data</strong>, shipped in fast iterations.'),
    'design-system': ('Designers and developers at Badi needed one shared source of foundations, components and patterns.',
                      '<strong>Product designer:</strong> research, naming, the Sketch library, documentation and the workflow with engineers.',
                      '<strong>Habitat</strong>, Badi’s first design system, with a shared library and documentation for design and engineering.'),
    'videogame-platform': ('Help gamers find other players to match with and discover new videogames.',
                           '<strong>Product designer:</strong> competitive analysis, personas, user flows, prototypes, style guide, branding and logo.',
                           'A social platform taken from <strong>research to build</strong> with engineering, with its own brand and style guide.'),
}
DIVIDERS = re.compile(r'more detailed explanation|full process', re.I)
METRIC_CH = re.compile(r'impact|result|outcome', re.I)

CONTENT = json.load(open(f'{ROOT}/_export/content.json'))
LABELS = {'year', 'company', 'services', 'stack', 'client', 'role'}
BACK = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 18l-6-6 6-6"/></svg>'


def txt(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()


def heading(h):
    h = re.sub(r':\s*$', '', h.strip())
    h = re.sub(r'<br\s*/?>', ' ', h)
    h = re.sub(r'</?(strong|b|em|i)>', '', h)
    return re.sub(r'\s+', ' ', h).strip()


def is_spaced(h):
    return bool(re.fullmatch(r'(?:\S\s+){4,}\S', txt(h)))


def unspace(h):
    t = re.sub(r'\s{2,}', '|', re.sub(r'<[^>]+>', ' ', h).strip())
    t = ' '.join(w.replace(' ', '') for w in t.split('|'))
    return t.capitalize()


def items_of(key):
    out = []
    for si, sec in enumerate(CONTENT.get(key, [])):
        if sec['t'] != 'section':
            continue
        for b in sec['blocks']:
            for it in b['items']:
                out.append(dict(it, sec=si))
    return out


def split_hero(items):
    first = items[0]['sec'] if items else 0
    title = intro = None
    meta, body = [], []
    i = 0
    while i < len(items):
        it = items[i]
        if it['sec'] != first:
            body.extend(items[i:])
            break
        t = it['t']
        if t == 'p' and txt(it['html']).lower() in LABELS and i + 1 < len(items) and items[i + 1]['t'] in ('h4', 'h3', 'p'):
            meta.append((txt(it['html']).capitalize(), items[i + 1]['html']))
            i += 2
            continue
        if t == 'h1' and title is None:
            title = heading(it['html'])
        elif t == 'p' and is_spaced(it['html']):
            body.append(dict(it, t='note'))
        elif t == 'p' and title is not None and intro is None:
            intro = it['html']
        else:
            body.append(it)
        i += 1
    return title, intro, meta, body


def figure(run):
    def one(it):
        w, h = int(it.get('w') or 0), int(it.get('h') or 0)
        tall = ' tall' if w and h and h / w > 1.6 else ''
        return f'<figure class="cs-fig{tall}">{pic(it["src"], it.get("alt") or "", "(max-width: 900px) 100vw, 1120px")}</figure>'
    if len(run) == 1:
        return one(run[0])
    return '<div class="cs-gallery">' + ''.join(one(x) for x in run) + '</div>'


POINT = re.compile(r'^\s*(?P<e1>[^\w<\s&]{1,4}\s*)?<strong>\s*(?P<e2>[^\w<\s&]{1,4}\s*)?(?P<t>.+?)(?:<br\s*/?>)?\s*</strong>\s*(?:<br\s*/?>|[–—:-])?\s*(?P<d>.*)$', re.S)
NUM = re.compile(r'([−+-]?\d[\d.,]*\s?%|\d+\s?(?:→|->|to)\s?\d+%?)')


def as_point(html):
    m = POINT.match(html)
    if not m:
        return None
    t = heading(m.group('t')).strip(' –-:')
    d = m.group('d').strip()
    e = (m.group('e1') or m.group('e2') or '').strip()
    if not t or len(txt(t)) > 90 or txt(d) == txt(t):
        return None
    if not txt(d) and not e:
        return None
    return dict(e=e, t=t, d=d)


def points_html(pts, metric=False):
    cells = ''
    for p in pts:
        n = NUM.search(p['t']) if metric else None
        nd = NUM.search(txt(p['d'])) if metric and not n else None
        d = f'<span>{p["d"]}</span>' if txt(p['d']) else ''
        if n:
            label = (p['t'][:n.start()] + p['t'][n.end():]).strip(' –-:')
            cells += f'<li class="metric"><strong class="n">{n.group(1)}</strong><b>{label}</b>{d}</li>'
        elif nd:
            cells += f'<li class="metric"><strong class="n">{nd.group(1)}</strong><b>{p["t"]}</b>{d}</li>'
        elif p.get('plain'):
            cells += f'<li class="plain"><span>{p["d"]}</span></li>'
        else:
            e = f'<i aria-hidden="true">{p["e"]}</i>' if p['e'] else ''
            cells += f'<li>{e}<b>{p["t"]}</b>{d}</li>'
    return f'<ul class="cs-points{" metrics" if metric else ""}">{cells}</ul>'


CSO = ('challenge', 'problem', 'solution', 'approach', 'outcome', 'result', 'results', 'goal', 'impact')


def is_label(it):
    if it['t'] not in ('p', 'note'):
        return False
    t = txt(it['html'])
    if is_spaced(it['html']):
        return True
    return bool(t) and t.upper() == t and any(ch.isalpha() for ch in t) and len(t.split()) <= 5 and len(t) < 48


def label_text(it):
    t = txt(it['html'])
    return unspace(it['html']) if is_spaced(it['html']) else t.capitalize()


def prepare(run, chname=''):
    out, i = [], 0
    while i < len(run):
        it = run[i]
        nxt = run[i + 1] if i + 1 < len(run) else None
        # Challenge / Solution / Outcome blocks
        if is_label(it) and txt(it['html']).lower() in CSO:
            parts, j = [], i
            while j < len(run) and is_label(run[j]) and txt(run[j]['html']).lower() in CSO:
                lab, body, j = label_text(run[j]), [], j + 1
                while j < len(run) and not is_label(run[j]) and run[j]['t'] in ('p', 'ul', 'ol'):
                    body.append(run[j]); j += 1
                parts.append((lab, body))
            if len(parts) >= 2:
                out.append({'t': 'cso', 'parts': parts}); i = j; continue
            if len(parts) == 1 and parts[0][1]:
                out.append({'t': 'h3', 'html': parts[0][0]}); out.extend(parts[0][1]); i = j; continue
        # Label + statement -> callout
        if is_label(it) and nxt and nxt['t'] in ('h3', 'h4') and len(txt(nxt['html'])) > 60:
            out.append({'t': 'callout', 'html': heading(nxt['html']), 'cap': label_text(it)}); i += 2; continue
        if is_label(it):
            if nxt is None:
                i += 1; continue
            out.append({'t': 'h3', 'html': label_text(it)}); i += 1; continue
        # Short subheading + one paragraph, repeated -> cards
        if it['t'] in ('h3', 'h4') and len(txt(it['html'])) <= 60 and nxt and nxt['t'] == 'p' and len(txt(nxt['html'])) <= 420:
            pairs, j = [], i
            while j + 1 < len(run) and run[j]['t'] in ('h3', 'h4') and len(txt(run[j]['html'])) <= 60 and run[j + 1]['t'] == 'p' and len(txt(run[j + 1]['html'])) <= 420 and (j + 2 >= len(run) or run[j + 2]['t'] in ('h3', 'h4')):
                pairs.append(dict(e='', t=heading(run[j]['html']), d=run[j + 1]['html'])); j += 2
            if len(pairs) >= 2:
                out.append({'t': 'pts', 'pts': pairs}); i = j; continue
        # "#1 … #2 …" or one-line-per-goal paragraphs -> text cards
        if it['t'] == 'p':
            lines = [l.strip() for l in re.split(r'<br\s*/?>', it['html']) if txt(l)]
            if len(lines) >= 3 and all(re.match(r'#\d', txt(l)) for l in lines):
                out.append({'t': 'pts', 'pts': [dict(e='', t='', d=re.sub(r'^#\d+\s*', '', txt(l)), plain=True) for l in lines]}); i += 1; continue
        # Plain lists in role / takeaway chapters -> text cards
        if it['t'] == 'ul' and re.search(r'role|takeaway|learning|responsib', chname, re.I) and 2 <= len(it['items']) <= 10 and not all(as_point(x) for x in it['items']):
            out.append({'t': 'pts', 'pts': [dict(e='', t='', d=x, plain=True) for x in it['items']]}); i += 1; continue
        out.append(it); i += 1
    return out


def cso_html(parts):
    cells = ''
    for lab, body in parts:
        inner = ''.join(f'<{b["t"]}>' + ''.join(f'<li>{x}</li>' for x in b['items']) + f'</{b["t"]}>' if b['t'] in ('ul', 'ol') else f'<p>{b["html"]}</p>' for b in body)
        k = lab.lower()
        cls = ' out' if k in ('outcome', 'result', 'results', 'impact') else ''
        cells += f'<div class="{k}{cls}"><dt>{lab}</dt><dd>{inner}</dd></div>'
    return f'<dl class="cs-cso">{cells}</dl>'


def textrun(run, metric=False, chname=''):
    run = prepare(run, chname)
    # Group runs of "Title – description" paragraphs (and lists of them) into scannable cards
    grouped, buf = [], []
    for it in run:
        if it['t'] in ('pts', 'cso', 'callout'):
            if buf:
                grouped.append(('pts', buf)); buf = []
            grouped.append(('it', it)); continue
        pt = as_point(it['html']) if it['t'] == 'p' else None
        if pt:
            buf.append(pt); continue
        if buf:
            grouped.append(('pts', buf)); buf = []
        if it['t'] == 'ul' and len(it['items']) >= 2:
            lp = [as_point(x) for x in it['items']]
            if all(lp):
                grouped.append(('pts', lp)); continue
        grouped.append(('it', it))
    if buf:
        grouped.append(('pts', buf))
    run = []
    for k, v in grouped:
        if k == 'pts' and len(v) >= 2:
            run.append({'t': 'pts', 'pts': v})
        elif k == 'pts':
            run.append({'t': 'p', 'html': f'<strong>{v[0]["e"]} {v[0]["t"]}</strong><br>{v[0]["d"]}'})
        else:
            run.append(v)
    out = []
    for it in run:
        if it['t'] == 'cso':
            out.append(cso_html(it['parts'])); continue
        if it['t'] == 'callout':
            out.append(f'<figure class="cs-callout"><p>{it["html"]}</p><figcaption>{it["cap"]}</figcaption></figure>'); continue
        if it['t'] == 'pts':
            out.append(points_html(it['pts'], metric or all(NUM.match(p['t'].strip()) or NUM.search(p['t'][:12]) for p in it['pts'])))
            continue
        t = it['t']
        if t in ('ul', 'ol'):
            out.append(f'<{t}>' + ''.join(f'<li>{x}</li>' for x in it['items']) + f'</{t}>')
        elif t in ('h3', 'h4'):
            if len(txt(it['html'])) > 90:
                out.append(f'<p class="cs-statement">{heading(it["html"])}</p>')
            else:
                out.append(f'<h3>{heading(it["html"])}</h3>')
        elif t == 'note' or (t == 'p' and is_spaced(it['html'])):
            out.append(f'<p class="cs-note">{unspace(it["html"])}</p>')
        elif t == 'blockquote':
            out.append(f'<blockquote>{it["html"]}</blockquote>')
        elif t == 'embed' and it.get('src'):
            src = it['src'] if it['src'].startswith('http') else 'https:' + it['src']
            out.append(f'<div class="cs-embed"><iframe src="{src}" loading="lazy" allowfullscreen title="Video"></iframe></div>')
        elif t == 'button':
            out.append(f'<p><a class="btn" href="{it["href"]}">{it["html"]} {ARROW}</a></p>')
        elif t in ('p', 'h1', 'h2'):
            out.append(f'<p>{it["html"]}</p>')
    return ''.join(out)


def chapters(body):
    chs, cur = [], {'h': None, 'items': []}
    big = sum(1 for it in body if it['t'] in ('h1', 'h2') and len(txt(it['html'])) < 60)
    levels = ('h1', 'h2') if big >= 3 else ('h1', 'h2', 'h3', 'h4')
    for it in body:
        if cur['h'] and DIVIDERS.search(cur['h']):
            levels = ('h1', 'h2', 'h3', 'h4')
        if it['t'] in levels and len(txt(it['html'])) < (60 if it['t'] in ('h1', 'h2') else 50) and not txt(it['html']).startswith('('):
            if cur['h'] or cur['items']:
                chs.append(cur)
            cur = {'h': heading(it['html']), 'items': []}
        else:
            cur['items'].append(it)
    if cur['h'] or cur['items']:
        chs.append(cur)
    html = []
    seen_div = False
    for ch in chs:
        rows, run, kind = [], [], None
        for it in ch['items'] + [None]:
            k = None if it is None else ('img' if it['t'] == 'img' else 'txt')
            if k != kind and run:
                rows.append((kind, run))
                run = []
            if it is not None:
                run.append(it)
                kind = k
        inner = ''
        metric = bool(ch['h'] and METRIC_CH.search(ch['h']))
        for k, r in rows:
            if k == 'img':
                inner += f'<div class="cs-wide">{figure(r)}</div>'
            else:
                inner += f'<div class="cs-text">{textrun(r, metric, ch["h"] or "")}</div>'
        cid = re.sub(r'[^a-z0-9]+', '-', (ch['h'] or '').lower()).strip('-')
        ch['id'] = cid
        if ch['h'] and DIVIDERS.search(ch['h']):
            short = len(rows) == 1 and rows[0][0] == 'txt' and len(rows[0][1]) <= 3
            band = f'<section class="cs-ch cs-divider" id="{cid}"><h2>The full process</h2><p class="cs-sub">Research, decisions and iterations, step by step.</p>{inner if short else ""}</section>'
            html.append(band if (short or not inner) else band + f'<section class="cs-ch no-h">{inner}</section>')
            seen_div = True
            continue
        h = f'<h2>{ch["h"]}</h2>' if ch['h'] else ''
        html.append(f'<section class="cs-ch{"" if ch["h"] else " no-h"}"{f" id={chr(34)}{cid}{chr(34)}" if cid else ""}>{h}{inner}</section>')
    CHAPTERS.clear()
    for c in chs:
        if not c['h']:
            continue
        if DIVIDERS.search(c['h']):
            CHAPTERS.append(('The full process', c['id']))
            break
        CHAPTERS.append((c['h'], c['id']))
    return ''.join(html)


CHAPTERS = []


def meta_html(meta):
    if not meta:
        return ''
    cells = ''
    for k, v in meta:
        parts = [p.strip() for p in re.split(r'<br\s*/?>', v) if txt(p)]
        if len(parts) == 1 and ',' in parts[0] and '<a' not in parts[0]:
            parts = [x.strip() for x in parts[0].split(',') if x.strip()]
        val = ''.join(f'<span>{p}</span>' for p in parts)
        cells += f'<div><dt>{k}</dt><dd>{val}</dd></div>'
    return f'<dl class="cs-meta">{cells}</dl>'


def overview(p):
    sm = SUMMARY.get(p['slug'])
    if not sm:
        return ''
    cols = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in zip(('The challenge', 'My role', 'The outcome'), sm))
    return f'<section class="cs-overview" aria-label="Overview"><dl>{cols}</dl></section>'


OVERRIDE = {
    'illustrations': dict(title='European-inspired illustrations',
                          intro='I create <strong>illustrations and watercolour prints</strong> inspired by the places, colours and little details of <strong>European life</strong>, and sell them in my <strong>Etsy shop</strong>. From Casa Batlló and Park Güell in Barcelona to the Alhambra, Valencia, Menorca and Ibiza.',
                          cta=('Visit the Etsy shop', 'https://www.etsy.com/shop/amespunn')),
}


def case_page(key, p, back, back_label, nxt, nxt_href, kind):
    items = items_of(key)
    title, intro, meta, body = split_hero(items)
    title = title or p['title']
    ov = OVERRIDE.get(p['slug'], {})
    title, intro = ov.get('title', title), ov.get('intro', intro)
    k = ''
    if p.get('kpis') and not p.get('notes'):
        k = '<div class="kpis cs-kpis">' + ''.join(f'<div class="kpi"><strong>{v}</strong>{l}</div>' for v, l in p['kpis']) + '</div>'
    lede = f'<p class="lede">{intro}</p>' if intro else ''
    if ov.get('cta'):
        lede += f'<p><a class="btn primary" href="{ov["cta"][1]}" target="_blank" rel="noopener">{ov["cta"][0]} {EXT}</a></p>'
    cover = f'<figure class="cs-cover" style="view-transition-name:cover-{p["slug"]}">{pic(p["cover"], p.get("alt", ""), "(max-width: 1200px) 100vw, 1200px", eager=True)}</figure>'
    nxt_html = (f'<a class="cs-next" href="{nxt_href}">'
                f'<span class="media">{pic(nxt["cover"], "", "(max-width: 900px) 100vw, 560px")}</span>'
                f'<span class="t"><small>Next {kind}</small><b>{nxt["title"]}</b><span class="more">Open {ARROW}</span></span></a>')
    desc = txt(intro)[:155] if intro else p['title']
    body_html = chapters(body)
    index_html = ''
    if len(CHAPTERS) >= 4:
        index_html = '<nav class="cs-index" aria-label="In this case study"><p>In this case study</p><ol>' + ''.join(f'<li><a href="#{i}">{h}</a></li>' for h, i in CHAPTERS) + '</ol></nav>'
    page = head(f'{title} · Aïda Martínez Espún', desc, '../../') + nav('../../', 'Work' if kind == 'project' else 'Studio')
    page += f'''
<main class="wrap cs" id="main">
  <section class="cs-hero">
    <a class="back" href="{back}">{BACK} {back_label}</a>
    {tags(p["tags"])}
    <h1>{title}</h1>
    {lede}
    {meta_html(meta)}
    {k}
  </section>
  {cover}
  {overview(p)}
  {index_html}
  <article class="cs-body">{body_html}</article>
  <nav class="cs-foot" aria-label="More work">
    {nxt_html}
    <a class="btn" href="{back}">{back_label} {ARROW}</a>
  </nav>
'''
    return page + contact('../../') + foot()


def studio_items():
    return [dict(slug=slug, title=n, tags=[k], cover=SQ + u, alt=n, role=k) for n, k, slug, u in STUDIO]


def localize(html, base):
    def rep(m):
        n = int(m.group(2)) if m.group(2) else 1600
        return best(m.group(1), n)
    html = re.sub(re.escape(SQ) + r'([^"?\s)\']+)(?:\?format=(\d+)w)?', rep, html)
    def link(m):
        p = m.group(1).strip('/')
        if p in ('contact', 'contact-me'): return 'href="#contact"'
        if p.startswith('designstudio'): p = 'studio' + p[len('designstudio'):]
        return f'href="@@/{p}/"' if p else 'href="@@/"'
    html = re.sub(r'href="(?:https?://(?:www\.)?amespun\.com)?(/[^"#]*)"', link, html)
    html = html.replace('etsy.com/shop/amespunprints', 'etsy.com/shop/amespunn')
    def ext(m):
        tag = m.group(0)
        return tag if 'target=' in tag else tag[:-1] + ' target="_blank" rel="noopener">'
    html = re.sub(r'<a\s[^>]*href="https?://(?!amespun\.github\.io|(?:www\.)?amespun\.com)[^"]*"[^>]*>', ext, html)
    return html.replace('@@/', base)


def write(rel, html, base):
    path = f'{ROOT}/{rel}'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(localize(html, base))


write('index.html', home(), '')
write('work/index.html', work(), '../')
write('about/index.html', about(), '../')
write('studio/index.html', studio(), '../')
for i, p in enumerate(PROJECTS):
    nx = PROJECTS[(i + 1) % len(PROJECTS)]
    write(f'work/{p["slug"]}/index.html', case_page('work__' + p['slug'], p, '@@/work/', 'All work', nx, f'@@/work/{nx["slug"]}/', 'project'), '../../')
SI = studio_items()
for i, p in enumerate(SI):
    nx = SI[(i + 1) % len(SI)]
    write(f'studio/{p["slug"]}/index.html', case_page('designstudio__' + p['slug'], p, '@@/studio/', 'All studio work', nx, f'@@/studio/{nx["slug"]}/', 'studio project'), '../../')
print('built')
