from html import entities
from bottle import route, run, template


@route('/')
def index():
    return template('<h1>Emojis and Special Chars <hr> {{!data}}',
                    data=tuple(entities.html5.items()))


run()
