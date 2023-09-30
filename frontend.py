import requests
import streamlit as st

# Streamlit UI
st.title("Search Here")
search_data = st.text_input("Enter your search query:")
search_button = st.button("Search")

# Backend API endpoint
api_url = "http://localhost:5000/data"


# Function to fetch data from the backend
def fetch_data(query):
    response = requests.get(api_url, params={"query": query})
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Display search results
if search_button:
    if search_data:
        st.write("Searching for:", search_data)
        results = fetch_data(search_data)
        if results:
            st.write("Search Results:")
            for result in results:
                st.write("-", result)
        else:
            st.write("No results found.")
    else:
        st.write("Please enter a search query.")
