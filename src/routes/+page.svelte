<script>
  import { base } from '$app/paths';
</script>

<svelte:head>
  <title>MedPre - Medicina de Precisión Ecuador</title>
  <meta name="description" content="Líder en diagnóstico molecular de precisión para tiroides en Ecuador" />
</svelte:head>

<!-- Hero Section -->
<div class="hero-section">
  <div class="hero-overlay"></div>
  <div class="container hero-content">
    <h1>Medicina de Precisión Ecuador</h1>
    <p class="hero-subtitle">Innovación en diagnóstico molecular para tiroides</p>
    <div class="hero-buttons">
      <a href="./" class="btn btn-white">
        <i class="fas fa-calendar-check"></i>
        Agendar Consulta
      </a>
      <a href="#learn-more" class="btn btn-outline">
        <i class="fas fa-arrow-down"></i>
        Descubrir Más
      </a>
    </div>
  </div>
</div>

<!-- Main Content -->
<div id="learn-more" class="page-section pattern-transition">
  <div class="container">
    <h2 class="section-title">
      <i class="fi fi-rr-diploma"></i>
      Excelencia en Diagnóstico Molecular
    </h2>
    <p class="section-subtitle">
      Utilizamos tecnología de última generación para proporcionar resultados precisos y confiables
    </p>

    <div class="content-grid">
      <div class="info-card">
        <i class="fi fi-rr-dna"></i>
        <h3>Precisión Molecular</h3>
        <p>Análisis detallado del ADN para diagnósticos precisos y personalizados que guían el tratamiento más efectivo.</p>
      </div>

      <div class="info-card">
        <i class="fi fi-rr-microscope"></i>
        <h3>Tecnología Avanzada</h3>
        <p>Equipamiento de última generación y métodos validados internacionalmente para resultados confiables.</p>
      </div>

      <div class="info-card">
        <i class="fi fi-rr-doctor"></i>
        <h3>Experiencia Profesional</h3>
        <p>Equipo médico altamente capacitado con experiencia en diagnóstico molecular y medicina personalizada.</p>
      </div>
    </div>

    <!-- Estadísticas -->
    <div class="stats-section">
      <div class="stat-item">
        <span class="stat-number">98%</span>
        <p>Precisión Diagnóstica</p>
      </div>
      <div class="stat-item">
        <span class="stat-number">+1000</span>
        <p>Pacientes Atendidos</p>
      </div>
      <div class="stat-item">
        <span class="stat-number">24h</span>
        <p>Tiempo de Respuesta</p>
      </div>
    </div>

    <!-- Por qué elegirnos -->
    <div class="why-us-section">
      <h2>¿Por qué elegir MedPre?</h2>
      <div class="features-grid">
        <div class="feature-item">
          <i class="fas fa-check-circle"></i>
          <h4>Resultados Rápidos</h4>
          <p>Entrega de resultados en 24 horas para casos prioritarios</p>
        </div>
        <div class="feature-item">
          <i class="fas fa-shield-alt"></i>
          <h4>Certificación Internacional</h4>
          <p>Procedimientos avalados por estándares internacionales</p>
        </div>
        <div class="feature-item">
          <i class="fas fa-heart"></i>
          <h4>Atención Personalizada</h4>
          <p>Seguimiento individual para cada paciente</p>
        </div>
        <div class="feature-item">
          <i class="fas fa-globe"></i>
          <h4>Tecnología de Punta</h4>
          <p>Equipamiento de última generación</p>
        </div>
      </div>
    </div>

    <div class="cta-section">
      <h2>¿Listo para comenzar?</h2>
      <p>Contáctanos hoy mismo para más información o para agendar tu consulta</p>
      <div class="cta-buttons">
        <a href="./" class="btn btn-primary">
          <i class="fas fa-envelope"></i>
          Contactar
        </a>
        <a href="./" class="btn btn-outline">
          <i class="fas fa-plus-circle"></i>
          Conocer más
        </a>
      </div>
    </div>
  </div>
  <div class="medical-symbols"></div>
</div>

<style>
  .hero-section {
    height: calc(100vh - 80px);
    background: linear-gradient(135deg, #0CBAB8, #007D79);
    position: relative;
    display: flex;
    align-items: center;
    color: var(--white);
  }

  .hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(
      circle at center,
      rgba(255, 255, 255, 0.1) 0%,
      transparent 70%
    );
  }

  .hero-content {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 2rem;
  }

  .hero-content h1 {
    font-size: 4rem;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 125, 121, 0.3);
  }

  .hero-subtitle {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 2px rgba(0, 125, 121, 0.3);
  }

  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }

  .stats-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin: 4rem 0;
    padding: 2rem;
    background: var(--white);
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .stat-item {
    text-align: center;
  }

  .stat-number {
    font-size: 2.5rem;
    font-weight: bold;
    color: #0CBAB8;
    display: block;
    margin-bottom: 0.5rem;
  }

  .why-us-section {
    margin: 4rem 0;
    text-align: center;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }

  .feature-item {
    background: var(--white);
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .feature-item i {
    font-size: 2rem;
    color: #0CBAB8;
    margin-bottom: 1rem;
  }

  .feature-item h4 {
    color: #0CBAB8;
    margin-bottom: 1rem;
  }

  .content-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 4rem 0;
  }

  .info-card {
    background: var(--white);
    padding: 2rem;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }

  .info-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(12, 186, 184, 0.15);
  }

  .info-card i {
    font-size: 2.5rem;
    color: #0CBAB8;
    margin-bottom: 1rem;
  }

  .info-card h3 {
    color: #0CBAB8;
    margin-bottom: 1rem;
    font-size: 1.5rem;
  }

  .info-card p {
    color: var(--text-color);
    line-height: 1.6;
  }

  .cta-section {
    text-align: center;
    margin-top: 4rem;
    padding: 3rem;
    background: var(--white);
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .cta-section h2 {
    color: #0CBAB8;
    font-size: 2rem;
    margin-bottom: 1rem;
  }

  .cta-section p {
    color: var(--text-color);
    margin-bottom: 2rem;
  }

  .cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }

  @media (max-width: 768px) {
    .hero-content h1 {
      font-size: 2.5rem;
    }

    .hero-subtitle {
      font-size: 1.2rem;
    }

    .hero-buttons {
      flex-direction: column;
    }

    .stats-section {
      grid-template-columns: 1fr;
    }

    .cta-buttons {
      flex-direction: column;
      align-items: stretch;
    }

    .btn {
      width: 100%;
      justify-content: center;
    }
  }

  .btn-primary {
    background: #0CBAB8;
    color: var(--white);
  }

  .btn-primary:hover {
    background: #007D79;
  }

  .btn-outline {
    border: 2px solid #0CBAB8;
    color: #0CBAB8;
  }

  .btn-outline:hover {
    background: #0CBAB8;
    color: var(--white);
  }

  .btn-white {
    background: var(--white);
    color: #0CBAB8;
  }

  .btn-white:hover {
    background: rgba(255, 255, 255, 0.9);
    transform: translateY(-2px);
  }

  .feature-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(12, 186, 184, 0.12);
  }

  .fi {
    margin-right: 0.5rem;
    vertical-align: middle;
  }

  .info-card i {
    font-size: 2.5rem;
    color: #0CBAB8;
    margin-bottom: 1rem;
  }

  .section-title i {
    font-size: 2rem;
    color: #0CBAB8;
    margin-right: 1rem;
  }

  .hero-content h1 i {
    font-size: 3rem;
    margin-right: 1rem;
    vertical-align: middle;
  }
</style>
