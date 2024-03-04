# recommendation_script.py

import pickle
import pandas as pd
# Load the model
with open('BOW_model.pkl', 'rb') as model_file:
    similarity = pickle.load(model_file)

df = pd.read_csv('D:\\PROJECTS\\Movie-recommender-system\\df.csv')

# Define the recommend function
def recommend(movie):
    movies = []
    index = df[df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        movies.append(df.iloc[i[0]].title)
    return movies


