import webbrowser
from urllib.parse import quote

class ChatbotMedPre:
    def __init__(self):
        # Información base de MedPre
        self.info = {
            'contacto': {
                'whatsapp': '593979136217',  # Formato para link de WhatsApp
                'whatsapp_display': '(+593) 97 913 6217',  # Formato para mostrar
                'email': 'medpre.ecuador@gmail.com',
                'web': 'www.precisionecuador.com'
            },
            'precios': {
                'estudio': 1300
            }
        }
        
        # Preguntas frecuentes
        self.faqs = {
            '1': '¿Qué es un nódulo tiroideo grado III o IV?',
            '2': '¿Cómo funciona el estudio molecular?',
            '3': '¿Cuál es el costo del estudio?',
            '4': '¿Qué ventajas tiene frente a la cirugía?',
            '5': '¿Cómo puedo contactarlos?',
            '6': 'Abrir WhatsApp',
            '7': 'Enviar correo',
            '8': 'Ver todas las preguntas frecuentes'
        }

    def mostrar_menu(self) -> str:
        menu = (
            "Seleccione una opción:\n\n"
            "1. ¿Qué es un nódulo tiroideo grado III o IV?\n"
            "2. ¿Cómo funciona el estudio molecular?\n"
            "3. ¿Cuál es el costo del estudio?\n"
            "4. ¿Qué ventajas tiene frente a la cirugía?\n"
            "5. ¿Cómo puedo contactarlos?\n"
            "6. 📱 Abrir WhatsApp\n"
            "7. 📧 Enviar correo\n"
            "8. ❓ Ver todas las preguntas frecuentes\n"
            "9. 💬 Hacer otra pregunta\n"
            "\nEscriba el número de su elección o su pregunta:"
        )
        return menu

    def abrir_whatsapp(self):
        """Abre WhatsApp Web con el número predefinido"""
        numero = self.info['contacto']['whatsapp']
        mensaje = quote("Hola, me gustaría información sobre el estudio molecular MIR-THYPE Full")
        url = f"https://wa.me/{numero}?text={mensaje}"
        webbrowser.open(url)
        return "Abriendo WhatsApp en su navegador..."

    def abrir_correo(self):
        """Abre el cliente de correo predeterminado"""
        email = self.info['contacto']['email']
        subject = quote("Información sobre estudio molecular")
        url = f"mailto:{email}?subject={subject}"
        webbrowser.open(url)
        return "Abriendo su cliente de correo..."

    def procesar_opcion_menu(self, opcion: str) -> str:
        if opcion == '6':
            return self.abrir_whatsapp()
        elif opcion == '7':
            return self.abrir_correo()
        elif opcion == '8':
            return self.mostrar_todas_faqs()
        elif opcion == '9':
            return "Por favor, escriba su pregunta:"
        elif opcion in self.faqs:
            return self.generar_respuesta(self.faqs[opcion])
        else:
            return self.generar_respuesta(opcion)

    def mostrar_todas_faqs(self) -> str:
        faqs_completas = {
            "¿Qué es un nódulo tiroideo grado III o IV?": (
                "Son nódulos donde el diagnóstico tradicional no puede determinar con certeza "
                "si son benignos o malignos. Solo 2 de cada 10 resultan ser malignos."
            ),
            "¿Cómo funciona el estudio molecular?": (
                "El estudio MIR-THYPE Full analiza marcadores moleculares específicos usando "
                "la misma muestra de la primera biopsia, sin procedimientos adicionales."
            ),
            "¿Cuál es el costo?": (
                f"El costo es ${self.info['precios']['estudio']} (IVA incluido). Incluye envío de "
                "muestras, estudio completo y consulta con especialista."
            ),
            "¿Cuánto demoran los resultados?": (
                "Los resultados están listos en menos de un mes."
            ),
            "¿Qué tan preciso es el estudio?": (
                "Tiene un valor predictivo negativo del 96% y evita cirugías innecesarias "
                "en el 80% de los casos."
            ),
            "¿Necesito repetir la biopsia?": (
                "No, utilizamos la muestra de su primera biopsia."
            ),
            "¿Aceptan tarjetas de crédito?": (
                "Sí, aceptamos todas las tarjetas de crédito."
            ),
            "¿Cómo agendo una consulta?": (
                f"Puede contactarnos por WhatsApp al {self.info['contacto']['whatsapp_display']} "
                f"o por email a {self.info['contacto']['email']}"
            )
        }
        
        respuesta = "PREGUNTAS FRECUENTES:\n\n"
        for pregunta, respuesta_faq in faqs_completas.items():
            respuesta += f"❓ {pregunta}\n➡️ {respuesta_faq}\n\n"
        
        respuesta += (
            "Para más información:\n"
            f"📱 WhatsApp: {self.info['contacto']['whatsapp_display']}\n"
            f"📧 Email: {self.info['contacto']['email']}"
        )
        return respuesta

    def obtener_intencion(self, mensaje: str) -> str:
        mensaje = mensaje.lower()
        
        for intencion, palabras in self.keywords.items():
            if any(palabra in mensaje for palabra in palabras):
                return intencion
        
        return 'general'

    def generar_respuesta(self, mensaje: str) -> str:
        intencion = self.obtener_intencion(mensaje)
        
        respuestas = {
            'nodulo': (
                "Un nódulo tiroideo de grado III o IV según Bethesda indica una situación donde "
                "el diagnóstico tradicional no puede determinar con certeza si es benigno o maligno.\n\n"
                "Datos importantes:\n"
                "• Solo 2 de cada 10 nódulos indeterminados son malignos\n"
                "• Nuestro estudio molecular puede evitar cirugías innecesarias en el 80% de los casos\n"
                "• Tenemos un valor predictivo negativo del 96%\n\n"
                f"Para más información, contáctenos al WhatsApp: {self.info['contacto']['whatsapp']}"
            ),
            
            'estudio': (
                "El estudio molecular MIR-THYPE Full es un análisis avanzado que:\n\n"
                "✓ Utiliza la misma muestra de su primera biopsia\n"
                "✓ Tiene 96% de precisión\n"
                "✓ Evita cirugías innecesarias\n"
                "✓ Entrega resultados en menos de un mes\n\n"
                f"Para consultas:\n"
                f"📱 WhatsApp: {self.info['contacto']['whatsapp']}\n"
                f"📧 Email: {self.info['contacto']['email']}"
            ),
            
            'precio': (
                f"El estudio molecular tiene un costo de ${self.info['precios']['estudio']} (IVA incluido).\n\n"
                "El precio incluye:\n"
                "✓ Envío de muestras al extranjero\n"
                "✓ Realización del estudio completo\n"
                "✓ Consulta con especialista\n\n"
                "Aceptamos todas las tarjetas de crédito.\n\n"
                f"Para más detalles, contáctenos:\n"
                f"📱 WhatsApp: {self.info['contacto']['whatsapp']}"
            ),
            
            'contacto': (
                "Puede contactarnos a través de:\n\n"
                f"📱 WhatsApp: {self.info['contacto']['whatsapp']}\n"
                f"📧 Email: {self.info['contacto']['email']}\n"
                f"🌐 Web: {self.info['contacto']['web']}\n\n"
                "Nuestro equipo está listo para atenderle."
            ),
            
            'ventajas': (
                "MedPre ofrece importantes ventajas:\n\n"
                "1. Evita cirugías innecesarias en el 80% de los casos\n"
                "2. No requiere repetir la biopsia\n"
                "3. Incluye consulta gratuita con especialista\n"
                "4. Resultados en menos de un mes\n"
                "5. Respaldo de asociaciones internacionales\n"
                "6. Alta precisión (96% valor predictivo negativo)\n\n"
                f"Para más información:\n"
                f"📱 WhatsApp: {self.info['contacto']['whatsapp']}"
            ),
            
            'consulta': (
                "Para una evaluación profesional, contacte directamente con nuestros especialistas:\n\n"
                f"📱 WhatsApp: {self.info['contacto']['whatsapp']}\n"
                f"📧 Email: {self.info['contacto']['email']}"
            ),
            
            'general': (
                "Gracias por contactar a MedPre. Podemos ayudarle con información sobre:\n\n"
                "1. Nódulos tiroideos grado III y IV\n"
                "2. Nuestro estudio molecular MIR-THYPE Full\n"
                "3. Ventajas frente a la cirugía\n"
                "4. Costos y facilidades de pago\n\n"
                "Para contacto directo:\n"
                f"📱 WhatsApp: {self.info['contacto']['whatsapp']}\n"
                f"📧 Email: {self.info['contacto']['email']}"
            )
        }
        
        return respuestas.get(intencion, respuestas['general']) 