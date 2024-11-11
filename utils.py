import MySQLdb

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db = 'pmysql',
            host = 'localhost',
            user = 'bzin',
            passwd = 'bzin',
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro ao conectar ao servidor: {e}')

def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    if len(produtos) > 0:
        print('Listando produtos...')
        print('====================')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Nome: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Quantidade: {produto[3]}')
            print('====================')
    else:
        print('Nenhum produto cadastrado.')
    desconectar(conn)

def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    cursor = conn.cursor()
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))
    estoque = int(input('Digite a quantidade do produto: '))
    cursor.execute(f'INSERT INTO produtos (nome, preco, estoque) VALUES ("{nome}", {preco}, {estoque})')
    conn.commit()
    if cursor.rowcount == 1:
        print(f'Produto {nome} inserido com sucesso.')
    else:
        print('Erro ao inserir produto.')
    desconectar(conn)

def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Digite o ID do produto: '))
    nome = input('Digite o novo nome do produto: ')
    preco = float(input('Digite o novo preço do produto: '))
    estoque = int(input('Digite a nova quantidade em estoque: '))
    cursor.execute(f'UPDATE produtos SET nome = "{nome}", preco = {preco}, estoque = {estoque} WHERE id = {codigo}')
    conn.commit()
    if cursor.rowcount == 1:
        print(f'Produto {codigo} atualizado com sucesso.')
    else:
        print('Erro ao atualizar produto.')
    desconectar(conn)

def deletar():
    """
    Função para deletar um produto
    """  
    conn = conectar()
    cursor = conn.cursor()
    codigo = int(input('Digite o ID do produto: '))
    cursor.execute(f'DELETE FROM produtos WHERE id = {codigo}')
    conn.commit()
    if cursor.rowcount == 1:
        print(f'Produto {codigo} deletado com sucesso.')
    else:
        print('Erro ao deletar produto.')
    desconectar(conn)

def menu():
    """
    Função para gerar o menu inicial
    """
    while True:
        print('=========Gerenciamento de Produtos==============')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print('5 - Sair.')
        print('Selecione uma opção: ')
        
        opcao = int(input())
        
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        elif opcao == 5:
            print("Encerrando o programa.")
            break  # Encerra o loop e o programa
        else:
            print('Opção inválida. Tente novamente.')
