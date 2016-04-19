from bottle import route, run, template


@route('/')
def index():
    return template('<h1> Hello World  {{data}}', data="")


run()
