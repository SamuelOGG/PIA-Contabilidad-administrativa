print("Bienvenido al programa que te ayudara con el presupuesto maestro")
print("1.Presupuesto de ventas")

Producto1 = input(f"\nDime el nombre de tu primer producto: ")
UnidadesVenderSem1P1 = int(input("Dime las unidades a vender del producto en el primer semestre: "))
PrecioVentaSem1P1 = float(input("Dime el precio de venta de tu producto en el primer semestre: "))
ImporteSem1P1 = UnidadesVenderSem1P1 * PrecioVentaSem1P1
print(f"\nTu importe de venta del semestre uno del producto {Producto1} es {ImporteSem1P1}")
UnidadesVenderSem2P1 = int(input("Dime las unidades a vender del producto en el segundo semestre: "))
PrecioVentaSem2P1 = float(input("Dime el precio de venta de tu producto en el segundo semestre: "))
ImporteSem2P1 = UnidadesVenderSem2P1 * PrecioVentaSem2P1
print(f"\nTu importe de venta del semestre dos del producto {Producto1} es {ImporteSem2P1}")
ImporteAnualP1 = ImporteSem1P1 + ImporteSem2P1
print(f"El Importe para el siguiente año del prodcuto {Producto1} es {ImporteAnualP1}")

Producto2 = input(f"\nDime el nombre de tu producto: ")
UnidadesVenderSem1P2 = int(input("Dime las unidades a vender del producto en el primer semestre: "))
PrecioVentaSem1P2 = float(input("Dime el precio de venta de tu producto en el primer semestre: "))
ImporteSem1P2 = UnidadesVenderSem1P2 * PrecioVentaSem1P2
print(f"\nTu importe de venta del semestre uno del producto {Producto2} es {ImporteSem1P2}")
UnidadesVenderSem2P2 = int(input("Dime las unidades a vender del producto en el segundo semestre: "))
PrecioVentaSem2P2 = float(input("Dime el precio de venta de tu producto en el segundo semestre: "))
ImporteSem2P2 = UnidadesVenderSem2P2 * PrecioVentaSem2P2
print(f"\nTu importe de venta del semestre dos del producto {Producto2} es {ImporteSem2P2}")
ImporteAnualP2 = ImporteSem1P2 + ImporteSem2P2
print(f"El Importe para el siguiente año del prodcuto {Producto2} es {ImporteAnualP2}")

Producto3 = input(f"\nDime el nombre de tu producto: ")
UnidadesVenderSem1P3 = int(input("Dime las unidades a vender del producto en el primer semestre: "))
PrecioVentaSem1P3 = float(input("Dime el precio de venta de tu producto en el primer semestre: "))
ImporteSem1P3 = UnidadesVenderSem1P3 * PrecioVentaSem1P3
print(f"\nTu importe de venta del semestre uno del producto {Producto3} es {ImporteSem1P3}")
UnidadesVenderSem2P3 = int(input("Dime las unidades a vender del producto en el segundo semestre: "))
PrecioVentaSem2P3 = float(input("Dime el precio de venta de tu producto en el segundo semestre: "))
ImporteSem2P3 = UnidadesVenderSem2P3 * PrecioVentaSem2P3
print(f"\nTu importe de venta del semestre dos del producto {Producto3} es {ImporteSem2P3}")
ImporteAnualP3 = ImporteSem1P3 + ImporteSem2P3
print(f"El Importe para el siguiente año del prodcuto {Producto3} es {ImporteAnualP3}")

print(f"\n***TOTAL DE VENTAS***")
TotalVentasSem1 = ImporteSem1P1 + ImporteSem1P2 + ImporteSem1P3
TotalVentasSem2 = ImporteSem2P1 + ImporteSem2P2 + ImporteSem2P3
TotalVentasAño = ImporteAnualP1 + ImporteAnualP2 + ImporteAnualP3

print(f"El total de ventas del semestre 1 es: {TotalVentasSem1}")
print(f"El total de ventas del semestre 2 es: {TotalVentasSem2}")
print(f"El total de ventas del año es: {TotalVentasAño}")

#-------------------------------------------------------------------------------------------------------------------------------

print(f"2. Determinacion del saldo de clientes y flujo de entradas")
SaldoClientesAñoPasado = float(input("Dime el saldo de clientes del año pasado: "))
TotalClientesAñoNuevo = SaldoClientesAñoPasado + TotalVentasAño

print(f"\nTu saldo total de clientes para este nuevo año es {TotalClientesAñoNuevo}")
print(f"\nEntradas de efectivo")
PorcentajeVentasPorCobrar = int(input("Dime el porcentaje de cuentas por cobrar del año pasado: "))
PorCobrarAñoPasado1 = SaldoClientesAñoPasado - (SaldoClientesAñoPasado * (PorcentajeVentasPorCobrar * .01))
PorCobrarAñoPasado =  SaldoClientesAñoPasado - PorCobrarAñoPasado1
print(f"Tu saldo por cobrar del año pasado es {PorCobrarAñoPasado}")
PorcentajeVentasPorCobrarAñoNuevo = int(input("\nDime el porcentaje de cuentas por cobrar del año nuevo: "))
PorCobrarAñoNuevo1 = TotalVentasAño - (TotalVentasAño * (PorcentajeVentasPorCobrarAñoNuevo * .01))
PorCobrarAñoNuevo = TotalVentasAño - PorCobrarAñoNuevo1
print(f"Tu saldo por cobrar del año nuevo es {PorCobrarAñoNuevo}")

TotalCobranza = PorCobrarAñoPasado + PorCobrarAñoNuevo
print(f"\nEl total por cobrar del año nuevo es {TotalCobranza}")
SaldoClientesAñoNuevo = TotalClientesAñoNuevo - TotalCobranza
print(f"Tu saldo de clientes para este nuevo año es {SaldoClientesAñoNuevo}")

#------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n3. Presupuesto de produccion")
print(f"Empezaremos con el producto {Producto1}")
print(f"Las unidades a vender del semestre uno del producto {Producto1} son {UnidadesVenderSem1P1}")
InventarioFinalP1Sem1 = int(input(f"Dime el inventario final del producto {Producto1} del semestre 1: "))
TotalUnidadesSem1P1 = UnidadesVenderSem1P1 + InventarioFinalP1Sem1
print(f"\nEl total de unidades a vender del semestre 1 del producto {Producto1} son {TotalUnidadesSem1P1}")
InventarioInicialP1Sem1 = int(input(f"Dime el Inventario Inicial del producto {Producto1} para el semestre 1: "))
UnidadesProducirP1Sem1 = TotalUnidadesSem1P1 - InventarioInicialP1Sem1
print(f"Las unidades a producir del {Producto1} en el semestre 1 son {UnidadesProducirP1Sem1}")

print(f"\nSeguiremos con el segundo semestre del {Producto1}")
print(f"Las unidades a vender del semestre dos del producto {Producto1} son {UnidadesVenderSem2P1}")
InventarioFinalP1Sem2 = int(input(f"Dime el inventario final del producto {Producto1} del semestre 2: "))
TotalUnidadesSem2P1 = UnidadesVenderSem2P1 + InventarioFinalP1Sem2
print(f"\nEl total de unidades a vender del semestre 2 del producto {Producto1} son {TotalUnidadesSem2P1}")
InventarioInicialP1Sem2 = int(input(f"Dime el Inventario Inicial del producto {Producto1} para el semestre 2: "))
UnidadesProducirP1Sem2 = TotalUnidadesSem2P1 - InventarioInicialP1Sem2
print(f"Las unidades a producir del {Producto1} en el semestre 2 son {UnidadesProducirP1Sem2}")

