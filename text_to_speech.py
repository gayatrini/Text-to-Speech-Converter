import streamlit as st
from gtts import gTTS
from IPython.display import Audio

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg with a blur effect.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.wallpaperscraft.com/image/single/glare_circles_spots_47521_1280x720.jpg");
             background-size: cover;

         }}

         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()

def custom_button_css(button_color, text_color, hover_bg_color, hover_text_color, input_border_color):
    return f"""
        <style>
        
        .stApp {{
            background-color: #f0f2f6;
        }}
        .stButton>button {{
            color: {text_color};
            background-color: {button_color};
            border: none;
            border-radius: 4px;
            padding: 10px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition-duration: 0.4s;
        }}
        .stButton>button:hover {{
            background-color: {hover_bg_color};
            color: {hover_text_color};
            border: 2px solid {button_color};
        }}
        .stTextArea textarea {{
            border: 2px solid {input_border_color};
            border-radius: 4px;
            padding: 8px 12px;
            width: 100%;
            box-sizing: border-box;
        }}
        .stSelectbox div[data-baseweb="select"] > div {{
            border: 2px solid {input_border_color};
            border-radius: 4px;
            padding: 8px 12px;
            width: 100%;
            box-sizing: border-box;
        }}
        </style>
    """

# Set colors
button_color = "#4CAF50"  # Green
text_color = "white"
hover_bg_color = "white"
hover_text_color = "black"
input_border_color = "#ccc"  # Light gray


# Apply custom CSS
st.markdown(custom_button_css(button_color, text_color, hover_bg_color, hover_text_color, input_border_color), unsafe_allow_html=True)

# Streamlit app
st.title("Text to Speech")
st.write("Enter the text you want to convert to speech:")

# Input text from user
user_text = st.text_area("Enter text here")

# Generate Speech button
if st.button("Generate Speech"):
    # Generate the audio file using gTTS
    text_to_speech = gTTS(user_text, lang='hi')
    audio_file = 'text_to_speech_gtts.wav'
    text_to_speech.save(audio_file)
    
    # Load and play the audio file
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/wav')
    st.success("Audio generated successfully!")
