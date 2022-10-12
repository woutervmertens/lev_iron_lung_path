import matplotlib.pyplot as plt
import json

bump = [[725.32, 578.58], [243.38, 356.21]]
bump2 = [[182.07, 277.06], [605.62, 633.84]]

# setup
img = plt.imread("iron_lung_bg.png")
fig, ax = plt.subplots()

# load datapoints
with open('coords.json', 'r') as f:
    data = json.load(f)
x = [c[0] for c in data]
y = [c[1] for c in data]

# draw bg
ax.imshow(img, extent=[0, 1000, 0, 1000])

# draw lines
ax.plot(x, y, '--', linewidth=1, color='firebrick')
ax.plot(bump[0], bump[1], '-', linewidth=2, color='yellow')
ax.plot(bump2[0], bump2[1], '-', linewidth=2, color='yellow')

plt.show()
fig.savefig('Lev_Iron_lung_path.png')