print(f"\nAhora haremos los calculos para el siguiente año del {Producto1}")
UnidadesVenderAñoP1 = UnidadesVenderSem1P1 + UnidadesVenderSem2P1
print(f"Las unidades a vender para el siguiente año del producto {Producto1} son {UnidadesVenderAñoP1}")
InventarioFinalAñoP1 = InventarioFinalP1Sem2
print(f"El inventario fina para el siguiente año del producto {Producto1} son {InventarioFinalAñoP1}")
TotalUnidadesAñoP1 = UnidadesVenderAñoP1 + InventarioFinalAñoP1
print(f"El total de unidades a vender del producto {Producto1} son {TotalUnidadesAñoP1}")
InventarioInicialP1Año = InventarioInicialP1Sem1
print(f"El inventario inicial del año del producto {Producto1} es {InventarioFinalAñoP1}")
UnidadesProducirP1Año = TotalUnidadesAñoP1 - InventarioFinalAñoP1
print(f"Las unidades a producir para el año del producto {Producto1} son {UnidadesProducirP1Año}")
#----------------------------------------
print(f"Seguiremos con el producto {Producto2}")
print(f"Las unidades a vender del semestre uno del producto {Producto2} son {UnidadesVenderSem1P2}")
InventarioFinalP2Sem1 = int(input(f"Dime el inventario final del producto {Producto2} del semestre 1: "))
TotalUnidadesSem1P2 = UnidadesVenderSem1P2 + InventarioFinalP2Sem1
print(f"\nEl total de unidades a vender del semestre 1 del producto {Producto2} son {TotalUnidadesSem1P2}")
InventarioInicialP2Sem1 = int(input(f"Dime el Inventario Inicial del producto {Producto2} para el semestre 1: "))
UnidadesProducirP2Sem1 = TotalUnidadesSem1P2 - InventarioInicialP2Sem1
print(f"Las unidades a producir del {Producto2} en el semestre 1 son {UnidadesProducirP2Sem1}")

print(f"\nSeguiremos con el segundo semestre del {Producto2}")
print(f"Las unidades a vender del semestre dos del producto {Producto2} son {UnidadesVenderSem2P2}")
InventarioFinalP2Sem2 = int(input(f"Dime el inventario final del producto {Producto2} del semestre 2: "))
TotalUnidadesSem2P2 = UnidadesVenderSem2P2 + InventarioFinalP2Sem2
print(f"\nEl total de unidades a vender del semestre 2 del producto {Producto2} son {TotalUnidadesSem2P2}")
InventarioInicialP2Sem2 = int(input(f"Dime el Inventario Inicial del producto {Producto2} para el semestre 2: "))
UnidadesProducirP2Sem2 = TotalUnidadesSem2P2 - InventarioInicialP2Sem2
print(f"Las unidades a producir del {Producto2} en el semestre 2 son {UnidadesProducirP2Sem2}")

print(f"Ahora haremos los calculos para el siguiente año del {Producto2}")
UnidadesVenderAñoP2 = UnidadesVenderSem1P2 + UnidadesVenderSem2P2
print(f"Las unidades a vender para el siguiente año del producto {Producto2} son {UnidadesVenderAñoP2}")
InventarioFinalAñoP2 = InventarioFinalP2Sem2
print(f"El inventario fina para el siguiente año del producto {Producto2} son {InventarioFinalAñoP2}")
TotalUnidadesAñoP2 = UnidadesVenderAñoP2 + InventarioFinalAñoP2
print(f"El total de unidades a vender del producto {Producto2} son {TotalUnidadesAñoP2}")
InventarioInicialP2Año = InventarioInicialP2Sem1
print(f"El inventario inicial del año del producto {Producto2} es {InventarioFinalAñoP2}")
UnidadesProducirP2Año = TotalUnidadesAñoP2 - InventarioFinalAñoP2
print(f"Las unidades a producir para el año del producto {Producto2} son {UnidadesProducirP2Año}")
#-----------------------------------------------
print(f"Seguiremos con el producto {Producto3}")
print(f"Las unidades a vender del semestre uno del producto {Producto3} son {UnidadesVenderSem1P3}")
InventarioFinalP3Sem1 = int(input(f"Dime el inventario final del producto {Producto3} del semestre 1: "))
TotalUnidadesSem1P3 = UnidadesVenderSem1P3 + InventarioFinalP3Sem1
print(f"\nEl total de unidades a vender del semestre 1 del producto {Producto3} son {TotalUnidadesSem1P3}")
InventarioInicialP3Sem1 = int(input(f"Dime el Inventario Inicial del producto {Producto3} para el semestre 1: "))
UnidadesProducirP3Sem1 = TotalUnidadesSem1P3 - InventarioInicialP3Sem1
print(f"Las unidades a producir del {Producto3} en el semestre 1 son {UnidadesProducirP3Sem1}")

print(f"\nSeguiremos con el segundo semestre del {Producto3}")
print(f"Las unidades a vender del semestre dos del producto {Producto3} son {UnidadesVenderSem2P3}")
InventarioFinalP3Sem2 = int(input(f"Dime el inventario final del producto {Producto3} del semestre 2: "))
TotalUnidadesSem2P3 = UnidadesVenderSem2P3 + InventarioFinalP3Sem2
print(f"\nEl total de unidades a vender del semestre 2 del producto {Producto3} son {TotalUnidadesSem2P3}")
InventarioInicialP3Sem2 = int(input(f"Dime el Inventario Inicial del producto {Producto3} para el semestre 2: "))
UnidadesProducirP3Sem2 = TotalUnidadesSem2P3 - InventarioInicialP3Sem2
print(f"Las unidades a producir del {Producto3} en el semestre 2 son {UnidadesProducirP3Sem2}")

print(f"Ahora haremos los calculos para el siguiente año del {Producto3}")
UnidadesVenderAñoP3 = UnidadesVenderSem1P3 + UnidadesVenderSem2P3
print(f"Las unidades a vender para el siguiente año del producto {Producto3} son {UnidadesVenderAñoP3}")
InventarioFinalAñoP3 = InventarioFinalP3Sem2
print(f"El inventario fina para el siguiente año del producto {Producto3} son {InventarioFinalAñoP3}")
TotalUnidadesAñoP3 = UnidadesVenderAñoP3 + InventarioFinalAñoP3
print(f"El total de unidades a vender del producto {Producto3} son {TotalUnidadesAñoP3}")
InventarioInicialP3Año = InventarioInicialP3Sem1
print(f"El inventario inicial del año del producto {Producto3} es {InventarioFinalAñoP3}")
UnidadesProducirP3Año = TotalUnidadesAñoP3 - InventarioFinalAñoP3
print(f"Las unidades a producir para el año del producto {Producto3} son {UnidadesProducirP3Año}")

#-------------------------------------------------------------------------------------------------------------------------------------

