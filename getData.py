#!/usr/bin/python
import ss2_config
import ss2
import cgi, cgitb
import urllib
import json
import os
form = cgi.FieldStorage()
data=form.getvalue('jsonString')
if(data!=""):
	shieldsquare_service_url ='http://' + ss2_config._ss2_domain + '/getss2data'
	shieldsquare_post_data = str(form['jsonString'])
	shieldsquare_post_data = shieldsquare_post_data[:-2]
	shieldsquare_post_data = shieldsquare_post_data.replace("MiniFieldStorage('jsonString', '","")
	shieldsquare_post_data = shieldsquare_post_data.replace('\\','')
	shieldsquare_post_data = urllib.unquote(shieldsquare_post_data)
	shieldsquare_post_arr=json.loads(shieldsquare_post_data)
	shieldsquare_post_arr['sid']=ss2_config._sid
	shieldsquare_post_arr['host']=os.environ[ss2_config._ipaddress]
	shieldsquare_post_data = json.dumps(shieldsquare_post_arr)
	if(ss2_config._async_http_post == "true"):
		error_code=ss2.shieldsquare_post_async(shieldsquare_service_url, shieldsquare_post_data,str(ss2_config._timeout_value))
	else:
		error_code=ss2.shieldsquare_post_sync(shieldsquare_service_url, shieldsquare_post_data, ss2_config._timeout_value)
	print "Content-type: text/html\n\n"
