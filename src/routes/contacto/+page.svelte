<script>
	import { fade, fly } from 'svelte/transition';

	const contactInfo = [
		{
			icon: 'brands/whatsapp',
			title: 'WhatsApp',
			description: '(+593) 97 913 6217',
			link: 'https://wa.me/593979136217'
		},
		{
			icon: 'envelope',
			title: 'Email',
			description: 'medpre.ecuador@gmail.com',
			link: 'mailto:medpre.ecuador@gmail.com'
		},
		{
			icon: 'clock',
			title: 'Horario de Atención',
			description: 'Lunes a Viernes: 9:00 - 18:00'
		},
		{
			icon: 'location-dot',
			title: 'Ubicación',
			description: 'Guayaquil, Ecuador'
		}
	];
</script>

<svelte:head>
	<title>Contacto - MedPre Ecuador</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</svelte:head>

<main>
	<!-- Hero Section -->
	<section class="hero">
		<div class="hero-background"></div>
		<div class="hero-overlay"></div>
		<div class="container">
			<div class="hero-content" in:fade={{ duration: 1000 }}>
				<h1>Contáctanos</h1>
				<p class="hero-subtitle">
					Estamos aquí para resolver todas tus dudas
				</p>
			</div>
		</div>
	</section>

	<!-- Contact Info Section -->
	<section class="contact-info">
		<div class="container">
			<div class="info-grid">
				{#each contactInfo as info, index}
					<div 
						class="info-card"
						in:fly={{ y: 50, duration: 1000, delay: index * 200 }}
					>
						<div class="info-icon">
							<i class={info.icon.includes('brands/') ? 
								`fab fa-${info.icon.split('/')[1]}` : 
								`fas fa-${info.icon}`}></i>
						</div>
						<h3>{info.title}</h3>
						{#if info.link}
							<a href={info.link} class="info-link">{info.description}</a>
						{:else}
							<p>{info.description}</p>
						{/if}
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- Contact Form Section -->
	<section class="contact-form">
		<div class="container">
			<h2>Envíanos un Mensaje</h2>
			<div class="form-container" in:fly={{ y: 50, duration: 1000 }}>
				<form>
					<div class="form-group">
						<label for="name">Nombre Completo</label>
						<input type="text" id="name" required>
					</div>
					<div class="form-group">
						<label for="email">Correo Electrónico</label>
						<input type="email" id="email" required>
					</div>
					<div class="form-group">
						<label for="phone">Teléfono</label>
						<input type="tel" id="phone" required>
					</div>
					<div class="form-group">
						<label for="message">Mensaje</label>
						<textarea id="message" rows="5" required></textarea>
					</div>
					<button type="submit" class="btn btn-primary">
						<i class="fas fa-paper-plane"></i>
						Enviar Mensaje
					</button>
				</form>
			</div>
		</div>
	</section>

	<!-- CTA Section -->
	<section class="cta">
		<div class="container">
			<div class="cta-content">
				<h2>¿Prefieres una respuesta inmediata?</h2>
				<p>Contáctanos directamente por WhatsApp o correo electrónico</p>
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

	/* Contact Info Section */
	.contact-info {
		padding: 6rem 0;
		background: var(--color-white);
	}

	.info-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 2rem;
	}

	.info-card {
		background: white;
		padding: 2.5rem;
		border-radius: 1rem;
		text-align: center;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		transition: all 0.3s ease;
	}

	.info-card:hover {
		transform: translateY(-5px);
		box-shadow: 0 12px 24px rgba(28, 61, 110, 0.15);
	}

	.info-icon {
		font-size: 2.5rem;
		color: var(--color-secondary);
		margin-bottom: 1.5rem;
	}

	.info-card h3 {
		font-size: 1.5rem;
		color: var(--color-primary);
		margin-bottom: 1rem;
	}

	.info-card p,
	.info-link {
		font-size: 1.1rem;
		color: var(--color-text);
		text-decoration: none;
		transition: color 0.3s ease;
	}

	.info-link:hover {
		color: var(--color-secondary);
	}

	/* Contact Form Section */
	.contact-form {
		padding: 6rem 0;
		background: linear-gradient(135deg, rgba(28, 61, 110, 0.05) 0%, rgba(0, 196, 180, 0.05) 100%);
	}

	.contact-form h2 {
		font-size: 3.2rem;
		font-weight: 800;
		text-align: center;
		margin-bottom: 3rem;
		color: var(--color-primary);
		position: relative;
		padding-bottom: 1rem;
	}

	.contact-form h2::after {
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

	.form-container {
		max-width: 800px;
		margin: 0 auto;
		background: white;
		padding: 3rem;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
	}

	.form-group {
		margin-bottom: 1.5rem;
	}

	label {
		display: block;
		font-size: 1.1rem;
		color: var(--color-primary);
		margin-bottom: 0.5rem;
	}

	input,
	textarea {
		width: 100%;
		padding: 1rem;
		border: 2px solid rgba(28, 61, 110, 0.1);
		border-radius: 0.5rem;
		font-size: 1.1rem;
		transition: all 0.3s ease;
	}

	input:focus,
	textarea:focus {
		outline: none;
		border-color: var(--color-secondary);
		box-shadow: 0 0 0 3px rgba(0, 196, 180, 0.1);
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
		border: none;
		cursor: pointer;
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

		.info-grid {
			grid-template-columns: 1fr;
		}

		.form-container {
			padding: 2rem;
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