<script>
	import { fade, fly } from 'svelte/transition';
</script>

<svelte:head>
	<title>MedPre - Medicina de Precisión Ecuador</title>
	<meta name="description" content="Evaluación precisa de nódulos tiroideos mediante tecnología molecular avanzada en Ecuador" />
	<meta name="keywords" content="medicina de precisión, nódulos tiroideos, diagnóstico molecular, Ecuador" />
	<meta property="og:title" content="MedPre - Medicina de Precisión Ecuador" />
	<meta property="og:description" content="Evaluación precisa de nódulos tiroideos mediante tecnología molecular avanzada" />
	<meta property="og:image" content="https://images.unsplash.com/photo-1579165466741-7f35e4755660" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://medpre.vercel.app" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</svelte:head>

<main>
	<!-- Hero Section Simplificado -->
	<section class="hero">
		<div class="hero-background" style="background-image: url('https://images.unsplash.com/photo-1579165466741-7f35e4755660?q=80')"></div>
		<div class="hero-overlay"></div>
		<div class="container">
			<div class="hero-content" in:fade={{ duration: 1000 }}>
				<h1>Diagnóstico Molecular de Precisión</h1>
				<p class="hero-subtitle">
					Evaluación precisa de nódulos tiroideos mediante tecnología molecular avanzada
				</p>
				
				<!-- Stats mejorados -->
				<div class="hero-stats">
					<div class="hero-stat">
						<div class="stat-circle">
							<span class="stat-value">96%</span>
							<svg class="stat-ring">
								<circle cx="60" cy="60" r="54"></circle>
								<circle cx="60" cy="60" r="54" style="--percent: 96"></circle>
							</svg>
						</div>
						<span class="stat-label">Precisión diagnóstica</span>
					</div>
					<div class="hero-stat">
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

				<!-- Botones de acción -->
				<div class="hero-buttons">
					<a href="/contacto" class="btn btn-primary">
						<i class="fas fa-stethoscope"></i>
						Contáctanos
					</a>
					<a href="/quienes-somos" class="btn btn-outline">
						<i class="fas fa-users"></i>
						Conócenos
					</a>
				</div>
			</div>
		</div>
	</section>

	<!-- Sección de Proceso Médico -->
	<section class="process">
		<div class="container">
			<h2>Proceso Diagnóstico</h2>
			<div class="process-grid">
				<div class="process-step">
					<div class="step-number">1</div>
					<div class="step-icon">
						<i class="fas fa-notes-medical"></i>
					</div>
					<h3>Evaluación Inicial</h3>
					<p>Análisis de nódulos tiroideos grado III y IV según Bethesda</p>
				</div>
				<div class="process-step">
					<div class="step-number">2</div>
					<div class="step-icon">
						<i class="fas fa-vial"></i>
					</div>
					<h3>Estudio Molecular</h3>
					<p>Análisis MIR-THYPE Full con la muestra de la primera punción</p>
				</div>
				<div class="process-step">
					<div class="step-number">3</div>
					<div class="step-icon">
						<i class="fas fa-file-medical-alt"></i>
					</div>
					<h3>Resultados</h3>
					<p>Entrega de resultados precisos en menos de un mes</p>
				</div>
				<div class="process-step">
					<div class="step-number">4</div>
					<div class="step-icon">
						<i class="fas fa-user-md"></i>
					</div>
					<h3>Consulta Especializada</h3>
					<p>Asesoría gratuita con especialistas para interpretar resultados</p>
				</div>
			</div>
		</div>
	</section>

	<!-- Sección de Beneficios Clínicos -->
	<section class="benefits">
		<div class="container">
			<h2>Beneficios Clínicos</h2>
			<div class="benefits-grid">
				<div class="benefit-card">
					<i class="fas fa-shield-alt"></i>
					<h3>Alta Precisión</h3>
					<p>Valor predictivo negativo del 96% en la detección de malignidad</p>
				</div>
				<div class="benefit-card">
					<i class="fas fa-procedures"></i>
					<h3>Menos Cirugías</h3>
					<p>Reducción del 75% en cirugías innecesarias</p>
				</div>
				<div class="benefit-card">
					<i class="fas fa-clock"></i>
					<h3>Resultados Rápidos</h3>
					<p>Diagnóstico completo en menos de 30 días</p>
				</div>
				<div class="benefit-card">
					<i class="fas fa-certificate"></i>
					<h3>Respaldo Internacional</h3>
					<p>Avalado por consenso internacional y asociaciones médicas</p>
				</div>
			</div>
		</div>
	</section>

	<!-- Sección de Contacto Profesional -->
	<section class="contact">
		<div class="container">
			<div class="contact-content">
				<div class="contact-info">
					<h2>Consulta Profesional</h2>
					<p>Agenda una consulta con nuestros especialistas para evaluar tu caso</p>
					<div class="contact-methods">
						<a href="https://wa.me/593979136217" class="contact-method">
							<i class="fab fa-whatsapp"></i>
							<div>
								<h4>WhatsApp</h4>
								<span>(+593) 97 913 6217</span>
							</div>
						</a>
						<a href="mailto:medpre.ecuador@gmail.com" class="contact-method">
							<i class="fas fa-envelope"></i>
							<div>
								<h4>Correo Electrónico</h4>
								<span>medpre.ecuador@gmail.com</span>
							</div>
						</a>
						<div class="contact-method">
							<i class="fas fa-map-marker-alt"></i>
							<div>
								<h4>Ubicación</h4>
								<span>Quito, Ecuador</span>
							</div>
						</div>
					</div>
				</div>
				<div class="contact-image">
					<img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?q=80" 
						 alt="Consulta médica"
						 loading="lazy">
				</div>
			</div>
		</div>
	</section>
