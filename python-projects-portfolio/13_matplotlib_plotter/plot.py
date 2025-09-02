import matplotlib.pyplot as plt

x = list(range(1, 8))
y = [3, 5, 2, 6, 7, 8, 4]

plt.figure()
plt.plot(x, y, marker="o")
plt.title("Sample Trend")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("chart.png", dpi=150)
print("Saved chart.png")
