import bottle

@bottle.route('/')
def home_page():
    myThings = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', username="Chrisi", things=myThings)
bottle.debug(True)
bottle.run(host='localhost', port=8081)