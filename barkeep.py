import math
total = 0
orderList = []
orderSales = {}
setDrinks = ["martini", "manhattan", "alexander", "maitai", "sazerac", "oldfashioned", "aviation"]

# List of spirits
spiritsList = ["roku", "dryvermouth", "sweetvermouth", "stoli", "amaretto", "citadelle", "ferrand", "maraschino", "popov", "italicus", "pimms", "mezcal", "bourbon", "curacao", "violette", "bacardi", "llords", "regnier", "hennessy", "plantation"]
spirits375 = {"maraschino":35}
spirits750 = {"roku":33, "dryvermouth":22, "sweetvermouth":22, "amaretto":12, "ferrand":62, "italicus":40, "pimms":25, "mezcal":20, "bourbon":25, "curacao":30, "violette":30, "bacardi":25, "llords":12, "regnier":10, "hennessy":55, "plantation":35}
spirits1500 = {"stoli":44, "citadelle":46, "popov":15}

def new(order):
    global orderList
    global orderSales
    if order in orderList:
        print("Order already exists.")
    else:
        orderList.append(order)
        orderSales[order] = 0

def close(order):
    global orderList
    global orderSales
    global total
    if order in orderList:
        orderList.remove(order)
        print(order, "total:", orderSales[order])
        total = total + orderSales[order]
        print("Sales:", total)
        del orderSales[order]
    else:
        print("No such order.")

def end():
    for x in orderList:
        close(x)

def order(order):
    global orderList
    global orderSales
    if not order in orderList:
        print("No such order.")
        return
    prompt = str(order) + " $ "
    orderTotal = 0
    while True:
        orderCommand = input(prompt)
        if orderCommand == "done":
            break
        if orderCommand in setDrinks:
            cost = setDrink(orderCommand)
            orderTotal = orderTotal + cost
            break
        parsedOrderCommand = orderCommand.split()
        ingredient = parsedOrderCommand[0]
        if ingredient not in spiritsList:
            print("No such spirit.")
            continue
        try:
            quantity = float(parsedOrderCommand[1])
        except:
            print("Bad quantity.")
            continue
        cost = pour(ingredient, quantity)
        orderTotal = orderTotal + cost
    print(orderTotal)
    pourMarkup = orderTotal * 1.25
    print(pourMarkup)
    garnishMarkup = pourMarkup + 1
    print(garnishMarkup)
    shrinkageMarkup = garnishMarkup * 1.20
    print(shrinkageMarkup)
    price = math.ceil(shrinkageMarkup)
    print(price)
    priorTotal = orderSales[order]
    newTotal = priorTotal + price
    orderSales[order] = newTotal
    print(newTotal)

def pour(spirit, quantity):
    if spirit in spirits1500:
        divisor = 52.8
        pony = spirits1500.get(spirit) / divisor
    elif spirit in spirits750:
        divisor = 26.4
        pony = spirits750.get(spirit) / divisor
    elif spirit in spirits375:
        divisor = 13.2
        pony = spirits375.get(spirit) / divisor
    pourCost = pony * quantity
    return pourCost

def setDrink(drink):
    baseCost = 0
    pour1 = 0
    pour2 = 0
    pour3 = 0
    if drink == "martini":
        pour1 = pour("roku", 1.5)
        pour2 = pour("dryvermouth", 0.5)
    elif drink == "manhatttan":
        pour1 = pour("bourbon", 1.75)
        pour2 = pour("sweetvermouth", 0.75)
    elif drink == "maitai":
        pour1 = pour("bacardi", 1)
        pour2 = pour("plantation", 1)
        pour3 = pour("curacao", 0.5)
    elif drink == "alexander":
        pour1 = pour("ferrand", 1)
        pour2 = pour("llords", 1)
    elif drink == "oldfashioned":
        pour1 = pour("bourbon", 1.5)
    elif drink == "sazerac":
        pour1 = pour("ferrand", 1.75)
        pour2 = pour("regnier", 0.25)
    elif drink == "aviation":
        pour1 = pour("roku", 1.5)
        pour2 = pour("maraschino", 0.5)
        pour3 = pour("violette", 0.25)
    baseCost = baseCost + pour1 + pour2 + pour3
    return baseCost

# Initial shell
while True:
    rawCommand = input("# ")
    if rawCommand == "end":
        end()
        quit()
    elif rawCommand in orderList:
        order(rawCommand)
        continue
    parsedCommand = rawCommand.split()
    try:
        command = parsedCommand[0]
        argument = parsedCommand[1]
    except:
        print("Invalid command.")
        continue
    if command == "new":
        new(argument)
    elif command == "close":
        close(argument)
    else:
        print("Invalid command.")