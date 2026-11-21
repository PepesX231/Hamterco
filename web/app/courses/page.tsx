// "คอร์ส" is now Hams Route. Old links to /courses/ land here and move on.
export default function Page() {
  return (
    <main style={{ padding: "140px 16px", textAlign: "center" }}>
      <meta httpEquiv="refresh" content="0; url=/Hamterco/next/routes/" />
      <script dangerouslySetInnerHTML={{ __html: "location.replace('/Hamterco/next/routes/')" }} />
      <a href="/Hamterco/next/routes/">ไปที่ Hams Route</a>
    </main>
  );
}
