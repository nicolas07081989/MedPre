<script>
  import { fly } from 'svelte/transition';

  const mainAdvantages = [
    {
      icon: "fas fa-dna",
      title: "Tecnología Avanzada",
      description: "Análisis molecular de última generación con precisión superior al 96%"
    },
    {
      icon: "fas fa-clock",
      title: "Resultados Rápidos",
      description: "Entrega de resultados en menos de 48 horas tras recibir la muestra"
    },
    {
      icon: "fas fa-shield-alt",
      title: "Diagnóstico Preciso",
      description: "Evita cirugías innecesarias en el 80% de los casos indeterminados"
    }
  ];

  const comparisons = [
    {
      title: "Diagnóstico Tradicional",
      features: [
        "Resultados indeterminados frecuentes",
        "Posibles cirugías innecesarias",
        "Mayor tiempo de espera",
        "Menor precisión diagnóstica",
        "Múltiples procedimientos invasivos"
      ],
      isTraditional: true
    },
    {
      title: "Diagnóstico Molecular",
      features: [
        "Resultados definitivos",
        "Evita cirugías innecesarias",
        "Resultados en 48 horas",
        "96% de precisión",
        "Un solo procedimiento"
      ],
      isTraditional: false
    }
  ];

  const stats = [
    {
      number: "96%",
      label: "Precisión",
      icon: "fas fa-bullseye"
    },
    {
      number: "80%",
      label: "Cirugías Evitadas",
      icon: "fas fa-user-shield"
    },
    {
      number: "48h",
      label: "Tiempo de Respuesta",
      icon: "fas fa-clock"
    }
  ];
</script>

