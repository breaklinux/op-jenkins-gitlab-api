from tools.config import gitlabToken, gitlaburl
import requests
url = 'http://47.105.48.22/api/v4/projects?private_token=K2rq9kUsPkAS8jtKzh8z&per_page=50'
user_url = "http://47.105.48.22/api/v4/projects/{}/users?private_token=K2rq9kUsPkAS8jtKzh8z&per_page=100"
#http://10.10.10.217/api/v3/projects/45/users?private_token=K2rq9kUsPkAS8jtKzh8z　　#获取项目id为45的信息
#获取项目id和项目名称

def GetProject_id(project_url):
    r = requests.get(project_url)
    data = r.json()
    ProjectId_list = []
    ProjectName_list = []
    for i in data:
        ProjectId_list.append(i['id'])
        ProjectName_list.append(i['name'])
    return ProjectId_list, ProjectName_list

#根据项目id获取项目下的用户信息
def GetProject_userlist():
    IdList = GetProject_id(url)
    project_id = IdList[0]
    project_name = IdList[1]
    for id in project_id:
        l = []
        project_user = requests.get(user_url.format(id))#生成完整的用于显示项目下所有user的连接
        req_data = project_user.json()
        for i in req_data:
            l.append(i['name'])
        print (project_name[project_id.index(id)],l)

GetProject_userlist()