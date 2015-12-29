from flask import Flask, jsonify, render_template,\
request, url_for, request, Response
import requests
import ss2

app = Flask(__name__)


@app.route('/')
def index():
    print request.headers
    #print request.remote_addr
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



@app.route('/cap')
def cap():
    #print request.headers
    return render_template('index.html')


@app.route('/capsolve', methods=['POST'])
def capsolve():
    dict_data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    frm = request.form

    print type(frm)
    print "--------Data from google--------"
    print frm

    google_cap_data = {
        "secret" : "6Lf9KA4TAAAAAGLFYivqkNud4sLAQO5wwadBx4lP",
        "response"  :   frm['g-recaptcha-response'],
        "remoteip"  :   request.remote_addr
    }

    google_cap_api_url = "https://www.google.com/recaptcha/api/siteverify"
    res = requests.post(google_cap_api_url, data = google_cap_data)
    print res.text
    return "True"

if __name__ == '__main__':
    app.run()
