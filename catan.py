import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pvalue import get_p_value, autoplay_audio
from chart import make_chart, background_image

# Display the title
st.title("Nel Catan ci vuole Culo")

with open("data/data.txt", "r") as f:
    p_numbers = f.readlines()

with open("data/series.txt", 'r') as file:
    series = [[int(num) for num in line.split()] for line in file]
    
cols = st.columns(7)
for i in range(2):
    for j in range(6):
        n = i * 6 + j + 1
        if cols[j].button(str(n)):
            if n == 1:
                st.success("A'ncefalitico, guarda che non può uscì l'uno...")
            else:
                if is_special(n,p_numbers, series):
                    pass
                elif n == 7:
                    autoplay_audio("media/la bela la va al fosso.mp3")
                with open("data/data.txt", "a") as f:
                    f.write(f"{n}\n")

with open("data/data.txt", "r") as f:
    numbers = f.readlines()
numbers = [int(n.strip()) for n in numbers]
if len(numbers) > 10:
    cols[6].write('# {:.0f}%'.format(get_p_value(numbers)*100))

st.pyplot(make_chart(numbers))
st.image('media/xlabels.png', use_column_width='auto')
# Add a button to clear all the data
if st.button("Clear All Data"):
    with open("data/data.txt", "w") as f:
        f.write("")
    st.success("All data has been cleared!")

background_image("media/background.png")
