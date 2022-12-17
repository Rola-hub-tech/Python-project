import requests
from bs4 import BeautifulSoup
import pandas

list_of_url = ['https://www.trustpilot.com/review/briangavindiamonds.com',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=2',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=3',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=4',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=5',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=6',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=7',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=8',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=9',
               'https://www.trustpilot.com/review/briangavindiamonds.com?page=10']
names = []
reviews = []
data_string = ""
for url in list_of_url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.find_all("span", {'class', 'typography_heading-xxs__QKBS8 typography_appearance-default__AAY17'}):
        data_string = data_string + item.get_text()
        names.append(data_string)
        data_string = ""
    for item in soup.find_all("p", {'class', 'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'}):
        data_string = data_string + item.get_text()
        reviews.append(data_string)
        data_string = ""
reviews_dict = {'Reviewer Name': names, 'Reviews': reviews}
df = pandas.DataFrame.from_dict(reviews_dict, orient='index')
df.dropna(axis=1, inplace=True)
store_reviews = df.to_dict('list')
for i in store_reviews:
    print(int(i + 1), store_reviews[i], "\n")
