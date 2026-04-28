
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"

def get_genres():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    genres = []
    for li in soup.select('.side_categories ul li ul li'):
        genre_name = li.text.strip()
        genre_url = BASE_URL + li.find('a')['href']
        genres.append({'name': genre_name, 'url': genre_url})
    return genres

def get_books_in_genre(genre_url):
    books = []
    while genre_url:
        response = requests.get(genre_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for article in soup.select('article.product_pod'):
            title = article.h3.a['title']
            book_url = BASE_URL + "catalogue/" + article.h3.a['href'].replace('../../../', '')
            price = article.select_one('.price_color').text
            rating = article.p['class'][1]  # e.g., 'Three'
            books.append({'title': title, 'url': book_url, 'price': price, 'rating': rating})
        next_btn = soup.select_one('li.next a')
        genre_url = BASE_URL + "catalogue/category/books/" + next_btn['href'] if next_btn else None
    return books

def get_book_details(book_url):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    upc = soup.find('th', text='UPC').find_next_sibling('td').text
    stock = soup.find('p', class_='instock availability').text.strip()
    summary = soup.select_one('#product_description ~ p').text.strip()
    return {'upc': upc, 'stock': stock, 'summary': summary}

def rating_to_int(rating_str):
    ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    return ratings.get(rating_str, 0)

def main():
    genres = get_genres()
    print("Available genres:")
    for idx, genre in enumerate(genres):
        print(f"{idx+1}. {genre['name']}")
    choice = int(input("Pick a genre by number: ")) - 1
    genre = genres[choice]
    books = get_books_in_genre(genre['url'])
    books.sort(key=lambda b: rating_to_int(b['rating']), reverse=True)
    print(f"\nBooks in {genre['name']} (best rated first):")
    for idx, book in enumerate(books):
        print(f"{idx+1}. {book['title']} | {book['price']} | {book['rating']} stars")
    book_choice = int(input("Select a book for more details: ")) - 1
    book = books[book_choice]
    details = get_book_details(book['url'])
    print(f"\nTitle: {book['title']}")
    print(f"Price: {book['price']}")
    print(f"Rating: {book['rating']} stars")
    print(f"Stock: {details['stock']}")
    print(f"UPC: {details['upc']}")
    print(f"Summary: {details['summary']}")
    print(f"Buy here: {book['url']}")

if __name__ == "__main__":
    main()
