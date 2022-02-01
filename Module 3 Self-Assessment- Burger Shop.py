#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[138]:


#Gerolakkitis Elenie  2022.Feb.01

class FoodItem:
    
    def __init__(self, price):
        self.price=price
        
    def display(self):
        print("Price: $"+ str("{:.2f}".format(self.price)))

class Burger(FoodItem):
    def __init__(self, price, butter, pickles, lettuce, tomato, cheese, ingredient_list):
        FoodItem.__init__(self,price)
        self.butter=butter
        self.pickles=pickles
        self.lettuce=lettuce
        self.tomato=tomato
        self.cheese=cheese
        self.ingredient_list=ingredient_list
        
    def display(self):
        print("Burger ingredients: ")
        counter=1
        for x in self.ingredient_list:
            print(str(counter)+": ", x)
            counter=counter+1
        FoodItem.display(self)
        
    
class Drink(FoodItem):
    def __init__(self, price, size, type_of_drink):
        FoodItem.__init__(self,price)
        self.size=size
        self.drink_type=type_of_drink
        
    def display(self):
        print("Drink ordered:", self.drink_type)
        print("Drink size:",self.size)
        FoodItem.display(self)
        
    
class Side(FoodItem):
    def __init__(self, price, type_of_side):
        FoodItem.__init__(self,price)
        self.side_type=type_of_side
        
    def display(self):
        print("Side ordered:", self.side_type)
        FoodItem.display(self)
    
class Combo(FoodItem):
    def __init__(self, price, burger, drink, side):
        FoodItem.__init__(self,price)
        self.burger=burger
        self.side=side
        self.drink=drink
        
    def display(self):
        print("=============")
        print("COMBO INFO:")
        self.burger.display()
        print()
        self.side.display()
        print()
        self.drink.display()
        print()
        print("Total combo price is: $"+str(self.price))
    
    

class Order:
    def __init__(self):
        self.order=list()
    
    def add_item_to_Order(self,item):
        self.order.append(item)
 

def user_input_burger():
    #     ask user for input and store it in burger object 
    
    print("\nAdd additional condiments to your burger - Answer with (YES/NO):")
    butter=input("Butter? $0.00 : ")
    butter=butter.lower()
    pickles=input("Pickles? $0.10 : ")
    pickles=pickles.lower()
    lettuce=input("Lettuce? $0.30 : ")
    lettuce=lettuce.lower()
    tomato=input("Tomato? $0.30 : ")
    tomato=tomato.lower()
    cheese=input("Cheese? $0.25 : ")
    cheese=cheese.lower()
    
    
    burger_price=4.20
    ingredient_list=list()
    if butter=="yes":
        ingredient_list.append("Butter")
    if pickles=="yes":
        ingredient_list.append("Pickles")
        burger_price=burger_price+0.10
    if lettuce=="yes":
        ingredient_list.append("Lettuce")
        burger_price=burger_price+0.30
    if tomato=="yes":
        ingredient_list.append("Tomato")
        burger_price=burger_price+0.30
    if cheese=="yes":
        ingredient_list.append("Cheese")
        burger_price=burger_price+0.25

    b = Burger(burger_price, butter, pickles, lettuce, tomato, cheese, ingredient_list)
    
    return b
 
def user_input_drink():
    #ask user for input and store it in drink object 

    type_of_drink=""
    while(type_of_drink!="coca-cola" and type_of_drink!="sprite" and type_of_drink!="orange juice" and type_of_drink!="water"):
        type_of_drink=input("\nWhat kind of drink would you like (small size)? \n1. Coca-Cola $1.50\n2. Sprite $1.50/         \n3. Orange Juice $2.75\n4. Water $1.00\n")
        type_of_drink=type_of_drink.lower()
        
        if (type_of_drink!="coca-cola" and type_of_drink!="sprite" and type_of_drink!="orange juice" and type_of_drink!="water"):
            print("Invalid drink! Available drinks: Coca-cola, Sprite, Orange Juice, and Water")
        
    
    size="small"
    if type_of_drink=="coca-cola" or type_of_drink=="sprite":
        price= 1.50
    elif type_of_drink=="orange juice":
        price= 2.75
    else:
        price=1.00
        
    sizeQuestion=input("\nWould you like to upgrade your drink from small to large for an additional $0.75 (YES/NO): ")
    sizeQuestion=sizeQuestion.lower()
    if sizeQuestion=="yes":
        size="large"
        price=price+0.75
        
    d = Drink(price, size, type_of_drink)
    
    return d
 
