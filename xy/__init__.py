import numpy as np

# def plot_intervals(intervals):
#     plt.figure(figsize=(10, 4))
#
#     for i, interval in enumerate(intervals):
#         plt.plot([interval[0], interval[1]], [i, i], 'o-')
#
#     plt.yticks(range(len(intervals)), [f'Interval {i+1}' for i in range(len(intervals))])
#     plt.xlabel('Position')
#     plt.ylabel('Intervals')
#     plt.title('Intervals on 2D Coordinate')
#     plt.grid(True)
#     plt.show()

# def plot_intervals(intervals):
#     plt.figure(figsize=(8, 4))
#
#     for interval in intervals:
#         plt.plot([interval[0], interval[1]], [0, 0], marker='o', markersize=10)
#
#     plt.yticks([])
#     plt.xlabel('X Coordinate')
#     plt.title('Interval Positions on X-Y Coordinate')
#     plt.grid(True)
#     plt.show()

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    ts = np.transpose(intervals)
    print(ts)