print(f"\n4. Presupuesto de requerimiento de materiales")
material1 = input(f"\nDime el nombre del primer material")
material2 = input("Dime el nombre del segundo material")
material3 = input("Dime el nombre del tercer material")
#--------Producto 1 Material 1
Material1P1Sem1 = int(input(f"\nDime la cantidad de {material1} que el {Producto1} va a necesitar en el semestre 1: "))
MaterialT1P1Sem1 = Material1P1Sem1 * UnidadesProducirP1Sem1
print(f"La cantidad de material total de {material1} que va a necesitar en el semestre 1 para el producto {Producto1} es {MaterialT1P1Sem1}")

Material1P1Sem2 = int(input(f"\nDime la cantidad de {material1} que el {Producto1} va a necesitar en el semestre 2: "))
MaterialT1P1Sem2 = Material1P1Sem2 * UnidadesProducirP1Sem2
print(f"La cantidad de material total de {material1} que va a necesitar en el semestre 2 para el producto {Producto1} es {MaterialT1P1Sem2}")

MaterialT1P1Año = MaterialT1P1Sem1 + MaterialT1P1Sem2
print(f"La cantidad de material total de {material1} que va a necesitar en el año para el producto {Producto1} es {MaterialT1P1Año}")
#--------Producto 1 Material 2
Material2P1Sem1 = int(input(f"\nDime la cantidad de {material2} que el {Producto1} va a necesitar en el semestre 1: "))
MaterialT2P1Sem1 = Material2P1Sem1 * UnidadesProducirP1Sem1
print(f"La cantidad de material total de {material2} que va a necesitar en el semestre 1 para el producto {Producto1} es {MaterialT2P1Sem1}")

Material2P1Sem2 = int(input(f"\nDime la cantidad de {material2} que el {Producto1} va a necesitar en el semestre 2: "))
MaterialT2P1Sem2 = Material2P1Sem2 * UnidadesProducirP1Sem2
print(f"La cantidad de material total de {material2} que va a necesitar en el semestre 2 para el producto {Producto1} es {MaterialT2P1Sem2}")

MaterialT2P1Año = MaterialT2P1Sem1 + MaterialT2P1Sem2
print(f"La cantidad de material total de {material2} que va a necesitar en el año para el producto {Producto1} es {MaterialT2P1Año}")
#--------Producto 1 Material 3
Material3P1Sem1 = int(input(f"\nDime la cantidad de {material3} que el {Producto1} va a necesitar en el semestre 1: "))
MaterialT3P1Sem1 = Material3P1Sem1 * UnidadesProducirP1Sem1
print(f"La cantidad de material total de {material3} que va a necesitar en el semestre 1 para el producto {Producto1} es {MaterialT3P1Sem1}")

Material3P1Sem2 = int(input(f"\nDime la cantidad de {material3} que el {Producto1} va a necesitar en el semestre 2: "))
MaterialT3P1Sem2 = Material3P1Sem2 * UnidadesProducirP1Sem2
print(f"La cantidad de material total de {material3} que va a necesitar en el semestre 2 para el producto {Producto1} es {MaterialT3P1Sem2}")

MaterialT3P1Año = MaterialT3P1Sem1 + MaterialT3P1Sem2
print(f"La cantidad de material total de {material3} que va a necesitar en el año para el producto {Producto1} es {MaterialT3P1Año}")
#--------Producto 2 Material 1
Material1P2Sem1 = int(input(f"\nDime la cantidad de {material1} que el {Producto2} va a necesitar en el semestre 1: "))
MaterialT1P2Sem1 = Material1P2Sem1 * UnidadesProducirP2Sem1
print(f"La cantidad de material total de {material1} que va a necesitar en el semestre 1 para el producto {Producto2} es {MaterialT1P2Sem1}")

Material1P2Sem2 = int(input(f"\nDime la cantidad de {material1} que el {Producto2} va a necesitar en el semestre 2: "))
MaterialT1P2Sem2 = Material1P2Sem2 * UnidadesProducirP2Sem2
print(f"La cantidad de material total de {material1} que va a necesitar en el semestre 2 para el producto {Producto2} es {MaterialT1P2Sem2}")

MaterialT1P2Año = MaterialT1P2Sem1 + MaterialT1P2Sem2
print(f"La cantidad de material total de {material1} que va a necesitar en el año para el producto {Producto2} es {MaterialT1P2Año}")
#--------Producto 2 Material 2
Material2P2Sem1 = int(input(f"\nDime la cantidad de {material2} que el {Producto2} va a necesitar en el semestre 1: "))
MaterialT2P2Sem1 = Material2P2Sem1 * UnidadesProducirP2Sem1
print(f"La cantidad de material total de {material2} que va a necesitar en el semestre 1 para el producto {Producto2} es {MaterialT2P2Sem1}")

Material2P2Sem2 = int(input(f"\nDime la cantidad de {material2} que el {Producto2} va a necesitar en el semestre 2: "))
MaterialT2P2Sem2 = Material2P2Sem2 * UnidadesProducirP2Sem2
print(f"La cantidad de material total de {material2} que va a necesitar en el semestre 2 para el producto {Producto2} es {MaterialT2P2Sem2}")

MaterialT2P2Año = MaterialT2P2Sem1 + MaterialT2P2Sem2
print(f"La cantidad de material total de {material2} que va a necesitar en el año para el producto {Producto2} es {MaterialT2P2Año}")
#--------Producto 2 Material 3
Material3P2Sem1 = int(input(f"\nDime la cantidad de {material3} que el {Producto2} va a necesitar en el semestre 1: "))
MaterialT3P2Sem1 = Material3P2Sem1 * UnidadesProducirP2Sem1
print(f"La cantidad de material total de {material3} que va a necesitar en el semestre 1 para el producto {Producto2} es {MaterialT3P2Sem1}")

Material3P2Sem2 = int(input(f"\nDime la cantidad de {material3} que el {Producto2} va a necesitar en el semestre 2: "))
MaterialT3P2Sem2 = Material3P2Sem2 * UnidadesProducirP2Sem2
print(f"La cantidad de material total de {material3} que va a necesitar en el semestre 2 para el producto {Producto2} es {MaterialT3P2Sem2}")

MaterialT3P2Año = MaterialT3P2Sem1 + MaterialT3P2Sem2
print(f"La cantidad de material total de {material3} que va a necesitar en el año para el producto {Producto2} es {MaterialT3P2Año}")

#--------Producto 3 Material 1
Material1P3Sem1 = int(input(f"\nDime la cantidad de {material1} que el {Producto3} va a necesitar en el semestre 1: "))
MaterialT1P3Sem1 = Material1P3Sem1 * UnidadesProducirP3Sem1
print(f"La cantidad de material total de {material1} que va a necesitar en el semestre 1 para el producto {Producto3} es {MaterialT1P3Sem1}")

Material1P3Sem2 = int(input(f"\nDime la cantidad de {material1} que el {Producto3} va a necesitar en el semestre 2: "))
MaterialT1P3Sem2 = Material1P3Sem2 * UnidadesProducirP3Sem2
print(f"La cantidad de material total de {material1} que va a necesitar en el semestre 2 para el producto {Producto3} es {MaterialT1P3Sem2}")

MaterialT1P3Año = MaterialT1P3Sem1 + MaterialT1P3Sem2
print(f"La cantidad de material total de {material1} que va a necesitar en el año para el producto {Producto3} es {MaterialT1P3Año}")
#--------Producto 3 Material 2
Material2P3Sem1 = int(input(f"\nDime la cantidad de {material2} que el {Producto3} va a necesitar en el semestre 1: "))
MaterialT2P3Sem1 = Material2P3Sem1 * UnidadesProducirP3Sem1
print(f"La cantidad de material total de {material2} que va a necesitar en el semestre 1 para el producto {Producto3} es {MaterialT2P3Sem1}")

