#!/usr/bin/python3
"""Module to compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['34.239.248.111', '54.175.89.17']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
        """Deploys  files to server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # upload archive to servers
                put(archive_path, '/tmp/')

                # creates target direcory
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                # delete the .tgz file and uncomprees archive
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                # code to remove the archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # code to remove erroneous directory
                 run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                 # code to delete pre-existing symbilic link
                  run('sudo rm -rf /data/web_static/current')

                  # code to re-establish symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        return True
