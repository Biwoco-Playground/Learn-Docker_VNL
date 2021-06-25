import sys
import unicodedata

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s,'\n'+'-'*20)
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None
}
a = s.translate(remap)
print(a)

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD',a)
print(b)
b.translate(cmb_chrs)
print('-'*20+'\n',b.translate(cmb_chrs))