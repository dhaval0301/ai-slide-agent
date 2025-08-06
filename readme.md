




````markdown
#  Slide Agent — Autonomous Slide Generator with AI

An Agentic AI-powered tool that **automatically creates professional slide decks** based on a topic and target audience. It generates:
- Slide structure
- Slide content
- Speaker notes
- AI-generated visuals (via DALL·E)
- Optionally exports to Google Slides or PDF

Ideal for:
- Teachers
- Content creators
- Startup founders
- Anyone who hates making slides manually 😅


##  Features

- 🔍 Understands a topic + audience context
- 🪄 Generates multi-slide structure and talking points
- 📝 Adds speaker notes per slide
- 🖼️ Auto-generates relevant visuals using DALL·E
- 📤 Export to **Google Slides** or download as **PDF**
- 🧠 Built using agentic AI logic with modular tasks

---

##  Tech Stack

| Layer         | Tools Used                          |
|---------------|--------------------------------------|
| Language Model| OpenAI GPT-4-turbo                   |
| Agents        | Custom modular functions             |
| PDF Export    | FPDF with Unicode support            |
| UI            | Streamlit                            |
| Image Gen     | DALL·E (OpenAI Image API)            |
| Cloud Slides  | Google Slides API                    |

---

##  Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/dhaval0301/ai-slide-agent.git
cd slide-agent
````

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  API Keys Required

To use this project, you must set up credentials for:

###  OpenAI API

* Sign up at [OpenAI](https://platform.openai.com/)
* Create an API key and add it to your `.env` file as:

```env
OPENAI_API_KEY=your-openai-key
```

---

###  Google Slides API

* Go to [Google Cloud Console](https://console.cloud.google.com/)
* Create a project and enable the **Google Slides API** and **Drive API**
* Create **OAuth 2.0 Credentials**
* Download `credentials.json` and place it in the project root
* On first run, a browser will open for Google login and token storage

---

## Run the App

```bash
streamlit run main.py
```

---

##  Export Options

You can export your slides in two ways:

* **PDF** (via FPDF)
* **Google Slides** (requires login + access approval)

---

##  Project Structure

```
slide-agent/
├── main.py
├── agents.py
├── utils.py
├── google_slides.py
├── requirements.txt
├── credentials.json     # Google OAuth credentials
├── output/              # Generated PDFs + fonts
└── README.md
```

---

##  Sample Prompt

```text
Topic: The Role of AI in Healthcare
Target Audience: High school students
```

The agent will then generate:

* Title & outline
* Slide-by-slide content
* Speaker notes
* DALL·E images
* Export buttons

---

## Upcoming Features

* 🌐 Add voice narration
* 🎨 Add theme templates
* 📊 Add charts with CSV input
* 💼 Google Slides formatting improvements

##  Credits

Built by Dhaval Ingale using OpenAI, Streamlit, and Google APIs.
Inspired by the power of agentic automation.

---


