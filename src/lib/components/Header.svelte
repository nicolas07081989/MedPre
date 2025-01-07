<script lang="ts">
	import { page } from '$app/stores';
	import { slide } from 'svelte/transition';
	let isMenuOpen = false;

	const menuItems = [
		{ href: '/', label: 'Inicio' },
		{ href: '/quienes-somos', label: 'Quiénes Somos' },
		{ href: '/respuestas', label: 'Respuestas' },
		{ href: '/ventajas', label: 'Ventajas' },
		{ href: '/inversion', label: 'Inversión' },
		{ href: '/contacto', label: 'Contacto' }
	];
</script>

<header class="header">
	<div class="container">
		<div class="header-content">
			<a href="/" class="logo">
				<img 
					src="/logo-color.png" 
					alt="MedPre - Medicina de Precisión Ecuador" 
					class="logo-image"
				/>
			</a>

			<!-- Desktop Menu -->
			<nav class="desktop-menu">
				{#each menuItems as { href, label }}
					<a
						{href}
						class="nav-link {$page.url.pathname === href ? 'active' : ''}"
					>
						{label}
					</a>
				{/each}
			</nav>

			<!-- Mobile Menu Button -->
			<button 
				class="mobile-menu-btn" 
				on:click={() => (isMenuOpen = !isMenuOpen)}
				aria-label="Menu"
			>
				<div class="hamburger" class:open={isMenuOpen}>
					<span></span>
					<span></span>
					<span></span>
				</div>
			</button>
		</div>

		<!-- Mobile Menu -->
		{#if isMenuOpen}
			<nav class="mobile-menu" transition:slide>
				{#each menuItems as { href, label }}
					<a
						{href}
						class="mobile-link {$page.url.pathname === href ? 'active' : ''}"
						on:click={() => (isMenuOpen = false)}
					>
						{label}
					</a>
				{/each}
			</nav>
		{/if}
	</div>
</header>

<style>
	.header {
		background: var(--color-white);
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 1000;
		height: 80px;
	}

	.container {
		max-width: 1400px;
		margin: 0 auto;
		padding: 0 2rem;
		height: 100%;
	}

	.header-content {
		display: flex;
		justify-content: space-between;
		align-items: center;
		height: 100%;
		position: relative;
	}

	.logo {
		display: flex;
		align-items: center;
	}

	.logo-image {
		height: 55px;
		width: auto;
	}

	.desktop-menu {
		display: none;
		position: absolute;
		left: 50%;
		transform: translateX(-50%);
		white-space: nowrap;
	}

	@media (min-width: 768px) {
		.desktop-menu {
			display: flex;
			gap: 3rem;
			align-items: center;
		}
	}

	.nav-link {
		color: var(--color-primary);
		text-decoration: none;
		font-weight: 500;
		padding: 0.75rem 0;
		position: relative;
		transition: all 0.3s ease;
		font-size: 1.05rem;
		white-space: nowrap;
	}

	.nav-link::after {
		content: '';
		position: absolute;
		bottom: -2px;
		left: 0;
		width: 0;
		height: 2px;
		background: var(--color-secondary);
		transition: width 0.3s ease;
	}

	.nav-link:hover::after,
	.nav-link.active::after {
		width: 100%;
	}

	.nav-link:hover,
	.nav-link.active {
		color: var(--color-secondary);
	}

	/* Mobile Menu Button */
	.mobile-menu-btn {
		display: block;
		background: none;
		border: none;
		cursor: pointer;
		padding: 0;
	}

	@media (min-width: 768px) {
		.mobile-menu-btn {
			display: none;
		}
	}

	.hamburger {
		width: 24px;
		height: 20px;
		position: relative;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	.hamburger span {
		display: block;
		width: 100%;
		height: 2px;
		background: var(--color-primary);
		transition: all 0.3s ease;
	}

	.hamburger.open span:first-child {
		transform: rotate(45deg);
	}

	.hamburger.open span:nth-child(2) {
		opacity: 0;
	}

	.hamburger.open span:last-child {
		transform: rotate(-45deg);
	}

	/* Mobile Menu */
	.mobile-menu {
		position: absolute;
		top: 75px;
		left: 0;
		right: 0;
		background: var(--color-white);
		padding: 1rem;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	.mobile-link {
		display: block;
		padding: 0.75rem 1rem;
		color: var(--color-primary);
		text-decoration: none;
		transition: all 0.3s ease;
	}

	.mobile-link:hover,
	.mobile-link.active {
		background: var(--color-accent);
	}
</style> 