# Wechi Elementor Rebuild - Full Conversation Handoff

Date: 2026-07-06

This file is a fuller handoff/export for a colleague. It combines the project context, important conversation decisions, current staging state, mistakes/risks, and detailed Elementor rebuild instructions.

The temporary WordPress password from the chat is intentionally not included. Share credentials separately through a secure channel.

## 1. Original Request

Recreate the existing website `https://wechi.info/` in WordPress Elementor as closely as possible.

The user’s important requirements:

- Work only on the staging site.
- Do not touch the live website.
- Build the full one-page website.
- Use Elementor containers/flexbox, not old sections/columns where possible.
- Use Elementor settings and widgets wherever possible.
- Set up global colors, fonts, button styles, and layout first.
- Recreate header, footer, floating contact button, newsletter popup, and full page.
- Match spacing, typography, colors, images, buttons, backgrounds, and responsive behavior.
- Use uploaded/downloaded assets where available.
- Use Elementor Form for the form.
- Use Elementor Pro popup functionality for the newsletter popup.
- Do not install plugins without asking first.
- Add custom CSS only if Elementor cannot recreate the design accurately.
- The goal is not to redesign or improve the website.

## 2. URLs

Original live website:

- https://wechi.info/

Staging site:

- https://demo-wechi.snelleweb.com/v1/

Staging admin:

- https://demo-wechi.snelleweb.com/v1/wp-admin

Username shared:

- `snelleweb`

Password:

- Not included in this handoff.

## 3. Local Reference Materials

Screenshots, treated as visual source of truth:

- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/website-screenshots/Wechi-Management-Company-desktop.png`
- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/website-screenshots/Wechi-Management-Company-tablet.png`
- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/website-screenshots/Wechi-Management-Company-mobile.png`

Downloaded original HTML:

- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/Website downloaded html/Wechi Management Company.html`

Downloaded original assets:

- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/Website downloaded html/Wechi Management Company_files`

Important transparent logo files generated during the work:

- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/logo_horizontaal_modified_transparent.png`
- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/logo_horizontaal_modified_transparent_header.png`
- `/Users/rich/Documents/GitHub/demo-apps/Wechi-instructions/logo_wechi_transparent.png`

Important warning:

- The downloaded file `logo_horizontaal_modified_1x.png` has a black rectangular background baked into it. Do not use it directly on the white header.

## 4. What Happened In The Conversation

The initial goal was to analyze and rebuild the site in Elementor.

Staging setup actions discussed/performed:

- Logged into the staging WordPress site.
- Changed permalink settings.
- Set the page as the homepage.
- Created/edited the one-page website page.
- Added a floating contact/offering button request:
  - WhatsApp
  - Chat
  - Email
  - Newsletter/updates popup
- Created an Elementor Pro newsletter popup.
- Tried to correct the header logo.
- Tried to fix full-width gaps.

Major issue:

- The page was built largely inside an Elementor HTML widget. This is not acceptable for the final Elementor deliverable because it makes the page hard to edit and forces layout fixes into CSS instead of Elementor controls.

User feedback:

- The user noticed the wrong black-background logo.
- The user noticed left/right white gaps instead of full-width layout.
- The user objected strongly to using so much CSS.
- The user later objected strongly to the page being built in an HTML widget and asked why Elementor was being used at all.

Correct conclusion:

- The current HTML-widget approach should not be polished as the final build.
- The page should be rebuilt properly using real Elementor containers and widgets.

## 5. Current WordPress/Elementor State Mentioned

These items were mentioned during the work and should be verified directly in WordPress:

- Page ID: `17`
- Page title: `Wechi Management Company`
- Page set as static homepage
- Permalinks set to Post Name
- Elementor page currently contains large HTML widget(s)
- Main HTML widget previously mentioned:
  - Widget ID: `65ef7d4`
  - Contains most of the page structure
- Elementor Pro popup:
  - Popup post ID: `44`
  - Title: `Wechi Newsletter Popup`
  - Slug: `wechi-newsletter-popup`

Because the staging site became intermittently unreachable, verify these directly before continuing.

## 6. Staging Availability Issue

The staging site intermittently timed out.

Observed error:

- `This site can’t be reached`
- `demo-wechi.snelleweb.com took too long to respond`
- `ERR_CONNECTION_TIMED_OUT`

Before rebuilding, confirm:

- Frontend loads.
- `/wp-admin` loads.
- Elementor editor loads.
- Update/publish works.
- The site is not blocked by firewall, rate limiting, verification, or hosting timeout.

## 7. Required Direction From Here

Do not continue improving the giant HTML widget as the final version.

Recommended approach:

1. Keep/duplicate the current staging page as a backup if useful.
2. Create a clean Elementor version using containers and real widgets.
3. Use Elementor global styles.
4. Rebuild the one-page site section by section.
5. Use minimal custom CSS only where Elementor cannot match the original.
6. Remove or replace the HTML-widget version only after the real Elementor version is complete and checked.

## 8. Global Elementor Setup

Global colors:

- Primary brown: `#6F4E37`
- Button/form brown token: `#6A5C3B`
- Black/nav: `#000000`
- Dark heading: `#2F3033`
- Body text gray: `#777777`
- Light gray text: `#9A9A9A`
- White: `#FFFFFF`
- Footer dark gray: `#555555`
- Accent blue/cyan, team eyebrow: `#00AEEF`
- Social colors:
  - Facebook `#1877F2`
  - Instagram `#C13584`
  - WhatsApp `#25D366`

