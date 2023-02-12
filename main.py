import pandas as pd
import numpy as np
import requests
import json
from flask import Flask, render_template, request

api_key = '8265bd1679663a7ea12ac168da84d2e8'

# Importing The Files
text_df = pd.read_pickle("movies_list.pkl")
similarity_df = pd.read_pickle("similarity_df.pkl")
list(text_df['title'])
# Function Which Recommends Movies Based on Search

app = Flask(__name__, template_folder='template', static_folder='static')
@app.route('/')
def hello():
    return render_template('home.html', suggestions=list(text_df['title']))

@app.route('/Recommended', methods=['POST'])
def Recommend():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
    title=to_predict_list['movie_title']
    index = text_df[text_df['title'] == title].index.values[0]
    distances = pd.DataFrame(similarity_df.loc[index])
    suggestions_index = distances.sort_values(by=index, ascending=False).index[:5]
    suggestions_name = text_df[text_df.index.isin(suggestions_index)]['title'].values
    suggestions_posters = []
    suggestions_description = []
    suggestion_links = []
    suggestion_rating = []
    for movie_id in suggestions_index:
        request_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        print(request_url)
        response = requests.get(request_url)
        response = response.json()
        suggestions_posters.append('https://image.tmdb.org/t/p/original/%s' % response['poster_path'])
        suggestions_description.append('%s' % response['overview'])
        suggestion_links.append('https://www.imdb.com/title/%s/'%response['imdb_id'])
        suggestion_rating.append(round(response['vote_average'], 2))
    all_list = zip(suggestion_links, suggestions_posters, suggestions_name, suggestions_description,suggestion_rating)
    return render_template('results.html', search=title, all_list=all_list)

@app.route('/Notebook')
def view_notebook():
    return render_template('Notebook.html')

@app.route('/info')
def view_info():
    return render_template('idea.html')
if __name__ == "__main__":
    app.run(debug=True)
