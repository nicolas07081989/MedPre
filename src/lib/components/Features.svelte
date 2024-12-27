<section class="features">
  <h2>Nuestras Características</h2>
  <div class="features-grid">
    <div class="feature">
      <i class="fas fa-dna"></i>
      <h3>Precisión Molecular</h3>
      <p>Análisis detallado del ADN para diagnósticos precisos</p>
    </div>
    <!-- Agrega más características según necesites -->
  </div>
</section>

<style>
  .features {
    padding: 4rem 2rem;
    background: var(--light-bg);
  }

  h2 {
    text-align: center;
    font-size: var(--font-3xl);
    margin-bottom: 3rem;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .feature {
    text-align: center;
    padding: 2rem;
    background: var(--white);
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .feature i {
    font-size: 2.5rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
  }

  h3 {
    font-size: var(--font-xl);
    margin-bottom: 1rem;
  }
</style> 