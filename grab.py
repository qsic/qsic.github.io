import os
import re
from urllib.parse import urlparse
import urllib.request


def get_files():
    rootdir = '.'

    for root, subdirs, files in os.walk(rootdir):
        for file_ in files:
            if not file_.endswith('.html'):
                continue
            yield root + '/' + file_


def get_lines():
    files = get_files()
    for file_ in files:
        with open(file_) as fp:
            for line in fp:
                yield line


pat = re.compile(r'"([\S^"]*amazonaws[\S^"]*)"')

def main():
    img_urls = set()
    for line in get_lines():
        match = pat.search(line)
        if match:
            url = match.group(1)
            if url.startswith('//'):
                url = 'http:' + url
            img_urls.add(url)

    for img_url in img_urls:
        print(img_url)
        o = urlparse(img_url)
        img_path = o.path.lstrip('/')
        with urllib.request.urlopen(img_url) as f:
            with open(img_path, 'wb') as fp:
                fp.write(f.read())

main()

