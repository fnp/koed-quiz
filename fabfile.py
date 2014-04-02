from fnpdjango.deploy import *


env.project_name = 'koedquiz'

@task
def openquiz():
    env.hosts = ['giewont.icm.edu.pl']
    env.user = 'rczajka'
    env.app_path = '/srv/koedquiz/openquiz'
    env.services = [
        DebianGunicorn('openquiz'),
    ]

@task
def pdquiz():
    env.hosts = ['giewont.icm.edu.pl']
    env.user = 'rczajka'
    env.app_path = '/srv/koedquiz/pdquiz'
    env.services = [
        DebianGunicorn('pdquiz'),
    ]
