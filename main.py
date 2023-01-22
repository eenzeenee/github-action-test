import os
from datetime import datetime
from pytz import timezone
from crawling_yes24 import parsing_beautifulsoup, extract_book_data
from github_utils import get_github_repo, upload_github_issue

if __name__ == '__main__':
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = 'github-action-test'
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seolu_timezone)
    today_date = today.strftime('%Y년 %m월 %d일')

    yes24_kor_fiction_new_product_url = 'http://www.yes24.com/24/Category/NewProductList/001001046001?sumGb=01'

    soup = parsing_beautifulsoup(yes24_kor_fiction_new_product_url)

    issue_title = f"YES24 한국소설 신간 도서 알림 ({today_date})"
    uploaded_contents = extract_book_data(soup)
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, uploaded_contents)
    print('Upload Github Issue Success!!')