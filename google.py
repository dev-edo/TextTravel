import httplib2
import xml.etree.ElementTree as ET
from urllib import urlencode
def directions(origin, destination):
    parameters = {"origin":origin + ", uk", "destination":destination + ", uk","mode":"transit", "key":"AIzaSyB-6vE5lQe3GwCXRZLpsbek9R2nmzB6Dl4"}
    nice = urlencode(parameters)
    
    h = httplib2.Http(".cache")
    response, content = h.request("https://maps.googleapis.com/maps/api/directions/xml?" + nice)

    root = ET.fromstring(content)
    dep_stop = root.find(".//transit_details/departure_stop/name").text
    dep_time = root.find(".//transit_details/departure_time/text").text
    arr_stop = root.find(".//transit_details/arrival_stop/name").text
    arr_time = root.find(".//transit_details/arrival_time/text").text
    line = root.find(".//transit_details/line/short_name").text

    inst = "Departing from " + dep_stop + " at " + dep_time + ". Arriving at " + arr_stop + " at " + arr_time + ". TOC: " + line + "."

    return inst
    
print directions("huddersfield", "slough")
