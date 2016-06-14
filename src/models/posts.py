import time


class Post(object):
    def __init__(self, title, created_at, reading_time, subtitle, url):
        self.title = title,
        self.created_at = created_at,
        self.reading_time = reading_time
        self.subtitle = subtitle,
        self.url = 'https://medium.com/@matthewedanwoo/%s' % url

    def json(self):
        title = unicode(self.title).strip("(),' "" ")
        subtitle = unicode(self.subtitle).strip("(),'")
        created_at = unicode(self.created_at).strip("(),")
        created_at = int(created_at)
        created_at = time.strftime('%B %d %Y', time.localtime(created_at/1000))
        reading_time = round(float(unicode(self.reading_time).strip("(),")),2)
        return{
            'title': title,
            'created_at': created_at,
            'reading_time': reading_time,
            'subtitle': subtitle,
            'url': self.url
        }

