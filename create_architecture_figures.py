import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def draw_block(ax, x, y, width, height, text, color='lightblue', fontsize=14, linewidth=2):
    """Draw a rounded rectangle block with text"""
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.03,rounding_size=0.12",
                         facecolor=color, edgecolor='#333333', linewidth=linewidth)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight='bold', wrap=True)

def draw_arrow(ax, x1, y1, x2, y2, lw=2):
    """Draw an arrow between two points"""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#333333', lw=lw))

# ==================== FIGURE 1: Xception Architecture (HORIZONTAL) ====================
fig1, ax1 = plt.subplots(1, 1, figsize=(16, 8))
ax1.set_xlim(0, 16)
ax1.set_ylim(0, 8)
ax1.axis('off')

# Title
ax1.text(8, 7.5, 'Xception CNN Architecture', fontsize=28, fontweight='bold', ha='center', color='#0066CC')

# Blocks - HORIZONTAL flow
x_positions = [1.5, 4, 6.3, 8.3, 10.3, 12.3, 14.5]
y_center = 4.5

blocks = [
    (x_positions[0], y_center, 2.2, 1.6, 'Input\n299×299×3', '#E8F5E9', 14),
    (x_positions[1], y_center, 2.5, 2, 'Xception\nBase\n21.1M', '#BBDEFB', 14),
    (x_positions[2], y_center, 1.8, 1.4, 'Global\nMaxPool', '#E3F2FD', 12),
    (x_positions[3], y_center, 1.6, 1.2, 'Flatten', '#FFF3E0', 13),
    (x_positions[4], y_center, 1.8, 1.4, 'Dense\n(128)', '#E1BEE7', 13),
    (x_positions[5], y_center, 1.8, 1.4, 'Dropout', '#FFECB3', 13),
    (x_positions[6], y_center, 2, 1.6, 'Dense(4)\nSoftmax', '#C8E6C9', 13),
]

for x, y, w, h, text, color, fs in blocks:
    draw_block(ax1, x, y, w, h, text, color, fs)

# Arrows between blocks
for i in range(len(x_positions) - 1):
    x1 = x_positions[i] + blocks[i][2]/2
    x2 = x_positions[i+1] - blocks[i+1][2]/2
    draw_arrow(ax1, x1 + 0.1, y_center, x2 - 0.1, y_center)

# Output labels
ax1.text(8, 2.3, 'Output Classes: Glioma | Meningioma | No Tumor | Pituitary',
         fontsize=16, ha='center', style='italic', color='#444444')

# Training info box
ax1.add_patch(FancyBboxPatch((0.3, 0.3), 4.5, 1.5,
                             boxstyle="round,pad=0.02", facecolor='#F5F5F5',
                             edgecolor='#999999', linewidth=1))
ax1.text(2.55, 1.4, 'Training: Adamax | LR: 0.001', fontsize=12, ha='center', fontweight='bold')
ax1.text(2.55, 0.8, 'Epochs: 10 | Batch: 32', fontsize=12, ha='center')

# Architecture info box
ax1.add_patch(FancyBboxPatch((11.2, 0.3), 4.5, 1.5,
                             boxstyle="round,pad=0.02", facecolor='#F5F5F5',
                             edgecolor='#999999', linewidth=1))
ax1.text(13.45, 1.4, 'Depthwise Separable Conv', fontsize=12, ha='center', fontweight='bold')
ax1.text(13.45, 0.8, 'Entry → Middle → Exit Flow', fontsize=12, ha='center')

plt.tight_layout()
fig1.savefig('/Users/umutturklay/dev/UE/pattern_recog/Figures_PNG/Architecture_Xception.png',
             dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.2)
plt.close(fig1)
print("Saved: Architecture_Xception.png")

# ==================== FIGURE 2: Comparison Models (HORIZONTAL) ====================
fig2, ax2 = plt.subplots(1, 1, figsize=(16, 8))
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 8)
ax2.axis('off')

# Title
ax2.text(8, 7.5, 'Comparison Model Architectures', fontsize=28, fontweight='bold', ha='center', color='#0066CC')

models = [
    ('DenseNet121', '7.2M params', '#BBDEFB', 2.7),
    ('ResNet50', '23.9M params', '#C8E6C9', 8),
    ('EfficientNetB0', '4.2M params', '#FFECB3', 13.3),
]

for model_name, params, color, x_center in models:
    # Model name
    ax2.text(x_center, 6.5, model_name, fontsize=18, fontweight='bold', ha='center', color='#0066CC')

    # Simplified vertical blocks
    blocks = [
        (x_center, 5.2, 2.5, 0.8, 'Input (299×299)', '#E8F5E9', 11),
        (x_center, 4.0, 2.8, 1.0, f'{model_name}\n({params})', color, 11),
        (x_center, 2.8, 2.3, 0.7, 'GlobalMaxPool', '#E3F2FD', 11),
        (x_center, 1.8, 2.0, 0.7, 'Dense (128)', '#E1BEE7', 11),
        (x_center, 0.8, 2.0, 0.7, 'Dense (4)', '#C8E6C9', 11),
    ]

    for x, y, w, h, text, c, fs in blocks:
        draw_block(ax2, x, y, w, h, text, c, fs, linewidth=1.5)

    # Arrows
    y_positions = [5.2, 4.0, 2.8, 1.8, 0.8]
    heights = [0.8, 1.0, 0.7, 0.7, 0.7]
    for i in range(len(y_positions) - 1):
        y1 = y_positions[i] - heights[i]/2
        y2 = y_positions[i+1] + heights[i+1]/2
        draw_arrow(ax2, x_center, y1 - 0.05, x_center, y2 + 0.05, lw=1.5)

# Divider lines
ax2.axvline(x=5.35, color='#CCCCCC', linewidth=1, linestyle='--')
ax2.axvline(x=10.65, color='#CCCCCC', linewidth=1, linestyle='--')

plt.tight_layout()
fig2.savefig('/Users/umutturklay/dev/UE/pattern_recog/Figures_PNG/Architecture_Comparison.png',
             dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.2)
plt.close(fig2)
print("Saved: Architecture_Comparison.png")

print("\nArchitecture figures created successfully!")
