import urllib.request
import json

def printData(data):

  # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

  # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded\n")

  # for each event, print the place where it occurred
    for i, event in enumerate(theJSON["features"]):
        print(str(i + 1) + ") " + str(event["properties"]["place"]))
    print("\n-----------\n")

  # print the events that only have a magnitude greater than 4
    i = 1
    for event in theJSON["features"]:
        if(event["properties"]["mag"] >= 4.0):
            print(str(i) + ") " + "%2.1f" % event["properties"]["mag"], event["properties"]["place"])
            i += 1
    print("\n-----------\n")
    
  # print only the events where at least 1 person reported feeling something
    for event in theJSON["features"]:
        feltReports = event["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" % event["properties"]["mag"], event["properties"]["place"], 
                    " reported " + str(feltReports) + " times")

  
def main():
  # Variable that holds the source URL
  # In this case it is the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)

  # If response code is 200 OK print the data,
  # oherwise print corresponding error
  if(webUrl.getcode() == 200):
      data = webUrl.read()
      printData(data)
  else:
      print("Received error, cannot parse results")



if __name__ == "__main__":
  main()