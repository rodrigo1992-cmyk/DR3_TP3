import streamlit as st
from agent import *

st.title("Music Industry Chatbot")
st.subheader("Please ask a question in english to get started.")

# -----------------INICIALIZAÇÃO--------------------
# Inicializar variável de ambiente
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I will help you find any information about the music industry. Please ask a question to get started."}]

# Exibe as mensagens armazenadas no histórico  (Se não tiver essa parte toda vez que é digitada uma nova mensagem o chat é limpo)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------USUÁRIO--------------------
# Cria a caixa de input e exibe um placeholder. Se foi digitado algo na caixa, atribui o valor a variável user_input
if user_input := st.chat_input("Digite aqui"):

    # Exibe no chat a mensagem que o usuário havia inputado
    with st.chat_message("user"): 
        st.markdown(user_input)

    # Adiciona a mensagem do usuário na variável de ambiente (histórico de mensagens)
    st.session_state.messages.append({"role": "user", "content": user_input})


    #-----------------CHAMADA AO LLM-------------------
    # Adicionar spinner enquanto está aguardando a resposta do LLM

    with st.chat_message("assistant"): 
        with st.spinner("Aguarde alguns instantes..."):    
            try:
                response = ask_to_lmm(user_input)
                st.write(response['output'])

                st.session_state.messages.append({"role": "assistant", "content": response['output']})
                
            except:
                st.write("Sorry, I had a difficulty and unfortunately I won't be able to help you right now. Please try again later.")

    