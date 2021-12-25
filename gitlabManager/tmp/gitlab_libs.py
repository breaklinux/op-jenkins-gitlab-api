import gitlab
from tools.config import gitlabToken, gitlaburl
gitLabLogin = gitlab.Gitlab(url=gitlaburl, private_token=gitlabToken)

# 获取所有的project的项目和id
for p in gitLabLogin.projects.list(all=True, as_list=False):
    print(p.name, p.id)

#查找项目
projects = gitLabLogin.projects.list(search='op-cicd-api')
print(projects)


project = gitLabLogin.projects.get(2)
# # 创建一个项目
# project = gitLabLogin.projects.create({'name':'op-cmdb-api'})
# print(project)

branches = project.branches.list()
print(branches)

tags = project.tags.list()
print(tags)

# tag = project.tags.create({'tag_name':'k8s#2021122500111', 'ref':'master'})
# print(tag)

commits = project.commits.list()
for c in commits:
    print(c.author_name, c.message, c.title)
