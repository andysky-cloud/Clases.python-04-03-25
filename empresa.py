from clases import *
from datetime import date

# Empresa
miEmpresa = Empresa("Adem Solutions", "3204567890", "Pasto")

# Departamentos
dep1 = Departamento(1, "Sistemas", "Piso 2")
dep2 = Departamento(2, "Administración", "Piso 1")

miEmpresa.registrarDepartamento(dep1)
miEmpresa.registrarDepartamento(dep2)

# Contratos
contrato1 = Contrato(101, "Indefinido", date.today(), date.today())
contrato2 = Contrato(102, "Fijo", date.today(), date.today())

# Empleados
emp1 = Administrativo(1, "Mariana Pareja", 2500, "123456", contrato1, "Gerente")
emp2 = Operativo(2, "Carlos Figuera", 1800, "789456", contrato2, "Producción")

# Empleados en los departamentos
dep1.agregarEmpleado(emp1)
dep1.agregarEmpleado(emp2)

# Listar empleados
print("Empleados del Departamento Sistemas")
dep1.listarEmpleados()

print("***************************************************")
print(f"Empleado: {emp1.get_nombre()}")
print(f"Salario Final: {emp1.calcularSalario()}")