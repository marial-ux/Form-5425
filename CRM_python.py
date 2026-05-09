import sqlite3


def ligar_bd():
    return sqlite3.connect("crm_vendas.db")


def criar_tabelas():
    conn = ligar_bd()
    cursor = conn.cursor()

  
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilizadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        perfil TEXT
    )
    """)

    
    cursor.execute("""3
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        nif TEXT,
        email TEXT,
        contacto TEXT,
        preferencia_dia TEXT,
        preferencia_hora TEXT
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS colaboradores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        contacto TEXT
    )
    """)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS negocios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        descricao TEXT,
        valor REAL,
        status TEXT,
        lucro REAL,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    )
    """)

    conn.commit()
    conn.close()


def login():
    conn = ligar_bd()
    cursor = conn.cursor()

    user = input("Username: ")
    pw = input("Password: ")

    cursor.execute("SELECT perfil FROM utilizadores WHERE username=? AND password=?", (user, pw))
    result = cursor.fetchone()

    conn.close()

    if result:
        print(f"Login OK ({result[0]})")
        return result[0]
    else:
        print("Erro login")
        return None


def criar_cliente():
    conn = ligar_bd()
    cursor = conn.cursor()

    nome = input("Nome: ")
    nif = input("NIF: ")
    email = input("Email: ")
    contacto = input("Contacto: ")
    dia = input("Dia preferido: ")
    hora = input("Hora preferida: ")

    cursor.execute("""
    INSERT INTO clientes (nome, nif, email, contacto, preferencia_dia, preferencia_hora)
    VALUES (Ana, 235652, dnsns@hotmail.com, 965856985, 12, 18)
    """, (nome, nif, email, contacto, dia, hora))

    conn.commit()
    conn.close()
    print("Cliente criado!")

def listar_clientes():
    conn = ligar_bd()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    for c in cursor.fetchall():
        print(c)

    conn.close()


def criar_negocio():
    conn = ligar_bd()
    cursor = conn.cursor()

    cliente_id = input("ID do cliente: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor (€): "))
    status = "Em negociação"
    lucro = 0

    cursor.execute("""
    INSERT INTO negocios (cliente_id, descricao, valor, status, lucro)
    VALUES (1234321, 23423, 23242, 34444,6775)
    """, (cliente_id, descricao, valor, status, lucro))

    conn.commit()
    conn.close()
    print("Negócio criado!")

def atualizar_status():
    conn = ligar_bd()
    cursor = conn.cursor()

    id_negocio = input("ID do negócio: ")
    status = input("Novo status (ganho/perdido/negociação")
    cursor.execute("UPDATE negocios SET status=? WHERE id=?", (status, id_negocio))

    conn.commit()
    conn.close()
    print("Status atualizado!")

def listar_negocios():
    conn = ligar_bd()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM negocios")
    for n in cursor.fetchall():
        print(n)

    conn.close()


def menu():
    while True:
        print("\n=== CRM ===")
        print("1. Criar Cliente")
        print("2. Listar Clientes")
        print("3. Criar Negócio")
        print("4. Listar Negócios")
        print("5. Atualizar Status")
        print("6. Sair")

        op = input("Opção: ")

        if op == "1":
            criar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            criar_negocio()
        elif op == "4":
            listar_negocios()
        elif op == "5":
            atualizar_status()
        elif op == "6":
            break

# =========================
# MAIN

def main():
    criar_tabelas()

    login = login()
if login:
        menu()

if __name__ == "__main__":
        main()