<script>
  let isOpen = false;
  
  function toggleChat() {
    isOpen = !isOpen;
  }
</script>

<div class="chatbot {isOpen ? 'open' : ''}">
  <div class="chatbot-button">
    <button on:click={toggleChat}>
      <img src="/icons/misc/chatbot.svg" alt="Chat" class="chatbot-icon" />
    </button>
  </div>
  
  {#if isOpen}
    <div class="chat-window">
      <div class="chat-header">
        <h3>Chat con MedPre</h3>
        <button on:click={toggleChat}>
          <i class="fas fa-times"></i>
        </button>
      </div>
      <!-- Contenido del chat -->
    </div>
  {/if}
</div>

<style>
  .chatbot {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    z-index: 1000;
  }

  .chat-toggle {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--primary-color);
    color: white;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .chat-window {
    position: absolute;
    bottom: 80px;
    right: 0;
    width: 300px;
    height: 400px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .chatbot-icon {
    width: 24px;
    height: 24px;
    filter: invert(100%);
  }
</style> 