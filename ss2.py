#! /usr/bin/python

import Cookie
from StringIO import StringIO
import datetime
import json
import math
import os
import random
import subprocess
import time
import urllib
import urllib2
import uuid

import pycurl

import ss2_config
from tty import CFLAG


class shieldsquareRequest:

	_zpsbd0 = "false"
	_zpsbd1 = ""
	_zpsbd2 = ""
	_zpsbd3 = ""
	_zpsbd4 = ""
	_zpsbd5 = ""
	_zpsbd6 = ""
	_zpsbd7 = ""
	_zpsbd8 = ""
	_zpsbd9 = ""
	_zpsbda = ""
	__uzma = ""
	__uzmb = 0
	__uzmc = ""
	__uzmd = 0

class shieldsquareCurlResponseCode:

	error_string = ""
	responsecode = 0


class shieldsquareResponse:

	pid = ""
	responsecode= 0
	url = ""
	reason =""


class shieldsquareCodes:

	ALLOW   = 0
	MONITOR = 1
	CAPTCHA = 2
	BLOCK   = 3
	FFD   = 4
	ALLOW_EXP = -1

def shieldsquare_ValidateRequest( shieldsquare_username, shieldsquare_calltype, shieldsquare_pid ):

	shieldsquare_low  = 10000
	shieldsquare_high = 99999
	shieldsquare_a = 1
	shieldsquare_b = 3
	shieldsquare_c = 7
	shieldsquare_d = 1
	shieldsquare_e = 5
	shieldsquare_f = 10
	shieldsquare_time = int(time.time())
	cflg=0
	shieldsquare_request = shieldsquareRequest()
	shieldsquare_RETURNCODES = shieldsquareCodes()
	shieldsquare_response = shieldsquareResponse()
	shieldsquare_response.dynamic_JS = "var __uzdbm_c = 2+2"
	shieldsquare_curl_response = shieldsquareCurlResponseCode()
	shieldsquare_service_url = 'http://' + ss2_config._ss2_domain + '/getRequestData'


	if( ss2_config._timeout_value > 1000 ):
	    shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW_EXP
	    shieldsquare_response.reason = "ShieldSquare Timeout cant be greater then 1000 Milli seconds"
	    return shieldsquare_response.__dict__;
	if( shieldsquare_calltype == 1 ):
		try:
			shieldsquare_pid = shieldsquare_generate_pid(ss2_config._sid)
		except ValueError:
			shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW_EXP
			shieldsquare_response.reason = "Invalid SID"
			return shieldsquare_response.__dict__;
	else:
		if ( len(shieldsquare_pid) == 0 ):
			shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW_EXP
			shieldsquare_response.reason = "PID Cant be null"
			return shieldsquare_response.__dict__;
	cookie=Cookie.SimpleCookie()

	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		cflg=1
	except (Cookie.CookieError, KeyError):
		cflg=0

	if cflg == 1 and cookie.has_key('__uzma'):

		cookie_string=os.environ.get('HTTP_COOKIE')
		cookie.load(cookie_string)
		shieldsquare_lastaccesstime =  (cookie["__uzmd"].value if (cookie.has_key("__uzmd")) else 0)
		shieldsquare_uzmc = (cookie["__uzmc"].value if (cookie.has_key("__uzmc")) else 0)
		shieldsquare_uzmc = shieldsquare_uzmc[shieldsquare_e:]
		shieldsquare_a = int(shieldsquare_uzmc) - shieldsquare_c / (shieldsquare_b + shieldsquare_d)
		shieldsquare_uzmc= str(random.randint(shieldsquare_low, shieldsquare_high)) + str(shieldsquare_c+shieldsquare_a*shieldsquare_b) + str(random.randint(shieldsquare_low, shieldsquare_high))
		shieldsquare_ex_time = 3600*24*365*10 + 1*1*3*60*60
		cookie['__uzma'] = cookie["__uzma"].value
		cookie['__uzma']['expires']= shieldsquare_ex_time
		cookie['__uzmb']=cookie["__uzmb"].value
		cookie['__uzmb']= shieldsquare_ex_time
		cookie['__uzmc']=shieldsquare_uzmc
		cookie['__uzmc']['expires']= shieldsquare_ex_time
		cookie['__uzmd']=shieldsquare_time
		cookie['__uzmd']['expires']= shieldsquare_ex_time

		shieldsquare_request.__uzma = cookie["__uzma"].value
		shieldsquare_request.__uzmb = (cookie["__uzmb"].value if (cookie.has_key("__uzmb")) else 0)
		shieldsquare_request.__uzmc = shieldsquare_uzmc
		shieldsquare_request.__uzmd = shieldsquare_lastaccesstime

	else:
		shieldsquare_uzma = uuid.uuid1()
		str(shieldsquare_uzma)
		shieldsquare_lastaccesstime = shieldsquare_time
		shieldsquare_uzmc= str(random.randint(shieldsquare_low, shieldsquare_high)) + str(shieldsquare_c+shieldsquare_a*shieldsquare_b) + str(random.randint(shieldsquare_low, shieldsquare_high))
		shieldsquare_ex_time =3600*24*365*10 + 1*1*3*60*60
		cookie['__uzma']=shieldsquare_uzma
		cookie['__uzma']['expires']= shieldsquare_ex_time
		cookie['__uzmb']=int(time.time())
		cookie['__uzmb']['expires']= shieldsquare_ex_time
		cookie['__uzmc']=shieldsquare_uzmc
		cookie['__uzmc']['expires']= shieldsquare_ex_time
		cookie['__uzmd']=int(time.time())
		cookie['__uzmd']['expires']= shieldsquare_ex_time

		shieldsquare_request.__uzma = str(shieldsquare_uzma)
		shieldsquare_request.__uzmb = shieldsquare_time
		shieldsquare_request.__uzmc = shieldsquare_uzmc
		shieldsquare_request.__uzmd = shieldsquare_lastaccesstime

	if(ss2_config._mode == "Active"):
		shieldsquare_request._zpsbd0 = 'true'
	else:
		shieldsquare_request._zpsbd0 = 'false'

	shieldsquare_request._zpsbd1 = ss2_config._sid
	shieldsquare_request._zpsbd2 = shieldsquare_pid
	shieldsquare_request._zpsbd3 = ''
	shieldsquare_request._zpsbd4 = ''
	shieldsquare_request._zpsbd5 = ''
	shieldsquare_request._zpsbd6 = ''
	shieldsquare_request._zpsbd7 = ''

	if "HTTP_REFERER" in os.environ:
		shieldsquare_request._zpsbd3 = os.environ['HTTP_REFERER']

	if "REQUEST_URI" in os.environ:
		shieldsquare_request._zpsbd4 = os.environ['REQUEST_URI']

	if cookie.has_key(ss2_config._sessid):
		shieldsquare_request._zpsbd5 = cookie[ss2_config._sessid].value

	if ss2_config._ipaddress in os.environ:
		shieldsquare_request._zpsbd6 = os.environ[ss2_config._ipaddress]

	if "HTTP_USER_AGENT" in os.environ:
		shieldsquare_request._zpsbd7 = os.environ['HTTP_USER_AGENT']

	shieldsquare_request._zpsbd8 = shieldsquare_calltype
	shieldsquare_request._zpsbd9 = shieldsquare_username
	shieldsquare_request._zpsbda = shieldsquare_time
	shieldsquare_json_obj = json.dumps(shieldsquare_request.__dict__)
	shieldsquare_response.pid =shieldsquare_pid
	shieldsquare_response.url =ss2_config._js_url
	if(ss2_config._mode == "Active"):
		shieldsquare_curl_response = shieldsquare_post_sync(shieldsquare_service_url, shieldsquare_json_obj, ss2_config._timeout_value)
		if(str(shieldsquare_curl_response[1]) != '200'):
			shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW_EXP
			shieldsquare_response.reason = shieldsquare_curl_response[0]
		else:
			shieldsquare_response_from_ss = json.loads(str(shieldsquare_curl_response[0]))
			shieldsquare_response.dynamic_JS = shieldsquare_response_from_ss['dynamic_JS']
			n=int(shieldsquare_response_from_ss['ssresp'])
			if n==0:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW
			elif n==1:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.MONITOR
			elif n==2:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.CAPTCHA
			elif n==3:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.BLOCK
			elif n==4:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.FFD
			else:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW_EXP
				shieldsquare_response.reason = str(shieldsquare_curl_response[1])
	else:
		if(ss2_config._async_http_post == 'true'):
			error_code=shieldsquare_post_async(shieldsquare_service_url, shieldsquare_json_obj,str(ss2_config._timeout_value))
			if(str(error_code[1])!='None'):
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW_EXP
				shieldsquare_response.reason = "Request Timed Out/Server Not Reachable"
			else:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW
		else:
			error_code=shieldsquare_post_sync(shieldsquare_service_url, shieldsquare_json_obj,ss2_config._timeout_value)

			if(str(error_code[1])!='200'):
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW_EXP
				shieldsquare_response.reason = str(error_code[0])
			else:
				shieldsquare_response.responsecode = shieldsquare_RETURNCODES.ALLOW
		#shieldsquare_response.dynamic_JS = "var __uzdbm_c = 2+2"
	return shieldsquare_response.__dict__;

