from mplsoccer import Pitch
import matplotlib.pyplot as plt

# DATA
x = [108, 94, 88, 106, 78, 92, 89]
y = [42, 38, 45, 48, 50, 55, 40]
xg = [0.12, 0.25, 0.08, 0.65, 0.04, 0.15, 0.09]
outcome = ['Shot','Shot','Shot','Goal','Shot','Shot','Shot']

fig, ax = plt.subplots(figsize=(8.5, 12))
fig.set_facecolor('#7ab86f')

# Grass stripes
for i in range(0, 120, 10):
    col = '#7ab86f' if i % 20 == 0 else '#6aa86f'
    ax.axvspan(i, i+10, color=col, zorder=0)

pitch = Pitch(pitch_type='statsbomb', pitch_color='#7ab86f',
              line_color='white', linewidth=2, stripe=True, goal_type='box')
pitch.draw(ax=ax)

# Shots - White and Red
for i in range(len(x)):
    if outcome[i] == 'Goal':
        col = '#E63946'
        size = xg[i] * 2800 + 250
    else:
        col = 'white'
        size = xg[i] * 2200 + 180

    pitch.scatter(x[i], y[i], s=size, c=col, edgecolors='black',
                  linewidth=1.5, ax=ax, zorder=5)

# HEADER
fig.text(0.5, 0.96, 'ABHA FC vs AL HAZM', ha='center', fontsize=20,
         fontweight='bold', color='white')
fig.text(0.5, 0.93, '13 AUG 2026 | SHOT MAP | L 1-2 | xG 1.38',
         ha='center', fontsize=11, color='white')

# SMALL OUTCOME BOX - FIXED (no patheffects)
from matplotlib.patches import FancyBboxPatch
box = FancyBboxPatch((0.68, 0.82), 0.28, 0.1, boxstyle="round,pad=0.02",
                     facecolor='white', edgecolor='black', alpha=0.95,
                     transform=fig.transFigure, zorder=10)
fig.patches.append(box)

fig.text(0.82, 0.905, 'OUTCOME', ha='center', fontsize=11,
         fontweight='bold', color='black', zorder=11)

fig.text(0.70, 0.87, '●', fontsize=18, color='white', ha='left', va='center', zorder=11)
fig.text(0.74, 0.87, 'Shot', fontsize=10, color='black', fontweight='bold', zorder=11)

fig.text(0.70, 0.84, '●', fontsize=18, color='#E63946', ha='left', va='center', zorder=11)
fig.text(0.74, 0.84, 'Goal', fontsize=10, color='black', fontweight='bold', zorder=11)

fig.text(0.5, 0.02, 'Analyst: Salman | Data: FBRef', ha='center', fontsize=9, color='white')

plt.axis('off')
plt.savefig('ABHA_GREEN_PRO.png', dpi=500, bbox_inches='tight', facecolor='#7ab86f')
plt.show()
print("SAVED: ABHA_GREEN_PRO.png - 500 DPI!")