def user_input_side():
    #ask user for input and store it in side object
    side_type=""
    
    while(side_type!="mac" and side_type!="side salad" and side_type!="french fries"):
        print("\nWhat kind of side would you like?")
        print("Options: \n1.Mac $3.00, \n2.Side Salad $3.25, \n3.French Fries $2.40")
        side_type=input()
        side_type=side_type.lower()
        
        if (side_type!="mac" and side_type!="side salad" and side_type!="french fries"):
            print("Invalid side. Available Sides: Mac, Side Salad, and French Fries. Try again!")
        
    
    if side_type=="mac":
        price=3.00
    elif side_type=="side salad":
        price=3.25
    else:
        price=2.40
    
    s = Side(price, side_type)
    print()
    
    return s
 
def user_input_combo():
    #ask user for input and store it in combo object 
    #a combo must include one burger, one side, and one drink
    burger=user_input_burger()
    drink=user_input_drink()
    side=user_input_side()
    
    price=burger.price+drink.price+side.price
    c = Combo(price, burger, drink, side)

    return c
 
def take_order():    
    #ask user for name for the order 
    customer_name=input("What is your name: ")
    customer_name=str.title(customer_name)
    print("Welcome to Burger Shop",customer_name)
    #repeat taking order until client is done 
    
    user_input=""
    customers_order=Order()
    total_cost=0
    counter=0
    while (user_input!="done"):
        
        user_input=input("\nChoose items from the menu (Enter 'DONE' when finished): \n1. Burger $4.20\n2. Side $2.40-$3.00        \n3. Drink $1.50-$2.75 \n4. Combo (Burger, Side, Drink) $10.00 \n")
        user_input=user_input.lower()
        
        
        if (user_input=="burger" or user_input=="side" or user_input=="drink" or user_input=="combo"):
            #add instructions
            if user_input=="burger":
                menu_item=user_input_burger()
                print("Burger added")
            elif user_input=="drink":
                menu_item=user_input_drink()
                print("Drink added")
            elif user_input=="side":
                menu_item=user_input_side()
                print("Side added")
            else:
                menu_item=user_input_combo()
                print("Combo added")
            customers_order.add_item_to_Order(menu_item)
            
            xCounter=0
            for x in customers_order.order:
                if xCounter!=counter:
                    xCounter=xCounter+1
                else:
                    total_cost=total_cost+float(x.price)
            counter=counter+1
            print("\nTotal items ordered: ", len(customers_order.order))
            print("Total Cost of all items: $"+str("{:.2f}".format(total_cost)))
            
            
        elif(user_input=="done"):
            pass
        
        else:
            print("Invalid menu option. Acceptable entries: Burger, Side, Drink, Combo")
           
        if len(customers_order.order)>0 and user_input!="done":
            removeItem=input("\nWould you like to remove an item? (YES/NO)")
            removeItem=removeItem.lower()

            if removeItem=="yes":
                print("Total Cost of all items: $"+str("{:.2f}".format(total_cost)))
                counter=0
                for x in customers_order.order:
                    print("\nITEM:",counter+1)
                    x.display()
                    counter=counter+1
                    print("..................")
                    
                deleteItem=input("Enter a number for an item to delete: ")
                if deleteItem.isnumeric():
                    deleteItem=int(deleteItem)-1
                    if deleteItem<len(customers_order.order):
                        total_cost=total_cost-float(customers_order.order[deleteItem].price)
                        del customers_order.order[deleteItem]
                        print("=========================================")
                        print("\nUpdated list of total items ordered: ", len(customers_order.order))
                        print("Updated total Cost of all items: $"+str("{:.2f}".format(total_cost)))
                        print("=========================================")
                    else:
                        print("Number entered does not exist!")
                
        if user_input!="done":           
            print("-----------------------------------------")
            
            
    print("\n=========================================")
    print("=========================================")
    print("=========================================\n")
    print("Number of items ordered: ", len(customers_order.order))
    print("Total Cost of items ordered $"+str("{:.2f}".format(total_cost)))
    
   

    print()
    
    for x in customers_order.order:
        x.display()
        print()
    
    #display order details
    
    #display a thank you message
    print("\nThank you "+customer_name+"!")
    
 
take_order()


# In[ ]:




