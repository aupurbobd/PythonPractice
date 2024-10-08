itemlist=[
    {
        'item': 'Black Coffee',
        'code': 10,
        'price': 2.0
    },
    {
        'item': 'Cappuccino',
        'code': 12,
        'price': 2.5
    },
    {
        'item': 'Latte',
        'code': 14,
        'price': 3.0
    },
    {
        'item': 'Americano',
        'code': 16,
        'price': 1.5
    },
    {
        'item': 'Coffee Mocha',
        'code': 18,
        'price': 3.5
    },
    {
        'item': 'Hot Chocolate',
        'code': 20,
        'price': 0.80
    }
]

rawitems=[
    {
        'item':'coffee powder',
        'quantity': 500,
        'uom':'gram'
    },
    {
        'item':'cocoa powder',
        'quantity': 500,
        'uom':'gram'
    },
    {
        'item':'milk',
        'quantity': 1000,
        'uom':'ml'
    },
{
        'item':'milk foam',
        'quantity': 1000,
        'uom':'ml'
    },
    {
        'item':'sugar',
        'quantity': 2000,
        'uom':'gram'
    },
    {
        'item':'water',
        'quantity': 1000,
        'uom':'ml'
    },
    {
        'item':'chocolate powder',
        'quantity': 1000,
        'uom':'gram'
    },
    {
        'item':'chocolate syrup',
        'quantity': 1000,
        'uom':'gram'
    },
    {
        'item':'plastic cup',
        'quantity': 10,
        'uom':'pcs'
    }
]

recipes = [
    {
        'code': 10,
        'water': 200,
        'coffee powder': 7
    },
    {
        'code': 12,
        'milk': 100,
        'milk foam': 100,
        'coffee powder': 15
    },
    {
        'code': 14,
        'milk': 160,
        'milk foam': 40,
        'coffee powder': 20
    },
    {
        'code': 16,
        'water': 160,
        'coffee powder': 20
    },
    {
        'code': 18,
        'milk': 120,
        'coffee powder': 100,
        'chocolate syrup': 75,
        'sugar': 15
    },
    {
        'code': 20,
        'milk': 190,
        'cocoa powder': 3,
        'chocolate powder': 30,
        'sugar': 15
    }
]



def updateRawItems(rawItem, qty):
    for items in rawitems:
        if items['item']== rawItem:
            remQty = items['quantity'] - qty
            rawitems.append(
                {'item' : items['item'], 'quantity': remQty, 'uom': items['uom']}
            )
            break

updateRawItems('water', 100)
