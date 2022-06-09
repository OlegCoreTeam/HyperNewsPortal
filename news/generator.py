import datetime

from django.conf import settings
import json, uuid


def get_all_data():
    with open(f"{settings.BASE_DIR}/hypernews/news.json", "r") as jsonfile:
        return json.load(jsonfile)


def set_data(text, title):
    data = get_all_data()
    now = datetime.datetime.now()
    data.append({
        'created': now.strftime("%Y-%m-%d %H:%M:%S"),
        'text': text,
        'title': title,
        'link': int(str(uuid.uuid4().int)[:8])
    })
    with open(f"{settings.BASE_DIR}/hypernews/news.json", 'w', encoding='utf8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)


def get_searched_data(searched_text):
    data = get_all_data()
    new_data = []
    for post in data:
        if searched_text.lower() in post['title'].lower():
            new_data.append(post)
        else:
            continue
    return new_data
