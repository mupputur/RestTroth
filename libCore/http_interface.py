import urllib.request
import json
from libCore.log_provider import Logger

def create_resource(method="POST",**kwargs):
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
    Logger.log_info("{} {} {}".format(url, headers, data))
    try:
        res = urllib.request.Request(url, headers=headers, data=data, method=method)
        with urllib.request.urlopen(res) as resp:
            Logger.log_info("posting,updating some information succesfully ")
            Logger.log_info(resp.status)
            return resp
    except Exception as e:
        Logger.log_error("unable to post,update the response {}".format(str(e)))
        raise Exception(str(e))

def get_resource(url,headers):
    """
    :param url: enter the url that access to the api to get the info
    :param headers: giving authorization to the access the account
    :return:it will return the information of the page that we are accessing
    """
    try:
        req = urllib.request.Request(url, headers=headers, method="GET")
        response = urllib.request.urlopen(req)
        Logger.log_info(response.code)
        if response.code == 200:
            response = json.loads(response.read().decode("utf-8"))
            Logger.log_info("sucessfully getting data from response")
            return response
    except Exception as e:
        Logger.log_error("unable to get the response {}".format(str(e)))

def delete_resourse(url,headers):
    try:
        res = urllib.request.Request(url, headers=headers, method="DELETE")
        with urllib.request.urlopen(res) as resp:
            Logger.log_info("{} - sucessfully deleting resource from given data: {}".format("DELETE", resp))

            Logger.log_info(resp.read().decode('utf-8'))
            Logger.log_info(dir(resp))
            Logger.log_info(resp.status)
            if resp.status == 204:
                return True
    except Exception as e:
        Logger.log_error(f"failed to delete the repo {str(e)}")
