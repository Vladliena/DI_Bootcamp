import requests
import random
import json
import psycopg2



connection = psycopg2.connect(
    database="DailyChallenge2",
    user="postgres",
    password="masahiro38",
    host="localhost",
    port="5432",
)


def random_country(country_num):
   api_response = requests.get('https://restcountries.com/v3.1/all')
   if api_response.status_code == 200:
       print(api_response.status_code)
       data = api_response.text
       parse_json = json.loads(data)
       random_countries = random.sample(parse_json,country_num)
       return random_countries
   else:
        print(f"Failed to fetch countries.")


def insert_to_table():
    try:
        data = random_country(10)
        with connection:
            with connection.cursor() as curs:
                 for country in data:
                     name = country['name']['common']
                     capital = country['capital'][0] if 'capital' in country else None
                     population = country['population'] if 'population' in country else None
                     query = f"""INSERT INTO COUNTRIES (name, capital, population)
                     VALUES
                     ('{name}', '{capital}',{population})"""
                     curs.execute(query)
                     connection.commit()
    except Exception as err:
        print("SOME ERROR",err)
        
insert_to_table()       
connection.close()



