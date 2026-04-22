# Prajwal Banthiya — Portfolio Website

A full-featured, animated dark-theme portfolio built with Next.js 14, TypeScript, Framer Motion, and Three.js.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 📁 Updating Your Content

**All personal content lives in one file:**
```
app/lib/data.ts
```
Edit your name, bio, projects, skills, experience, education, and achievements there.

---

## 📧 Setting Up Email (Contact Form)

1. Sign up at [EmailJS](https://www.emailjs.com/)
2. Create a service, template, and get your public key
3. In `app/components/Contact.tsx`, replace the timeout simulation with:

```typescript
import emailjs from 'emailjs-com';

await emailjs.send(
  process.env.NEXT_PUBLIC_EMAILJS_SERVICE_ID!,
  process.env.NEXT_PUBLIC_EMAILJS_TEMPLATE_ID!,
  form,
  process.env.NEXT_PUBLIC_EMAILJS_PUBLIC_KEY!
);
```

4. Create `.env.local`:
```
NEXT_PUBLIC_EMAILJS_SERVICE_ID=your_service_id
NEXT_PUBLIC_EMAILJS_TEMPLATE_ID=your_template_id
NEXT_PUBLIC_EMAILJS_PUBLIC_KEY=your_public_key
```

---

## 🖼️ Adding Your Photo

Replace the initials placeholder in `app/components/About.tsx`:

```tsx
// Replace the initials div with:
<Image
  src="/images/profile.jpg"
  alt="Prajwal Banthiya"
  fill
  className="object-cover rounded-full"
/>
```

Add your photo at `public/images/profile.jpg`.

---

## 📄 Adding Resume

Place your resume PDF at:
```
public/resume.pdf
```

---

## 🌐 Deploy to Vercel

```bash
npm install -g vercel
vercel
```

Or connect your GitHub repo at [vercel.com](https://vercel.com) for automatic deployments.

Add your environment variables in Vercel Dashboard → Settings → Environment Variables.

---

## 🛠️ Tech Stack

- **Next.js 14** — App Router, SSR
- **TypeScript** — Full type safety
- **Framer Motion** — All animations
- **Three.js / @react-three/fiber** — 3D particle background
- **Tailwind CSS** — Utility-first styling
- **EmailJS** — Contact form
- **Vercel** — Deployment

---

## 📌 Sections

| Section | ID |
|---|---|
| Hero | `#home` |
| About | `#about` |
| Skills | `#skills` |
| Projects | `#projects` |
| Experience | `#experience` |
| Education | `#education` |
| Achievements | `#achievements` |
| Contact | `#contact` |

---

Built with ❤️ by Prajwal Banthiya
