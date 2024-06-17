import os
import pandas as pd
import matplotlib.pyplot as plt
import pylab
from matplotlib.lines import Line2D

NS3 = "/home/etftk/ns3-datacenter-master/simulator/ns-3.39"
plots_dir = "/home/etftk/ns3-datacenter-master/simulator/ns-3.39/examples/PowerTCP/dump_fairness_promjenatokova8/"

plt.rcParams.update({'font.size': 18})

algs = ["dcqcn", "powerInt", "hpcc", "powerDelay", "timely", "dctcp"]
algnames = {
    "dcqcn": "DCQCN",
    "powerInt": "PowerTCP",
    "hpcc": "HPCC",
    "powerDelay": r'$\theta$-PowerTCP',
    "timely": "TIMELY",
    "dctcp": "DCTCP"
}

######## FAIRNESS #############

results_dir = NS3 + "/examples/PowerTCP/results_fairness_promjenatokova8/"

plt.rcParams.update({'font.size': 24})

figlegend = pylab.figure(figsize=(20.5, 1.5))
legend_elements = []

# Definiranje boja i oznaka za legende
colorsFair = ["#d65151", "#7ab547", "#478fb5", "#8b0000", "#8b4513"]
labels = ['flow-1', 'flow-2', 'flow-3', 'flow-4', 'flow-5']

# Stvaranje legendi za svaki od algoritama
for i in range(len(labels)):
    legend_elements.append(Line2D([0], [0], color=colorsFair[i], lw=6, label=labels[i]))

# Iteriranje kroz sve algoritme i crtanje grafika
for alg in algs:
    
    # Učitavanje podataka iz CSV datoteka za svaki algoritam
    df1 = pd.read_csv(results_dir + 'result-' + alg + '.1', delimiter=' ', usecols=[5, 7], names=["th", "time"])
    df2 = pd.read_csv(results_dir + 'result-' + alg + '.2', delimiter=' ', usecols=[5, 7], names=["th", "time"])
    df3 = pd.read_csv(results_dir + 'result-' + alg + '.3', delimiter=' ', usecols=[5, 7], names=["th", "time"])
    df4 = pd.read_csv(results_dir + 'result-' + alg + '.4', delimiter=' ', usecols=[5, 7], names=["th", "time"])
    
    # Stvaranje novog grafa za svaki algoritam
    fig, ax = plt.subplots(1, 1)
    ax.xaxis.grid(True, ls='--')
    ax.yaxis.grid(True, ls='--')
    
    ax.set_ylabel("Throughput (Gbps)")
    ax.set_xlabel("Time (s)")
    
    # Postavljanje granica x-osi
    ax.set_xlim(0, 0.7)
    
    # Crtanje linija za svaki od DataFrame-ova
    ax.plot(df1["time"].values, df1["th"].values / 1e9, c=colorsFair[0])
    ax.plot(df2["time"].values, df2["th"].values / 1e9, c=colorsFair[1])
    ax.plot(df3["time"].values, df3["th"].values / 1e9, c=colorsFair[2])
    ax.plot(df4["time"].values, df4["th"].values / 1e9, c=colorsFair[3])
    
    # Spremanje grafova kao PDF i PNG datoteka
    fig.tight_layout()
    fig.savefig(plots_dir + 'fairness/' + alg + '.pdf')
    fig.savefig(plots_dir + 'fairness/' + alg + '.png')

# Postavljanje legende
figlegend.tight_layout()
figlegend.legend(handles=legend_elements, loc=9, ncol=5, framealpha=0, fontsize=48)
figlegend.savefig(plots_dir + '/fairness/fair-legend.pdf')

