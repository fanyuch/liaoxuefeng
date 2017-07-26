# -*- coding : utf-8 -*-

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
    return f

x = None

f1 = count()
x = f1()

pass
#正则表达式
import re
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(2))
#
# re_match = re.match(r'@gmail.com$', 'fanyuchen@gmail.com')
#
# print(re_match)

r = r'\d{3}-\d{3,8}'
text= '010-12565,520-66369, 2520023214-45852,,4474-96adsl 102 ,7'
mRe = re.compile(r)

for x in mRe.findall(text):
    print(x)
pass


from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
