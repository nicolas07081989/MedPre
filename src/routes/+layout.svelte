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

<svelte:head>
	<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">
	<title>MedPre - Medicina de Precisión Ecuador</title>
	<link 
		rel="stylesheet" 
		href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
	/>
</svelte:head>

<div class="app-wrapper">
	<Header />
	<nav class="main-nav">
		<div class="container">
			<a href="/" class="nav-link">
				<img src="/icons/home.svg" alt="Inicio" class="nav-icon" />
				<span>Inicio</span>
			</a>
			<a href="/quienes-somos" class="nav-link">
				<img src="/icons/team.svg" alt="Quiénes Somos" class="nav-icon" />
				<span>Quiénes Somos</span>
			</a>
			<a href="/inversion" class="nav-link">
				<img src="/icons/investment.svg" alt="Inversión" class="nav-icon" />
				<span>Inversión</span>
			</a>
			<a href="/respuestas" class="nav-link">
				<img src="/icons/faq.svg" alt="Respuestas" class="nav-icon" />
				<span>Respuestas</span>
			</a>
			<a href="/contacto" class="nav-link">
				<img src="/icons/contact.svg" alt="Contacto" class="nav-icon" />
				<span>Contacto</span>
			</a>
		</div>
	</nav>
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
		margin: 0;
		padding: 0;
	}

	main {
		flex: 1;
		margin-top: 80px;
		margin-bottom: 0;
		padding-bottom: 0;
		display: flex;
		flex-direction: column;
	}

	.main-nav {
		background: var(--color-white);
		box-shadow: 0 2px 4px rgba(0,0,0,0.1);
		padding: 1rem 0;
		position: sticky;
		top: 0;
		z-index: 100;
	}

	.main-nav .container {
		display: flex;
		justify-content: center;
		gap: 2rem;
	}

	.nav-link {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		color: var(--color-primary);
		text-decoration: none;
		font-weight: 500;
		padding: 0.5rem 1rem;
		border-radius: 0.5rem;
		transition: all 0.3s ease;
	}

	.nav-link:hover {
		background: var(--color-accent);
		color: var(--color-primary);
	}

	.nav-icon {
		width: 24px;
		height: 24px;
		object-fit: contain;
	}

	@media (max-width: 768px) {
		.nav-icon {
			width: 20px;
			height: 20px;
		}

		.main-nav .container {
			gap: 1rem;
		}

		.nav-link span {
			display: none;
		}
	}
</style>
