

# Movie Recommendation Engine

The Movie Recommendation Engine is a content-based web application that suggests movies to users based on item attributes (such as genres, tags, or plot descriptions). Built using **Python**, **Pandas**, **Scikit-Learn**, and **Streamlit**, it converts unstructured textual movie metadata into mathematical vectors and uses similarity metrics to recommend titles closely related to a user's selection.

---

## 🏗️ Core Architecture & Data Pipeline

The system operates across a 4-stage pipeline:

```text
[ Raw CSV Data ] ➡️ [ Data Preprocessing ] ➡️ [ Feature Extraction (TF-IDF) ]
                                                            │
                                                            ▼
[ Streamlit Web UI ] ⬅️ [ Top-N Ranking ] ⬅️ [ Cosine Similarity Matrix ]

1.Data Ingestion & Preprocessing
	Dataset: movielens_100k.csv contains movie metadata including unique identifiers, titles, and content attributes (genres/tags).
	Cleaning: Pandas processes the dataset to remove null values, clean formatting, and combine metadata fields into a unified text feature string per movie (e.g., combining genre keywords like "Action Adventure Sci-Fi").
2.Text Feature Extraction (TF-IDF Vectorization)
Computers cannot directly evaluate textual titles or genres, so text must be converted into numerical representations using TF-IDF (Term Frequency-Inverse Document Frequency):
	Term Frequency ("TF" ): Measures how frequently a word appears in a specific movie's metadata.
	Inverse Document Frequency ("IDF" ): Measures how common or rare a word is across the entire dataset. Words that appear everywhere (e.g., "the", "movie") receive a lower weight, while specific genre descriptors (e.g., "Noir", "Cyberpunk") receive higher weights.
  "TF-IDF" (t,d,D)="TF" (t,d)×log⁡(N/(|{d∈D:t∈d}|))
  Scikit-Learn's TfidfVectorizer transforms the dataset into a high-dimensional numerical matrix where each row represents a movie and each column represents a weighted term score.
3. Similarity Calculation (Cosine Similarity)
  To determine how similar two movies are, the system calculates the angle between their high-dimensional vector representations using Cosine Similarity:
  "Cosine Similarity" (A,B)=(A⋅B)/(‖A‖‖B‖)
	Score = 1.0: Perfect similarity (identical content features).
	Score = 0.0: No similarity (completely distinct attributes).
The resulting Similarity Matrix stores precomputed closeness scores for every pair of movies in the dataset.
4. Recommendation Engine Logic & Web UI
	User Input: The user selects a movie title via a Streamlit dropdown menu in app.py.
	Lookup & Sorting: The engine identifies the selected movie's row index in the similarity matrix, extracts all similarity scores relative to other movies, sorts them in descending order, and filters out the query movie itself.
	Output: The top-N most similar movies (e.g., Top 5 or Top 10) are returned and displayed on the Streamlit web dashboard.

PROJECT ARCHITECTURE & STEPS INVOLVED
The project implementation is divided into four key stages:
Step 1: Data Loading & Preprocessing
	     Loaded movie metadata from movielens_100k.csv using Pandas.
	     Cleaned missing values, removed duplicates, and formatted text fields (e.g., titles, genres, and overviews/tags) into standardized string tokens.
Step 2: Feature Extraction (TF-IDF Vectorization)
	     Utilized Scikit-Learn's TfidfVectorizer to convert text descriptions and genre tags into numerical feature vectors.
	     TF-IDF (Term Frequency-Inverse Document Frequency) measures word importance while downweighting common non-informative words.
Step 3: Similarity Computation (Cosine Similarity)
	      Computed pairwise similarity using Cosine Similarity:
        "Cosine Similarity"=(A⋅B)/‖A‖‖B‖ 
	      Constructed a similarity matrix mapping each movie vector against all other titles to calculate geometrical closeness.
Step 4: Web UI Development & Recommendation Generation
	      Designed a web interface in app.py using Streamlit.
	      Added a dropdown/search selection for titles.
	      When a user selects a movie, the engine retrieves its row index, ranks the top cosine similarity scores in descending order, and displays the top recommended titles.
        Tech Stack
	      Language: Python 3.10+
	      Data Manipulation: Pandas, NumPy
	     Machine Learning / NLP: Scikit-Learn (TfidfVectorizer, cosine_similarity)
	     Frontend Web Framework: Streamlit


How to Run Locally
1. Clone the Repository
Bash
git clone [https://github.com/tarushi23bai11182/movie-recommender.git](https://github.com/tarushi23bai11182/movie-recommender.git)
cd movie-recommender
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Run the Application
Bash
streamlit run app.py
The Streamlit web server will start and automatically open in your local browser at http://localhost:8501.

Features
- Search for movies in the dataset.
- Get instant content-based recommendations using TF-IDF and Cosine Similarity.
- Interactive user interface built with Streamlit.

Tech Stack
- **Python**
- **Pandas**
- **Scikit-Learn**
- **Streamlit**





  
