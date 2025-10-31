# import pymongo

# cliente = pymongo.MongoClient("mongodb://localhost:27017/")
# cliente = pymongo.MongoClient("mongodb+srv://rrbsiilva_db_user:BE8KKy8Oaqp6DFeW@cluster0.6alfy2x.mongodb.net/?appName=Cluster0")


# lojinha = cliente["lojinhadb"]

# users = lojinha["users"]

# doc = {"Nome":"Raíssa", "idade":30, "trabalho":"não tem"}

# #users.insert_one(doc)
# print(users.find_one({"Nome":{"$gt":"Raí"}}))
# users.delete_one({"Nome":"Raíssa"})
# print(users.find_one({"Nome":{"$gt":"Raí"}}))
# #print(cliente.list_database_names())

# #print(cliente)
import pymongo

cliente = pymongo.MongoClient("mongodb+srv://rrbsiilva_db_user:BE8KKy8Oaqp6DFeW@cluster0.6alfy2x.mongodb.net/?appName=Cluster0")