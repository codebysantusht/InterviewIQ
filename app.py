import html
import streamlit as st

from ai_engine import generate_question, evaluate_answer


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="InterviewIQ | AI Interview Studio",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# TARGET ROLES
# =========================================================

TARGET_ROLES = [
    # Software development
    "Software Engineer",
    "Software Developer",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Python Developer",
    "Java Developer",
    "C++ Developer",
    "JavaScript Developer",
    "Mobile App Developer",
    "Android Developer",
    "iOS Developer",
    "Game Developer",
    "Embedded Software Engineer",
    "QA Engineer",
    "Software Development Engineer in Test (SDET)",
    "Automation Test Engineer",

    # Cybersecurity
    "Cybersecurity Analyst",
    "SOC Analyst",
    "Security Engineer",
    "Penetration Tester",
    "Ethical Hacker",
    "Application Security Engineer",
    "Cloud Security Engineer",
    "Network Security Engineer",
    "Incident Response Analyst",
    "Digital Forensics Analyst",
    "Threat Intelligence Analyst",
    "Vulnerability Management Analyst",
    "Security Operations Engineer",
    "GRC Analyst",
    "IAM Engineer",
    "Malware Analyst",
    "Security Architect",
    "Red Team Operator",
    "Blue Team Analyst",
    "Detection Engineer",
    "DevSecOps Engineer",

    # Cloud, DevOps and infrastructure
    "DevOps Engineer",
    "Site Reliability Engineer (SRE)",
    "Cloud Engineer",
    "Cloud Architect",
    "Platform Engineer",
    "Systems Administrator",
    "Network Engineer",
    "Linux System Administrator",
    "Infrastructure Engineer",
    "IT Support Engineer",
    "Release Engineer",
    "Build Engineer",

    # Data and AI
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "Machine Learning Engineer",
    "AI Engineer",
    "Generative AI Engineer",
    "NLP Engineer",
    "Computer Vision Engineer",
    "Business Intelligence Analyst",
    "MLOps Engineer",
    "Research Engineer",
    "Analytics Engineer",

    # Database and enterprise technology
    "Database Administrator",
    "Database Engineer",
    "Solutions Architect",
    "Enterprise Application Developer",
    "Salesforce Developer",
    "ERP Consultant",
    "Technical Consultant",
    "SAP Consultant",

    # Product, business and IT
    "Product Manager",
    "Technical Product Manager",
    "Business Analyst",
    "Systems Analyst",
    "Technical Business Analyst",
    "IT Project Coordinator",
    "Technical Support Engineer",
    "Technical Account Manager",
    "Customer Success Engineer",
    "Pre-Sales Engineer",

    # Electronics and emerging technology
    "IoT Engineer",
    "Robotics Software Engineer",
    "Firmware Engineer",
    "Blockchain Developer",
    "Hardware Engineer",
    "VLSI Design Engineer",

    # Graduate and entry-level roles
    "Graduate Engineer Trainee",
    "Associate Software Engineer",
    "IT Graduate Trainee",
    "Associate Technical Consultant",
]


# =========================================================
# DESIGN SYSTEM
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #0A0D16;
    --panel: #111625;
    --border: #252D42;
    --text: #F1F5F9;
    --muted: #94A3B8;
    --purple: #8B7CFF;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 70% 0%, rgba(105, 85, 255, 0.09), transparent 35%),
        var(--bg);
    color: var(--text);
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1500px;
    padding: 2rem 2.5rem 3rem;
}

section[data-testid="stSidebar"] {
    background: #0D1120;
    border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: -0.6px;
}

h1 {
    font-size: 2.25rem !important;
    font-weight: 700 !important;
}

h2 {
    font-size: 1.55rem !important;
}

p, label, li {
    line-height: 1.7;
}

