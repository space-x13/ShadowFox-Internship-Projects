# 1. Web Scraper: Extract data from websites using libraries like
# Beautiful Soup or Scrapy.

# importing libraries to extract and fetch data from websites
import requests
from bs4 import BeautifulSoup

# sending requests to the website
url = "http://books.toscrape.com"

# handling error with response for http status code
try:
    response = requests.get(url)
    response.raise_for_status() # raising an error for bad status code
    print("Website accessed successfully")

except requests.exceptions.HTTPError as http_error:
    # specifying http error
    print(f"HTTP error occured: {http_error}")

except Exception as err:
    # General error
    print(f"An error occured: {err}")

# pasrsing the html content using BeautifulSoup library
soup = BeautifulSoup(response.content, "html.parser")

# extracting all the book
books = soup.find_all('articles', class_='product_pod')

# iteration to find the book titles
for book in books:
    title = book.find('h3').find('a').get('title')
    print(f"Book Title: {title}")

# saving the extracted data to csv file
import csv

# defining it path
csv_file_path = 'books_data.csv'

# defining the header
header = ['Tittle']

# writing to csv file
with open(csv_file_path, mode= 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for book in books:
        title = book.h3.a['Title']
        writer.writerow([title])

print(f"Data has been saved to {csv_file_path}")
