
# 🎧 WanderVoice AI

 > Transform any destination into a personalized audio-guided travel experience using AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-green)

---

## 🌍 Overview

WanderVoice AI is an intelligent travel companion that generates immersive, personalized audio tours for destinations around the world.

Simply enter a destination, choose your interests, and the application researches the location, creates a structured travel narrative, and converts it into a natural audio-guided experience.

Whether you're interested in history, culture, architecture, food, or local attractions, the agent delivers a tailored tour in seconds.

---

## ✨ Features

### 🎯 Personalized Tour Generation
Generate destination-specific tours based on user-selected interests.

### 🗺️ Intelligent Destination Research
Automatically gathers relevant information about landmarks, culture, history, and local highlights.

### 🎙️ Audio Narration
Converts generated travel content into an engaging voice-guided experience.

### 🌐 Multi-Language Support
Generate tours in different languages for global accessibility.

### ⚡ Fast AI Processing
Optimized prompt orchestration reduces response time while maintaining content quality.

### ✅ Structured Output Validation
Uses Pydantic schemas to ensure reliable and consistent AI responses.

---

## 🚀 How It Works

1. Enter a destination.
2. Select tour duration.
3. Choose interests (History, Culture, Architecture, Food, etc.).
4. AI researches the destination.
5. A personalized travel script is generated.
6. The script is converted into audio narration.
7. Enjoy your virtual guided tour.

---

## 🏗️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Pydantic
- Text-to-Speech (TTS)

---

## 📂 Project Structure

```text
WanderVoice-AI/
│
├── ai_audio_tour_agent.py          # Streamlit Frontend
├── manager.py                      # AI Orchestration Layer
├── agent.py                        # Prompt Engineering & Schemas
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/meenuparashar18/WanderVoice-AI.git
cd AI_Audio_Tour_Agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run ai_audio_tour_agent.py
```

---

## 📸 Demo

Add screenshots or GIFs here.

```md
![Demo](assets/demo.png)
```

---

## 🎯 Example Use Case

**Destination:** Paris

**Interests:** History, Architecture, Culture

**Output:**

- AI-generated travel narrative
- Audio-guided tour
- Key landmarks and historical insights
- Personalized storytelling experience

---

## 🔮 Future Enhancements

- Real-time travel recommendations
- Interactive voice conversations
- Route planning integration
- Maps support
- Travel itinerary generation
- Downloadable audio guides

---
