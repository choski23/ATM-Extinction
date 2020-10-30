{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "small = ('ATM per 100,000 by GDP Quantile 2008-2019', (1, 3, 1), x0, y0, 'Year', 'ATM per 100k', [0, 350], 'Small GDP', red)\n",
    "medium = \n",
    "large = "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (<ipython-input-2-ec0734f91139>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-2-ec0734f91139>\"\u001b[0;36m, line \u001b[0;32m3\u001b[0m\n\u001b[0;31m    fig = plt.figure(figsize=(8,5))\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "def plot_scatter_fitline(title, subplot, x, y, x_label, y_label, ylim, label, c):\n",
    "        fig = plt.figure(figsize=(8,5))\n",
    "         _ = fig.suptitle(title, size=24)\n",
    "\n",
    "        ax = fig.add_subplot(1,3,1)\n",
    "    _ = ax.scatter(x, y, marker = '*', alpha = .1, c=c, label=label )\n",
    "_ = ax.set_ylim(ylim)\n",
    "_ = ax.set_xlabel(x_label)\n",
    "_ = ax.set_ylabel(y_label)\n",
    "a, b = best_fit(x, y)\n",
    "yfit0 = [a + b * xi for xi in x]\n",
    "_= ax.plot(x0, yfit0, c='black', lw='3.0')\n",
    "_= plt.legend(loc='upper center')\n",
    "\n",
    "# ax2 = fig.add_subplot(1,3,2)\n",
    "# _ = ax2.scatter(x1, y1, marker = '^', alpha = .1, c='blue', label=\"Medium GDP\")\n",
    "# _ = ax2.set_ylim([0, 325])\n",
    "# _ = ax2.set_xlabel('Year')\n",
    "# _ = ax2.set_ylabel('ATM per 100,000')\n",
    "# # _ = ax2.set_title('Medium GDP')\n",
    "# a, b = best_fit(x1, y1)\n",
    "# yfit1 = [a + b * xi for xi in x1]\n",
    "# _= ax2.plot(x1, yfit1, c='black', lw='3.0')\n",
    "# _= plt.legend(loc='upper center')\n",
    "\n",
    "\n",
    "# ax3 = fig.add_subplot(1,3,3)\n",
    "# _ = ax3.scatter(x2, y2, marker = 'o', alpha = .1, c='green', label=\"Large GDP\")\n",
    "# _ = ax3.set_ylim([0, 325])\n",
    "# _ = ax3.set_xlabel('Year')\n",
    "# _ = ax3.set_ylabel('ATM per 100,000')\n",
    "# # _ = ax3.set_title('Large GDP')\n",
    "# a, b = best_fit(x2, y2)\n",
    "# yfit2 = [a + b * xi for xi in x2]\n",
    "# _= ax3.plot(x2, yfit2, c='black', lw='3.0')\n",
    "# _= plt.legend(loc='upper center')\n",
    "\n",
    "plt.subplots_adjust(wspace=0.2,hspace=.4)\n",
    "plt.tight_layout()\n",
    "plt.savefig(title)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def best_fit(x, y):\n",
    "    xbar = sum(x)/len(x)\n",
    "    ybar = sum(y)/len(y)\n",
    "    n = len(x) \n",
    "\n",
    "    num = sum([xi*yi for xi,yi in zip(x, y)]) - n * xbar * ybar\n",
    "    den = sum([xi**2 for xi in x]) - n * xbar**2\n",
    "\n",
    "    b = num / den\n",
    "    a = ybar - b * xbar\n",
    "\n",
    "    return a, b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
