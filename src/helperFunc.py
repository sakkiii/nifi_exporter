import requests
import json


def getToken(url, login, password):
  endpoint = url
  data = {"username":login, "password":password}
  headers = {'Content-Type' : 'application/x-www-form-urlencoded' }
  p = requests.post(endpoint, data,headers=headers, verify=False)
	
  if p.status_code == 201:
    return p.text
  else:
    return p

def getHeaders(token):
  headers = {}
  if token != None:
    headers = {'authorization': "Bearer " + token }
  return headers

def getCluster(url, token, cert, ca_cert_file):
  headers = getHeaders(token)
  response = requests.get(url, headers=headers, verify=ca_cert_file, cert=cert)
  #logger.debug( response.text)
  jData = json.loads(response.text)
  return jData['cluster']['nodes']

def convertStatus(status):
  if status == 'CONNECTED':
    return 1
  else:
    return 0

def getFlow(url, token, cert, ca_cert_file):
  headers = getHeaders(token)
  response = requests.get(url, headers=headers, verify=ca_cert_file, cert=cert)
  jData = json.loads(response.text)
  return jData['controllerStatus']

def about(url, token, cert, ca_cert_file):
  headers = getHeaders(token)
  response = requests.get(url, headers=headers, verify=ca_cert_file, cert=cert)
  jData = json.loads(response.text)
  return jData['about']

def getProcessorFlow(url, token, cert, ca_cert_file):
  headers = getHeaders(token)
  response = requests.get(url, headers=headers, verify=ca_cert_file, cert=cert)
  jData = json.loads(response.text)
  return jData['processGroups']