Global font:

- Font family: Open Sans
- Body: 15-16px, weight 300/400, line-height 1.7
- Small eyebrow labels: 12-13px, uppercase, weight 700, letter spacing about 0.5px
- Section headings desktop: 42-46px, weight 700/800, uppercase, line-height 1.2
- Mobile section headings: 38-48px depending section, uppercase, line-height 1.15
- Card titles: 22-24px desktop, 30px mobile, weight 800, uppercase
- Navigation: 12px, uppercase, weight 700
- Buttons: 13-16px desktop, 28-30px mobile hero/contact CTA, uppercase where shown, weight 700/800

Page/container width:

- Full-width sections for header/nav/hero/stats/team/video/map/footer
- Inner content max width: 1140px desktop
- Tablet inner width: 82-86%
- Mobile inner width: 86-92%

Buttons:

- Background: `#6F4E37`
- Text: white
- Border: none
- Border radius: 999px for main CTA pills
- Height desktop: 42-52px
- Height mobile: 76-92px for large CTA buttons
- Padding desktop: 16px 38px
- Padding mobile: 20px 34px
- No visible shadow

Spacing rules:

- Most white sections: 80-110px top/bottom desktop
- Tablet: 70-95px
- Mobile: 70-110px, with very large vertical gaps around Projects and Team
- Decorative heading divider: brown horizontal bar, about 55-75px wide, 7-9px high

Border radius/shadows:

- Images: square corners, no radius
- Cards: no visible card box, no border, no shadow
- Social icons: circular pale gray backgrounds, 52-64px mobile

## 9. Detailed Page Structure

### A. Top Contact Header

Container:

- Full-width white section
- Inner horizontal container, max 1140px desktop
- 5 columns: logo, call, address, email, social icons

Desktop:

- Height about 115-120px
- Logo left, about 180px wide
- Contact columns divided by thin vertical lines
- Icons above labels, gray/brown tone

Tablet:

- Same contact row remains visible
- Logo about 180-210px
- Columns narrower

Mobile:

- Stack vertically
- Logo large, nearly full width
- Center all text
- Order: logo, Call Us, Address, Email Us, social icons
- Padding top/bottom around 38-50px

Content:

