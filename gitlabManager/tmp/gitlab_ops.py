import gitlab
import requests
from tools.config import gitlabToken


class gitlabOps():
    def __init__(self, protocol, url):
        self.protocol = protocol
        self.url = url

    def get_gitlab_cli(self,path,methods="get"):
        operatingRange = ["get", "post", "put", "delete"]
        if methods in operatingRange:
            if methods == "get":
                headers = {"PRIVATE-TOKEN": gitlabToken}
                acc_gitlab = requests.get(self.protocol + "://" + self.url + "/api/v4" + path, headers=headers)
                acc_gitlab.close()
                result = acc_gitlab.json()
                return result
            elif methods == "post":
                  pass
            elif  methods == "put":
                pass
            elif methods == "delett":
                pass


        else:
            return "需要操作输入方法,只支持" + operatingRange

    def create_project(self,projectName):
        pass


    @property
    def get_project_lists(self):
        data = self.get_gitlab_cli("/projects")
        return data

    @property
    def get_groups_lists(self):
        data = self.get_gitlab_cli("/groups")
        return data



gl = gitlabOps("http", "47.105.48.22")
project = gl.get_project_lists
print(project)

groups = gl.get_groups_lists
print(groups)
