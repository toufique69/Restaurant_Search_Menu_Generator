import streamlit as st
import langchain_helper

# Set up the page configuration and aesthetics of the app
st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️", layout="wide")


# Function to load and apply custom CSS for styling the app
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')


# App title and description, displayed at the top of the app
st.title("🍽️ Restaurant Name Generator")
st.markdown("""
    Generate unique names and menu items for different cuisines.
    Select a cuisine and food type, and let the magic happen!
""")

# Sidebar configuration for user input
# This section contains a dropdown menu for selecting cuisines
with st.sidebar:
    st.header("Choose Options")
    cuisine = st.selectbox("Pick a Cuisine",
                           ("Finnish", "Italian", "Mexican", "Arabic", "American", "Spanish", "Bangali"))

    # New dropdown for food type, visible after selecting a cuisine
    food_type = None
    if cuisine:
        food_type = st.selectbox("Select Food Type", ("Halal", "All Food Items"))

# Main content based on selected options
if cuisine and food_type:
    st.markdown(f"## You selected {cuisine} cuisine with {food_type} food.")

    # Call the function from langchain_helper.py to generate restaurant name and menu items
    result = langchain_helper.generate_restaurant_name_and_items(cuisine, food_type)

    # Display the generated restaurant name and menu items
    st.markdown(f"### Generated Restaurant Name: {result['name']}")
    st.markdown(f"### Menu Items:")
    for item in result['menu_items']:
        st.markdown(f"- {item}")

# You can expand this section based on the specific functionalities of your application.


# Footer section of the app
# Includes a simple text footer
st.markdown("---")
st.markdown("👩‍🍳 Built with Streamlit and LangChain")
st.markdown("© 2023 by Toufique Hasan")