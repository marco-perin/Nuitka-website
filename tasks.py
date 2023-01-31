import os
import sys

from invoke import Collection, task

from _docs import doc, intl

# Disable pipenv warning, we run potentially inside the virtualenv already,
# Visual Code e.g. picks it up and there is no harm in that. This is only
# to not confuse people with a pipenv warning that it may not be working.
os.environ["PIPENV_VERBOSITY"] = "-1"


@task
def virtualenv(c):
    '''create and install env'''
    c.run(f'{sys.executable} -m pip install -U pdm')
    c.run(f'{sys.executable} -m pdm install -G doc')
    c.run(f'{sys.executable} -m pdm config python.use_venv false -g')


@task
def run(c, target='build-site'):
    '''
    :target: can be `update-docs`, `build-site`, `serve-site`
    '''
    c.run(f'{sys.executable} -m pdm run python update.py --{target}')


ns = Collection(intl, doc, run, virtualenv)
