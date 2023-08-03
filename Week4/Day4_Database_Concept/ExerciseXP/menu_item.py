import psycopg2


connection = psycopg2.connect(
    database="Menu_exercise",
    user="postgres",
    password="masahiro38",
    host="localhost",
    port="5432",
)

class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def save(self):
     try:
        with connection:
            with connection.cursor() as curs:
                query = f"""
                INSERT INTO menu_items (items_name, item_price)
                VALUES
                ('{self.name}',{self.price})
                """
                curs.execute(query)
                connection.commit()
     except Exception as err:
        print("SOME ERROR",err)
    
    
    @staticmethod
    def delete(name,price):
     try:
        with connection:
            with connection.cursor() as curs:
                query = f"""
                DELETE FROM menu_items
                WHERE items_name = '{name}' and item_price = {price}
                """
                curs.execute(query)
                connection.commit()
     except Exception as err:
        print("SOME ERROR",err)
     
     
    @staticmethod   
    def update(other_product,price,name):
     try:
        with connection:
            with connection.cursor() as curs:
                query = f"""
                UPDATE menu_items
                SET items_name = '{other_product}',item_price = {price}
                WHERE items_name = '{name}'
                """
                curs.execute(query)
                connection.commit()
     except Exception as err:
        print("SOME ERROR",err)
        
