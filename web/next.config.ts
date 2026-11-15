import type { NextConfig } from "next";

// Static export for GitHub Pages: the built site lives at /Hamterco/next/ next to the old slime.html.
const nextConfig: NextConfig = {
  output: "export",
  basePath: "/Hamterco/next",
  trailingSlash: true,
  images: { unoptimized: true },
};

export default nextConfig;
