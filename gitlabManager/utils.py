# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.

#from tools.config import REPOS_DIR
from gitlabManager.libs.git_ops import Git
import shutil
import os
from models import Setting

REPOS_DIR = "E:/python/op-cicd-api/"
# def parse_envs(text):
#     data = {}
#     if text:
#         for line in text.split('\n'):
#             fields = line.split('=',1)
#             if len(fields) != 2 or fields[0].strip() == '':
#                 raise Exception(f'解析自定义全局变量{line!r}失败，确认其遵循 key = value 格式')
#             data[fields[0].strip()] = fields[1].strip()
#     return data


def get_default(key, default=None):
    info = Setting.query.filter_by(key=key).first()
    if not info:
        return default
    return info.value


def fetch_versions():
    git_repo = "git@47.105.48.22:op/op-cicd-api.git"
    repo_dir = os.path.join(REPOS_DIR, str(1))
    pkey = get_default('private_key')
    with Git(git_repo, repo_dir, pkey) as git:
        return git.fetch_branches_tags()


def fetch_repo(git_repo):
    repo_dir = os.path.join(REPOS_DIR, str(1))
    pkey = get_default('private_key')
    with Git(git_repo, repo_dir, pkey) as git:
        return git.fetch_branches_tags()

def remove_repo():
    shutil.rmtree(os.path.join(REPOS_DIR, str(1)), True)

