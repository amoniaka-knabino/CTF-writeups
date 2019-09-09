'''
Here we have a message which was encrypted 2 times with the same modulus and different exponent.
Attack: https://gist.github.com/apogiatzis/00b047b6d6570d4e94b4ae00db6fc6e7#file-common_modulus-py
'''
import subprocess
from Crypto.Util import number

flag0 = number.bytes_to_long(open('flag0.enc', 'rb').read())
flag1 = number.bytes_to_long(open('flag1.enc', 'rb').read())

n = 116419190680498712166130179135294003253219676921416438120512111710690221006172514356855288286263972350219787474739935093867343858328823427217475837520092762600151989566463221718583035342933980123524247320312860747904980577343222394742690401968493284643328860324217195081007119112146769642988061747098713581731
e0 = 17
e1 = 65537

command = "python  common_modulus.py  -n " + str(n) + ' -e1 ' + str(e0) + ' -e2 ' + str(e1) + ' -ct1 ' + str(flag0) + ' -ct2 ' + str(flag1)
process = subprocess.Popen(command.split())