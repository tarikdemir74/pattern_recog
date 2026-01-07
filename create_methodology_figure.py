import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 8))
ax.set_xlim(0, 16)
ax.set_ylim(0, 8)
ax.axis('off')

def draw_block(ax, x, y, width, height, text, color='lightblue', fontsize=14, text_color='black'):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.03,rounding_size=0.15",
                         facecolor=color, edgecolor='#333333', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight='bold',
            color=text_color, wrap=True)

def draw_arrow(ax, x1, y1, x2, y2, color='#333333', lw=2.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))

# Title
ax.text(8, 7.5, 'Hybrid Brain Tumor Classification Pipeline',
        fontsize=26, fontweight='bold', ha='center', color='#0066CC')

# ===== MAIN PIPELINE (horizontal) =====
y_main = 5

# Stage 1: Input
draw_block(ax, 1.3, y_main, 2, 1.4, 'MRI\nInput', '#E8F5E9', 16)

# Stage 2: Preprocessing
draw_block(ax, 4, y_main, 2.2, 1.4, 'Preprocess\n(299×299)', '#FFF3E0', 14)

# Stage 3: CNN
draw_block(ax, 7, y_main, 2.2, 1.6, 'Xception\nCNN', '#BBDEFB', 16)

# Stage 4: Meta-Learner
draw_block(ax, 10.5, y_main, 2.2, 1.6, 'Meta-\nLearner', '#E1BEE7', 16)

# Stage 5: Rule Engine
draw_block(ax, 14, y_main, 2.2, 1.6, 'Rule\nEngine', '#FFCDD2', 16)

# Arrows main flow
draw_arrow(ax, 2.3, y_main, 2.9, y_main)
draw_arrow(ax, 5.1, y_main, 5.9, y_main)
draw_arrow(ax, 8.1, y_main, 9.4, y_main)
draw_arrow(ax, 11.6, y_main, 12.9, y_main)

# ===== SHAPE FEATURES BRANCH =====
y_shape = 2.2
draw_block(ax, 7, y_shape, 2.5, 1.2, 'Shape\nFeatures', '#FFECB3', 14)

# Arrow from preprocessing down and to shape
ax.plot([4, 4, 5.75], [y_main - 0.7, y_shape, y_shape], 'k-', lw=2.5)
ax.annotate('', xy=(5.75, y_shape), xytext=(5.6, y_shape),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=2.5))

# Arrow from shape features up to meta-learner
ax.plot([8.25, 9.5, 9.5], [y_shape, y_shape, y_main - 0.8], 'k-', lw=2.5)
ax.annotate('', xy=(10.5, y_main - 0.8), xytext=(9.5, y_main - 0.8),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=2.5))

# ===== CNN OUTPUT (Probabilities) =====
draw_block(ax, 7, 6.8, 2, 0.9, 'Probabilities', '#C8E6C9', 13)
draw_arrow(ax, 7, y_main + 0.8, 7, 6.35)

# Arrow from probabilities to meta-learner
ax.plot([8, 9.5, 9.5], [6.8, 6.8, y_main + 0.8], 'k-', lw=2.5)
ax.annotate('', xy=(10.5, y_main + 0.8), xytext=(9.5, y_main + 0.8),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=2.5))

# ===== OUTPUTS =====
# Accept output
draw_block(ax, 14, 6.8, 1.8, 0.9, 'ACCEPT\n(89%)', '#C8E6C9', 13)
draw_arrow(ax, 14, y_main + 0.8, 14, 6.35)

# Refer output
draw_block(ax, 14, 3.2, 1.8, 0.9, 'REFER\n(11%)', '#FFCDD2', 13)
draw_arrow(ax, 14, y_main - 0.8, 14, 3.65)

# ===== INFO BOXES =====
# Shape features info
ax.add_patch(FancyBboxPatch((4.5, 0.3), 5, 1.1,
                            boxstyle="round,pad=0.02", facecolor='#FFF8E1',
                            edgecolor='#999999', linewidth=1))
ax.text(7, 1.05, 'Shape Features:', fontsize=11, ha='center', fontweight='bold')
ax.text(7, 0.55, 'Area | Perimeter | Circularity | Solidity | Irregularity', fontsize=10, ha='center')

# Rule engine info
ax.add_patch(FancyBboxPatch((10.5, 0.3), 4.5, 1.1,
                            boxstyle="round,pad=0.02", facecolor='#FFEBEE',
                            edgecolor='#999999', linewidth=1))
ax.text(12.75, 1.05, 'Decision Rules:', fontsize=11, ha='center', fontweight='bold')
ax.text(12.75, 0.55, 'Confidence < 0.80 OR Irregularity > 26.81', fontsize=10, ha='center')

plt.tight_layout()
fig.savefig('/Users/umutturklay/dev/UE/pattern_recog/Figures_PNG/Methodology_Pipeline.png',
            dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.2)
plt.close(fig)
print("Saved: Methodology_Pipeline.png")