Material2P3Sem2 = int(input(f"\nDime la cantidad de {material2} que el {Producto3} va a necesitar en el semestre 2: "))
MaterialT2P3Sem2 = Material2P3Sem2 * UnidadesProducirP3Sem2
print(f"La cantidad de material total de {material2} que va a necesitar en el semestre 2 para el producto {Producto3} es {MaterialT2P3Sem2}")

MaterialT2P3Año = MaterialT2P3Sem1 + MaterialT2P3Sem2
print(f"La cantidad de material total de {material2} que va a necesitar en el año para el producto {Producto3} es {MaterialT2P3Año}")
#--------Producto 3 Material 3
Material3P3Sem1 = int(input(f"\nDime la cantidad de {material3} que el {Producto3} va a necesitar en el semestre 1: "))
MaterialT3P3Sem1 = Material3P3Sem1 * UnidadesProducirP3Sem1
print(f"La cantidad de material total de {material3} que va a necesitar en el semestre 1 para el producto {Producto1} es {MaterialT3P3Sem1}")

Material3P3Sem2 = int(input(f"\nDime la cantidad de {material3} que el {Producto3} va a necesitar en el semestre 2: "))
MaterialT3P3Sem2 = Material3P3Sem2 * UnidadesProducirP3Sem2
print(f"La cantidad de material total de {material3} que va a necesitar en el semestre 2 para el producto {Producto3} es {MaterialT3P3Sem2}")

MaterialT3P3Año = MaterialT3P3Sem1 + MaterialT3P3Sem2
print(f"La cantidad de material total de {material3} que va a necesitar en el año para el producto {Producto3} es {MaterialT3P3Año}")
#--------Total de requerimiento
TotalRequerimientoMaterial1Sem1 = MaterialT1P1Año + MaterialT1P2Año + MaterialT1P3Año
TotalRequerimientoMaterial1Sem2 = MaterialT1P1Año + MaterialT1P2Año + MaterialT1P3Año
TotalRequerimientoMaterial1Año = MaterialT1P1Año + MaterialT1P2Año + MaterialT1P3Año

TotalRequerimientoMaterial2Sem1 = MaterialT2P1Año + MaterialT2P2Año + MaterialT2P3Año
TotalRequerimientoMaterial2Sem2 = MaterialT2P1Año + MaterialT2P2Año + MaterialT2P3Año
TotalRequerimientoMaterial2Año = MaterialT2P1Año + MaterialT2P2Año + MaterialT2P3Año

TotalRequerimientoMaterial3Sem1 = MaterialT3P1Año + MaterialT3P2Año + MaterialT3P3Año
TotalRequerimientoMaterial3Sem2 = MaterialT3P1Año + MaterialT3P2Año + MaterialT3P3Año
TotalRequerimientoMaterial3Año = MaterialT3P1Año + MaterialT3P2Año + MaterialT3P3Año
print(f"\nTOTAL REQUERIMIENTO")
print(f"El total de material {material1} requerido en el semestre 1 es {TotalRequerimientoMaterial1Sem1}")
print(f"El total de material {material1} requerido en el semestre 2 es {TotalRequerimientoMaterial1Sem2}")
print(f"El total de material {material1} requerido en el año es {TotalRequerimientoMaterial1Año}")
print(f"El total de material {material2} requerido en el semestre 1 es {TotalRequerimientoMaterial2Sem1}")
print(f"El total de material {material2} requerido en el semestre 2 es {TotalRequerimientoMaterial2Sem2}")
print(f"El total de material {material2} requerido en el año es {TotalRequerimientoMaterial2Año}")
print(f"El total de material {material3} requerido en el semestre 1 es {TotalRequerimientoMaterial3Sem1}")
print(f"El total de material {material3} requerido en el semestre 2 es {TotalRequerimientoMaterial3Sem2}")
print(f"El total de material {material3} requerido en el año es {TotalRequerimientoMaterial3Año}")

#------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n5. Presupuesto de Compra de materiales")
#----Material 1
print(f"\nEmpezaremos con el material {material1}")
print(f"El total de material {material1} requerido en el semestre 1 es {TotalRequerimientoMaterial1Sem1}")
InventarioFinalM1Sem1 = int(input(f"Dime del {material1} el inventario final en el semestre 1: "))
TotalMateriales1Sem1 = TotalRequerimientoMaterial1Sem1 + InventarioFinalM1Sem1
print(f"\nEl total de materiales es {TotalMateriales1Sem1}")
InventarioInicialM1Sem1 = int(input(F"Dime del {material1} el inventario inicial del semestre 1: "))
MaterialAComprar1Sem1 = TotalMateriales1Sem1 - InventarioInicialM1Sem1
print(f"\nLos materiales a comprar del material {material1} para el semestre 1 son {MaterialAComprar1Sem1}")
PrecioCompraM1Sem1 = float(input(f"Dime el precio de compra del material {material1} para el semestre 1: "))
TotalMaterial1Sem1Pesos = MaterialAComprar1Sem1 * PrecioCompraM1Sem1
print(f"\nEl precio total del material {material1} en pesos es ${TotalMaterial1Sem1Pesos}")
#----Semestre 2
print(f"\nSeguiremos con el material {material1} Semestre 2")
print(f"El total de material {material1} requerido en el semestre 2 es {TotalRequerimientoMaterial1Sem2}")
InventarioFinalM1Sem2 = int(input(f"Dime del {material1} el inventario final en el semestre 2: "))
TotalMateriales1Sem2 = TotalRequerimientoMaterial1Sem2 + InventarioFinalM1Sem2
print(f"\nEl total de materiales es {TotalMateriales1Sem2}")
InventarioInicialM1Sem2 = InventarioFinalM1Sem1
MaterialAComprar1Sem2 = TotalMateriales1Sem2 - InventarioInicialM1Sem2
print(f"\nLos materiales a comprar del material {material1} para el semestre 2 son {MaterialAComprar1Sem2}")
PrecioCompraM1Sem2 = float(input(f"Dime el precio de compra del material {material1} para el semestre 2: "))
TotalMaterial1Sem2Pesos = MaterialAComprar1Sem2 * PrecioCompraM1Sem2
print(f"\nEl precio total del material {material1} en pesos es ${TotalMaterial1Sem2Pesos}")
#----Año
print(f"\nSeguiremos con el material {material1} Total año")
TotalMaterial1AñoPesos = TotalMaterial1Sem1Pesos + TotalMaterial1Sem2Pesos
print(f"El total que se debe pagar por el material {material1} al año en pesos es ${TotalMaterial1AñoPesos}")

