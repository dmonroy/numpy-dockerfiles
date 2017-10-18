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
    '1.13.3',
    '1.12.1',
    '1.11.3',
]


def main():
    with open('Dockerfile.alpine') as f:
        template = f.read()

    try:
        shutil.rmtree('dockerfiles')
    except FileNotFoundError:
        pass

    for python_version in PYTHON_VERSIONS:
        for numpy_version in NUMPY_VERSIONS:
            path = 'dockerfiles/{python_version}/{numpy_version}'.format(**locals())
            os.makedirs(path, exist_ok=True)

            with open('{path}/Dockerfile'.format(**locals()), 'w') as f:
                f.write('# FILE GENERATED AUTOMATICALLY, DO NOT EDIT MANUALLY\n\n')
                f.write(template.format(**locals()))


if __name__ == '__main__':
    main()