- Call Us: `+5999 724 3131 / +5999 724 3132`
- Address: `Wechi Kavel E4-07, Curaçao`
- Email Us: `info@wechi.cw`
- Social links: Facebook, Instagram, WhatsApp

### B. Navigation Bar

Container:

- Full-width black section
- Desktop menu centered

Desktop:

- Height about 70px
- Menu items:
  - Home
  - About Wechi
  - Our Houses
  - Meet the Team
  - Contact Us
- White uppercase text, tight spacing

Tablet/mobile:

- Black bar height about 72px
- Hide menu links
- Show hamburger icon aligned right
- Hamburger color: light gray/white
- Mobile bar appears directly below stacked contact header

### C. Hero

Container:

- Full-width section with background aerial Wechi neighborhood image
- Background size: cover
- Background position: center center desktop/tablet, center lower on mobile
- Add dark overlay around 25-35%

Desktop:

- Height about 690-720px including image
- Centered content horizontally and vertically
- H1: `WECHI TA E LUGÁ`
- Subtitle: `Invest in Curaçao’s Future – Secure Your Place in Wechi Development Project`
- Button: `REQUEST INVESTMENT DETAILS`
- Button link: anchor to contact/register section

Tablet:

- Taller hero, about 830px
- Text centered, larger than desktop proportionally
- Button remains centered

Mobile:

- Height about 1200-1300px including visible image area
- Text appears lower-middle
- H1 around 43px
- Subtitle wraps into two lines
- Button wide pill, about 75-80% width

### D. Stats Band

Container:

- Full-width brown background `#6F4E37`
- Inner max 1140px

Desktop:

- 3 columns
- Padding 70px top/bottom
- White line icons above stats

Stat text:

- `87 UNITS` / `FOR SALE`
- `+50` / `SATISFIED CLIENTS`
- `3 YEARS` / `OF IMPECCABLE REPUTATION`

Tablet:

- First two stats in two columns, third drops below left/center depending screen
- Very tall brown area

Mobile:

- Stack all 3 vertically centered
- Large spacing between stats
- Numbers around 54-60px
- Total section height about 1450px in screenshot

### E. About Wechi

Important responsive note:

- Visible on desktop and tablet.
- Hidden on mobile screenshot.
- Use Elementor responsive visibility to hide the entire section on mobile.

Desktop/tablet structure:

- White section
- Inner 2 columns
- Left text column, right image column
- Left width about 38%, right 48%
- About image: `zd5ni4u6uecxmgxhmxwtdycqvxgtz4rn7zgurlls_2x_2x_1x.jpg`
- Padding top/bottom about 90px

Content:

- Eyebrow: `About Wechi`
- Heading: `WELCOME TO WECHI!`
- Brown dot/divider below heading
- Paragraphs:
  - `Where Space, Tranquility, and Lasting Value Meet.`
  - `Start your journey today and take the first step toward a new life at Wechi.`
  - Bold subhead: `Find the Home That Fits You`
  - Main body about residences
  - Bold subhead: `Discover Wechi First-Hand`
  - Main body about tour
- Large centered/brown statement:
  - `YOUR HOME IN A SAFE, GREEN, AND FUTURE-ORIENTED NEIGHBORHOOD.`
- Button: `INVEST NOW`, anchor to contact

### F. Projects

Container:

- White section
- Inner max 1140px
- Header centered
- Project cards below

Header content:

- Eyebrow: `Projects`
- Heading: `OUR PROJECTS`
- Brown divider
- Intro:
  - `Already more than 50 of our clients have become happy owners of beautiful, cozy apartments according to their requests and on favorable terms. Become one of them, too!`

Desktop:

- 4 columns
- Equal-width cards
- Images square
- No card background or border
- Text left aligned
- Bottom centered CTA: `BOOK YOUR FUTURE HOME`

Tablet:

- Use carousel/slider showing 3 cards across
- Brown square arrow controls at left/right screen edges
- CTA below cards

Mobile:

