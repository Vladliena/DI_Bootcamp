from menu_item import MenuItem,connection


class MenuManager(MenuItem):
     
    @staticmethod   
    def get_by_name(name):
     try:
        with connection:
            with connection.cursor() as curs:
                query = f"""
                SELECT items_name,item_price FROM menu_items
                WHERE items_name = '{name}'
                """
                curs.execute(query)
                print(curs.fetchall())
     except Exception as err:
        print("SOME ERROR",err)
        
    @staticmethod
    def all_items():
     try:
        with connection:
            with connection.cursor() as curs:
                query = f"""
                SELECT * FROM menu_items
                """
                curs.execute(query)
                print(curs.fetchall())
     except Exception as err:
        print("SOME ERROR",err)  
    
    
        
client1 = MenuItem('Beef',5)
client1.save()
client1.delete('Beef',5)
client1.update('Onion',1,'Milk')
client2 = MenuManager.get_by_name('Chicken')
clients = MenuManager.all_items()

connection.close()
    
