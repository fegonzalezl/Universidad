import pandas as pd

def load_data(file_path):
    """
    Lee un archivo Excel y valida que contenga las columnas necesarias.

    Args:
        file_path (str): Ruta al archivo Excel.

    Returns:
        pandas.DataFrame: DataFrame con los datos del Excel.
    """
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        raise Exception(f"Error: No se encontró el archivo en la ruta: {file_path}")
    except Exception as e:
        raise Exception(f"Error al leer el archivo Excel: {e}")

    required_columns = [
        'x_real', 'y_real', 'x_planificada', 'y_planificada',
        'diferencia_x', 'diferencia_y', 'id'
    ]

    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Error: La columna '{col}' no se encuentra en el archivo Excel.")

    # Validar que las columnas de coordenadas sean numéricas
    for col in ['x_real', 'y_real', 'x_planificada', 'y_planificada']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if df[col].isnull().any():
            raise Exception(f"Error: La columna '{col}' contiene valores no numéricos.")

    return df
