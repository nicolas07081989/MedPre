import adapter from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			runtime: 'edge'
		}),
		prerender: {
			handleHttpError: ({ path, referrer, message }) => {
				// Ignorar errores 404 específicos durante el prerender
				if (path.startsWith('/images/') || path.startsWith('/icons/')) {
					console.warn(`Warning: Asset not found: ${path}`);
					return;
				}
				throw new Error(message);
			}
		}
	},
	preprocess: vitePreprocess()
};

export default config;