</main>

<style>
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

	/* Hero Section base */
	.hero {
		position: relative;
		height: 100vh;
		height: 100dvh;
		margin-top: -80px;
		padding-top: 80px;
		display: flex;
		align-items: center;
		color: var(--color-white);
		text-align: center;
		overflow: hidden;
	}

	.hero-background {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		width: 100%;
		height: 100vh;
		height: 100dvh;
		background-image: url('https://images.unsplash.com/photo-1579165466741-7f35e4755660?q=80');
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		z-index: -2;
	}

	.hero-overlay {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		width: 100%;
		height: 100vh;
		height: 100dvh;
		background: linear-gradient(
			135deg,
			rgba(28, 61, 110, 0.98) 0%,
			rgba(0, 196, 180, 0.95) 100%
		);
		z-index: -1;
	}

	.hero-content {
		position: relative;
		z-index: 10;
		width: 100%;
		padding: 2rem 0;
		margin-top: auto;
		margin-bottom: auto;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	/* Ajustes específicos para iPhone moderno */
	@supports (-webkit-touch-callout: none) {
		.hero {
			min-height: -webkit-fill-available;
			height: 100vh;
			display: flex;
			flex-direction: column;
			justify-content: center;
		}

		.hero-background,
		.hero-overlay {
			position: fixed;
			top: 0;
			left: 0;
			right: 0;
			bottom: 0;
			height: 100vh;
			min-height: -webkit-fill-available;
			z-index: 1;
		}

		.hero-content {
			position: relative;
			z-index: 10;
			padding: env(safe-area-inset-top) 1rem env(safe-area-inset-bottom);
			min-height: auto;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
		}

		.hero-buttons {
			position: relative;
			z-index: 10;
			width: 100%;
			padding: 0 1.5rem;
			margin-top: 2rem;
			margin-bottom: env(safe-area-inset-bottom, 1rem);
		}
	}

	/* Ajustes específicos para iPhone 14 Pro y similares */
	@media only screen and (device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3),
		   only screen and (device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3),
		   only screen and (device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3),
		   only screen and (device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) {
		.hero-content {
			padding-top: max(env(safe-area-inset-top), 2rem);
			padding-bottom: env(safe-area-inset-bottom, 2rem);
		}

		.hero-buttons {
			margin-bottom: max(env(safe-area-inset-bottom), 2rem);
		}

		.btn {
			position: relative;
			z-index: 10;
		}
	}

	/* Asegurarse de que el contenido esté siempre sobre el fondo */
	.hero-content * {
		position: relative;
		z-index: 2;
	}

	/* Ajustes para móviles */
	@media (max-width: 767px) {
		.hero {
			min-height: 100vh;
			min-height: 100dvh;
		}

		.hero-content {
			padding: 1rem 0;
			display: flex;
			flex-direction: column;
			justify-content: center;
			min-height: calc(100vh - 80px);
			min-height: calc(100dvh - 80px);
		}

		.hero-stats {
			margin: 2rem 0;
		}
	}

	/* Ajustes para iPhone */
	@supports (padding: env(safe-area-inset-top)) {
		.hero-background,
		.hero-overlay {
			padding-top: env(safe-area-inset-top);
			padding-bottom: env(safe-area-inset-bottom);
		}

		.hero-content {
			padding-top: max(env(safe-area-inset-top), 1rem);
			padding-bottom: max(env(safe-area-inset-bottom), 1rem);
		}
	}

	/* Ajustes generales para móviles */
	@media (max-width: 767px) {
		.hero {
			min-height: 100vh;
			height: auto;
			padding-bottom: 2rem;
		}

		.hero-content {
			padding: 2rem 0;
		}

		.hero h1 {
			font-size: 2.2rem;
			line-height: 1.2;
			margin-bottom: 1rem;
			padding: 0 1rem;
		}

		.hero-subtitle {
			font-size: 1.1rem;
			line-height: 1.4;
			padding: 0 1.2rem;
			margin-bottom: 1.5rem;
		}

		.hero-stats {
			flex-direction: row;
			flex-wrap: wrap;
			justify-content: center;
			gap: 1.5rem;
			padding: 1rem;
		}

		.hero-buttons {
			flex-direction: column;
			padding: 0 1.5rem;
			gap: 0.8rem;
		}

		.btn {
			padding: 0.8rem 1.5rem;
			font-size: 1rem;
		}
	}

	/* Ajustes para tablets */
	@media (min-width: 768px) and (max-width: 1024px) {
		.hero h1 {
			font-size: 3rem;
			padding: 0 2rem;
		}

		.hero-subtitle {
			font-size: 1.3rem;
			padding: 0 3rem;
		}

		.hero-stats {
			justify-content: center;
			gap: 2.5rem;
			padding: 2rem;
		}

		.stat-circle {
			width: 100px;
			height: 100px;
		}
	}

	/* Ajustes para notch y diseños con recortes */
	@supports (padding-top: env(safe-area-inset-top)) {
		.hero {
			padding-top: max(80px, env(safe-area-inset-top));
			padding-left: env(safe-area-inset-left);
			padding-right: env(safe-area-inset-right);
		}
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

	/* Stats Cards con nuevo esquema de color */
	.stat-card {
		background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
		padding: 2.5rem;
		text-align: center;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		transition: all 0.3s ease;
		border: 1px solid rgba(28, 61, 110, 0.1);
	}

	.stat-icon {
		font-size: 2.5rem;
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		margin-bottom: 1rem;
	}

	.stat-number {
		font-size: 3.5rem;
		font-weight: 800;
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		margin-bottom: 1rem;
	}

	.stat-card:hover {
		transform: translateY(-8px);
		box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
	}

	/* Feature Cards Mejorados */
	.feature-card {
		background: var(--color-white);
		padding: 2.5rem;
		text-align: center;
		border-radius: 1rem;
		transition: all 0.3s ease;
		box-shadow: 0 4px 6px rgba(28, 61, 110, 0.1);
		border: 1px solid rgba(28, 61, 110, 0.1);
	}

	.feature-icon {
		font-size: 2.5rem;
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		margin-bottom: 1.5rem;
	}

	.feature-card:hover {
		transform: translateY(-8px);
		box-shadow: 0 12px 24px rgba(28, 61, 110, 0.15);
		border: 1px solid rgba(0, 196, 180, 0.2);
	}

	/* CTA Section con gradiente mejorado */
	.cta {
		position: relative;
		padding: 8rem 0;
		color: var(--color-white);
		text-align: center;
		overflow: hidden;
	}

	.cta-background {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background-image: url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80');
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		z-index: -2;
	}

	.cta-overlay {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: linear-gradient(
			135deg,
			rgba(28, 61, 110, 0.97) 0%,
			rgba(0, 196, 180, 0.90) 100%
		);
		z-index: -1;
	}

	/* Buttons Mejorados */
	.btn {
		position: relative;
		z-index: 10;
		display: inline-flex;
		align-items: center;
		gap: 0.75rem;
		padding: 1rem 2rem;
		border-radius: 0.5rem;
		font-weight: 600;
		text-decoration: none;
		transition: all 0.3s ease;
	}

	.btn i {
		font-size: 1.2rem;
	}

	.btn-primary {
		background: var(--color-secondary);
		color: var(--color-white);
		box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
		border: none;
	}

	.btn-primary:hover {
		background: var(--color-white);
		color: var(--color-primary);
		transform: translateY(-2px);
	}

	.btn-outline {
		border: 2px solid var(--color-white);
		color: var(--color-white);
		background: transparent;
	}

	.btn-outline::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		width: 0;
		height: 100%;
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		transition: all 0.3s ease;
		z-index: -1;
	}

	.btn-outline:hover::before {
		width: 100%;
	}

	.btn-outline:hover {
		border-color: transparent;
		color: var(--color-white);
		transform: translateY(-2px);
	}

	/* Responsive ajustado */
	@media (max-width: 768px) {
		.hero h1 {
			font-size: 3rem;
		}

		.hero-subtitle {
			font-size: 1.25rem;
		}

		.hero-buttons,
		.cta-buttons {
			flex-direction: column;
		}

		.btn {
			width: 100%;
			justify-content: center;
		}
	}

	/* Efectos adicionales */
	.stat-card:hover,
	.feature-card:hover {
		background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
		border-color: rgba(0, 196, 180, 0.2);
	}

	@keyframes gradient {
		0% { background-position: 0% 50%; }
		50% { background-position: 100% 50%; }
		100% { background-position: 0% 50%; }
	}

	/* Nuevo estilo para el proceso médico */
	.process {
		padding: 6rem 0;
		background: linear-gradient(to bottom, #f8f9fa, #ffffff);
	}

	.process-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
		gap: 2rem;
		margin-top: 3rem;
	}

	.process-step {
		position: relative;
		background: white;
		padding: 2rem;
		border-radius: 1rem;
		box-shadow: 0 4px 6px rgba(28, 61, 110, 0.1);
		text-align: center;
		transition: all 0.3s ease;
	}

	.step-number {
		position: absolute;
		top: -1rem;
		left: 50%;
		transform: translateX(-50%);
		width: 2rem;
		height: 2rem;
		background: linear-gradient(135deg, #1C3D6E, #00C4B4);
		color: white;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-weight: bold;
	}

	.step-icon {
		font-size: 2.5rem;
		color: #00C4B4;
		margin: 1rem 0;
	}

	/* Beneficios clínicos */
	.benefits {
		background: var(--color-white);
		padding: 6rem 0;
	}

	.benefits-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
		gap: 2rem;
		margin-top: 3rem;
	}

	.benefit-card {
		background: white;
		padding: 2rem;
		border-radius: 1rem;
		box-shadow: 0 4px 6px rgba(28, 61, 110, 0.1);
		text-align: center;
		transition: all 0.3s ease;
	}

	.benefit-card i {
		font-size: 2.5rem;
		color: #1C3D6E;
		margin-bottom: 1rem;
	}

	/* Contacto profesional */
	.contact {
		background: linear-gradient(135deg, #1C3D6E, #00C4B4);
		padding: 6rem 0;
		color: white;
	}

	.contact-content {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 4rem;
		align-items: center;
	}

	.contact-methods {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
		margin-top: 2rem;
	}

	.contact-method {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 1rem;
		background: rgba(255, 255, 255, 0.1);
		border-radius: 0.5rem;
		color: white;
		text-decoration: none;
		transition: all 0.3s ease;
	}

	.contact-method:hover {
		background: rgba(255, 255, 255, 0.2);
		transform: translateX(5px);
	}

	.contact-method i {
		font-size: 2rem;
	}

	.contact-image img {
		width: 100%;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
		object-fit: cover;
		height: 100%;
		min-height: 400px;
	}

	/* Responsive */
	@media (max-width: 768px) {
		.contact-content {
			grid-template-columns: 1fr;
		}

		.contact-image {
			display: none;
		}
	}

	/* Estilos generales para títulos de sección */
	section h2 {
		font-size: 3.2rem;
		font-weight: 800;
		text-align: center;
		margin-bottom: 3rem;
		color: var(--color-primary);
		position: relative;
		padding-bottom: 1rem;
	}

	section h2::after {
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

	/* Títulos de cards más grandes */
	.process-step h3,
	.benefit-card h3 {
		font-size: 1.8rem;
		font-weight: 700;
		margin: 1.5rem 0 1rem;
		color: var(--color-primary);
	}

	/* Título de contacto en blanco */
	.contact h2 {
		color: var(--color-white);
	}

	.contact h2::after {
		background: linear-gradient(90deg, var(--color-white), rgba(255, 255, 255, 0.5));
	}

	/* Responsive */
	@media (max-width: 768px) {
		section h2 {
			font-size: 2.5rem;
		}

		.hero h1 {
			font-size: 3rem;
		}

		.process-step h3,
		.benefit-card h3 {
			font-size: 1.5rem;
		}
	}

	/* Hero Stats Mejorados */
	.hero-stats {
		display: flex;
		justify-content: center;
		gap: 4rem;
		margin: 3rem 0;
	}

	.hero-stat {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
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
		color: var(--color-white);
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
		stroke: rgba(255, 255, 255, 0.1);
	}

	.stat-ring circle:last-child {
		stroke: var(--color-secondary);
		stroke-dashoffset: calc(339.292 * (1 - var(--percent, 0) / 100));
	}

	.stat-label {
		font-size: 1.2rem;
		font-weight: 500;
		color: var(--color-white);
		text-align: center;
		max-width: 150px;
		line-height: 1.3;
	}

	/* Botones del Hero */
	.hero-buttons {
		position: relative;
		z-index: 10;
		display: flex;
		gap: 1.5rem;
		justify-content: center;
		margin-top: 2rem;
		width: 100%;
		padding: 0 1.5rem;
	}

	.btn {
		position: relative;
		z-index: 10;
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

	.btn i {
		font-size: 1.2rem;
	}

	.btn-primary {
		background: var(--color-secondary);
		color: var(--color-white);
		box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
	}

	.btn-primary:hover {
		background: var(--color-white);
		color: var(--color-primary);
		transform: translateY(-2px);
	}

	.btn-outline {
		border: 2px solid var(--color-white);
		color: var(--color-white);
		background: transparent;
	}

	.btn-outline:hover {
		background: var(--color-white);
		color: var(--color-primary);
		transform: translateY(-2px);
	}

	/* Responsive */
	@media (max-width: 768px) {
		.hero-stats {
			flex-direction: column;
			gap: 2rem;
		}

		.hero-buttons {
			flex-direction: column;
			gap: 1rem;
			padding: 0 1rem;
		}

		.btn {
			width: 100%;
			justify-content: center;
		}
	}

	/* Mejoras responsive para el hero */
	@media (max-width: 768px) {
		.hero h1 {
			font-size: 2.8rem;
			padding: 0 1rem;
		}

		.hero-subtitle {
			font-size: 1.2rem;
			padding: 0 1rem;
			margin-bottom: 2rem;
		}

		.hero-stats {
			flex-direction: row;
			gap: 1.5rem;
			padding: 0 1rem;
		}

		.stat-circle {
			width: 100px;
			height: 100px;
		}

		.stat-value {
			font-size: 2rem;
		}

		.stat-label {
			font-size: 1rem;
		}

		.hero-buttons {
			flex-direction: column;
			padding: 0 2rem;
		}

		.btn {
			width: 100%;
			margin-bottom: 0.5rem;
		}
	}

	/* Mejoras para tablets */
	@media (min-width: 769px) and (max-width: 1024px) {
		.hero h1 {
			font-size: 3.5rem;
		}

		.hero-subtitle {
			font-size: 1.5rem;
		}
	}

	/* Mejoras para secciones de contenido en móvil */
	@media (max-width: 768px) {
		.process-grid,
		.benefits-grid {
			grid-template-columns: 1fr;
			gap: 1.5rem;
			padding: 0 1rem;
		}

		.process-step,
		.benefit-card {
			padding: 1.5rem;
		}

		section h2 {
			font-size: 2.2rem;
			margin-bottom: 2rem;
		}

		.contact-content {
			grid-template-columns: 1fr;
			gap: 2rem;
			padding: 0 1rem;
		}

		.contact-methods {
			gap: 1rem;
		}

		.contact-method {
			padding: 0.8rem;
		}

		.contact-method i {
			font-size: 1.5rem;
		}
	}

	/* Ajustes para tablet */
	@media (min-width: 768px) and (max-width: 1024px) {
		.hero h1 {
			font-size: 3.2rem;
			padding: 0 2rem;
			margin-bottom: 1.5rem;
		}

		.hero-subtitle {
			font-size: 1.4rem;
			padding: 0 2rem;
			margin-bottom: 2rem;
		}

		.hero-stats {
			flex-direction: row;
			justify-content: center;
			gap: 3rem;
			padding: 2rem;
		}

		.stat-circle {
			width: 110px;
			height: 110px;
		}

		.hero-buttons {
			flex-direction: row;
			justify-content: center;
			gap: 1.5rem;
			padding: 0 2rem;
		}

		.process-grid,
		.benefits-grid {
			grid-template-columns: repeat(2, 1fr);
			gap: 2rem;
			padding: 0 2rem;
		}
	}

	/* Ajustes para móvil */
	@media (max-width: 767px) {
		.hero h1 {
			font-size: 2.5rem;
			padding: 0 1rem;
			margin-bottom: 1rem;
		}

		.hero-subtitle {
			font-size: 1.2rem;
			padding: 0 1rem;
			margin-bottom: 2rem;
		}

		.hero-stats {
			flex-direction: column;
			align-items: center;
			gap: 2rem;
			padding: 1rem;
		}

		.hero-buttons {
			flex-direction: column;
			padding: 0 1.5rem;
			gap: 1rem;
		}

		.btn {
			width: 100%;
			justify-content: center;
		}

		.process-grid,
		.benefits-grid {
			grid-template-columns: 1fr;
			gap: 1.5rem;
			padding: 0 1rem;
		}

		section h2 {
			font-size: 2rem;
			padding: 0 1rem;
		}
	}
</style>
