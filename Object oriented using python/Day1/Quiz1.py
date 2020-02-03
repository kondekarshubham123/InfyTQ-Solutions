#OOPR-Exer-1
def purchase_mobile(price,Brand):
    if Brand == 'Apple':
        discount = 10
    else:
        discount = 5
    return price - price*discount/100
def purchase_shoe(price,material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    return price + price * tax / 100
                                                        
def purchase_product(product_type,price,mobile_brand,material):
    if product_type == "Mobile":
        total_price = purchase_mobile(price,mobile_brand)
    else:
        total_price = purchase_shoe(price,material)
    print("Total price of "+product_type+" is "+str(total_price))

purchase_product("Mobile",20000,"Apple",None)
purchase_product("Shoe",200,None,"leather")