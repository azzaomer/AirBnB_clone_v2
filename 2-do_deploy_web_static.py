#!/usr/bin/python3
# fabric script to distribute an archive to web servers
'''
fabric script to distribute an archive to web servers
----NEEDS TO REVISIT SCRIPT
'''

from fabric.api import put, run, env
from os.path import exists


env.hosts = ['35.174.184.17', '54.164.112.145']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name  = archive_path.split("/")[-1]
        split_file = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, split_file))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, split_file))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, split_file))
        run('rm -rf {}{}/web_static'.format(path, split_file))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, split_file))
        return True
    except:
        return False