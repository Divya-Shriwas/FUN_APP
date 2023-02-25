import streamlit as st

st.title(":red[Innomatics] Data App")
st.snow()
btn_click = st.button("Don't click Me")

st.write(btn_click)

if btn_click == True:
    st.subheader(":red[You clicked me]:cry:")
    st.balloons()