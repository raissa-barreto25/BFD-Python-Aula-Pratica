import pymongo

# cliente = pymongo.MongoClient("mongodb://localhost:27017/")
cliente = pymongo.MongoClient()
print(cliente)


# lojinha = cliente["lojinhadb"]

# users = lojinha["users"]

# doc = {"Nome":"Raíssa", "idade":30, "trabalho":"não tem"}

# #users.insert_one(doc)
# print(users.find_one({"Nome":{"$gt":"Raí"}}))
# users.delete_one({"Nome":"Raíssa"})
# print(users.find_one({"Nome":{"$gt":"Raí"}}))
# #print(cliente.list_database_names())

# #print(cliente)
# Comando - python aulas/aula20.py