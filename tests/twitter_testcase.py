from source.twitter.twitter_connect import *
from libCore.assertions import *


#@pytest.fixture
def test_get_connected():
    data = get_connected()

    assert_true('getting connected succesfully')
