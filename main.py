#Python code to illustrate parsing of XML files
# importing the
# cont ="" required modules
import csv
import requests
import xml.etree.ElementTree as ET


"""
BEGIN:VCARD
VERSION:2.1
N:Gump;Forrest;;Mr.
TEL;WORK;VOICE:
END:VCARD
"""     
def openFile():
    # xmlfile = parseXML('frank.dew')
    # create element tree object
    tree = ET.parse('frank.dew')
    # get root element
    root = (tree.getroot())
    # print(root)
    items = list(root)
    result =""
    cont =""
    for item in items:
        cont+="BEGIN:VCARD\nVERSION:2.1\nN:"
        name=""
        phone=""
        for x in list(item):
            if(x.tag == "name"):
                name = x.attrib["data1"].replace(" ", ";")+";;"
            elif(x.tag =="phone_v2"):
                phone+= "TEL;WORK;VOICE:"+x.attrib["data1"]+"\n"
        cont+=name+"\n"
        cont+=phone+"END:VCARD\n"

        fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
  
        # writing to csv file
        with open("contFrank.vcf", 'w') as file:
    
            file.write(cont)





def parseXML(xmlfile):
  
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    newsitems = []
  
    # iterate news items
    for item in root.findall('./channel/item'):
  
        # empty news dictionary
        news = {}
  
        # iterate child elements of item
        for child in item:
  
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
  
        # append news dictionary to news items list
        newsitems.append(news)
      
    # return news items list
    return newsitems
  
  
def savetoCSV(newsitems, filename):
  
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
  
    # writing to csv file
    with open(filename, 'w') as csvfile:
  
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
  
        # writing headers (field names)
        writer.writeheader()
  
        # writing data rows
        writer.writerows(newsitems)
  
      
def main():
    openFile()
    # # load rss from web to update existing xml file
    # loadRSS()
  
    # # parse xml file
    # newsitems = parseXML('topnewsfeed.xml')
  
    # # store news items in a csv file
    # savetoCSV(newsitems, 'topnews.csv')
      
      
if __name__ == "__main__":
    main()