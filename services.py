def getip():
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        iplocal = s.getsockname()[0]

        return iplocal

def getconnection():
    import mysql.connector

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sgdb"
    )

def getproductsequence(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT MAX(code) + 1 FROM PRODUCT")
        result = cursor.fetchone()
        return result[0] if result and result[0] else 1
    finally:
        cursor.close()

def createproduct(conn, name, description, price):
    sql = """
        INSERT INTO PRODUCT (code, name, description, price)
        VALUES (%s, %s, %s, %s)
    """
    code = getproductsequence(conn)
    params = (code, name, description, price)
    cursor = conn.cursor()

    try:
        cursor.execute(sql, params)
        conn.commit()
        return f"Produto com código {code} criado com sucesso!"
    finally:
        cursor.close()

def getproduct(conn, code):
    sql = """
        SELECT * FROM PRODUCT WHERE CODE = %s
    """
    params = [code]
    cursor = conn.cursor()

    try:
        cursor.execute(sql, params)
        result = cursor.fetchall()
        return "\n".join([str(row) for row in result])
    finally:
        cursor.close()

def getallproducts(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM PRODUCT")
        result = cursor.fetchall()
        return "\n".join([str(row) for row in result])
    finally:
        cursor.close()

def deleteproduct(conn, code):
    sql = """
        DELETE FROM PRODUCT WHERE CODE = %s
    """
    params = [code]
    cursor = conn.cursor()

    try:
        cursor.execute(sql, params)
        conn.commit()
        return f"Produto com codigo {code} deletado com sucesso!"
    finally:
        cursor.close()

def updateproduct(conn, code, name, description, price):
    # Usa a conexão para atualizar dados
    sql = """
        UPDATE PRODUCT  SET name = %s, description = %s, price = %s  WHERE code = %s
    """
    params = (name, description, price, code)
    cursor = conn.cursor()

    try:
        cursor.execute(sql, params)
        conn.commit()
        return f"Produto com código {code} atualizado com sucesso!"
    finally:
        cursor.close()

def decodeprotocol(protocol):
    split = protocol.split("//")

    #Criar produto
    if split[0] == "1":
        return createproduct(getconnection(), split[1], split[2], split[3])
    #Deletar produto
    if split[0] == "2":
        return deleteproduct(getconnection(), split[1])
    #Atualizar produto
    if split[0] == "3":
        return updateproduct(getconnection(), split[1], split[2], split[3], split[4])
    #Buscar produto
    if split[0] == "4":
        return getproduct(getconnection(), split[1])
    #Buscar todos os produtos
    if split[0] == "5":
        return getallproducts(getconnection())
