from Class import *
from Interfaces import *


def main():
    print("Starting...")
    scraper = CVEScraper()
    results = scraper.search("apache2")
    for result in results:
        print(result)

    print("ending...")

if __name__ == "__main__":
    main()
