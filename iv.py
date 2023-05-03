from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import urljoin


def search(url):
    while True:
        time.sleep(1)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            start_href = link.get("href")
            print(f"test: {start_href}")
            if start_href.endswith(".xlsx") or start_href.endswith(".xls"):
                print(f"Sussy links: {start_href}\n")


        for link in soup.find_all("a"):
            href = link.get("href")
            full_url = urljoin(url, href)
            time.sleep(1)
            response_one = requests.get(full_url)
            soup_one = BeautifulSoup(response_one.text, "html.parser")

            for link_one in soup_one.find_all("a"):
                href_one = link_one.get("href")
                full_url = urljoin(url, href_one)
                print(f"Pre-URL -> Indirect link to the xlsx file: {full_url}\n")
                time.sleep(1)
                response_two = requests.get(full_url)
                soup_two = BeautifulSoup(response_two.text, "html.parser")
                    
                for link_two in soup_two.find_all("a"):
                    href_two = link_two.get("href")
                    if href_two.endswith(".xlsx"):
                        xlsx_file_name = link_two["href"]
                        final_url = urljoin(url, xlsx_file_name)
                        print(f"The final download URL: {final_url}\n")
                    

search(url="https://hotelkamer.abunaicon.nl")
# search(url="https://www.excelvoorbeelden.nl")
# search(url='https://www.excelvoorbeelden.nl/download/maandkalender-2023')