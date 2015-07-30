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
            try:
                walk_to = step.find("./html_instructions").text
            except AttributeError:
                walk_to = "Unknown"

            try:
                time_to = step.find("./duration/text").text
            except AttributeError:
                time_to = "Unknown"

            try:
                step_details.append(walk_to + ". It will take " + time_to + ".")
            except AttributeError:
                time_to = "Unknown"

        else:
            try:
                html_inst = step.find("./html_instructions").text
            except AttributeError:
                html_inst = "Unknown"

            try:
                dep_stop = step.find(".//transit_details/departure_stop/name").text
            except AttributeError:
                dep_stop = "Unknown"
            try:
                dep_time = step.find(".//transit_details/departure_time/text").text
            except AttributeError:
                dec_stop = "Unknown"

            try:
                arr_stop = step.find(".//transit_details/arrival_stop/name").text
            except AttributeError:
                arr_stop = "Unknown"
            try:
                arr_time = step.find(".//transit_details/arrival_time/text").text
            except AttributeError:
                arr_time = "Unknown"

            if step.find(".//transit_details/line/short_name") != None:
                line = step.find(".//transit_details/line/short_name").text
            else:
                line = ""

            step_details.append("Take the " + html_inst + " Departing from " + dep_stop + " at " + dep_time + ". Arriving at " + arr_stop + " at " + arr_time + ". Route: " + line + ".")

    return step_details

