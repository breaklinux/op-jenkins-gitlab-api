"""
@author:lijx
@version: 1.0
"""
from flask import Flask
import os,time,logging

import instanceManager
from tools.config import MysqlConfig
from JenkinsManager.jenkinsApi.view import jenkinsUrl
from appManager.view import appMgUrl
from instanceManager.view import instanceMgUrl
from serviceManage.view import serviceUrl
from flask_cors import CORS
from gitlabManager.view import gitMgUrl


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(MysqlConfig)

    from models import db
    db.init_app(app)
    app.register_blueprint(jenkinsUrl,url_prefix='/jenkins')
    app.register_blueprint(appMgUrl, url_prefix='/app')
    app.register_blueprint(serviceUrl,url_prefix='/service')
    app.register_blueprint(instanceMgUrl, url_prefix='/instance')
    app.register_blueprint(gitMgUrl, url_prefix='/git')
    configure_logger(app)
    return app

def configure_logger(app):
    log_dir_name = "logs"
    log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    log_file_str = log_dir_name + os.sep + log_file_name
    log_level = logging.WARNING
    handler = logging.FileHandler(log_file_str, encoding='UTF-8')
    handler.setLevel(log_level)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
