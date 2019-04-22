from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()


def download(img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open("1.html", "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(download, "http://www.baidu.com"),
        gevent.spawn(download, "http://www.sina.com")
    ])


if __name__ == '__main__':
    main()
