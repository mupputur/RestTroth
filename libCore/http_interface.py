import urllib.request
import json

class Http:

    def create_resource(self,method="POST",**kwargs):
        """
            :param url:
            :param headers:
            :param data:
            :param method:
            :return:
        """
        url = kwargs.get("url")
        headers = kwargs.get("headers")
        data = kwargs.get("data")
        print("{} {} {}".format(url, headers, data))
        try:
            res = urllib.request.Request(url, headers=headers, data=data, method=method)
            with urllib.request.urlopen(res) as resp:
                print("posting,updating some information succesfully ")
                print(resp.status)
                return resp
        except Exception as e:
            print("unable to post,update the response {}".format(str(e)))
            raise Exception(str(e))

    def get_resource(self,url,headers):
        """
        :param url: enter the url that access to the api to get the info
        :param headers: giving authorization to the access the account
        :return:it will return the information of the page that we are accessing
        """
        try:
            req = urllib.request.Request(url, headers=headers, method="GET")
            response = urllib.request.urlopen(req)
            print(response.code)
            if response.code == 200:
                response = json.loads(response.read().decode("utf-8"))
                print("sucessfully getting data from response")
                return response
        except Exception as e:
            print("unable to get the response {}".format(str(e)))

    def delete_resourse(self,url,headers):
        try:
            res = urllib.request.Request(url, headers=headers, method="DELETE")
            with urllib.request.urlopen(res) as resp:
                print("{} - sucessfully deleting resource from given data: {}".format("DELETE", resp))

                print(resp.read().decode('utf-8'))
                print(dir(resp))
                print(resp.status)
                if resp.status == 204:
                    return True
        except Exception as e:
            print(f"failed to delete the repo {str(e)}")
if __name__=="__main__":
    a=Http()
    a.get_resource()