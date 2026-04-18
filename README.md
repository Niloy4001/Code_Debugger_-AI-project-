


# 🚀 Code Debugger (AI Powered)

An AI-powered web application that helps you debug code from screenshots. Built using Streamlit and Google Gemini API, this tool provides step-by-step hints or full corrected solutions based on uploaded code images.

---

## 🌐 Live Demo

🔗 Live App: [https://your-live-link-here ](https://correct-your-code-40.streamlit.app/) 
🔗 GitHub Repo: [https://github.com/your-username/your-repo](https://github.com/Niloy4001/Code_Debugger_-AI-project-)

---

## ✨ Features

- 📤 Upload up to 3 code screenshots  
- 🧠 AI-generated debugging hints  
- 💡 Option to get full corrected solution with code  
- 🖼️ Preview uploaded images  
- ⚡ Simple and clean Streamlit UI  
- 🔥 Fast AI response using Gemini API  

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit  
- Google Gemini API  

---

## 📂 Project Structure

```

.
├── app.py
├── api_calling.py
├── .env
├── requirements.txt
└── README.md

````

---

## ⚙️ How It Works

1. User uploads code screenshots  
2. Images are processed using PIL  
3. Images are sent to Google Gemini API  
4. AI analyzes the code  
5. Returns:
   - Step-by-step hints (no code) OR  
   - Full corrected solution with code  

---

## 🚀 Installation & Run Locally

```bash
# Clone repository
git clone https://github.com/your-username/your-repo.git

# Move into project folder
cd your-repo

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
````

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 💡 Future Improvements

* 🌍 Multi-language code support
* 🧠 Better error detection accuracy
* 🌙 Dark mode UI
* 📜 History of previous debugging sessions
* 📱 Mobile-friendly UI improvements



---

## ⭐ Support

If you like this project, please ⭐ star the repository and share it with others!