#----Material 2
#----Semestre  1
print(f"\nEmpezaremos con el material {material2}")
print(f"El total de material {material2} requerido en el semestre 1 es {TotalRequerimientoMaterial2Sem1}")
InventarioFinalM2Sem1 = int(input(f"Dime del {material2} el inventario final en el semestre 1: "))
TotalMateriales2Sem1 = TotalRequerimientoMaterial2Sem1 + InventarioFinalM2Sem1
print(f"\nEl total de materiales es {TotalMateriales2Sem1}")
InventarioInicialM2Sem1 = int(input(F"Dime del {material2} el inventario inicial del semestre 1: "))
MaterialAComprar2Sem1 = TotalMateriales2Sem1 - InventarioInicialM2Sem1
print(f"\nLos materiales a comprar del material {material2} para el semestre 1 son {MaterialAComprar2Sem1}")
PrecioCompraM2Sem1 = float(input(f"Dime el precio de compra del material {material2} para el semestre 1: "))
TotalMaterial2Sem1Pesos = MaterialAComprar2Sem1 * PrecioCompraM2Sem1
print(f"\nEl precio total del material {material2} en pesos es ${TotalMaterial2Sem1Pesos}")
#----Semestre 2
print(f"\nSeguiremos con el material {material2} Semestre 2")
print(f"El total de material {material2} requerido en el semestre 2 es {TotalRequerimientoMaterial2Sem2}")
InventarioFinalM2Sem2 = int(input(f"Dime del {material2} el inventario final en el semestre 2: "))
TotalMateriales2Sem2 = TotalRequerimientoMaterial2Sem2 + InventarioFinalM2Sem2
print(f"\nEl total de materiales es {TotalMateriales2Sem2}")
InventarioInicialM2Sem2 = InventarioFinalM2Sem1
MaterialAComprar2Sem2 = TotalMateriales2Sem2 - InventarioInicialM2Sem2
print(f"\nLos materiales a comprar del material {material2} para el semestre 2 son {MaterialAComprar2Sem2}")
PrecioCompraM2Sem2 = float(input(f"Dime el precio de compra del material {material2} para el semestre 2: "))
TotalMaterial2Sem2Pesos = MaterialAComprar2Sem2 * PrecioCompraM2Sem2
print(f"\nEl precio total del material {material2} en pesos es ${TotalMaterial2Sem2Pesos}")
#----Año
print(f"\nSeguiremos con el material {material2} Total año")
TotalMaterial2AñoPesos = TotalMaterial2Sem1Pesos + TotalMaterial2Sem2Pesos
print(f"El total que se debe pagar por el material {material2} al año en pesos es ${TotalMaterial2AñoPesos}")

#----Material 3
#----Semestre  1
print(f"\nEmpezaremos con el material {material3}")
print(f"El total de material {material3} requerido en el semestre 1 es {TotalRequerimientoMaterial3Sem1}")
InventarioFinalM3Sem1 = int(input(f"Dime del {material3} el inventario final en el semestre 1: "))
TotalMateriales3Sem1 = TotalRequerimientoMaterial3Sem1 + InventarioFinalM3Sem1
print(f"\nEl total de materiales es {TotalMateriales3Sem1}")
InventarioInicialM3Sem1 = int(input(F"Dime del {material3} el inventario inicial del semestre 1: "))
MaterialAComprar3Sem1 = TotalMateriales3Sem1 - InventarioInicialM3Sem1
print(f"\nLos materiales a comprar del material {material3} para el semestre 1 son {MaterialAComprar3Sem1}")
PrecioCompraM3Sem1 = float(input(f"Dime el precio de compra del material {material3} para el semestre 1: "))
TotalMaterial3Sem1Pesos = MaterialAComprar3Sem1 * PrecioCompraM3Sem1
print(f"\nEl precio total del material {material3} en pesos es ${TotalMaterial3Sem1Pesos}")
#----Semestre 2
print(f"\nSeguiremos con el material {material3} Semestre 2")
print(f"El total de material {material3} requerido en el semestre 2 es {TotalRequerimientoMaterial3Sem2}")
InventarioFinalM3Sem2 = int(input(f"Dime del {material3} el inventario final en el semestre 2: "))
TotalMateriales3Sem2 = TotalRequerimientoMaterial3Sem2 + InventarioFinalM3Sem2
print(f"\nEl total de materiales es {TotalMateriales3Sem2}")
InventarioInicialM3Sem2 = InventarioFinalM3Sem1
MaterialAComprar3Sem2 = TotalMateriales3Sem2 - InventarioInicialM3Sem2
print(f"\nLos materiales a comprar del material {material3} para el semestre 2 son {MaterialAComprar3Sem2}")
PrecioCompraM3Sem2 = float(input(f"Dime el precio de compra del material {material3} para el semestre 2: "))
TotalMaterial3Sem2Pesos = MaterialAComprar3Sem2 * PrecioCompraM3Sem2
print(f"\nEl precio total del material {material3} en pesos es ${TotalMaterial3Sem2Pesos}")
#----Año
print(f"\nSeguiremos con el material {material3} Total año")
TotalMaterial3AñoPesos = TotalMaterial3Sem1Pesos + TotalMaterial3Sem2Pesos
print(f"El total que se debe pagar por el material {material3} al año en pesos es ${TotalMaterial3AñoPesos}")

print(f"\n***COMPRAS TOTALES***")
ComprasTotalesSem1 = TotalMaterial1Sem1Pesos + TotalMaterial2Sem1Pesos + TotalMaterial3Sem1Pesos
ComprasTotalesSem2 = TotalMaterial1Sem2Pesos + TotalMaterial2Sem2Pesos + TotalMaterial3Sem2Pesos
ComprasTotalesAño = TotalMaterial1AñoPesos + TotalMaterial2AñoPesos + TotalMaterial3AñoPesos

print(f"Las compras totales en el semestre 1 fueron de ${ComprasTotalesSem1}")
print(f"Las compras totales en el semestre 2 fueron de ${ComprasTotalesSem2}")
print(f"Las compras totales en el año fueron de ${ComprasTotalesAño}")

#--------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n6. Determinacion del saldo de proveedores y saldo de salidas")
SaldoProveedoresAñoPasado = int(input("Dime el saldo de tus proveedores del año pasado: "))
print(f"Tus compras para el siguiente año son {ComprasTotalesAño}")
TotalProveedoresAño = SaldoProveedoresAñoPasado + ComprasTotalesAño
print(f"Tus total de proveedores para el siguiente año es {TotalProveedoresAño}")

PorcentajePorProveedoresAñoPasado = int(input("Dime el porcentaje que le vas a pagar a tus proveedores: "))
PorProveedoresAñoPasado1 = SaldoProveedoresAñoPasado - (SaldoProveedoresAñoPasado * (PorcentajePorProveedoresAñoPasado * 0.01))
PorProveedoresAñoPasado = SaldoProveedoresAñoPasado - PorProveedoresAñoPasado1

PorcentajePorProveedoresAñoNuevo = int(input("Dime el porcentaje que vas a pagar a tus proveedores en el siguiente año: "))
PorProveedoresAñoNuevo1 = ComprasTotalesAño - (ComprasTotalesAño * (PorcentajePorProveedoresAñoNuevo * 0.01))
PorProveedoresAñoNuevo = ComprasTotalesAño - PorProveedoresAñoNuevo1

TotalSalidasAñoNuevo = PorProveedoresAñoNuevo + PorProveedoresAñoPasado
print(f"El total de salidas para este nuevo año es {TotalSalidasAñoNuevo}")

SaldoProveedoresAñoNuevo = TotalProveedoresAño - TotalSalidasAñoNuevo
print(f"El total del saldo para tus proveedores en el año es {SaldoProveedoresAñoNuevo}")

#-------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n7. Presupuesto de mano de obra")

