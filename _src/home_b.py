# Version B of the home page (A/B proposal, inspired by LABB Creative Studio). Hidden: noindex, not linked, not in the sitemap.
def home_b():
    base = '../'
    def card_b(p, cls):
        tg = ''.join(f'<span>{t}</span>' for t in p['tags'][:2])
        k = ''.join(f'<li><b>{v}</b> {l}</li>' for v, l in p.get('kpis', [])[:2]) if not p.get('notes') else ''
        return f'''<a class="pj {cls}" href="{base}work/{p["slug"]}/">
      <span class="media">{pic(p["cover"], p["alt"], "(max-width: 900px) 100vw, 700px")}</span>
      <span class="t"><b>{p["who"]}</b><span class="d">{p["title"]}</span>{f'<ul class="k">{k}</ul>' if k else ''}<span class="pills">{tg}</span></span>
    </a>'''
    projects = [FEATURED[0], FEATURED[1], FEATURED[2], EARLIER[0], FEATURED[3]]
    layout = ['p1', 'p2', 'p3', 'p4', 'p5']
    bring = [('UX strategy', 'Aligning product, engineering and sales on what to build, and why.'),
             ('Design systems', 'Foundations, components and documentation that teams actually use.'),
             ('Product discovery', 'Interviews, prototypes and testing before a single sprint is spent.'),
             ('Growth & data', 'Experiments and metrics that prove the design worked.'),
             ('Leadership', 'Mentoring designers and raising UX maturity across teams.')]
    stats = [('−39.8%', 'Support tickets', 'EV charging dashboard for property managers, EVPassport.'),
             ('+46.6%', 'Engagement', 'App-free EV charging across iOS, Android and App Clip.'),
             ('7→3 min', 'Onboarding', 'Teampact retrospectives that teams actually finish, Haufe Group.'),
             ('10+', 'Years in product', 'Startups and scale-ups, from Barcelona to the Netherlands.')]
    steps = [('Discover', 'Interviews, data and competitor research to find the real problem, not the loudest one.'),
             ('Align', 'Product, engineering and sales agree on what we build and how we measure it.'),
             ('Design & test', 'Prototypes in Figma, tested with users and refined in short iterations.'),
             ('Ship & measure', 'Hand-off through the design system, then tracking the numbers after launch.')]
    q = QUOTES[1]
    nav_html = nav(base, None).replace('class="topbar" data-island', 'class="topbar b-top" data-island')
    page = head('Aïda Martínez Espún · Senior Product Designer (version B)', 'Proposal B for the home page.', base).replace(
        '<meta name="theme-color" content="#ffffff">', '<meta name="theme-color" content="#ffffff">\n<meta name="robots" content="noindex, nofollow">').replace(
        '</head>', f'<link rel="stylesheet" href="{base}assets/b.css?v={B_V}">\n</head>').replace('<body>', '<body class="b">')
    page += nav_html + f'''
<section class="b-hero" aria-labelledby="b-h1">
  {pic(FEATURED[0]["cover"], "", "100vw", eager=True)}
  <div class="b-wrap">
    <h1 id="b-h1"><span class="l1">Product</span><span class="l2">designer</span><span class="l3">Aïda Martínez Espún</span></h1>
    <p class="b-sub">Senior Product Designer for B2B and B2C SaaS, marketplaces and green tech. Based in the Netherlands.</p>
    <button class="b-pill" type="button" data-copy>{COPY_ICON}{labels("Copy email")}</button>
  </div>
</section>
<main id="main">
  <section class="b-wrap b-stats">
    <a class="b-link" href="#contact">↳ Let’s talk</a>
    <h2>Behind every number is a design decision. Here’s what my work changed.</h2>
    <dl>{''.join(f'<div><dt data-count>{v}</dt><dd><b>{t}</b><span>{d}</span></dd></div>' for v, t, d in stats)}</dl>
  </section>

  <section class="b-big" aria-label="From complex to simple">
    <p><span>From complex</span><span>to simple.</span></p>
  </section>

  <section class="b-logos" aria-label="Companies I’ve worked with">
    <ul>{''.join(f'<li class="{k}"><img src="{logo_src(u)}" alt="{n}" loading="lazy" decoding="async"></li>' for n, u, k in LOGOS)}</ul>
  </section>

  <section class="b-wrap b-work" id="work">
    <h2>From research to results</h2>
    <div class="b-grid">{''.join(card_b(p, c) for p, c in zip(projects, layout))}</div>
    <a class="b-all" href="{base}work/">{ARROW}<span>All projects</span><sup>({len(PROJECTS)})</sup></a>
  </section>

  <section class="b-bring" aria-labelledby="b-bring-h">
    <div class="b-wrap">
      <div class="left">
        <h2 id="b-bring-h">What I bring</h2>
        <span class="ph">{pic(PHOTOS["portrait"], "Aïda Martínez Espún", "(max-width: 900px) 60vw, 280px")}</span>
        <p data-bring-text>{bring[0][1]}</p>
      </div>
      <ol class="words">{''.join(f'<li{" class=on" if i == 0 else ""} data-text="{d}"><span>{w}</span><sup>({i + 1:02d})</sup></li>' for i, (w, d) in enumerate(bring))}</ol>
      <a class="b-link" href="#contact">↳ Let’s work together</a>
    </div>
  </section>

  <section class="b-wrap b-quote">
    <span class="ph">{pic(PHOTOS["smile"], "", "(max-width: 900px) 50vw, 260px")}</span>
    <blockquote><p>“{q[0]}”</p><footer><b>{q[1]}</b><span>{q[2]}</span></footer></blockquote>
  </section>

  <section class="b-wrap b-process">
    <div class="left">
      <h2>How I work</h2>
      <p>From the first interview to the numbers after launch, product, engineering and business stay in the loop.</p>
      <a class="b-link" href="{base}about/">↳ More about me</a>
    </div>
    <ol>{''.join(f'<li><span class="n">{i + 1:02d}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps))}</ol>
  </section>
''' + contact(base) + foot().replace('</script>', B_JS + '</script>', 1)
    return page
