<script>
  import { page } from '$app/stores';
</script>

<div class="error-container">
  <h1>{$page.status}: {$page.error?.message}</h1>
  <a href="/" class="btn btn-primary">Volver al inicio</a>
</div>

<style>
  .error-container {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 2rem;
  }

  h1 {
    color: var(--primary-color);
    margin-bottom: 2rem;
  }
</style> 