def shieldsquare_post_async(url, payload, timeout):
	data = urllib.quote(payload)
	cmd = 'curl --fail --silent -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" -m '+ timeout + ' ' + url + " -d '"+ data + "'" +" &"
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	response=[output,err]
	return response;

def shieldsquare_post_sync(url, params, timeout):
	data = urllib.quote(params)
	storage = StringIO()
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.TIMEOUT_MS, timeout)
	c.setopt(pycurl.NOSIGNAL, 1)
	c.setopt(pycurl.VERBOSE, False)
	c.setopt(pycurl.WRITEFUNCTION, storage.write)
	c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, data)
	try:
		response=c.perform()
		content = storage.getvalue()
		response=[content,c.getinfo(c.RESPONSE_CODE)]
	except:
		response=["Request Timed Out/Server Not Reachable","0"]
	c.close()
	return response;
def microtime(get_as_float = False):
	if get_as_float:
		return time.time();
	else:
		return '%f %d' % math.modf(time.time());

def shieldsquare_generate_pid(shieldsquare_sid):
	t=microtime()
	tm=t.split(" ")
	p1,p2,p3,p4,p5 = shieldsquare_sid.split("-")
	sid_min = num = int(p4,16);
	rmstr1= "00000000" + "%x" % int(tm[1])
	rmstr2= "0000" + "%x" % int(round(float(tm[0]) * 65536))
	return '%08s-%04x-%04s-%04s-%04x%04x%04x' % (shieldsquare_IP2Hex(),sid_min,rmstr1[-4:],rmstr2[-4:],
			random.randint(0,0xffff), random.randint(0,0xffff), random.randint(0,0xffff));


def shieldsquare_IP2Hex():
	hexx=""
	ip=os.environ[ss2_config._ipaddress]
	part=ip.split('.')
	hexx=""
	for i in range(0,len(part)):
		dt = "0" + "%x" % int(part[i])
		hexx = hexx + dt[-2:]

	return hexx;

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

if __name__== "__main__":
	ls = shieldsquare_ValidateRequest( "testuser", 1, '')
	print ls
