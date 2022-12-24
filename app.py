import openai
import os
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")



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

    texto = st.text_area("Ingresa el texto a evaluar. Al finalizar, Ctrl+Enter")
    if texto:
        respuesta = evaluar_texto(texto)
        st.markdown(respuesta)
