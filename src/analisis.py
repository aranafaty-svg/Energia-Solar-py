import pandas as pd


def cargar_datos(ruta_csv: str) -> pd.DataFrame:
    """Carga el dataset desde un archivo CSV."""
    return pd.read_csv(ruta_csv)


def mostrar_columnas(df: pd.DataFrame) -> list:
    """Devuelve la lista de columnas del DataFrame."""
    return df.columns.tolist()


def resumen_dataset(df: pd.DataFrame) -> dict:
    """Devuelve un resumen general del dataset."""
    return {
        "filas": len(df),
        "columnas": len(df.columns),
        "nombres_columnas": df.columns.tolist(),
        "valores_nulos": df.isnull().sum().to_dict(),
    }


if __name__ == "__main__":
    ruta = "data/solar_paraguay_limpio.csv"
    df = cargar_datos(ruta)

    print("Dataset cargado correctamente")
    print("Columnas:", mostrar_columnas(df))

    resumen = resumen_dataset(df)
    print("Cantidad de filas:", resumen["filas"])
    print("Cantidad de columnas:", resumen["columnas"])
    print("Valores nulos por columna:")
    print(resumen["valores_nulos"])