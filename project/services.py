from nap.url import Url
import requests

from project.constants import BASE_URL

class JsonApi(Url):
    def after_request(self, response):
        if response.status_code != 200:
            response.raise_for_status()
        
        return response.json()

api = JsonApi(BASE_URL)


def get_all_users():
    try:
        return(api.get('users'))
    except requests.exceptions.HTTPError as e:
        print('Response was not OK, it was: %s' % e.response.status_code)

def get_user_by_id(id):
    try:
        return(api.get('users?id=' + id))
    except requests.exceptions.HTTPError as e:
        print('Response was not OK, it was: %s' % e.response.status_code)

def create_new_user():
    try:
        return(api.post('users'))
    except requests.exceptions.HTTPError as e:
        print('Response was not OK, it was: %s' % e.response.status_code)
