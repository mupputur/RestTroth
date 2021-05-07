from common.http_interface import *

headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIM0KgEAAAAAwHcFGS8WYq1cY2TWkBeJ2wOLRVc'
                            '%3DBJuLWVBrRqzZC7Q0ub9O2sD881xAxHYq4bHxh41KKJl5OPvBR1'}

def get_connected():
    try:
        url = "https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=Sriahari2&skip_status=true" \
              "&include_user_entities=false "
        response = get_resource(url, headers)
        return response
    except Exception as e:
        print("unable to get connected through url {} ".format(e))


def get_all_following():
    try:
        s = []
        url = "https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=Sriahari2&skip_status=true" \
              "&include_user_entities=false "
        response = get_resource(url, headers)
        users = response["users"]
        #print(users)
        for user in users:
            s.append(user["name"])
        return s
        Logger.log_info("getting all friends list")
    except Exception as e:
        Logger.log_error("unable to get the friends {}".format(str(e)))

#print(get_all_following())
print(get_connected())


