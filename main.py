import streamlit as st
import os
from dotenv import load_dotenv
import openai

def set_openai_api_key(api_key):
    """Set the OpenAI API key as an environment variable."""
    os.environ["OPENAI_API_KEY"] = api_key

def check_api_key():
    """Check if the OpenAI API key is valid."""
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.Model.list()
        return True
    except:
        return False

def main():
    st.title("OpenAI API Test Application")

    # Sidebar for API key input
    st.sidebar.title("Configuration")
    api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

    if api_key:
        set_openai_api_key(api_key)
        if check_api_key():
            st.success("API key is valid. You can now use the application.")
            
            # Main application functionality
            st.write("test")
            
        else:
            st.error("Invalid API key. Please check your API key and try again.")
    else:
        st.info("Please enter your OpenAI API key in the sidebar to use the application.")

if __name__ == "__main__":
    main()