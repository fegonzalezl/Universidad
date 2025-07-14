import ezdxf

def get_color(diff_x, diff_y):
    """
    Determina el color del punto en función de las diferencias.
    """
    diff_x = abs(diff_x)
    diff_y = abs(diff_y)
    if (0 <= diff_x <= 0.5) or (0 <= diff_y <= 0.5):
        return 3  # Verde
    elif (0.5 < diff_x <= 1) or (0.5 < diff_y <= 1):
        return 2  # Amarillo
    else:
        return 1  # Rojo

def create_dxf(data, output_path):
    """
    Crea un archivo DXF a partir de los datos de un DataFrame.
    """
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Crear capas
    doc.layers.new(name="PUNTOS_PLANIFICADOS", dxfattribs={'color': 7})  # Blanco
    doc.layers.new(name="PUNTOS_REALES", dxfattribs={'color': 7})  # Blanco
    doc.layers.new(name="IDS", dxfattribs={'color': 7})  # Blanco

    for index, row in data.iterrows():
        # 1. Dibujar punto planificado (X)
        plan_point = (row['x_planificada'], row['y_planificada'])
        msp.add_line((plan_point[0] - 0.15, plan_point[1] - 0.15),
                     (plan_point[0] + 0.15, plan_point[1] + 0.15),
                     dxfattribs={'layer': 'PUNTOS_PLANIFICADOS'})
        msp.add_line((plan_point[0] - 0.15, plan_point[1] + 0.15),
                     (plan_point[0] + 0.15, plan_point[1] - 0.15),
                     dxfattribs={'layer': 'PUNTOS_PLANIFICADOS'})

        # 2. Dibujar punto real (círculo)
        real_point = (row['x_real'], row['y_real'])
        color = get_color(row['diferencia_x'], row['diferencia_y'])
        msp.add_circle(real_point, radius=0.15, dxfattribs={'layer': 'PUNTOS_REALES', 'color': color})

        # 3. Añadir texto de ID
        text_position = (real_point[0] + 0.2, real_point[1])
        msp.add_text(str(row['id']),
                     dxfattribs={
                         'layer': 'IDS',
                         'height': 0.2,
                         'insert': text_position
                     })

    doc.saveas(output_path)
