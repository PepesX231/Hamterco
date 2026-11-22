import type { Metadata, Viewport } from "next";
import { Anuphan, IBM_Plex_Sans_Thai, Kanit, Mali } from "next/font/google";
import "./globals.css";
import "./store.css";
import { LOADER_HTML, LOADER_JS } from "@/lib/loader";

const plex = IBM_Plex_Sans_Thai({ subsets: ["thai", "latin"], weight: ["400", "500", "600"], variable: "--font-plex", display: "swap" });
const anuphan = Anuphan({ subsets: ["thai", "latin"], variable: "--font-anuphan", display: "swap" });
const kanit = Kanit({ subsets: ["thai", "latin"], weight: ["900"], variable: "--font-kanit", display: "swap" });
const mali = Mali({ subsets: ["thai", "latin"], weight: ["700"], variable: "--font-mali", display: "swap" });

export const metadata: Metadata = {
  title: "Hamster Hub",
  description: "คอร์ส ค่าย และพอร์ตสำหรับน้อง ม.4–6 ที่อยากสร้างเกม แอป และสตาร์ทอัพของตัวเอง",
};

export const viewport: Viewport = { themeColor: "#F6AE55" };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="th" suppressHydrationWarning className={`${plex.variable} ${anuphan.variable} ${mali.variable} ${kanit.variable}`}>
      <head>
        <link rel="preload" href="/Hamterco/next/legacy/legacy.css" as="style" />
        <link rel="preload" href="/Hamterco/next/legacy/body.html" as="fetch" crossOrigin="anonymous" />
        <link rel="preload" href="/Hamterco/next/legacy/manifest.json" as="fetch" crossOrigin="anonymous" />
      </head>
      <body>
        <div id="hhL" role="status" aria-label="กำลังโหลด Hamster Hub" dangerouslySetInnerHTML={{ __html: LOADER_HTML }} />
        <script dangerouslySetInnerHTML={{ __html: LOADER_JS }} />
        {children}
      </body>
    </html>
  );
}
