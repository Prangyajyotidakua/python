mystr = "hi my name is prangya jyoti dakua "
words = mystr.split()
words.sort()
for word in words:
    print(word)

"""
dakua
hi
is
jyoti
my
name
prangya
"""
mystr2 = "hi my name is prangya jyoti dakua "

print(sorted(mystr2))
"""
' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a'
, 'a', 'a', 'd', 'e', 'g', 'h', 'i',
 'i', 'i', 'j', 'k', 'm', 'm', 'n',
   'n', 'o', 'p', 'r', 's', 't', 'u',
     'y', 'y', 'y']"""
