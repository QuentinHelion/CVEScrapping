class CVE:
    def __init__(self):
        self.detailsPath = "Results/Details-Results/"

    def writeDetails(self,name,data):
        output = self.detailsPath + name+ '.txt'
        with open(output,'w') as txt:
            for key, value in data.items():
                txt.write(f'{key}: {value}\n')