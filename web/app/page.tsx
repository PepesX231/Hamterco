import { Hero } from "@/components/Hero";
import { HomeStore } from "@/components/HomeStore";
import { LegacyRuntime } from "@/components/LegacyRuntime";

export default function Home() {
  return (
    <main>
      <div className="nx-home">
        <Hero />
        <HomeStore />
      </div>
      {/* the rest of the home page still runs from the original code; parts already moved to React are hidden there */}
      <LegacyRuntime view="home" hide={['[data-view="home"] > .zq', '[data-view="home"] > .je', '[data-view="home"] > section.ft', '[data-view="home"] > section.zc2']} />
    </main>
  );
}
