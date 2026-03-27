import openai
from gtts import gTTS
import os

# Configuração da API (Deixamos pronto para o usuário inserir sua própria chave)
# No GitHub, por segurança, não subimos a chave real.
api_key = "SUA_CHAVE_OPENAI_AQUI"
client = openai.OpenAI(api_key=api_key)

def pipeline_assistente_voz(caminho_audio):
    """
    Função que realiza o pipeline completo:
    1. Transcreve áudio com Whisper.
    2. Gera resposta com ChatGPT.
    3. Converte resposta em áudio com gTTS.
    """
    try:
        # --- 1. TRANSCRIÇÃO (Speech-to-Text) ---
        with open(caminho_audio, "rb") as audio:
            transcricao = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio
            )
            pergunta = transcricao.text
        
        # --- 2. INTELIGÊNCIA (ChatGPT) ---
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pergunta}]
        )
        texto_resposta = resposta.choices[0].message.content
        
        # --- 3. VOZ (Text-to-Speech) ---
        tts = gTTS(text=texto_resposta, lang='pt')
        tts.save("resposta.mp3")
        
        return texto_resposta

    except Exception as e:
        return f"Erro no processamento: {e}"

# Exemplo de execução (Comentado para evitar erro sem arquivo de áudio)
# if __name__ == "__main__":
#     resultado = pipeline_assistente_voz("meu_audio.mp3")
#     print(f"ChatGPT: {resultado}")