div[data-testid="stButton"] > button {
    min-height: 44px;
    border-radius: 10px;
    border: 1px solid #35345C;
    background: linear-gradient(135deg, #8271F8, #6656D9);
    color: white;
    font-weight: 600;
    transition: all 0.2s ease;
}

div[data-testid="stButton"] > button:hover {
    border-color: #B4AAFF;
    background: linear-gradient(135deg, #9485FF, #7667ED);
    box-shadow: 0 5px 22px rgba(124, 105, 255, 0.20);
    color: white;
}

div[data-testid="stButton"] > button[kind="secondary"] {
    background: #151B2C;
    border: 1px solid var(--border);
    color: #E2E8F0;
}

div[data-testid="stTextArea"] textarea {
    background: #0D1220;
    border: 1px solid #303951;
    color: #F1F5F9;
    border-radius: 12px;
    line-height: 1.8;
}

div[data-testid="stTextArea"] textarea:focus {
    border-color: #8B7CFF;
    box-shadow: 0 0 0 1px #8B7CFF;
}

div[data-testid="stSelectbox"] > div > div {
    background: #13192A;
    border-color: #303951;
    border-radius: 9px;
}

div[data-testid="stMetric"] {
    background: #121829;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px 20px;
}

div[data-testid="stMetricLabel"] {
    color: #A5B4C8;
}

div[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif;
    color: #F8FAFC;
}

div[data-testid="stProgressBar"] > div {
    background: #252D42;
    border-radius: 10px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #7465E8, #A99DFF);
    border-radius: 10px;
}

hr {
    border-color: var(--border);
}

#MainMenu, footer {
    visibility: hidden;
}

a {
    color: #B4AAFF !important;
}

.brand-mark {
    width: 43px;
    height: 43px;
    border-radius: 13px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #9485FF, #5947CE);
    color: white;
    font-size: 23px;
    box-shadow: 0 5px 20px rgba(105, 85, 255, .22);
}

.brand-row {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-bottom: 8px;
}

.brand-name {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 22px;
    color: #F8FAFC;
    line-height: 1.2;
}

.brand-subtitle {
    font-size: 10px;
    color: #8E9AB1;
    letter-spacing: 1.6px;
    margin-top: 4px;
}

.eyebrow {
    font-size: 11px;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    font-weight: 700;
    color: #A99DFF;
    margin-bottom: 10px;
}

.hero {
    background:
        radial-gradient(ellipse at 90% 15%, rgba(139,124,255,.22), transparent 40%),
        linear-gradient(125deg, #171D32, #111625 65%);
    border: 1px solid #343654;
    border-radius: 20px;
    padding: 32px;
    overflow: hidden;
}

.hero h1 {
    margin: 0;
    line-height: 1.17;
}

.hero-description {
    color: #A9B5CA;
    font-size: 15px;
    max-width: 620px;
    line-height: 1.8;
    margin-top: 15px;
}

.hero-tag {
    display: inline-block;
    background: rgba(139,124,255,.13);
    border: 1px solid rgba(139,124,255,.3);
    color: #C5BDFF;
    padding: 6px 11px;
    border-radius: 20px;
    font-size: 11px;
    letter-spacing: .6px;
    margin-bottom: 18px;
}

.panel {
    background: linear-gradient(145deg, #141A2A, #101523);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 22px;
    height: 100%;
}

.panel-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 16px;
    font-weight: 600;
    color: #F1F5F9;
    margin-bottom: 6px;
}

.panel-description {
    color: #93A0B5;
    font-size: 13px;
    line-height: 1.7;
}

.mini-label {
    font-size: 11px;
    color: #8E9AB1;
    text-transform: uppercase;
    letter-spacing: 1.1px;
    font-weight: 600;
}

.question-card {
    background: linear-gradient(145deg, #171E31, #111625);
    border: 1px solid #353653;
    border-radius: 18px;
    padding: 26px;
    margin: 12px 0 20px;
}

.question-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 21px;
    line-height: 1.65;
    font-weight: 500;
    color: #F8FAFC;
    margin-top: 18px;
    overflow-wrap: anywhere;
}

.pill {
    display: inline-block;
    border: 1px solid #3B3B63;
    background: #22213D;
    color: #C6BEFF;
    padding: 5px 10px;
    border-radius: 7px;
    font-size: 11px;
    margin-right: 6px;
}

.section-kicker {
    color: #9DAAC0;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.feedback-card {
    background: #131A29;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 19px;
    margin-bottom: 10px;
}

.feedback-card-title {
    font-size: 14px;
    color: #E8ECF5;
    font-weight: 600;
    margin-bottom: 8px;
}

.feedback-body {
    font-size: 13px;
    color: #AAB6CA;
    line-height: 1.8;
    overflow-wrap: anywhere;
}

.score-circle {
    border: 1px solid #514A86;
    background: radial-gradient(circle at center, #292447, #151829);
    border-radius: 18px;
    padding: 24px 12px;
    text-align: center;
}

.score-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 43px;
    font-weight: 700;
    color: #C2B9FF;
    line-height: 1.3;
}

.score-caption {
    color: #9DAAC0;
    font-size: 12px;
}

.empty-state {
    background: #111625;
    border: 1px dashed #343D54;
    border-radius: 16px;
    padding: 30px;
    text-align: center;
    color: #A3AEC2;
}

.sidebar-note {
    background: #151A2B;
    border: 1px solid #2B3348;
    border-radius: 12px;
    padding: 13px;
    color: #9EABC0;
    font-size: 12px;
    line-height: 1.7;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 2rem;
    }
    .hero {
        padding: 22px;
    }
    .question-text {
        font-size: 18px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "question": None,
    "feedback": None,
    "interview_config": None,
    "answer": "",
    "error_message": None,
    "questions_generated": 0,
    "evaluations_completed": 0,
    "history": [],
    "active_page": "Dashboard",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# HELPERS
# =========================================================

def safe_text(value):
    return html.escape(str(value))


def start_new_question(role, level, interview_type):
    st.session_state.question = None
    st.session_state.feedback = None
    st.session_state.answer = ""
    st.session_state.error_message = None

    st.session_state.interview_config = {
        "role": role,
        "level": level,
        "interview_type": interview_type,
    }

    with st.spinner("Preparing your personalized interview question..."):
        try:
            question = generate_question(role, level, interview_type)
            st.session_state.question = question
            st.session_state.questions_generated += 1
            st.session_state.active_page = "Mock Interview"
        except Exception as error:
            st.session_state.error_message = str(error)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("""
    <div class="brand-row">
        <div class="brand-mark">✦</div>
        <div>
            <div class="brand-name">InterviewIQ</div>
            <div class="brand-subtitle">INTERVIEW INTELLIGENCE</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="mini-label">WORKSPACE</div>', unsafe_allow_html=True)

    page_options = ["Dashboard", "Mock Interview", "Performance Report"]
    current_page = st.session_state.active_page
    if current_page not in page_options:
        current_page = "Dashboard"

    selected_page = st.radio(
        "Workspace navigation",
        page_options,
        index=page_options.index(current_page),
        label_visibility="collapsed",
        key="page_navigation",
    )
    st.session_state.active_page = selected_page

    st.markdown("---")
    st.markdown('<div class="mini-label">INTERVIEW CONFIGURATION</div>', unsafe_allow_html=True)

    # Streamlit selectbox supports typing to search its options.
    role = st.selectbox(
    "Target role",
    TARGET_ROLES,
    index=TARGET_ROLES.index("Python Developer"),
    key="setup_role",
    placeholder="Search or select a target role",
)

    level = st.selectbox(
        "Experience level",
        ["Beginner", "Intermediate", "Advanced"],
        key="setup_level",
    )

    interview_type = st.selectbox(
        "Interview format",
        ["Technical", "HR", "Mixed"],
        key="setup_type",
    )

    if st.button("✦  Start New Interview", use_container_width=True):
        start_new_question(role, level, interview_type)
        st.rerun()

    st.markdown("---")
    st.markdown("""
    <div class="sidebar-note">
        <b style="color:#DCE2F1;">AI Interview Studio</b><br>
        Practice role-specific questions, receive structured feedback,
        and identify opportunities to improve.<br><br>
        <span style="color:#A99DFF;">●</span> Powered by Gemini
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<p style="color:#65718A;font-size:10px;text-align:center;'
        'margin-top:20px;">INTERVIEWIQ · STUDENT PROJECT</p>',
        unsafe_allow_html=True,
    )


# =========================================================
# TOP HEADER
# =========================================================

header_left, header_right = st.columns([4, 1])

with header_left:
    st.markdown(
        '<div class="eyebrow">AI-POWERED INTERVIEW PLATFORM</div>',
        unsafe_allow_html=True,
    )

with header_right:
    st.markdown(
        '<div style="text-align:right;color:#94A3B8;'
        'font-size:12px;padding-top:8px;">PERSONAL WORKSPACE</div>',
        unsafe_allow_html=True,
    )

if st.session_state.error_message:
    st.error(st.session_state.error_message)
    if st.button("Dismiss error", key="dismiss_error"):
        st.session_state.error_message = None
        st.rerun()


# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.active_page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <div class="hero-tag">✦ YOUR PERSONAL AI INTERVIEW COACH</div>
        <h1>Practice with purpose.<br>
        <span style="color:#A99DFF;">Perform with confidence.</span></h1>
        <div class="hero-description">
            Turn interview preparation into a measurable learning experience.
            Practice job-specific questions, understand your strengths, and
            discover where you can improve.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown("### Your Overview")
    st.caption("A snapshot of your activity in this session.")

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric("Questions Generated", st.session_state.questions_generated)

    with metric2:
        st.metric("Answers Evaluated", st.session_state.evaluations_completed)

    with metric3:
        if st.session_state.history:
            average = sum(item["score"] for item in st.session_state.history) / len(st.session_state.history)
            average_label = f"{average:.1f}/10"
        else:
            average_label = "—"
        st.metric("Average Score", average_label)

    st.write("")
    st.markdown("### Your Interview Workspace")

    workspace1, workspace2 = st.columns([1.15, 1])

    with workspace1:
        st.markdown("""
        <div class="panel">
            <div class="eyebrow">01 / PRACTICE</div>
            <div class="panel-title" style="font-size:21px;">Mock Interview</div>
            <div class="panel-description">
                Simulate a real interview tailored to your target role,
                experience level, and interview format.
            </div><br>
            <span class="pill">Role-specific</span>
            <span class="pill">Technical / HR / Mixed</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Start Practicing  →", key="dashboard_start", use_container_width=True):
            start_new_question(role, level, interview_type)
            st.rerun()

    with workspace2:
        st.markdown("""
        <div class="panel">
            <div class="eyebrow">02 / IMPROVE</div>
            <div class="panel-title" style="font-size:21px;">Performance Insights</div>
            <div class="panel-description">
                Review evaluation scores, strengths, areas for improvement,
                and AI-generated suggested answers.
            </div><br>
            <span class="pill">Scoring breakdown</span>
            <span class="pill">Actionable feedback</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button("View Performance  →", key="dashboard_report", use_container_width=True):
            st.session_state.active_page = "Performance Report"
            st.rerun()

    st.write("")
    st.markdown("### Recent Activity")

    if st.session_state.history:
        for item in reversed(st.session_state.history[-5:]):
            with st.container(border=True):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.markdown(f"**{item['role']}**")
                    st.caption(item["question"])
                with c2:
                    st.markdown("**Score**")
                    st.write(f"{item['score']:.1f}/10")
                with c3:
                    st.markdown("**Level**")
                    st.write(item["level"])
    else:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size:28px;margin-bottom:8px;">◷</div>
            <b style="color:#E2E8F0;">Your activity will appear here</b>
            <p style="font-size:13px;">
                Start your first mock interview to build your performance history.
            </p>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# MOCK INTERVIEW
# =========================================================

elif st.session_state.active_page == "Mock Interview":

    st.title("Mock Interview")
    st.caption(
        "Your dedicated interview workspace. Think through your answer "
        "and respond as you would in a real interview."
    )

    if not st.session_state.interview_config:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size:36px;margin-bottom:12px;">✦</div>
            <h3 style="color:#F1F5F9;">Ready to begin?</h3>
            <p>
                Choose your target role, experience level, and interview
                format in the sidebar, then start a new interview.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Start My Interview", key="empty_start"):
            start_new_question(role, level, interview_type)
            st.rerun()

    else:
        config = st.session_state.interview_config

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**TARGET ROLE**")
            st.write(config["role"])

        with col2:
            st.markdown("**EXPERIENCE LEVEL**")
            st.write(config["level"])

        with col3:
            st.markdown("**INTERVIEW FORMAT**")
            st.write(config["interview_type"])

        st.divider()

        if st.session_state.question:
            st.markdown('<div class="section-kicker">YOUR INTERVIEW QUESTION</div>', unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="question-card">
                    <span class="pill">AI GENERATED</span>
                    <span class="pill">{safe_text(config['interview_type'])}</span>
                    <div class="question-text">{safe_text(st.session_state.question)}</div>
                    <div class="panel-description" style="margin-top:16px;">
                        Tip: Structure your response clearly and support your
                        explanation with a practical example where relevant.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("### Your Response")
            st.caption(
                "The AI evaluator assesses correctness, relevance, clarity, "
                "and completeness."
            )

            st.text_area(
                "Answer editor",
                key="answer",
                height=230,
                placeholder=(
                    "Start writing your answer here...\n\n"
                    "Explain your approach, reasoning, and relevant examples."
                ),
                label_visibility="collapsed",
            )

            action1, action2 = st.columns([2, 1])

            with action1:
                submit = st.button(
                    "✦  Evaluate My Answer",
                    type="primary",
                    use_container_width=True,
                    key="evaluate_answer",
                )

            with action2:
                next_question = st.button(
                    "New Question",
                    use_container_width=True,
                    key="next_question",
                )

            if submit:
                answer = st.session_state.answer.strip()

                if not answer:
                    st.warning("Please enter your answer before submitting.")
                else:
                    st.session_state.feedback = None
                    st.session_state.error_message = None

                    with st.spinner("Evaluating your answer against the scoring rubric..."):
                        try:
                            result = evaluate_answer(
                                config["role"],
                                config["level"],
                                st.session_state.question,
                                answer,
                            )

                            st.session_state.feedback = result
                            st.session_state.evaluations_completed += 1
                            st.session_state.history.append({
                                "role": config["role"],
                                "level": config["level"],
                                "question": st.session_state.question,
                                "answer": answer,
                                "score": float(result["score"]),
                                "feedback": result,
                            })

                        except Exception as error:
                            st.session_state.error_message = str(error)

                    st.rerun()

            if next_question:
                start_new_question(
                    config["role"],
                    config["level"],
                    config["interview_type"],
                )
                st.rerun()

        # Evaluation results
        if st.session_state.feedback:
            feedback = st.session_state.feedback
            score = float(feedback["score"])

            st.divider()
            st.markdown('<div class="eyebrow">AI ASSESSMENT REPORT</div>', unsafe_allow_html=True)
            st.markdown('<h2 style="margin-top:0;">Your Performance Analysis</h2>', unsafe_allow_html=True)

            left, right = st.columns([1, 2.2])

            with left:
                st.markdown(
                    f"""
                    <div class="score-circle">
                        <div class="mini-label">OVERALL SCORE</div>
                        <div class="score-number">{score:g}<span style="font-size:20px;color:#8D91A8;">/10</span></div>
                        <div class="score-caption">AI evaluation</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with right:
                st.markdown("#### Evaluation Summary")
                st.write(feedback["summary"])
                st.progress(min(max(score / 10, 0.0), 1.0))

                if score >= 8:
                    st.success("Strong performance. Keep refining your answers.")
                elif score >= 5:
                    st.info("Good foundation. Review the improvement points to strengthen your response.")
                else:
                    st.warning("Use the feedback below to rebuild your answer step by step.")

            st.write("")
            st.markdown("### Scoring Breakdown")

            score1, score2, score3, score4 = st.columns(4)

            with score1:
                st.metric("Technical Correctness", feedback["technical_correctness"])
            with score2:
                st.metric("Relevance", feedback["relevance"])
            with score3:
                st.metric("Clarity", feedback["clarity"])
            with score4:
                st.metric("Completeness", feedback["completeness"])

            st.divider()
            strengths_col, improvement_col = st.columns(2)

            with strengths_col:
                st.markdown("### Strengths")
                for item in feedback["strengths"]:
                    st.markdown(
                        f"""
                        <div class="feedback-card">
                            <span style="color:#42D6A4;">✓</span>
                            &nbsp; {safe_text(item)}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            with improvement_col:
                st.markdown("### Areas to Improve")
                for item in feedback["areas_for_improvement"]:
                    st.markdown(
                        f"""
                        <div class="feedback-card">
                            <span style="color:#F4B860;">↗</span>
                            &nbsp; {safe_text(item)}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            st.divider()
            st.markdown("### Suggested Answer")
            st.markdown(
                f"""
                <div class="panel">
                    <div class="panel-description" style="font-size:14px;color:#D4DCEC;">
                        {safe_text(feedback['suggested_answer'])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write("")
            st.markdown("### Follow-up Question")
            st.markdown(
                f"""
                <div class="question-card">
                    <div class="eyebrow">GO ONE LEVEL DEEPER</div>
                    <div class="question-text" style="font-size:18px;">
                        {safe_text(feedback['follow_up_question'])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            report_col1, report_col2 = st.columns(2)

            with report_col1:
                if st.button("Practice Another Question", use_container_width=True, key="report_next"):
                    start_new_question(config["role"], config["level"], config["interview_type"])
                    st.rerun()

            with report_col2:
                if st.button("View Full Performance Report", use_container_width=True, key="report_open"):
                    st.session_state.active_page = "Performance Report"
                    st.rerun()


# =========================================================
# PERFORMANCE REPORT
# =========================================================

elif st.session_state.active_page == "Performance Report":

    st.title("Performance Report")
    st.caption(
        "Review completed evaluations and understand your performance "
        "across the current application session."
    )

    history = st.session_state.history

    if not history:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size:36px;margin-bottom:12px;">▤</div>
            <h3 style="color:#F1F5F9;">No evaluation data yet</h3>
            <p>
                Complete a mock interview to see your scores, performance
                trends, and detailed feedback.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Go to Mock Interview"):
            st.session_state.active_page = "Mock Interview"
            st.rerun()

    else:
        scores = [float(item["score"]) for item in history]
        average = sum(scores) / len(scores)
        best = max(scores)

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("Evaluations Completed", len(history))
        with m2:
            st.metric("Average Score", f"{average:.1f}/10")
        with m3:
            st.metric("Best Score", f"{best:.1f}/10")

        st.write("")
        st.markdown("### Score History")

        chart_data = {
            "Evaluation": [f"Attempt {i + 1}" for i in range(len(scores))],
            "Score": scores,
        }

        st.line_chart(chart_data, x="Evaluation", y="Score")
        st.caption(
            "Scores represent evaluations completed in this running "
            "application session. They are not saved permanently."
        )

        st.divider()
        st.markdown("### Evaluation History")

        for item in reversed(history):
            with st.expander(
                f"{item['role']}  ·  {item['score']:.1f}/10  ·  {item['level']}"
            ):
                st.markdown("**Question**")
                st.write(item["question"])

                st.markdown("**Your Answer**")
                st.write(item["answer"])

                st.markdown("**Evaluation Summary**")
                st.write(item["feedback"]["summary"])

                st.markdown("**Suggested Answer**")
                st.write(item["feedback"]["suggested_answer"])

        st.write("")
        if st.button("Start Another Interview"):
            start_new_question(role, level, interview_type)
            st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

footer_left, footer_right = st.columns(2)

with footer_left:
    st.markdown(
        '<p style="color:#6F7B92;font-size:11px;">'
        'INTERVIEWIQ · AI INTERVIEW STUDIO</p>',
        unsafe_allow_html=True,
    )

with footer_right:
    st.markdown(
        '<p style="color:#6F7B92;font-size:11px;text-align:right;">'
        'Built with Streamlit and Gemini</p>',
        unsafe_allow_html=True,
    )
