#from dotenv import load_dotenv
import streamlit as st #streamlit을 실행시키는 법은 cmd 창에서 streamlit run main.py를 입력하면 됨.
#load_dotenv()   # Load environment variables from .env file
import time


# def main():
st.title("LangChain Poet")
st.write("Welcome to the LangChain Poet application!")
title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

if st.button("Say hello"):
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)
        st.write("Why hello there")


# if __name__ == "__main__":
#     main()