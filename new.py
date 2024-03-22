class Cart():
    bag = 'Brown'

    item = ''
    qty = 0
    dict = {}

    def __init__(self, item, qty):
        self.item = item 
        self.qty = qty 
    
    def addItem(self, item, qty):
        item = input('What item do you want to add? ')
        self.dict[item] = qty

    def addQty(self):
        qty = input('How many do you want? ')
        self.qty 

    def cartShow():
        print('You have {qty} and have added this many of {item}')
    


def run():
    print('A')
    cart = Cart('oreos', 4)


    while True:
        print('')

        response = input('What would you like to do?  add/show/quit ?')
        
        print(response)
        if response == 'quit':
            print(f'Thank you for shopping with us! ')
            break
        
        elif response == 'add':
            cart.addItem()
        
        elif response == 'show':
            cartShow()

run()