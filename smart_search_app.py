# Import necessary libraries
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict

class CourseSearchEngine:
    def __init__(self, courses_csv: str):
        """
        Initialize the search engine with course data from a CSV file.
        
        Args:
            courses_csv (str): Path to the CSV file containing course data.
        """
        self.courses_df = pd.read_csv(courses_csv)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Create embeddings for all course titles and descriptions (categories)
        self.course_texts = (self.courses_df['Course Title'] + ' ' + self.courses_df['Categories']).tolist()
        self.course_embeddings = self.model.encode(self.course_texts)

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Search for courses based on a query.
        
        Args:
            query (str): The search query.
            top_k (int): The number of top matching courses to return.
            
        Returns:
            List[Dict]: A list of top matching courses with their details.
        """
        # Get query embedding
        query_embedding = self.model.encode([query])[0]
        
        # Calculate similarities between query and course embeddings
        similarities = np.dot(self.course_embeddings, query_embedding)
        
        # Get indices of top k matches
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Prepare result
        results = []
        for idx in top_indices:
            course = self.courses_df.iloc[idx].to_dict()
            course['similarity_score'] = float(similarities[idx])
            results.append(course)
        
        return results

# Load course data and initialize search engine
courses_csv = 'courses_pandas_20241108_190711.csv'  # Replace with your CSV path
search_engine = CourseSearchEngine(courses_csv)

# Streamlit app layout
st.title("Analytics Vidhya Course Search Engine")
st.write("Find courses based on topics of interest!")

# User input for query
query = st.text_input("Enter a topic or course title", "")

# Number of results to display
top_k = st.slider("Number of results to display", 1, 10, 5)

# Trigger search on button click
if st.button("Search"):
    if query:
        # Fetch search results
        results = search_engine.search(query, top_k=top_k)
        
        # Display results
        for result in results:
            st.subheader(result['Course Title'])
            st.write(f"Categories: {result['Categories']}")
            st.write(f"Rating: {result['Rating']} | Reviews: {result['Number of Reviews']}")
            st.write(f"[Course Link]({result['Course URL']})")
            st.write(f"Similarity Score: {result['similarity_score']:.2f}")
            st.markdown("---")  # Separator line
    else:
        st.warning("Please enter a query to search.")
