const isMobile = window.innerWidth <= 768;
const threshold = isMobile ? 0.2 : 0.5;

export function setupScrollAnimations() {
  const options = {
    threshold: threshold,
    rootMargin: isMobile ? '0px' : '50px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, options);

  const elements = document.querySelectorAll('.scroll-reveal, .section');
  elements.forEach(el => observer.observe(el));
} 