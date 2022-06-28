import pynbody 
import numpy as np

file1 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000016'
file2 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000032'
file3 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000048'
file4 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000064'
file5 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000080'
file6 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000096'
file7 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000112'
file8 = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/DMOnlyCollapse_test1.000128'

a = pynbody.load(file1)
b = pynbody.load(file2)
c = pynbody.load(file3)
d = pynbody.load(file4)
e = pynbody.load(file5)
f = pynbody.load(file6)
g = pynbody.load(file7)
h = pynbody.load(file8)

files = [a, b, c, d, e, f, g, h]

for i in files:
    print(i.stars['pos'])
    print(i.stars['vel'])
else: 
    print("Cool data")



