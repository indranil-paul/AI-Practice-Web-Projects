import streamlit as st
from services.chatbot_service import ChatBotService


CHATBOT_TITLE = "Simple Chatbot :robot:"
SESSION_ID = "123"  # Placeholder for session management, can be replaced with a unique identifier


class ChatBot:

    def __init__(self):
        # Initialize the ChatBotService instance for handling API interactions
        self.service = ChatBotService()
        # self.start_session()

    def __del__(self):
        # self.end_session()
        pass  # Placeholder for any cleanup logic if needed

    def start_session(self):
        pass  # Placeholder for any session initialization logic if needed

    def end_session(self):
        pass  # Placeholder for any session cleanup logic if needed 

    def render_chatbot(self):
        st.title(CHATBOT_TITLE)
        st.divider()

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        prompt = st.chat_input("Ask anything...")
        if not prompt:
            return
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt) 

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = self.service.send_message(message=prompt, session_id=SESSION_ID)
                except Exception:
                    st.error("Error: Failed to send message")
                else:
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
