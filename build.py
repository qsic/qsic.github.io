import os
import re


def get_files():
    rootdir = '.'

    for root, subdirs, files in os.walk(rootdir):
        for file_ in files:
            if not file_.endswith('.html'):
                continue
            yield root + '/' + file_


def update_file(file_, top, bottom):
    with open(file_) as fp:
        data = fp.read()

    data = top + data + bottom

    with open(file_, 'w') as fp:
        fp.writelines(data)


def main():
    files = get_files()
    with open('top') as fp:
        top = fp.read()
    with open('bottom') as fp:
        bottom = fp.read()
    for file_ in files:
        update_file(file_, top, bottom)

main()

