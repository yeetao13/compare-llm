# LLM Model Comparison App

This repository contains a Streamlit application for comparing the outputs of different Language Models (LLMs) side by side. The app allows users to select two models, enter a custom prompt, and view the generated responses for easy comparison.

## Features

- **Model Selection**: Choose from a variety of pre-configured LLMs.
- **Prompt Input**: Enter a prompt to see how different models respond.
- **Side-by-Side Comparison**: View the outputs from two models simultaneously.

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yeetao13/compare-llm.git
cd llm-comparison-app
```
### 2. Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the required packages by running:

```bash
pip install -r requirements.txt
```

### 4. Create a .env File

You will need to create a .env file in the root directory of the project to store your Hugging Face API token and model names. The .env file should look like this:

```bash
HUGGINGFACE_TOKEN=your_huggingface_token
MODEL1_NAME=mistralai/Mistral-7B-Instruct-v0.3
MODEL2_NAME=mistralai/Mixtral-8x7B-Instruct-v0.1
```

### 5. Run the Application

After setting up your environment and .env file, you can run the Streamlit app using the following command:

```bash
streamlit run app.py
```

![image](https://github.com/user-attachments/assets/bbd0751d-3b12-4108-80d1-937942c8e1d2)

