<section class="services">
  <div class="container">
    <h2>Nuestros Servicios</h2>
    <div class="services-grid">
      <div class="service-card">
        <i class="fas fa-microscope"></i>
        <h3>Diagnóstico Molecular</h3>
        <p>Análisis preciso de nódulos tiroideos</p>
      </div>
      <!-- Agrega más servicios según necesites -->
    </div>
  </div>
</section>

<style>
  .services {
    padding: 4rem 2rem;
    background: var(--light-bg);
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  h2 {
    text-align: center;
    font-size: var(--font-3xl);
    margin-bottom: 3rem;
  }

  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
  }

  .service-card {
    background: var(--white);
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .service-card i {
    font-size: 2.5rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
  }

  h3 {
    margin-bottom: 1rem;
    color: var(--text-color);
  }
</style> 