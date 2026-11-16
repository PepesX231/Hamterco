import { Header } from "@/components/Header";
import { LegacyRuntime } from "@/components/LegacyRuntime";

// Not yet rewritten as React components: the original page runs here (see components/LegacyRuntime.tsx).
export default function Page() {
  return (
    <main>
      <Header tone="solid" active="กิจกรรม" />
      <LegacyRuntime view="activity" />
    </main>
  );
}
