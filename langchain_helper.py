from langchain.llms import OpenAI  # Import OpenAI from LangChain library
from secret_key import openapi_key  # Import the API key from a separate file

import os

# Set the OpenAI API key as an environment variable
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize the OpenAI model with a specified temperature
llm = OpenAI(temperature=0.7)


def generate_restaurant_name_and_items(cuisine, food_type):
    """
    Function to generate a restaurant name and menu items based on the given cuisine and food type.

    Args:
        cuisine (str): The type of cuisine for which the restaurant name and menu items are generated.
        food_type (str): The type of food (e.g., Halal, All Food Items) for the restaurant.

    Returns:
        dict: A dictionary containing the generated restaurant name and menu items.
    """

    # Example prompt incorporating both cuisine and food type
    prompt = f"Generate a unique restaurant name and a list of menu items for a {food_type} {cuisine} restaurant."

    # Generate response using LangChain, passing prompt as a list
    response = llm.generate([prompt], max_tokens=100)

    # Extracting the response text from the nested Generation object
    if response.generations and response.generations[0]:
        response_text = response.generations[0][0].text
    else:
        response_text = "N/A"

    # Processing the response text to extract restaurant name and menu items
    response_lines = response_text.split('\n')
    restaurant_name = None
    menu_items = []

    for line in response_lines:
        line = line.strip()
        if line.startswith('Restaurant Name:'):
            restaurant_name = line.split(':', 1)[-1].strip()
        elif line and not line.startswith('Menu Items:'):
            # Remove leading bullet points or characters
            cleaned_line = line.lstrip('-•').strip()
            if cleaned_line:
                menu_items.append(cleaned_line)

    if not restaurant_name:
        restaurant_name = "N/A"

    return {
        'name': restaurant_name,
        'menu_items': menu_items
    }
