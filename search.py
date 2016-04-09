import os
import re


def get_files():
    rootdir = '.'

    for root, subdirs, files in os.walk(rootdir):
        for file_ in files:
            if not file_.endswith('.html'):
                continue
            yield root + '/' + file_

string = 'http://qsic-data.s3.amazonaws.com'

def update_file(file_):
    with open(file_) as fp:
        data = fp.read()

    data = data.replace(string, '')

    with open(file_, 'w') as fp:
        fp.writelines(data)


def main():
    files = get_files()
    for file_ in files:
        update_file(file_)

main()

