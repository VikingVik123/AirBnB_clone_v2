#!/usr/bin/python3
"""
Fabric script to zip web static
"""
import os
from datetime import datetime
from fabric import task

@task
def do_pack(c):
    """
    Generates a .tgz file from the contents of the web_static folder.
    """
    dir = "versions"
    if not os.path.exists(dir):
        os.makedirs(dir)

    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    archive_path = os.path.join(dir, archive_name)

    try:
        print(f"Packing web_static to {archive_path}")
        c.local(f"tar -czvf {archive_path} web_static")
        print(f"web_static packed: {archive_path}")
        return archive_path
    except Exception as e:
        print(f"Failed to create archive: {e}")
        return None
