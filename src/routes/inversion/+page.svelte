<script>
	import { fade, fly } from 'svelte/transition';

	const beneficios = [
		{
			icon: 'microscope',
			title: 'Estudio Completo',
			description: 'Análisis molecular MIR-THYPE Full para nódulos tiroideos'
		},
		{
			icon: 'truck-fast',
			title: 'Envío Incluido',
			description: 'Traslado seguro de muestras a nivel nacional'
		},
		{
			icon: 'user-md',
			title: 'Consulta Especializada',
			description: 'Asesoría gratuita con especialistas para interpretar resultados'
		},
		{
			icon: 'file-medical',
			title: 'Resultados Detallados',
			description: 'Informe completo con recomendaciones específicas'
		}
	];
</script>

<svelte:head>
	<title>Inversión - MedPre Ecuador</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</svelte:head>

<main>
	<!-- Hero Section -->
	<section class="hero">
		<div class="hero-background"></div>
		<div class="hero-overlay"></div>
		<div class="container">
			<div class="hero-content" in:fade={{ duration: 1000 }}>
				<h1>Inversión en tu Salud</h1>
				<p class="hero-subtitle">
					Una decisión inteligente para tu bienestar y tranquilidad
				</p>
			</div>
		</div>
	</section>

	<!-- Precio Section -->
	<section class="precio">
		<div class="container">
			<div class="precio-card" in:fly={{ y: 50, duration: 1000 }}>
				<div class="precio-header">
					<h2>Estudio Molecular MIR-THYPE Full</h2>
					<div class="precio-amount">
						<span class="currency">$</span>
						<span class="amount">1,300</span>
					</div>
					<p class="precio-note">Precio incluye IVA</p>
				</div>
				<div class="precio-features">
					{#each beneficios as beneficio}
						<div class="feature-item">
							<i class="fas fa-{beneficio.icon}"></i>
							<div>
								<h3>{beneficio.title}</h3>
								<p>{beneficio.description}</p>
							</div>
						</div>
					{/each}
				</div>
			</div>
		</div>
	</section>

	<!-- Métodos de Pago -->
	<section class="payment">
		<div class="container">
			<h2>Facilidades de Pago</h2>
			<div class="payment-grid">
				<div class="payment-card">
					<div class="payment-icon">
						<i class="fas fa-credit-card"></i>
					</div>
					<h3>Tarjetas de Crédito</h3>
					<p>Aceptamos todas las tarjetas principales con opción a diferir</p>
				</div>
				<div class="payment-card">
					<div class="payment-icon">
						<i class="fas fa-university"></i>
					</div>
					<h3>Transferencia Bancaria</h3>
					<p>Transferencia directa a nuestra cuenta empresarial</p>
				</div>
			</div>
		</div>
	</section>

	<!-- CTA Section -->
	<section class="cta">
		<div class="container">
			<div class="cta-content">
				<h2>Comienza tu Diagnóstico</h2>
				<p>Contacta con nosotros para iniciar tu proceso</p>
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

	/* Precio Section */
	.precio {
		padding: 6rem 0;
		background: var(--color-white);
	}

	.precio-card {
		max-width: 800px;
		margin: 0 auto;
		background: white;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		overflow: hidden;
	}

	.precio-header {
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		color: white;
		padding: 3rem;
		text-align: center;
	}

	.precio-header h2 {
		font-size: 2.5rem;
		margin-bottom: 2rem;
		color: white;
	}

	.precio-amount {
		font-size: 4rem;
		font-weight: 800;
		line-height: 1;
		margin-bottom: 1rem;
	}

	.precio-note {
		font-size: 1.1rem;
		opacity: 0.9;
	}

	.precio-features {
		padding: 3rem;
	}

	.feature-item {
		display: flex;
		align-items: flex-start;
		gap: 1.5rem;
		margin-bottom: 2rem;
	}

	.feature-item i {
		font-size: 2rem;
		color: var(--color-secondary);
		flex-shrink: 0;
	}

	.feature-item h3 {
		font-size: 1.3rem;
		color: var(--color-primary);
		margin-bottom: 0.5rem;
	}

	.feature-item p {
		font-size: 1.1rem;
		color: var(--color-text);
	}

	/* Payment Section */
	.payment {
		padding: 6rem 0;
		background: linear-gradient(135deg, rgba(28, 61, 110, 0.05) 0%, rgba(0, 196, 180, 0.05) 100%);
	}

	.payment h2 {
		font-size: 3.2rem;
		font-weight: 800;
		text-align: center;
		margin-bottom: 3rem;
		color: var(--color-primary);
		position: relative;
		padding-bottom: 1rem;
	}

	.payment h2::after {
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

	.payment-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 3rem;
		max-width: 800px;
		margin: 0 auto;
	}

	.payment-card {
		background: white;
		padding: 2.5rem;
		border-radius: 1rem;
		text-align: center;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		transition: all 0.3s ease;
	}

	.payment-card:hover {
		transform: translateY(-5px);
		box-shadow: 0 12px 24px rgba(28, 61, 110, 0.15);
	}

	.payment-icon {
		font-size: 3rem;
		color: var(--color-secondary);
		margin-bottom: 1.5rem;
	}

	.payment-card h3 {
		font-size: 1.8rem;
		color: var(--color-primary);
		margin-bottom: 1rem;
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

		.precio-amount {
			font-size: 3rem;
		}

		.payment-grid {
			grid-template-columns: 1fr;
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