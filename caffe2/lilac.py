#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
repo_depends = ['confu-git', 'python-peachpy-git', 'python-scikit-image', 'python-lmdb', 'python-leveldb', 'python-glog', 'python-nvd3', 'python-slugify', 'rdma-core']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
