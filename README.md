# Movie Recommendation Engine
![Image](https://img.freepik.com/free-vector/seamless-pattern-with-cinema-elements_225004-1154.jpg?t=st=1715784274~exp=1715787874~hmac=d7427c470a321aafb34f0063d5ad070ed7338f028d5c9becea4ffa1f84fd3435&w=740)
## Introduction
The Movie Recommendation Engine is a content-based filtering system designed to recommend movies to users based on their movie preferences. It employs machine learning algorithms to analyze the user's past movie ratings and suggests new movies that closely match their tastes. The system creates a user profile to capture movie preferences and compares it to a database of movie attributes to find similar movies.

## Goals
The primary goal of the Movie Recommendation Engine is to provide users with personalized movie recommendations based on their selected Movie,
thus enhancing their movie-watching experience.

## Skills
The development of the Movie Recommendation Engine involves expertise in the following areas:
- Machine Learning
- Natural Language Processing
- Data Analysis
- Web Development (for the recommendation engine interface)
- Flask


## Live Running On
The recommendation engine is live and accessible at [Movie Recommendation Engine](https://movie-recommendation-pofr.onrender.com).

## Usage
To use the recommendation engine, follow these steps:
1. Visit the provided link to access the recommendation engine.
2. Enter your movie preferences, such as genre, cast, director, etc.
3. Click on the "Recommend" button to receive personalized movie recommendations.

## Data
The movie dataset used by the recommendation engine is a subset of the TMDB Movies dataset. It includes movie attributes such as genre, cast, director, and plot summary.

## Algorithm
The recommendation engine utilizes the cosine similarity algorithm to find similar movies based on their attributes. T
his algorithm computes the cosine similarity between two movie vectors and returns a value between 0 and 1, with 1 indicating a perfect match.

## Project Flow
1. Data Preprocessing: Utilized natural language processing (NLP) techniques to process and clean movie attributes such as plot summaries and cast information.
2. Feature Engineering: Implemented vectorization techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) to represent movie attributes as numerical vectors.
3. Algorithm Development: Developed the recommendation algorithm using cosine similarity to calculate the similarity between user preferences and movie attributes.
4. Model Deployment: Deployed the recommendation engine using web development frameworks for user interaction and hosted it on a server for accessibility.

## Limitations
The content-based filtering movie recommendation engine has some limitations:
- It heavily relies on movie attributes, potentially overlooking new or lesser-known movies with fewer shared attributes.
- It does not consider the user's social connections or wider industry trends, which may limit the diversity of recommended movies.

## Contributing
If you are interested in contributing to the recommendation engine, please fork the repository and submit a pull request. We welcome contributions of all types, including bug fixes, feature enhancements, and documentation improvements.
