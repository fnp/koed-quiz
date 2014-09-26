from fnpdjango.deploy import *


env.project_name = 'koedquiz'
env.hosts = ['giewont.icm.edu.pl']
env.user = 'rczajka'
env.app_path = '/srv/koedquiz'
env.services = [
    Supervisord('koedquiz'),
    ]

