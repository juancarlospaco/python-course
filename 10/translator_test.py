from urllib import parse, request
from json import loads

from bottle import route, run, template


def tinyslation(s, to="es", fm="en"):
    """Translate from internet via API from mymemory.translated.net."""
    api = "http://mymemory.translated.net/api/get?q={st}&langpair={fm}|{to}"
    req = request.Request(url=api.format(st=parse.quote(s), fm=fm, to=to),
                          headers={'User-Agent': ''})
    responze = request.urlopen(req).read().decode("utf-8")
    return loads(responze)['responseData']


@route('/<word_to_translate>')
def index(word_to_translate):
    return template(
        '<h1>Type 1 ENGLISH WORD on the URL to Translate<hr>{{!data}}',
        data=tinyslation(word_to_translate))


run()
