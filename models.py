"""
@author:lijx
@version: 1.0
"""
# -*- coding: utf-8 -*-
import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
@author:lijx
@version: 1.0
"""
# -*- coding: utf-8 -*-
import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import text


class Cicdmg(db.Model):
    __tablename__ = "cicdmg"
    id = db.Column(db.Integer, primary_key=True)
    env = db.Column(db.String(1024), nullable=False)
    appname = db.Column(db.String(1024), nullable=False)
    appversion = db.Column(db.String(1024), nullable=False)
    branch = db.Column(db.String(1024), nullable=False)
    instance_ip = db.Column(db.Text, nullable=False)
    giturl = db.Column(db.Text, nullable=False)
    language_type = db.Column(db.String(1024), nullable=False)
    release_type = db.Column(db.String(1024), nullable=False)
    release_reason = db.Column(db.Text, nullable=False)
    jenkins_callback = db.Column(db.Text, nullable=False)
    releasetime = db.Column(db.DateTime(timezone=False), default=datetime.datetime.now())

    def to_dict(self):
        return {"id": self.id, "env": self.env, "appname": self.appname, "appversion": self.appversion,
                "branch": self.branch, "instance_ip": self.instance_ip,
                "giturl": self.giturl, "language_type": self.language_type, "release_type": self.release_type,
                "release_reason": self.release_reason, "callback": self.jenkins_callback,
                "releasetime": str(self.releasetime)}


class Appmg(db.Model):  # 父表
    __tablename__ = "appname"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business = db.Column(db.String(256), nullable=False)
    group = db.Column(db.String(1024), nullable=False)
    appname = db.Column(db.String(2048), nullable=False)
    apptype = db.Column(db.String(1024), nullable=False)
    giturl = db.Column(db.Text, nullable=False)
    port = db.Column(db.String(16), nullable=False)
    level = db.Column(db.String(64), nullable=False)
    owner = db.Column(db.String(256), nullable=False)
    used = db.Column(db.Text, nullable=False)
    createtime = db.Column(db.DateTime(timezone=False), default=datetime.datetime.now())

    def to_dict(self):
        return {"id": self.id, "business": self.business, "group": self.group, "appname": self.appname,
                "apptype": self.apptype,
                "giturl": self.giturl, "owner": self.owner, "port": self.port, "level": self.level,
                "used": self.used, "createtime": str(self.createtime)}

    def to_appNameList(self):
        return {"env": self.appname}


class Instancemg(db.Model):  # 从表
    __tablename__ = "instance"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instancename = db.Column(db.String(256), nullable=False)
    appname = db.Column(db.String(2048), nullable=False)
    domain = db.Column(db.String(2048), nullable=False)
    ip = db.Column(db.String(256), nullable=False)
    env = db.Column(db.String(64), nullable=False)
    createtime = db.Column(db.DateTime(timezone=False), default=datetime.datetime.now())

    def to_dict(self):
        return {"id": self.id, "appname": self.appname, "instancename": self.instancename, "domain": self.domain,
                "ip": self.ip, "env": self.env,
                "createtime": str(self.createtime)}

    def to_appname(self):
        return {"appname": self.appname}


class ldapmg(db.Model):  # ldap用户表
    __tablename__ = "ldap"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(2048), nullable=False)
    name = db.Column(db.String(256), nullable=False)
    mail = db.Column(db.String(64), nullable=False)
    createtime = db.Column(db.DateTime(timezone=False), default=datetime.datetime.now())

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password, "name": self.name,
                "mail": self.mail,
                "createtime": str(self.createtime)}


##服务管理日志表记录
class serviceLog(db.Model):
    __tablename__ = 'servicelog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descname = db.Column(db.String(128), nullable=True)  #########模块名称###########
    source = db.Column(db.String(64), nullable=True)  ########ip源地址###########
    channelID = db.Column(db.String(128), nullable=True)  #######授权id#####
    username = db.Column(db.String(64), nullable=True)  ####谁调用#########
    request = db.Column(db.Text, nullable=True)  #######请求参数##########
    response = db.Column(db.Text, nullable=True)  ########返回参数###########
    opsmethod = db.Column(db.String(64), nullable=True)  ########返回方法##########
    run_time = db.Column(db.DateTime(timezone=False), default=datetime.datetime.now())

    def to_dict(self):
        return {"id": self.id, "descname": self.descname, "source": self.source, "channelID": self.channelID,
                "username": self.username,
                "request": self.request, "response": self.response, "opsmethod": self.opsmethod, "run_time":
                    str(self.run_time)}

class Setting(db.Model):
    __tablename__ = "Setting"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(64), unique=True)
    value = db.Column(db.Text, nullable=False)
    desc = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime(timezone=False), default=datetime.datetime.now())
    def to_dict(self):
        return {"id": self.id, "key": self.key, "value": self.value, "desc": self.desc,
                "create_time": str(self.create_time)}
