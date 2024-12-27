<script>
  import { page } from '$app/stores';
  import { fly } from 'svelte/transition';
  import { base } from '$app/paths';
  
  let isMenuOpen = false;

  const menuItems = [
    { id: "home", label: "Inicio", href: "/" },
    { id: "about", label: "Quiénes Somos", href: "/quienes-somos" },
    { id: "answers", label: "Respuestas", href: "/respuestas" },
    { id: "advantages", label: "Ventajas", href: "/ventajas" },
    { id: "investment", label: "Inversión", href: "/inversion" },
    { id: "contact", label: "Contacto", href: "/contacto" }
  ];

  function handleNavigation(event, item) {
    event.preventDefault();
    if (item.href.startsWith('/#')) {
      const id = item.href.replace('/#', '');
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    } else {
      window.location.href = item.href;
    }
    isMenuOpen = false;
  }

  $: isActive = (href) => $page.url.pathname === href || ($page.url.pathname === '/' && href === '/');
</script>

<header class="header">
  <div class="header-content">
    <div class="logo">
      <a href="{base}/" class="logo-link">
        <img src="{base}/assets/Logo_Color.png" alt="MedPre Logo" class="logo-image" />
      </a>
    </div>

    <nav class="desktop-menu">
      {#each menuItems as item}
        <a 
          href={item.href}
          class="nav-link {isActive(item.href) ? 'active' : ''}"
          on:click={(event) => handleNavigation(event, item)}
        >
          {item.label}
          {#if isActive(item.href)}
            <span class="active-indicator"></span>
          {/if}
        </a>
      {/each}
    </nav>

    <button 
      class="mobile-menu-button" 
      on:click={() => isMenuOpen = !isMenuOpen}
      aria-label="Menu"
    >
      <span class="hamburger {isMenuOpen ? 'open' : ''}"></span>
    </button>
  </div>

  {#if isMenuOpen}
    <nav class="mobile-menu" transition:fly={{ y: -20, duration: 300 }}>
      {#each menuItems as item}
        <a 
          href={item.href}
          class="nav-link {isActive(item.href) ? 'active' : ''}"
          on:click={(event) => handleNavigation(event, item)}
        >
          {item.label}
        </a>
      {/each}
    </nav>
  {/if}
</header>

<style>
  .header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: var(--white);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
  }

  .header-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .logo {
    display: flex;
    align-items: center;
  }

  .logo-link {
    display: flex;
    align-items: center;
    text-decoration: none;
  }

  .logo-image {
    height: 60px;
    width: auto;
    object-fit: contain;
    transition: all 0.3s ease;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
  }

  .logo-link:hover .logo-image {
    transform: scale(1.02);
    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.15));
  }

  .logo-image path {
    transition: all 0.3s ease;
  }

  .logo-link:hover .logo-image path {
    stroke-width: 22px;
  }

  .logo-image text {
    transition: all 0.3s ease;
  }

  .logo-link:hover .logo-image text {
    filter: brightness(1.1);
  }

  .brand-name {
    font-size: 1.8rem;
    font-weight: bold;
    color: var(--primary-color);
  }

  .desktop-menu {
    display: flex;
    gap: 1rem;
  }

  .nav-link {
    position: relative;
    padding: 0.8rem 1.2rem;
    color: var(--text-color);
    font-size: 1rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.3s ease;
    border-radius: 8px;
    font-family: var(--font-primary);
    font-weight: var(--font-weight-medium);
  }

  .nav-link:hover {
    color: var(--secondary-color);
    background: rgba(12, 186, 184, 0.1);
  }

  .nav-link.active {
    color: var(--primary-color);
    font-weight: var(--font-weight-semibold);
    background: rgba(12, 186, 184, 0.1);
  }

  .active-indicator {
    position: absolute;
    bottom: -2px;
    left: 50%;
    transform: translateX(-50%);
    width: 24px;
    height: 3px;
    background: var(--secondary-color);
    border-radius: 2px;
  }

  .mobile-menu-button {
    display: none;
    background: none;
    border: none;
    padding: 1rem;
    cursor: pointer;
  }

  .hamburger {
    display: block;
    width: 24px;
    height: 2px;
    background: var(--text-color);
    position: relative;
    transition: all 0.3s ease;
  }

  .hamburger::before,
  .hamburger::after {
    content: '';
    position: absolute;
    width: 24px;
    height: 2px;
    background: var(--text-color);
    transition: all 0.3s ease;
  }

  .hamburger::before {
    top: -8px;
  }

  .hamburger::after {
    bottom: -8px;
  }

  .hamburger.open {
    background: transparent;
  }

  .hamburger.open::before {
    transform: rotate(45deg);
    top: 0;
  }

  .hamburger.open::after {
    transform: rotate(-45deg);
    bottom: 0;
  }

  .mobile-menu {
    display: none;
    padding: 1rem;
    background: var(--white);
    border-top: 1px solid var(--light-bg);
  }

  @media (max-width: 1024px) {
    .header-content {
      padding: 1rem;
    }

    .nav-link {
      padding: 0.6rem 1rem;
      font-size: 0.95rem;
    }

    .logo-image {
      height: 50px;
    }
  }

  @media (max-width: 768px) {
    .desktop-menu {
      display: none;
    }

    .mobile-menu-button {
      display: block;
    }

    .mobile-menu {
      display: flex;
      flex-direction: column;
      padding: 1rem;
    }

    .mobile-menu .nav-link {
      padding: 1rem;
      width: 100%;
      text-align: left;
      border-radius: 8px;
    }

    .logo-image {
      height: 45px;
    }
  }

  @media (max-width: 576px) {
    .header-content {
      padding: 0.8rem;
    }

    .logo-image {
      height: 40px;
    }
  }

  .logo-link {
    display: flex;
    align-items: center;
    gap: 1rem;
    text-decoration: none;
  }

  .nav-link {
    text-decoration: none;
    /* ... resto de estilos existentes para nav-link ... */
  }

  button.nav-link {
    font-family: inherit;
  }
</style> 