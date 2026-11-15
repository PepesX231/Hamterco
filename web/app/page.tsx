import { Header } from "@/components/Header";
import { Hero } from "@/components/Hero";
import { OLD_SITE } from "@/lib/site";

export default function Home() {
  return (
    <main>
      <Header />
      <Hero />
      {/* The rest of the home page is still being moved over. */}
      <section className="mx-auto max-w-[760px] px-4 pb-24 pt-32 text-center">
        <p className="text-[17px] text-ink/70">ส่วนอื่นของหน้ากำลังย้ายมาที่เวอร์ชันใหม่</p>
        <a href={`${OLD_SITE}#home`} className="mt-2 inline-block font-semibold underline underline-offset-4">
          ดูหน้าเต็มที่เว็บปัจจุบัน
        </a>
      </section>
    </main>
  );
}
