def has_item(collection, item):
    return item in collection


collection = range(10000000)
print(has_item(collection, 10000000))

