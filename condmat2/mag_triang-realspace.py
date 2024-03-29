#!/usr/bin/env python3

import numpy as np

from matplotlib import pyplot as plt
## comentar as 4 linhas abaixo caso nao tenha o LaTeX no matplotlib ###
from matplotlib import rc
plt.style.use('bmh')
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{physics} \usepackage{bm}')
#matplotlib.verbose.level = 'debug-annoying'
#######################################################################
#from scipy.integrate import simpson

def main():
    m = 0.4
    Qx, Qy = 2*np.pi/3, 2*np.pi/np.sqrt(3)
    a1x, a1y = 1, 0
    a2x, a2y = 1/2, np.sqrt(3)/2

    M = np.linspace(-5, 7, 13)
    N = np.linspace(-5, 7, 13)
    Rx = M[0] * a1x + N * a2x
    Ry = M[0] * a1y + N * a2y
    m_r = m * np.cos(Qx * Rx + Qy * Ry)
    m_i = m * np.sin(Qx * Rx + Qy * Ry)
    QV = plt.quiver(Rx, Ry, m_r, m_i, color='#A60628', angles='xy', scale_units='xy', scale=1)
    for x in M:
        Rx = x * a1x + N * a2x
        Ry = x * a1y + N * a2y
        m_r = m * np.cos(Qx * Rx + Qy * Ry)
        m_i = m * np.sin(Qx * Rx + Qy * Ry)
        if x != M[0]:
            plt.quiver(Rx, Ry, m_r, m_i, color='#A60628', angles='xy', scale_units='xy', scale=1)
        for y in N:
            Rx = x * a1x + y * a2x
            Ry = x * a1y + y * a2y
            plt.plot([Rx], [Ry], marker='o', linewidth='5', color='#348ABD')
    #plt.quiver([0.5], [0.5], [0], [0.5], color='#A60628', angles='xy', scale_units='xy', scale=1)
    plt.xlabel(r'$x$', fontsize=20)
    plt.ylabel(r'$y$', fontsize=20)
    plt.xlim(-0.6, 5.6)
    plt.ylim(-0.6, 5.6)
    #plt.legend(fontsize=12)
    plt.grid(False)
    plt.title(r'Magnetização $m_j = m e^{i \bm{Q} \vdot \bm{R}_j}$ para a rede triangular')
    plt.savefig("mag_triang-real_space.png", dpi=300, format='png', bbox_inches="tight")
    plt.clf()

# unused code
#plt.savefig("plot.png", dpi=300, format='png', bbox_inches="tight")
#plt.clf()

if __name__ == '__main__':
    main()
