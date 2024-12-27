<script>
  import { fly } from 'svelte/transition';

  let formData = {
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  };

  const contactInfo = [
    {
      icon: "fas fa-map-marker-alt",
      title: "Ubicación",
      details: ["Quito, Ecuador", "Av. Principal 123"],
      action: "https://goo.gl/maps/xyz",
      actionText: "Ver en Mapa",
      color: "#00B4D8"
    },
    {
      icon: "fas fa-phone-alt",
      title: "Teléfonos",
      details: ["+593 97 913 621", "02-123-4567"],
      action: "tel:+59397913621",
      actionText: "Llamar Ahora",
      color: "#4CAF50"
    },
    {
      icon: "fas fa-envelope",
      title: "Email",
      details: ["medpre.ecuador@gmail.com"],
      action: "mailto:medpre.ecuador@gmail.com",
      actionText: "Enviar Email",
      color: "#FF4444"
    },
    {
      icon: "fas fa-clock",
      title: "Horario de Atención",
      details: ["Lunes a Viernes: 8:00 - 18:00", "Sábados: 9:00 - 13:00"],
      color: "#FFA000"
    }
  ];

  function handleSubmit() {
    // Implementar lógica de envío
    console.log('Formulario enviado:', formData);
  }
</script>

<div class="contact-page">
  <!-- Hero Section -->
  <section class="hero-section">
    <div class="hero-overlay">
      <div class="container">
        <div class="hero-content">
          <h1>
            <span class="highlight">Contáctenos</span>
            <span class="main-title">Estamos para Ayudarle</span>
          </h1>
          <p>Nuestro equipo está disponible para resolver todas sus dudas</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Info Section -->
  <section class="contact-info-section">
    <div class="container">
      <div class="info-grid">
        {#each contactInfo as info}
          <div class="info-card" in:fly={{ y: 50, duration: 1000 }}>
            <div class="info-icon" style="--card-color: {info.color}">
              <i class={info.icon}></i>
            </div>
            <h3>{info.title}</h3>
            {#each info.details as detail}
              <p>{detail}</p>
            {/each}
            {#if info.action}
              <a href={info.action} class="info-action" style="--card-color: {info.color}">
                {info.actionText}
                <i class="fas fa-arrow-right"></i>
              </a>
            {/if}
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Contact Form Section -->
  <section class="form-section">
    <div class="container">
      <div class="form-wrapper">
        <div class="form-content">
          <h2>Envíenos un Mensaje</h2>
          <p class="section-subtitle">Complete el formulario y le responderemos a la brevedad</p>
          
          <form on:submit|preventDefault={handleSubmit} class="contact-form">
            <div class="form-grid">
              <div class="form-group">
                <label for="name">Nombre Completo</label>
                <input 
                  type="text" 
                  id="name" 
                  bind:value={formData.name}
                  required
                  placeholder="Ingrese su nombre"
                />
              </div>

              <div class="form-group">
                <label for="email">Correo Electrónico</label>
                <input 
                  type="email" 
                  id="email" 
                  bind:value={formData.email}
                  required
                  placeholder="ejemplo@correo.com"
                />
              </div>

              <div class="form-group">
                <label for="phone">Teléfono</label>
                <input 
                  type="tel" 
                  id="phone" 
                  bind:value={formData.phone}
                  required
                  placeholder="+593 ..."
                />
              </div>

              <div class="form-group">
                <label for="subject">Asunto</label>
                <input 
                  type="text" 
                  id="subject" 
                  bind:value={formData.subject}
                  required
                  placeholder="¿Sobre qué nos quiere consultar?"
                />
              </div>

              <div class="form-group full-width">
                <label for="message">Mensaje</label>
                <textarea 
                  id="message" 
                  bind:value={formData.message}
                  required
                  placeholder="Escriba su mensaje aquí..."
                  rows="5"
                ></textarea>
              </div>
            </div>

            <button type="submit" class="btn btn-primary">
              Enviar Mensaje
              <i class="fas fa-paper-plane"></i>
            </button>
          </form>
        </div>

        <div class="form-image">
          <img 
            src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80" 
            alt="Contacto MedPre"
          />
        </div>
      </div>
    </div>
  </section>

  <!-- Map Section -->
  <section class="map-section">
    <div class="map-wrapper">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3989.7974113326166!2d-78.4922876!3d-0.1806532!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91d59a4002427c9f%3A0x44b991e158ef5572!2sQuito%2C+Ecuador!5e0!3m2!1ses!2sec!4v1234567890"
        width="100%"
        height="450"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>
  </section>
</div>

<style>
  .contact-page {
    background: var(--white);
  }

  /* Hero Section */
  .hero-section {
    background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                      url('https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&q=80');
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
  }

  .hero-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 2rem;
    text-align: center;
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

  /* Contact Info Section */
  .contact-info-section {
    margin-top: -100px;
    position: relative;
    z-index: 2;
    padding: 0 0 6rem;
  }

  .info-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
  }

  .info-card {
    background: var(--white);
    padding: 2.5rem 2rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
  }

  .info-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
  }

  .info-icon {
    width: 70px;
    height: 70px;
    background: var(--light-bg);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    transition: all 0.3s ease;
    color: var(--primary-color);
  }

  .info-card:hover .info-icon {
    background: var(--card-color);
  }

  .info-icon i {
    font-size: 1.8rem;
    color: var(--card-color);
    transition: all 0.3s ease;
  }

  .info-card:hover .info-icon i {
    color: var(--white);
  }

  .info-card h3 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    color: var(--primary-color);
  }

  .info-card p {
    margin: 0.5rem 0;
    font-size: 1.1rem;
    color: var(--text-color);
  }

  .info-action {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1.5rem;
    color: var(--card-color);
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
  }

  .info-action:hover {
    gap: 1rem;
    opacity: 0.8;
  }

  /* Form Section */
  .form-section {
    padding: 8rem 0;
    background: var(--white);
    position: relative;
  }

  .form-wrapper {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 4rem;
    align-items: center;
  }

  .form-content h2 {
    font-size: 2.5rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
  }

  .section-subtitle {
    font-size: 1.2rem;
    color: var(--text-color);
    margin-bottom: 3rem;
    opacity: 0.8;
  }

  .form-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
  }

  .form-group.full-width {
    grid-column: 1 / -1;
  }

  label {
    color: var(--text-color);
    font-weight: 600;
    font-size: 1.1rem;
  }

  input,
  textarea {
    padding: 1rem;
    border: 2px solid var(--light-bg);
    border-radius: 10px;
    font-size: 1rem;
    transition: all 0.3s ease;
    font-family: inherit;
  }

  input:focus,
  textarea:focus {
    border-color: var(--primary-color);
    outline: none;
    box-shadow: 0 0 0 3px rgba(12, 186, 184, 0.1);
  }

  textarea {
    resize: vertical;
    min-height: 120px;
  }

  .form-image {
    position: relative;
  }

  .form-image img {
    width: 100%;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  }

  .form-image::before {
    content: '';
    position: absolute;
    top: 20px;
    left: 20px;
    right: -20px;
    bottom: -20px;
    border: 2px solid var(--primary-color);
    border-radius: 20px;
    z-index: -1;
    opacity: 0.1;
  }

  /* Map Section */
  .map-section {
    padding: 0;
    background: var(--light-bg);
  }

  .map-wrapper {
    height: 450px;
    overflow: hidden;
  }

  .map-wrapper iframe {
    width: 100%;
    height: 100%;
    border: none;
  }

  /* Button Styles */
  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.8rem;
    padding: 1.2rem 3rem;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .btn-primary {
    background: var(--primary-color);
    color: var(--white);
  }

  .btn-primary:hover {
    background: var(--secondary-color);
    transform: translateY(-2px);
  }

  /* Responsive Design */
  @media (max-width: 1200px) {
    .info-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 968px) {
    .form-wrapper {
      grid-template-columns: 1fr;
    }

    .form-image {
      display: none;
    }

    .hero-content .main-title {
      font-size: 3rem;
    }
  }

  @media (max-width: 576px) {
    .info-grid {
      grid-template-columns: 1fr;
    }

    .form-grid {
      grid-template-columns: 1fr;
    }

    .hero-content .main-title {
      font-size: 2.5rem;
    }

    .hero-content .highlight {
      font-size: 1.5rem;
    }
  }
</style> 