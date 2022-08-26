import streamlit as st

st.set_page_config(
    page_title="Welcome to GaitScribe!",
    page_icon="👋",
)

#st.title("Main Page")
#st.sidebar.success("Select a page above.")
a1, a2, a3 = st.columns((3,3,3))
with a1:
    # name
with a2:
    # age
with a3:
    # Type of orthoses

b1, b2 , b3 = st.columns(3)
b1.metric("Cadence", "73 steps/min", "+8%")
b2.metric("Stride Length", "1.4 m", "-4%")
b3.metric("Knee Angle", "8°", "4%")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