- Use carousel/slider showing 1 card
- Brown square arrow controls mid-height at left/right edges
- Only first project visible in screenshot
- Large typography and wide image
- CTA huge pill, full-ish width

Project cards:

1. Milon di Seru
   - Image: `milon_di_seru_6_1x_1x.png`
   - Title: `MILON DI SERU`
   - Subtitle: `Two Floors. Endless Possibilities.`
   - Status: `✨ Coming Soon`
   - Bullets from live page
   - Link: `Read more & Book a unit`

2. Sentebibu
   - Image: `datu_vrijstaand_6_1x_1x.png`
   - Title: `SENTEBIBU`
   - Subtitle: `A home on its own plot with extra space, tranquility, and lasting value.`
   - Status: `📈 Pre-Sales Start 2026 ✅`
   - Link: `Read more & Book a unit`

3. Datu
   - Image: `untitled_design_1x_1x.png`
   - Title: `DATU`
   - Status: `✨ SOLD OUT`
   - No button visible

4. Datu-Duplo
   - Image: `untitled_design_1_1x_1x.png`
   - Title: `DATU-DUPLO`
   - Status: `✨ SOLD OUT`
   - No button visible

### G. Team

Container:

- Full-width section
- Background image: use team portraits as background, dark overlay 65-75%
- Foreground content overlaps lower white area

Desktop:

- Header over dark background
- 3 portrait cards in one row
- Images:
  - `021_2x_1x.jpg`
  - `028_large_2x_1x.jpg`
  - `048_2x_1x.jpg`
- Images 100% width, tall portrait crop
- Names/roles below on white

Tablet:

- 2 columns first row, third centered/left below
- Background header remains full width

Mobile:

- Header very tall, background centered on Diamela face
- Team members stacked one per row
- Portrait images nearly full width
- Large vertical spacing

Content:

- Eyebrow: `Professionals`
- Heading: `OUR TEAM`
- Text:
  - `Our specialists will help you find the ideal home. We have a huge selection of objects and our specialists will select you exactly what you want, according to your requirements.`
- Kani Gidder: `Finance Manager`
- Diamela Martines: `Operational Director`
- Tracy Job: `Real Estate & Sales`

### H. Life At Wechi / Video

Container:

- White heading section
- Full-width video image/thumbnail section below with dark overlay

Header:

- Eyebrow: `Life at Wechi`
- Heading: `HEAR FROM THOSE WHO CALL IT HOME`
- Brown divider
- Text:
  - `Step inside the stories of our residents and see why Wechi is more than just a neighborhood – it’s a community built on safety, greenery, and peace of mind.`

Video:

- Background thumbnail from YouTube/video screenshot
- Play icon centered
- Overlay text:
  - `WATCH THE VIDEO AND DISCOVER`
  - `WHAT YOUR FUTURE COULD LOOK LIKE AT WECHI.`
- Link: YouTube popup `https://youtu.be/pZhwiyfChv0`
- Button below: `SCHEDULE MY VISIT`, anchor to contact

Desktop:

- Video height about 450px
- Button centered below

Mobile:

- Heading very large
- Video height about 800px
- Button huge pill below video

### I. FAQ

Container:

- White section
- Inner 2 columns desktop/tablet
- Left: image and intro
- Right: accordion list

Image:

- `vho7gdsyrmsjdulptm65ghvabcprgk7p3hjd829p_1x.png`

Content:

- Heading: `FREQUENTLY ASKED QUESTIONS`
- Description as shown on live page
- Accordion items:
  - Master Plan
  - Local Financing
  - Long-term land lease (Erfpacht)
  - Can I rent out my house?
  - What are the additional costs?
  - Service Costs
  - Security

Style:

- Question mark icon left
- Brown divider line under each item
- Chevron/arrow right
- Uppercase, weight 700
- Keep all closed by default if possible

Desktop/tablet:

- Two columns, image/intro left, accordion right

