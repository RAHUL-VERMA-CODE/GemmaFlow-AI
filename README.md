# 🤖 GemmaFlow AI

A private, local AI chatbot interface built using **Streamlit**, **LangChain**, **Ollama**, and **Gemma**. GemmaFlow AI lets you interact with open-weight Gemma models locally with integrated observability through **LangSmith**.

---

## 📷 Interface Preview
![alt text](<frontend.png>)

---

## ✨ Key Features

- **100% Local Inference:** Powered by Ollama running Google's Gemma models (`gemma:2b`, `gemma2:2b`) entirely on your machine.
- **Interactive Chat Interface:** Clean UI rendered using Streamlit chat components.
- **Observability Integration:** Built-in tracing with LangSmith via `.env` configuration.
- **Dynamic Model Selection:** Switch models on the fly from the sidebar.
- **Session Management:** Clear chat history with a single click.

---

## 🛠️ Tech Stack

- **Frontend / Framework:** Streamlit
- **LLM Orchestration:** LangChain Core (`ChatPromptTemplate`, `StrOutputParser`)
- **Model Server:** Ollama (`langchain_community.llms.Ollama`)
- **Observability:** LangSmith
- **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

```text
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