print(f"\nEmpezaremos con el producto {Producto1}")
horasP1 = int(input(f"Dime cuantas horas tarda el {Producto1} en fabricar: "))
HorasRequeridasP1Sem1 = UnidadesProducirP1Sem1 * horasP1
HorasRequeridasP1Sem2 = UnidadesProducirP1Sem2 * horasP1
HorasRequeridasP1Año = UnidadesProducirP1Año * horasP1

print(f"\nEl total de horas requeridas para el producto {Producto1} en el semestre 1 es de {HorasRequeridasP1Sem1} horas")
print(f"El total de horas requeridas para el producto {Producto1} en el semestre 2 es de {HorasRequeridasP1Sem2} horas")
print(f"El total de horas requeridas para el producto {Producto1} en el año es de {HorasRequeridasP1Año} horas")

CuotaP1Sem1 = float(input(f"\nDime la cuota por hora del {Producto1} para su fabricacion en el semestre 1: "))
CuotaP1Sem2 = float(input(f"Dime la cuota por hora del {Producto1} para su fabricacion en el semestre 2: "))

ImporteMODP1Sem1 = HorasRequeridasP1Sem1 * CuotaP1Sem1
ImporteMODP1Sem2 = HorasRequeridasP1Sem2 * CuotaP1Sem2
ImporteMODP1Año = ImporteMODP1Sem1 + ImporteMODP1Sem2

print(f"\nEl total a pagar en el semestre 1 por el producto {Producto1} es de {ImporteMODP1Sem1}")
print(f"El total a pagar en el semestre 2 por el producto {Producto1} es de {ImporteMODP1Sem2}")
print(f"El total a pagar en el año por el producto {Producto1} es de {ImporteMODP1Año}")
#-------------------------------------------
print(f"\nSeguiremos con el {Producto2}")
horasP2 = int(input(f"Dime cuantas horas tarda el {Producto2} en fabricar: "))
HorasRequeridasP2Sem1 = UnidadesProducirP2Sem1 * horasP2
HorasRequeridasP2Sem2 = UnidadesProducirP2Sem2 * horasP2
HorasRequeridasP2Año = UnidadesProducirP2Año * horasP2

print(f"\nEl total de horas requeridas para el producto {Producto2} en el semestre 1 es de {HorasRequeridasP2Sem1} horas")
print(f"El total de horas requeridas para el producto {Producto2} en el semestre 2 es de {HorasRequeridasP2Sem2} horas")
print(f"El total de horas requeridas para el producto {Producto2} en el año es de {HorasRequeridasP2Año} horas")

CuotaP2Sem1 = CuotaP1Sem1
CuotaP2Sem2 = CuotaP1Sem2

ImporteMODP2Sem1 = HorasRequeridasP2Sem1 * CuotaP2Sem1
ImporteMODP2Sem2 = HorasRequeridasP2Sem2 * CuotaP2Sem2
ImporteMODP2Año = ImporteMODP2Sem1 + ImporteMODP2Sem2

print(f"\nEl total a pagar en el semestre 1 por el producto {Producto2} es de {ImporteMODP2Sem1}")
print(f"El total a pagar en el semestre 2 por el producto {Producto2} es de {ImporteMODP2Sem2}")
print(f"El total a pagar en el año por el producto {Producto2} es de {ImporteMODP2Año}")
#-------------------------------------------
print(f"\nSeguiremos con el {Producto3}")
horasP3 = int(input(f"Dime cuantas horas tarda el {Producto3} en fabricar: "))
HorasRequeridasP3Sem1 = UnidadesProducirP3Sem1 * horasP3
HorasRequeridasP3Sem2 = UnidadesProducirP3Sem2 * horasP3
HorasRequeridasP3Año = UnidadesProducirP3Año * horasP3

print(f"\nEl total de horas requeridas para el producto {Producto3} en el semestre 1 es de {HorasRequeridasP3Sem1} horas")
print(f"El total de horas requeridas para el producto {Producto3} en el semestre 2 es de {HorasRequeridasP3Sem2} horas")
print(f"El total de horas requeridas para el producto {Producto3} en el año es de {HorasRequeridasP3Año} horas")

CuotaP3Sem1 = CuotaP1Sem1
CuotaP3Sem2 = CuotaP1Sem2

ImporteMODP3Sem1 = HorasRequeridasP3Sem1 * CuotaP3Sem1
ImporteMODP3Sem2 = HorasRequeridasP3Sem2 * CuotaP3Sem2
ImporteMODP3Año = ImporteMODP3Sem1 + ImporteMODP3Sem2

print(f"\nEl total a pagar en el semestre 1 por el producto {Producto3} es de {ImporteMODP3Sem1}")
print(f"El total a pagar en el semestre 2 por el producto {Producto3} es de {ImporteMODP3Sem2}")
print(f"El total a pagar en el año por el producto {Producto3} es de {ImporteMODP3Año}")

print(f"\nTotal de horas MOD")
TotalHorasMODSem1 = HorasRequeridasP1Sem1 + HorasRequeridasP2Sem1 + HorasRequeridasP3Sem1
TotalHorasMODSem2 = HorasRequeridasP1Sem2 + HorasRequeridasP2Sem2 + HorasRequeridasP3Sem2
TotalHorasMODAño = HorasRequeridasP1Año + HorasRequeridasP2Año + HorasRequeridasP3Año

print(f"\nTotal importe de horas MOD")
TotalImporteHorasMODSem1 = ImporteMODP1Sem1 + ImporteMODP2Sem1 + ImporteMODP3Sem1
TotalImporteHorasMODSem2 = ImporteMODP1Sem2 + ImporteMODP2Sem2 + ImporteMODP3Sem2
TotalImporteHorasMODAño = ImporteMODP1Año + ImporteMODP2Año + ImporteMODP3Año

print(f"El importe MOD total del semestre 1 fue de {TotalImporteHorasMODSem1}")
print(f"El importe MOD total del semestre 2 fue de {TotalImporteHorasMODSem2}")
print(f"El importe MOD total en el año fue de {TotalImporteHorasMODAño}")

#------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n8. Presupuesto de gastos indirectos de fabricacion")

depreciacionP8 = float(input(f"\nDime la depreciacion anual: "))
seguros = float(input("Dime cuanto pagas por seguros: "))
MantenimientoSem1 = float(input("Dime cuanto pagas por mantenimiento en el semestre 1: "))
MantenimientoSem2 = float(input("Dime cuanto pagas por mantenimiento en el semestre 2: "))
EnergeticosSem1 = float(input("Dime cuanto pagas por energia en el semestre 1: "))
EnergeticosSem2 = float(input("Dime cuanto pagas por energia en el semestre 2: "))
Varios = float(input("Dime cuanto pagas de varios: "))

TotalGIFSem1 = MantenimientoSem1 + EnergeticosSem1 + (depreciacionP8 / 2) + (seguros / 2) + (Varios / 2)
TotalGIFSem2 = MantenimientoSem2 + EnergeticosSem2 + (depreciacionP8 / 2) + (seguros / 2) + (Varios / 2)
TotalGIFAño = MantenimientoSem1 + MantenimientoSem2 + EnergeticosSem1 + EnergeticosSem2 + depreciacionP8 + seguros + Varios

print(f"\nEl total de G.I.F en el semestre 1 fue de {TotalGIFSem1}")
print(f"El total de G.I.F en el semestre 2 fue de {TotalGIFSem2}")
print(f"El total de G.I.F. en el año fue de {TotalGIFAño}")

