import streamlit as st

# st.title("First Streamlit App")
# st.title("My First Streamlit App")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is a simple text")
# st.write("This is a write command")
# st.markdown("### This is a markdown header")
# st.caption("This is a caption")
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")
age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)
st.write(f"You are {age} years old.")

#Slider
temperature = st.slider("Select temperature:", min_value=-0, max_value=100, value=25, step=1)
st.write(f"The selected temperature is {temperature}°C.")

#Button
if st.button("Click Me"):
    st.write("Button clicked!")
    st.balloons()

#Selectbox
color = st.selectbox("Select your favorite color:", ["Red", "Green", "Blue", "Yellow"])
st.write(f"Your favorite color is {color}.")

#Layout Components
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the first column.")
with col2:
    st.header("Column 2")
    st.write("This is the second column.")

#Sidebar
st.sidebar.title("Settings")
st.sidebar.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])
st.file_uploader("Upload a file:")
if uploaded_file is not None:
    st.sidebar.write("File not found.")