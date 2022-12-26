import openai
import os
import streamlit as st

def evaluar_texto(texto):
    # Utiliza GPT-3 para evaluar el texto
    model_engine = "text-davinci-003"
    prompt = (f"Evaluar la calidad del texto:\n{texto}\n\n"
              "Criterios de evaluación: gramática, puntuación y riqueza léxica. "
              "Señalar los errores y dar una calificación.")

    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                           temperature=0.5)
    respuesta = completions.choices[0].text

    # Devuelve la respuesta de GPT-3
    return respuesta

def ocultar_clave(clave):
    # Reemplaza cada carácter de la clave por un punto
    clave_oculta = "." * len(clave)

    return clave_oculta

def main():
    st.title("Evaluador de textos con GPT-3")

    # Muestra un subheader "Evaluador" en el menú
    st.sidebar.subheader("Evaluador")

    # Pide la clave de OpenAI en la barra lateral
    openai_key_input = st.sidebar.text_input("Ingresa tu clave de OpenAI:")
    openai_key = openai_key_input.text

    # Agrega un evento de cambio de texto al widget de entrada de texto
    # para reemplazar los caracteres de la clave por puntos
    @openai_key_input.on_change
    def reemplazar_por_puntos(change):
        openai_key_input.text = ocultar_clave(openai_key)

    if openai_key:
        openai.api_key = openai_key
        
    # Muestra un menú con dos opciones: subir archivo o pegar texto
    opcion = st.sidebar.radio("Selecciona una opción:", ("Subir archivo", "Pegar texto"))

    if opcion == "Subir archivo":
        uploaded_file = st.file_uploader("Selecciona un archivo:")

        if uploaded_file is not None:
            # Lee el contenido del archivo como una cadena de bytes
            file_content = uploaded_file.read()

            # Convierte la cadena de bytes a una cadena de texto
            # Utiliza la codificación utf-8 por defecto, pero puedes especificar otra
            # si el archivo tiene una codificación diferente
            file_content_text = file_content.decode("utf-8")

            # Evalúa el contenido del archivo
            respuesta = evaluar_texto(file_content_text)
            st.markdown(respuesta)

    elif opcion == "Pegar texto":
        texto = st.text_area("Ingresa el texto a evaluar. Al finalizar, Ctrl+Enter")
        if texto:
            respuesta = evaluar_texto(texto)
            st.markdown(respuesta)

if __name__ == "__main__":
    main()
