import matplotlib.pyplot as plt

dct={128:69.3333,256:126.2222, 512:240.0000, 1024: 467.5555, 2048: 922.6666}
x_axis_label="Packet Size"
y_axis_label="Throughput"
graph_name="Packet Size vs Throughput Comparison"


x = list(dct.keys())
y = list(dct.values())


plt.figure(figsize=(8, 6)) 
plt.plot(x, y, marker='o', linestyle='solid', color='c', label=y_axis_label)
for i in range(len(x)):
    plt.annotate(f"({x[i]}, {y[i]:.2f})", (x[i], y[i]), textcoords="offset points", xytext=(5, -3), ha='left', fontsize=8)

plt.xlabel(x_axis_label)
plt.ylabel(y_axis_label)
plt.title(graph_name)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlim(0, max(x) + max(x)*.2)
plt.ylim(0, max(y) + max(y)*.2)
plt.savefig(f"{graph_name}.png")