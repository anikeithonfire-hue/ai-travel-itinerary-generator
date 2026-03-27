import streamlit as st

st.set_page_config(page_title="Travel Planner")

st.title("AI Travel Itinerary Generator")

destination = st.text_input("Destination")
days = st.slider("Number of Days", 1, 15, 3)
interests = st.text_input("Interests")

if st.button("Generate"):
    st.write("Generating plan...")