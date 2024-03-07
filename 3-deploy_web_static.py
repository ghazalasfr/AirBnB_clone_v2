#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
from os import path


env.hosts = ['54.160.88.46', '54.152.234.160']


@runs_once
def do_pack():
    """Generates a .tgz
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(now)

    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(path))
    return path


def do_deploy(archive_path):
    """do_deploy
    """

    if path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))

        return True

    return False


def deploy():
    """Creates deploy
    """

    archive = do_pack()
    return do_deploy(archive)
