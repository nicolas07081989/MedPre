import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [sveltekit()],
  build: {
    target: 'esnext',
    minify: 'esbuild',
    cssMinify: true,
    rollupOptions: {
      output: {
        manualChunks: (id) => {
          if (id.includes('node_modules')) {
            if (id.includes('svelte')) return 'vendor-svelte';
            return 'vendor';
          }
          if (id.includes('src/lib')) return 'lib';
        }
      }
    },
    reportCompressedSize: false,
    chunkSizeWarningLimit: 1000,
    assetsInlineLimit: 4096
  },
  optimizeDeps: {
    include: ['svelte'],
    exclude: ['@sveltejs/kit']
  },
  server: {
    fs: {
      strict: false
    }
  },
  ssr: {
    noExternal: ['@sveltejs/kit']
  }
});
