import type { Metadata } from "next";
import "./styles/globals.css";

export const metadata: Metadata = {
  title: "Prajwal Banthiya | MERN Stack Developer",
  description:
    "Portfolio of Prajwal Banthiya — MERN Stack Developer, AWS Certified, Full Stack Engineer based in Maharashtra, India.",
  keywords: [
    "Prajwal Banthiya",
    "MERN Stack Developer",
    "Full Stack Developer",
    "React Developer",
    "Node.js",
    "MongoDB",
    "AWS Certified",
    "Portfolio",
    "Maharashtra",
    "WIT Solapur",
  ],
  authors: [{ name: "Prajwal Banthiya" }],
  openGraph: {
    title: "Prajwal Banthiya | MERN Stack Developer",
    description:
      "Portfolio of Prajwal Banthiya — MERN Stack Developer, AWS Certified, Full Stack Engineer.",
    url: "https://prajwalbanthiya.vercel.app",
    siteName: "Prajwal Banthiya Portfolio",
    locale: "en_IN",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Prajwal Banthiya | MERN Stack Developer",
    description:
      "Portfolio of Prajwal Banthiya — MERN Stack Developer, AWS Certified.",
    creator: "@prajwalbanthiya",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <link rel="icon" href="/favicon.ico" />
        <link
          href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body style={{ background: "#0a0a0f", color: "#e2e8f0" }}>
        {children}
      </body>
    </html>
  );
}
