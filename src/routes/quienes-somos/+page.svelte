<script>
  const teamMembers = [
    {
      name: "Dr. Juan Pérez",
      role: "Director Médico",
      specialty: "Especialista en Endocrinología",
      experience: "15 años de experiencia",
      education: "PhD en Medicina, Universidad de Barcelona",
      image: "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80"
    },
    {
      name: "Dra. María González",
      role: "Especialista en Diagnóstico Molecular",
      specialty: "PhD en Biología Molecular",
      experience: "12 años de experiencia",
      education: "Doctorado en Biología Molecular, Universidad de Stanford",
      image: "https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&q=80"
    },
    {
      name: "Dr. Carlos Rodríguez",
      role: "Jefe de Laboratorio",
      specialty: "Especialista en Patología Molecular",
      experience: "10 años de experiencia",
      education: "Máster en Patología Molecular, Universidad de Madrid",
      image: "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&q=80"
    }
  ];
</script>

<div class="about-page">
  <!-- Hero Section -->
  <section class="about-hero">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>Quiénes Somos</h1>
        <p>Líderes en diagnóstico molecular de precisión en Ecuador</p>
      </div>
    </div>
  </section>

  <!-- Introducción -->
  <section class="intro-section">
    <div class="container">
      <div class="intro-grid">
        <div class="intro-text">
          <h2>Nuestra Historia</h2>
          <p>MedPre nació a finales de 2024 con una misión clara: revolucionar el diagnóstico de cáncer de tiroides en Ecuador. Nos especializamos en estudios moleculares de precisión, ofreciendo a nuestros pacientes y profesionales médicos las herramientas más avanzadas para un diagnóstico certero.</p>
          <div class="stats-row">
            <div class="stat-item">
              <span class="stat-number">96%</span>
              <span class="stat-label">Precisión diagnóstica</span>
            </div>
            <div class="stat-item">
              <span class="stat-number">500+</span>
              <span class="stat-label">Pacientes atendidos</span>
            </div>
          </div>
        </div>
        <div class="intro-image">
          <img 
            src="https://images.unsplash.com/photo-1581595220892-b0739db3ba8c?auto=format&fit=crop&q=80" 
            alt="Equipo médico de MedPre"
          />
        </div>
      </div>
    </div>
  </section>

  <!-- Misión y Visión -->
  <section class="mission-vision-section">
    <div class="container">
      <div class="mission-vision-grid">
        <div class="mission-card">
          <i class="fas fa-heartbeat"></i>
          <h3>Nuestra Misión</h3>
          <p>Ayudar a todos los pacientes con nódulos de tiroides en el Ecuador a descubrir con certeza si existe o no la posibilidad de desarrollar cáncer a través de estudios moleculares de precisión, evitando cirugías innecesarias.</p>
        </div>
        <div class="vision-card">
          <i class="fas fa-eye"></i>
          <h3>Nuestra Visión</h3>
          <p>Superar los 500 estudios realizados entre el 2025 y 2030, haciendo que sean accesibles a toda la población ecuatoriana.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Equipo -->
  <section class="team-section">
    <div class="container">
      <h2>Nuestro Equipo Médico</h2>
      <p class="section-subtitle">
        Un equipo multidisciplinario de expertos dedicados a tu bienestar
      </p>
      
      <div class="team-grid">
        {#each teamMembers as member}
          <div class="team-member">
            <div class="member-image-container">
              <img src={member.image} alt={member.name} />
            </div>
            <div class="member-info">
              <h3>{member.name}</h3>
              <p class="role">{member.role}</p>
              <p class="specialty">{member.specialty}</p>
              <div class="member-details">
                <p><i class="fas fa-graduation-cap"></i> {member.education}</p>
                <p><i class="fas fa-clock"></i> {member.experience}</p>
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-section pattern-transition">
    <div class="medical-symbols"></div>
    <div class="container">
      <div class="cta-content">
        <h2>¿Necesitas más información?</h2>
        <p>Nuestro equipo está listo para atender todas tus consultas</p>
        <div class="cta-buttons">
          <a href="/contacto" class="btn btn-primary">Contactar Ahora</a>
          <a href="tel:+59397913621" class="btn btn-outline">
            <i class="fas fa-phone"></i>
            Llamar
          </a>
        </div>
      </div>
    </div>
  </section>
</div>

<style>
  .about-page {
    background: var(--light-bg);
  }

  /* Hero Section */
  .about-hero {
    background-image: url('https://images.unsplash.com/photo-1504813184591-01572f98c85f?auto=format&fit=crop&q=80');
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
    justify-content: center;
    text-align: center;
  }

  .hero-content h1 {
    font-size: 4rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  }

  .hero-content p {
    font-size: 1.5rem;
    opacity: 0.9;
  }

  /* Intro Section */
  .intro-section {
    padding: 6rem 0;
    background: var(--white);
    position: relative;
    margin-top: -60px;
    border-radius: 30px 30px 0 0;
  }

  .intro-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .intro-text h2 {
    color: var(--primary-color);
    font-size: 2.5rem;
    margin-bottom: 2rem;
    position: relative;
  }

  .intro-text h2::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 0;
    width: 60px;
    height: 4px;
    background: var(--accent-color);
    border-radius: 2px;
  }

  .intro-text p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--text-color);
    margin-bottom: 2rem;
  }

  .intro-image img {
    width: 100%;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }

  .intro-image:hover img {
    transform: scale(1.02);
  }

  .stats-row {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    margin-top: 3rem;
    background: var(--light-bg);
    padding: 2rem;
    border-radius: 15px;
  }

  .stat-item {
    text-align: center;
  }

  .stat-number {
    font-size: 3.5rem;
    font-weight: 800;
    color: var(--accent-color);
    display: block;
    line-height: 1;
  }

  .stat-label {
    color: var(--text-color);
    font-size: 1.1rem;
    margin-top: 0.5rem;
  }

  /* Mission Vision Section */
  .mission-vision-section {
    background: var(--light-bg);
    padding: 6rem 0;
    position: relative;
    overflow: hidden;
  }

  .mission-vision-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
  }

  .mission-card,
  .vision-card {
    background: var(--white);
    padding: 3rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    text-align: center;
    transition: transform 0.3s ease;
    position: relative;
    overflow: hidden;
  }

  .mission-card:hover,
  .vision-card:hover {
    transform: translateY(-10px);
  }

  .mission-card i,
  .vision-card i {
    font-size: 3rem;
    color: var(--primary-color);
    margin-bottom: 1.5rem;
    background: var(--light-bg);
    width: 80px;
    height: 80px;
    line-height: 80px;
    border-radius: 50%;
  }

  .mission-card h3,
  .vision-card h3 {
    color: var(--primary-color);
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
  }

  .mission-card p,
  .vision-card p {
    color: var(--text-color);
    line-height: 1.8;
  }

  /* Team Section */
  .team-section {
    padding: 8rem 0;
    background: var(--white);
    text-align: center;
  }

  .team-section h2 {
    color: var(--primary-color);
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  .section-subtitle {
    font-size: 1.2rem;
    color: var(--text-color);
    margin-bottom: 4rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }

  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 3rem;
    margin-top: 3rem;
  }

  .team-member {
    text-align: center;
  }

  .member-image-container {
    position: relative;
    width: 250px;
    height: 250px;
    margin: 0 auto 2rem;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  }

  .member-image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }

  .member-image-container:hover img {
    transform: scale(1.05);
  }

  .member-info {
    background: var(--light-bg);
    padding: 2rem;
    border-radius: 15px;
    margin-top: -30px;
    position: relative;
    z-index: 1;
  }

  .member-info h3 {
    color: var(--primary-color);
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }

  .role {
    color: var(--accent-color);
    font-weight: 600;
    margin: 0.5rem 0;
  }

  .specialty {
    color: var(--text-color);
    font-style: italic;
    margin-bottom: 1rem;
  }

  .member-details {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
  }

  .member-details p {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0.5rem 0;
    color: var(--text-color);
    font-size: 0.9rem;
  }

  .member-details i {
    color: var(--primary-color);
  }

  /* CTA Section */
  .cta-section {
    background: var(--primary-color);
    color: var(--white);
    padding: 6rem 0;
    text-align: center;
  }

  .cta-content h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  .cta-content p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    opacity: 0.9;
  }

  .cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }

  /* Responsive Design */
  @media (max-width: 968px) {
    .intro-grid,
    .mission-vision-grid {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .hero-content h1 {
      font-size: 3rem;
    }

    .intro-section {
      margin-top: -30px;
    }

    .team-grid {
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    }
  }

  @media (max-width: 576px) {
    .hero-content h1 {
      font-size: 2.5rem;
    }

    .stats-row {
      grid-template-columns: 1fr;
    }

    .cta-buttons {
      flex-direction: column;
    }

    .member-image-container {
      width: 200px;
      height: 200px;
    }
  }

  .team-member-card:hover {
    border-color: var(--secondary-color);
  }

  .specialty-icon {
    color: var(--primary-color);
  }
</style> 