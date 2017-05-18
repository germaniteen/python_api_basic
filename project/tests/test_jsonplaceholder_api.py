# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from project.services import *


def test_get_all_users():
    # Call the service, which will send a request to the server.
    response = get_all_users()
    
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)

def test_get_user_by_id():
    # Call the service, which will send a request to the server.
    response = get_user_by_id('2')
    
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)

def test_create_new_user():
    # Call the service, which will send a request to the server.
    response = create_new_user()
    
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)