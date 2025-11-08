# 🎬 Visualizing Movie Recommendation System

## 🧠 Introduction
**Visualizing Movie Recommendation System** is an interactive platform designed to make movie recommendations transparent, personalized, and engaging.  
Unlike conventional systems that simply suggest films, this project focuses on *explaining why* a movie is recommended — using visualizations to enhance user trust and experience.

By integrating **collaborative filtering (SVD)** with **interactive visualizations**, this project bridges the gap between data-driven predictions and user interpretability. It also includes upcoming **2025 movie releases**, making the recommendations more forward-looking and relevant.

---

## 🎯 Problem Definition
Traditional recommendation systems often suffer from:
- **Lack of transparency** – users are unsure why a film was suggested.  
- **Cold-start problem** – new users without prior ratings receive poor recommendations.  
- **Low engagement** – systems feel static and impersonal.  

This project addresses the core question:  
> *How can we visualize and explain personalized movie recommendations to improve user trust and engagement?*

---

## 🧩 Proposed Methods
Our solution combines **data-driven prediction** with **intuitive visualization** to make recommendations more understandable and enjoyable.

### Two-Step Recommendation Framework
1. **Collaborative Filtering (SVD)**  
   Predict user-movie ratings based on existing MovieLens data.
2. **Visualization Layer**  
   Provide explainable insights using genre comparison charts and latent space visualizations.

---

## ⚙️ Methodology

### 📊 Data Sources
- **MovieLens Small Dataset**  
  • 100,000 ratings across 9,000+ movies and 600+ users.  
  • Used for collaborative filtering and historical rating analysis.

- **Top 100 Trending Movies of 2025 (Kaggle)**  
  • Dataset includes upcoming movies with predicted box-office trends.  
  • Enables future-oriented recommendations.

---

### 🧼 Data Exploration and Preprocessing
- Cleaned and merged `movies.csv` and `ratings.csv` datasets.  
- Encoded categorical genres for analysis.  
- Conducted exploratory visualizations in **Tableau** to identify rating trends and genre distributions.

---

### 🤖 Machine Learning Pipeline
- Implemented **SVD (Singular Value Decomposition)** using the **Surprise** library for rating prediction.  
- Performed **PCA (Principal Component Analysis)** using **scikit-learn** to visualize latent relationships between movies.  
- Evaluated model accuracy through RMSE and MAE metrics.

---

### 📈 Visualization and Interaction
- **Tableau Dashboard:** Visualized genre distributions and top-rated movies.  
- **Plotly Interactive Charts:** Compared user preferences vs. recommended movies.  
- **Streamlit Web App:** Provided genre and movie selection blocks for new users, displaying recommendations dynamically with interactive charts.

---

## 🌟 Novel Aspects
- 🎨 **Visual Transparency:** Users can see *why* each recommendation was made.  
- 🧩 **Cold-Start Handling:** New users input genres and liked movies to bootstrap personalized recommendations.  
- 🧠 **Latent Space Visualization:** PCA projections illustrate relationships between movies in 2D.  
- 💬 **Interactive UI:** Built with **Streamlit + Plotly**, enhancing engagement and explainability.

---

## 🧮 Example Workflow

**User 1 Ratings:**
- Movie 1 (Drama, Thriller): 4.0  
- Movie 2 (Drama, Comedy): 5.0  
- Movie 3 (Comedy): 3.0  

**Genre Averages:**
- Drama: 4.5 | Thriller: 4.0 | Comedy: 4.0  

For a new movie “*Thunderbolts*” (Action, Adventure), the system estimates:  
> **Predicted Rating:** (4.0 + 4.0) / 2 = 4.0  

This result is then visually represented through similarity charts and PCA scatter plots.

---

## 🧪 Experiments and Evaluation

| Task | Model | Metric | Result |
|------|--------|--------|--------|
| Rating Prediction | SVD | RMSE | ~0.87 |
| Dimensionality Reduction | PCA | Variance Retained | 93% |
| Visualization Performance | Streamlit + Plotly | Load Time | < 2 sec avg |

**Key Findings**
- The SVD model captures latent factors effectively.  
- Visualization significantly improves user interpretability.  
- Integrating future movie data enhances recommendation novelty.

---

## 🖼️ Visualization Interfaces

### Tableau Dashboard  
Displays top-rated genres and rating distributions.  
👉 [View on Tableau](https://public.tableau.com/app/profile/sanjana.jd/viz/Dashboard_Movies_17439531158310/Dashboard1?publish=yes)

### Streamlit Application  
Interactive interface for new users to explore recommendations.  
🎥 [Live Demo](https://movie-recommendation-hfgqpcxlsqpwxn59gwfknr.streamlit.app/)
(unavailable at the moment)

---

## 🧰 Tools and Frameworks

| Category | Technologies |
|-----------|---------------|
| Core | Python, Pandas |
| Machine Learning | Surprise (SVD), scikit-learn (PCA) |
| Visualization | Tableau, Plotly |
| Application | Streamlit |
| Environment | Jupyter, VSCode |

---

## 🚀 Future Improvements
- **Hybrid Models:** Combine collaborative and content-based methods.  
- **Deep Learning:** Integrate neural CF or autoencoders for non-linear interactions.  
- **Explainability Enhancements:** Visualize “why this movie” through attention maps or SHAP.  
- **Deployment:** Containerize with Docker and explore A/B testing for live user feedback.

---

## 💬 Conclusions and Discussion
The system successfully:
- Improves transparency in recommendations.  
- Enhances engagement through interactive visuals.  
- Provides meaningful predictions for both current and upcoming movies.  

By visualizing the reasoning behind recommendations, users gain insight into their preferences — making the system more trustworthy and enjoyable.

---

## 📚 Bibliography
- Harper & Konstan (2015): *The MovieLens Datasets: History and Context.*  
- Koren et al. (2009): *Matrix Factorization Techniques for Recommender Systems.*  
- Bellogin et al. (2020): *Transparency in Recommender Systems.*  
- Lex et al. (2020): *Exploring Evolving User Preferences in Entertainment Data.*

---
