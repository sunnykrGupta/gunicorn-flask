#!/usr/bin/python2.7

#print #Enter your SID
_sid = "651a9649-23c0-4300-9272-a6aad8bb60f0"

#Please specify the mode in which you want to operate
#mode = "Active";
#mode = "Monitor";
_mode = 'Monitor'

#Asynchronous HTTP Data Post
#Setting this value to true will reduce the page load time when you are in Monitor mode.
#This uses Linux CURL to POST the HTTP data using the EXEC command.
#Note: Enable this only if you are hosting your applications on Linux environments.
_async_http_post = 'false'

#* Timeout in Seconds or Milliseconds (based on the  $_timeout_type value)
_timeout_value = 100

#* PHPSESSID is the default session ID for PHP, please change it if needed
_sessid = ''

#* Change this value if your servers are behind a firewall or proxy
_ipaddress = ''

#* Enter the URL fo the JavaScript Data Collector
_js_url = '/getData.py'

# Set the ShieldSquare domain based on your Server Locations
#    US/Europe    	-    'ss_scus.shieldsquare.net'
#    India/Asia    -    'ss_sa.shieldsquare.net'
_ss2_domain='0.0.0.0:5000/api/v1/ssjs'


