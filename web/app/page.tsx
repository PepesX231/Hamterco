import { Header } from "@/components/Header";
import { Hero } from "@/components/Hero";
import { Courses } from "@/components/Courses";
import { OLD_SITE } from "@/lib/site";

export default function Home() {
  return (
    <main>
      <Header />
      <Hero />
      <Courses />
      {/* The rest of the home page is still being moved over. */}
      <section className="mx-auto max-w-[760px] px-4 pb-24 pt-8 text-center">
        <a href={`${OLD_SITE}#home`} className="font-semibold underline underline-offset-4">ส่วนอื่นยังอยู่ที่เว็บปัจจุบัน</a>
      </section>
    </main>
  );
}
