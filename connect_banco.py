import mysql.connector
from mysql.connector import errorcode

try:
    print("tentando")
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='354555',
        database='dbtasks'
    )

    print("Conectado!")

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)

# cursor = db_connection.cursor(buffered=True)



# query = "INSERT INTO tarefas (Tarefa, Descricao, Dia, Hora, UsuarioId)" \
#         "values(%s,%s,%s,%s,%s);"
#
# cursor.execute(query, (("rezar"), ("falar"), ("cantar"), ("chorar"), ("1")))

# query = "SELECT * FROM `tarefas`" \
#         "where UsuarioId = %s;"
#
# cursor.execute(query, ([1]))
#
# for (TarefasID, Tarefa, Descricao, Dia, Hora, UsuarioId) in cursor:
#     print("TarefasID:{}     Tarefa:{}       Descricao:{}        Dia:{}      Hora:{}     UsuarioId:{}".format(TarefasID, Tarefa, Descricao, Dia, Hora, UsuarioId))


# cursor.close()
# db_connection.commit()


# print("Connection Close!")