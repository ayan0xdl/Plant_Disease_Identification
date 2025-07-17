import streamlit as st
import requests

st.set_page_config(page_title="🌿 Plant Disease Detector", layout="centered")

# --- Initialize session state ---
if "menu" not in st.session_state:
    st.session_state.menu = "Disease Detection"  # Default view

# --- Sidebar Navigation ---
menu_options = ["About", "Disease Detection", "BotaniQ"]
selected = st.sidebar.selectbox(
    "Select View",
    menu_options,
    index=menu_options.index(st.session_state.menu)
)
st.session_state.menu = selected

# --- ABOUT PAGE ---
if st.session_state.menu == "About":
    st.image("https://images.wallpaperscraft.com/image/single/leaves_plant_green_118405_1280x720.jpg")
    st.markdown("""
    ## Welcome to BotaniQ - Your Smart Plant Doctor 

    Ever worried about unusual spots or patches on your plant leaves?  
    **BotaniQ** is here to help! This intelligent assistant detects plant diseases from leaf images and provides clear, actionable treatment suggestions — instantly.

    ---

    ### 🔧 How It Works:
    - 📷 **Upload a Leaf Image** – Just a simple click!
    - 🧠 **AI-Powered Diagnosis** – Our model classifies the disease using deep learning.
    - 💬 **BotaniQ Recommends** – Get curated treatment advice via conversational chat.

    ---

    ### 🛠️ Tech Stack:
    - **TensorFlow 2.x** – For robust image classification  
    - **FastAPI + Gemini** – Backend brain for intelligent conversation  
    - **Streamlit** – Clean, interactive, and beautiful user interface  

    ---

    ### 👤 Author:
    Built with 💚 by **Ayan**  
    GitHub: [ayan0xdl](https://github.com/ayan0xdl)
    """)


# --- DISEASE DETECTION PAGE ---
elif st.session_state.menu == "Disease Detection":
    st.title("🌿 Plant Disease Recognition")

    uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image")

        with st.spinner("Predicting..."):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://localhost:8000/predict", files=files)
            result = response.json()

            disease = result["disease"]

            st.session_state["last_disease"] = disease  # Save for use in BotaniQ

        st.success(f"🩺 Predicted: **{disease}**")

        if st.button("💬 Ask BotaniQ"):
            st.session_state.menu = "BotaniQ"
            st.rerun()

# --- BOTANIQ PAGE ---
elif st.session_state.menu == "BotaniQ":
    st.markdown("### Chat with BotaniQ")
    st.info("BotaniQ can help you understand the disease, suggest treatment, and guide future prevention.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    default_prompt = f"What should I know about {st.session_state.last_disease}?" if "last_disease" in st.session_state else ""

    user_input = st.text_input("You:", value=default_prompt, key="input")

    if st.button("Send"):
        if user_input.strip() != "":
            st.session_state.chat_history.append(("user", user_input))

            with st.spinner("BotaniQ is thinking..."):
                response = requests.post("http://localhost:8000/gemini_disease_info", json={"query": user_input,},timeout=10)
                bot_reply = response.json().get("reply", "❌ Couldn’t fetch BotaniQ's response.")

            st.session_state.chat_history.append(("bot", bot_reply))

    # Scrollable and styled chat history
    with st.container():
        st.markdown(
            """
            <style>
            .chat-box {
                max-height: 400px;
                overflow-y: auto;
                padding-right: 10px;
            }
            </style>
            <div class='chat-box'>
            """,
            unsafe_allow_html=True
        )

        for role, msg in st.session_state.chat_history:
            if role == "user":
                st.markdown(
                    f"""

                        <strong>You:</strong><br>{msg}
                    
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                        <strong>BotaniQ:</strong><br>{msg}

                    """,
                    unsafe_allow_html=True
                )

        #auto scrolling
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div id='dummy_scroll'></div>", unsafe_allow_html=True)
        st.markdown("<script>document.getElementById('dummy_scroll').scrollIntoView();</script>", unsafe_allow_html=True)
