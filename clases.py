class Contrato(): 
    
     
    def __init__(self, idContrato, tipoContrato, fechaInicio, fechaFin):
        self.__idContrato = idContrato
        self.__tipoContrato = tipoContrato
        self.__fechaInicio = fechaInicio 
        self.__fechaFin = fechaFin 
        
    def generarContrato(self):
        return f"contrato {self.__tipoContrato} generado."
    
    def finalizarContrato(self):
        return f"contrato finalizado {self.__fechaFin}"
    
    

        
class Empleado():
    def __init__(self, idEmpleado, nombre, salario, cedula, contrato):
        self.__idEmpleado = idEmpleado
        self.__nombre = nombre
        self.__salario = salario
        self.__cedula = cedula
        self.__contrato = contrato
        
    def get_nombre(self):
        return self.__nombre
    
    def get_salario(self):
        return self.__salario 
    
    def calcularSalario(self):
        return self.__salario
    
    def mostrarInformacion(self):
        return f"Empleado: {self.__nombre} Salario: {self.calcularSalario()}"
    

        
class Administrativo(Empleado):
    def __init__(self,idEmpleado, nombre, salario, cedula, contrato, cargo):
        super().__init__(idEmpleado, nombre, salario, cedula, contrato)
        self.__cargo = cargo
        
    def calcularSalario(self):
        return self.get_salario() + 500
    
    def aprobarDocumentos(self):
        return "Documentos aprobados."
    

    
        
class Operativo(Empleado):
    def __init__(self, idEmpleado, nombre, salario, cedula, contrato, areaTrabajo):
        super().__init__(idEmpleado, nombre, salario, cedula, contrato)
        self.__areaTrabajo = areaTrabajo

    def calcularSalario(self):
        return self.get_salario() + 300
    
    def realizarTarea(self):
        return "Tarea realizada."
        

    
class Departamento:
    def __init__(self, idDepartamento, nombre, ubicacion):
        self.__idDepartamento = idDepartamento
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__empleados = [] 

    def agregarEmpleado(self, empleado):
        self.__empleados.append(empleado)

    def eliminarEmpleado(self, empleado):
        self.__empleados.remove(empleado)

    def listarEmpleados(self):
        for emp in self.__empleados:
            print(emp.mostrarInformacion())
        
        
        
class Empresa():
    def __init__(self, nombre, telefono, direccion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion
        self.__departamentos = [] 

    def registrarDepartamento(self, departamento):
        self.__departamentos.append(departamento)

    def listarDepartamentos(self):
        for dep in self.__departamentos:
            print(dep)