CostoDeHoraGIF = TotalGIFAño / TotalHorasMODAño
print(f"\nEl total del costo de horas G.I.F. por año es de {CostoDeHoraGIF}")

#-------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n9. Presupuesto de gastos de operacion")

depreciacionP9 = float(input(f"\nDime la depreciacion anual: "))
SueldosYSalarios = float(input("Dime cuanto pagas por Sueldos y salarios: "))
PorcentajeVentasProyectadas = int(input("Dime el porcentaje para las ventas proyectadas: "))
ComisionesSem1 = TotalVentasSem1 - (TotalVentasSem1 * (PorcentajeVentasProyectadas * 0.01))
ComisionesSem2 = TotalVentasSem2 - (TotalVentasSem2 * (PorcentajeVentasProyectadas * 0.01))
InteresPorObligacion = float(input("Dime cuanto pagas por Intereses por obligacion: "))
VariosSem1 = float(input("Dime cuanto pagas de varios en el semestre 1: "))
VariosSem2 = float(input("Dime cuanto pagas de varios en el semestre 2: "))

print(f"\n***TOTAL GASTOS DE OPERACION***")
TotalGastosOperacionSem1 = (depreciacionP9 / 2) + (SueldosYSalarios / 2) + ComisionesSem1 + (InteresPorObligacion  / 2) + VariosSem1
TotalGastosOperacionSem2 = (depreciacionP9 / 2) + (SueldosYSalarios / 2) + ComisionesSem2 + (InteresPorObligacion  / 2) + VariosSem2
TotalGastosOperacionAño = depreciacionP9 + SueldosYSalarios + ComisionesSem1 + ComisionesSem2 + InteresPorObligacion + VariosSem1 + VariosSem2

print(f"El total de gastos de operacion en el semestre 1 fue de {TotalGastosOperacionSem1}")
print(f"El total de gastos de operacion en el semestre 2 fue de {TotalGastosOperacionSem2}")
print(f"El total de gastos de operacion en el año fue de {TotalGastosOperacionAño}")

#-------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n10. Determinacion del costo unitario de materiales terminados")

print(f"\nUsaremos el producto {Producto1}")
print(f"{material1}, {PrecioCompraM1Sem2}, {Material1P1Sem2}")
print(f"{material2}, {PrecioCompraM2Sem2}, {Material2P1Sem2}")
print(f"{material3}, {PrecioCompraM3Sem2}, {Material3P1Sem2}")
print(f"Mano de obra, {CuotaP1Sem2}, {horasP1}")
print(f"Gastos indirectos de fabricacion, {CostoDeHoraGIF}, {horasP1}")

Material1CostoUnitarioP1 = PrecioCompraM1Sem2 * Material1P1Sem2
Material2CostoUnitarioP1 = PrecioCompraM2Sem2 * Material2P1Sem2
Material3CostoUnitarioP1 = PrecioCompraM3Sem2 * Material3P1Sem2
ManoObraCostoUnitarioP1 = CuotaP1Sem2 * horasP1
GIFP1 = CostoDeHoraGIF * horasP1

CostoUnitarioP1 = Material1CostoUnitarioP1 + Material2CostoUnitarioP1 + Material3CostoUnitarioP1 + ManoObraCostoUnitarioP1 + GIFP1
print(f"\nEl costo Unitario del {Producto1} es un total de {CostoUnitarioP1}")

print(f"\nUsaremos el producto {Producto2}")
print(f"{material1}, {PrecioCompraM1Sem2}, {Material1P2Sem2}")
print(f"{material2}, {PrecioCompraM2Sem2}, {Material2P2Sem2}")
print(f"{material3}, {PrecioCompraM3Sem2}, {Material3P2Sem2}")
print(f"Mano de obra, {CuotaP2Sem2}, {horasP2}")
print(f"Gastos indirectos de fabricacion, {CostoDeHoraGIF}, {horasP2}")

Material1CostoUnitarioP2 = PrecioCompraM1Sem2 * Material1P2Sem2
Material2CostoUnitarioP2 = PrecioCompraM2Sem2 * Material2P2Sem2
Material3CostoUnitarioP2 = PrecioCompraM3Sem2 * Material3P2Sem2
ManoObraCostoUnitarioP2 = CuotaP2Sem2 * horasP2
GIFP2 = CostoDeHoraGIF * horasP2

CostoUnitarioP2 = Material1CostoUnitarioP2 + Material2CostoUnitarioP2 + Material3CostoUnitarioP2 + ManoObraCostoUnitarioP2 + GIFP2
print(f"\nEl costo Unitario del {Producto2} es un total de {CostoUnitarioP2}")

print(f"\nUsaremos el producto {Producto3}")
print(f"{material1}, {PrecioCompraM1Sem2}, {Material1P3Sem2}")
print(f"{material2}, {PrecioCompraM2Sem2}, {Material2P3Sem2}")
print(f"{material3}, {PrecioCompraM3Sem2}, {Material3P3Sem2}")
print(f"Mano de obra, {CuotaP3Sem2}, {horasP3}")
print(f"Gastos indirectos de fabricacion, {CostoDeHoraGIF}, {horasP3}")

Material1CostoUnitarioP3 = PrecioCompraM1Sem2 * Material1P3Sem2
Material2CostoUnitarioP3 = PrecioCompraM2Sem2 * Material2P3Sem2
Material3CostoUnitarioP3 = PrecioCompraM3Sem2 * Material3P3Sem2
ManoObraCostoUnitarioP3 = CuotaP3Sem2 * horasP3
GIFP3 = CostoDeHoraGIF * horasP3

CostoUnitarioP3 = Material1CostoUnitarioP3 + Material2CostoUnitarioP3 + Material3CostoUnitarioP3 + ManoObraCostoUnitarioP3 + GIFP3
print(f"\nEl costo Unitario del {Producto3} es un total de {CostoUnitarioP3}")

#-------------------------------------------------------------------------------------------------------------------------------------------

print(f"\n11. Evaluacion de inventarios finales")

print(f"\nMATERIALES")
print(f"{material1}, {InventarioFinalM1Sem2}, {PrecioCompraM1Sem2}")
CostoTotalM1 = InventarioFinalM1Sem2 * PrecioCompraM1Sem2
print(f"El costo total es {CostoTotalM1}")

print(f"\n{material2}, {InventarioFinalM2Sem2}, {PrecioCompraM2Sem2}")
CostoTotalM2 = InventarioFinalM2Sem2 * PrecioCompraM2Sem2
print(f"El costo total es {CostoTotalM2}")

print(f"\n{material3}, {InventarioFinalM3Sem2}, {PrecioCompraM3Sem2}")
CostoTotalM3 = InventarioFinalM3Sem2 * PrecioCompraM3Sem2
print(f"El costo total es {CostoTotalM3}")

InventarioFinalDeMateriales = CostoTotalM1 + CostoTotalM2 + CostoTotalM3
print(f"\nEl inventario total de materiales es {InventarioFinalDeMateriales}")

print(f"\nPRODUCTOS")
print(f"{Producto1}, {InventarioFinalP1Sem2}, {CostoUnitarioP1}")
CostoTotalP1 = InventarioFinalP1Sem2 * CostoUnitarioP1
print(f"El costo total del producto {Producto1}, es {CostoTotalP1}")

