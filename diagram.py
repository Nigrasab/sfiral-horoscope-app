import matplotlib.pyplot as plt
import numpy as np

def plot_phase_diagram(age):
    theta = np.linspace(0, 4 * np.pi, 500)
    r = 0.4 + 0.01 * age + 0.1 * np.sin(4 * theta)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    ax.plot(x, y, color="navy", linewidth=2.5)
    ax.set_title("Сфиральная диаграмма", fontsize=14, fontweight='bold')
    ax.set_aspect("equal")
    ax.axis("off")

    # Метки фаз (без эмодзи)
    phases = ["зарождение", "рост", "расцвет", "убывание"]
    angles = [0, np.pi / 2, np.pi, 3 * np.pi / 2]

    for phase, angle in zip(phases, angles):
        ax.text(1.1 * np.cos(angle), 1.1 * np.sin(angle), phase,
                ha="center", va="center", fontsize=10, color="darkred",
                fontweight='bold', bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.2'))

    plt.savefig("static/diagram.png", bbox_inches="tight")
    plt.close()
