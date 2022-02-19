import requests
from bs4 import BeautifulSoup
import pandas as pd


# in collection_num  soll die aktuelle Gesamtzahl der Kollektion eingegeben werden
def linkcheck(collection_num):

    error_status = []
    error_links = []
    error_linktitle = []
    collection_no = []

    prefix = "https://www.ub.uzh.ch/apps/fachinformationen/de/api/collection/"
    suffix = ".html?version=1.0"

    for i in range(1, collection_num):
        url = prefix + str(i) + suffix
        resp = requests.get(url)

        print("checking the collection no. " + str(i))

        # Für den Fall, wenn eine Kollektion gelöscht ist
        if resp.status_code == 404:
            continue
        soup = BeautifulSoup(resp.text, 'html.parser')

        for a_tag in soup.find_all('a'):
            link = a_tag.get('href')

            # Link sollte schon vorhanden sein, aber hier sollen mögliche Fehler abgedeckt sein
            if link is None:
                error_status.append("No URL")
                error_links.append("no url")
                error_linktitle.append(a_tag.text.strip())
                collection_no.append(str(i))
                continue

            elif link == "#":
                error_status.append("No URL")
                error_links.append("no url")
                error_linktitle.append(a_tag.text.strip())
                collection_no.append(str(i))
                continue

            elif link == "https://":
                error_status.append("Broken url")
                error_links.append(link)
                error_linktitle.append(a_tag.text.strip())
                collection_no.append(str(i))
                continue

            elif "http" not in link:
                error_status.append("Broken url")
                error_links.append(link)
                error_linktitle.append(a_tag.text.strip())
                collection_no.append(str(i))
                continue
            
            # Zum Debuggen 
            # print(link)

            # link wird gecheckt. Ausser dem Status 200 wird der Error verzeichnet
            re = requests.get(link)
            if re.status_code == 200:
                continue
            
            error_status.append(str(re.status_code))
            error_links.append(link)
            error_linktitle.append(a_tag.text.strip())
            collection_no.append(str(i))
    
    if not error_status:
        print("no defect link detected")
    else: 
        print("there are some defect links")
        df = pd.DataFrame(list(zip(error_status, error_links, error_linktitle, collection_no)), columns = ["Error status","URL","Linktitle","Found in Collection"])
        df.to_csv("link_error_log.csv")


if __name__ == "__main__":
    # Momentan (19.Feb. 2022) sind 225 Kollektionnen vorhanden
    linkcheck(225)

