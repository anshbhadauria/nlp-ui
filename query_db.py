import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()
                   
c.execute('''
          SELECT
          a.product_name,
          b.price
          FROM products a
          LEFT JOIN prices b ON a.product_id = b.product_id
          ''')

df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
print (df)