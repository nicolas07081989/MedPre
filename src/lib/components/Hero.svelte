<script>
  import { base } from '$app/paths';
</script>

<section class="hero">
  <div class="hero-content">
    <h1>Medicina de Precisión Ecuador</h1>
    <p>Diagnóstico molecular de precisión para tiroides</p>
    <div class="cta-buttons">
      <a href="{base}/contacto" class="btn primary">Contáctanos</a>
      <a href="{base}/quienes-somos" class="btn secondary">Conoce más</a>
    </div>
  </div>
</section>

<style>
  .hero {
    min-height: calc(100vh - 80px);
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--gradient-primary);
    color: var(--white);
    padding: 2rem;
  }

  .hero-content {
    max-width: 800px;
    text-align: center;
  }

  h1 {
    font-size: var(--font-6xl);
    font-weight: var(--font-weight-bold);
    margin-bottom: 1rem;
  }

  p {
    font-size: var(--font-xl);
    margin-bottom: 2rem;
  }

  .cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }

  .btn {
    padding: 1rem 2rem;
    border-radius: 8px;
    font-weight: var(--font-weight-semibold);
    text-decoration: none;
    transition: all 0.3s ease;
  }

  .primary {
    background: var(--white);
    color: var(--primary-color);
  }

  .secondary {
    border: 2px solid var(--white);
    color: var(--white);
  }

  @media (max-width: 768px) {
    h1 {
      font-size: var(--font-4xl);
    }

    p {
      font-size: var(--font-lg);
    }

    .cta-buttons {
      flex-direction: column;
    }
  }
</style> 