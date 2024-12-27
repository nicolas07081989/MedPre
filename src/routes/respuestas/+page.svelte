<script>
  import { slide } from 'svelte/transition';

  const faqs = [
    {
      category: "Diagnóstico",
      questions: [
        {
          question: "¿Qué es un nódulo tiroideo indeterminado?",
          answer: "Un nódulo tiroideo indeterminado es aquel que, tras una biopsia inicial (PAAF), no puede ser clasificado definitivamente como benigno o maligno. Corresponde a las categorías III y IV del sistema Bethesda."
        },
        {
          question: "¿Por qué necesito un estudio molecular?",
          answer: "El estudio molecular proporciona información genética crucial sobre el comportamiento del nódulo, permitiendo una evaluación más precisa del riesgo de malignidad y ayudando a evitar cirugías innecesarias."
        }
      ]
    },
    {
      category: "Proceso",
      questions: [
        {
          question: "¿Se necesita una nueva biopsia?",
          answer: "No, utilizamos la misma muestra de tu primera punción (PAAF). Esto evita procedimientos adicionales y hace el proceso más cómodo para el paciente."
        },
        {
          question: "¿Cuánto tiempo toma obtener resultados?",
          answer: "Los resultados están disponibles en menos de 48 horas después de recibir la muestra en nuestro laboratorio."
        }
      ]
    },
    {
      category: "Precisión",
      questions: [
        {
          question: "¿Qué tan preciso es el estudio?",
          answer: "Nuestro estudio molecular tiene una precisión superior al 96%, lo que nos permite ofrecer diagnósticos altamente confiables."
        },
        {
          question: "¿Qué pasa si el resultado es indeterminado?",
          answer: "En el raro caso de un resultado indeterminado, ofrecemos una segunda opinión sin costo adicional y consulta con nuestros especialistas."
        }
      ]
    }
  ];

  let activeCategory = "Diagnóstico";
  let activeQuestion = null;

  function setActiveQuestion(question) {
    activeQuestion = activeQuestion === question ? null : question;
  }
</script>

