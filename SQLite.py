import sqlite3

def create_table(name,fields):
    """

    :param name:    str, name of the table
    :param fields:  list, column titles
    :return:
    """
    fields = ", ".join(fields)
    command = f"CREATE TABLE movie({fields})"

    cur.execute(f"CREATE TABLE movie" + command)

def insert_to_table(value):
    """
    insert one row to table
    :param value: list, the desired row
    :return:
    """
    #values = ["'" + v + "'" ]
    values = "('" + "', '".join(value) + "')"


    command = f"""
        INSERT INTO lior VALUES
            {values}
    """
    print(command)

    cur.execute(command)
    con.commit()

def multi_insert_to_table(values):
    """

    :param values: list of lists for
    :return:
    """
    for value in values:
        insert_to_table(value)

