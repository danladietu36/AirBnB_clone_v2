#!/usr/bin/python3
from time import strftime
from datetime import date
from fabric.api import local


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    fileName = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(fileName))

        return "versions/web_static_{}.tgz".format(fileName)

    except Exception as e:
        return None