Mobile:

- Single column
- Image full width first
- Heading and intro below image
- Accordion full width

### J. Map

Container:

- Full-width Google Map embed
- Height desktop/tablet: about 420-500px
- Height mobile: about 760px
- Location: Wechi, Willemstad, Curaçao

Note:

- The screenshot shows a Google Maps API error modal. Do not intentionally recreate the error if using a valid map widget, but if exact screenshot matching is required, use a static screenshot of the map/error as the background.

### K. Contact / Form

Container:

- White section
- Desktop/tablet: 2 columns
- Mobile: stacked

Left column:

- Heading: `GET YOUR HOUSE NOW`
- Text:
  - `Fill out the feedback form to ask a question or leave a request for an apartment.`
  - `You can also contact us in any way convenient for you:`
- Contact grid:
  - Email icon, `EMAIL`, `info@wechi.cw`
  - Phone icon, `TEL.:`, `+5999 724 3131 / +5999 724 3132`
  - WhatsApp icon, `WHATSAPP`, `+5999 724 3131`

Right column form:

- Heading: `Discover Your Future at Wechi`
- Description:
  - `Get floor plans, pricing, and availability — start your journey today.`
- Fields:
  - First Name
  - Last Name
  - Phone
  - E-mail
- Submit: `Contact Me`
- Field background: `#F7F7F7`
- Submit button: rectangular brown, small radius
- Use Elementor Form.

Mobile:

- Left contact cards stack vertically with horizontal dividers
- Form below contact blocks
- Full-width inputs and button

### L. Footer

Container:

- Full-width dark gray `#555555`
- Inner max 1140px

Desktop/tablet:

- Copyright left
- Social icons right
- Floating chat button bottom right if using Bitrix/WhatsApp widget
- Back-to-top circle bottom left

Mobile:

- Copyright centered/left
- Social icons centered below
- Keep dark gray height around 300px

Footer text:

- `© 2026 All rights reserved @WECHI`

## 10. Newsletter Popup

User supplied a screenshot of a missing popup. Build this with Elementor Pro popup functionality.

Popup visual:

- White rounded modal
- Gray page overlay behind it
- Wide desktop popup
- Rounded corners around 10-14px
- Close button top-right in a muted mauve/gray circular background
- Bottom edge has a brown border/accent in the screenshot

Text:

- Heading:
  - `Get Exclusive Updates on Curaçao’s Future Living`
- Subtitle:
  - `Subscribe to the Wechi newsletter and be the first to know about new releases, investment insights, and community updates`

Form:

- Use Elementor Form.
- Fields:
  - `First Name *`
  - `E-mail *`
- Button:
  - `Keep Me Informed`
- Button background brown.
- Button full width.

Trigger:

- Connect it to the floating contact/offering icon option for Updates/Newsletter.

## 11. Floating Contact / Offering Icon

The original has a bottom-right floating contact/offering button.

When clicked, it should reveal options:

- WhatsApp
- Chat
- Email
- Updates/newsletter popup

Use Elementor where possible. If a plugin is needed, ask before installing. Elementor Pro popup should handle the newsletter popup. Elementor Form should be used for forms.

## 12. Assets List

Use/download/recreate:

- Logo: `logo_horizontaal_modified_1x.png`
- Favicon/standing logo if needed: `logo_wechi_staand_1.png`
- Hero aerial neighborhood image: use live hero image or screenshot crop if unavailable
- About aerial image: `zd5ni4u6uecxmgxhmxwtdycqvxgtz4rn7zgurlls_2x_2x_1x.jpg`
- Milon di Seru: `milon_di_seru_6_1x_1x.png`
- Sentebibu: `datu_vrijstaand_6_1x_1x.png`
- Datu sold out: `untitled_design_1x_1x.png`
- Datu-Duplo sold out: `untitled_design_1_1x_1x.png`
- Team Kani: `021_2x_1x.jpg`
- Team Diamela: `028_large_2x_1x.jpg`
- Team Tracy: `048_2x_1x.jpg`
- FAQ image: `vho7gdsyrmsjdulptm65ghvabcprgk7p3hjd829p_1x.png`
- Video thumbnail/background: recreate from YouTube thumbnail or screenshot
- Play icon: `play.png`
- Map marker: `spotlight-poi3_hdpi.png`
- Icons: phone, map pin, envelope, house/hand, smile, trophy, email, phone arrow, WhatsApp, question mark, chevron, social icons

