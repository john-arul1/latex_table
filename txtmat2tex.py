# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:04:43 2019

@author: A. John Arul, kalpakkam, India
The software is issued without any warranty and free to distribute licence

Generates smiple  latex table from ascii text file containing table in columns and rows.
"""

import numpy as np
import sys

arg=sys.argv[:]
narg=len(arg)
if narg < 2:
    print ("input file name not specified")
    sys.exit(1)


in_file=arg[1]    

fi=open(in_file,"r")
txtmn=fi.readline() 

m,n,tr,align=txtmn.split(',')
align=align.rstrip()
print ("m={:s},n={:s},transpose={:s},algn={:s}".format(m,n,tr,align))

data=fi.readlines()
fi.close()

n=int(n)
m=int(m)
D=np.empty([m,n],dtype=object)

i=0
for line in data:
    values=line.split(',')
    D[i,:]=values
    D[i,n-1]=D[i,n-1].rstrip()
    i+=1
    
    
if tr==1:
    D=D.transpose()

if narg==3:
    out_file=sys.argv[2]
else:    
    out_file="latex_table1.txt"
    
tab=open(out_file,'w')

#preamble
tab.write("\\begin{table}[h]\n\\centering\n\\caption{ }\n\\label{tab:my-table}\n\\begin{tabular}{")
for j in range(n):
    tab.write("|"+align)
tab.write("|}\n")

#body
tab.write("\\hline \n")
for i in range(m):
    for j in range(n-1):
        tab.write("{:s}&".format(D[i,j]))
    tab.write("{:s}\\\ \\hline \n".format(D[i,n-1]))

#closure
tab.write("\\end{tabular}\n\\end{table}\n")

tab.close()

