import base64
import streamlit as st
from scipy.stats import chisquare


def expected_frequencies(n):
    probs = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
    return [p * n for p in probs]


def observed_frequencies(outcomes):
    freq = [0]*11
    for outcome in outcomes:
        if 2 <= outcome <= 12:
            freq[outcome - 2] += 1
    return freq


def get_p_value(outcomes):
    n = len(outcomes)
    observed = observed_frequencies(outcomes)
    expected = expected_frequencies(n)
    chi2, p = chisquare(observed, expected)
    return p

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

def is_special(n, p, series):
    if len(p) > 1:
        input_list = p[-2:].append(n)
        # Check if the input list contains the same number three times
        if len(set(input_list)) == 1:
            autoplay_audio("media/gnomo3.mp3")
            st.success("Pesca due carte che vuoi")                           
        # Check if the input list matches an item in the series list
        elif input_list in series:
            autoplay_audio("media/gnomo3.mp3")
            st.success("Pesca quattro carte che vuoi") 
        
