import matplotlib.pyplot as plt
import numpy as np

def plot_phase_diagram(age):
    theta = np.linspace(0, 4 * np.pi, 500)  # два оборота
    r = 0.3 + 0.05 * age + 0.1 * np.sin(4 * theta)  # вложенная фаза

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(x, y, color="darkblue", linewidth=2)
    ax.set_title("Сфиральная диаграмма", fontsize=12)
    ax.set_aspect("equal")
    ax.axis("off")

    # Метки фаз
    phases = ["зарождение", "рост", "расцвет", "убывание"]
    emojis = ["🌑", "🌱", "🌻", "🍂"]
    for i, (label, emoji) in enumerate(zip(phases, emojis)):
        angle = i * np.pi / 2
        ax.text(0.5 * np.cos(angle), 0.5 * np.sin(angle), emoji + "\n" + label, 
                ha="center", va="center", fontsize=10, color="darkred")

    plt.savefig("static/diagram.png", bbox_inches="tight")
    plt.close()
