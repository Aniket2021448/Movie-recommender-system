myAPI_key = "apikey 7hSbLbqnMVnRvRsttatgRx:1HxgNB8iJnU9eWI5FHMjp1"


import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': myAPI_key
    }

conn.request("GET", "/imdb/imdbSearchById?movieId=tt1375666", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))