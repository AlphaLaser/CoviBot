import streamlit as st
import chatbot
import nltk
nltk.download('popular', quiet=True)
from PIL import Image
from bokeh.models.widgets import Div
import tts
import intents

m = st.sidebar.markdown("""
<style>

.reportview-container .main .block-container{
    padding-top : 35px ;

}

div.stButton > button:first-child {
    width : 95% ;
    align: center;
    border-radius : 10px ;
    height: 100px ;

}
</style>
""", unsafe_allow_html=True)

m = st.markdown("""
<style>
    st.form.submit_button{

        background-color : blue ;

    }
}
</style>
""", unsafe_allow_html=True)
title = st.sidebar.header('Navigator 🧭')
st.sidebar.markdown('<hr>', unsafe_allow_html=True)
# st.sidebar.markdown('<br>', unsafe_allow_html=True)

if st.sidebar.button('What to ask'):
    js = "window.open('https://light-feeling-5c3.notion.site/What-to-ask-Question-database-7111cde13ffe428faa66075aee099f29')"  # New tab or window
    # js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

if st.sidebar.button('Github'):
    js = "window.open('https://github.com/AlphaLaser/para-tools')"  # New tab or window
    # js = "window.location.href = 'https://github.com/AlphaLaser/para-tools'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
st.sidebar.markdown('<br>', unsafe_allow_html=True)
st.sidebar.markdown('<br>', unsafe_allow_html=True)
title = st.sidebar.header('Contact Us 📞')
st.sidebar.markdown('<hr>', unsafe_allow_html=True)
# st.sidebar.markdown('<br>', unsafe_allow_html=True)

if st.sidebar.button('E-Mail'):
    js = "window.open('mailto:aditmagotra@gmail.com')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

if st.sidebar.button('Whatsapp'):
    js = "window.open('https://api.whatsapp.com/send?phone=919958877036')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
logo = Image.open(r'images\logo.png')
st.image(logo)
st.markdown('<hr>', unsafe_allow_html=True)
tts_text = (chatbot.para_bot(intents.intents))
print("This tts text ." + tts_text + ".")
st.markdown('<hr>', unsafe_allow_html=True)

if tts_text != " " :
    st.header('Audio Output')
    st.markdown('<br>', unsafe_allow_html=True)
    tts.tts(tts_text)
else :
    st.header("Ask a question to listen to the audio output !")


