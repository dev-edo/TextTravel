import httplib2
import xml.etree.ElementTree as ET
from urllib import urlencode
def directions(origin, destination):
    parameters = {"origin":origin + ", uk", "destination":destination + ", uk","mode":"transit", "key":"AIzaSyB-6vE5lQe3GwCXRZLpsbek9R2nmzB6Dl4"}
    nice = urlencode(parameters)
    
    h = httplib2.Http()
    response, content = h.request("https://maps.googleapis.com/maps/api/directions/xml?" + nice)

    root = ET.fromstring(content)

    step_details = []
    
    for step in root.findall(".//leg/step"):
        if step.find("./travel_mode").text == "WALKING":
            walk_to = step.find("./html_instructions").text
            time_to = step.find("./duration/text").text
            step_details.append(walk_to + ". It will take " + time_to + ".")
        else:
            html_inst = step.find("./html_instructions").text
            dep_stop = step.find(".//transit_details/departure_stop/name").text
            dep_time = step.find(".//transit_details/departure_time/text").text
            arr_stop = step.find(".//transit_details/arrival_stop/name").text
            arr_time = step.find(".//transit_details/arrival_time/text").text
            if step.find(".//transit_details/line/short_name") != None:
                line = step.find(".//transit_details/line/short_name").text
            else:
                line = ""

            step_details.append("Take the " + html_inst + " Departing from " + dep_stop + " at " + dep_time + ". Arriving at " + arr_stop + " at " + arr_time + ". TOC: " + line + ".")

    return step_details

