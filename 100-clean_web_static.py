#!/usr/bin/python3
from fabric.api import *
import os


env.hosts = ['34.239.248.111', '54.175.89.17']


def do_clean(number=0):
    """ Delete oudated archives.
    Arguments:
        number(int): no of archives to keep

     If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives
    """

     number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
