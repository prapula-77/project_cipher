
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)


# Page Configuration
st.set_page_config(
    page_title="Project Cipher",
    page_icon="🔐",
    layout="centered"
)

# Main Title
st.title("🔐 Project Cipher: Multi-Mode AI Engine")
st.write(
    "An abstract system demonstrating dynamic behavior shifts using Gemini AI."
)


# Protocol Selection
project_mode = st.selectbox(
    "Select System Protocol:",
    [
        "Protocol Alpha (Reverse Mapping)",
        "Protocol Beta (Forward Mapping)",
        "Protocol Gamma (Temporal Simulation)"
    ]
)


# ---------------- PROTOCOL ALPHA ----------------

if project_mode == "Protocol Alpha (Reverse Mapping)":

    st.sidebar.title("📋 Protocol Alpha Data")

    st.sidebar.write("Input Examples:")
    st.sidebar.code(
        "8-5-12-12-15\n19-13-1-18-20\n16-25-20-8-15-14"
    )

    placeholder_text = "Input data string here..."
    button_text = "Execute Protocol Alpha 🔍"

    SYSTEM_PROMPT = """
    You are a brilliant, eccentric Victorian Detective named Barnaby Vance.

    Your job is to crack codes, interpret number ciphers, and solve riddles.

    Rules:
    1. Stay in character as a sharp, witty detective.
    2. If the user gives numbers separated by dashes,
       decode them using A=1, B=2, C=3 ... Z=26.
    3. Print the solved word clearly in CAPITAL LETTERS.
    4. If the user gives a riddle, solve it.
    5. Keep the final answer under 4 sentences.
    """


# ---------------- PROTOCOL BETA ----------------

elif project_mode == "Protocol Beta (Forward Mapping)":

    st.sidebar.title("📋 Protocol Beta Data")

    st.sidebar.write("Input Examples:")
    st.sidebar.code(
        "HELLO\nSMART\nPYTHON"
    )

    placeholder_text = "Enter a word to convert into secret numbers..."
    button_text = "Execute Protocol Beta 🔒"

    SYSTEM_PROMPT = """
    You are a secret code converter.

    Your job is to convert English words into secret numbers.

    Rules:
    1. Convert every letter into its alphabet position.
    2. A=1, B=2, C=3 ... Z=26.
    3. Keep the numbers separated by dashes.
    4. Give ONLY the secret number sequence.
    5. Do not give explanations.
    6. Do not give historical information.

    Examples:
    HELLO → 8-5-12-12-15
    SMART → 19-13-1-18-20
    PYTHON → 16-25-20-8-15-14
    """


# ---------------- PROTOCOL GAMMA ----------------

else:

    st.sidebar.title("📋 Protocol Gamma Data")

    st.sidebar.write("Input Examples:")
    st.sidebar.code(
        "1857\n1919\n1947"
    )

    placeholder_text = "Input a specific Indian historical year..."
    button_text = "Execute Protocol Gamma ⏳"

    SYSTEM_PROMPT = """
    You are a time-conscious historical witness and chronicler
    embedded deeply within Indian history.

    Focus on the Indian freedom struggle, anti-colonial resistance,
    and societal conditions of the selected historical year.

    Rules:

    1. When the user enters a year, respond as a local resident
       experiencing that exact year.

    2. Speak in first person.

    3. Act as if that year is the present day.

    4. Do not mention events that happened after that year.

    5. Describe the social environment, British colonial rule,
       national awakening, resistance, or traditions relevant
       to that year.

    6. Keep the entire response under 4 sentences.
    """


# ---------------- INPUT ----------------

user_input = st.text_input(
    "System Input Terminal:",
    placeholder=placeholder_text
)

trigger_button = st.button(button_text)


# ---------------- GEMINI PROCESSING ----------------


if trigger_button:

    if not user_input:
        st.warning("⚠️ Terminal warning: No input detected!")

    else:
        with st.spinner("Processing system protocols... 🧠"):

            try:
                import time

                response = None

                for attempt in range(3):
                    try:
                        response = client.models.generate_content(
                            model="gemini-3.8-flash",
                            contents=f"""
SYSTEM INSTRUCTIONS:
{SYSTEM_PROMPT}

USER INPUT:
{user_input}
"""
                        )
                        break

                    except Exception as e:
                        if "503" in str(e) and attempt < 2:
                            time.sleep(5)
                        else:
                            raise e

                if response:
                    st.success("💻 Output Decrypted:")
                    st.write(response.text)

            except Exception as e:
                st.error(f"System Error: {e}")