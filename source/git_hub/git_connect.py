#  Dont import urllib here
import json
import os
from libCore.http_interface import Http

#with open('G:\\RestAPIFramework\\Config\\user_info.json') as f:
#  data = json.load(f)
  #print(data["User2"]['_access_token'])
  #print(data['User2']['_owner'])

#_owner = "chennakesava89"
#_access_token = '3e5dc90644462b8f596ff60ba4de8b19afbd391f'

class Connect:

    def __init__(self):
        self.h =Http()
        self.data = self.get_auth_from_config()
        self.g_headers = {'Authorization': "Token " + self.data["User3"]['_access_token'] ,
                     'Content-Type': "application/json"}
        self.get_auth_from_config()

    def get_auth_from_config(self):
        try:
            path = "../../Config/user_info.json"
            if os.path.exists(path):
                with open(path) as f:
                    data = json.load(f)
                    print("file exists")
            else:
                raise Exception("FILE NOT FOUND")
            return data
        except Exception as e:
            print("unable to find the path {}".format(str(e)))

    def get_all_repos(self):
        try:
            url = f"https://api.github.com/users/{self.data['User3']['_owner']}/repos"
            response = self.h.get_resource(url, self.g_headers)
            print(response)
            repos = [dict_repo["name"] for dict_repo in response]
            print("getting all repos as expected ")
            #return repos
            print(repos)
            return True
        except Exception as e:
            print("unable to get the repos {}".format(str(e)))

    def is_repo_name_exist(self, repo_name):
        try:
            repos = self.get_all_repos()
            #print(repos)
            if repo_name in repos:
                print("repo name is existed in the response")
                return True
            else:
                print("repo name doesn't exist in the list")
                return False
        except Exception as e:
            print("unable to locate the repo name from existing response{}".format(str(e)))

    def get_all_collaborators(self):
        try:
            url = f"https://api.github.com/repos/{self.data['User3']['_owner']}/MOBILE/collaborators"
            response = self.h.get_resource(url, self.g_headers)
            #print(response)
            repos = [dict_repo["login"] for dict_repo in response]
            print("getting all collabortors form the given repo");
            print(repos)
            return True

        except Exception as e:
            print("unable to get the collaborators{}".format(str(e)))


    def add_collaborator(self, repo, user):
        try:
            url = f"https://api.github.com/repos/{self.data['User3']['_owner']}/{repo}/collaborators/{user}"
            response = self.h.create_resource(url=url, headers=self.g_headers, method="PUT")
            print("requested succesfully to add a collaborator");
            return response.code
        except Exception as e:
            print("getting issues to add a collaborator{}".format(str(e)))

    def delete_repo(self, repo_name):
        try:
            data = json.dumps(repo_name).encode('utf-8')
            url = f"https://api.github.com/repos/{self.data['User3']['_owner']}/{repo_name}"
            response = self.h.delete_resourse(url, self.g_headers)
            print("sucessfully deleting a repo ")
            return response.code
        except Exception as e:
            print("unable to delete the repo{}".format(str(e)))

    def create_repo(self, value):
        try:
            value = value
            data = json.dumps(value).encode('utf-8')
            print(data)
            url = f"https://api.github.com/user/repos"
            #response = self.h.create_resource(url=url, headers=self.g_headers, data=self.data)
            response=self.h.create_resource(url=url, headers=self.g_headers,data=data)

            print("creating a repository succesfully")
            return response.code
        except Exception as e:
            raise Exception("Not able to create a repo{}".format(str(e)))


if __name__ == "__main__":
    c = Connect()
    #c.get_all_repos()
    #print(c.is_repo_name_exist("MOBILE"))
    #c.add_collaborator("MOBILE","mupputur")
    #print(c.get_all_collaborators())
    #c.create_repo(value={"name":"Windows"})
    #print(c.delete_repo("Windows"))


