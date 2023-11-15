import streamlit as st
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pvalue import get_p_value, autoplay_audio, is_special, roll_two_dice
from chart import make_chart, background_image

# Display the title
cs = st.columns([0.8, 0.2])
cs[0].write('## Nel Catan ci vuole Culo')
if cs[1].button('Reset'):
    pass

if 'numbers' not in st.session_state:
    st.session_state['numbers'] = [3,4,4,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,10,10,11]

with open("data/series.txt", 'r') as file:
    series = [[int(num) for num in line.split()] for line in file]

click_sounds = ['bonk', 'boom', 'bruh', 'fart', 'pop', 'sicko mode', 'slap-ahh', 'shaq-boom', 'indian-virus']
seven_sounds = ['la bela la va al fosso', 'nani', 'no god no', 'protegeme-senor', 'ooh', 'suspence', 'goofy']

cols = st.columns(7)
for i in range(2):
    for j in range(6):
        n = i * 6 + j + 1
        if cols[j].button(str(n)):
            if n == 1:
                st.success("A'ncefalitico, guarda che non può uscì l'uno...")
            else:
                if is_special(n, st.session_state['numbers'], series):
                    pass
                elif n == 7:
                    autoplay_audio(np.random.choice(seven_sounds))
                elif random.random() < 0.25:
                    autoplay_audio(np.random.choice(click_sounds))
                st.session_state['numbers'].append(n)

if len(st.session_state['numbers']) > 10:
    cols[6].write('# {:.0f}%'.format(get_p_value(st.session_state['numbers'])*100))

st.pyplot(make_chart(st.session_state['numbers']))
st.image('media/xlabels.png', use_column_width='auto')
# Add a button to clear all the data
if st.button("Clear All Data"):
    autoplay_audio('go again')
    st.success("All data has been cleared!")

background_image("media/background.png")
