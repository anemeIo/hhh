from functools import reduce


news = []
fil = 'Для 2 задачи.txt'

with open(fil, "r") as f:
    news = [line.strip() for line in f]
    positive_news = reduce(lambda x, y: x + [y] if int(y.split()[0]) > int(x[-1].split()[0]) else x, news[1:], [news[0]])

for news in positive_news:
    print(news.split(maxsplit=1)[1])