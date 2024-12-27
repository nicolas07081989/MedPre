<section class="contact">
  <div class="container">
    <h2>Contacto</h2>
    <div class="contact-info">
      <div class="info-item">
        <i class="fas fa-phone"></i>
        <p>+593 97 913 621</p>
      </div>
      <div class="info-item">
        <i class="fas fa-envelope"></i>
        <p>medpre.ecuador@gmail.com</p>
      </div>
      <div class="info-item">
        <i class="fas fa-map-marker-alt"></i>
        <p>Quito, Ecuador</p>
      </div>
    </div>
  </div>
</section>

<style>
  .contact {
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

  .contact-info {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    text-align: center;
  }

  .info-item {
    padding: 2rem;
    background: var(--white);
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .info-item i {
    font-size: 2rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
  }

  .info-item p {
    font-size: var(--font-lg);
  }
</style> 