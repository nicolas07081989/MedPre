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
					href="https://linkedin.com/company/tu-empresa" 
					target="_blank" 
					rel="noopener noreferrer"
					aria-label="Síguenos en LinkedIn"
				>
					<i class="fab fa-linkedin"></i>
				</a>
				<a 
					href="https://facebook.com/tu-pagina" 
					target="_blank" 
					rel="noopener noreferrer"
					aria-label="Síguenos en Facebook"
				>
					<i class="fab fa-facebook"></i>
				</a>
				<a 
					href="https://instagram.com/tu-cuenta" 
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
		gap: 1rem;
	}

	.social-links a {
		background: rgba(255, 255, 255, 0.1);
		width: 40px;
		height: 40px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		transition: all 0.3s ease;
	}

	.social-links a:hover {
		background: var(--primary-color, #4a90e2);
		transform: translateY(-3px);
	}

	.footer-bottom {
		text-align: center;
		padding-top: 2rem;
		margin-top: 2rem;
		border-top: 1px solid rgba(255, 255, 255, 0.1);
	}

	@media (max-width: 768px) {
		.footer-content {
			grid-template-columns: 1fr;
		}

		.footer-section {
			text-align: center;
		}

		h3::after {
			left: 50%;
			transform: translateX(-50%);
		}

		.social-links {
			justify-content: center;
		}
	}
</style> 