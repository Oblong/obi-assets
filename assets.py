'''
Basic template for creating new assets repos.
'''

from __future__ import print_function
from subprocess import call
import errno
import jinja2
import os

def ensure_dir(path):
    '''
    mkdir -p for python
    '''
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def obi_new(**kwargs):
    '''
    obi new assets <project_name>
    '''
    project_name = kwargs['project_name']
    pairs = list([
        [os.path.join("debian", "changelog"), os.path.join("debian", "changelog")],
        [os.path.join("debian", "compat"), os.path.join("debian", "compat")],
        [os.path.join("debian", "control"), os.path.join("debian", "control")],
        [os.path.join("debian", "rules"), os.path.join("debian", "rules")],
        [".gitignore", "gitignore"],
        [".gitattributes", "gitattributes"],
        ["noop.sh", "noop.sh"],
        ["project.yaml", "project.yaml"],
        ["README.md", "README.md"],
        [os.path.join(project_name, ".gitignore"), "gitignore"]
        ])
    env = jinja2.Environment(loader=jinja2.PackageLoader(__name__),
                             keep_trailing_newline=True)
    project_path = kwargs['project_path']
    for file_path, template_name in pairs:
        file_path = os.path.join(project_path, file_path)
        ensure_dir(os.path.dirname(file_path))
        # look for the template in any of the envs
        # break as soon as we find it
        try:
            template = env.get_template(template_name)
            with open(file_path, 'w+') as fil:
                fil.write(template.render(kwargs))
        except jinja2.TemplateNotFound:
            print("Warning: Could not find template {0}".format(template_name))

    os.chmod(project_path + '/noop.sh', 0755)
    # git init
    os.chdir(project_path)
    call(["git", "init"])
    call(["git", "lfs", "install"])
    call(["git", "lfs", "update"])
    call(["git", "add", "--all"])
    call(["git", "commit", "-m", "initial commit from obi template assets"])
    call(["git", "tag", "-am", "dev-0.1", "dev-0.1"])
    return 0
