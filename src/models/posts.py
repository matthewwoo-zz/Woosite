
class Post(object):
    def __init__(self, title, created_at, reading_time, subtitle, url):
        self.title = title,
        self.created_at = created_at,
        self.reading_time = reading_time,
        self.subtitle = subtitle
        self.url = 'https://medium.com/@matthewedanwoo/%s' % url

    def json(self):
        return {
            'title': self.title,
            'created_at': self.created_at,
            'reading_time': self.reading_time,
            'subtitle': self.subtitle,
            'url': self.url
        }


