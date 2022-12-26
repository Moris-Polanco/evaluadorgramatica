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

def main():
    st.title("Evaluador de textos con GPT-3")

    # Muestra un subheader "Evaluador" en el menú
    st.sidebar.subheader("Evaluador")

    # Pide la clave de OpenAI en la barra lateral
    openai_key_input = st.sidebar.text_input("Ingresa tu clave de OpenAI:", type='password')
    openai_key = openai_key_input.value

    if openai_key:
        openai.api_key = openai_key

    # Muestra un menú con dos opciones: subir archivo o pegar texto
    opcion = st.sidebar.radio("Selecciona una opción:", ["Subir archivo", "Pegar texto"])

    if opcion == "Subir archivo":
        # Pide al usuario que seleccione un archivo
        archivo = st.file_uploader("Selecciona un archivo:")

        if archivo is not None:
            # Lee el contenido del archivo y lo almacena en una variable
            with open(archivo, "r") as f:
                texto = f.read()

            # Evalúa el texto y muestra la respuesta de GPT-3
            respuesta = evaluar_texto(texto)
            st.markdown(respuesta)
    else:
        # Pide al usuario que ingrese el texto
        texto = st.text_area("Ingresa el texto a evaluar. Al finalizar, Ctrl+Enter")

        if texto:
            # Evalúa el texto y muestra la respuesta de GPT-3
            respuesta = evaluar_texto(texto)
            st.markdown(respuesta)


if __name__ == "__main__":
    main()
