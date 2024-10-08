import coffeedata
import time


def display_item(items):
    print('{:7s}{:28s}{:5s}'.format('Code','Item','Price'))
    print('-'*40)
    for data in items:
        print(f'{data['code']:3d}    {data['item']:20s}        {data['price']}')

def checkRecipe(itemcode):
    for item in coffeedata.recipes:
        if item['code'] == itemcode:
            # print(item)
            return item
            # break

def checkRawItems(rawItem):
    for items in coffeedata.rawitems:
        if items['item'] == rawItem:
            return items['quantity']

# def updateRawItems(rawItem, qty):
#     for items in coffeedata.rawitems:
#         if items['item']== rawItem:
#             remQty = items['quantity'] - qty
#             coffeedata.rawitems.append(
#                 {'item' : items['item'], 'quantity': remQty, 'uom': items['uom']}
#             )
#             break


# def getItemName()
display_item(coffeedata.itemlist)
wrongitem=True
while wrongitem:
    itemcode=int(input('\nEnter an item code:'))
    for i in coffeedata.itemlist:
        if i['code']==itemcode:
            itemname=i['item']
            itemprice=i['price']
            wrongitem=False
            break
    if wrongitem== True:
        print('Wrong number!')

recipe=checkRecipe(itemcode)
# print(recipe)
for i in recipe:
    if i!='code':
        quantity = checkRawItems(i)
        # print(quantity)
        if recipe[i]>quantity:
            print(f'Sorry! Insufficient {i}')



# for items in coffeedata.rawitems:
#     print(items)
#print('Insert coins:')
totalvalue=0.0
while True:
    no_coins=int(input('Insert number of coins (0 to exit):'))
    if no_coins==0:
        break
    else:
        typeflag=False
        cointype = int(input('Type of coin (1 for euro, 2 for cent):'))
        while typeflag==False:
            if cointype not in (1,2):
                cointype=int(input('Wrong type! Enter coin type again (1 for euro, 2 for cent:'))
            else:
                typeflag=True
        coinvalue=int(input('Enter the value of the coin:'))
        if cointype==1:
            totalvalue+=coinvalue*no_coins
        else:
            totalvalue+=(coinvalue*no_coins)/100

if totalvalue<itemprice:
    if totalvalue !=0:
        print(f'Insufficient payment! Please take your {totalvalue} euro back.')
    else:
        print("Good bye!")
else:
    remaining=round(totalvalue-itemprice,2)
    print(f'Preparing your {itemname}, please wait.')
    if remaining > 0:
        print(f'Please collect  your change of {remaining} euro.')
    time.sleep(5)
    print('☕')



    for i in recipe:
        if i != 'code':
            coffeedata.updateRawItems(i, recipe[i])

    #         # quantity = checkRawItems(i)
    #         # print(quantity)
    #         if recipe[i] > quantity:
    #             print(f'Sorry! Insufficient {i}')
    time.sleep(0.5)
    print(f'Your {itemname} is ready. Thank you!')




