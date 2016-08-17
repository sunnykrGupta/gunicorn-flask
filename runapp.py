

import requests

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort, jsonify
from flask.ext.cors import CORS, cross_origin

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
        "secret" : "6LvqkNu-DEV-API-KEY--wadBx4lP",
        "response"  :   frm['g-recaptcha-response'],
        "remoteip"  :   request.remote_addr
    }

    google_cap_api_url = "https://www.google.com/recaptcha/api/siteverify"
    res = requests.post(google_cap_api_url, data = google_cap_data)
    print res.text
    return "True"


total_api_ss_pack  = 0

@app.route('/api/ep/' , methods=['POST', 'GET'])
@cross_origin(origin="*") # Allow All Cross Origin call
def api_jscall():
    global total_api_ss_pack
    total_api_ss_pack += 1
    print "API/v1/ssjs -------------log : ", total_api_ss_pack, " \n\n"
    print "HTTP Method Type : %s" % request.method

    print request.headers

    print "\nREMOTE ADDR-- : \t", request.remote_addr

    '''
    print "\nPath requested-------------"
    print request.path

    print "\nCookie -------------"
    print request.cookies
    '''
    print "\nData Recieved ->",
    print request.json
    print request.data

    '''
    r = requests.post(SS_JS_API, request.json)
    print r.status_code
    #print r.json
    print r.text
    '''
    time.sleep(.1) # delays for 100 milli-seconds
    rmtext = {"data" : "this is body .. Wait more"}
    return make_response(jsonify(rmtext), 200)
    #return make_response(open('angular_flask/templates/index.html').read())



@app.route('/api/health' , methods=['GET'])
@cross_origin(origin="*") # Allow All Cross Origin call
def api_health():
    print "/api/health --", "HTTP Method Type : %s" % request.method

    print request.headers

    print "\nREMOTE ADDR-- : \t", request.remote_addr

    return make_response("OK API", 200)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

