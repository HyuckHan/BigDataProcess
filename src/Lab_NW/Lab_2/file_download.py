import urllib
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve("http://storage.googleapis.com/patents/grantbib/2014/ipgb20141125_wk47.zip", "ipgb20141125_wk47.zip" )
