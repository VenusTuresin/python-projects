# Spotify Top Hits – Data Analysis 🎶

This project explores Spotify’s **Top Hits (2000–2019)** dataset.  
Main goals were to identify the **most popular artists** and analyze how **Rihanna’s music features evolved over time**.

---

## 📂 Dataset
- Source: [Kaggle – Top Hits Spotify 2000–2019](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019)  
- Processed file: `songs_normalize.csv` (included in `data/` folder)  
- 2000 songs, 18 columns (artist, song, year, audio features like danceability, energy, tempo, etc.)  

---

## 🎯 Research Questions
1. Who are the top 15 artists with the highest cumulative popularity from 2000 to 2019?  
2. How have key audio features (Popularity, Danceability, Energy, Tempo, Valence, Acousticness, etc.) in **Rihanna’s songs** evolved over time?  

---

## 🛠 Tools & Libraries
- Python: Pandas, NumPy  
- Visualization: Matplotlib, Seaborn  
- Data source: Kaggle  

---

## 📊 Key Insights
- **Top Artists:** Identified the 15 most popular artists (2000–2019).  
- **Rihanna’s Evolution:**  
  - Popularity peaked in 2008 and 2016, reflecting both commercial hits and critical acclaim.  
  - Danceability and energy fluctuated with albums, balancing artistic depth and commercial appeal.  
  - Acousticness and instrumentalness remained very low, highlighting electronic production focus.  
  - Personal/professional events (e.g., 2009 crisis, album releases) visibly impacted her popularity trends.  

---

## 📈 Visuals
Example plots included in the notebook:  
- Bar chart of top 15 artists by cumulative popularity.  
- Line chart of Rihanna’s average popularity over years.  
- Distribution plots for Rihanna’s **danceability, energy, speechiness, tempo, valence**, and more.  

---

## 📝 Files
- `Programming_TopHitsSpotify.ipynb` → main analysis notebook  
- `data/songs_normalize.csv` → normalized dataset used in the analysis  
- `SpotifyTopHits.pdf` → presentation slides summarizing results  

---

## 🚀 Final Thoughts
This project demonstrates how music analytics can uncover both **market trends** (top artists) and **artistic evolution** (Rihanna). It combines **data cleaning, visualization, and storytelling** in a real-world dataset.

