__author__ = 'mbagget1'

import argparse
from lxml import etree

parser = argparse.ArgumentParser(description='Use to specify a collection')
parser.add_argument("-c", "--collection", dest="collection", help="namespace of collection", required=True)
parser.add_argument("-l", "--link", dest="fedoraurl", help="url of fedora instance")
parser.add_argument("-p", "--port", dest="portnumber", help="port number of fedora instance")
parser.add_argument("-f", "--filename", dest="destfilename", help="name of file you want to save your set to")
args = parser.parse_args()

def createfile(filename):
    f = open(filename, 'w')
    token = etree.parse(fullSearchString).findall('//{http://www.fedora.info/definitions/1/0/types/}token')
    processresults(fullSearchString, f, token)

def processresults(fullSearchString, f, token):
    token = etree.parse(fullSearchString).findall('//{http://www.fedora.info/definitions/1/0/types/}token')
    results = etree.parse(fullSearchString).findall('//{http://www.fedora.info/definitions/1/0/types/}pid')
    tokenval = etree.parse(fullSearchString).findall('//{http://www.fedora.info/definitions/1/0/types/}token')[0].text
    for item in results:
        f.write(item.text)
    if len(token) == 1:
        newSearchString = fullSearchString + "&sessionToken=" + tokenval
        processresults(newSearchString, f, token)
    else:
        f.close()

if __name__ == "__main__":

    # Defaults
    fedoraurl = 'http://digital.lib.utk.edu'
    fedcollection = ''
    portnumber = ":8080"
    filename = "recordset.txt"

    if args.fedoraurl:
        fedoraurl = "http://{0}".format(args.fedoraurl)
    if args.collection:
        fedcollection = "{0}*".format(args.collection)
    if args.portnumber:
        portnumber = args.portnumber
    if args.destfilename:
        filenamedest = "{0}.txt".format(args.destfilename)

    fullSearchString = fedoraurl + ":8080/fedora/objects?query=pid%7E" + fedcollection + "&pid=true&resultFormat=xml"

    createfile(filename)
