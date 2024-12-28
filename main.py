import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

#from dotenv import load_dotenv
#load_dotenv()

client = ChatGroq(
    model_name="llama3-8b-8192", 
    api_key=os.environ.get("GROQ_API_KEY")  
)

st.title('BlogMate')
title = st.text_input(
    "블로그 주제를 입력해 주세요! 해당 주제에 대한 참고할 내용을 제공해 드리겠습니다.",
    max_chars=30,
    help='30자 이내로 작성해주세요.'
)

messages = [
    ("system", "여러분은 큐티 블로거입니다. 해당 주제와 관련된 블로그 글을 한글로 작성합니다."),
    ("user", f"이글에 대한 블로그글을 한글로 작성해줘 주제 : {title}")
]

# Prompt 템플릿 생성
prompt = ChatPromptTemplate.from_messages(messages)

if st.button("내용 요청하기"):
    with st.spinner("내용 작성 중..."):
        try:
            
            input_text = f"이글에 대한 블로그글을 한글로 작성해줘 주제 : {title}"
            response = client.invoke(input=input_text)
                    
            st.write(response.content)  
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