## 13. Responsive Behavior Summary

- Header contact: desktop/tablet horizontal, mobile stacked and centered.
- Navigation: desktop menu links, tablet/mobile hamburger only.
- Hero: full-width image, text centered; mobile uses taller image and larger wrapped text.
- Stats: desktop 3 columns, tablet 2 plus 1, mobile single stacked column.
- About: desktop/tablet 2 columns, hidden on mobile to match screenshot.
- Projects: desktop 4 columns, tablet carousel 3 visible, mobile carousel 1 visible.
- Team: desktop 3 columns, tablet 2/1, mobile stacked.
- Video: full-width, taller on mobile.
- FAQ: desktop/tablet 2 columns, mobile stacked.
- Contact: desktop/tablet 2 columns, mobile stacked with full-width form.
- Footer: desktop horizontal, mobile centered/stacked.

## 14. Custom CSS Guidance

No custom CSS should be required if Elementor Pro containers, responsive visibility, carousel, accordion, background overlays, and global styles are used correctly.

Only add CSS if:

- The active theme forces unwanted heading margins.
- The active theme prevents full-width sections.
- Elementor cannot reproduce the required button radius/spacing.
- The floating launcher needs a tiny positioning adjustment.

Do not rebuild the page as a single HTML/CSS blob.

## 15. Rebuild Checklist

1. Confirm staging is reachable.
2. Confirm login/admin/editor access.
3. Backup or duplicate current page if needed.
4. Set Elementor global colors and Open Sans typography.
5. Upload all image assets.
6. Set page layout to full-width/Canvas as appropriate.
7. Build top contact header for desktop/tablet, then mobile stacking.
8. Build black nav with desktop menu and tablet/mobile hamburger.
9. Build hero with background image, overlay, centered text, and CTA anchor.
10. Build brown stats band with 3 icon/stat blocks.
11. Build About section and hide it on mobile.
12. Build Projects header and project carousel/grid; set desktop 4, tablet 3, mobile 1.
13. Add large `BOOK YOUR FUTURE HOME` CTA.
14. Build Team section with dark background overlay and foreground portrait layout.
15. Build Life at Wechi heading and video banner with YouTube popup.
16. Add `SCHEDULE MY VISIT` CTA.
17. Build FAQ section with image/intro and accordion.
18. Add Google Map or static map screenshot if matching the error state exactly.
19. Build contact section with contact methods and Elementor form styling.
20. Build footer with copyright, social icons, back-to-top, and chat/WhatsApp widget.
21. Build Elementor Pro newsletter popup.
22. Connect floating launcher option to the newsletter popup.
23. Test desktop against screenshot.
24. Test tablet against screenshot.
25. Test mobile against screenshot.
26. Remove/deactivate old HTML-widget content only after the real Elementor version is complete.

## 16. Manual Verification Needed

Verify:

- Staging site does not timeout.
- The page is not still mainly inside an HTML widget.
- Full-width sections touch viewport edges.
- Header logo has no black rectangle.
- Hero image matches original.
- Nav and header match original spacing.
- About is hidden on mobile.
- Projects use proper responsive carousel behavior.
- Contact form is Elementor Form.
- Newsletter popup opens/closes correctly.
- Floating contact button expands to all expected options.
- Footer and floating controls match original.
- No unnecessary plugins were installed.
- No broad custom CSS was added unless truly necessary.

