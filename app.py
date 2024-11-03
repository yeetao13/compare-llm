import streamlit as st
from streamlit_option_menu import option_menu
from models import mixtral8x7b, Mistral7b, BiggieSmoLlm, Phi3mini4k

# Define your model options
models = {
    "Mixtral-8x7B-Instruct-v0.1": mixtral8x7b,
    "Mistral-7B-Instruct-v0.3": Mistral7b,
    "Biggie-SmoLlm-0.15B-Base": BiggieSmoLlm,
    "Phi-3-mini-4k-instruct": Phi3mini4k
}

# Sidebar for navigation with option_menu
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Introduction", "Model Selection"],
        icons=["house", "gear"],
        menu_icon="cast",
        default_index=0,
    )

# Enhanced Introduction Page
if selected == "Introduction":
    st.title("Welcome to the LLM Model Comparison App")
    st.write("""
        ### Overview
        The LLM Comparison App is designed to help you compare the outputs of various language models (LLMs). 
        These models can generate human-like text based on the prompts you provide. This tool is particularly useful 
        for researchers, developers, and anyone interested in understanding how different language models perform 
        on the same input.

        ### Features
        - **Model Selection**: Choose from a variety of pre-loaded language models.
        - **Prompt Input**: Enter your own custom prompt to see how different models respond.
        - **Side-by-Side Comparison**: View the outputs of two models side by side for easy comparison.
        
        ### How to Use
        1. **Navigate**: Use the sidebar to go to the "Model Selection" page.
        2. **Select Models**: Choose two models from the dropdown menus.
        3. **Enter Prompt**: Type your prompt in the provided text area.
        4. **Generate**: Click the "Generate" button to see the responses from the selected models.

        ### About Language Models
        Language models are powerful tools trained on vast amounts of text data. They can generate coherent and contextually 
        relevant text based on the input they receive. This app uses several state-of-the-art models, including Mixtral 8x7B, 
        Mistral 7B, and Biggie SmoLlm. Each model has its own unique characteristics and strengths.

        ### Privacy and Security
        - Your inputs are not stored or shared. 
        - The generated outputs are not saved after your session ends.
        
        We hope you find this app useful for your projects and research. Enjoy exploring the fascinating world of language models!
        
        #### Note
        This application is still in development, and we welcome your feedback to improve its functionality and user experience. 
        If you encounter any issues or have suggestions, please let us know.
    """)

# Model Selection Page
elif selected == "Model Selection":
    st.title("Model Selection")

    st.sidebar.header("Select Models")
    model1 = st.sidebar.selectbox("Choose first model", list(models.keys()), key="model1")
    model2 = st.sidebar.selectbox("Choose second model", list(models.keys()), key="model2")

    prompt = st.text_area("Enter your prompt here")

    if st.button("Generate"):
        if model1 and model2 and prompt:
            # Generate response from the first model
            with st.spinner(f"Generating response from {model1}..."):
                response1 = models[model1](prompt)
            st.success(f"{model1} response generated!")

            # Generate response from the second model
            with st.spinner(f"Generating response from {model2}..."):
                response2 = models[model2](prompt)
            st.success(f"{model2} response generated!")

            # Display the responses side by side
            col1, col2 = st.columns(2)

            with col1:
                st.subheader(f"Response from {model1}")
                st.write(response1)

            with col2:
                st.subheader(f"Response from {model2}")
                st.write(response2)
        else:
            st.warning("Please select both models and enter a prompt.")
