from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hi puppy</h1>"

@app.route('/info')
def info():
    return "<h1>Puppies are funny</h1>"

# creating a dynamic route
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1".format(name.upper())
    # return "<h1>50th letter: {}</h1".format(name[50])

@app.route('/puppy/latin/<name>')
def puppyLatin(name):
    if name[-1]!='y':
        return "<h1>{}y</h1".format(name)
    else:
        newName = name[0:-1]
        return "<h1>{}iful</h1>".format(newName)


# run the app. 
# debug=True when developing the app; set to false when the app is in production
if __name__ == '__main__':
    app.run(debug=True)
