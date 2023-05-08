#!/usr/bin/python3
"""Module to deploy an archive to servers with Fabric3"""

from fabric import api
from fabric.contrib import files
import os


api.env.hosts = ['34.239.248.111', '54.175.89.17']
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/alx_server'


def do_deploy(archive_path):
    """This  transfers archive_path to web servers.
    Arguments:
        archive_path (str): .tgz file to transfer
    Returns: 1 on success, 0 otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    with api.cd('/tmp'):
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        outpath1 = '/data/web_static/releases/{}'.format(root)
        try:
            putpath1 = api.put(archive_path)
            if files.exists(outpath1):
                api.run('rm -rdf {}'.format(outpath1))
            api.run('mkdir -p {}'.format(outpath1))
            api.run('tar -xzf {} -C {}'.format(putpath1[0], outpath1))
            api.run('rm -f {}'.format(putpath1[0]))
            api.run('mv -u {}/web_static/* {}'.format(outpath1, outpath1))
            api.run('rm -rf {}/web_static'.format(outpath1))
            api.run('rm -rf /data/web_static/current')
            api.run('ln -sf {} /data/web_static/current'.format(outpath1))
            print('New version deployed!')
        except:
            return False
        else:
            return True
