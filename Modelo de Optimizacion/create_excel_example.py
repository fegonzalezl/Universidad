import pandas as pd

data = {
    'x_real': [100.1, 100.6, 101.2],
    'y_real': [200.2, 200.8, 201.5],
    'x_planificada': [100, 100, 101],
    'y_planificada': [200, 201, 201],
    'diferencia_x': [0.1, 0.6, 0.2],
    'diferencia_y': [0.2, -0.2, 0.5],
    'id': ['P1', 'P2', 'P3']
}

df = pd.DataFrame(data)
df.to_excel('datos_ejemplo.xlsx', index=False)
