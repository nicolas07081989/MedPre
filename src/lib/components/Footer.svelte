<script>
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';

	let year = new Date().getFullYear();
	let isVisible = false;

	onMount(() => {
		isVisible = true;
	});
</script>

<footer 
	class="footer-container"
	in:fade={{duration: 1000, delay: 200}}
>
	<div class="footer-content">
		<div class="footer-section">
			<img 
				src="/images/logos/Logo_Color Vertical.png" 
				alt="Logo Vertical" 
				class="footer-logo"
			/>
		</div>

		<div class="footer-section">
			<h3>Contacto</h3>
			<ul>
				<li>
					<a href="mailto:medpre.ecuador@gmail.com">
						<i class="fas fa-envelope"></i>
						medpre.ecuador@gmail.com
					</a>
				</li>
				<li>
					<a href="https://wa.me/593979136217">
						<i class="fas fa-phone"></i>
						(+593) 97 913 6217
					</a>
				</li>
				<li>
					<i class="fas fa-map-marker-alt"></i>
					Quito, Ecuador
				</li>
			</ul>
		</div>

		<div class="footer-section">
			<h3>Enlaces Rápidos</h3>
			<ul>
				<li><a href="/">Inicio</a></li>
				<li><a href="/quienes-somos">Quiénes Somos</a></li>
				<li><a href="/inversion">Inversión</a></li>
				<li><a href="/contacto">Contacto</a></li>
			</ul>
		</div>

		<div class="footer-section">
			<h3>Síguenos</h3>
			<div class="social-links">
				<a 
					href="https://www.facebook.com/medpre.ec" 
					target="_blank" 
					rel="noopener noreferrer"
					aria-label="Síguenos en Facebook"
				>
					<i class="fab fa-facebook"></i>
				</a>
				<a 
					href="https://www.instagram.com/medpre.ec/?hl=es" 
					target="_blank" 
					rel="noopener noreferrer"
					aria-label="Síguenos en Instagram"
				>
					<i class="fab fa-instagram"></i>
				</a>
			</div>
		</div>
	</div>

	<div class="footer-bottom">
		<p>&copy; {year} MedPre. Todos los derechos reservados.</p>
	</div>
</footer>

<style>
	.footer-container {
		background: linear-gradient(to right, #1a1a1a, #2d2d2d);
		color: #ffffff;
		padding: 4rem 2rem 1rem 2rem;
		margin-top: 0;
	}

	.footer-content {
		max-width: 1200px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
			gap: 2rem;
	}

	.footer-section {
		padding: 1rem;
	}

	.footer-logo {
		max-width: 200px;
		height: auto;
		margin-bottom: 1rem;
	}

	h3 {
		color: #ffffff;
		font-size: 1.2rem;
		margin-bottom: 1.5rem;
		position: relative;
	}

	h3::after {
		content: '';
		position: absolute;
		left: 0;
		bottom: -0.5rem;
		width: 50px;
		height: 2px;
		background: var(--primary-color, #4a90e2);
	}

	ul {
		list-style: none;
		padding: 0;
	}

	li {
		margin-bottom: 1rem;
	}

	a {
		color: #ffffff;
		text-decoration: none;
		transition: color 0.3s ease;
		display: inline-flex;
		align-items: center;
		gap: 0.5rem;
	}

	a:hover {
		color: var(--primary-color, #4a90e2);
	}

	.social-links {
		display: flex;
		gap: 1.5rem;
	}

	.social-links a {
		background: rgba(255, 255, 255, 0.1);
		width: 45px;
		height: 45px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		transition: all 0.3s ease;
		position: relative;
		overflow: hidden;
	}

	.social-links a i {
		font-size: 1.5rem;
		position: relative;
		z-index: 2;
		transition: all 0.3s ease;
	}

	.social-links a::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: var(--gradient-primary);
		opacity: 0;
		transition: all 0.3s ease;
		z-index: 1;
	}

	.social-links a:hover {
		transform: translateY(-5px);
		box-shadow: 0 5px 15px rgba(0, 196, 180, 0.3);
	}

	.social-links a:hover::before {
		opacity: 1;
	}

	.social-links a:hover i {
		color: #ffffff;
		transform: scale(1.2);
	}

	/* Estilos específicos para cada red social */
	.social-links a:nth-child(1):hover {
		box-shadow: 0 5px 15px rgba(66, 103, 178, 0.4); /* Facebook blue */
	}

	.social-links a:nth-child(2):hover {
		box-shadow: 0 5px 15px rgba(225, 48, 108, 0.4); /* Instagram gradient */
	}

	.footer-bottom {
		text-align: center;
		padding-top: 2rem;
		margin-top: 2rem;
		border-top: 1px solid rgba(255, 255, 255, 0.1);
	}

	@media (max-width: 768px) {
		.footer-container {
			padding: 3rem 1rem 1rem;
		}

		.footer-content {
			grid-template-columns: 1fr;
			text-align: center;
			gap: 2.5rem;
		}

		.footer-section {
			padding: 0;
		}

		.footer-logo {
			max-width: 180px;
			margin: 0 auto 1rem;
		}

		h3 {
			font-size: 1.4rem;
			margin-bottom: 1.2rem;
		}

		h3::after {
			left: 50%;
			transform: translateX(-50%);
			width: 60px;
		}

		ul {
			display: flex;
			flex-direction: column;
			align-items: center;
			gap: 0.8rem;
		}

		li {
			margin-bottom: 0;
		}

		a {
			font-size: 1.1rem;
			padding: 0.5rem;
		}

		.social-links {
			justify-content: center;
			gap: 1.5rem;
		}

		.social-links a {
			width: 45px;
			height: 45px;
			font-size: 1.2rem;
		}

		.footer-bottom {
			margin-top: 2rem;
			padding-top: 1.5rem;
		}

		.footer-bottom p {
			font-size: 0.9rem;
		}
	}

	/* Mejoras para tablets */
	@media (min-width: 769px) and (max-width: 1024px) {
		.footer-content {
			grid-template-columns: repeat(2, 1fr);
			gap: 3rem;
		}

		.footer-section:first-child {
			grid-column: 1 / -1;
			text-align: center;
		}

		.footer-logo {
			margin: 0 auto;
		}
	}

	/* Mejoras generales de interacción */
	.footer-section ul li a {
		position: relative;
		padding: 0.3rem 0;
	}

	.footer-section ul li a::after {
		content: '';
		position: absolute;
		width: 0;
		height: 2px;
		bottom: 0;
		left: 50%;
		background: var(--primary-color, #4a90e2);
		transition: all 0.3s ease;
		transform: translateX(-50%);
	}

	.footer-section ul li a:hover::after {
		width: 100%;
	}

	.social-links a {
		position: relative;
		overflow: hidden;
	}

	.social-links a::before {
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background: var(--primary-color, #4a90e2);
		transform: scale(0);
		transition: transform 0.3s ease;
		border-radius: 50%;
		z-index: -1;
	}

	.social-links a:hover::before {
		transform: scale(1);
	}
</style> 