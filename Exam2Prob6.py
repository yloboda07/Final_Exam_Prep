class Localizer: 
    def __init__(self, filename): 
        self.translations = self.read_file(filename) 

    def read_file(self, filename): 
        word = "" 
        lang = "" 
        trans = {} 
        with open(filename) as fh: 
            for line in fh: 
                line = line.strip() 
                eqloc = line.find("=") 
                if eqloc ==-1: 
                    word = line 
                else: 
                    lang = line[:eqloc]
                    new = line[eqloc + 1 :] 
                    trans[(word, lang)] = new 
        return trans 
    def localize(self, word, lang): 
        return self.translations.get((word, lang), word)



my_localizer = Localizer("data2.txt")
print(my_localizer.localize("Open", "de"))