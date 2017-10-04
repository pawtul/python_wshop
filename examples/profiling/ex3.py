def has_item(collection, item):
    found = False
    for i in collection:
        if item == i:
            found = True
    return found


@profile
def main():
    collection = range(10000000)
    print(has_item(collection, 10000000))


main()

