import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SQL Trainer",
    page_icon="👋",
    layout="wide"
)

st.info("Kirjaudu SQL Trainer -palveluun omalla MOOC-tunnuksellasi!", icon="🚨")

components.iframe("https://sqltrainer.withmooc.fi/#1", width=1000, height=1000, scrolling=True)