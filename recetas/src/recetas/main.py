from modelos.base import RecetaError
from modelos.ingrediente import Ingrediente
from modelos.plato import Plato, PlatoGourmet
from modelos.gestor import Gestor

def linea_separadora(titulo=""):
    print(f"\n--- {titulo} ---")

def main():
    print("=== INICIANDO PRUEBAS DEL SISTEMA DE RECETAS ===")

    # ---------------------------------------------------------
    # 1. PRUEBA DE INGREDIENTES
    # ---------------------------------------------------------
    linea_separadora("PRUEBA DE INGREDIENTES")
    
    # Crear ingredientes
    harina = Ingrediente("Harina", 500, "gramos")
    tomate = Ingrediente("Tomate", 3, "unidades")
    queso = Ingrediente("Mozzarella", 200, "gramos")

    # Probar __str__
    print(f"Ingrediente creado: {harina}")
    print(f"Ingrediente creado: {tomate}")

    # Probar igualdad (__eq__)
    harina_2 = Ingrediente("Harina", 100, "kilos")
    print(f"¿Es 'Harina' igual a 'Harina' (otra cantidad)? {harina == harina_2}") 
    print(f"¿Es 'Harina' igual a 'Tomate'? {harina == tomate}")

    # Probar edición y Excepción personalizada
    print("\n> Intentando editar cantidad con valor negativo:")
    try:
        harina.editar_cantidad(-50)
    except RecetaError as e:
        print(f"Excepción capturada correctamente: {e}")

    harina.editar_cantidad(600)
    print(f"Cantidad editada correctamente: {harina}")


    # ---------------------------------------------------------
    # 2. PRUEBA DE GESTOR Y CREACIÓN DE PLATOS
    # ---------------------------------------------------------
    linea_separadora("PRUEBA DE GESTOR Y PLATOS")
    
    mi_gestor = Gestor()

    # Crear un plato válido
    print("> Creando plato válido (Pizza):")
    pizza = mi_gestor.crear_plato("Pizza Margarita", 45)

    # Intentar crear un plato con tiempo inválido (validación estática)
    print("\n> Intentando crear plato con tiempo excesivo (1000 min):")
    try:
        mi_gestor.crear_plato("Banquete Vikingo", 1000)
    except RecetaError as e:
        print(f"Excepción capturada por validación de tiempo: {e}")



    linea_separadora("DETALLES DEL PLATO")

    # Agregar ingredientes
    try:
        pizza.agregar_ingrediente(harina)
        pizza.agregar_ingrediente(tomate)
        pizza.agregar_ingrediente(queso)
        # Intentar agregar algo que no es ingrediente
        pizza.agregar_ingrediente("Sal (String no válido)") 
    except RecetaError as e:
        print(f"Error al agregar ingrediente inválido: {e}")


    pizza.asignar_imagen("http://img.com/pizza.jpg")
    if pizza.imagen:
        print(f"Imagen asignada con URL: {pizza.imagen.url}")

    print(f"Número de ingredientes en la Pizza: {len(pizza)}")

    linea_separadora("PRUEBA DE HERENCIA (GOURMET)")

    risotto = PlatoGourmet("Risotto de Setas", 60, "Gordon Ramsay")
    risotto.agregar_ingrediente(Ingrediente("Arroz Arboreo", 300, "g"))
    

    mi_gestor._catalogo_platos.append(risotto)


    print(f"Info Plato Normal:  {pizza.mostrar_info()}")
    print(f"Info Plato Gourmet: {risotto.mostrar_info()}")


    linea_separadora("BÚSQUEDA EN GESTOR")

    busqueda = mi_gestor.buscar_por_nombre("pizza margarita")
    if busqueda:
        print(f"Plato encontrado: {busqueda.nombre}")
    else:
        print("Plato no encontrado")

    busqueda_fail = mi_gestor.buscar_por_nombre("Hamburguesa")
    if busqueda_fail:
         print(f"Plato encontrado: {busqueda_fail.nombre}")
    else:
        print("Correcto: 'Hamburguesa' no existe en el catálogo.")



if __name__ == "__main__":
    main()

