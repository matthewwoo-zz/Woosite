from src.models.posts import Post
import requests
import json
import unidecode

def get_posts(x):
    result = requests.get('https://medium.com/@matthewedanwoo/latest?format=json')
    result_content = result.content[16:]
    medium_json = json.loads(result_content)
    i = 0
    posts = []
    while i < x:
        title = medium_json['payload']['posts'][i]['title']
        title = unidecode.unidecode(title)
        url = medium_json['payload']['posts'][i]['uniqueSlug']
        created_at = medium_json['payload']['posts'][i]['createdAt']
        subtitle = medium_json['payload']['posts'][i]['virtuals']['snippet']
        subtitle = unidecode.unidecode(subtitle)
        reading_time = medium_json['payload']['posts'][i]['virtuals']['readingTime']
        posts.append(Post(title=title, url=url, created_at=created_at, subtitle=subtitle,
                          reading_time=reading_time).json())
        i += 1
    return posts







