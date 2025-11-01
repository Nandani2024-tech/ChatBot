# 💬 AI Chatbot

A fully functional **AI-powered chatbot** built with **Flask**, **PyTorch**, and **Hugging Face Transformers**.  
This chatbot can understand natural language queries and respond intelligently using a pre-trained NLP model.

---

## 🚀 Features

- 🧠 Conversational AI powered by `transformers`
- ⚡ Lightweight Flask web interface
- 💬 Context-aware text responses
- 🌐 Easy local or cloud deployment
- 🔒 `.env` support for configuration and API keys

---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Python 3.13** | Core language |
| **Flask** | Backend web framework |
| **Transformers** | NLP model utilities |
| **PyTorch (Nightly)** | Deep learning backend for model inference |
| **python-dotenv** | Manage environment variables |

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nandani2024-tech/Chatbot.git
cd Chatbot



2️⃣ Create and Activate a Virtual Environment
py -3.13 -m venv venv
venv\Scripts\activate


3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt


If you’re on Python 3.13, PyTorch must be installed manually:

pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu

4️⃣ Set Up Environment Variables

Create a .env file in your project’s root directory:

MODEL_NAME=distilgpt2
PORT=5000


(You can change MODEL_NAME to any Hugging Face model name if desired.)

5️⃣ Run the Chatbot
python app.py



Once it starts, open your browser and visit:
👉 http://127.0.0.1:5000

🧠 Example Questions

Try chatting with:

“Hi, how are you?”

“Tell me a joke.”

“Explain quantum computing in simple terms.”

“Write a short poem about coding.”

“Who created you?”

“Generate a Python function to reverse a string.”


📁 Folder Structure
Chatbot/
│
├── app.py              # Main Flask application
├── requirements.txt    # Dependency list
├── .env                # Environment variables (not tracked)
├── templates/          # Frontend HTML templates
├── static/             # JS/CSS/Assets
├── venv/               # Virtual environment (ignored)
└── README.md           # Project documentation

🛡️ Notes

Ensure your .env file is NOT committed to GitHub.

Works best on Python 3.12+.

For deployment (Render, Heroku, etc.), configure environment variables directly in your hosting dashboard.

💖 Credits

Developed by Nandani Kumari
AI model powered by Hugging Face Transformers and PyTorch.
Built with ❤️ using Flask.