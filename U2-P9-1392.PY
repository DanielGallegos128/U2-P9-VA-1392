import matplotlib.pyplot as plt
import numpy as np
# Daniel Gallegos NC 1392
materias = ["Vision A","Machine L","Lenguaje N","Pensamiento M","Ingles"]
calificaciones = [9,10,8,10,9]

plt.pie(calificaciones, labels=materias, autopct= '% 1.1f%%')
plt.title("Grafica de Pie 1392")
plt.show()
print("Daniel Gallegos NC 1392")