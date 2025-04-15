from database import Database
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree

# Obtencion de los datos
db = Database()
datos = db.obtener_datos_numpy()
db.close()

# Seleccionando los datos para el entrenamiento y validacion
X = datos[:, :-1]  
y = datos[:, -1]  

X_entrena, X_prueba, y_entrena, y_prueba = train_test_split( X, y, random_state = 10 )

# Creacion del clasificador
modelo = tree.DecisionTreeClassifier(random_state=31)
modelo.fit(X, y)

exactitud = modelo.score(X_entrena, y_entrena)
print( "Entrenamiento:", exactitud )

exactitud = modelo.score(X_prueba, y_prueba)
print( "Prueba:", exactitud )

#nuevo_producto = np.array([[9500.0, 4.7]])  # Formato: [precio, calificación]
#prediccion = modelo.predict(nuevo_producto)
## 3. Interpretar el resultado
#print("\n🔮 Predicción para nuevo producto:")
#print(f"Precio: ${nuevo_producto[0][0]:.2f}, Calificación: {nuevo_producto[0][1]}")
#print("Recomendado:", "✅ Sí" if prediccion[0] == 1 else "❌ No")
