import httplib2
from urllib import urlencode
def directions(origin, destination):
    parameters = {"origin":origin + ", uk", "destination":destination + ", uk","mode":"transit", "key":"AIzaSyB-6vE5lQe3GwCXRZLpsbek9R2nmzB6Dl4"}
    nice = urlencode(parameters)

    h = httplib2.Http(".cache")
    response, content = h.request("https://maps.googleapis.com/maps/api/directions/json?" + nice)
    return content

print directions("cambridge", "kings cross")
