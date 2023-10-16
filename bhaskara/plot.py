import numpy as np
import matplotlib.pyplot as plt
from bhaskara.calculator import calcula_bhaskara

# v1, v2, v3 = -1, 1, 6
v1, v2, v3 = 1, 7, 12

x1, x2, x, y = calcula_bhaskara(v1, v2, v3)
print(x1, x2, x, y)

fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x1, max(y), c='r')
ax.scatter(x2, max(y), c='r')
ax.scatter(np.mean(x), min(y), c='r')

ax.set(xlim=(min(x)-1, max(x)+1), ylim=(min(y)-1, max(y)+1), aspect='equal')

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('x', size=12, labelpad=-2, x=1)
ax.set_ylabel('y', size=12, labelpad=24, x=1, rotation=0)

ticks_frequency = 1
x_ticks = np.arange(min(x), max(x)+1, ticks_frequency)
y_ticks = np.arange(min(y), max(y)+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])

ax.set_xticks(np.arange(min(x), max(x)+1), minor=True)
ax.set_yticks(np.arange(min(y), max(y)+1), minor=True)

ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.plot(x, y)
plt.show()
