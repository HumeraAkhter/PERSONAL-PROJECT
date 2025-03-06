import streamlit as st


st.set_page_config(page_title= "MY EXPERIENCE  OF GIAIC 🌃")
st.title("JOURNEY OF GIAIC BY HUMERA YAHYA🌟 ")

st.header("How did i know about giaic program 🌠")
st.write("watched videos in youtube about giaic💻")

st.header("Giaic first test experince✍️")
st.write("It was a mix of excitement and anxiety, facing a new challenge in a competitive environment. ✌️")

st.header("completion of two quarter")
st.write(" Pass two exame succesfully ,Halfway there — keep going strong!🌟")

st.header(" Third Quarter of PYTHON started 💲")
st.write("A new Python class is a blueprint for creating objects, defining their properties and behaviors through attributes and methods ✨.")

st.header("WHAT IS YOUR CHALLANGE IN PYTHON CLASS")
user_input=st.text_input("Describe a challenge  you are facing 🔯")
if user_input:
    st.success(f"✌️ You 're facing:{user_input} keep pushing fowerd to your goal! 🌟")
else:
    st.warning("Tell us about your challenge to get challenge!")

st.header("🤴 WHAT IS YOUR GOAL!") 
achivement=st.text_input("Share something you want to achieve") 

if achivement:
    st.success(f"👼 Amazing you achived: {achivement}")
else:
    st.info("Every achivement count! Share one now 👩‍✈️") 

st.write("---") 
st.write("Strength and growth come only through continuous effort and struggle, Without struggle, there’s no progress — just stillness.🏃 ") 
st.write("** CREATED BY HUMERA YAHYA**")  

