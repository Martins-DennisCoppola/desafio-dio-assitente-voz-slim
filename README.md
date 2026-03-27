# desafio-dio-assitente-voz-slim
Rio de Janeiro | Projeto de assistente de voz utilizando Whisper e GPT-3.5 para o desafio prático da DIO.

#  Assistente de Voz com Inteligência Artificial

Este projeto é um desafio prático da **DIO** que cria um assistente de voz completo. Ele "ouve" um áudio, entende o que foi dito usando IA e responde falando de volta.

##  Como o projeto funciona:
O sistema segue três passos simples:
1. **Ouve:** Transcreve o áudio para texto usando o **Whisper** (OpenAI).
2. **Pensa:** Envia o texto para o **ChatGPT** para gerar uma resposta inteligente.
3. **Fala:** Transforma a resposta do texto em áudio usando o **gTTS** (Google).

##  Onde foi desenvolvido:
O projeto foi criado e testado no **Google Colab**, utilizando a linguagem **Python**.

##  O que você precisa para rodar:
1. Uma chave de API da **OpenAI**.
2. As seguintes bibliotecas instaladas (o código já faz isso):
   - `openai`
   - `gTTS`

##  Arquivos no Repositório:
- `assistente_voz.py`: O código principal do projeto.
- `README.md`: Explicação do projeto (este arquivo).
- `LICENSE`: Licença MIT de uso do código.

---
Projeto desenvolvido por **Dennis Coppola MArtins** para o bootcamp Bradesco - GenAI & Dados.
