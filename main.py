import streamlit as st
import pandas as pd

st.title(body="Hello,CHI SEI ")

name = st.text_input(label="Inserisci qua il tuo nome penso lo capisci ")

if name:
    st.write(f"{name}!")
    if name == "Lu":
        st.write("Saverio è un grande il migliore ,NON DORMIAMO A LEZIONE Lucrez")

clicked = False
button = st.button(label="Greet me!")
if button and name:
    clicked = True
    st.write(f"Hello again, {name}!")

if st.button(label="Say Goodbye") and name:
    st.write(f"Goodbye, {name}!")

data = {
    "Name": ["Saverio", "Lu", "Charlie"],
    "Age": [21, 20, 35],
    "soprannome": ["Savez", "Lucertola", "Charlie"],
    "Aura": [1000, 500, 2],
    "sonno": [50, 1000000000, 2],
}
df = pd.DataFrame(data)

if name:
    st.write(df)

    st.bar_chart(data=df, x="Name", y="Aura")

    st.title("quanto ci piaece dormire")
    st.line_chart(data=df, x="Name", y="sonno")