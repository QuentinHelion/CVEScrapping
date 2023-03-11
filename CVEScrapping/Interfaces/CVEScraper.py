import requests
from bs4 import BeautifulSoup

class CVEScraper:
    def __init__(self):
        self.base_url = "https://www.cvedetails.com"

    def search(self, query):
        url = self.base_url + "/vulnerability-search.php?f=1&keywords=" + query
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        results_table = soup.find('table', {'class': 'searchresults'})
        if not results_table:
            return []

        results = []
        ID_CELLS = 1
        SEVERITY_CELLS = 7
        PLUBLISHED_CELLS = 5

        for row in results_table.find_all(name='tr', class_='srrowns'):
            cells = row.find_all('td')

            if len(cells) != 15:
                continue
            cve_id = cells[ID_CELLS].find('a').text.strip()
            severity = cells[SEVERITY_CELLS].find('div').text.strip()
            published_date = cells[PLUBLISHED_CELLS].text.strip()
            results.append({
                'cve_id': cve_id,
                'severity': severity,
                'published_date': published_date
            })
        return results

    def details(self, cve_id):
        url = self.base_url + "/cve/" + cve_id
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        summary = soup.find('div', {'class': 'cvedetailssummary'}).text.strip()
        details_table = soup.find('table', {'id': 'cvssscorestable'})
        cells = details_table.find_all('td')

        if len(cells) != 9:
            return


        SEVERITY_CELL  = 0
        CONFIDENTIALITY_CELL  = 1
        INTEGRITY_CELL  = 2
        IMPACT_CELL  = 3
        COMPLEXITY_CELL  = 4
        AUTHENTICATION_CELL  = 5
        TYPE_CELL = 7


        details = {
            'name':             cve_id,
            'severity':         cells[SEVERITY_CELL].text.strip(),
            'confidentiality':  cells[CONFIDENTIALITY_CELL].find('span').text.strip() if cells[CONFIDENTIALITY_CELL].find('span').text.strip() != '' else "N/A",
            'integrity':        cells[INTEGRITY_CELL].find('span').text.strip() if cells[INTEGRITY_CELL].find('span').text.strip() != '' else "N/A",
            'impact':           cells[IMPACT_CELL].find('span').text.strip() if cells[IMPACT_CELL].find('span').text.strip() != '' else "N/A",
            'complexity':       cells[COMPLEXITY_CELL].find('span').text.strip() if cells[COMPLEXITY_CELL].find('span').text.strip() != '' else "N/A",
            'authentication':   cells[AUTHENTICATION_CELL].find('span').text.strip() if cells[AUTHENTICATION_CELL].find('span').text.strip() != '' else "N/A",
            'type':             cells[TYPE_CELL].text.strip() if cells[TYPE_CELL].text.strip() != '' else "N/A",
            'link':             self.base_url + "/cve/" + cve_id
        }

        return details
