import json

class CVE:
    def __init__(self):
        self.detailsTXTPath = "Results/Details-Results/TXT-files/"
        self.searchTXTPath = "Results/Search-Results/TXT-files/"
        self.detailsJSONPath = "Results/Details-Results/JSON-files/"
        self.searchJSONPath = "Results/Search-Results/JSON-files/"

    def writeDetailstxt(self,name,data):
        output = self.detailsTXTPath + name+ '.txt'
        with open(output,'w') as txt:
            for key, value in data.items():
                txt.write(f'{key}: {value}\n')

    def writeDetailsjson(self,name,data):
        output = self.detailsJSONPath + name+ '.json'
        with open(output,'w') as output:
            json.dump(data,output)

    def writeSearchtxt(self,name,data):
        output = self.searchTXTPath + name + '.txt'
        with open(output,'w') as txt:
            for item in data:
                for key, value in item.items():
                    txt.write(f'{key}: {value}\n')
    
    def writeSearchjson(self,name,data):
        output = self.searchJSONPath + name + '.json'
        with open(output,'w') as txt:
            for item in data:
                txt.write(item)