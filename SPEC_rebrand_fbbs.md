# Spec: Rebrand homepage-clone as "FBBS Training Academy" + add Contact page

Goal: reuse the existing cloned page structure/layout/CSS/JS/animations as
a template, but replace ALL text content, navigation, footer, and imagery
references with new content for a fictional business, "FBBS Training
Academy" (hair, beauty & wellness education). This is new original content
provided by the site owner — not a clone of the original charity's copy.

Work on TWO deliverables:

## 1. `homepage-clone/index.html` — rewrite in place

Keep the existing DOM/CSS/JS structure, classes, animations, and layout
sections (hero, card grids, icon-list sections, testimonial slider, CTA
banner, etc.) exactly as-is — only replace the text content, headings,
links, and nav items inside them. Where a section requires an image and no
new image is supplied, keep the existing placeholder image in that slot
(don't break the layout by removing `<img>` tags).

Replace content as follows:

**Site name / branding:** FBBS Training Academy
**Tagline:** Professional Hair, Beauty & Wellness Education
**Hero heading:** Advance Your Career in Hair, Beauty & Wellness

**Main navigation** (replace all existing nav items with, in order):
Home, About, Courses, CPD, One-to-One Training, Open Days, Gallery, FAQs,
Contact, and a gold "Book Online" button/CTA.

**Footer navigation** (replace all existing footer links with):
About FBBS, Hair Courses, Beauty Courses, Professional Development, CPD,
One-to-One Training, Open Days, Student Support, Gallery, Contact, Privacy
Policy, Terms & Conditions, Cookies Policy.

**Footer contact block:**
- FBBS Training Academy
- Phone: 07951 261087
- Email: info@funmibraidsgroup.com
- Website: www.fbbstrainingacademy.com
- By Appointment Only

**Intro/welcome section:**
Heading "Welcome to FBBS Training Academy" followed by two paragraphs:
"FBBS Training Academy provides industry-led education for aspiring and
established professionals in the hair, beauty and wellness industries."
and "Through practical training, Continuing Professional Development (CPD)
and personalised learning, we help individuals develop technical
excellence, build professional confidence and progress their careers."

**"Our Training" section** — four cards, each with heading, one-line
description, and a CTA link, replacing whatever the current card-grid
section contains:
1. Hair Academy — "Professional practical training for aspiring and
   experienced hair professionals." — CTA "View Hair Courses"
2. Beauty Academy — "Professional beauty education focused on practical
   skills and industry standards." — CTA "View Beauty Courses"
3. Professional Development — "Develop your career with business,
   professional practice and employability training." — CTA "Explore
   Professional Development"
4. One-to-One Training — "Receive personalised coaching tailored to your
   individual learning goals." — CTA "Book a Tutorial"

**"Why Choose FBBS?" section** — checklist/icon-list with these items:
Industry-Led Education, Experienced Educators, Practical Learning, Small
Group Training, One-to-One Support, Flexible Learning.

**"Featured Training" section**, grouped under three sub-headings:
- Hair: "Precision Cornrows & Advanced Braiding", "Blow-Drying &
  Professional Styling", "Editorial, Session & Runway Hair Styling"
- Beauty: "Professional Makeup Instruction", "Colour Theory for Diverse
  Skin Tones"
- Professional Development: "Business & Career Development"
Followed by a "View All Courses" CTA link.

**"Who We Support" section** — checklist/icon-list with: College Students,
Newly Qualified Professionals, Salon Professionals, Career Changers,
Professionals Returning to the Industry, Future Salon Owners.

**Testimonials section** — keep the existing testimonial-slider markup
structure but replace copy with 3 short generic placeholder learner
quotes (write natural short quotes about training experience/confidence
gained) with placeholder names; keep existing placeholder photos.

**Booking CTA banner** near the bottom:
Heading "Book an Appointment", subhead "Not sure where to begin?", body
"Book a personal appointment to discuss your learning goals and discover
the training that's right for you.", button "Book Now".

**All calls-to-action site-wide**: wherever the current copy has a CTA
button/link, use one of: "Book an Appointment", "View Courses", "Book a
One-to-One Tutorial", "Book an Open Day", "Enquire Today", "Start Your
Professional Journey", "Speak to an Educator" — pick whichever fits the
section contextually.

Update `<title>`, meta description, and any Open Graph/meta tags containing
the old charity name/description to match the new branding.

## 2. New `contact-clone/` page

Create a new folder `contact-clone/` reusing the same header, footer, nav,
CSS, JS and asset references as `homepage-clone/` (copy/reference the same
`assets/` — reuse `homepage-clone/assets/` via relative paths, don't
re-download). Build `contact-clone/index.html` with:

**Heading:** Contact FBBS Training Academy
**Intro:** "We'd love to hear from you. Whether you're interested in our
courses, one-to-one training or CPD opportunities, we're here to help."

**Contact details block:**
- Telephone: 07951 261087
- Email: info@funmibraidsgroup.com
- Appointments: By appointment only.
- Opening Hours: Monday to Friday, 9:00 am to 6:00 pm

**Enquiry form** (plain HTML form, no backend — just render the fields,
`action`/`onsubmit` can be a no-op placeholder):
- First Name (text)
- Last Name (text)
- Telephone (tel)
- Email (email)
- "I'm interested in:" (select/dropdown) with options: Hair Training,
  Beauty Training, Professional Development, One-to-One Training, CPD,
  Open Day
- Message (textarea)
- Submit button labeled "Send Enquiry"

Style the form and page to match the visual language (fonts, colors,
spacing, buttons) already established in homepage-clone's CSS — reuse
existing form/input styling classes from the site's CSS if present,
otherwise add minimal consistent CSS.

Add `contact-clone/README.md` (one-line local view instruction) and an
`npm run start:contact` script in the root `package.json` serving
`contact-clone` on port 4175. Don't touch the existing `start` /
`start:wellbeing` scripts.

## Out of scope

- Do not modify `wellbeing-support-clone/` at all.
- Do not remove or break any existing animations, sliders, or JS behavior
  — only change the text/content/links inside the existing structure.
- Do not create git commits.
