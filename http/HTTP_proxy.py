import os

proxy = 'http://user_name:password@proxy_domain:port'

## precent encode you username and password
##precent encoding for @ is %40

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy


