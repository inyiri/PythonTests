import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Paraméterek
mu = 50  # átlag (perc)
sigma = 10  # szórás (perc)

# Adattartomány
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Normál eloszlás sűrűségfüggvénye
y = stats.norm.pdf(x, mu, sigma)

# Grafikon rajzolása
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue')
plt.title('Normál eloszlás grafikonja (Átlag: 50 perc, Szórás: 10 perc)')
plt.xlabel('Futási idő (perc)')
plt.ylabel('Valószínűségi sűrűség')
plt.grid(True)
plt.show()
