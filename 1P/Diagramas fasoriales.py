import numpy as np
import matplotlib.pyplot as plt

def plot_fasorial(angulo, modulo, label=None, color='b'):
    """
    Función para graficar un número complejo en el plano complejo.
    """
    # Convertir el ángulo a radianes
    angulo_radianes = np.deg2rad(angulo)
    # Calcular las coordenadas finales para la flecha
    x_arrow = modulo * np.cos(angulo_radianes)
    y_arrow = modulo * np.sin(angulo_radianes)
    # Dibujar el vector
    plt.polar([0, angulo_radianes], [0, modulo], color=color)
    #if label:
        #plt.text(angulo_radianes, modulo, label, fontsize=12)
    # Dibujar la flecha
    plt.annotate('', xy=(angulo_radianes, modulo), xytext=(0, 0),
                 arrowprops=dict(facecolor=color, edgecolor=color, arrowstyle="->"))

# Ángulos y módulos de ejemplo
angulo_z1 = 0  # en grados
modulo_z1 = 68
angulo_z2 = -30  # en grados
modulo_z2 = 9

# Graficar los números complejos
plt.figure(figsize=(8, 6))
plot_fasorial(angulo_z1, modulo_z1, label='V', color='r')
plt.text(np.deg2rad(angulo_z1), modulo_z1, 'V', fontsize=12)
plot_fasorial(angulo_z2, modulo_z2, label='I', color='g')
plt.text(np.deg2rad(angulo_z2), modulo_z2-4, 'I', fontsize=12)

# Configuración de la gráfica polar
plt.title('Diagrama Fasorial (Formato Polar)')
plt.grid(True)

# Mostrar leyenda
plt.legend()

# Mostrar gráfica
plt.show()
