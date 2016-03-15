# encoding=utf-8
__author__ = 'm4tuu'
import os
import re
import time

from fabric.api import env, local, cd, abort, sudo, get, put, task, runs_once, run
from fabric.colors import green, red
from fabric.contrib.console import confirm
from fabric.contrib.project import rsync_project

env.hosts = ["tecnica.apps.zille.com.ar:5000"]
env.user = 'webapps'
env.key_filename = '/home/matuu/.ssh/id_rsa'



# remote paths
code_dir = "/home/webapps/zweb/zweb"
proj_dir = code_dir  # os.path.join(code_dir, ".")
remote_media = os.path.join(proj_dir, "media")

# local
virtualenv_dir = "/home/webapps/zweb"
virtualenv_name = "zweb"
local_media = os.path.join(os.path.abspath(os.path.dirname(__file__)), "media")

# directorio local para backups
backup_dir = "bkp-dbs"

def run_cmd_env(command):
    """
    Ejecuta un comando con el ve activado
    """
    # Con virtualenv
    run("source %(ve_dir)s/bin/activate; cd %(ve_dir)s/zweb/z_web/;%(cmd)s" % {
       've_dir': virtualenv_dir,
       'cmd': command,
    })


@task
def run_backup():
    """
    Realiza un backup de la base de datos y la almacena localmente.
    """
    host = re.search("([\w.-]+)[:]?", env.host).group()
    date = time.strftime('%Y%m%d%H%M%S')
    fname = 'zweb-backup-%(date)s.gz' % {'date': date}
    green("Ingrese la contraseña de la clave privada local.")
    sudo("mysqldump -u zilledb -pz1i2l3l4e5 zilleprojects | gzip > /tmp/%s" % fname, user="webapps")
    get("/tmp/%s" % fname, os.path.join(backup_dir, fname))
    sudo("rm /tmp/%s" % fname, user="webapps")


@task
def deploy(backup=False):
    """
    Deploy to the selected servers, arguments: test, backup
    """
    if not confirm(green("¿Seguro que querés deployear?")):
        abort(red("Abortado por el usuario."))

    current_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
    if current_branch != 'master':
        abort(red("Abortado, no estás en el branch master."))

    if backup:
        green("Realizando backup de la base de datos y descargando copia.")
        run_backup()

    with cd(code_dir):
        green("Actualizando codigo")
        run("git pull")
        green("Actualizando dependencias")
        run_cmd_env("pip --exists-action b install -r ../requirements/production.txt")
    with cd(proj_dir):
        run_cmd_env("python manage.py migrate")
        run_cmd_env("python manage.py bower_install")
        sudo("sudo supervisorctl reread")
        sudo("sudo supervisorctl update")
        sudo("sudo supervisorctl restart zweb")
        sudo("service nginx restart")
        run_cmd_env("python manage.py collectstatic --noinput")
