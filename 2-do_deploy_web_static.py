#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
from os import path


env.hosts = ['54.160.88.46', '54.152.234.160']


def do_pack():
    """do_pack function
    """

    datefornow = datetime.now()
    now = datefornow.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))


def do_deploy(archive_path):
    """do_deploy function
    """

    if path.exists(archive_path):
        archive = archive_path.split('/')[1]
        lien = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        lien2 = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, lien)
        run("mkdir -p {}".format(lien2))
        run("tar -xzf {} -C {}".format(lien, lien2))
        run("rm {}".format(lien))
        run("mv -f {}web_static/* {}".format(lien2, lien2))
        run("rm -rf {}web_static".format(lien2))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(lien2))

        return True

    return False

