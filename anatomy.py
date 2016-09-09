# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. 
# Distributed under the MIT License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter

np.random.seed(123)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1,Y2,len(X))

plt.figure(figsize=(8,8), facecolor="w")
ax = plt.subplot(111, aspect=1)

plt.axes().xaxis.set_major_locator(MultipleLocator(1.000))
plt.axes().xaxis.set_minor_locator(MultipleLocator(0.250))
plt.axes().yaxis.set_major_locator(MultipleLocator(1.000))
plt.axes().yaxis.set_minor_locator(MultipleLocator(0.250))

def minor_tick(x, pos):
    if not x % 1.0:return ""
    return "%.2f" % x
plt.axes().xaxis.set_minor_formatter(FuncFormatter(minor_tick))

plt.xlim(0,4)
plt.ylim(0,4)

plt.tick_params(which='major', width=1.0)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', width=1.0, labelsize=10)
plt.tick_params(which='minor', length= 5, labelsize=10, labelcolor='.25')

plt.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

plt.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
plt.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
plt.scatter(X, Y3, c='w')

plt.title("Anatomy of a figure", fontsize=20)
plt.suptitle("Sources available at "
             "http://github.com/rougier/figure-anatomy",
             fontsize=10, family="monospace", color='.5')
plt.xlabel("X axis label")
plt.ylabel("Y axis label")

plt.legend(frameon=False)


def circle(x, y, radius=0.15):
    center = x,y
    circle = Circle(center, radius, clip_on=False, zorder=10,
                    edgecolor='white', facecolor='none', linewidth=5.0)
    plt.axes().add_artist(circle)
    circle = Circle(center, radius, clip_on=False, zorder=20,
                    edgecolor='none', facecolor='black', alpha=.025)
    plt.axes().add_artist(circle)
    circle = Circle(center, radius, clip_on=False, zorder=30,
                    edgecolor='black', facecolor='none', linewidth=1.0)
    plt.axes().add_artist(circle)

def text(x, y, text):
    plt.text(x,y, text, backgroundcolor="white", 
             ha='center', va='top', weight='bold', color='blue')

circle( 0.50, -.05) # Minor tick
text(0.50,-0.25, "Minor tick label")

circle( 4.00, 2.00) # Major tick
text(4.00,1.80, "Major tick")

circle( .25, 4.00) # Minor tick
text(.25,3.80, "Minor tick")

circle(-0.05, 3.00) # Major tick label
text(-0.05,2.80, "Major tick label")

circle( 1.80,-0.22) # X Label
text(1.80,-0.4, "X axis label")

circle(-0.20, 1.80) # Y Label
text(-0.20,1.6, "Y axis label")

circle( 1.60, 4.10) # Title
text(1.60,3.9, "Title")

circle( 1.75, 2.80) # Blue plot
text(1.75,2.60, "Line\n(line plot)")

circle( 1.20, 0.60) # Red plot
text(1.20, 0.40, "Line\n(line plot)")

circle( 3.20, 1.75) # Scatter plot
text(3.20,1.55, "Markers\n(scatter plot)")

circle( 3.00, 3.00) # Grid
text(3.00,2.80, "Grid")

circle( 3.70, 3.75) # Legend
text(3.70,3.55, "Legend")

circle(.5, .5) # Axis
text(.5,.3, "Axis")

circle(-.3, .65) # Plot
text(-.3,.45, "Plot")

color = 'blue'
plt.annotate('Spines', xy=(4.0, 0.35), xycoords='data',
             xytext=(3.3, 0.5), textcoords='data',
             weight='bold', color=color,
             arrowprops=dict(arrowstyle='->',
                             connectionstyle="arc3",
                             color=color))

plt.annotate('', xy=(3.15, 0.0), xycoords='data',
             xytext=(3.45, 0.45), textcoords='data',
             weight='bold', color=color,
             arrowprops=dict(arrowstyle='->',
                             connectionstyle="arc3",
                             color=color))

plt.text(4.0, -0.4, "Made with http://matplotlib.org",
         fontsize=10, ha="right", color='.5')

plt.savefig("anatomy.pdf")
plt.savefig("anatomy.png", dpi=150)
plt.show()
