<script lang="ts">
	import '../app.css';
	import '$lib/styles/global.css';
	import '$lib/styles/animations.css';
	import { fly } from 'svelte/transition';
	import { pageTransition } from '$lib/utils/animations';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import ChatBot from '$lib/components/ChatBot.svelte';
</script>

<div class="app-wrapper">
	<Header />
	<main 
		in:fly={pageTransition.in} 
		out:fly={pageTransition.out}
		class="animate-gradient"
	>
		<slot />
	</main>
	<Footer />
	<ChatBot />
</div>

<style>
	.app-wrapper {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		margin-top: 80px;
	}
</style>
