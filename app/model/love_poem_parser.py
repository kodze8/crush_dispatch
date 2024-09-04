import requests
from bs4 import BeautifulSoup

url_1 = "https://www.poetryfoundation.org/collections/145134/love-poems"

response = requests.get(url_1)
html_content = response.content
parser = BeautifulSoup(html_content, "html.parser")

with open("../templates/email_layout.html", "w") as f:
    f.write(parser.prettify())

peom_links = []
ul_s = parser.find_all('ul')[23]  # found by counter

for link in ul_s.find_all_next("a", href=True):
    if len(peom_links) > 18:
        break
    peom_links.append(link['href'])