<div class="answers-page">
  <!-- Hero Section -->
  <section class="hero-section">
    <div class="hero-overlay">
      <div class="container">
        <div class="hero-content">
          <h1>
            <span class="highlight">Respuestas Claras</span>
            <span class="main-title">para su Tranquilidad</span>
          </h1>
          <p>Resolvemos sus dudas sobre el diagnóstico molecular de tiroides</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Proceso Section -->
  <section class="process-section">
    <div class="container">
      <h2 class="section-title">Proceso Diagnóstico</h2>
      <p class="section-subtitle">Conoce nuestro enfoque paso a paso</p>
      
      <div class="process-timeline">
        <div class="timeline-item">
          <div class="timeline-icon">
            <i class="fas fa-file-medical"></i>
          </div>
          <div class="timeline-content">
            <h3>1. Evaluación Inicial</h3>
            <p>Revisión de tu historial médico y resultados previos de PAAF</p>
          </div>
        </div>

        <div class="timeline-item">
          <div class="timeline-icon">
            <i class="fas fa-dna"></i>
          </div>
          <div class="timeline-content">
            <h3>2. Análisis Molecular</h3>
            <p>Estudio molecular avanzado con tecnología de última generación</p>
          </div>
        </div>

        <div class="timeline-item">
          <div class="timeline-icon">
            <i class="fas fa-microscope"></i>
          </div>
          <div class="timeline-content">
            <h3>3. Interpretación</h3>
            <p>Análisis exhaustivo por nuestro equipo de especialistas</p>
          </div>
        </div>

        <div class="timeline-item">
          <div class="timeline-icon">
            <i class="fas fa-user-md"></i>
          </div>
          <div class="timeline-content">
            <h3>4. Consulta Personalizada</h3>
            <p>Explicación detallada y recomendaciones específicas</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="faq-section">
    <div class="container">
      <h2 class="section-title">Preguntas Frecuentes</h2>
      <p class="section-subtitle">Todo lo que necesita saber sobre nuestro servicio</p>

      <div class="faq-container">
        <div class="faq-categories">
          {#each faqs as category}
            <button 
              class="category-btn {activeCategory === category.category ? 'active' : ''}"
              on:click={() => activeCategory = category.category}
            >
              {category.category}
            </button>
          {/each}
        </div>

        <div class="faq-content">
          {#each faqs.find(cat => cat.category === activeCategory).questions as question}
            <div class="faq-item">
              <button 
                class="faq-question {activeQuestion === question ? 'active' : ''}"
                on:click={() => setActiveQuestion(question)}
              >
                {question.question}
                <i class="fas fa-chevron-down"></i>
              </button>
              {#if activeQuestion === question}
                <div class="faq-answer" transition:slide>
                  <p>{question.answer}</p>
                </div>
              {/if}
            </div>
          {/each}
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="cta-section">
    <div class="container">
      <div class="cta-content">
        <h2>¿Tiene más preguntas?</h2>
        <p>Nuestro equipo está disponible para resolver todas sus dudas</p>
        <div class="cta-buttons">
          <a href="/contacto" class="btn btn-primary">
            <i class="fas fa-envelope"></i>
            Contactar Ahora
          </a>
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
  .answers-page {
    background: var(--white);
  }

  /* Hero Section */
  .hero-section {
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
                      url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&q=80');
    background-size: cover;
    background-position: center;
    height: 60vh;
    position: relative;
    color: var(--white);
  }

  .hero-overlay {
    background: var(--gradient-overlay);
    height: 100%;
    display: flex;
    align-items: center;
  }

  .hero-content {
    max-width: 800px;
    padding: 2rem;
  }

  .hero-content h1 {
    font-size: 3.5rem;
    line-height: 1.2;
    margin-bottom: 1.5rem;
  }

  .hero-content .highlight {
    display: block;
    font-size: 2rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
  }

  .hero-content .main-title {
    display: block;
    font-weight: 800;
  }

  .hero-content p {
    font-size: 1.25rem;
    opacity: 0.9;
  }

  /* Process Section */
  .process-section {
    padding: 8rem 0;
    background: var(--white);
    margin-top: -60px;
    border-radius: 30px 30px 0 0;
    position: relative;
  }

  .process-timeline {
    max-width: 800px;
    margin: 4rem auto 0;
    position: relative;
  }

  .process-timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 100%;
    background: var(--primary-color);
    opacity: 0.2;
  }

  .timeline-item {
    display: flex;
    align-items: center;
    margin-bottom: 3rem;
    position: relative;
  }

  .timeline-icon {
    width: 60px;
    height: 60px;
    background: var(--primary-color);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.5rem;
    flex-shrink: 0;
    position: relative;
    z-index: 1;
    box-shadow: 0 0 0 10px var(--white);
  }

  .timeline-content {
    flex: 1;
    margin-left: 2rem;
    background: var(--light-bg);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  }

  .timeline-content h3 {
    color: var(--primary-color);
    margin-bottom: 0.5rem;
    font-size: 1.3rem;
  }

  /* FAQ Section */
  .faq-section {
    padding: 8rem 0;
    background: var(--light-bg);
  }

  .faq-container {
    max-width: 900px;
    margin: 4rem auto 0;
  }

  .faq-categories {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 3rem;
  }

  .category-btn {
    padding: 1rem 2rem;
    border: none;
    border-radius: 30px;
    background: var(--white);
    color: var(--text-color);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .category-btn.active {
    background: var(--primary-color);
    color: var(--white);
  }

  .faq-item {
    background: var(--white);
    border-radius: 10px;
    margin-bottom: 1rem;
    overflow: hidden;
  }

  .faq-question {
    width: 100%;
    padding: 1.5rem;
    text-align: left;
    background: none;
    border: none;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-color);
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .faq-question i {
    transition: transform 0.3s ease;
  }

  .faq-question.active i {
    transform: rotate(180deg);
  }

  .faq-answer {
    padding: 0 1.5rem 1.5rem;
    color: var(--text-color);
    line-height: 1.6;
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
    .hero-content h1 {
      font-size: 2.5rem;
    }

    .hero-content .highlight {
      font-size: 1.5rem;
    }

    .process-timeline::before {
      left: 30px;
    }

    .timeline-item {
      flex-direction: column;
      align-items: flex-start;
      padding-left: 60px;
    }

    .timeline-icon {
      position: absolute;
      left: 0;
      top: 0;
    }

    .timeline-content {
      margin-left: 0;
      margin-top: 1.5rem;
      width: 100%;
    }

    .faq-categories {
      flex-wrap: wrap;
    }
  }

  @media (max-width: 576px) {
    .hero-content h1 {
      font-size: 2rem;
    }

    .cta-buttons {
      flex-direction: column;
    }

    .btn {
      width: 100%;
    }

    .category-btn {
      width: 100%;
    }
  }

  .timeline-icon:hover {
    background: var(--secondary-color);
  }

  .category-btn.active {
    background: var(--primary-color);
  }

  .faq-question.active {
    color: var(--primary-color);
  }
</style> 