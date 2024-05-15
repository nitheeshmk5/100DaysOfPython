import requests
from bs4 import BeautifulSoup

res = requests.get(url='https://www.empireonline.com/movies/features/best-movies-2/')
content = res.text
soup = BeautifulSoup(content,'html.parser')
movie_name_list = soup.find_all(name='h3',class_='listicleItem_listicle-item__title__BfenH')

movie_names = [names.getText() for names in movie_name_list]

movie_names.reverse()

with open('bestMovies.txt','a') as fil:
    for movies in movie_names:
        fil.write(f'{movies}\n')