import streamlit as st

# ASCII Logo fallback (or import art if available)
LOGO = r"""
  ____                               ____ _       _               
 / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|   
                                          |_|                    
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(original_text: str, shift_amount: int, encode_or_decode: str) -> str:
    """Encodes or decodes text while preserving non-alphabet characters."""
    cipher_text = ""
    for char in original_text:
        is_upper = char.isupper()
        lower_char = char.lower()

        if lower_char in alphabet:
            idx = alphabet.index(lower_char)
            if encode_or_decode == "encode":
                new_idx = (idx + shift_amount) % len(alphabet)
            else:
                new_idx = (idx - shift_amount) % len(alphabet)

            transformed = alphabet[new_idx]
            cipher_text += transformed.upper() if is_upper else transformed
        else:
            # Keep numbers, spaces, and punctuation unchanged
            cipher_text += char

    return cipher_text


# Page Configuration
st.set_page_config(page_title="Caesar Cipher Chat", page_icon="🔐", layout="centered")

st.markdown(f"```\n{LOGO}\n```")
st.title("🔐 Caesar Cipher Bot")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Cipher Controls")
    mode = st.radio("Select Mode:", ("encode", "decode"), format_func=lambda x: x.capitalize())
    shift = st.slider("Shift Amount:", min_value=1, max_value=25, value=3)

    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat history cleared. Send a message to encode or decode!"}
        ]
        st.rerun()

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Caesar Cipher bot. Enter any message below to transform it."}
    ]

# Display conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Chat Input
user_input = st.chat_input("Type your message here...")

if user_input:
    # 1. Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Process cipher
    result = cipher(original_text=user_input, shift_amount=shift, encode_or_decode=mode)
    response = f"**{mode.capitalize()}d (Shift: {shift}):**\n`{result}`"

    # 3. Display bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)