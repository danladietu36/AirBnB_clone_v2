#!/usr/bin/python3
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['34.239.248.111', '54.175.89.17']


def do_pack():
    """Creates a tar gzip archive of the web_static dir"""
    d_time = datetime.utcnow()
    fileName = "versions/web_static_{}{}{}{}{}{}.tgz".format(d_time.year,
                                                         d_time.month,
                                                         dt.day,
                                                         d_time.hour,
                                                         d_time.minute,
                                                         d_time.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(fileName)).failed is True:
        return None
    return fileName


def do_deploy(archive_path):
    """Distributes archive to web server.
    Arguments:
        archive_path (str): path of archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    fileName = archive_path.split("/")[-1]
    name1 = fileName.split(".")[0]

    if put(archive_path, "/tmp/{}".format(fileName)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name1)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name1)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name1)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name1, name1)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name1)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name1)).failed is True:
        return False
    return True


def deploy():
    """Creates and distribute archive to server."""
    fileName = do_pack()
    if file is None:
        return False
    return do_deploy(fileName)
