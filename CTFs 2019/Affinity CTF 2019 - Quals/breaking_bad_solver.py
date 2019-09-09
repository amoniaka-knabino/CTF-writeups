from itertools import chain

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)

enc_flag = 'HoRfSbMtInMcLvFlAcAmInMcAmTeErFmInHoLvDbRnMd'

enc_flag_iter = grouper(enc_flag, 2)

enc_flag_list = [''.join(chain(x)) for x in enc_flag_iter]
enc_flag_el = set(enc_flag_list)

dic = {"Ac":  89, "Er":  68, "Rn":  86, "Mc": 115 ,"Lv":  116, "Md":  101, "Fl": 114, "Db": 105 , "Am":  95, "Te": 52 , "Fm":  100, "In": 49 , "Ho":  67, "Rf":  104, "Sb":  51, "Mt":109  }

for x in enc_flag_list:
    print(chr(dic[x]), end='')