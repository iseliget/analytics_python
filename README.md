# analytics_python
some useful codes for doing advanced analytics using Python


### DatabaseKaiwa
```
column_names = ['name','gpa','undergrad','grad','past_companies']
new_kaiwa = DatabaseKaiwa(db_host="127.0.0.1", db_name="application", db_user="admin", db_password="123", colnames=column_names, db_type="mysql")
new_kaiwa.execute("SELECT * FROM candidates_info")
undergrad_info = new_kaiwa.fetch_columns(exclude=['graduate'])
```
