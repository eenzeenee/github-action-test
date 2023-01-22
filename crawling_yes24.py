import requests
from bs4 import BeautifulSoup

def parsing_beautifulsoup(url):
    """
    BeautifulSoup으로 parsing하는 함수
    : param url: parsing할 URL, 여기서는 YES24 한국소설 신간 링크
    : return: BeautifulSoup soup Object
    """
    data = requests.get(url)
    html = data.text
    return BeautifulSoup(html, 'html.parser')

def extract_book_data(soup):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    : pram soup: BeautifulSoup soup Object
    : return: contents(str)
    """

    uploaded_contents = ''
    new_books = soup.select(".goodsTxtInfo")
    url_prefix = 'http://www.yes24.com'

    for new_book in new_books:
        book_name = new_book.select('a')[0].text
        url_suffix = new_book.select('a')[1].attrs['href']
        url = url_prefix + url_suffix
        price = new_book.select('.priceB')[0].text

        content = f'<a href={url}>'+book_name+'</a>'+', '+price+'<br/>\n'
        uploaded_contents += content

    return uploaded_contents