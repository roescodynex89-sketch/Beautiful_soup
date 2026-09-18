import requests
from bs4 import BeautifulSoup
import csv
import json


# ==========================================
# STEP 16 + 17
# Requests + BeautifulSoup
# Website HTML/XML 
# ==========================================

URL = "https://feeds.bbci.co.uk/news/rss.xml"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=10)

print("Status:", response.status_code)

response.raise_for_status()

soup = BeautifulSoup(response.content, "xml")


# ==========================================
# STEP 18
# Article scraping
# ==========================================

articles = soup.find_all("item")

print("Total articles:", len(articles))


data = []


for article in articles:

    # Title
    title_tag = article.find("title")
    title = title_tag.get_text(strip=True) if title_tag else None

    # Link
    link_tag = article.find("link")
    link = link_tag.get_text(strip=True) if link_tag else None

    # Description
    description_tag = article.find("description")
    description = (
        description_tag.get_text(strip=True)
        if description_tag
        else None
    )

    # Published date
    date_tag = article.find("pubDate")
    published_at = (
        date_tag.get_text(strip=True)
        if date_tag
        else None
    )


    # ==========================================
    # STEP 21
    # Dictionary 
    # ==========================================

    article_data = {
        "title": title,
        "link": link,
        "description": description,
        "published_at": published_at
    }

    data.append(article_data)


# ==========================================
# Output
# ==========================================

for article in data:

    print("\n-------------------------")

    print("Title:", article["title"])
    print("Link:", article["link"])
    print("Description:", article["description"])
    print("Published:", article["published_at"])


# ==========================================
# STEP 22
# JSON Save
# ==========================================

with open(
    "bbc_news.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        ensure_ascii=False,
        indent=4
    )


# ==========================================
# STEP 22
# CSV Save
# ==========================================

with open(
    "bbc_news.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "title",
        "link",
        "description",
        "published_at"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(data)


print("\nData saved successfully!")
print("bbc_news.json")
print("bbc_news.csv")