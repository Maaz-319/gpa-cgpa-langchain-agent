import streamlit as st
from langchain.messages import HumanMessage
from agent import agent

st.set_page_config(page_title="PUCIT GPA Assistant")
st.title("PUCIT GPA Assistant")
st.caption("Ask about GPA, CGPA, courses, or reaching a target CGPA.")

if "display" not in st.session_state:
    st.session_state.display = []
if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.display:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if st.button("New conversation"):
    st.session_state.display = []
    st.session_state.history = []
    st.rerun()

if prompt := st.chat_input("e.g. What GPA do I need this semester?"):
    st.session_state.display.append({"role": "user", "content": prompt})
    st.session_state.history.append(HumanMessage(prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = agent.invoke({"messages": st.session_state.history})
        st.session_state.history = result["messages"]
        answer = result["messages"][-1].text
        st.markdown(answer)
        st.session_state.display.append({"role": "assistant", "content": answer})
