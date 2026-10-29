# 🎯 InterviewIQ — AI-Powered Mock Interview & Feedback Assistant

**Practice smarter. Improve faster. Interview with confidence.**

InterviewIQ is an AI-powered mock interview platform that helps candidates practice role-specific interview questions, submit their answers, and receive structured feedback using Google's Gemini API.

The platform provides an interactive interview workspace, AI-generated questions, answer evaluation, scoring breakdowns, suggested answers, and performance reports through a modern Streamlit interface.

## ✨ Features

- **Role-Based Interview Practice:** Supports 90+ target roles across software development, cybersecurity, cloud computing, DevOps, data science, AI/ML, IT operations, and more.
- **Multiple Experience Levels:** Choose Beginner, Intermediate, or Advanced.
- **Flexible Interview Formats:** Practice Technical, HR, or Mixed interviews.
- **AI Question Generation:** Generate interview questions tailored to the selected role, level, and interview type.
- **Structured Answer Evaluation:** Evaluate responses based on technical correctness, relevance, clarity, and completeness.
- **Scoring System:** Receive an overall score out of 10 with a category-wise breakdown.
- **Personalized Feedback:** Identify strengths and areas for improvement.
- **Suggested Answers:** Review an improved answer to understand how to strengthen your response.
- **Follow-Up Questions:** Explore related questions to deepen your understanding.
- **Performance Dashboard:** View evaluation history, average scores, best scores, and score trends during the current application session.
- **Modern User Interface:** Navigate a dark-themed dashboard, interview workspace, and performance report.

## 🖥️ Application Preview

Add screenshots of your application here after capturing them from the running project.

| Dashboard | Mock Interview |
|---|---|
| Add dashboard screenshot | Add interview workspace screenshot |

| AI Evaluation | Performance Report |
|---|---|
| Add evaluation screenshot | Add performance report screenshot |

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| Google Gemini API | Question generation and answer evaluation |
| `google-genai` | Gemini API integration |
| `python-dotenv` | Environment variable management |
| Git and GitHub | Version control and project hosting |

## 📁 Project Structure

```text
InterviewIQ/
├── app.py
├── ai_engine.py
├── test_gemini.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

**Note:** The `.env` file contains your local API key and must not be committed to GitHub. It is listed here to explain the local project setup.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/codebysantusht/InterviewIQ.git
cd InterviewIQ
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Obtain an API key through [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own API key. Never publish your real API key in source code or commit it to GitHub.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use InterviewIQ.

## 🧠 How It Works

1. **Configure an interview:** Select a target job role, experience level, and interview type.
2. **Generate a question:** The application requests a relevant interview question from Gemini.
3. **Submit an answer:** Enter your response in the interview workspace.
4. **Evaluate performance:** Gemini evaluates the response using a structured scoring rubric.
5. **Review feedback:** Explore the overall score, scoring breakdown, strengths, improvement areas, and suggested answer.
6. **Track progress:** Review completed evaluations and score trends in the performance report.

## 📊 Evaluation Criteria

The current evaluation rubric assigns up to 10 points across four categories.

| Criterion | Maximum Score |
|---|---:|
| Technical Correctness | 4 |
| Relevance | 2 |
| Clarity | 2 |
| Completeness | 2 |
| **Total** | **10** |

The feedback is AI-generated and intended to support interview preparation. Scores should be treated as guidance rather than a definitive measure of interview readiness.

## 🔐 API Configuration and Limitations

- An active Gemini API key is required for AI-powered question generation and evaluation.
- API availability, quotas, rate limits, and model access depend on the Google AI project configuration.
- AI responses may vary and can contain inaccuracies.
- Performance history is maintained in the current application session and is not permanently stored in a database.
- The project is an educational prototype and is not intended to guarantee interview outcomes.

## 🚀 Future Enhancements

- Multi-question interview sessions with session-level scoring.
- Adaptive follow-up questions based on candidate responses.
- Persistent user accounts and interview history.
- Downloadable interview performance reports.
- Skill-wise progress tracking and analytics.
- Resume-based interview question generation.
- Additional AI evaluation validation and testing.
- Interview session management and progress tracking.

## 🎓 Project Information

**Project:** InterviewIQ — AI-Powered Mock Interview & Feedback Assistant

**Domain:** Artificial Intelligence / Natural Language Processing

**Framework:** Streamlit

**AI Integration:** Google Gemini API

**Developer:** Santusht Lakhanpal

**GitHub Repository:** [codebysantusht/InterviewIQ](https://github.com/codebysantusht/InterviewIQ)

---

*InterviewIQ aims to make interview preparation more structured, accessible, and feedback-driven through AI-assisted practice.*
