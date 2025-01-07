<script>
	const socialLinks = [
		{ name: 'Facebook', icon: '/icons/social/facebook.svg', url: '#' },
		{ name: 'Twitter', icon: '/icons/social/twitter.svg', url: '#' },
		{ name: 'Instagram', icon: '/icons/social/instagram.svg', url: '#' },
		{ name: 'LinkedIn', icon: '/icons/social/linkedin.svg', url: '#' },
		{ name: 'WhatsApp', icon: '/icons/social/whatsapp.svg', url: '#' }
	];
</script>

<footer class="footer">
	<div class="container">
		<div class="footer-content">
			<div class="footer-section">
				<img src="/images/logos/Logo_Color Vertical.png" alt="MedPre Logo" class="footer-logo" />
				<p>Tu salud, nuestra prioridad</p>
			</div>
			
			<div class="footer-section">
				<h3>Contacto</h3>
				<div class="contact-info">
					<p>
						<img src="/icons/misc/location.svg" alt="Ubicación" class="icon" />
						Dirección de la empresa
					</p>
					<p>
						<img src="/icons/misc/phone.svg" alt="Teléfono" class="icon" />
						+1 234 567 890
					</p>
					<p>
						<img src="/icons/misc/email.svg" alt="Email" class="icon" />
						contacto@medpre.com
					</p>
				</div>
			</div>
			
			<div class="footer-section">
				<h3>Síguenos</h3>
				<div class="social-links">
					{#each socialLinks as { name, icon, url }}
						<a href={url} target="_blank" rel="noopener noreferrer" class="social-link">
							<img src={icon} alt={name} class="social-icon" />
						</a>
					{/each}
				</div>
			</div>
		</div>
		
		<div class="footer-bottom">
			<p>&copy; {new Date().getFullYear()} MedPre. Todos los derechos reservados.</p>
		</div>
	</div>
</footer>

<style>
	.footer {
		background: var(--white);
		padding: 4rem 0 2rem;
		box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
	}

	.footer-content {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
		gap: 2rem;
		margin-bottom: 2rem;
	}

	.footer-section {
		padding: 1rem;
	}

	.footer-logo {
		max-width: 200px;
		margin-bottom: 1rem;
	}

	.contact-info p {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		margin-bottom: 0.5rem;
	}

	.icon {
		width: 20px;
		height: 20px;
		filter: brightness(0) saturate(100%) invert(47%) sepia(82%) saturate(4462%) hue-rotate(166deg) brightness(95%) contrast(101%);
	}

	.social-links {
		display: flex;
		gap: 1rem;
	}

	.social-link {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 40px;
		height: 40px;
		border-radius: 50%;
		background: var(--light-bg);
		transition: all 0.3s ease;
	}

	.social-link:hover {
		background: var(--primary-color);
	}

	.social-icon {
		width: 20px;
		height: 20px;
		filter: brightness(0) saturate(100%) invert(47%) sepia(82%) saturate(4462%) hue-rotate(166deg) brightness(95%) contrast(101%);
		transition: all 0.3s ease;
	}

	.social-link:hover .social-icon {
		filter: brightness(0) saturate(100%) invert(100%);
	}

	.footer-bottom {
		text-align: center;
		padding-top: 2rem;
		border-top: 1px solid var(--light-bg);
	}

	@media (max-width: 768px) {
		.footer-content {
			grid-template-columns: 1fr;
			text-align: center;
		}

		.footer-logo {
			margin: 0 auto 1rem;
		}

		.contact-info p {
			justify-content: center;
		}

		.social-links {
			justify-content: center;
		}
	}
</style> 