print(f"{Producto2}, {InventarioFinalP2Sem2}, {CostoUnitarioP2}")
CostoTotalP2 = InventarioFinalP2Sem2 * CostoUnitarioP2
print(f"El costo total del producto {Producto2}, es {CostoTotalP2}")

print(f"{Producto3}, {InventarioFinalP3Sem2}, {CostoUnitarioP3}")
CostoTotalP3 = InventarioFinalP3Sem2 * CostoUnitarioP3
print(f"El costo total del producto {Producto3}, es {CostoTotalP3}")

InventarioFinalProductos = CostoTotalP1 + CostoTotalP2 + CostoTotalP3
print(f"\nEl invenatario total de productos es {InventarioFinalProductos}")

print(f"\nPresupuesto Financiero")
print(f"\nEstado de costo de produccion")

SaldoInicialMateriales = float(input(f"\nDime el saldo inicial de materiales: "))
print(f"El total de compras de materiales en el año fue de {ComprasTotalesAño}")
MaterialDisponible = SaldoInicialMateriales + ComprasTotalesAño
print(f"\nEl material disponible es {MaterialDisponible}")
print(f"El inventario final de materiales es {InventarioFinalDeMateriales}")
MaterialesUtilizados = MaterialDisponible - InventarioFinalDeMateriales
print(f"\nLos materiales utilizados fueron {MaterialesUtilizados}")
print(f"El total de mano de obra directa fue {TotalImporteHorasMODAño}")
print(f"El total de gastos indirectos de fabricacion fue {TotalGIFAño}")
CostoProduccion = MaterialesUtilizados + TotalImporteHorasMODAño + TotalGIFAño
print(f"\nEl total de costo de produccion fue {CostoProduccion}")
InventarioFinalDeProductosTerminados = int(input("Dime el inventario final de productos terminados: "))
TotalProduccionDisponible = CostoProduccion + InventarioFinalDeProductosTerminados
print(f"El total de produccion disponible es {TotalProduccionDisponible}")
costoVentas = TotalProduccionDisponible - InventarioFinalProductos
print(f"\nEl costo de ventas es {costoVentas}")
#------------------------------------------------
print(f"\nEstado de resultados")
print(f"\nEl total de ventas es {TotalVentasAño}")
UtilidadBruta = TotalVentasAño - costoVentas
print(f"La utilidad bruta es  {UtilidadBruta}")
print(f"\nEl total de gastos de operacion es {TotalGastosOperacionAño}")
UtilidadOperacion = UtilidadBruta - TotalGastosOperacionAño

ImpuestoSobreRenta = int(input("Dime el ISR actual: "))
Ptu = int(input("Dime el PTU actual: "))

Isr = UtilidadOperacion - (UtilidadOperacion - (UtilidadOperacion * (ImpuestoSobreRenta * .01)))
PTu = UtilidadOperacion - (UtilidadOperacion - (UtilidadOperacion * (Ptu * .01)))

UtilidadNeta = UtilidadOperacion - Isr - PTu
print(f"\nLa utilidad neta es {UtilidadNeta}")
#-----------------------------------------------------------------------
print(f"\nEstado de flujo de efectivo")

SaldoInicialEfectivo = float(input("Dime el saldo inicial de efectivo: "))
print("\nEntrada")
print(f"Tu cobranza del año nuevo es {PorCobrarAñoNuevo} y del año pasado es {PorCobrarAñoPasado}")
print(f"Tu total de cobranza es {TotalCobranza}")
EfectivoDisponible = SaldoInicialEfectivo + TotalCobranza
print(f"Tu efectivo disponible es {EfectivoDisponible}")
print("\nSalidas")
print(f"Tu saldo de proveedores del año pasado es {PorProveedoresAñoPasado} y del año nuevo es {PorProveedoresAñoNuevo}")
print(f"El total de mano de obra directa es {TotalImporteHorasMODAño}")
print(f"Los gastos indirectos de fabricacion son {TotalGIFAño}")
PagoGastosOperacion = TotalGastosOperacionAño - depreciacionP8
print(f"El total de gastos de operacion al año es {PagoGastosOperacion}")
CompraActivo = float(input("Dime la compra de activo fijo (Maquinaria): "))
PagoISRAñoPasado = float(input("Dime cuanto pagaste de ISR del año pasado: "))
PagoISRAñoNuevo = Isr
TotalDeSalidas = PorProveedoresAñoNuevo + PorProveedoresAñoPasado + TotalImporteHorasMODAño + TotalGIFAño + PagoGastosOperacion + CompraActivo + PagoISRAñoNuevo + PagoISRAñoPasado
print(f"\nEl total de salidas fue {TotalDeSalidas}")
FlujoEfectivoActual = EfectivoDisponible - TotalDeSalidas
print(f"El flujo de efectivo disponible es {FlujoEfectivoActual}")
#-------------------------------------------------
print(f"\nBalanceGeneral")
print(f"\nActivos circulantes")
print(f"El flujo de efectivo es {FlujoEfectivoActual}, clientes {SaldoClientesAñoNuevo}, Inventario Materiales {InventarioFinalDeMateriales}")
print(f"Inventario productos {InventarioFinalProductos}")
TotalActivosCirculante = FlujoEfectivoActual + SaldoClientesAñoNuevo + InventarioFinalDeMateriales + InventarioFinalProductos
print(f"El total de activos circulantes es {TotalActivosCirculante}")

print(f"\nActivos No circulante")
Terreno = float(input("Dime cuanto pagas de terreno: "))
PlantaEquipo = float(input("Dime cuanto pagas de planta: "))
PlantaEquipo = PlantaEquipo + CompraActivo
Depreciacion = float(input("Dime la depreciacion que tienes para sumarle las pasadas depreciaciones: "))
Depreciacion = Depreciacion + depreciacionP8 + depreciacionP9

TotalActivosNoCirculante = Terreno + PlantaEquipo - Depreciacion
print(f"\nEl total activos no circulante es {TotalActivosNoCirculante}")
ActivoTotal = TotalActivosNoCirculante + TotalActivosCirculante
print(f"\nEl total de activos es {ActivoTotal}")

print("Pasivos")
print(f"\nPasivo corto plazo")
Proveedores = SaldoProveedoresAñoNuevo
DocumentosPorPagar = float(input("Dime cuanto vas a pagar por documentos por pagar: "))
TotalPasivosCortoPlazo = Proveedores + DocumentosPorPagar + Ptu
print(f"\nLos pasivos a corto plazo tienen un total de {TotalPasivosCortoPlazo}")

print(f"\nPasivo Largo Plazo")
ObligacionesPorPagar = float(input("Dime las obligaciones por pagar: "))
print(f"El total de pasivos largo plazo es {ObligacionesPorPagar}")

TotalPasivos = TotalPasivosCortoPlazo + ObligacionesPorPagar
print(f"\nEl total de pasivos es {TotalPasivos}")

print(f"\nCapital")
CapitalAportado = float(input("Dime el capital aportado: "))
CapitalGanado = float(input("Dime el capital ganado: "))
UtilidadDelEjercicio = UtilidadNeta

CapitalTotal = CapitalAportado + CapitalGanado + UtilidadDelEjercicio
print(f"\nEl capital Total es {CapitalTotal}")

comprobacion = CapitalTotal + TotalPasivos
print(f"\nLa suma de pasivos y capital da {comprobacion}")
print(f"Tus activos sumaron un total de {ActivoTotal}")

