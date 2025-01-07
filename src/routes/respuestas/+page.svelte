<script>
	import { fade, fly } from 'svelte/transition';

	// Lista de preguntas frecuentes
	const faqs = [
		{
			question: '¿Qué es el estudio molecular MIR-THYPE Full?',
			answer: 'Es un estudio de precisión que analiza nódulos tiroideos para determinar con alta precisión la probabilidad de malignidad, ayudando a evitar cirugías innecesarias.'
		},
		{
			question: '¿Cómo se obtiene la muestra para el estudio?',
			answer: 'Se utiliza la misma muestra de la primera punción (PAAF) realizada para el diagnóstico citológico, no se requieren punciones adicionales.'
		},
		{
			question: '¿Cuánto tiempo toma obtener los resultados?',
			answer: 'Los resultados están disponibles en menos de un mes, permitiendo una toma de decisiones oportuna.'
		},
		{
			question: '¿Qué tan preciso es el estudio?',
			answer: 'El estudio tiene un valor predictivo negativo del 96%, lo que significa una alta precisión en la detección de casos benignos.'
		},
		{
			question: '¿El estudio está avalado internacionalmente?',
			answer: 'Sí, el estudio está respaldado por consenso internacional y asociaciones médicas reconocidas.'
		}
	];
</script>

<svelte:head>
	<title>Respuestas - MedPre Ecuador</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</svelte:head>

<main>
	<!-- Hero Section -->
	<section class="hero">
		<div class="hero-background"></div>
		<div class="hero-overlay"></div>
		<div class="container">
			<div class="hero-content" in:fade={{ duration: 1000 }}>
				<h1>Preguntas Frecuentes</h1>
				<p class="hero-subtitle">
					Resolvemos tus dudas sobre el diagnóstico molecular de precisión
				</p>
			</div>
		</div>
	</section>

	<!-- FAQ Section -->
	<section class="faq">
		<div class="container">
			<div class="faq-grid">
				{#each faqs as faq, index}
					<div 
						class="faq-card"
						in:fly={{ y: 50, duration: 1000, delay: index * 200 }}
					>
						<div class="faq-icon">
							<i class="fas fa-question-circle"></i>
						</div>
						<h3>{faq.question}</h3>
						<p>{faq.answer}</p>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- Información Adicional -->
	<section class="additional-info">
		<div class="container">
			<h2>Información Importante</h2>
			<div class="info-cards">
				<div class="info-card">
					<div class="info-icon">
						<i class="fas fa-clipboard-check"></i>
					</div>
					<h3>Proceso Simple</h3>
					<p>No requiere procedimientos adicionales, utilizamos la muestra inicial de la punción.</p>
				</div>
				<div class="info-card">
					<div class="info-icon">
						<i class="fas fa-user-md"></i>
					</div>
					<h3>Consulta Gratuita</h3>
					<p>Incluye asesoría con especialistas para interpretar los resultados.</p>
				</div>
			</div>
		</div>
	</section>

	<!-- CTA Section -->
	<section class="cta">
		<div class="container">
			<div class="cta-content">
				<h2>¿Tienes más preguntas?</h2>
				<p>Nuestro equipo está disponible para resolver todas tus dudas</p>
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

	/* Hero Section con los mismos estilos que inicio */
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

	/* FAQ Section */
	.faq {
		padding: 6rem 0;
		background: var(--color-white);
	}

	.faq-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
		gap: 2rem;
	}

	.faq-card {
		background: white;
		padding: 2.5rem;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		transition: all 0.3s ease;
	}

	.faq-card:hover {
		transform: translateY(-5px);
		box-shadow: 0 12px 24px rgba(28, 61, 110, 0.15);
	}

	.faq-icon {
		font-size: 2.5rem;
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		margin-bottom: 1.5rem;
	}

	.faq-card h3 {
		font-size: 1.8rem;
		color: var(--color-primary);
		margin-bottom: 1rem;
		font-weight: 700;
	}

	.faq-card p {
		font-size: 1.1rem;
		line-height: 1.6;
		color: var(--color-text);
	}

	/* Información Adicional */
	.additional-info {
		background: linear-gradient(135deg, rgba(28, 61, 110, 0.05) 0%, rgba(0, 196, 180, 0.05) 100%);
		padding: 6rem 0;
	}

	.additional-info h2 {
		font-size: 3.2rem;
		font-weight: 800;
		text-align: center;
		margin-bottom: 3rem;
		color: var(--color-primary);
		position: relative;
		padding-bottom: 1rem;
	}

	.additional-info h2::after {
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

	.info-cards {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 3rem;
		margin-top: 3rem;
	}

	.info-card {
		background: white;
		padding: 2.5rem;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		transition: all 0.3s ease;
		text-align: center;
	}

	.info-card:hover {
		transform: translateY(-5px);
		box-shadow: 0 12px 24px rgba(28, 61, 110, 0.15);
	}

	.info-icon {
		font-size: 3rem;
		color: var(--color-secondary);
		margin-bottom: 1.5rem;
	}

	.info-card h3 {
		font-size: 1.8rem;
		color: var(--color-primary);
		margin-bottom: 1rem;
		font-weight: 700;
	}

	.info-card p {
		font-size: 1.1rem;
		line-height: 1.6;
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

		.info-cards {
			grid-template-columns: 1fr;
		}

		.faq-grid {
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