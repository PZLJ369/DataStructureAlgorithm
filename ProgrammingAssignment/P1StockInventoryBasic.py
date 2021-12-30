# Name: JI ZHUOLIN
# AdminNO: 202016N
# Group: IT2153_05
# Part 1 - Stock Inventory - Basic Features

# Inventory_store = {}
Inventory_store = {1001:{'desc':'SportShoe', 'price':500, 'qua':50, 'madeIn': 'Singapore', 'year':2020},
                   1002:{'desc':'HighHeel', 'price':200, 'qua':20, 'madeIn': 'China', 'year':2015},
                   1003:{'desc':'Slipper', 'price':35, 'qua':30, 'madeIn': 'Vietnam', 'year':2017}}
maxStorage = 20
ThisYear = 2021


def mainMenu():
    print('========= Stock Inventory Menu =========')
    if len(Inventory_store) < maxStorage:
        print('(1) Add items into the Stock Inventory')
    else:
        print("- Store is full unable to add more items! -")
    if len(Inventory_store) > 0:
        print('(2) Update selected item')
    else:
        print('- Store in empty! Cannot update -')
    print('(3) Remove items Inventory')
    print('(4) Display items in Inventory')
    if len(Inventory_store) >= 2:
        print('(5) Sort items')
    else:
        print('- Not enough items to do sorting -')
    print('(6) Search item')
    print('(0) Exit Application')
    print('')
    CHOICE = int(input(">> Enter choice: "))
    print('')
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1 and len(Inventory_store) < maxStorage:
        addInventory()  # working
    elif CHOICE == 2:
        updateInventory()  # working
    elif CHOICE == 3:
        removeInventory()  # working
    elif CHOICE == 4:
        displayInventory()  # working
    elif CHOICE == 5 and len(Inventory_store) >= 2:
        sortInventory()  # working + more function (reverse sort)
    elif CHOICE == 6:
        searchInventory()  # working
    elif CHOICE == 0:  # working
        exit()
    else:
        print('Invalid input. Please Retry!')
        print('')
        mainMenu()

def addInventory():
    if len(Inventory_store) < maxStorage:
        print("===== Adding Inventory =====")
        item_index = int(input("Enter item index (4 digit): "))

        while item_index in Inventory_store:
            print("- Item index already exist - ")
            addInventory()
        while item_index not in range(1000, 9999):
            print("- Item index need to be 4 digit number! -")
            addInventory()

        item_description = input("Enter item name: ")
        item_selling_price = int(input("Enter item price: "))

        item_quantity = int(input("Enter item quantity: "))
        item_made_in = input("This item is made in: ")
        item_produce_year = int(input("Year of production: "))
        while item_produce_year not in range(1900, ThisYear+1):
            print("- Year of production is invalid! -")
            item_produce_year = int(input("Year of production: "))

        Inventory_store[item_index] = {'desc': item_description,
                                       'price': item_selling_price,
                                       'qua': item_quantity,
                                       'madeIn': item_made_in,
                                       'year': item_produce_year}

    continue_exit()

def updateInventory():
    print("===== Updating Inventory =====")
    item_index = int(input("Enter item index: "))

    if item_index in Inventory_store.keys():
        # only allow user to update certain values
        item_description = Inventory_store[item_index]['desc']
        item_selling_price = int(input("Enter item price: "))  # update price
        item_quantity = int(input("Enter item quantity: "))   # update quantity
        item_made_in = Inventory_store[item_index]['madeIn']
        item_produce_year = Inventory_store[item_index]['year']

        Inventory_store[item_index] = {'desc': item_description,
                                       'price': item_selling_price,
                                       'qua': item_quantity,
                                       'madeIn': item_made_in,
                                       'year': item_produce_year}
    else:
        print("- item not found! -")

    continue_exit()


def removeInventory():
    print("===== Removing Inventory =====")
    item_index = int(input("Enter item index: "))

    if item_index in Inventory_store.keys():
        ConfirmDel = input("** Confirm Delete ** (y/n): ")
        if ConfirmDel == 'y':
            del(Inventory_store[item_index])
            print(">>",item_index,"Removed!")
        else:
            print('cancel')
    else:
        print("- item not found! -")

    continue_exit()

def displayInventory():
    print("===== Display Inventory =====")
    for key in Inventory_store:
        print("Item index:", key)
        print("Item description:", Inventory_store[key]['desc'])
        print("Item price: $", Inventory_store[key]['price'])
        print("Item stock level:", Inventory_store[key]['qua'])
        print("Item made in:", Inventory_store[key]['madeIn'])
        print("Year of production:", Inventory_store[key]['year'])
        print("-----------------------------")

    continue_exit()

