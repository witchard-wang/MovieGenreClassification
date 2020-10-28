import requests
import pandas as pd
import tmdbsimple as tmdb

tmdbv3 = '9bc7e5ee4b6c54454c8b6f0fadf4a1cf'
tmdbv4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5YmM3ZTVlZTRiNmM1NDQ1NGM4YjZmMGZhZGY0YTFjZiIsInN1YiI6IjVmOTYzMTQxODhiMTQ4MDAzNjQ0OGQwYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nycR-lmbBjeFTabTI4aEa3-cSpQf83BgwW1ZrJqRWmQ'

tmdb.API_KEY = tmdbv3
movie = tmdb.Movies(603)
response = movie.info()
print(movie.title)
