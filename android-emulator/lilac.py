#!/usr/bin/env python3
from lilaclib import *
import os

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
repo_depends = ['ncurses5-compat-libs']

def pre_build():
    aur_pre_build()
    os.environ['http_proxy'] = '127.0.0.1:8123'
    os.environ['https_proxy'] = '127.0.0.1:8123'

def post_build():
    aur_post_build()
    del os.environ['http_proxy']
    del os.environ['https_proxy']

if __name__ == '__main__':
    single_main(build_prefix)
