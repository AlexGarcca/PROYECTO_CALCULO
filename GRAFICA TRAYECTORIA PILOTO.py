import numpy as np
import matplotlib.pyplot as plt

# Datos dados
h = 35000  # pies
k = 860    # mi/h^2
v = 300    # mi/h

# Convertir altura de pies a millas (1 milla = 5280 pies)
h_mi = h / 5280

# Calcular l
l = np.sqrt(6 * h_mi / k)

# Coeficientes del polinomio cúbico P(x) = ax^3 + bx^2
a = -2 * h_mi / l**3
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
h = 6.63  # Altitud de crucero en millas
L = 64.52  # Distancia horizontal en millas

# Polinomio cúbico
x = np.linspace(0, L, 500)
y = - (2 * h / L**3) * x**3 + (3 * h / L**2) * x**2

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Trayectoria de aproximación')
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.axvline(0, color='black', linewidth=1, linestyle='--')
plt.axvline(L, color='red', linewidth=1, linestyle='--', label=f'Punto de inicio del descenso ({L:.2f} millas)')
plt.xlabel('Distancia horizontal (millas)')
plt.ylabel('Altitud (millas)')
plt.title('Trayectoria de aterrizaje del avion y su piloto.')
plt.legend()
plt.grid(True)
plt.show()
