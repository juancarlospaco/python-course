from datetime import datetime
from bottle import route, run, template


@route('/')
def index():
    return template('<h1>Clock | Reloj<hr> {{data}}', data=datetime.now())


run()
