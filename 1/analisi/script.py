
#%%
import pandas  as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import numpy as np

########################################
from matplotlib import rc
rc("text",usetex=True)
rc('font', family='serif')

def latex_float(f):
    float_str = "{0:.2g}".format(f)
    if "e" in float_str:
        base, exponent = float_str.split("e")
        return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
    else:
        return float_str

def latex_format(x):
    return r"\num{{{0:.2g}}}".format(x)

def latex_format_null(x):
    return r'{0:.2g}'.format(x)

def odg(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    if (float(a)==0):
        return r'0'
    if (float(b)!=0):
        return r'${} \times 10^{{{}}}$'.format(a, b)
    elif (float(b)==0):
        return r'${}$'.format(a)


########################################################

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

table  = sys.argv[1]
table1 = sys.argv[2]
table2 = sys.argv[3]
table3 = sys.argv[4]

fig, ax = plt.subplots(figsize=(8,8))

########################################################

name = table.split("/")[-1]
name = name[:-4]

x_min = None
x_max = None
y_min = None
y_max = None

axis_x = "SigT"
axis_y = "Sig"

if len(sys.argv) > 5:
    x_min = float(sys.argv[5])
    if len(sys.argv) > 6:
        y_min = float(sys.argv[6])
        if len(sys.argv) > 7:
            x_max = float(sys.argv[7])
            if len(sys.argv) > 8:
                y_max = float(sys.argv[8])

print("Tabella inserita : ",table)
print("Nome del grafico generato : ",name)

data = pd.read_table(table,sep=",")
data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

rows_to_drop = []

len_x = len(data[axis_x])
len_y = len(data[axis_y])
same_len = min(len_x,len_y)

for i in range (0,same_len):
    if not isFloat(data[axis_x][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)
    if not isFloat(data[axis_y][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)

rows_to_drop = list(set(rows_to_drop))
rows_to_drop.sort()

data = pd.read_table(table,sep=",",skiprows=rows_to_drop)

data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

x = np.array(data[axis_x], dtype="float64")
y = np.array(data[axis_y],dtype="float64")

#ax.plot(x , y, marker="o", color='gray', linewidth=2, markersize=5, markerfacecolor='red')

#######1

name = table1.split("/")[-1]
name = name[:-4]

x_min = None
x_max = None
y_min = None
y_max = None

axis_x = "SigT"
axis_y = "Sig"

if len(sys.argv) > 5:
    x_min = float(sys.argv[5])
    if len(sys.argv) > 6:
        y_min = float(sys.argv[6])
        if len(sys.argv) > 7:
            x_max = float(sys.argv[7])
            if len(sys.argv) > 8:
                y_max = float(sys.argv[8])

print("Tabella inserita : ",table)
print("Nome del grafico generato : ",name)

data = pd.read_table(table1,sep=",")
data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

rows_to_drop = []

len_x = len(data[axis_x])
len_y = len(data[axis_y])
same_len = min(len_x,len_y)

for i in range (0,same_len):
    if not isFloat(data[axis_x][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)
    if not isFloat(data[axis_y][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)

rows_to_drop = list(set(rows_to_drop))
rows_to_drop.sort()

data = pd.read_table(table1,sep=",",skiprows=rows_to_drop)

data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

x1 = np.array(data[axis_x], dtype="float64")
y1 = np.array(data[axis_y],dtype="float64")

#ax.plot(x , y, marker="o", color='gray', linewidth=2, markersize=5, markerfacecolor='orange')

#########2

name = table2.split("/")[-1]
name = name[:-4]

x_min = None
x_max = None
y_min = None
y_max = None

axis_x = "SigT"
axis_y = "Sig"

if len(sys.argv) > 5:
    x_min = float(sys.argv[5])
    if len(sys.argv) > 6:
        y_min = float(sys.argv[6])
        if len(sys.argv) > 7:
            x_max = float(sys.argv[7])
            if len(sys.argv) > 8:
                y_max = float(sys.argv[8])

print("Tabella inserita : ",table2)
print("Nome del grafico generato : ",name)

data = pd.read_table(table2,sep=",")
data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

rows_to_drop = []

len_x = len(data[axis_x])
len_y = len(data[axis_y])
same_len = min(len_x,len_y)

for i in range (0,same_len):
    if not isFloat(data[axis_x][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)
    if not isFloat(data[axis_y][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)

rows_to_drop = list(set(rows_to_drop))
rows_to_drop.sort()

data = pd.read_table(table2,sep=",",skiprows=rows_to_drop)

data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

x2 = np.array(data[axis_x], dtype="float64")
y2 = np.array(data[axis_y],dtype="float64")

#ax.plot(x , y, marker="o", color='gray', linewidth=2, markersize=5, markerfacecolor='blue')

###########3

name = table3.split("/")[-1]
name = name[:-4]

x_min = None
x_max = None
y_min = None
y_max = None

axis_x = "SigT"
axis_y = "Sig"

if len(sys.argv) > 5:
    x_min = float(sys.argv[5])
    if len(sys.argv) > 6:
        y_min = float(sys.argv[6])
        if len(sys.argv) > 7:
            x_max = float(sys.argv[7])
            if len(sys.argv) > 8:
                y_max = float(sys.argv[8])

print("Tabella inserita : ",table)
print("Nome del grafico generato : ",name)

data = pd.read_table(table3,sep=",")
data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

rows_to_drop = []

len_x = len(data[axis_x])
len_y = len(data[axis_y])
same_len = min(len_x,len_y)

for i in range (0,same_len):
    if not isFloat(data[axis_x][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)
    if not isFloat(data[axis_y][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)

rows_to_drop = list(set(rows_to_drop))
rows_to_drop.sort()

data = pd.read_table(table3,sep=",",skiprows=rows_to_drop)

data.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

x3 = np.array(data[axis_x], dtype="float64")
y3 = np.array(data[axis_y],dtype="float64")

ax.plot(x , y, marker="o", color='red', linewidth=0, markersize=5, markerfacecolor='red',		label='Albume CPMG')
ax.plot(x1 , y1, marker="o", color='orange', linewidth=0, markersize=5, markerfacecolor='orange',	label='Albume IR')
ax.plot(x2 , y2, marker="o", color='green', linewidth=0, markersize=5, markerfacecolor='green',	label='Tuorlo CPMG')
ax.plot(x3 , y3, marker="o", color='blue', linewidth=0, markersize=5, markerfacecolor='blue',		label='Tuorlo IR')

ax.legend()
ax.set_xlim(x_min,x_max)
ax.set_ylim(y_min,y_max)
ax.set_xlabel(axis_x+"(ms)")
ax.set_ylabel(axis_y)

ax.xaxis.set_major_formatter(tkr.FuncFormatter(odg))
ax.yaxis.set_major_formatter(tkr.FuncFormatter(odg))


#fig.savefig(outdir+name)

plt.show(block=True)
