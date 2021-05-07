from common.http_interface import *

headers = None
class Services:

    def get_connected(self):
        try:
            url = "https://reqres.in/api/users?page=1"
            response = get_resource(url, headers)
            # print(response)
            return response
        except Exception as e:
            print("unable to get connected through url {}".format(e))

    def get_all_following(self):
        try:
            url = "https://reqres.in/api/users?page=2"
            response = get_resource(url, headers)
            return response
            Logger.log_info("getting all the list of employees")
        except Exception as e:
            Logger.log_error("unable to get the employees {}".format(str(e)))

    def create_data(self,value):
        try:
            value = value
            data = json.dumps(value).encode('utf-8')
            url = 'https://reqres.in/api/users'
            response = create_resource(url=url, headers=headers, data=data)
            Logger.log_info(response.status_code)
            # data = json.dumps(value).encode('utf-8')
            if response.status_code == 201:
                resp = json.dumps(response.json())
                Logger.log_info("posting,updating some information succesfully ")

            return resp
        except Exception as e:
            Logger.log_error("unable to get the response {}".format(str(e)))

s = Services()
print(s.get_all_following())
print(s.get_connected())
print(s.create_data(value={"name": "gopi", "job": "Automation tester"}))