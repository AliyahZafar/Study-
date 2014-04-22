from bottle import route, run, view


@route('/test/<person_name>')
@view('mytemplate')
def test(person_name):
    return {'name': person_name}


@route('/AliyaZafar')
@view('name')
def name():
    return {}


@route('/Objective')
@view('obj')
def obj():
    return {}


@route('/Summary')
@view('summary')
def summ():
    return {}

@route('/Skills')
@view('skills')
def skills():
    return {}


@route('/Experience')
@view('exp')
def exp():
    return {}


@route('/Hobbies')
@view('hobbies')
def hob():
    return {}




run(host='localhost', port=8080, debug=True)


