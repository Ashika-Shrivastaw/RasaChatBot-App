import xml.etree.ElementTree as ET


def buildUrl(value):
    tree = ET.parse("http://cdn.salontracker.co.uk/publicwebdownloads/HelpVideos/HelpVideoConfig.xml")
    root = tree.getroot()
    descriptionArray = []
    categoryNameArray = []
    videoNameArray = []
    for x in root.iter('Description'):
        descriptionArray.append(x.text)
    for y in root.iter('VideoName'):
         videoNameArray.append(y.text)

    url = "http://cdn.salontracker.co.uk/publicwebdownloads/HelpVideos/"+y
    print(url)
    return url