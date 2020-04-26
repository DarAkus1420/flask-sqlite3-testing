import backend.server as sv
import backend.data_base as db
import backend.client as clt


if __name__ == "__main__":
	#Creacion db, si gusta puede eliminarla o cambiarle el nombre, el programa seguira funcionando
    db = db.DataBase('db.db')
    sv.db = db
    clientes = []
    #Se crean los clientes
    try:
        clientes.append(clt.Client(1, "Juan", "Temuco", 150000))
        clientes.append(clt.Client(2, "Jose", "Pitrufquen", 500))
        clientes.append(clt.Client(3, "Maria", "Cajon", 23112))
        clientes.append(clt.Client(4, "Ana", "Temuco", 45555))
        clientes.append(clt.Client(5, "Sofia", "Cajon", 56544))
        clientes.append(clt.Client(6, "Pedro", "Temuco", 4564564))
        clientes.append(clt.Client(7, "Vanessa", "Cajon", 4564))
        clientes.append(clt.Client(8, "Victor", "Pitrufquen", 677888))
        clientes.append(clt.Client(9, "Fernando", "Temuco", 666789))
        clientes.append(clt.Client(10, "Francisco", "Temuco", 79979))

        #Se crea la tabla de clientes
        db.create_table("Clientes", clientes[0].to_sql(), clientes[0].extra_param_sql())
        #Se insertan los clientes
        for cliente in clientes:
            db.insert_data(cliente.return_data(), "Clientes")
    except:
        print("No se pueden agregar mas valores")
    

    sv.app.run(debug=True)