# Rohanth Bakki — Premium 3D Futuristic Portfolio

> High-End 3D Animated Developer-Style Portfolio for **Rohanth Bakki** — Digital Creator & Instagram Influencer (@rohanthbakki) based in Rajahmundry, Andhra Pradesh, India.

---

## 🌟 Overview & Architecture

This portfolio is engineered to deliver an award-winning, cinematic Awwwards-style experience inspired by Apple's minimalist luxury aesthetics and modern WebGL interactive art.

### Key Highlights
- **WebGL 3D Interactive Universe**: Built on Three.js featuring an interactive particle starfield, floating holographic geometric sculptures (Torus Knot with glowing core, dual orbiting cyber rings, and floating polyhedra), and dual-color dynamic point lights (Neon Violet `#a855f7` & Electric Cyan `#06b6d4`) that react in real-time to cursor coordinates and scroll velocity.
- **Genuine Identity & Profile Presentation**: Preserves Rohanth Bakki's actual face and portrait photograph (`assets/images/rohanth-profile.jpg`) inside an interactive 3D holographic card with orbital glow badges and specular glare reflection.
- **Instagram Showcase (@rohanthbakki)**: Features Rohanth's genuine 1,080 followers with a smooth rolling counter animation on scroll, verified creator badge styling, and direct link to his official Instagram page.
- **Interactive Photography Gallery**: Modern responsive masonry grid with filter pills (*All*, *Portraits*, *Cinematic*, *Urban*, *Creative*) and a full lightbox preview with keyboard navigation (Esc, Arrow keys).
- **Dual-Facet Project Showcase**:
  1. *Digital Creator Portfolio*: Creative identity, content creation, photography, and video editing.
  2. *NeuroScan AI – Brain Stroke Detection*: Medical imaging AI project with genuine scan visualization and direct link to the live platform (`https://brainstroke-0w0m.onrender.com`).
- **Brand Collaborations**: Structured partnership cards for sponsored campaigns, product aesthetics, and creative direction with direct inquiry triggers.
- **Glassmorphic Navigation & Mobile Drawer**: Sticky transparent navigation with backdrop blur, active section highlighting (scroll spy), and an animated responsive mobile hamburger drawer.
- **Performance & Zero Dependency**: Works instantly offline and online with bundled vendor scripts, zero build friction, 60fps animations, and accessibility overrides for `prefers-reduced-motion`.

---

## 🚀 How to Run Locally

You can launch and preview the website in several convenient ways:

### Option 1: Double-Click Launcher (Windows — Easiest)
Simply double-click the included batch script in the project root:
```cmd
start-dev-server.bat
```
This automatically starts the local server and opens `http://localhost:3000` in your default browser!

