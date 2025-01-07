<script>
	import { fade, fly } from 'svelte/transition';

	const ventajas = [
		{
			icon: 'vial',
			title: 'Muestra Inicial',
			description: 'Utilizamos la muestra de la primera punción, sin necesidad de procedimientos adicionales.'
		},
		{
			icon: 'user-md',
			title: 'Consulta Gratuita',
			description: 'Asesoría sin costo con especialistas para interpretar tus resultados.'
		},
		{
			icon: 'certificate',
			title: 'Respaldo Internacional',
			description: 'Avalado por consenso internacional y asociaciones médicas reconocidas.'
		},
		{
			icon: 'clock',
			title: 'Resultados Rápidos',
			description: 'Entrega de resultados en menos de un mes.'
		},
		{
			icon: 'chart-line',
			title: 'Alta Precisión',
			description: 'Reducción del 75% de cirugías innecesarias con un valor predictivo negativo del 96%.'
		},
		{
			icon: 'shield-alt',
			title: 'Confiabilidad',
			description: 'Tecnología de última generación respaldada por estudios científicos.'
		}
	];
</script>

<svelte:head>
	<title>Ventajas - MedPre Ecuador</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</svelte:head>

<main>
	<!-- Hero Section -->
	<section class="hero">
		<div class="hero-background"></div>
		<div class="hero-overlay"></div>
		<div class="container">
			<div class="hero-content" in:fade={{ duration: 1000 }}>
				<h1>Nuestras Ventajas</h1>
				<p class="hero-subtitle">
					Descubre por qué MedPre es la mejor opción para tu diagnóstico molecular
				</p>
			</div>
		</div>
	</section>

	<!-- Ventajas Grid -->
	<section class="ventajas">
		<div class="container">
			<div class="ventajas-grid">
				{#each ventajas as ventaja, index}
					<div 
						class="ventaja-card"
						in:fly={{ y: 50, duration: 1000, delay: index * 200 }}
					>
						<div class="ventaja-icon">
							<i class="fas fa-{ventaja.icon}"></i>
						</div>
						<h3>{ventaja.title}</h3>
						<p>{ventaja.description}</p>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- Estadísticas -->
	<section class="stats">
		<div class="container">
			<h2>Resultados Comprobados</h2>
			<div class="stats-grid">
				<div class="stat-card">
					<div class="stat-circle">
						<span class="stat-value">96%</span>
						<svg class="stat-ring">
							<circle cx="60" cy="60" r="54"></circle>
							<circle cx="60" cy="60" r="54" style="--percent: 96"></circle>
						</svg>
					</div>
					<span class="stat-label">Precisión diagnóstica</span>
				</div>
				<div class="stat-card">
					<div class="stat-circle">
						<span class="stat-value">75%</span>
						<svg class="stat-ring">
							<circle cx="60" cy="60" r="54"></circle>
							<circle cx="60" cy="60" r="54" style="--percent: 75"></circle>
						</svg>
					</div>
					<span class="stat-label">Reducción de cirugías</span>
				</div>
			</div>
		</div>
	</section>

	<!-- CTA Section -->
	<section class="cta">
		<div class="container">
			<div class="cta-content">
				<h2>¿Listo para comenzar?</h2>
				<p>Contacta con nuestro equipo y descubre todos los beneficios</p>
				<div class="cta-buttons">
					<a href="https://wa.me/593979136217" class="btn btn-primary">
						<i class="fab fa-whatsapp"></i>
						WhatsApp (+593) 97 913 6217
					</a>
					<a href="mailto:medpre.ecuador@gmail.com" class="btn btn-outline">
						<i class="fas fa-envelope"></i>
						medpre.ecuador@gmail.com
					</a>
				</div>
			</div>
		</div>
	</section>
</main>

<style>
	/* Estilos base copiados de la página de inicio */
	main {
		margin-top: 0;
		padding-top: 0;
		position: relative;
	}

	.container {
		max-width: 1200px;
		margin: 0 auto;
		padding: 0 1.5rem;
	}

	/* Hero Section */
	.hero {
		position: relative;
		height: 60vh;
		margin-top: -80px;
		padding-top: 80px;
		display: flex;
		align-items: center;
		color: var(--color-white);
		text-align: center;
		overflow: hidden;
	}

	.hero-background {
		position: absolute;
		top: -80px;
		left: 0;
		right: 0;
		bottom: 0;
		background-image: url('https://images.unsplash.com/photo-1579165466741-7f35e4755660?q=80');
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		z-index: -2;
	}

	.hero-overlay {
		position: absolute;
		top: -80px;
		left: 0;
		right: 0;
		bottom: 0;
		background: linear-gradient(
			135deg,
			rgba(28, 61, 110, 0.95) 0%,
			rgba(0, 196, 180, 0.85) 100%
		);
		z-index: -1;
	}

	.hero h1 {
		font-size: 4.5rem;
		font-weight: 800;
		margin-bottom: 1.5rem;
		color: var(--color-white);
		text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
		line-height: 1.2;
	}

	.hero-subtitle {
		font-size: 1.75rem;
		margin-bottom: 2.5rem;
		opacity: 0.95;
		text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
	}

	/* Ventajas Section */
	.ventajas {
		padding: 6rem 0;
		background: var(--color-white);
	}

	.ventajas-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		gap: 2rem;
	}

	.ventaja-card {
		background: white;
		padding: 2.5rem;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		transition: all 0.3s ease;
		text-align: center;
	}

	.ventaja-card:hover {
		transform: translateY(-5px);
		box-shadow: 0 12px 24px rgba(28, 61, 110, 0.15);
	}

	.ventaja-icon {
		font-size: 3rem;
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		margin-bottom: 1.5rem;
	}

	.ventaja-card h3 {
		font-size: 1.8rem;
		color: var(--color-primary);
		margin-bottom: 1rem;
		font-weight: 700;
	}

	.ventaja-card p {
		font-size: 1.1rem;
		line-height: 1.6;
		color: var(--color-text);
	}

	/* Stats Section */
	.stats {
		padding: 6rem 0;
		background: linear-gradient(135deg, rgba(28, 61, 110, 0.05) 0%, rgba(0, 196, 180, 0.05) 100%);
	}

	.stats h2 {
		font-size: 3.2rem;
		font-weight: 800;
		text-align: center;
		margin-bottom: 3rem;
		color: var(--color-primary);
		position: relative;
		padding-bottom: 1rem;
	}

	.stats h2::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 50%;
		transform: translateX(-50%);
		width: 80px;
		height: 4px;
		background: linear-gradient(90deg, var(--color-primary), var(--color-secondary));
		border-radius: 2px;
	}

	.stats-grid {
		display: flex;
		justify-content: center;
		gap: 4rem;
		margin-top: 3rem;
	}

	.stat-circle {
		position: relative;
		width: 120px;
		height: 120px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.stat-value {
		position: relative;
		font-size: 2.5rem;
		font-weight: 800;
		color: var(--color-primary);
		z-index: 1;
	}

	.stat-ring {
		position: absolute;
		width: 120px;
		height: 120px;
		transform: rotate(-90deg);
	}

	.stat-ring circle {
		fill: none;
		stroke-width: 8;
		stroke-linecap: round;
		stroke-dasharray: 339.292;
		stroke-dashoffset: 339.292;
		transition: stroke-dashoffset 1s ease;
	}

	.stat-ring circle:first-child {
		stroke: rgba(28, 61, 110, 0.1);
	}

	.stat-ring circle:last-child {
		stroke: var(--color-secondary);
		stroke-dashoffset: calc(339.292 * (1 - var(--percent, 0) / 100));
	}

	.stat-label {
		font-size: 1.2rem;
		font-weight: 500;
		color: var(--color-primary);
		text-align: center;
		margin-top: 1rem;
		display: block;
	}

	/* CTA Section */
	.cta {
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		color: var(--color-white);
		text-align: center;
		padding: 6rem 0;
	}

	.cta h2 {
		font-size: 3.2rem;
		font-weight: 800;
		color: var(--color-white);
		margin-bottom: 1.5rem;
	}

	.cta p {
		font-size: 1.2rem;
		margin-bottom: 2rem;
		opacity: 0.9;
	}

	.cta-buttons {
		display: flex;
		gap: 1.5rem;
		justify-content: center;
		margin-top: 3rem;
	}

	.btn {
		display: inline-flex;
		align-items: center;
		gap: 0.75rem;
		padding: 1rem 2rem;
		font-size: 1.1rem;
		font-weight: 600;
		border-radius: 0.5rem;
		transition: all 0.3s ease;
		text-decoration: none;
	}

	.btn-primary {
		background: var(--color-white);
		color: var(--color-primary);
	}

	.btn-outline {
		border: 2px solid var(--color-white);
		color: var(--color-white);
	}

	.btn:hover {
		transform: translateY(-2px);
		box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
	}

	/* Responsive */
	@media (max-width: 768px) {
		.hero h1 {
			font-size: 3rem;
		}

		.hero-subtitle {
			font-size: 1.25rem;
		}

		.stats-grid {
			flex-direction: column;
			align-items: center;
			gap: 3rem;
		}

		.cta-buttons {
			flex-direction: column;
		}

		.btn {
			width: 100%;
			justify-content: center;
		}
	}
</style> 