import argparse
import data_loader
import dxf_generator

def main():
    parser = argparse.ArgumentParser(description="Convierte datos de Excel a un archivo DXF para Vulcan.")
    parser.add_argument("excel_file", help="Ruta al archivo Excel de entrada.")
    parser.add_argument("dxf_file", help="Ruta al archivo DXF de salida.")
    args = parser.parse_args()

    try:
        print(f"Leyendo datos de {args.excel_file}...")
        data = data_loader.load_data(args.excel_file)

        print(f"Generando archivo DXF en {args.dxf_file}...")
        dxf_generator.create_dxf(data, args.dxf_file)

        print("¡Proceso completado con éxito!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
