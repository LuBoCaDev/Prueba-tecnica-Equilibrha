import pandas

def ConsultaEntrevista():
    try:
        datos = pandas.read_csv('datos_prueba_tecnica.csv', sep=';')
    except FileNotFoundError:
        print("El archivo 'datos_prueba_tecnica.csv' no se encontró. Verifica la ruta.")
        return
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return
    
    # Mostrar el total de empleados y la cantidad de hombres y mujeres
    hombres = datos[datos['sexo'] == 'H'].shape[0]
    mujeres = datos[datos['sexo'] == 'M'].shape[0]
    print(f"Total de empleados: {hombres + mujeres} (Hombres: {hombres}, Mujeres: {mujeres})")

    # Calcular la suma de salarios brutos anuales en Equilibrha IT (CT2)
    filtro_empresa_centro = (datos['Nombre empresa'] == 'Equilibrha IT') & (datos['Nombre centro trabajo'] == 'Alovera')
    suma_salarios = datos.loc[filtro_empresa_centro, 'salario bruto anual'].sum()
    print(f"Suma de salarios brutos anuales en Equilibrha IT (CT2): {suma_salarios} €")

    # Listar empleados con salario mayor a 28000€ en Equilibrha RRHH
    filtro_salario_empresa = (datos['Nombre empresa'] == 'Equilibrha RRHH') & (datos['salario bruto anual'] > 28000)
    empleados_filtrados = datos.loc[filtro_salario_empresa, ['id empleado', 'nombre', 'apellido1', 'apellido2', 'salario bruto anual', 'Nombre empresa']]
    print("\nListado de empleados con salario mayor a 28000€ en Equilibrha RRHH:")
    if empleados_filtrados.empty:
        print("No hay empleados que cumplan con los criterios.")
    else:
        print(empleados_filtrados.to_string(index=False))

if __name__ == "__main__":
    ConsultaEntrevista()