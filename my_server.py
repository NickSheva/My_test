import requests
from bs4 import BeautifulSoup

url = 'http://samotlor.tv'

page = requests.get(url)

print(page.status_code)

new_news = []
news = []
news_items = []

# Самое время воспользоваться BeautifulSoup  и скармить ему наш page, указав в кавычках как он нам поможет 'html.parser'
soup = BeautifulSoup(page.text, 'html.parser')
soup2 = str(soup)
with open('my_file.txt', 'w') as f:
    f.write(soup2)
#print(soup)


# функция поиска
#news = soup.findAll('a', class_='lenta')
news = soup.findAll('h4', class_='entry-title')
print(news)

for news_items in news:
    if news_items.find('a') is not None:
        new_news.append(news_items.text)

for i in range(len(new_news)):
    f.write("\n".join(new_news))

f.close()
for news_item in news:
    if news_item.find('span', class_='time2 time3') is not None:
        news.append(news_item.text)
print(f'{news =}')

for data in new_news:
    print(data)