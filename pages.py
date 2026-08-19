#!/usr/bin/env python3
from build import page_shell, write, BASE_URL, EMAIL, GITHUB, LINKEDIN

# Decorative hero graphic — a benchmark/survey-mark motif tying the
# visual language to the Digital Land Records project. Purely
# decorative, so it is hidden from assistive tech and carries no alt text.
HERO_GRAPHIC = """        <svg class="hero-graphic" viewBox="0 0 200 200" width="160" height="160" aria-hidden="true" focusable="false">
          <circle cx="100" cy="100" r="70" fill="none" stroke="#1D4E89" stroke-width="1.5" opacity="0.5"/>
          <circle cx="100" cy="100" r="40" fill="none" stroke="#9C5B1D" stroke-width="1.5" opacity="0.6"/>
          <line x1="100" y1="10" x2="100" y2="190" stroke="#1C2321" stroke-width="1" opacity="0.35"/>
          <line x1="10" y1="100" x2="190" y2="100" stroke="#1C2321" stroke-width="1" opacity="0.35"/>
          <circle cx="100" cy="100" r="4" fill="#1D4E89"/>
        </svg>"""

# ---------------------------------------------------------------
# HOME
# ---------------------------------------------------------------
person_jsonld = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Pooja N",
    "jobTitle": "Information Science and Engineering Student",
    "description": "Information Science and Engineering student and aspiring full-stack developer based in Bengaluru, India.",
    "url": "{BASE_URL}/",
    "email": "mailto:{EMAIL}",
    "sameAs": ["{GITHUB}", "{LINKEDIN}"],
    "alumniOf": {{
      "@type": "CollegeOrUniversity",
      "name": "Sai Vidya Institute of Technology, Bengaluru"
    }}
  }}
  </script>
"""

home_main = f"""    <section class="hero">
      <div class="wrap hero-flex">
        <div class="hero-copy">
          <span class="hero-eyebrow">Portfolio &middot; Bengaluru, India</span>
          <h1>Pooja N</h1>
          <p class="hero-lede">Information Science &amp; Engineering student and aspiring Full-Stack Developer.
          Passionate about learning, building, and exploring technology.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="projects.html">View projects</a>
            <a class="btn btn-secondary" href="contact.html">Get in touch</a>
          </div>
        </div>
        <div class="hero-graphic-wrap">
{HERO_GRAPHIC}
        </div>
      </div>
    </section>

    <section aria-labelledby="quick-facts-heading">
      <div class="wrap">
        <div class="section-head">
          <span class="section-tag">Record summary</span>
          <h2 id="quick-facts-heading">Quick facts</h2>
        </div>
        <div class="grid grid-3">
          <div class="record-card">
            <h3>Education</h3>
            <p>B.E. in Information Science and Engineering, Sai Vidya Institute of Technology, Bengaluru. Expected graduation 2028. CGPA 8.7.</p>
          </div>
          <div class="record-card">
            <h3>Focus areas</h3>
            <p>Full-stack web development, with growing interest in generative AI and prompt engineering.</p>
          </div>
          <div class="record-card">
            <h3>Based in</h3>
            <p>Bengaluru, Karnataka, India.</p>
          </div>
        </div>
      </div>
    </section>

    <section aria-labelledby="featured-projects-heading">
      <div class="wrap">
        <div class="section-head">
          <span class="section-tag">Selected work</span>
          <h2 id="featured-projects-heading">Featured projects</h2>
        </div>
        <div class="grid grid-2">
          <article class="record-card">
            <h3><a href="projects.html#digital-land-records">Digital Land Records Management System</a></h3>
            <p>A web-based system to digitize and simplify land record management, reducing manual paperwork
            and making land-related information more organized and accessible.</p>
            <p><a href="{GITHUB}/BhuLekh">View repository on GitHub</a></p>
          </article>
          <article class="record-card">
            <h3><a href="projects.html#village-health-access">Village Health Access</a></h3>
            <p>A platform that helps people in rural and underserved communities find nearby healthcare
            facilities and connect with available medical resources.</p>
            <p><a href="{GITHUB}/village-health-access">View repository on GitHub</a></p>
          </article>
        </div>
        <p class="link-more"><a href="projects.html">See all projects &rarr;</a></p>
      </div>
    </section>

    <section aria-labelledby="cta-heading">
      <div class="wrap">
        <div class="section-head">
          <h2 id="cta-heading">Let&rsquo;s work together</h2>
          <p>Open to internships, hackathons, and collaborative projects in full-stack development.</p>
        </div>
        <a class="btn btn-primary" href="contact.html">Contact me</a>
      </div>
    </section>
