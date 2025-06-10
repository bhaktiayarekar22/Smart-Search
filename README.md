# 🔍 Analytics Vidhya Course Search Engine

A semantic search engine built with Streamlit and Sentence Transformers that helps users find relevant courses from Analytics Vidhya's course catalog based on natural language queries.

## 📌 Project Overview

This project implements an intelligent course recommendation system that uses semantic similarity to match user queries with relevant courses. Unlike traditional keyword-based search, this system understands the context and meaning of queries to provide more accurate course recommendations.

## ✨ Features

- **Semantic Search**: Uses pre-trained sentence transformers to understand query context
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Similarity Scoring**: Provides relevance scores for each course recommendation
- **Customizable Results**: Users can adjust the number of results displayed
- **Course Details**: Shows comprehensive information including ratings, reviews, and direct links

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Sentence Transformers**: Pre-trained model for semantic embeddings
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **all-MiniLM-L6-v2**: Lightweight transformer model for embeddings

## 📋 Prerequisites

```bash
pip install streamlit pandas sentence-transformers numpy
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd course-search-engine
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Ensure your CSV file contains columns: `Course Title`, `Categories`, `Rating`, `Number of Reviews`, `Course URL`
   - Update the `courses_csv` variable in the code with your CSV file path

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📊 How It Works

1. **Data Loading**: Loads course data from CSV file
2. **Embedding Generation**: Creates vector embeddings for course titles and categories
3. **Query Processing**: Converts user queries into embeddings
4. **Similarity Calculation**: Computes cosine similarity between query and course embeddings
5. **Results Ranking**: Returns top-k most similar courses with similarity scores

## 🎯 Usage

1. Enter a topic or course-related query in the search box
2. Adjust the number of results using the slider (1-10)
3. Click "Search" to get recommendations
4. Browse through results with similarity scores and course details

## 📁 Project Structure

```
course-search-engine/
├── app.py                 # Main Streamlit application
├── courses_data.csv       # Course dataset
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🙏 Acknowledgments

- [Sentence Transformers](https://www.sbert.net/) for the pre-trained models
- [Streamlit](https://streamlit.io/) for the web framework
- [Analytics Vidhya](https://www.analyticsvidhya.com/) for the course data

---

⭐ If you found this project helpful, please give it a star!
