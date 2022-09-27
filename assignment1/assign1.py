from bs4 import BeautifulSoup
from requests import get
import re
import pandas as pd


headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://www.imdb.com/title/tt5420376/episodes?season=1' #getting the page
response = get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

episode_containers = soup.find_all('div', class_='info')
episode_containers[0].a['title']
episode_containers[0].meta['content']
episode_containers[0].find('div', class_='airdate').text.strip()
episode_containers[0].find('span', class_='ipl-rating-star__rating').text
episode_containers[0].find('span', class_='ipl-rating-star__total-votes').text
episode_containers[0].find('div', class_='item_description').text.strip()

riverdale_episodes = []

for sn in range(1,7):
    response = get('https://www.imdb.com/title/tt5420376/episodes?season=' + str(sn))
    page_html = BeautifulSoup(response.text, 'html.parser')
    episode_containers = page_html.find_all('div', class_ = 'info')

    for episodes in episode_containers:
            season = sn
            episode_number = episodes.meta['content']
            title = episodes.a['title']
            airdate = episodes.find('div', class_='airdate').text.strip()
            rating = episodes.find('span', class_='ipl-rating-star__rating').text
            total_votes = episodes.find('span', class_='ipl-rating-star__total-votes').text
            desc = episodes.find('div', class_='item_description').text.strip()
            episode_data = [season, episode_number, title, airdate, rating, total_votes, desc]
            riverdale_episodes.append(episode_data)


riverdale_episodes = pd.DataFrame(riverdale_episodes, columns = ['season', 'episode_number', 'title', 'airdate', 'rating', 'total_votes', 'desc'])
riverdale_episodes.head()


def remove_str(votes):
    for r in ((',', ''), ('(', ''), (')', '')):
        votes = votes.replace(*r)

    return votes

riverdale_episodes['total_votes'] = riverdale_episodes.total_votes.apply(remove_str).astype(int)

riverdale_episodes.head()

riverdale_episodes.to_csv('Riverdale_Episodes_IMDb_Ratings.csv',index=False)


