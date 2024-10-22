import os  # Import os for system commands

# Define pizza costs
costo_G = 200  # Cost of large pizza
costo_M = 150  # Cost of medium pizza
costo_C = 100  # Cost of small pizza

ordenes = []  # Initialize an empty list for orders
debug = True  # Debug mode flag

# Try to load existing orders from the file
try:
    f = open("Support Files/pedidos.txt", "r")  # Open the file for reading
    ordenes = eval(f.read())  # Read and evaluate the content as a list
    f.close()
except Exception as err:
    print("Jefe su archivo no existe")  # Inform the user if the file doesn't exist
    if debug:
        print(err)  # Print error details if in debug mode

x = True  # Control variable for the ordering loop
while x:
    os.system("cls")  # Clear the console
    print("Manu´s Pizzeria")  # Print the pizzeria name
    name = input("Mi compaaa bienvenido! \nA nombre de quien sera el pedido:\n>>> ")  # Get customer's name

    # Input validation for the quantity of pizzas
    valid = False
    while not valid:
        try:
            pizzas_qty = int(input("Cuantas pizzas va a llevar?\n>>> "))  # Get the number of pizzas
            valid = True
        except:
            print("Güero vuelva a introducir el numero de pizzas que quiere, no typeo bien")

    # Input validation for the size of pizzas
    valid = False
    while not valid:
        try:
            pizzas_size = int(input("De que tamaño quiere sus pizzas?\n1. Grande\n2. Mediana\n3. Chica\n>>> "))  # Get size choice
            valid = True
        except:
            print("Jefe vuelva el tamaño de pizzas que quiere, no typeo bien")

    # Calculate cost based on size
    if pizzas_size == 1:
        costo = costo_G * pizzas_qty  # Cost for large pizzas
    elif pizzas_size == 2:
        costo = costo_M * pizzas_qty  # Cost for medium pizzas
    elif pizzas_size == 3:
        costo = costo_C * pizzas_qty  # Cost for small pizzas
    else:
        costo = 10  # Default cost (shouldn't happen)

    orden = [name, pizzas_qty, pizzas_size, costo]  # Create order record
    print(f"Su total es: ${costo}")  # Display total cost
    ordenes.append(orden)  # Add the order to the list

    # Prompt for more orders
    i = int(input("Desea ordenar algo mas patron?\n1. Si \n2. No\n>>> "))
    if i == 2:
        x = False  # Exit loop if no more orders
    else:
        x = True

    # Save the orders to the file
    f = open("Support Files/pedidos.txt", "w")
    f.write(str(ordenes))  # Write orders to file
    f.close()

print(ordenes)  # Print all orders
