import openai

# Define tu clave de API de OpenAI
api_key = "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"

def obtener_preguntas_sobre_tema(tema):
    # Tu consulta a GPT-3.5 para obtener preguntas sobre el tema
    consulta = f"Genera preguntas sobre el tema: {tema}"
    
    # Llama a la API de GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-003",  # El motor de GPT-3.5
        prompt=consulta,
        max_tokens=50,  # Número máximo de tokens en la respuesta
        api_key=api_key
    )
    
    # Analiza y muestra las preguntas generadas
    preguntas_generadas = response.choices[0].text.strip()
    return preguntas_generadas

if __name__ == "__main__":
    tema = "Inteligencia Artificial"  # Reemplaza con el tema que desees
    preguntas = obtener_preguntas_sobre_tema(tema)
    
    print("Preguntas generadas sobre el tema:")
    print(preguntas)
