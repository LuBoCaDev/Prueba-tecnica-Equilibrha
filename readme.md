# Prueba Técnica Equilibrha

## Descripción
Para realizar la prueba he utilizado el archivo .csv.

Se realizan las siguientes operaciones:
1. Cuenta el total de hombres y mujeres.
2. Suma del salario bruto anual de los empleados de Equilibra IT en el centro CT2 Aloovera.
3. Genera un listado de empleados que cobran más de 28k y pertenecen a Equilibrha.

## Requisitos

Librería necesaria: `pandas`. Se instala ejecutando :
   ```bash
   pip install pandas
   ```

## Instrucciones de Ejecución

1. Abrir terminal en la carpeta donde está el archivo `prueba_tecnica.py` y el CSV.
2. Ejecutar el comando:
   ```bash
   python prueba_tecnica.py
   ```
3. Los resultados que se mostrarán en la consola:
   - Total de empleados: 25 (Hombres: 12, Mujeres: 13)
   - Suma de salarios brutos anuales en Equilibrha IT (CT2): 134332 €
   - Listado de empleados con salario mayor a 28000€ en Equilibrha RRHH:

| id empleado | nombre    | apellido1   | apellido2   | salario bruto anual | Nombre empresa   |
|-------------|-----------|-------------|-------------|---------------------|------------------|
| E00018      | ALEJANDRO | YEBRA       | LUENGO      | 31333               | Equilibrha RRHH  |
| E00019      | PAULA     | TIRADO      | MARTINEZ    | 32833               | Equilibrha RRHH  |
| E00020      | LAIA      | MULLER      | SANCHEZ     | 34333               | Equilibrha RRHH  |
| E00023      | EMMA      | FERNANDEZ   | SANCHEZ     | 28333               | Equilibrha RRHH  |
| E00024      | ALBA      | BOTICARIO   | ABAD        | 29833               | Equilibrha RRHH  |
