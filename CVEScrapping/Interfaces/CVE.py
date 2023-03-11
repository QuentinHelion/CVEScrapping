class CVE:
    def __init__(self):
        self.detailsPath = "Results/Details-Results/"
        self.searchPath = "Results/Search-Results/"

    def writeDetails(self,name,data):
        output = self.detailsPath + name+ '.txt'
        with open(output,'w') as txt:
            for key, value in data.items():
                txt.write(f'{key}: {value}\n')

    def writeSearch(self,name,data):
        output = self.searchPath + name + '.txt'
        with open(output,'w') as txt:
            for item in data:
                txt.write(item)