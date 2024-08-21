import sqlite3 as sq

date = ''
amount = 0
category = ''
category_deep = ''

connection = sq.connect('finances.db')
cursor = connection.cursor()

finances = '''
CREATE TABLE IF NOT EXISTS finances (
     operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
     date TEXT NO NULL,
     type TEXT NOT NULL,
     amount INTEGER CHECK (amount > 0),
     category TEXT NOT NULL
)
'''

cursor.execute(finances)
connection.commit()

while True:
    date = input('Enter date: ')
    if date == '-1':
        break
    type = input('Type of operation: ')
    amount = int(input('Amount: '))
    category = input('Category: ')
    new_operation = (date, type, amount, category)

    cursor = connection.cursor()
    cursor.execute(finances)
    connection.commit()

    request_to_insert_data = '''
    INSERT INTO finances (date, type, amount, category) VALUES (?, ?, ?, ?);
    '''
    cursor.execute(request_to_insert_data, new_operation)
    connection.commit()

cursor.close()
connection.close()