# Version C of the home page: A's calm style and structure, plus B's strongest moments
# (positioning, count-up numbers, What I bring). Hidden: noindex, not linked, not in the sitemap.
def home_c():
    base = '../'
    bring = [('UX strategy', 'Aligning product, engineering and design on what to build and why. Depending on the company, support, customer success, sales, marketing and growth too.'),
             ('Design systems', 'Starting design systems from scratch, scaling them and helping them grow, with engineers and every stakeholder on board, and pushing for adoption.'),
             ('Product discovery', 'Qualitative and quantitative interviews, prototypes and usability tests on Lyssna before a single sprint is spent.'),
             ('Growth & data', 'Everything is tracked, so every decision goes with its data. I analyse the numbers before and after each change.'),
             ('Leadership', 'Mentoring designers and raising UX maturity across teams.')]
    stats = [('−39.8%', 'Support tickets', 'EV charging dashboard for property managers, EVPassport.'),
             ('+46.6%', 'Engagement', 'App-free EV charging across iOS, Android and App Clip.'),
             ('7→3 min', 'Onboarding', 'Teampact retrospectives that teams actually finish, Haufe Group.'),
             ('10+', 'Years in product', 'Startups and scale-ups, from Barcelona to the Netherlands.')]
    beyond = ''.join(
        f'<li><b>{t}</b><p>{d}</p>' + (f'<a class="ext-link" href="{l[1] if l[1].startswith("http") else base + l[1]}">{l[0]} {EXT if l[1].startswith("http") else ARROW}</a>' if l else '') + '</li>' for t, d, l in BEYOND)
    page = head('Aïda Martínez Espún · Senior Product Designer (version C)', 'Proposal C for the home page.', base).replace(
        '<meta name="theme-color" content="#ffffff">', '<meta name="theme-color" content="#ffffff">\n<meta name="robots" content="noindex, nofollow">').replace(
        '</head>', f'<link rel="stylesheet" href="{base}assets/c.css?v={C_V}">\n</head>').replace('<body>', '<body class="c">')
    page += nav(base, None) + f'''
<main class="wrap" id="main">
  <section class="hero c-hero">
    <div>
      <p class="c-eyebrow">Aïda Martínez Espún · Senior Product Designer</p>
      <h1><span>From complex</span> <span>to simple.</span></h1>
      <p class="lede">10+ years designing B2B and B2C products across SaaS, marketplaces and green tech. Companies bring me their most complex products. I make them simple for the people who use them, and prove it with data.</p>
      <div class="hero-actions">
        <a class="btn primary" href="#work">View selected work {ARROW_DOWN}</a>
        <button class="btn secondary" type="button" data-copy>{COPY_ICON}{labels("Copy email")}</button>
      </div>
    </div>
    <div class="art">{pic(DEVICES, "Product screens from recent projects", "(max-width: 900px) 100vw, 520px", eager=True, w=1500, h=1060)}</div>
  </section>
  <div class="worked"><p>Worked with</p><ul class="logos" aria-label="Companies I’ve worked with">{''.join(f'<li class="{k}"><img src="{logo_src(u)}" alt="{n}" loading="lazy" decoding="async"></li>' for n, u, k in LOGOS)}</ul></div>

  <section class="section c-stats" aria-labelledby="c-stats-h">
    <h2 class="h2" id="c-stats-h">Behind every number is a design decision.</h2>
    <p class="c-sub">Here’s what my work changed.</p>
    <dl>{''.join(f'<div><dt data-count>{v}</dt><dd><b>{t}</b><span>{d}</span></dd></div>' for v, t, d in stats)}</dl>
  </section>

  <section class="section" id="work">
    <div class="section-head"><h2>Selected work</h2><a class="more-link" href="{base}work/">All {len(PROJECTS)} projects {ARROW}</a></div>
    <div class="grid featured">{card(FEATURED[0], lead=True)}{card(FEATURED[1], lead=True)}</div>
    {more_work(base)}
  </section>

  <section class="c-bring" aria-labelledby="c-bring-h">
  <div class="in">
    <div class="left">
      <h2 class="h2" id="c-bring-h">What I bring</h2>
      <p data-bring-text aria-live="polite">{bring[0][1]}</p>
    </div>
    <ol class="words">{''.join(f'<li{" class=on" if i == 0 else ""} data-text="{d}"><button type="button" aria-pressed="{"true" if i == 0 else "false"}"><span>{w}</span><sup>{i + 1:02d}</sup></button></li>' for i, (w, d) in enumerate(bring))}</ol>
  </div>
</section>

  <section class="section about-home" id="about">
    {collage()}
    <div class="about-copy">
      <h2 class="h2">Hi, I’m Aïda.</h2>
      <p>I spent ten years in Barcelona designing B2B and B2C products for Spanish startups and for US, German and UK companies with teams there. Now I’m in the Netherlands. I like the messy part: getting product, engineering and the business aligned on what to build, then proving it with research and numbers.</p>
      {facts()}
      {quote_html(QUOTES[0])}
      <a class="more-link" href="{base}about/">More about me {ARROW}</a>
    </div>
  </section>

  <section class="section beyond" id="beyond">
    <div class="intro"><h2 class="h2">Beyond the day job</h2><p>What I design when nobody asks me to.</p></div>
    <ul>{beyond}</ul>
  </section>
''' + contact(base) + foot().replace('</script>', C_JS + '</script>', 1)
    return page
