<section class="testimonials">
  <div class="container">
    <h2>Testimonios</h2>
    <div class="testimonials-grid">
      <div class="testimonial">
        <div class="quote">"Excelente servicio y resultados precisos"</div>
        <div class="author">Dr. Juan Pérez</div>
      </div>
      <!-- Agrega más testimonios según necesites -->
    </div>
  </div>
</section>

<style>
  .testimonials {
    padding: 4rem 2rem;
    background: var(--white);
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

  .testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  .testimonial {
    padding: 2rem;
    background: var(--light-bg);
    border-radius: 12px;
    text-align: center;
  }

  .quote {
    font-size: var(--font-lg);
    margin-bottom: 1rem;
    color: var(--text-color);
  }

  .author {
    color: var(--primary-color);
    font-weight: var(--font-weight-semibold);
  }

  .testimonials-container {
    display: grid;
    gap: 2rem;
    padding: 2rem;
  }

  @media screen and (max-width: 768px) {
    .testimonials-container {
      grid-template-columns: 1fr;
      padding: 1rem;
    }

    .testimonial-card {
      padding: 1rem;
    }
  }

  @media screen and (min-width: 769px) and (max-width: 1024px) {
    .testimonials-container {
      grid-template-columns: repeat(2, 1fr);
    }
  }
</style> 