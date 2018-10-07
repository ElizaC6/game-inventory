# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    lista = list(inventory.values())
    lista2 = list(inventory.keys())
    print('Inventory: ')
    for i in range(len(lista)):
        print(lista[i], lista2[i])
    print('total number of items:', sum(inventory.values()))    


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        try:
            inventory[i] += 1
        except KeyError:
            inventory.update({i: 1})
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    temp = len('item name')
    temp1 = len('count')
    a = '-'
    lista = []
    lista2 = []
    l=list(inventory.items())
    if order == "count,asc":
        l = sorted(inventory.items(), key=lambda kv: kv[1])
    elif order == "count,desc":
        l = sorted(inventory.items(), key=lambda kv: kv[1],reverse=True)
    for i in l:
        lista2.append(i[0])
        lista.append(i[1])
    for i in inventory.values():
        if len(str(i)) > temp1:
            temp1 = len(str(i))
    for i in inventory.keys():
        if len(i) > temp:
            temp = len(i)
    print('Inventory: ')
    print(' count', (temp - len('item name')) * ' ', 'item name')
    print(18 * a)
    for i in range(len(lista)):
        print((temp1 - len(str(lista[i]))) * ' ', lista[i], (temp - len(lista2[i])) * ' ', lista2[i])
    print(18 * a)
    print('total number of items:', sum(inventory.values()))






# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    try:
        file = open(filename, "r")
        line=file.readlines()
        list_of_items = line[0].split(',')
        print(list_of_items)
        return add_to_inventory(list_of_items, inventory)
    except FileNotFoundError:
        return inventory




# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    if filename == None:
        filename = "test_inventory_export.csv"
    export_file = open(filename, "w",  buffering = 1 ,encoding = 'UTF-8')
    a=""
    for key, values in inventory.items():
        for i in range(0,values):
            a += key + ","
    a=a.strip(",")
    export_file.write(a)
    export_file.close()



# Main function sets initial variables and stores rest of the functions
def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(inv)
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(dragon_loot, inv)
    display_inventory(inv)
    print_table(inv)
    print_table(inv,"count,desc")
    print_table(inv,"count,asc")
    inv = import_inventory(inv, "test_inventory.csv")
    print_table(inv)
    export_inventory(inv, "new_export.csv")

