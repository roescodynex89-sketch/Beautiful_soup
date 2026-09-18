from bs4 import BeautifulSoup


# 1. Opening the local HTML file in Python
with open("sample_2.html", "r", encoding="utf-8") as file:
 html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

product = soup.find("div", class_="product")

title = product.find("h2").get_text(strip=True)

price = product.find(
    "p",
    class_="price"
).get_text(strip=True)

image = product.find("img").get("src")

link = product.find("a").get("href")

print("Title:", title)
print("Price:", price)
print("Image:", image)
print("Link:", link)