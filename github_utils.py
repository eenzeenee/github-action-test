from github import Github

def get_github_repo(access_token, repository_name):
    """
    github repository를 얻는 함수
    :param access_token: Github access token
    :param repository_name: repository 이름
    :return: repository object
    """

    g = Github(access_token)
    return g.get_user().get_repo(repository_name)

def upload_github_issue(repo, title, body):
    """
    특정 repository에 title 이름으로 issue 생성하고, 내용을 body로 작성하는 함수
    :param repo: repository 이름
    :param title: issue 제목
    :param body: issue에 작성할 내용
    :return: None
    """

    repo.create_issue(title=title, body=body)