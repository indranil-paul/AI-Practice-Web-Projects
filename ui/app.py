import streamlit as st
from components.chatbot import ChatBot


PAGE_TITLE = "AI Practice Web Projects"
PAGE_ICON = ":robot:"
PAGE_LAYOUT = "centered"


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    initialize_session_state()
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=PAGE_LAYOUT)
    chatbot = ChatBot()
    chatbot.render_chatbot()


if __name__ == "__main__":
    main()
