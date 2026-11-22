import { LegacyRuntime } from "@/components/LegacyRuntime";
import { SheetWorks } from "@/components/SheetWorks";

// Not yet rewritten as React components: the original page runs here (see components/LegacyRuntime.tsx).
export default function Page() {
  return (
    <main>
      <SheetWorks />
      <LegacyRuntime view="works" />
    </main>
  );
}
