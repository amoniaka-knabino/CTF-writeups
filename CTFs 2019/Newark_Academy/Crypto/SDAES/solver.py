from binascii import unhexlify

def replace_keys_and_values_in_list(orig_list):
    ans = [-1 for i in range(len(orig_list))]
    for i in range(len(orig_list)):
        ans[orig_list[i]] = i
    return ans

def substitute(hexBlock, substitution):
    substitutedHexBlock = ""
    for hexDigit in hexBlock:
        newDigit = substitution[int(hexDigit, 16)]
        substitutedHexBlock += hex(newDigit)[2:]
    return substitutedHexBlock

def permute(hexBlock, permutation):
    block = int(hexBlock, 16)
    permutedBlock = 0
    for i in range(32):
        bit = (block & (1 << i)) >> i
        permutedBlock |= bit << permutation[i]
    return hexpad(hex(permutedBlock)[2:])

def hexpad(hexBlock):
    numZeros = 8 - len(hexBlock)
    return numZeros*"0" + hexBlock

def round(hexMessage, substitution, permutation):
    numBlocks = len(hexMessage)//8
    permutedHexMessage = ""
    for i in range(numBlocks):
        permutedHexMessage += permute(hexMessage[8*i:8*i+8], permutation)
    substitutedHexMessage = ""
    for i in range(numBlocks):
        substitutedHexMessage += substitute(permutedHexMessage[8*i:8*i+8], substitution)
    #print('{} {} {} {} {}'.format(numBlocks, len(substitutedHexMessage), len(permutedHexMessage), substitutedHexMessage, permutedHexMessage))
    return substitutedHexMessage
    
def pad(message):
    numBytes = 4-(len(message)%4)
    return message + numBytes * chr(numBytes)

def main():
    substitution =  [8, 4, 15, 9, 3, 14, 6, 2, 
                13, 1, 7, 5, 12, 10, 11, 0]
    permutation =   [6, 22, 30, 18, 29, 4, 23, 19, 
                15, 1, 31, 11, 28, 14, 25, 2, 
                27, 12, 21, 26, 10, 16, 0, 24,
                    7, 5, 3, 20, 13, 9, 17, 8]
    back_subst = replace_keys_and_values_in_list(substitution)
    bask_perm = replace_keys_and_values_in_list(permutation)

    print(bask_perm, back_subst)

    with open('cipher.txt') as c:
        flag = c.read()
    print(flag)
    for i in range(10000):
        flag = round(flag, back_subst, bask_perm)
        #print(flag)

    flag = unhexlify(flag)
    print(flag)

    flag = flag.decode('ascii')
    #c3 = unpad(c2)
    print(flag)

if __name__ == '__main__':
    main()