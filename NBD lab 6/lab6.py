# - *- coding: utf- 8 - *-

from riak import RiakClient

client = RiakClient(pb_port=8087)
bucket = client.bucket('s26365')

# a) wrzucanie elementu do bazy dokument
new_doc = {
    'firstName': 'John',
    'lastName': 'Elton',
    'age': 27,
    'isEmployed': True
}
key = 'lab06'
bucket.new(key, data=new_doc).store()

# b) pobieranie i wyświetlanie
doc = bucket.get(key)
print(f'Newly created document:\n{doc.data}\n\n')

# c) modyfikacja elementu
doc.data["isEmployed"] = False
doc.store()

# d) poberanie i wyświetlanie
doc_modified = bucket.get(key)
print(f'Modified document:\n{doc_modified.data}\n\n')

# e) usuwanie elementu, następnie próba wyświetlania
doc_modified.delete()

doc_deleted = bucket.get(key)
print(f'Deleted document:\n{doc_deleted.data}')
