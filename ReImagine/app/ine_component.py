from . import ine
from . import models

def get_posts(rslash,limit):
    obj = ine.INE()
    total_posts = []
    posts = obj.getNewPost(rslash,limit)
    for i in posts:
        url = i[0]
        title = i[1]
        _post  = models.Post(title,url)
        total_posts.append(_post)
    return total_posts
