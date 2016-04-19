from calendar import HTMLCalendar
from bottle import route, run, template


@route('/')
def index():
    return template('<h1>Calendar | Calendario<hr> {{!data}}',
                    data=HTMLCalendar().formatyearpage(2016))


run()
