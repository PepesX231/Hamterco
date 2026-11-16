import { Header } from "@/components/Header";
import { Hero } from "@/components/Hero";
import { Courses } from "@/components/Courses";
import { LegacyRuntime } from "@/components/LegacyRuntime";

export default function Home() {
  return (
    <main>
      <Header />
      <Hero />
      <Courses />
      {/* the rest of the home page still runs from the original code; parts already moved to React are hidden there */}
      <LegacyRuntime view="home" hide={['[data-view="home"] > .zq', '[data-view="home"] > .je', '[data-view="home"] > section.ft']} />
    </main>
  );
}
