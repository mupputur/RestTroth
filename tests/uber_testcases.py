from source.uber.uber_service import Services
from libCore.assertions import *

class TestCases:

    @pytest.fixture()
    def s(self):
        return Services()
    @pytest.mark.skip
    def test_get_connected(self, s):
        data = s.get_connected()
        assert_equal(exp=200, act=data)
        print("true")

    @pytest.mark.skip
    def test_get_all_followings(self, s):
        data = s.get_all_following()
        assert_equal(exp=200, act=data)
        print("true")

    @pytest.mark.skip
    def test_create_data(self,s):
        data = s.create_data(value={"name": "gopi", "job": "Automation tester"})
        assert_equal(exp=201, act=data)
        print("true")


