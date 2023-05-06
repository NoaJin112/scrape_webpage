from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import urljoin
import urllib.request as urls
import ssl
import sys
from urllib.error import HTTPError as invalid_url

# This is to bypass the SSL certificate error
ssl._create_default_https_context = ssl._create_unverified_context


def search(url):

    while True:
        time.sleep(1)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            start_href = link.get("href")
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
                    try:
                        if href_two.endswith(".xlsx"):
                            xlsx_file_name = link_two["href"]
                            final_url = urljoin(url, xlsx_file_name)
                            print(f"The final download URL: {final_url}\n")
                            filename = final_url.split('/')[-1]
                            urls.urlretrieve(final_url, filename)
                            print(f'{filename} has been downloaded from {final_url}')
                    except AttributeError:#href_two -> none -> empty
                        print('AttributeError, no more hrefs to be found.')
                        sys.exit()
                    except invalid_url:
                        print('Invalid URL, looking for more hrefs......')

search(url="")
