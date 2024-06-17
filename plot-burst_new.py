#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 06:46:30 2021

@author: vamsi
"""
import os
import requests
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import pylab
from matplotlib.lines import Line2D 


NS3="/home/etftk/ns3-datacenter-master/simulator/ns-3.39/"
plots_dir="/home/etftk/ns3-datacenter-master/simulator/ns-3.39/examples/PowerTCP/dump_burst_scenarij3/"
results=NS3+"examples/PowerTCP/results_burst_scenarij3/"

# plots_dir="/home/vamsi/Powertcp-NSDI/"
plt.rcParams.update({'font.size': 18})
#plt.rcParams['agg.path.chunksize'] = 10000
#plt.rcParams['path.simplify_threshold'] = 0.05


algs = ["dcqcn", "powerInt", "hpcc", "powerDelay", "timely", "dctcp"]
algnames = {
    "dcqcn": "DCQCN",
    "powerInt": "PowerTCP",
    "hpcc": "HPCC",
    "powerDelay": r'$\theta$-PowerTCP',
    "timely": "TIMELY",
    "dctcp": "DCTCP"
}

colorsBurst = ["#1979a9", "red", "#478fb5", "tab:brown", "tab:gray"]
labels = ['Throughput', 'Qlen']
legend_elements = [Line2D([0], [0], color=color, lw=6, label=label) for color, label in zip(colorsBurst, labels)]

plt.rcParams.update({'font.size': 22})

for alg in algs:
    
    df = pd.read_csv(results + 'result-' + alg + '.burst', delimiter=' ', usecols=[5, 9, 11, 13], names=["th", "qlen", "time", "power"])

    fig, ax = plt.subplots(1, 1)
    ax.xaxis.grid(True, ls='--')
    ax.yaxis.grid(True, ls='--')
    ax1 = ax.twinx()
    ax.set_yticks([10e9, 25e9, 40e9, 80e9, 100e9])
    ax.set_yticklabels(["10", "25", "40", "80", "100"])
    ax.set_ylabel("Throughput (Gbps)")
    
    start = 0.15
    xtics = [i * 0.001 + start for i in range(0, 6)]
    ax.set_xticks(xtics)
    xticklabels = [str(i) for i in range(0, 6)]
    ax.set_xticklabels(xticklabels)
    
    ax.set_xlabel("Time (ms)")
    ax.set_xlim(0.1495, 0.154)
    ax.plot(df["time"].values, df["th"].values, label="Throughput", c='#1979a9', lw=2)
    ax1.set_ylim(0, 600)
    ax1.set_ylabel("Queue length (KB)")
    ax1.plot(df["time"].values, df["qlen"].values / (1000), c='r', label="Qlen", lw=2)

    fig.tight_layout()    
    fig.savefig(plots_dir + 'burst/' + alg + '.pdf')
    fig.savefig(plots_dir + 'burst/' + alg + '.png')

    fig1, ax2 = plt.subplots(1, 1)
    ax2.xaxis.grid(True, ls='--')
    ax2.yaxis.grid(True, ls='--')
    ax3 = ax2.twinx()
    ax2.set_yticks([10e9, 25e9, 40e9, 80e9, 100e9])
    ax2.set_yticklabels(["10", "25", "40", "80", "100"])
    ax2.set_ylabel("Throughput (Gbps)")
    
    start = 0.15
    xtics = [i * 0.001 + start for i in range(0, 6)]
    ax2.set_xticks(xtics)
    xticklabels = [str(i) for i in range(0, 6)]
    ax2.set_xticklabels(xticklabels)
    ax2.set_xlabel("Time (ms)")
    ax2.set_xlim(0.1495, 0.154)
    ax2.plot(df["time"].values, df["th"].values, label="Throughput", c='#1979a9', lw=2)
    ax3.set_ylabel("Normalized Power")
    ax3.set_ylim(0, 2)
    ax3.plot(df["time"].values, df["power"].values, c='g', label="NormPower", lw=2)
    fig1.tight_layout()
    fig1.savefig(plots_dir + 'burst/' + alg + '-power.pdf')
    fig1.savefig(plots_dir + 'burst/' + alg + '-power.png')


figlegend = pylab.figure(figsize=(11.5, 1.5))
figlegend.legend(handles=legend_elements, loc=9, ncol=2, framealpha=0, fontsize=48)
figlegend.tight_layout()
# figlegend.savefig(plots_dir + '/burst/burst-legend.pdf')

