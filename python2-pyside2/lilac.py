#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
repo_depends = ['python2-shiboken2']
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if not line.startswith('groups=('):
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
