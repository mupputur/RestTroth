from source.git_hub.git_connect import Connect
from libCore.assertions import *

class TestCases:

    @pytest.fixture()
    def c(self):
        return Connect()

    def test_repo_exists(self, c):
        resp = c.is_repo_name_exist('chenna')
        assert_true(resp == True, "getting repo name exists")
        print("true")

    @pytest.mark.skip
    def test_create_repo(self, c):
        data = c.create_repo(value={"name": "harry19"})
        assert_equal(exp=201, act=data)
        print("true")

    @pytest.mark.skip
    def test_deleate_repo(self, c):
        c.deleate_repo('harry22')
        resp = c.is_repo_name_exist('harry22')
        assert_false(resp, "deleting and checking the repo")
        print("true")

    @pytest.mark.skip
    def test_get_collaborators(self, c):
        expeced = ['chennakesava89']
        data = c.get_all_collaborators()
        assert_true(data == expeced, "getting collaborators as expected")
        print("true")

    @pytest.mark.skip
    def test_add_collaborators(self, c):
        data = c.add_collaborator('chenna', 'harry22')
        assert_equal(exp=201, act=data)
        print("true")
