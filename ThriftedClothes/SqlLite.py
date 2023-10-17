import sqlite3

# Función para crear la tabla

def create_table(table_name, columns):
    """
    Create a table with the specified columns.

    Parameters:
    table_name (str): The name of the table.
    columns (str): The column definitions in SQL format.

    Example usage:
    create_table('usuarios', 'id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER')
    """
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Construye la consulta SQL dinámicamente
    query = f'CREATE TABLE {table_name} ({columns})'

    # Ejecuta la consulta para crear la tabla
    cursor.execute(query)
    
    conn.commit()
    conn.close()

# Función para insertar datos
def insert_data(table_name, **kwargs):
    """
    Insert data into the specified table.

    Parameters:
    table_name (str): The name of the table.
    kwargs (dict): Column-value pairs to be inserted.

    Example usage:
    insert_data('usuarios', nombre='Alice', edad=30)
    """
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Construye la consulta SQL dinámicamente
    columns = ', '.join(kwargs.keys())
    placeholders = ', '.join('?' for _ in kwargs)
    query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'

def select_data(table_name, columns='*', where=None, join=None, order_by=None, group_by=None):
    """
    Perform a SELECT query on the specified table with optional conditions and joins.

    Parameters:
    table_name (str): The name of the table.
    columns (str): The columns to select (default is '*').
    where (str): The WHERE clause of the query (default is None).
    join (str): The JOIN clause of the query (default is None).
    order_by (str): The ORDER BY clause of the query (default is None).
    group_by (str): The GROUP BY clause of the query (default is None).

    Returns:
    list: A list of rows resulting from the SELECT query.

    Example usage:
    rows = select_data('usuarios', columns='nombre, edad', where='edad > 25', order_by='nombre')
    """
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    # Construye la consulta SQL dinámicamente
    query = f'SELECT {columns} FROM {table_name}'

    if join:
        query += f' {join}'

    if where:
        query += f' WHERE {where}'

    if group_by:
        query += f' GROUP BY {group_by}'

    if order_by:
        query += f' ORDER BY {order_by}'

    # Ejecuta la consulta y obtiene los resultados
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()
    return rows

