# 🎧 AI Audio Tour Agent

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Gemini%202.5%20Flash-00BCD4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Pydantic-E91E63?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
</p>

---

## 🌟 Introduction

**AI Audio Tour Agent** is a next-generation, personalized audio travel guide application. It dynamically researches any global destination based on explicit user-selected interests (such as History, Architecture, Culinary, or Culture) and a specified duration to craft a highly engaging, localized audio script in the user's preferred language (e.g., English, Hindi).

### The Architecture Evolution
The initial iteration of this system utilized a multi-stage sequential agent system that independently triggered specific research workers. While modular, this design led to severe API rate-limiting issues on free-tier quotas. 

This current version features a highly optimized **Single-Shot Orchestration Layer**. By merging multi-agent intelligence into a single consolidated, deeply contextualized prompt, the application entirely mitigates rate limits, slashes response latency by more than half, and retains rigorous structural validation.

---

## 🔥 Features

- **🎯 Granular Personalization:** Dynamically builds a travel script covering only the specific categories selected by the user.
- **🌐 Seamless Localization:** Generates native text outputs perfectly aligned with the user's chosen target language.
- **🎙️ Audio-Ready Content:** Scripts are synthesized as fluid, natural conversational paragraphs completely free of markdown clutter, structural headers, or bullet points—making them immediately ready for Text-to-Speech (TTS) engines.
- **⚡ Quota-Friendly Architecture:** Groups planning, deep topic research, and structural editing capabilities into a single API call to guarantee high uptime and stability.

---

## 🏗️ Technical Architecture & Design Philosophy

The backend execution workflow bypasses complex, sequential network overhead:

Instead of managing an asynchronous pool of fragmented workers, `manager.py` utilizes an expressive master prompt detailing technical instructions, topic boundaries, and strict language rules. To ensure data formatting consistency between the LLM output and the UI, the application enforces **Pydantic Structural Validation** (`FinalTour`), preventing structural runtime failures.

---

## ⚙️ Setup & Local Installation

Follow these steps to configure and execute the project locally on your machine:

1. Clone the GitHub repository

```bash
git clone https://github.com/meenuparashar18/Ai_audio_tour_agent.git
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt

3. Get your Gemini API Key
4. Configure Environment Variables
Create a secure .env file in the root directory of the project to map your API authorization credentials:
GEMINI_API_KEY="your_actual_gemini_api_key_here"

5. Run the Streamlit App
```bash
streamlit run ai_audio_tour_agent.py
```
📂 Project Structure
├── ai_audio_tour_agent.py  # Streamlit UI Layer (Frontend)
├── manager.py               # Orchestration Layer & Single-Shot API Call (Backend)
├── agent.py                 # Pydantic Schemas & Prompt Configurations
├── .env                     # API Credentials (Local Only)
├── .gitignore               # Automated Git Exclusions
└── README.md                # Comprehensive Documentation
