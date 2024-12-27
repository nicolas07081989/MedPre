<script>
  import { fly } from 'svelte/transition';

  const pricingPlan = {
    name: "Estudio Molecular Completo",
    price: "$1300",
    features: [
      "Análisis molecular MIR-THYPE Full",
      "Consulta con especialista",
      "Interpretación detallada de resultados",
      "Recomendaciones personalizadas",
      "Seguimiento post-resultado",
      "Garantía de precisión del 96%"
    ]
  };

  const paymentMethods = [
    {
      icon: "fas fa-credit-card",
      title: "Tarjetas de Crédito",
      description: "Diferido hasta 12 meses sin intereses",
      brands: ["Visa", "Mastercard", "American Express"]
    },
    {
      icon: "fas fa-university",
      title: "Transferencia Bancaria",
      description: "Transferencia directa a nuestra cuenta corporativa",
      banks: ["Pichincha", "Guayaquil", "Pacífico"]
    },
    {
      icon: "fas fa-money-bill-wave",
      title: "Efectivo",
      description: "Pago en efectivo con facturación inmediata",
      benefit: "5% de descuento"
    }
  ];

  const serviceInclusions = [
    {
      icon: "fas fa-flask",
      title: "Procesamiento de Muestra",
      description: "Análisis completo en laboratorio especializado con tecnología de última generación"
    },
    {
      icon: "fas fa-plane",
      title: "Envío Internacional",
      description: "Traslado seguro de la muestra a laboratorios internacionales con cadena de frío garantizada"
    },
    {
      icon: "fas fa-file-medical-alt",
      title: "Informe Detallado",
      description: "Reporte completo con interpretación profesional y recomendaciones específicas"
    },
    {
      icon: "fas fa-user-md",
      title: "Consulta Médica",
      description: "Cita con especialista para revisión de resultados y plan de seguimiento personalizado"
    }
  ];
</script>

