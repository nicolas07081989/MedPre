import adapter from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			runtime: 'edge',
			regions: ['iad1'],
			split: true
		}),
		prerender: {
			handleHttpError: ({ path, referrer, message }) => {
				if (path.startsWith('/images/') || path.startsWith('/icons/')) {
					console.warn(`Warning: Asset not found: ${path}`);
					return;
				}
				throw new Error(message);
			},
			entries: ['*'],
			origin: 'https://medpre.vercel.app'
		},
		alias: {
			$components: 'src/lib/components',
			$styles: 'src/styles'
		},
		csrf: {
			checkOrigin: true
		}
	},
	preprocess: vitePreprocess({
		onwarn: (warning, handler) => {
			if (warning.code === 'css-unused-selector') return;
			handler(warning);
		},
		style: {
			postcss: true
		}
	}),
	compilerOptions: {
		dev: process.env.NODE_ENV !== 'production',
		enableSourcemap: process.env.NODE_ENV !== 'production'
	}
};

export default config;
