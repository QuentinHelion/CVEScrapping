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
            print("not find")
            return []

        results = []
        for row in results_table.find_all(name='tr', class_='srrowns'):
            cells = row.find_all('td')

            if len(cells) != 15:
                continue
            cve_id = cells[1].find('a').text.strip()
            severity = cells[7].find('div').text.strip()
            published_date = cells[5].text.strip()
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

        summary = soup.find('div', {'id': 'cvssscorestable'}).find('div', {'class': 'cvedetailssummary'}).text.strip()
        references = []
        for reference in soup.find_all('a', {'class': 'ref-link'}):
            references.append(reference['href'])

        return {
            'summary': summary,
            'references': references
        }
