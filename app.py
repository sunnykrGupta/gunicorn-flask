from flask import Flask, jsonify, render_template,\
request, url_for, request, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('redr.html')

@app.route('/page')
def render_page():
    return render_template('web.html')

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


# Define a route for the default URL, which loads the form
@app.route('/form')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)
    #return "Data passed"


if __name__ == '__main__':
    app.run()
