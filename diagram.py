import matplotlib.pyplot as plt
import numpy as np

def plot_phase_diagram(age):
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1 + 0.3 * np.sin(age * theta / 4)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.figure(figsize=(4, 4))
    plt.plot(x, y, label=f"Фаза {age % 4}")
    plt.title("Сфиральная диаграмма")
    plt.axis("off")
    plt.savefig("static/diagram.png")
    plt.close()
