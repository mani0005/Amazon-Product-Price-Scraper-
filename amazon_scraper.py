import requests
from bs4 import BeautifulSoup
import csv
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

BASE_URL = "https://www.amazon.in"

def get_product_links(search_url, pages):
    links = []

    for page in range(1, pages + 1):
        url = f"{search_url}&page={page}"
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")

        for item in soup.select("a.a-link-normal.s-no-outline"):
            href = item.get("href")
            if href:
                links.append(BASE_URL + href)

        time.sleep(2)

    return list(set(links))


def get_product_details(product_url):
    response = requests.get(product_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        name = soup.find("span", id="productTitle").get_text(strip=True)
    except:
        name = "Not Available"

    try:
        price = soup.find("span", class_="a-price-whole").get_text(strip=True)
    except:
        price = "Not Available"

    try:
        rating = soup.find("span", class_="a-icon-alt").get_text(strip=True)
    except:
        rating = "Not Available"

    try:
        availability = soup.find("div", id="availability").get_text(strip=True)
    except:
        availability = "Not Available"

    return [name, price, rating, availability]


def scrape_multiple_products(search_url, pages):
    product_links = get_product_links(search_url, pages)

    data = []

    for link in product_links[:10]:  # limit products (ethical)
        details = get_product_details(link)
        data.append(details)
        time.sleep(2)

    with open("amazon_products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Rating", "Availability"])
        writer.writerows(data)

    return data
