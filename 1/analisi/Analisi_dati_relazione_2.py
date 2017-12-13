
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

table_1 = "C:\\Users\\carli\\Dropbox\\UNIVERSITY!\\Fisica applicata alla medicina\\RELAZIONI\\PRIMA PROVA\\Dall'Olio_Montanari\\ALBUME\\CPMG\\CPMGalbume1M.dat"

table_2 = "C:\\Users\\carli\\Dropbox\\UNIVERSITY!\\Fisica applicata alla medicina\\RELAZIONI\\PRIMA PROVA\\Dall'Olio_Montanari\\TUORLO\\CPMG\\CPMGtuorlo1M.dat"


name = "T_tuorlo_merge"


axis_x = "T"
axis_y = "PctNp"
outdir = "C:\\Users\\carli\\Dropbox\\UNIVERSITY!\\Fisica applicata alla medicina\\RELAZIONI\\Relazioni_FAM"


fig, ax = plt.subplots(figsize=(8,8))

data_1 = pd.read_table(table_1,sep=",")
data_1.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

rows_to_drop = []

len_x = len(data_1[axis_x])
len_y = len(data_1[axis_y])
same_len = min(len_x,len_y)

for i in range (0,same_len):
    if not isFloat(data_1[axis_x][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)
    if not isFloat(data_1[axis_y][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)

rows_to_drop = list(set(rows_to_drop))
rows_to_drop.sort()

data_1 = pd.read_table(table_1,sep=",",skiprows=rows_to_drop)

data_1.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

x_1 = np.array(data_1[axis_x], dtype="float64")
y_1 = np.array(data_1[axis_y],dtype="float64")

data_2 = pd.read_table(table_2,sep=",")
data_2.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

rows_to_drop = []

len_x = len(data_2[axis_x])
len_y = len(data_2[axis_y])
same_len = min(len_x,len_y)

for i in range (0,same_len):
    if not isFloat(data_2[axis_x][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)
    if not isFloat(data_2[axis_y][i]):
        index_to_drop = i+1
        rows_to_drop.append(index_to_drop)

rows_to_drop = list(set(rows_to_drop))
rows_to_drop.sort()

data_2 = pd.read_table(table_2,sep=",",skiprows=rows_to_drop)

data_2.columns = ['T','SigNp','Rate#','PctNp','CumPct','SigT','E:SNR0129','Sig','SigCalc','Range','Zero']

x_2 = np.array(data_2[axis_x], dtype="float64")
y_2 = np.array(data_2[axis_y],dtype="float64")

ax.plot(x_1 , y_1, marker="o", color='green', linewidth=2, markersize=5, markerfacecolor='black', label="$T_2 Albume$")
ax.plot(x_2 , y_2, marker="o", color='yellow', linewidth=2, markersize=5, markerfacecolor='orange', label="$T_2 Tuorlo$")
ax.set_xlim(0,750)
ax.set_ylim(0)
ax.set_xlabel(axis_x+"(ms)")
ax.set_ylabel("Densita' di Segnale Normalizzato(a.u.)")

ax.legend(loc='best')
ax.set_title("$T_2$ di albume e tuorlo a confronto")
ax.xaxis.set_major_formatter(tkr.FuncFormatter(odg))
ax.yaxis.set_major_formatter(tkr.FuncFormatter(odg))


fig.savefig(outdir+name)

plt.show(block=True)
