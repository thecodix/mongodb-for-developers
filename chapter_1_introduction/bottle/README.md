# Bottle
Bottle is a fast, simple and lightweight WSGI micro web-framework for Python. It is distributed as a single file module and has no dependencies other than the Python Standard Library.

Its main features are:

* __Routing__: Requests to function-call mapping with support for clean and dynamic URLs.
* __Templates__: Fast and pythonic built-in template engine and support for mako, jinja2 and cheetah templates.
* __Utilities__: Convenient access to form data, file uploads, cookies, headers and other HTTP-related metadata.
* __Server__: Built-in HTTP development server and support for paste, fapws3, bjoern, gae, cherrypy or any other WSGI capable HTTP server.

<img style="float: left" src="http://quintagroup.com/cms/python/bottle-python.png">

### Example: “Hello World” in a bottle

    from bottle import route, run, template
    
    @route('/hello/<name>')
    def index(name):
        return template('<b>Hello {{name}}</b>!', name=name)
    
    run(host='localhost', port=8080)

## Installation

Piece of cake.

Just run a pip install

    $ pip install bottle
    
You can save the example mentioned before on a python file, or better, locate the hello_bottle.py file on the downloaded files for the chapter 1, and run it in python

    $ python hello_bottle.py
    
Now going on the browser and opening the following address should provide you with a nice 'Hello michael' message

    http://localhost:8080/hello/michael
    
You can use the name that you want to perform the test, but is important that bottle is up and listening in port 8080 for the example to succeed

## Features
### URL Handling

An optional section shows how Bottle handles URL requests

The example attached should be straightforward. When a certain URL is targeted, the right html template is loaded
 
    import bottle
    
    @bottle.route('/')
    def home_page():
        return "Hello world\n"
    
    @bottle.route('/testpage')
    def test_page():
        return "This is a test page\n"
    
    
    bottle.debug(True)
    bottle.run(host='localhost', port=8080)


### Views

We can use custom templates, that contain html as well as python code, that will be linked to our bottle application

Example:

__fruit_form.py__

    import bottle
    
    @bottle.route('/')
    def home_page():
        mythings = ['apple', 'orange', 'banana', 'peach']
        return bottle.template('hello_world', {'username':"Richard", 'things':mythings})
        
__hello_world.tpl__

    <!DOCTYPE hml>
    <html>
    <head>
    <title>Hello World!</title>
    </head>
    <body>
    <p>
    Welcome {{username}}
    <p>
    <ul>
    %for thing in things:
    <li>{{thing}}</li>
    %end
    </ul><p>
    </body>
    </html>
    
### Handling form content

An extension on the views example before, form content is received by bottle and used on a different route


__hello_world.tpl__

    <!DOCTYPE hml>
    <html>
    <head>
    <title>Hello World!</title>
    </head>
    <body>
    <p>
    Welcome {{username}}
    <p>
    <ul>
    %for thing in things:
    <li>{{thing}}</li>
    %end
    </ul><p>
    <form action="/favorite_fruit" method="POST">
    What is your favorite fruit?
    <input type="text" name="fruit" size="40" value=""><br>
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    
__hello_world.py__
   
    import bottle

    @bottle.route('/')
    def home_page():
        mythings = ['apple', 'orange', 'banana', 'peach']
        return bottle.template('hello_world', {'username':"Richard", 'things':mythings})
    
    @bottle.post('/favorite_fruit')
    def favorite_fruit():
        fruit = bottle.request.forms.get("fruit")
        if (fruit == None or fruit == ""):
            fruit="No fruit selected"

        return bottle.template('fruit_selection.tpl', {'fruit': fruit})

### Using cookies

Cookies can store information when the page is reloaded, or visited again over a period of time

That helps for cleaner solution to access persistent data

The example shown stores a variable in a cookie, to retrieve it on a different form.

Just the code involving the cookie management is displayed this time

    @bottle.post('/favorite_fruit')
    def favorite_fruit():
        fruit = bottle.request.forms.get("fruit")
        if (fruit == None or fruit == ""):
            fruit="No fruit selected"
    
        bottle.response.set_cookie("fruit", fruit)
        bottle.redirect("/show_fruit")
    
    @bottle.route('/show_fruit')
    def show_fruit():
        fruit = bottle.request.get_cookie("fruit")
    
        return bottle.template('fruit_selection.tpl', {'fruit':fruit})

