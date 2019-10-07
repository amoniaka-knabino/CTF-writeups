import re
import md5
from Crypto.Util.number import *

reg = re.compile('^0{1,}e[0-9]+$')
salt = "f789bbc328a3d1a3"

def check(x):
    string = salt + str(x)
    m = md5.new()
    m.update(string)
    ans = m.hexdigest()
    if len(reg.findall(ans)):
        return True
    else:
        return False

for x in range(10**10):
    if check(x):
        print(x)
        break