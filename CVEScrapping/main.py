from Class import *
from Interfaces import *


def main():
    print("Starting...")
    scraper = CVEScraper()
    # results = scraper.search("apache2")
    # for result in results:
        # print(result)

    details = scraper.details("CVE-2022-23943")
    print(details)

    print("ending...")

if __name__ == "__main__":
    main()
