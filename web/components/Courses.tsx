import { LINE_URL, img } from "@/lib/site";

// "คอร์สที่เราแนะนำ": the open course big, the two waiting for their next round beside each other.
export function Courses() {
  return (
    <section className="mx-auto max-w-[1240px] px-4 py-20 md:px-6">
      <h2 className="font-display text-[clamp(34px,4vw,56px)] font-extrabold leading-tight">คอร์สที่เราแนะนำ</h2>
      <p className="mt-2 text-ink/70">คอร์สหลักของ Hamster Hub เลือกตามสิ่งที่น้องอยากได้</p>

      <a href="https://www.hamsterhub.co/portex-site/index.html" target="_blank" rel="noopener" className="mt-8 grid overflow-hidden bg-[#1E1A3A] text-white md:grid-cols-[1.25fr_1fr]">
        <div className="relative aspect-[16/9] md:aspect-auto">
          <video src={img("portex-hero.mp4")} poster={img("portex-poster.webp")} muted loop autoPlay playsInline preload="none" className="absolute inset-0 size-full object-cover" />
          <span className="absolute left-4 top-4 bg-white px-3 py-1 text-[13px] font-semibold text-[#1a7f3c]">● เริ่มเรียนแล้ว 9 พ.ย.</span>
        </div>
        <div className="p-6 md:p-10">
          <p className="text-[15px] font-semibold text-[#F6B26B]">สำหรับน้อง ม.6 ที่ยังไม่มีผลงาน</p>
          <h3 className="mt-2 font-display text-[clamp(30px,3.2vw,46px)] font-bold">Port Express</h3>
          <p className="mt-3 text-white/85">เรียนเขียนโปรแกรมสร้างเกมของตัวเองด้วย Unity จบคอร์สได้เกมที่ทำเองไว้ใส่พอร์ต</p>
          <dl className="mt-6 grid grid-cols-3 gap-4">
            {[["2 เดือน", "จันทร์ พุธ ศุกร์"], ["9 พ.ย. 2569", "เริ่มเรียน"], ["5,990 บาท", "ทั้งคอร์ส"]].map(([b, s]) => (
              <div key={b}>
                <dt className="font-display text-[18px] font-bold">{b}</dt>
                <dd className="text-[14px] text-white">{s}</dd>
              </div>
            ))}
          </dl>
          <span className="mt-7 inline-block bg-[#F6B26B] px-5 py-3 font-display font-bold text-ink">ดูรายละเอียดคอร์ส</span>
        </div>
      </a>

      <div className="mt-4 grid gap-4 md:grid-cols-2">
        {[
          { cover: "cbp-hamstarter.webp", who: "สำหรับน้องที่ยังไม่เคยเขียนโปรแกรม", name: "Hamstarter", what: "เริ่มจากศูนย์ จนมีผลงานชิ้นแรกเป็นของตัวเอง", proof: "น้องปลื้มจากคอร์สนี้ ติดสถิติประยุกต์ฯ สจล." },
          { cover: "cbp-national.webp", who: "สำหรับน้องที่อยากมีรางวัลระดับประเทศในพอร์ต", name: "National Project", what: "ทำโปรเจกต์ส่งเวทีระดับประเทศ เช่น NSC (การแข่งขันพัฒนาโปรแกรมคอมพิวเตอร์แห่งประเทศไทย)", proof: "รุ่นพี่ 5 คนจากคอร์สนี้ ติดวิศวะคอมฯ CEDT และวิทย์คอมฯ" },
        ].map((c) => (
          <a key={c.name} href={LINE_URL} target="_blank" rel="noopener" className="grid grid-cols-[40%_1fr] border border-ink/15 bg-[#FFFDF8]">
            <img src={img(c.cover)} alt="" className="size-full object-cover" loading="lazy" />
            <div className="p-5">
              <p className="text-[14px] text-ink/60">○ รอเปิดรอบถัดไป</p>
              <p className="mt-3 text-[13px] font-semibold text-[#B4561B]">{c.who}</p>
              <h3 className="font-display text-[26px] font-bold">{c.name}</h3>
              <p className="mt-2 text-[15px] text-ink/75">{c.what}</p>
              <span className="mt-4 inline-block border border-ink px-4 py-2 text-[14px] font-semibold">ทัก LINE ขอข่าวรอบถัดไป</span>
              <p className="mt-4 text-[13px] text-ink/70">{c.proof}</p>
            </div>
          </a>
        ))}
      </div>
    </section>
  );
}
