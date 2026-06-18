import streamlit as st
from dotenv import load_dotenv
import os
import io
from gtts import gTTS


load_dotenv()


st.set_page_config(
    page_title="AI Audio Tour Agent",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="collapsed"
)


with st.sidebar:
    st.title("🔑 Settings")
    api_key = st.text_input(
        "Gemini API Key:", 
        value=os.getenv("GEMINI_API_KEY", ""), 
        type="password",
        help="Get your free key from aistudio.google.com"
    )
    if api_key:
        st.session_state["GEMINI_API_KEY"] = api_key
        os.environ["GEMINI_API_KEY"] = api_key
        st.success("Gemini API key saved!")


st.title("🎧 AI Audio Tour Agent")
st.markdown("""
    <div class='welcome-card'>
        <h3>Welcome to your personalized audio tour guide!</h3>
        <p>I'll help you explore any location with an engaging, natural-sounding tour tailored to your interests.</p>
    </div>
""", unsafe_allow_html=True)


col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📍 Where would you like to explore?")
    location = st.text_input("", placeholder="Enter a city, landmark, or location...")
    
    st.markdown("### 🎯 What interests you?")
    interests = st.multiselect(
        "",
        options=["History", "Architecture", "Culinary", "Culture"],
        default=["History", "Architecture"],
        help="Select the topics you'd like to learn about"
    )

with col2:
    st.markdown("### ⏱️ Tour Settings")
    duration = st.slider(
        "Tour Duration (minutes)",
        min_value=5,
        max_value=60,
        value=10,
        step=5,
        help="Choose how long you'd like your tour to be"
    )
    
   
    st.markdown("### 🌐 Select Language")
    selected_lang = st.selectbox(
        "Choose Tour Language",
        options=["English", "Hindi"],
        help="Select the language for text and audio tour"
    )
    
    st.markdown("### 🎙️ Voice Settings")
    voice_style = st.selectbox(
        "Guide's Voice Style",
        options=["Friendly & Casual", "Professional & Detailed", "Enthusiastic & Energetic"],
        help="Select the personality of your tour guide"
    )


if st.button("🎧 Generate Tour", type="primary"):
    current_key = st.session_state.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    
    if not current_key:
        st.error("Please enter your Gemini API key in the sidebar or setup .env file.")
    elif not location:
        st.error("Please enter a location.")
    elif not interests:
        st.error("Please select at least one interest.")
    else:
        with st.spinner(f"Creating your personalized tour of {location}..."):
            try:
                from manager import TourManager
                mgr = TourManager()
                
               
                final_tour_object = mgr.run(location, interests, duration, selected_lang)
                
      
                final_tour_text = (
                    f"✨ **Introduction** ✨\n{final_tour_object.introduction}\n\n"
                    f"🏛️ **Architecture** 🏛️\n{final_tour_object.architecture}\n\n"
                    f"📜 **History** 📜\n{final_tour_object.history}\n\n"
                    f"🎭 **Culture** 🎭\n{final_tour_object.culture}\n\n"
                    f"🍲 **Culinary** 🍲\n{final_tour_object.culinary}\n\n"
                    f"🏁 **Conclusion** 🏁\n{final_tour_object.conclusion}"
                )

              
                with st.expander("📝 Tour Content", expanded=True):
                    st.markdown(final_tour_text)
                
                
                with st.spinner("🎙️ Generating audio tour... (Please wait a few seconds)"):
                    
                    plain_text_script = f"{final_tour_object.introduction}\n"
                    if "Not requested" not in final_tour_object.architecture:
                        plain_text_script += f"{final_tour_object.architecture}\n"
                    if "Not requested" not in final_tour_object.history:
                        plain_text_script += f"{final_tour_object.history}\n"
                    if "Not requested" not in final_tour_object.culture:
                        plain_text_script += f"{final_tour_object.culture}\n"
                    if "Not requested" not in final_tour_object.culinary:
                        plain_text_script += f"{final_tour_object.culinary}\n"
                    plain_text_script += final_tour_object.conclusion
                    
                    
                    if selected_lang == "Hindi":
                        tts_engine = gTTS(text=plain_text_script, lang='hi')
                    else:
                        tts_engine = gTTS(text=plain_text_script, lang='en', tld='co.in')
                        
                    audio_buffer = io.BytesIO()
                    tts_engine.write_to_fp(audio_buffer)
                    audio_buffer.seek(0)
                
               
                st.markdown("### 🎧 Listen to Your Tour")
                st.audio(audio_buffer, format="audio/mp3")
                
               
                st.download_button(
                    label="📥 Download Audio Tour",
                    data=audio_buffer.getvalue(),
                    file_name=f"{location.lower().replace(' ', '_')}_tour.mp3",
                    mime="audio/mp3"
                )
                
            except Exception as e:
                st.error(f"Something went wrong: {e}")