from InstagramAPI import InstagramAPI

def setup():
    instagram = InstagramAPI('blalala35', 'blabla')
    instagram.login()
    return instagram

instagram = setup()