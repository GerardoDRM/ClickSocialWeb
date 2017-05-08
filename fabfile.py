import fabtools
from os.path import join
from contextlib import contextmanager
from datetime import datetime
from fabric.api import (
    env, task, hide, cd, get, put, prefix,
    sudo as _sudo, run as _run, require as _require
)
from fabric.colors import yellow, blue, red
from fabric.contrib.files import exists, append
from fabric.operations import prompt, local as _local
from fabric.utils import puts
from fabtools import require
from fabtools.vagrant import vagrant
import fabtools.supervisor
from fabtools.utils import run_as_root
from fabtools.shorewall import Ping, SSH, hosts, rule


env.use_ssh_config = True
# env.key_filename = "/home/gerardo/.ssh/id_rsa"
env.hosts = [
    '107.20.154.158'
]
env.user = 'mixtli'
env.app_user = 'mixtli'
env.app_group = 'kimetrics'
env.settings = 'datawarehouse'
env.data_site_path = '/home/gerardo/Documents/Business/ClickSocial/ClickSocialWeb'
env.data_site_path_front = '/clicksocial/l'
env.parent = 'origin'
env.branch = 'master'
env.app_port = '5000'
env.git_repo = "git@bitbucket.org:kimetrics/kimetrics-datawarehouse.git"
env.ip = '127.0.0.1'
env.root = '/kimetrics'
env.app_name = 'kimetrics-datawarehouse'
env.cookie_secret = 'kimetrics'
env.app_host = 'data.kimetrics.com'
env.site = "data.kimetrics.com"
env.db_name = 'redash'
env.db_user = 'kimetrics'
env.db_host = 'kliento-backup.cfe7cc4dillv.us-east-1.rds.amazonaws.com'
env.db_pass = 'Kpfp7eLt'


ENV_TPL = '''\
# ClickSocial Data environment setup script
# SECURITY NOTE: this file should be readable

export CLICKSOCIAL_DATA_APP=%(app_name)s
export CLICKSOCIAL_DATA_PORT=%(app_port)s
export CLICKSOCIAL_DATA_COOKIE_SECRET=%(cookie_secret)s
export CLICKSOCIAL_HOST=%(app_host)s
export CLICKSOCIAL_DATA_LOG_LEVEL="INFO"
'''


def _print(output):
    print output


def print_command(command, prompt='$'):
    _print(blue(prompt + " ", bold=True) +
           yellow(command, bold=True) +
           red(" ->", bold=True))


@task
def run(command, show=True, **kwargs):
    """
    Runs a shell comand on the remote server.
    """
    if show:
        print_command(command)
    with hide("running"):
        return _run(command, **kwargs)


@task
def sudo(command, show=True, **kwargs):
    """
    Runs a command as sudo.
    """
    if show:
        print_command(command, prompt='#')
    with hide("running"):
        return _sudo(command, **kwargs)


def runas(command, **kwargs):
    "Run the command as the app_user"
    return sudo(command, user=env.user, group=env.user, **kwargs)

def update_upgrade():
    """
        Update the default OS installation's
        basic default tools.
                                            """
    run("sudo apt-get update")

@task
def setup_mongo():
    """ Download and install mongoDB. """
    sudo('''apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6''')
    run('''echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list''')
    sudo('''sudo apt-get update''')
    sudo('''sudo apt-get install -y mongodb-org''')

@task
def setup_data():
    require.deb.uptodate_index()
    require.deb.packages([
        'build-essential',
        'libffi-dev',
        'libssl-dev',
        'libfreetype6',
        'libfreetype6-dev',
        'libjpeg62',
        'libjpeg62-dev',
        'libjpeg8',
        'libxml2-dev',
        'python3-dev',
        'python3-imaging',
        'python3-setuptools',
        'supervisor',
        'zlib1g-dev',
        'libgeos-c1',
        'libevent-dev',
        'libpq-dev',
        'libboost-dev',
        'libboost-test-dev',
        'libboost-program-options-dev',
        'libboost-filesystem-dev',
        'libboost-thread-dev',
        'libevent-dev',
        'automake',
        'libtool',
        'flex',
        'bison',
        'pkg-config',
        'g++',
        'libssl-dev',
        'libsasl2-dev'
    ])
    setup_mongo()
    require.nginx.server()

@task
def setup_frontend():
    # setup_ssh()
    require.deb.uptodate_index()

    require.deb.package("curl")

    runas("curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -")
    require.deb.package("nodejs")
    # Install frontend dependencies
    with cd(env.data_site_path_front):
        run("npm install")


@task
def deploy_project():
    # Create log directory
    # require.directory(join(env.data_site_path, 'logs'),
    #                   owner=env.user, use_sudo=True)
    #
    #
    # require.files.template_file(env.data_site_path + "/env.sh" % env,
    #                             template_contents=ENV_TPL, context=env,
    #                             owner=env.user, use_sudo=True)

    # Surpervisors
    # require.files.template_file("/etc/supervisor/conf.d/default.conf" % env,
    #                                 template_source="/home/gerardo/Documents/Business/ClickSocial/ClickSocialWeb/setup/ubuntu/files/supervisord.conf",
    #                                 owner=env.user, context=env, use_sudo=True)
    #
    # fabtools.supervisor.update_config()
    # fabtools.supervisor.restart_process("%s:*" % env.app_name)
    # require.nginx.site(env.settings+".mx",
    #                    template_source="setup/ubuntu/files/nginx.conf" % env,
    #                    port=80,
    #                    server_alias=env.app_host,
    #                    docroot=env.data_site_path,
    #                    app_port=env.app_port,
    #                    site_path=env.data_site_path,
    #                    app_name=env.app_name)
