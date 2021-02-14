from urllib.parse import urlparse


def domain_name(url):
    print(urlparse(url))

domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")


print('\n') #================================================================================


def domain_name(url):
    print(urlparse(url).netloc.split('.')[0])

domain_name("http://google.com")
domain_name("http://google.co.jp")


print('\n') #================================================================================


def domain_name(url):
    print(urlparse(url).netloc.split('.')[0])

domain_name("https://youtube.com")


print('\n') #================================================================================


def domain_name(url):
    if "http" in url:
        print(urlparse(url).netloc.split('.')[0])
    else:
        print(urlparse(url).path.split('.')[1])


domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")
