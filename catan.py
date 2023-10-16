import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pvalue import get_p_value
from chart import make_chart

# Display the title
st.title("Nel Catan ci vuole Culo")

cols = st.columns(7)
for i in range(2):
    for j in range(6):
        n = i * 6 + j + 1
        if cols[j].button(str(n)):
            if n == 1:
                st.success("A'ncefalitico, guarda che non può uscì l'uno...")
            else:
                with open("data.txt", "a") as f:
                    f.write(f"{n}\n")


# Load all numbers from the text file and display a histogram
with open("data.txt", "r") as f:
    numbers = f.readlines()
numbers = [int(n.strip()) for n in numbers]
if len(numbers) > 10:
    cols[6].write('# {:.0f}%'.format(get_p_value(numbers)*100))

st.pyplot(make_chart(numbers))

# Add a button to clear all the data
if st.button("Clear All Data"):
    with open("data.txt", "w") as f:
        f.write("")
    st.success("All data has been cleared!")
