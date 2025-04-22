import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ejemplo: Creamos un DataFrame de ejemplo con datos aleatorios
np.random.seed(42)
datos = {
    'Ventas': np.random.randint(100, 500, 12),
    'Gastos': np.random.randint(50, 400, 12),
    'Ganancias': np.random.randint(20, 300, 12)
}
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos, index=meses)

# Creamos una figura con múltiples subplots (uno por columna)
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 12))

# Iteramos por cada columna y eje para graficar
for ax, columna in zip(axes, df.columns):
    df[columna].plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title(f'{columna} Mensuales')
    ax.set_ylabel(columna)
    ax.set_xlabel('Meses')
    ax.grid(True)

plt.tight_layout()
plt.show()