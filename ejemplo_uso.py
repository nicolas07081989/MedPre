from chatbot_medpre import ChatbotMedPre

def main():
    chatbot = ChatbotMedPre()
    
    print("=== ChatBot MedPre ===")
    print("Bienvenido al asistente virtual de MedPre")
    
    while True:
        print("\n" + chatbot.mostrar_menu())
        opcion = input("\nTú: ").strip()
        
        if opcion.lower() in ['salir', 'exit', 'quit']:
            print("\nGracias por usar el chatbot de MedPre. ¡Hasta pronto!")
            break
            
        respuesta = chatbot.procesar_opcion_menu(opcion)
        print(f"\nMedPre: {respuesta}")

if __name__ == "__main__":
    main() 