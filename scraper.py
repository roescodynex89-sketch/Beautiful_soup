from bs4 import BeautifulSoup

# 1. Opening the local HTML file in Python
with open("sample.html", "r", encoding="utf-8") as file:
html_content = file.read()

# 2. Parsing the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# 3. Extracting data by targeting various elements

print("--- 1. Extracting the main title using ID ---")
main_title = soup.find(id="main-title").text
print(main_title)
print("\n")


print("--- 2. Extracting the name of the first book (using Tag) ---")
# Finds the first <h2> tag
first_book = soup.find("h2").text
print(first_book)
print("\n")


print("--- 3. Extracting information for all books using a loop ---")
# Finds all <div> elements with the class 'book'
all_books = soup.find_all("div", class_="book")

for book in all_books:
title = book.find("h2", class_="book-title").text
author = book.find("p", class_="author").text
price = book.find("p", class_="price").text

print(f"Book: {title} | {author} | {price}")