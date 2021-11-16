#!/usr/bin/python
import urllib
import urllib2 
import md5

data = 'e9654c012dc42f9f78f81a685073df98'
decode = 'c627e19450db746b739f41b64097d449:HHj57RG8BQA=4714c627c5195786fc112b67eca599d675d5454b:00000003:1064eaa9478a0396:auth:a2baed8041744d5c3d6cc250222d5930'
# a2 = 'auth:a2baed8041744d5c3d6cc250222d5930'

# url = 'http://ctfq.u1tramarine.blue/q9/htdigest'
url = 'https://ksnctf.sweetduet.info/problem/9/flag.html'
username = 'q9'
realm = 'secret'
nonce = ''
uri = '/~q9/flag.html'
algorithm = 'MD5'
responce = ''
qop = 'auth'
nc = '00000003'
cnonce = '1064eaa9478a0396'
a1 = 'c627e19450db746b739f41b64097d449'
a2 = 'GET:' + uri

def getNonce():
    try:
        data = urllib2.urlopen(url)
        html = data.read()
    except urllib2.HTTPError, e:
        nonce = e.info()['WWW-Authenticate'].split('"')[3]
        return nonce
    
def genMD5(str):
    return md5.new(str).hexdigest()

def genResponce(nonce):
    responce = genMD5(a1 + ':' + nonce + ':' + cnonce + ':' + qop + ':' + genMD5(a2))
    return responce

def genAuthorized(nonce, responce):
    genAuthorized = 'Digest username="' + username + '", realm"' + realm + '", nonce="' + nonce + '",uri="' + uri + '", algorithm=' + algorithm + ', response="' + response + '", qop=' + qop + ', nc=' + nc + ', cnonce="' + cnonce + '"'
    return genAuthorized

def main():
    nonce = getNonce()
    responce = getResponce(nonce)
    auth = getAuthorized(nonce, responce)
    header = {'Authorization' : auth}
    req = urllib2.Request(url, None, header)
    try:
        data = urllib2.urlopen(req)
        html = data.read()
        print(html)
    except urllib2.HTTPError, e:
        print(e.code)
        print(e.info())



