#!/usr/bin/python3
from fabric.api import local
from datetime import date
from time import strftime

def do_pack():
    """ This script generates archive of the content of web_static directory"""

    file_name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
                .format(file_name))
        
        return "versions/web_static_{}.tgz".format(file_name)
