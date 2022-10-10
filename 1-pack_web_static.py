#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generate a tar archives """
    date_recent = datetime.now().strftime("%Y%m%d%H%M%S")
    path_ruth = "versions/web_static_{}.tgz".format(date_recent)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(path_ruth))
        return path_ruth
    except:
        return None
