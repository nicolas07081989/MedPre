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
				// Ignora errores 404 para archivos de iconos durante el prerender
				if (path.startsWith('/icons/') && message.includes('404')) {
					return;
				}
				// Para otros errores, lanza el error
				throw new Error(message);
			}
		}
	},
	preprocess: vitePreprocess()
};

export default config;
