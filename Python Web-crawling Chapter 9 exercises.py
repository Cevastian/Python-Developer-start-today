from bs4 import BeautifulSoup

'''
ex1 = """
<html>
    <head>
        <title> HTML Exercise </title>
    </head>
    <body>
        <p align = "center"> text 1 </p>
        <img src = "C:\\Data\\image\\Falcon.jpg">
    </body>
</html> """



fp = open("BS web crawling exercise 001.html", "r")
# print(fp.text)

soup = BeautifulSoup(fp, 'html.parser')
print(soup.find("head"))
print(soup.find('p'))


fp = open("BS web crawling exercise 001.html", "r")

soup = BeautifulSoup(fp, 'html.parser')
print(soup.find('p', align = 'center'))

print(soup.find('p', align = 'right'))

print(soup.find('p', align = 'left'))



fp = open("BS web crawling exercise 001.html", "r")

soup = BeautifulSoup(fp, 'html.parser')

print(soup.find_all('p', 'head'))
 print(soup.find_all(string = ['p', 'head']))

# txt = soup.find('p')
# print(txt)
# print(txt.string)

txt2 = soup.find_all('p')
for i in txt2:
    print(i.string)


fp = open("BS web crawling exercise 001.html", "r")

soup = BeautifulSoup(fp, 'html.parser')

txt3 = soup.find_all('p')
for i in txt3:
    print(i.get_text())

'''

fp = open("HTML example for BS Test.html", "r")

soup = BeautifulSoup(fp, 'html.parser')

# print(soup.select('p'))
# print(soup.select(' .name1'))
# print(soup.select(' div > p > span'))
# print(soup.select(' div > p > span')[2:4])
# print(soup.select('p.name1 > span.store'))
# print(soup.select('#fruits1'))
# print(soup.select('#fruits2 > span.store'))
# print(soup.select('a[href]'))
# print(soup.select('a[href]')[1])
     