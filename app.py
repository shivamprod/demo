import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

radius = st.slider("Select the radius of the circle", min_value=0.0, max_value=100.0, value=1.0)
area = 3.14159 * radius ** 2
st.write(f"The area of the circle with radius {radius} is {area:.2f}")

if st.button("Calculate Area"):
    st.markdown(
        f"<h2 style='color: green;'>Area: {area:.2f}</h2>",
        unsafe_allow_html=True
    )