### Option 2: Python Command Line
Run the included custom development server with Python 3:
```bash
python server.py --open
```
or standard Python HTTP server:
```bash
python -m http.server 3000
```
Then visit [http://localhost:3000](http://localhost:3000) in your browser.

### Option 3: Direct File Open
You can also directly double-click `index.html` in any browser (Chrome, Edge, Opera GX, Safari, Firefox).

---

## 📝 Details You Can Update Later

All configuration is centralized and easy to customize without breaking any styles or animations:

### 1. Adding / Updating Photographs
- **Profile Photo**: Replace `assets/images/rohanth-profile.jpg` with any new high-resolution portrait.
- **Gallery Photos**:
  1. Save your photos into `assets/images/`.
  2. Open `js/gallery-data.js` in any text editor.
  3. Add a new item to the `GALLERY_ITEMS` array:
  ```javascript
  {
    id: 7,
    title: "Golden Hour Street",
    category: "urban",      // 'portraits', 'cinematic', 'urban', or 'creative'
    tag: "35mm / Sunset",
    date: "2026",
    src: "assets/images/my-new-photo.jpg",
    aspect: "tall",         // 'tall', 'wide', or 'square'
    description: "Captured during sunset in Rajahmundry."
  }
  ```

### 2. Updating Contact Information (Email & WhatsApp)
Open `index.html` and search for `contact@rohanthbakki.com` or `+91`:
- Update `contact@rohanthbakki.com` with your real email address.
- Update `+91 [Number Placeholder]` with your real WhatsApp Business phone number.

### 3. Updating Education Details
In `index.html` under the `#about` section:
- Look for the card with `Education` and `Diploma`.
- Update the institution name, specialization, or graduation year when ready.

### 4. Updating Follower Count
When your Instagram audience grows beyond 1,080:
- In `index.html`: Update `<div class="instagram-stat-num" id="follower-counter">1,080</div>`.
- In `js/main.js`: Update `animateCounter(followerCountElem, 1080, 2200)` to your new follower count.

---

## 📬 Connecting the Contact Form to Your Email

The contact form includes client-side validation and friendly toast feedback. To have submissions delivered directly to your inbox, you can connect **Formspree** or **Web3Forms** in 60 seconds:

### Using Formspree (Free & Simple)
1. Sign up at [formspree.io](https://formspree.io).
2. Create a new form and copy your Form ID (e.g., `xpznkowa`).
3. In `index.html`, add the `action` attribute to the `<form>` tag:
   ```html
   <form class="contact-form" id="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
4. Submissions will now arrive straight into your personal email inbox!

---

## 🌐 How to Deploy for Free

### Method 1: Vercel (Recommended)
1. Install Vercel CLI (`npm i -g vercel`) or visit [vercel.com](https://vercel.com).
2. Push your project to GitHub or run `vercel` in this folder.
3. Vercel automatically detects the pre-configured `vercel.json` and deploys your site to an ultra-fast global edge network with a free `rohanth-bakki.vercel.app` domain and free SSL!

### Method 2: Netlify
1. Go to [netlify.com](https://netlify.com).
2. Drag and drop the `portfolio` folder directly into the Netlify dashboard.
3. It deploys instantly using the included `netlify.toml`!

### Method 3: GitHub Pages
1. Create a GitHub repository named `portfolio` (or `rohanthbakki.github.io`).
2. Run:
   ```bash
   git init
   git add .
   git commit -m "Initial release of 3D portfolio"
   git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
   git push -u origin main
   ```
3. Go to **Settings > Pages > Branch: main / root** and click Save.
4. Your site will be live at `https://YOUR_USERNAME.github.io/portfolio/`.

---

## 📁 File Structure

```
portfolio/
├── assets/
│   ├── icons/
│   │   └── favicon.svg           # Futuristic RB monogram SVG favicon
│   └── images/
│       ├── rohanth-profile.jpg   # Rohanth Bakki's authentic photograph
│       ├── brain-scan.jpg        # NeuroScan AI real diagnostic scan preview
│       ├── project-creator.svg   # Digital Creator Portfolio preview
│       ├── gallery-cinematic.svg # Cinematic color study visual
│       ├── gallery-urban.svg     # Urban architectural perspective visual
│       ├── gallery-creative.svg  # Creative concept visual
│       ├── gallery-golden.svg    # Golden hour lighting visual
│       └── gallery-night.svg     # Cyberpunk nightscape visual
├── css/
│   └── style.css                 # Apple luxury glassmorphic styling & animations
├── js/
│   ├── gallery-data.js           # Easy-to-edit gallery configuration array
│   ├── three-scene.js            # Three.js 3D WebGL background, particles & lighting
│   ├── main.js                   # Navigation, 3D tilt, counter, lightbox, contact form
│   └── vendor/
│       ├── three.min.js          # Three.js r128 (local bundled for 100% offline support)
│       ├── gsap.min.js           # GSAP 3.12 (local bundled)
│       └── ScrollTrigger.min.js  # GSAP ScrollTrigger plugin (local bundled)
├── index.html                    # Semantic, accessible HTML5 structure & schema
├── server.py                     # Python local development server
├── start-dev-server.bat          # 1-click Windows dev launcher
├── package.json                  # Metadata and scripts
├── vercel.json                   # Edge routing & security headers for Vercel
├── netlify.toml                  # Edge routing & security headers for Netlify
└── README.md                     # Documentation and deployment guide
```

---

*Designed and developed for Rohanth Bakki.*
