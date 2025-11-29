# -*- coding: utf-8 -*-
"""
Created on Thu May 29 20:28:49 2025

@author: diya
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import norm

# Parameters for the Binomial distribution
n_trials = 10
p = 0.5
num_samples = 1000
sample_sizes = [5, 10, 30, 100, 500]

# Set up the figure and axis
fig, axes = plt.subplots(len(sample_sizes), 1, figsize=(6, 10), sharex=True)

def animate(frame):
    plt.cla()  # Clear the current figure
    fig.suptitle(f"Central Limit Theorem - Binomial Distribution (Frame: {frame})", fontsize=12)
    for i, sample_size in enumerate(sample_sizes):
        ax = axes[i]
        ax.clear()

        # Generate 'num_samples' sample means, each of 'sample_size' size
        sample_means = [np.mean(np.random.binomial(n_trials, p, sample_size)) for _ in range(num_samples)]

        # Plot histogram
        ax.hist(sample_means, bins=30, density=True, alpha=0.5, color='skyblue')

        # Plot normal distribution
        mu = n_trials * p
        sigma = np.sqrt(n_trials * p * (1 - p) / sample_size)
        x = np.linspace(min(sample_means), max(sample_means), 200)
        ax.plot(x, norm.pdf(x, mu, sigma), 'k')

        ax.set_ylabel("Density")
        ax.text(0.95, 0.8, f"Sample Size: {sample_size}", transform=ax.transAxes, ha='right')

    plt.tight_layout(rect=[0, 0, 1, 0.96])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=200)

plt.show()
