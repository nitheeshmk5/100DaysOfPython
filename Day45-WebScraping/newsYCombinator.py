import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://news.ycombinator.com/news')
yc_news = response.text

soup = BeautifulSoup(yc_news,'html.parser')
headings = soup.select('.titleline a')
main_headings =[]
for i in range(0,len(headings),2):
    main_headings.append(headings[i])


total_topics = []
total_link = []
for topics in main_headings:
    topic = topics.getText()
    article_link = topics.get('href')
    total_topics.append(topic)
    total_link.append(article_link)
    
    
score_list = soup.select('.score')
total_score = []

for sc in score_list:
    scores = sc.getText()
    score = scores.split(" ")
    total_score.append(int(score[0]))

max_upvote = max(total_score)
idx_max = total_score.index(max_upvote)

print(f'Great upvoted news is : "{total_topics[idx_max]}"\nlink : {total_link[idx_max]}\nUpvote : {max_upvote}')