"""

write("index.html", page_shell(
    "index.html",
    "Pooja N | Information Science &amp; Engineering Student, Aspiring Full-Stack Developer",
    "Portfolio of Pooja N, an Information Science and Engineering student at Sai Vidya Institute of Technology, Bengaluru, and aspiring full-stack developer.",
    "/",
    home_main,
    extra_jsonld=person_jsonld,
))

# ---------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------
about_main = """    <section aria-labelledby="page-title">
      <div class="wrap">
        <span class="section-tag">Profile</span>
        <h1 id="page-title">About</h1>
        <p class="hero-lede">I&rsquo;m a third-year Information Science &amp; Engineering student at Sai Vidya
        Institute of Technology, Bengaluru, with a growing interest in full-stack web development. I enjoy
        learning new technologies, building projects, and exploring how technology can be used to solve
        real-world problems.</p>
        <p class="hero-lede">I&rsquo;m currently developing my skills in web development and continuously
        learning through hands-on projects and experimentation. I&rsquo;m always looking for opportunities to
        learn, improve my technical skills, and grow as I continue my journey in technology.</p>
      </div>
    </section>

    <section aria-labelledby="education-heading">
      <div class="wrap">
        <div class="section-head">
          <span class="section-tag">Record entry</span>
          <h2 id="education-heading">Education</h2>
        </div>
        <div class="record-card">
          <h3>Bachelor of Engineering (B.E.), Information Science and Engineering</h3>
          <p>Sai Vidya Institute of Technology, Bengaluru</p>
          <ul class="tag-list">
            <li class="record-label">Expected graduation: 2028</li>
            <li class="record-label">CGPA: 8.7</li>
          </ul>
        </div>
      </div>
    </section>

    <section aria-labelledby="certifications-heading">
      <div class="wrap">
        <div class="section-head">
          <span class="section-tag">Record entry</span>
          <h2 id="certifications-heading">Certifications</h2>
        </div>
        <ul class="grid grid-2 card-list">
          <li class="record-card">
            <h3>Fundamentals of Generative AI</h3>
            <p>AWS</p>
          </li>
          <li class="record-card">
            <h3>Generative AI Mastermind</h3>
            <p>OutSkill</p>
          </li>
        </ul>
      </div>
    </section>

    <section aria-labelledby="experience-heading">
      <div class="wrap">
        <div class="section-head">
          <span class="section-tag">Record entry</span>
          <h2 id="experience-heading">Experience &amp; activities</h2>
          <p>A running log of clubs, hackathons, internships, and workshops. Entries are added as they
          are confirmed.</p>
        </div>
        <ul class="timeline">
          <li>
            <h3>AI Club / AIGNITE</h3>
            <p class="placeholder-note">Active member of the college AI club, participating in AI-focused workshops, discussions, and collaborative learning sessions.</p>
          </li>
          <li>
            <h3>Hackathons</h3>
            <p class="placeholder-note">Participated in college-level hackathons, building rapid prototypes and collaborating with cross-functional teams.</p>
          </li>
          <li>
            <h3>Internships</h3>
            <p class="placeholder-note">Seeking internship opportunities in web development and full-stack engineering.</p>
          </li>
          <li>
            <h3>Technical events &amp; workshops</h3>
            <p class="placeholder-note">Active participant in technical events and workshops, exploring emerging technologies and expanding practical knowledge. Engaging in hands-on learning sessions to develop technical skills and stay updated with industry trends.</p>
          </li>
        </ul>
      </div>
    </section>
"""

write("about.html", page_shell(
    "about.html",
    "About | Pooja N",
    "About Pooja N: education at Sai Vidya Institute of Technology, certifications, and ongoing activities.",
    "/about.html",
    about_main,
))

# ---------------------------------------------------------------
# SKILLS
# ---------------------------------------------------------------
def skill_group(tag, title, skills):
    items = "\n".join(f"          <li>{s}</li>" for s in skills)
    return f"""      <div class="record-card skill-group">
        <h3>{title}</h3>
        <ul>
{items}
        </ul>
      </div>"""

skills_groups = "\n".join([
    skill_group("frontend", "Frontend", ["HTML5", "CSS3", "JavaScript"]),
    skill_group("backend", "Backend", ["Node.js", "Express.js"]),
    skill_group("databases", "Databases", ["MongoDB", "SQLite"]),
    skill_group("languages", "Programming languages", ["Java", "C", "JavaScript"]),
    skill_group("tools", "Tools", ["Git", "GitHub", "VS Code"]),
    skill_group("additional", "Additional", ["Generative AI", "Prompt Engineering"]),
])

skills_main = f"""    <section aria-labelledby="page-title">
      <div class="wrap">
        <span class="section-tag">Skill set</span>
        <h1 id="page-title">Skills</h1>
        <p class="hero-lede">Technologies I use and am currently building with. Grouped by area,
        matching the tools used in my current projects.</p>
      </div>
    </section>

    <section aria-labelledby="skills-heading">
      <div class="wrap">
        <h2 id="skills-heading" class="visually-hidden">Skill categories</h2>
        <div class="grid grid-3">
{skills_groups}
        </div>
      </div>
    </section>
