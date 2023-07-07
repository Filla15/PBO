# XML Python
import xml.sax

class MovieHandler(xml.sax.ContentHandler):

    #constructor
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.start = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag

        if tag =="movie":
            print("******** Movie *******")
            title = attributes['title']
            print ("Title:", title)

    def endElement(self, tag):
        if self.CurrentData == "type":
            print ("Type: ", self.type)
        elif self.CurrentData == "format":
            print ("Format: ", self.format)
        elif self.CurrentData == "year":
            print ("Year: ", self.year)
        elif self.CurrentData == "rating":
            print ("Rating: ", self.rating)
        elif self.CurrentData == "stars":
            print ("Stars: ", self.start)
        elif self.CurrentData == "description":
            print ("Description: ", self.description)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        if self.CurrentData == "format":
            self.format = content
        if self.CurrentData == "year":
            self.year = content
        if self.CurrentData == "rating":
            self.rating = content
        if self.CurrentData == "stars":
            self.stars = content
        if self.CurrentData == "description":
            self.description = content

if ( __name__== "__main__"):
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces,0)

        Handler = MovieHandler()
        parser.setContentHandler(Handler)
        parser.parse("movie.xml")