def sortInventory():
    # global d
    # global callSortInventory
    print("===== Sort Items =====")
    print('(1) Sort items by Price')
    print('(2) Sort items by Quantity')
    print('(3) Sort items by Year of production')
    SortByMethod = int(input("Sort items By: "))
    print('')
    Inventory_list = list(Inventory_store.items())
    if SortByMethod == 1:  # ------------ Bubble Sort ------------
        print("===== Sort items by Price =====")
        for i in range(len(Inventory_list)-1, 0, -1):
            Swap = False
            for j in range(i):
                # print("Price:", Inventory_list[j][1]['price'])
                if Inventory_list[j][1]['price'] > Inventory_list[j+1][1]['price']:
                    tmpStore = Inventory_list[j]
                    Inventory_list[j] = Inventory_list[j+1]
                    Inventory_list[j+1] = tmpStore
                    Swap = True
            if not Swap:
                break
        d = dict(Inventory_list)
        # callSortInventory = True
        # displayInventory()
        for key in d:
            print("Item index:", key)
            print("Item description:", d[key]['desc'])
            print("Item price: $", d[key]['price'])
            print("Item stock level:", d[key]['qua'])
            print("Item made in:", d[key]['madeIn'])
            print("Year of production:", d[key]['year'])
            print("-----------------------------")

    elif SortByMethod == 2:   # ------------ Selection Sort ------------
        print("===== Sort items by Quantity =====")
        for i in range(len(Inventory_list)-1):
            smallestQua = i  # Assume i is smallest
            for j in range(i+1, len(Inventory_list)):  # smallest in front will not change
                if Inventory_list[j][1]['qua'] < Inventory_list[smallestQua][1]['qua']:
                    smallestQua = j

            if smallestQua != i:  # Swap ith value & smallNdx value (if smallest value not in proper position)
                tmpStore = Inventory_list[i]
                Inventory_list[i] = Inventory_list[smallestQua]
                Inventory_list[smallestQua] = tmpStore
        d = dict(Inventory_list)
        for key in d:
            print("Item index:", key)
            print("Item description:", d[key]['desc'])
            print("Item price: $", d[key]['price'])
            print("Item stock level:", d[key]['qua'])
            print("Item made in:", d[key]['madeIn'])
            print("Year of production:", d[key]['year'])
            print("-----------------------------")

    elif SortByMethod == 3:  # ------------- Insertion sort -------------
        print("===== Sort items by Year of production =====")
        for i in range(1, len(Inventory_list)):  # Starts with the first item as the only sorted entry.
            tmpStore = Inventory_list[i]  # Save value to position
            yearvalue = Inventory_list[i][1]['year']
            pos = i  # Find position where value fits in ordered part of list.

            while pos > 0 and yearvalue < Inventory_list[pos - 1][1]['year']:
                Inventory_list[pos] = Inventory_list[pos-1]  # Shift items to right during search
                pos = pos - 1

            Inventory_list[pos] = tmpStore  # Put saved value into open slot.
        d = dict(Inventory_list)
        for key in d:
            print("Item index:", key)
            print("Item description:", d[key]['desc'])
            print("Item price: $", d[key]['price'])
            print("Item stock level:", d[key]['qua'])
            print("Item made in:", d[key]['madeIn'])
            print("Year of production:", d[key]['year'])
            print("-----------------------------")

    else:
        print("-- Invalid sort method! Please Retry. --")
        sortInventory()
    continue_exit()


def searchInventory():
    print("===== Search Item =====")
    print('(1) Search item index (linear)')
    print('(2) Search item index (Binary)')
    SearchMethod = int(input("Search Method: "))
    print('')
    Inventory_list = list(Inventory_store.items())
    item_index = int(input("Enter item index: "))
    if item_index in Inventory_store.keys():
        if SearchMethod == 1:
            # -------- Sequential Search --------
            for key in Inventory_store:
                if key == item_index:
                    print("Item index:", key, "found!")
                    print("Item description:", Inventory_store[key]['desc'])
                    print("Item price: $", Inventory_store[key]['price'])
                    print("Item stock level:", Inventory_store[key]['qua'])
                    print("Item made in:", Inventory_store[key]['madeIn'])
                    print("Year of production:", Inventory_store[key]['year'])
                    break
        elif SearchMethod == 2:
            # ---------- Binary Search ----------
            low = 0
            high = len(Inventory_list) - 1
            while low <= high:
                mid = (low+high)//2  # round down
                if Inventory_list[mid][0] == item_index:
                    print("Item index:", Inventory_list[mid][0],"found!")
                    print("Item description:", Inventory_list[mid][1]['desc'])
                    print("Item price: $", Inventory_list[mid][1]['price'])
                    print("Item stock level:", Inventory_list[mid][1]['qua'])
                    print("Item made in:", Inventory_list[mid][1]['madeIn'])
                    print("Year of production:", Inventory_list[mid][1]['year'])
                    break
                elif item_index < Inventory_list[mid][0]:
                    high = mid - 1
                else:
                    low = mid + 1

    else:
        print("- item not found! -")

    continue_exit()


def continue_exit():
    print(" *-------- Continue / Exit --------* ")
    CHOICE = int(input('Continue (9) / Exit (0): '))

    if CHOICE == 9:
        mainMenu()
    elif CHOICE == 0:
        exit()
    else:
        continue_exit()


mainMenu()


