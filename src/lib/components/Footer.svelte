<script>
  import { page } from '$app/stores';
  import { base } from '$app/paths';
</script>

<footer class="footer">
  <div class="footer-content">
    <div class="footer-main">
      <div class="footer-brand">
        <div class="footer-logo">
          <a href="/" class="logo-link">
            <img src="{base}/assets/Logo_Blanco.png" alt="MedPre Logo" class="logo-image" />
          </a>
        </div>
        <p class="brand-description">
          Líder en diagnóstico molecular de precisión para tiroides en Ecuador.
          Tecnología de vanguardia para resultados confiables.
        </p>
      </div>

      <!-- Enlaces rápidos -->
      <div class="footer-links">
        <h3>Enlaces Rápidos</h3>
        <ul>
          <li>
            <a sveltekit:prefetch href="{base}/">
              <i class="fas fa-home"></i>
              Inicio
            </a>
          </li>
          <li>
            <a sveltekit:prefetch href="{base}/quienes-somos">
              <i class="fas fa-users"></i>
              Quiénes Somos
            </a>
          </li>
          <li>
            <a sveltekit:prefetch href="{base}/respuestas">
              <i class="fas fa-question-circle"></i>
              Respuestas
            </a>
          </li>
          <li>
            <a sveltekit:prefetch href="{base}/ventajas">
              <i class="fas fa-star"></i>
              Ventajas
            </a>
          </li>
          <li>
            <a sveltekit:prefetch href="{base}/inversion">
              <i class="fas fa-dollar-sign"></i>
              Inversión
            </a>
          </li>
        </ul>
      </div>

      <!-- Información de contacto -->
      <div class="footer-contact">
        <h3>Contacto</h3>
        <ul>
          <li>
            <i class="fas fa-map-marker-alt"></i>
            <a href="https://goo.gl/maps/xyz" target="_blank" rel="noopener noreferrer">
              Quito, Ecuador
            </a>
          </li>
          <li>
            <i class="fas fa-phone"></i>
            <a href="tel:+59397913621">+593 97 913 621</a>
          </li>
          <li>
            <i class="fas fa-envelope"></i>
            <a href="mailto:medpre.ecuador@gmail.com">medpre.ecuador@gmail.com</a>
          </li>
        </ul>
      </div>

      <!-- Newsletter -->
      <div class="footer-newsletter">
        <h3>Mantente Informado</h3>
        <p>Suscríbete para recibir actualizaciones y noticias importantes.</p>
        <a 
          href="mailto:medpre.ecuador@gmail.com"
          class="subscribe-button"
          target="_blank"
          rel="noopener noreferrer"
        >
          <i class="fas fa-envelope"></i>
          Suscribirse al Newsletter
        </a>
      </div>
    </div>

    <!-- Redes sociales -->
    <div class="footer-social">
      <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" class="social-link">
        <i class="fab fa-facebook-f"></i>
      </a>
      <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="social-link">
        <i class="fab fa-instagram"></i>
      </a>
      <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="social-link">
        <i class="fab fa-linkedin-in"></i>
      </a>
      <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" class="social-link">
        <i class="fab fa-twitter"></i>
      </a>
    </div>

    <!-- Línea divisoria -->
    <div class="footer-divider"></div>

    <!-- Footer inferior -->
    <div class="footer-bottom">
      <p class="copyright">
        © {new Date().getFullYear()} MedPre. Todos los derechos reservados.
      </p>
      <div class="legal-links">
        <a href="/privacidad" on:click|preventDefault={(e) => handleNavigation(e, { href: '/privacidad' })}>
          Política de Privacidad
        </a>
        <span class="separator">|</span>
        <a href="/terminos" on:click|preventDefault={(e) => handleNavigation(e, { href: '/terminos' })}>
          Términos y Condiciones
        </a>
      </div>
    </div>
  </div>
</footer>

