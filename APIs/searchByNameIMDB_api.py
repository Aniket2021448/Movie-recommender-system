import http.client
import json
from urllib.parse import quote

def GetIDFromName(movie_name):

    myAPI_key = "apikey 7hSbLbqnMVnRvRsttatgRx:1HxgNB8iJnU9eWI5FHMjp1"

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': myAPI_key
        }

    # req_string = f
    encoded_movie_name = quote(movie_name)
    conn.request("GET", f"/imdb/imdbSearchByName?query={encoded_movie_name}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    # data.decode("utf-8")

    decoded_data = data.decode("utf-8")

    # Parse the JSON response
    json_data = json.loads(decoded_data)

    if 'result' in json_data:
        print("In IF condition")
        movies = json_data['result']

        # Check if there are movies in the list
        if movies: # there are all movies related to the name searched
            # print(movies)
            return movies[0]



requiredMovieDetails = GetIDFromName("Creed III")

print(requiredMovieDetails.get('Title'))
print(requiredMovieDetails.get('Poster'))
print(requiredMovieDetails.get('imdbID'))