"""

write("skills.html", page_shell(
    "skills.html",
    "Skills | Pooja N",
    "Technical skills of Pooja N across frontend, backend, databases, programming languages, and tools.",
    "/skills.html",
    skills_main,
))

# ---------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------
def project_article(anchor, name, description, tech, repo_url):
    tags = "\n".join(f'            <li class="record-label">{t}</li>' for t in tech)
    return f"""      <article class="record-card" id="{anchor}">
        <h2>{name}</h2>
        <p>{description}</p>
        <ul class="tag-list">
{tags}
        </ul>
        <p><a href="{repo_url}">View on GitHub<span class="visually-hidden"> &mdash; {name}</span></a></p>
      </article>"""

projects_main = f"""    <section aria-labelledby="page-title">
      <div class="wrap">
        <span class="section-tag">Registry</span>
        <h1 id="page-title">Projects</h1>
        <p class="hero-lede">Two web applications built to digitize manual, paper-based workflows.</p>
      </div>
    </section>

    <section aria-labelledby="projects-heading">
      <div class="wrap">
        <h2 id="projects-heading" class="visually-hidden">Project list</h2>
        <div class="grid grid-2">
{project_article(
    "digital-land-records",
    "Digital Land Records Management System",
    "A web-based system designed to digitize and simplify land record management, allowing users to "
    "securely store, access, and manage land-related information. It helps reduce manual paperwork and "
    "makes land records more organized, accessible, and efficient.",
    ["HTML", "CSS", "JavaScript", "Node.js", "Express.js", "SQLite", "Git &amp; GitHub"],
    f"{GITHUB}/BhuLekh",
)}
{project_article(
    "village-health-access",
    "Village Health Access",
    "A web-based platform designed to improve access to healthcare information and services for people "
    "in rural and underserved communities. It helps users find nearby healthcare facilities, access "
    "essential health information, and connect with available medical resources.",
    ["HTML", "CSS", "JavaScript", "Node.js", "Express.js", "MongoDB", "Git &amp; GitHub"],
    f"{GITHUB}/village-health-access",
)}
        </div>
      </div>
    </section>
"""

write("projects.html", page_shell(
    "projects.html",
    "Projects | Pooja N",
    "Web development projects by Pooja N, including a Digital Land Records Management System and Village Health Access.",
    "/projects.html",
    projects_main,
))

# ---------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------
contact_main = f"""    <section aria-labelledby="page-title">
      <div class="wrap">
        <span class="section-tag">Get in touch</span>
        <h1 id="page-title">Contact</h1>
        <p class="hero-lede">Reach out directly or use the form below &mdash; both go to the same inbox.</p>
      </div>
    </section>

    <section aria-labelledby="contact-details-heading">
      <div class="wrap grid grid-2">
        <div>
          <h2 id="contact-details-heading">Direct contact</h2>
          <address class="contact-list">
            <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
            <p><strong>GitHub:</strong> <a href="{GITHUB}">{GITHUB.replace('https://', '')}</a></p>
            <p><strong>LinkedIn:</strong> <a href="{LINKEDIN}">linkedin.com/in/pooja-n</a></p>
          </address>
        </div>

        <div>
          <h2 id="contact-form-heading">Send a message</h2>

          <div id="form-status" class="form-status" aria-live="polite"></div>

          <form id="contact-form" novalidate aria-labelledby="contact-form-heading">
            <div class="field">
              <label for="name">Full name <span class="required-mark" aria-hidden="true">*</span></label>
              <input
                type="text"
                id="name"
                name="name"
                autocomplete="name"
                required
                aria-required="true"
                aria-describedby="name-error"
                aria-invalid="false"
              />
              <p class="field-error" id="name-error" role="alert"></p>
            </div>

            <div class="field">
              <label for="email">Email address <span class="required-mark" aria-hidden="true">*</span></label>
              <input
                type="email"
                id="email"
                name="email"
                autocomplete="email"
                required
                aria-required="true"
                aria-describedby="email-hint email-error"
                aria-invalid="false"
              />
              <p class="field-hint" id="email-hint">We&rsquo;ll only use this to reply to you.</p>
              <p class="field-error" id="email-error" role="alert"></p>
            </div>

            <div class="field">
              <label for="subject">Subject <span class="required-mark" aria-hidden="true">*</span></label>
              <input
                type="text"
                id="subject"
                name="subject"
                autocomplete="off"
                required
                aria-required="true"
                aria-describedby="subject-error"
                aria-invalid="false"
              />
              <p class="field-error" id="subject-error" role="alert"></p>
            </div>

            <div class="field">
              <label for="message">Message <span class="required-mark" aria-hidden="true">*</span></label>
              <textarea
                id="message"
                name="message"
                rows="6"
                required
                aria-required="true"
                aria-describedby="message-error"
                aria-invalid="false"
              ></textarea>
              <p class="field-error" id="message-error" role="alert"></p>
            </div>

            <button type="submit" class="btn btn-primary">Send message</button>
          </form>
        </div>
      </div>
    </section>
"""

write("contact.html", page_shell(
    "contact.html",
    "Contact | Pooja N",
    "Get in touch with Pooja N by email, GitHub, LinkedIn, or the contact form.",
    "/contact.html",
    contact_main,
))

print("Done.")
