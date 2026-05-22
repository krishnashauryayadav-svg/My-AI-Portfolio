import streamlit as st

# ⚙️ 1. PAGE CONFIGURATION & THEME INJECTION
st.set_page_config(page_title="Krishna Shaurya Yadav | AI & ML Engineer", page_icon="🤖", layout="wide")

# 🪐 Custom Dark/Neon CSS for Mind-Blowing Visual Experience
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    h1 { color: #00FFCC !important; font-family: 'Courier New', monospace; font-weight: bold; }
    h2 { color: #FF007F !important; font-family: 'Segoe UI', sans-serif; }
    .stButton>button {
        background-color: #00FFCC; color: #0E1117; font-weight: bold;
        border-radius: 8px; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #FF007F; color: #FFFFFF; transform: scale(1.05); }
    .card {
        background: #1E2633; padding: 20px; border-radius: 12px;
        border-left: 5px solid #00FFCC; margin-bottom: 20px; color green;
    }
    .card-hacker { border-left: 5px solid #FF007F; }
    .card-lux { border-left: 5px solid #FFFF00; }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 🛸 HEADER SECTION
# =====================================================================
st.title("🛸 KRISHNA SHAURYA YADAV // AI & ML PRODIGY")
st.subheader("Aspiring Data Scientist & ML Engineer | India 🇮🇳")
st.markdown("#### *\"Data → Insight → Impact 🚀\"*")

st.write("---")

# =====================================================================
# 📊 SIDEBAR INFO & SOCIAL GATEWAYS
# =====================================================================
with st.sidebar:
    st.image("https://icons8.com", width=100)
    st.markdown("### 🌐 Connect Matrix")
    # 🔗 अपनी लिंक्डइन और गिटहब आईडी यहाँ पक्की कर लें भाई
    st.markdown("[🐙 GitHub Profile](https://github.com/krishnashauryayadav-svg)")
    st.markdown("[💼 LinkedIn Portfolio](https://www.linkedin.com/in/krishna-shaurya-yadav-864047411/)")
    st.write("---")
    st.markdown("### 🎯 Core Mission")
    st.info("🤖 Dream: To build an advanced Humanoid Robot and develop Self-Healing Multi-Agent Systems.")

# =====================================================================
# 🛠️ SECTION 1: TECH STACK MATRIX
# =====================================================================
st.header("🛠️ Tech Stack & Domain Expertise")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🐍 Core Programming")
    st.success("Python, SQL, Verilog (HDL)")

with col2:
    st.markdown("### 🧠 Machine Learning")
    st.success("TensorFlow, LLMs, Unsloth, Quantization (GGUF)")

with col3:
    st.markdown("### 📊 Data Intelligence")
    st.success("Power BI, Plotly, Data Wrangling & Visualization")

st.write("---")

# =====================================================================
# 📦 SECTION 2: SHOWCASING THE MONSTER PROJECTS
# =====================================================================
st.header("📦 Featured Autonomous AI Projects")

# Project 1: FRIDAY AI
st.markdown("""
<div class="card">
    <h2>💻 Project 1: FRIDAY AI - Multi-Agent Edge Suite</h2>
    <p><b>The Breakthrough:</b> Quantized a base Qwen-2.5 model into 4-bit GGUF (980 MB) using Unsloth to run entirely offline on a 2017 legacy laptop with 4GB RAM without choking hardware boundaries.</p>
    <p>🛡️ Packs a secure remote OS Automation Controller via Telegram Chat-ID verification, a static application vulnerability scanner (SAST), and an ATS Resume Keyword Optimizer.</p>
</div>
""", unsafe_allow_html=True)
st.link_button("View Code on GitHub", "https://github.com/Friday-AI-Suite")

# Project 2: LUX AI (Upcoming Spec)
st.markdown("""
<div class="card card-lux">
    <h2>⚡ Project 2: LUX AI - Self-Healing Hardware Agent (In Development)</h2>
    <p><b>The Vision:</b> An autonomous, local code execution and runtime agent equipped with an integrated Python debugging sandbox.</p>
    <p>🎙️ Features continuous offline voice synthesis modules (pyttsx3) and system hardware loop monitoring to dynamically scale thread variables under heavy memory loads.</p>
</div>
""", unsafe_allow_html=True)

# Project 3: Hacker AI & Smart News Aggregator
st.markdown("""
<div class="card card-hacker">
    <h2>🛡️ Project 3: AI-Powered Smart News Aggregator & Auditor (In Development)</h2>
    <p><b>The Vision:</b> Automating telemetry scraping setups across major technical indices using BeautifulSoup and filtering data structures locally via language model pipelines.</p>
    <p>📢 Features localized breaking news notifications for hardware updates like NVIDIA RTX 5090 launches and active cyber security leaks.</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# =====================================================================
# 📜 SECTION 3: THE RESOURCEFUL ENGINEER CHRONICLES
# =====================================================================
st.header("📜 The Resourceful Engineer Chronicles")
st.markdown("""
> *"I don't wait for enterprise workstations or University degrees to create technology. When faced with constrained 4GB hardware, I mastered 4-bit Quantization. When local compilers threw errors, I engineered proxy pipelines. I look at errors not as obstacles, but as features waiting to be debugged."*
""")

st.write("---")
st.caption("Designed and Maintained by Krishna Shaurya Yadav. Built with Streamlit 🚀")
