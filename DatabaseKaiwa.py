import pandas as pd
import MySQLdb
import pypyodbc as pyodbc

class DatabaseKaiwa:


    def __init__(self,db_host,db_name,db_user,db_password,colnames=None,db_type="mysql"):
    	"""
    	Args:
    	    db_type:	str. "sql_server" or "mysql"
    	"""

        self.db_type = db_type
        self.colnames = colnames

        if db_type == "mysql":
            self.db = MySQLdb.connect(host=db_host, port=3306, user=db_user, passwd=db_password, db=db_name)

        elif db_type == "sql_server":
            connection_string = "Driver={SQL Server};Server=" + db_host + ";Database=" + db_name + ";UID=" + db_user + ";PWD=" + db_password + ";"
            self.db = pyodbc.connect(self.connection_string)


    def execute(self,query_string):
    	query_string = query_string.lower()
        cursor = self.db.cursor()
        cursor_content = cursor.execute(query_string)

        if "select *" in query_string:
	        if self.db_type == "sql_server":
	            query_results = []
	            for i in cursor_content:
	                j = [k for k in i]
	                query_results.append(j)

	        elif self.db_type == "mysql":
	            cursor_content = cursor.fetchall()
	            query_results = []
	            for i in cursor_content:
	                j = [k for k in i]
	                query_results.append(j)

	        cursor.close()

	        self.results_df = pd.DataFrame(data=query_results)
	        self.results_df.columns = self.colnames

	        return self.results_df

    def fetch_columns(self,include=None,exclude=None):
        """
        Args:
            include:    list
            exclude:    list
        """

        if not(include is None) and exclude is None:
            return self.results_df[include]
        elif not(exclude is None) and include is None:
            return self.results_df[list(set(self.colnames)-set(exclude))]
        elif include is None and exclude is None:
            return self.results_df[self.colnames]

