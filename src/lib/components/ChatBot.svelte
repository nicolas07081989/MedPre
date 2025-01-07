<script>
  import { fade, fly } from 'svelte/transition';
  import { onMount } from 'svelte';

  let isOpen = false;
  let message = '';
  let chatHistory = [];
  let chatContainer;
  let isTyping = false;

  // Simular respuestas del chatbot (esto deberías reemplazarlo con tu API real)
  const getBotResponse = async (userMessage) => {
    isTyping = true;
    
    // Simular delay de respuesta
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    const responses = {
      default: "¿Cómo puedo ayudarte hoy?",
      greeting: ["hola", "hello", "hi", "buenos días", "buenas tardes", "buenas noches"],
      farewell: ["adiós", "chao", "hasta luego", "bye"],
      services: ["servicios", "qué ofrecen", "qué hacen"],
      contact: ["contacto", "contactar", "teléfono", "email", "correo"]
    };

    const userMessageLower = userMessage.toLowerCase();

    if (responses.greeting.some(word => userMessageLower.includes(word))) {
      return "¡Hola! ¿En qué puedo ayudarte hoy?";
    } else if (responses.farewell.some(word => userMessageLower.includes(word))) {
      return "¡Hasta luego! Que tengas un excelente día.";
    } else if (responses.services.some(word => userMessageLower.includes(word))) {
      return "Ofrecemos servicios de medicina de precisión. ¿Te gustaría conocer más detalles?";
    } else if (responses.contact.some(word => userMessageLower.includes(word))) {
      return "Puedes contactarnos al correo contacto@medpre.com o al teléfono +123456789";
    }

    return "Gracias por tu mensaje. ¿Hay algo específico en lo que pueda ayudarte?";
  };

  const sendMessage = async () => {
    if (!message.trim()) return;

    // Agregar mensaje del usuario
    chatHistory = [...chatHistory, { 
      text: message, 
      isUser: true,
      timestamp: new Date().toLocaleTimeString()
    }];
    
    const userMessage = message;
    message = '';

    // Obtener y agregar respuesta del bot
    const botResponse = await getBotResponse(userMessage);
    isTyping = false;
    
    chatHistory = [...chatHistory, { 
      text: botResponse, 
      isUser: false,
      timestamp: new Date().toLocaleTimeString()
    }];

    // Scroll al último mensaje
    setTimeout(() => {
      if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
      }
    }, 100);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };
</script>

<div class="chatbot-container">
  <!-- Botón flotante del chat -->
  <button 
    class="chat-button"
    on:click={() => isOpen = !isOpen}
    class:open={isOpen}
  >
    {#if !isOpen}
      <i class="fas fa-comments"></i>
    {:else}
      <i class="fas fa-times"></i>
    {/if}
  </button>

  <!-- Ventana del chat -->
  {#if isOpen}
    <div 
      class="chat-window"
      in:fly={{ y: 50, duration: 300 }}
      out:fade
    >
      <!-- Encabezado -->
      <div class="chat-header">
        <img src="/images/logos/Isotipo_Color.png" alt="Logo" class="chat-logo"/>
        <div class="header-text">
          <h3>Asistente MedPre</h3>
          <span class="status">En línea</span>
        </div>
      </div>

      <!-- Mensajes -->
      <div class="chat-messages" bind:this={chatContainer}>
        <!-- Mensaje de bienvenida -->
        {#if chatHistory.length === 0}
          <div class="message bot-message" in:fade>
            <div class="message-content">
              ¡Hola! Soy el asistente virtual de MedPre. ¿En qué puedo ayudarte?
            </div>
            <span class="timestamp">{new Date().toLocaleTimeString()}</span>
          </div>
        {/if}

        <!-- Historial de mensajes -->
        {#each chatHistory as message}
          <div 
            class="message {message.isUser ? 'user-message' : 'bot-message'}"
            in:fade
          >
            <div class="message-content">
              {message.text}
            </div>
            <span class="timestamp">{message.timestamp}</span>
          </div>
        {/each}

        <!-- Indicador de escritura -->
        {#if isTyping}
          <div class="message bot-message typing" in:fade>
            <div class="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        {/if}
      </div>

      <!-- Input del mensaje -->
      <div class="chat-input">
        <textarea
          bind:value={message}
          on:keypress={handleKeyPress}
          placeholder="Escribe tu mensaje..."
          rows="1"
        ></textarea>
        <button 
          on:click={sendMessage}
          disabled={!message.trim()}
        >
          <i class="fas fa-paper-plane"></i>
        </button>
      </div>
    </div>
  {/if}
</div>

<style>
  .chatbot-container {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    z-index: 1000;
  }

  .chat-button {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--color-primary, #4a90e2);
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .chat-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
  }

  .chat-button.open {
    background: #e74c3c;
  }

  .chat-window {
    position: absolute;
    bottom: 80px;
    right: 0;
    width: 350px;
    height: 500px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .chat-header {
    padding: 1rem;
    background: var(--color-primary, #4a90e2);
    color: white;
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .chat-logo {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
    background: white;
    padding: 5px;
  }

  .header-text {
    flex: 1;
  }

  .header-text h3 {
    margin: 0;
    font-size: 1.1rem;
  }

  .status {
    font-size: 0.8rem;
    opacity: 0.8;
  }

  .chat-messages {
    flex: 1;
    padding: 1rem;
    overflow-y: auto;
    background: #f8f9fa;
  }

  .message {
    margin-bottom: 1rem;
    max-width: 80%;
    display: flex;
    flex-direction: column;
  }

  .bot-message {
    align-self: flex-start;
  }

  .user-message {
    align-self: flex-end;
  }

  .message-content {
    padding: 0.8rem 1rem;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .bot-message .message-content {
    background: white;
    color: #333;
  }

  .user-message .message-content {
    background: var(--color-primary, #4a90e2);
    color: white;
  }

  .timestamp {
    font-size: 0.7rem;
    color: #666;
    margin-top: 0.3rem;
    align-self: flex-end;
  }

  .typing-indicator {
    display: flex;
    gap: 0.3rem;
    padding: 0.5rem 1rem;
  }

  .typing-indicator span {
    width: 8px;
    height: 8px;
    background: #90a4ae;
    border-radius: 50%;
    animation: bounce 1.4s infinite ease-in-out;
  }

  .typing-indicator span:nth-child(1) { animation-delay: -0.32s; }
  .typing-indicator span:nth-child(2) { animation-delay: -0.16s; }

  @keyframes bounce {
    0%, 80%, 100% { transform: scale(0); }
    40% { transform: scale(1); }
  }

  .chat-input {
    padding: 1rem;
    background: white;
    border-top: 1px solid #eee;
    display: flex;
    gap: 0.5rem;
  }

  textarea {
    flex: 1;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    resize: none;
    font-family: inherit;
    font-size: 0.9rem;
    line-height: 1.4;
  }

  textarea:focus {
    outline: none;
    border-color: var(--color-primary, #4a90e2);
  }

  .chat-input button {
    width: 40px;
    height: 40px;
    border-radius: 8px;
    border: none;
    background: var(--color-primary, #4a90e2);
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .chat-input button:disabled {
    background: #ccc;
    cursor: not-allowed;
  }

  .chat-input button:not(:disabled):hover {
    transform: scale(1.05);
  }

  @media (max-width: 480px) {
    .chat-window {
      width: calc(100vw - 4rem);
      height: calc(100vh - 100px);
      bottom: 80px;
    }

    .chatbot-container {
      bottom: 1rem;
      right: 1rem;
    }
  }
</style> 