<script>
	import { fade, fly } from 'svelte/transition';
</script>

<svelte:head>
	<title>Quiénes Somos - MedPre Ecuador</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</svelte:head>

<main>
	<!-- Hero Section -->
	<section class="hero">
		<div class="hero-background"></div>
		<div class="hero-overlay"></div>
		<div class="container">
			<div class="hero-content" in:fade={{ duration: 1000 }}>
				<h1>Quiénes Somos</h1>
				<p class="hero-subtitle">
					Medicina de Precisión Ecuador - Fundada a finales del 2024
				</p>
			</div>
		</div>
	</section>

	<!-- Misión y Visión -->
	<section class="mission-vision">
		<div class="container">
			<div class="mission-vision-grid">
				<div class="mission-card" in:fly={{ y: 50, duration: 1000, delay: 200 }}>
					<div class="card-icon">
						<i class="fas fa-bullseye"></i>
					</div>
					<h2>Misión</h2>
					<p>
						Ayudar a pacientes con nódulos de tiroides a descubrir con certeza la posibilidad de desarrollar 
						cáncer, evitando cirugías innecesarias mediante estudios moleculares de precisión.
					</p>
				</div>
				<div class="vision-card" in:fly={{ y: 50, duration: 1000, delay: 400 }}>
					<div class="card-icon">
						<i class="fas fa-binoculars"></i>
					</div>
					<h2>Visión</h2>
					<p>
						Entre 2025 y 2030, realizar más de 500 estudios accesibles a la población ecuatoriana, 
						contribuyendo significativamente a la salud de nuestros pacientes.
					</p>
				</div>
			</div>
		</div>
	</section>

	<!-- Información Médica -->
	<section class="medical-info">
		<div class="container">
			<h2>Información Médica</h2>
			<div class="info-grid">
				<div class="info-card">
					<div class="info-icon">
						<i class="fas fa-microscope"></i>
					</div>
					<h3>Nódulos Tiroideos</h3>
					<p>Especialización en el análisis de nódulos tiroideos grado III y IV según Bethesda.</p>
				</div>
				<div class="info-card">
					<div class="info-icon">
						<i class="fas fa-chart-pie"></i>
					</div>
					<h3>Estadísticas</h3>
					<p>Solo 2 de cada 10 nódulos operados resultan malignos. El 80% de los nódulos podrían evitar la cirugía.</p>
				</div>
			</div>
		</div>
	</section>

	<!-- Nuestro Equipo -->
	<section class="team">
		<div class="container">
			<h2>Equipo Especializado</h2>
			<div class="team-content">
				<div class="team-text">
					<p>
						Contamos con un equipo de profesionales altamente capacitados en medicina molecular y diagnóstico 
						de precisión, respaldados por años de experiencia y formación internacional.
					</p>
					<ul class="team-features">
						<li>
							<i class="fas fa-check-circle"></i>
							Especialistas en diagnóstico molecular
						</li>
						<li>
							<i class="fas fa-check-circle"></i>
							Experiencia en patología tiroidea
						</li>
						<li>
							<i class="fas fa-check-circle"></i>
							Formación continua y actualización
						</li>
						<li>
							<i class="fas fa-check-circle"></i>
							Compromiso con la excelencia médica
						</li>
					</ul>
				</div>
			</div>
		</div>
	</section>

	<!-- CTA Section -->
	<section class="cta">
		<div class="container">
			<div class="cta-content">
				<h2>¿Necesitas más información?</h2>
				<p>Nuestro equipo está listo para atender todas tus consultas</p>
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

	/* Estilos de sección */
	section {
		padding: 6rem 0;
	}

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

	/* Misión y Visión */
	.mission-vision {
		background: var(--color-white);
	}

	.mission-vision-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 3rem;
	}

	.mission-card,
	.vision-card {
		background: white;
		padding: 3rem;
		border-radius: 1rem;
		box-shadow: 0 8px 16px rgba(28, 61, 110, 0.1);
		text-align: center;
		transition: all 0.3s ease;
	}

	.mission-card:hover,
	.vision-card:hover {
		transform: translateY(-5px);
		box-shadow: 0 12px 24px rgba(28, 61, 110, 0.15);
	}

	.card-icon {
		font-size: 3.5rem;
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		-webkit-background-clip: text;
		background-clip: text;
		color: transparent;
		margin-bottom: 1.5rem;
	}

	/* Información Médica */
	.medical-info {
		background: linear-gradient(135deg, rgba(28, 61, 110, 0.05) 0%, rgba(0, 196, 180, 0.05) 100%);
	}

	.info-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 3rem;
	}

	.info-card {
		background: white;
		padding: 2.5rem;
		border-radius: 1rem;
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
		font-size: 1.8rem;
		margin-bottom: 1rem;
		color: var(--color-primary);
	}

	/* Equipo */
	.team {
		background: var(--color-white);
	}

	.team-content {
		max-width: 800px;
		margin: 0 auto;
	}

	.team-features {
		list-style: none;
		padding: 0;
		margin-top: 2rem;
	}

	.team-features li {
		display: flex;
		align-items: center;
		gap: 1rem;
		margin-bottom: 1.5rem;
		font-size: 1.2rem;
		padding: 1rem;
		background: linear-gradient(135deg, rgba(28, 61, 110, 0.05) 0%, rgba(0, 196, 180, 0.05) 100%);
		border-radius: 0.5rem;
		transition: all 0.3s ease;
	}

	.team-features li:hover {
		transform: translateX(10px);
		background: linear-gradient(135deg, rgba(28, 61, 110, 0.1) 0%, rgba(0, 196, 180, 0.1) 100%);
	}

	.team-features i {
		font-size: 1.5rem;
		color: var(--color-secondary);
	}

	/* CTA Section */
	.cta {
		background: linear-gradient(135deg, #1C3D6E 0%, #00C4B4 100%);
		color: var(--color-white);
		text-align: center;
	}

	.cta h2 {
		color: var(--color-white);
	}

	.cta h2::after {
		background: linear-gradient(90deg, var(--color-white), rgba(255, 255, 255, 0.5));
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

		section h2 {
			font-size: 2.5rem;
		}

		.mission-vision-grid,
		.info-grid {
			grid-template-columns: 1fr;
			gap: 2rem;
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