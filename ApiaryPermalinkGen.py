import fileinput
import argparse
import re
import errno

import sys

defaultOutputFile = "apiaryWithPermaLinks.txt"

apiNameLineRegex = "^## \w.*"
apiNameSliceRegex = "(?!##) (?!\w.)"
oldPermaLinkRegex = "<a.*>"

numPermalinks = 0
outPutFile = ""
cmdParser = object
removeOldPermalinks = False


def getMatchedLine(regex, line):
    m = re.search(regex, line)
    if m:
        return m
    return None


def getTokenizedApiName(slicePoint, foundLine):
    lowerCaseApiName = foundLine.lower()
    return lowerCaseApiName[3:slicePoint].replace(" ", "-")


def getPermaLinkName(foundLine):
    slicePoint = getMatchedLine(apiNameSliceRegex, foundLine)
    if slicePoint:
        slicePoint = slicePoint.start()
        return getTokenizedApiName(slicePoint, foundLine)


def getLineWithPermalink(line):
    foundLine = getMatchedLine(apiNameLineRegex, line)
    s = ""
    if foundLine:
        s = getPermaLinkName(foundLine.string)
        return "<a name=\"" + s + "\"/>"


def isOldPermalink(line):
    foundPermalink = getMatchedLine(oldPermaLinkRegex, line)
    if foundPermalink:
        return True
    return False


def writePermaLinkToFile(file, line, permaLink):
    s = line + permaLink + "\n"
    file.write(s)


def checkIfReadable(file):
    try:
        textfile = open(file, 'r')
        textfile.close()
    except IOError as e:
        if e.errno == errno.EACCES:
            print("file exists, but isn't readable")
        elif e.errno == errno.ENOENT:
            print("files isn't readable because it isn't there")
        sys.exit()


def writeToFile(inputFile, outFile=defaultOutputFile):
    with fileinput.FileInput(inputFile) as file, open(outFile, 'w') as new:
        global numPermalinks
        for line in file:
            s = ""
            permaLinkLine = getLineWithPermalink(line)
            if permaLinkLine:
                writePermaLinkToFile(new, line, permaLinkLine)
                numPermalinks += 1
            elif removeOldPermalinks and isOldPermalink(line):
                new.write("")
            else:
                new.write(line)


def createParser():
    global cmdParser
    cmdParser = argparse.ArgumentParser(description='Permalink creator for apiary Blueprint')
    cmdParser.add_argument('-i', '--input_file', help='File that contains apiary document', required=True)
    cmdParser.add_argument('-c', action="store_true", help='Clear existing permalinks', required=False)
    cmdParser.add_argument('-o', '--output_file', help='Output file apiary doument with permalinks', required=False)


def getArguments():
    return cmdParser.parse_args()


def checkForClearPermaliks(args):
    global removeOldPermalinks
    if args.c:
        removeOldPermalinks = True


def endPrint():
    print("Wrote: {} permalinks to {}".format(numPermalinks, outPutFile))


def main():
    global outPutFile
    createParser()

    inputFile = getArguments().input_file
    outPutFile = getArguments().output_file

    checkIfReadable(inputFile)
    checkForClearPermaliks(getArguments())

    if outPutFile:
        checkIfReadable(outPutFile)
        writeToFile(inputFile, outPutFile)
    else:
        outPutFile = defaultOutputFile
        writeToFile(inputFile)

    endPrint()


main()
