import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import pyttsx3

# Instalar las bibliotecas si no están instaladas
# pip install SpeechRecognition pyttsx3

# Inicializar el reconocedor de voz y el sintetizador de voz
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Función para reconocer el habla del usuario
def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Utilizar el reconocimiento de voz de Google
            text = recognizer.recognize_google(audio, language="es-ES")
            return text
        except sr.UnknownValueError:
            return "Lo siento, no pude entender lo que dijiste."
        except sr.RequestError:
            return "Lo siento, parece que hay un problema con el servicio de reconocimiento de voz."

# Función para generar la respuesta de voz
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para manejar la entrada de texto
def process_input():
    user_input = entry.get()
    entry.delete(0, tk.END)
    response = ": " + user_input
    speak(response)
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, response + "\n")
    text_output.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()
root.title("Asistente de Voz")

# Crear la caja de entrada de texto
entry = ttk.Entry(root, width=50)
entry.pack(pady=10)
entry.focus()

# Crear el botón de enviar
send_button = ttk.Button(root, text="Enviar", command=process_input)
send_button.pack()

# Crear el área de texto de salida
text_output = tk.Text(root, height=10, width=50)
text_output.pack(pady=10)
text_output.config(state=tk.DISABLED)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
