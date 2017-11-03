import os

import shutil

PYTHON_VERSIONS = [
    '3.7-rc',
    3.6,
    3.5,
    3.4,
    2.7
]

NUMPY_VERSIONS = [
    '1.13.3'
]

def render_travis():
    environments = []

    for python_version in PYTHON_VERSIONS:
        for numpy_version in NUMPY_VERSIONS:
            numpy_short_version = short_version(numpy_version)
            environments.append(
                '    - '
                'PYTHON_VERSION={python_version} '
                'NUMPY_VERSION={numpy_short_version}'.format(
                    **locals()
                )
            )

    with open('.travis.template') as f:
        template = f.read()

    with open('.travis.yml', 'w') as f:
        f.write('# FILE GENERATED AUTOMATICALLY, DO NOT EDIT MANUALLY\n\n')
        f.write(
            template.format(
                environments='\n'.join(
                    environments
                )
            )
        )

def short_version(v):
    return '.'.join(
        v.split('.')[0:2]
    )

def render_dockerfiles():
    try:
        shutil.rmtree('dockerfiles')
    except FileNotFoundError:
        pass

    for python_version in PYTHON_VERSIONS:
        for numpy_version in NUMPY_VERSIONS:
            numpy_short_version = short_version(numpy_version)
            render_dockerfile(**locals())

def render_dockerfile(**kwargs):
    with open('Dockerfile.alpine') as f:
        template = f.read()

    path = 'dockerfiles/{python_version}/{numpy_short_version}'.format(**kwargs)
    os.makedirs(path, exist_ok=True)

    with open('{path}/Dockerfile'.format(**locals(), **kwargs), 'w') as f:
        f.write('# FILE GENERATED AUTOMATICALLY, DO NOT EDIT MANUALLY\n\n')
        f.write(template.format(**kwargs))

def main():
    render_dockerfiles()
    render_travis()

if __name__ == '__main__':
    main()
