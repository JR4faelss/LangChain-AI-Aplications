from langchain_google_genai import ChatGoogleGenerativeAI

chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.messages import HumanMessage, SystemMessage

mensagens = [
    SystemMessage(content='Você é um especialista em esportes no geral.'),
    HumanMessage(content=input('Digite sua dúvida: '))
]
resposta = chat.invoke(mensagens)