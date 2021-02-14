def domain_name(url):
    print(url.split("//")[-1].split("www.")[-1].split(".")[0])

domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")


print('\n') #================================================================================


import re
def domain_name(url):
    print(re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name'))

domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")

