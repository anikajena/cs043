from lesson06.database import Simpledb

db = Simpledb(‘phonenumbers.txt’)
db.insert(‘relish’, ‘Pickled cucumber and sugar’)
print(db.select_one(‘relish’))