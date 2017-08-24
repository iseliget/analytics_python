# analytics_python
some useful codes for doing advanced analytics using Python


### DatabaseKaiwa
```
column_names = ['name','gpa','undergrad','grad','past_companies']
new_kaiwa = DatabaseKaiwa(db_host="127.0.0.1", db_name="application", db_user="admin", db_password="123", colnames=column_names, db_type="mysql")
new_kaiwa.execute("SELECT * FROM candidates_info")
undergrad_info = new_kaiwa.fetch_columns(exclude=['graduate'])
```
#### brutal_force_solver.py
```python
# suppose we have built a model that predicts income
# the model object is income_model and has method `predict`
# our purpose is to maximize income

optimal_comb, optimal_y = bf_optimizer(f=income_model, X=X, target="max",
      indp_vars=['educ_year','father_income','mother_income'],
      indp_vars_ranges=[np.arange(9,20,1), np.arange(30000,80000,100), np.arange(30000,80000,100)])
```