<div class="advantages-page">
  <!-- Hero Section -->
  <section class="hero-section">
    <div class="hero-overlay">
      <div class="container">
        <div class="hero-content">
          <h1>
            <span class="highlight">Ventajas Únicas</span>
            <span class="main-title">Diagnóstico de Precisión</span>
          </h1>
          <p>Descubra por qué somos líderes en diagnóstico molecular de tiroides</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Stats Section -->
  <section class="stats-section">
    <div class="container">
      <div class="stats-grid">
        {#each stats as stat}
          <div class="stat-card" in:fly={{ y: 50, duration: 1000 }}>
            <div class="stat-icon">
              <i class={stat.icon}></i>
            </div>
            <span class="stat-number">{stat.number}</span>
            <span class="stat-label">{stat.label}</span>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Main Advantages -->
  <section class="main-advantages">
    <div class="container">
      <h2 class="section-title">Nuestras Ventajas</h2>
      <p class="section-subtitle">Tecnología y experiencia a su servicio</p>
      
      <div class="advantages-grid">
        {#each mainAdvantages as advantage, i}
          <div 
            class="advantage-card"
            in:fly={{ y: 50, duration: 1000, delay: i * 200 }}
          >
            <div class="advantage-icon">
              <i class={advantage.icon}></i>
            </div>
            <h3>{advantage.title}</h3>
            <p>{advantage.description}</p>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Comparison Section -->
  <section class="comparison-section">
    <div class="container">
      <h2 class="section-title">Comparativa de Métodos</h2>
      <p class="section-subtitle">¿Por qué elegir el diagnóstico molecular?</p>

      <div class="comparison-grid">
        {#each comparisons as comparison}
          <div class="comparison-card {comparison.isTraditional ? 'traditional' : 'molecular'}">
            <div class="card-header">
              <i class={comparison.isTraditional ? 'fas fa-hospital' : 'fas fa-dna'}></i>
              <h3>{comparison.title}</h3>
            </div>
            <ul>
              {#each comparison.features as feature}
                <li>
                  <i class={comparison.isTraditional ? 'fas fa-times' : 'fas fa-check'}></i>
                  {feature}
                </li>
              {/each}
            </ul>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="cta-section">
    <div class="container">
      <div class="cta-content">
        <h2>Elija la Precisión</h2>
        <p>Tome la mejor decisión para su salud con diagnóstico molecular</p>
        <div class="cta-buttons">
          <a href="/contacto" class="btn btn-primary">
            <i class="fas fa-calendar-check"></i>
            Agendar Consulta
          </a>
          <a href="tel:+59397913621" class="btn btn-outline">
            <i class="fas fa-phone"></i>
            Llamar Ahora
          </a>
        </div>
      </div>
    </div>
  </section>
</div>

<style>
  .advantages-page {
    background: var(--light-bg);
  }

  /* Hero Section */
  .hero-section {
    background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                      url('https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?auto=format&fit=crop&q=80');
    background-size: cover;
    background-position: center;
    height: 60vh;
    position: relative;
    color: var(--white);
    margin-bottom: 0;
  }

  .hero-overlay {
    background: var(--gradient-overlay);
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 1rem;
  }

  .hero-content {
    max-width: 800px;
    text-align: center;
    margin: 0 auto;
  }

  .hero-content h1 {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }

  .hero-content .highlight {
    display: block;
    font-size: 2rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
    opacity: 0.9;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  .hero-content .main-title {
    display: block;
    font-size: 3.5rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    line-height: 1.2;
  }

  .hero-content p {
    font-size: 1.25rem;
    opacity: 0.9;
    max-width: 600px;
    margin: 0 auto 2rem;
    line-height: 1.6;
  }

  /* Stats Section - Nueva sección */
  .stats-section {
    background: var(--white);
    padding: 4rem 0;
    margin-top: -100px;
    position: relative;
    z-index: 2;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }

  .stat-card {
    background: var(--white);
    padding: 2.5rem 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease;
  }

  .stat-card:hover {
    transform: translateY(-5px);
  }

  .stat-icon {
    width: 70px;
    height: 70px;
    background: var(--light-bg);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
  }

  .stat-icon i {
    font-size: 1.8rem;
    color: var(--primary-color);
  }

  .stat-number {
    display: block;
    font-size: 2.8rem;
    font-weight: 800;
    color: var(--primary-color);
    margin-bottom: 0.5rem;
  }

  .stat-label {
    color: var(--text-color);
    font-size: 1.1rem;
    font-weight: 500;
  }

  /* Main Advantages Section - Mejorado */
  .main-advantages {
    padding: 8rem 0;
    background: var(--light-bg);
    position: relative;
  }

  .section-title {
    text-align: center;
    font-size: 2.5rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-weight: 700;
  }

  .section-subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: var(--text-color);
    margin-bottom: 4rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0.8;
  }

  .advantages-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5rem;
  }

  .advantage-card {
    background: var(--white);
    padding: 3rem 2rem;
    border-radius: 20px;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow: hidden;
  }

  .advantage-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--primary-color);
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .advantage-card:hover::before {
    opacity: 1;
  }

  .advantage-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  }

  .advantage-icon {
    width: 100px;
    height: 100px;
    background: var(--white);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 2rem;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
  }

  .advantage-icon i {
    font-size: 2.5rem;
    color: var(--primary-color);
  }

  .advantage-card h3 {
    color: var(--primary-color);
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }

  .advantage-card p {
    color: var(--text-color);
    line-height: 1.6;
  }

  /* Benefits Section */
  .benefits-section {
    padding: 8rem 0;
    background: var(--light-bg);
    position: relative;
    overflow: hidden;
  }

  .benefits-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
    margin-top: 4rem;
  }

  .benefit-card {
    display: flex;
    align-items: flex-start;
    gap: 2rem;
    background: var(--white);
    padding: 2.5rem;
    border-radius: 20px;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  }

  .benefit-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
  }

  .benefit-icon {
    width: 70px;
    height: 70px;
    background: var(--light-bg);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .benefit-icon i {
    font-size: 1.8rem;
    color: var(--primary-color);
  }

  .benefit-content h3 {
    color: var(--primary-color);
    font-size: 1.3rem;
    margin-bottom: 0.8rem;
  }

  .benefit-content p {
    color: var(--text-color);
    line-height: 1.6;
  }

  /* Comparison Section - Mejorado */
  .comparison-section {
    padding: 8rem 0;
    background: var(--white);
  }

  .comparison-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
    max-width: 1000px;
    margin: 4rem auto 0;
  }

  .comparison-card {
    padding: 3rem;
    border-radius: 20px;
    transition: all 0.3s ease;
  }

  .card-header {
    text-align: center;
    margin-bottom: 2rem;
  }

  .card-header i {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: inherit;
  }

  .card-header h3 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
  }

  .comparison-card.traditional {
    background: var(--light-bg);
    color: var(--text-color);
  }

  .comparison-card.molecular {
    background: var(--primary-color);
    color: var(--white);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
  }

  .comparison-card ul {
    list-style: none;
    padding: 0;
  }

  .comparison-card li {
    padding: 1rem 0;
    display: flex;
    align-items: center;
    gap: 1rem;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  }

  .comparison-card.molecular li {
    border-bottom-color: rgba(255, 255, 255, 0.1);
  }

  .comparison-card li:last-child {
    border-bottom: none;
  }

  .comparison-card.traditional i {
    color: var(--accent-color);
  }

  .comparison-card.molecular i {
    color: #4CAF50;
  }

  /* CTA Section - Mejorado */
  .cta-section {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: var(--white);
    padding: 6rem 0;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  .cta-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 0v10h10v10H30v10h10v10H30v10h10v10H20V50h10V40H20V30h10V20H20V10h10V0h10z' fill='%23ffffff' fill-opacity='0.05'/%3E%3C/svg%3E");
    opacity: 0.1;
  }

  .cta-content {
    position: relative;
    z-index: 1;
  }

  .cta-content h2 {
    font-size: 3rem;
    margin-bottom: 1.5rem;
    font-weight: 700;
  }

  .cta-content p {
    font-size: 1.3rem;
    margin-bottom: 3rem;
    opacity: 0.9;
  }

  .cta-buttons {
    display: flex;
    gap: 2rem;
    justify-content: center;
  }

  .btn {
    padding: 1.2rem 3rem;
    font-size: 1.1rem;
  }

  /* Responsive Design */
  @media (max-width: 968px) {
    .advantages-grid {
      grid-template-columns: repeat(2, 1fr);
    }

    .benefits-grid,
    .comparison-grid {
      grid-template-columns: 1fr;
    }

    .hero-content h1 {
      font-size: 3rem;
    }
  }

  @media (max-width: 576px) {
    .advantages-grid {
      grid-template-columns: 1fr;
    }

    .benefit-card {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .cta-buttons {
      flex-direction: column;
    }

    .btn {
      width: 100%;
    }

    .hero-content h1 {
      font-size: 2.5rem;
    }
  }

  .advantage-card:hover {
    border-color: var(--secondary-color);
  }

  .advantage-icon {
    color: var(--primary-color);
  }

  .comparison-card.molecular {
    background: var(--primary-color);
  }
</style> 