<div class="investment-page">
  <!-- Hero Section -->
  <section class="hero-section">
    <div class="hero-overlay">
      <div class="container">
        <div class="hero-content">
          <h1>
            <span class="highlight">Inversión en su Salud</span>
            <span class="main-title">Diagnóstico de Calidad</span>
          </h1>
          <p>Una decisión inteligente para su bienestar y tranquilidad</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Pricing Section -->
  <section class="pricing-section">
    <div class="container">
      <div class="pricing-card" in:fly={{ y: 50, duration: 1000 }}>
        <div class="pricing-header">
          <h2>{pricingPlan.name}</h2>
          <div class="price">
            <span class="amount">{pricingPlan.price}</span>
            <span class="period">IVA incluido</span>
          </div>
        </div>
        <ul class="features-list">
          {#each pricingPlan.features as feature}
            <li>
              <i class="fas fa-check-circle"></i>
              {feature}
            </li>
          {/each}
        </ul>
        <div class="pricing-footer">
          <a href="/contacto" class="btn btn-primary">Solicitar Ahora</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Payment Methods -->
  <section class="payment-section">
    <div class="container">
      <h2 class="section-title">Facilidades de Pago</h2>
      <p class="section-subtitle">Múltiples opciones para su comodidad</p>
      
      <div class="payment-grid">
        {#each paymentMethods as method}
          <div class="payment-card" in:fly={{ y: 50, duration: 1000 }}>
            <div class="payment-icon">
              <i class={method.icon}></i>
            </div>
            <h3>{method.title}</h3>
            <p>{method.description}</p>
            {#if method.brands}
              <div class="payment-brands">
                {#each method.brands as brand}
                  <span class="brand-tag">{brand}</span>
                {/each}
              </div>
            {/if}
            {#if method.banks}
              <div class="payment-brands">
                {#each method.banks as bank}
                  <span class="brand-tag">{bank}</span>
                {/each}
              </div>
            {/if}
            {#if method.benefit}
              <div class="payment-benefit">
                <i class="fas fa-tag"></i>
                {method.benefit}
              </div>
            {/if}
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Service Inclusions -->
  <section class="inclusions-section">
    <div class="container">
      <h2 class="section-title">¿Qué Incluye su Inversión?</h2>
      <p class="section-subtitle">Servicio completo y profesional</p>
      
      <div class="inclusions-grid">
        {#each serviceInclusions as inclusion}
          <div class="inclusion-card" in:fly={{ y: 50, duration: 1000 }}>
            <div class="inclusion-icon">
              <i class={inclusion.icon}></i>
            </div>
            <div class="inclusion-content">
              <h3>{inclusion.title}</h3>
              <p>{inclusion.description}</p>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="cta-section">
    <div class="container">
      <div class="cta-content">
        <h2>¿Listo para Invertir en su Salud?</h2>
        <p>Nuestro equipo está disponible para resolver todas sus dudas</p>
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
  .investment-page {
    background: var(--white);
  }

  /* Hero Section */
  .hero-section {
    background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                      url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&q=80');
    background-size: cover;
    background-position: center;
    height: 60vh;
    position: relative;
    color: var(--white);
  }

  .hero-overlay {
    background: var(--gradient-overlay);
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    text-align: center;
  }

  .hero-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 2rem;
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
    margin: 0 auto;
  }

  /* Pricing Section */
  .pricing-section {
    padding: 6rem 0;
    background: var(--white);
    margin-top: -60px;
    position: relative;
  }

  .pricing-card {
    background: var(--white);
    padding: 4rem;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
    position: relative;
    overflow: hidden;
  }

  .pricing-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: var(--gradient-primary);
  }

  .pricing-header h2 {
    color: var(--primary-color);
    font-size: 2rem;
    margin-bottom: 2rem;
  }

  .price {
    margin: 2rem 0;
  }

  .amount {
    font-size: 4.5rem;
    font-weight: 800;
    color: var(--primary-color);
    line-height: 1;
  }

  .period {
    display: block;
    color: var(--text-color);
    font-size: 1.1rem;
    margin-top: 0.8rem;
    opacity: 0.7;
  }

  .features-list {
    list-style: none;
    padding: 0;
    margin: 3rem 0;
    text-align: left;
  }

  .features-list li {
    margin: 1.2rem 0;
    display: flex;
    align-items: center;
    gap: 1rem;
    color: var(--text-color);
    font-size: 1.1rem;
    padding: 0.5rem 0;
  }

  .features-list i {
    color: var(--secondary-color);
    font-size: 1.3rem;
  }

  /* Payment Methods */
  .payment-section {
    padding: 8rem 0;
    background: var(--light-bg);
    position: relative;
  }

  .section-title {
    text-align: center;
    font-size: 2.5rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
  }

  .section-subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: var(--text-color);
    margin-bottom: 4rem;
    opacity: 0.8;
  }

  .payment-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5rem;
  }

  .payment-card {
    background: var(--white);
    padding: 3rem 2rem;
    border-radius: 20px;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  }

  .payment-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  }

  .payment-icon {
    width: 80px;
    height: 80px;
    background: var(--light-bg);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 2rem;
    transition: all 0.3s ease;
  }

  .payment-card:hover .payment-icon {
    background: var(--primary-color);
  }

  .payment-card:hover .payment-icon i {
    color: var(--white);
  }

  .payment-icon i {
    font-size: 2rem;
    color: var(--primary-color);
    transition: all 0.3s ease;
  }

  .payment-card h3 {
    color: var(--primary-color);
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }

  .payment-brands {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 1.5rem;
  }

  .brand-tag {
    background: var(--light-bg);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    color: var(--primary-color);
    transition: all 0.3s ease;
  }

  .payment-card:hover .brand-tag {
    background: var(--primary-color);
    color: var(--white);
  }

  .payment-benefit {
    margin-top: 1.5rem;
    color: var(--accent-color);
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }

  /* Service Inclusions */
  .inclusions-section {
    padding: 8rem 0;
    background: var(--white);
  }

  .inclusions-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2.5rem;
    margin-top: 4rem;
  }

  .inclusion-card {
    display: flex;
    align-items: flex-start;
    gap: 2rem;
    padding: 3rem;
    background: var(--light-bg);
    border-radius: 20px;
    transition: all 0.3s ease;
  }

  .inclusion-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
    background: var(--white);
  }

  .inclusion-icon {
    width: 70px;
    height: 70px;
    background: var(--white);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
  }

  .inclusion-icon i {
    font-size: 1.8rem;
    color: var(--primary-color);
  }

  .inclusion-content h3 {
    color: var(--primary-color);
    font-size: 1.4rem;
    margin-bottom: 1rem;
  }

  .inclusion-content p {
    color: var(--text-color);
    line-height: 1.6;
  }

  /* CTA Section */
  .cta-section {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: var(--white);
    padding: 8rem 0;
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
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.3s ease;
  }

  /* Responsive Design */
  @media (max-width: 968px) {
    .payment-grid {
      grid-template-columns: repeat(2, 1fr);
    }

    .inclusions-grid {
      grid-template-columns: 1fr;
    }

    .hero-content h1 {
      font-size: 3rem;
    }

    .pricing-card.highlight {
      transform: none;
    }
  }

  @media (max-width: 576px) {
    .payment-grid {
      grid-template-columns: 1fr;
    }

    .inclusion-card {
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

    .amount {
      font-size: 3rem;
    }
  }
</style> 