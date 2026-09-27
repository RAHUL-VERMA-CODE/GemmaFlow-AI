

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# LangSmith configuration
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = os.getenv(
        "LANGCHAIN_PROJECT",
        "GemmaFlow AI"
    )

# --------------------------------------------------
# Streamlit page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="GemmaFlow AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #777;
        margin-bottom: 30px;
    }

    .model-card {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("### Model")

    model_name = st.selectbox(
        "Select Ollama model",
        [
            "gemma:2b",
            "gemma2:2b"
        ],
        index=0
    )

    st.markdown("---")

    st.markdown("### 🧠 About")

    st.write(
        "GemmaFlow AI is a local AI assistant built "
        "using LangChain, Ollama, Gemma and Streamlit."
    )

    st.markdown("---")

    st.markdown("### 🔍 Observability")

    if os.getenv("LANGCHAIN_API_KEY"):
        st.success("LangSmith: Connected")
    else:
        st.warning("LangSmith: Not configured")

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --------------------------------------------------
# Main UI
# --------------------------------------------------
st.markdown(
    '<div class="main-title">🤖 GemmaFlow AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A private local AI assistant powered by LangChain + Ollama + Gemma'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Initialize chat history
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Display previous messages
# --------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Prompt template
# --------------------------------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are GemmaFlow AI, a helpful and concise AI assistant. "
            "Answer the user's question clearly and accurately."
        ),
        (
            "user",
            "{question}"
        )
    ]
)

# --------------------------------------------------
# Ollama Gemma model
# --------------------------------------------------
llm = Ollama(
    model=model_name
)

# --------------------------------------------------
# Output parser
# --------------------------------------------------
output_parser = StrOutputParser()

# --------------------------------------------------
# LangChain pipeline
# --------------------------------------------------
chain = prompt | llm | output_parser

# --------------------------------------------------
# Chat input
# --------------------------------------------------
user_input = st.chat_input(
    "Ask GemmaFlow AI anything..."
)

# --------------------------------------------------
# Generate response
# --------------------------------------------------
if user_input:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = chain.invoke(
                    {
                        "question": user_input
                    }
                )

                st.markdown(response)

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {str(e)}"
                )