<style>
  .footer {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: var(--white);
    padding: 4rem 0 2rem;
    position: relative;
    margin-top: -50px;
  }

  .footer::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 100%;
    background-image: url("data:image/svg+xml,%3Csvg width='24' height='40' viewBox='0 0 24 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 40c5.523 0 10-4.477 10-10V10C10 4.477 5.523 0 0 0h24c0 5.523-4.477 10-10 10v20c5.523 0 10 4.477 10 10H0z' fill='%230CBAB8' fill-opacity='0.05' fill-rule='evenodd'/%3E%3C/svg%3E");
    opacity: 0.1;
  }

  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
  }

  .footer-main {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 2fr;
    gap: 3rem;
    margin-bottom: 3rem;
  }

  .footer-brand {
    max-width: 300px;
  }

  .footer-logo {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
  }

  .brand-description {
    color: rgba(255, 255, 255, 0.8);
    line-height: 1.6;
  }

  .footer h3 {
    color: var(--white);
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
    position: relative;
    padding-bottom: 0.5rem;
    font-family: var(--font-primary);
    font-weight: var(--font-weight-semibold);
  }

  .footer h3::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 30px;
    height: 2px;
    background: var(--secondary-color);
  }

  .footer-links ul,
  .footer-contact ul {
    list-style: none;
    padding: 0;
  }

  .footer-links li,
  .footer-contact li {
    margin-bottom: 1rem;
  }

  .footer-links a,
  .footer-contact a {
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-primary);
    font-weight: var(--font-weight-medium);
    width: 100%;
    padding: 0.5rem 0;
  }

  .footer-links a i,
  .footer-contact a i {
    color: rgba(255, 255, 255, 0.8);
    opacity: 0.8;
    width: 20px;
    text-align: center;
    transition: all 0.3s ease;
  }

  .footer-links a:hover,
  .footer-contact a:hover {
    color: var(--secondary-color);
    transform: translateX(5px);
  }

  .footer-links a:hover i,
  .footer-contact a:hover i {
    color: #0CBAB8;
    opacity: 1;
  }

  .footer-contact li {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1rem;
  }

  .footer-contact i {
    width: 20px;
    text-align: center;
    color: inherit;
  }

  .newsletter-form {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
  }

  .newsletter-input {
    flex: 1;
    padding: 0.8rem 1rem;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 4px;
    color: white;
    font-family: inherit;
    font-size: 1rem;
  }

  .newsletter-input::placeholder {
    color: rgba(255, 255, 255, 0.6);
  }

  .newsletter-form button {
    padding: 0.8rem 1.5rem;
    background: white;
    color: var(--primary-color);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
    font-family: inherit;
    font-size: 1rem;
  }

  .newsletter-form button:hover {
    background: #0CBAB8;
    color: white;
  }

  .footer-social {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin: 2rem 0;
  }

  .social-link {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
  }

  .social-link .fab {
    color: rgba(255, 255, 255, 0.8);
    font-size: 1.2rem;
    transition: all 0.3s ease;
  }

  .social-link:hover .fab {
    color: #0CBAB8;
    transform: translateY(-2px);
  }

  .social-link:hover {
    background: rgba(255, 255, 255, 0.1);
  }

  .footer-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--white), transparent);
    margin: 2rem 0;
    opacity: 0.1;
  }

  .footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: rgba(255, 255, 255, 0.8);
    font-size: 0.9rem;
  }

  .legal-links {
    display: flex;
    gap: 1rem;
    align-items: center;
  }

  .legal-links a {
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    transition: all 0.3s ease;
  }

  .legal-links a:hover {
    color: var(--secondary-color);
  }

  .separator {
    color: rgba(255, 255, 255, 0.4);
  }

  @media (max-width: 968px) {
    .footer-main {
      grid-template-columns: 1fr 1fr;
      gap: 2rem;
    }

    .footer-brand {
      grid-column: 1 / -1;
      max-width: none;
    }
  }

  @media (max-width: 576px) {
    .footer-main {
      grid-template-columns: 1fr;
    }

    .footer-bottom {
      flex-direction: column;
      text-align: center;
      gap: 1rem;
    }

    .newsletter-form {
      flex-direction: column;
    }

    .newsletter-form button {
      width: 100%;
    }
  }

  .logo-link {
    display: inline-flex;
    align-items: center;
    text-decoration: none;
    transition: opacity 0.3s ease;
  }

  .logo-link:hover {
    opacity: 0.9;
  }

  .logo-image {
    height: 70px;
    width: auto;
    object-fit: contain;
    transition: all 0.4s ease;
    filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.2));
  }

  .logo-link:hover .logo-image {
    transform: scale(1.03);
    filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.3));
  }

  .logo-image path {
    transition: all 0.4s ease;
  }

  .logo-link:hover .logo-image path {
    stroke-width: 22px;
    filter: brightness(1.2);
  }

  .logo-image text {
    transition: all 0.4s ease;
  }

  .logo-link:hover .logo-image text {
    filter: brightness(1.2) drop-shadow(0 0 8px rgba(255, 255, 255, 0.4));
  }

  @media (max-width: 1024px) {
    .logo-image {
      height: 60px;
    }
  }

  @media (max-width: 768px) {
    .logo-image {
      height: 50px;
    }
  }

  @media (max-width: 576px) {
    .logo-image {
      height: 45px;
    }
  }

  .footer-logo svg path {
    stroke: var(--white);
  }

  .footer-logo svg text {
    fill: var(--white);
  }

  .footer-links a,
  .footer-contact a {
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 0;
    transition: all 0.3s ease;
  }

  .footer-links a::before,
  .footer-contact a::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 1px;
    background: var(--secondary-color);
    transition: width 0.3s ease;
  }

  .footer-links a:hover::before,
  .footer-contact a:hover::before {
    width: 100%;
  }

  .footer-contact i {
    color: var(--secondary-color);
  }

  /* Enlaces del footer */
  .footer-links a,
  .footer-contact a,
  .legal-links a {
    color: rgba(255, 255, 255, 0.9);
    transition: all 0.3s ease;
  }

  .footer-links a:hover,
  .footer-contact a:hover,
  .legal-links a:hover {
    color: #0CBAB8;
    transform: translateX(5px);
  }

  /* Iconos */
  .footer-links a i,
  .footer-contact a i {
    color: rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
  }

  .footer-links a:hover i,
  .footer-contact a:hover i {
    color: #0CBAB8;
  }

  /* Redes sociales */
  .social-link {
    background: rgba(255, 255, 255, 0.1);
  }

  .social-link:hover {
    background: #0CBAB8;
    color: white;
    transform: translateY(-3px);
  }

  /* Botón newsletter */
  .newsletter-form button {
    background: rgba(255, 255, 255, 0.9);
    color: var(--primary-color);
  }

  .newsletter-form button:hover {
    background: #0CBAB8;
    color: white;
    transform: translateY(-2px);
  }

  /* Línea de subrayado */
  .footer-links a::before,
  .footer-contact a::before {
    background: #0CBAB8;
  }

  /* Iconos de contacto y enlaces rápidos */
  .footer-links i,
  .footer-contact i {
    color: rgba(255, 255, 255, 0.8);
    width: 20px;
    text-align: center;
    transition: all 0.3s ease;
  }

  /* Hover de los iconos */
  .footer-links a:hover i,
  .footer-contact a:hover i,
  .footer-contact li:hover i {
    color: #0CBAB8;
  }

  /* Remover estilos anteriores que puedan interferir */
  .footer-contact i {
    color: rgba(255, 255, 255, 0.8); /* Color base igual para todos */
  }

  .subscribe-button {
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.8rem 1.5rem;
    background: white;
    color: var(--primary-color);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
  }

  .subscribe-button:hover {
    background: #0CBAB8;
    color: white;
    transform: translateY(-2px);
  }

  .subscribe-button i {
    font-size: 1.1rem;
  }
</style> 