import tkinter as tk
import functools
import pandas as pd

# import mysql.connector as conn

# con = conn.connect(user = 'root', password = 'cout<<Anoop[1011]', host = 'localhost', database = 'sensorData')
# cursor = con.cursor()

# cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = '%s' " ,('sensorData',))
# noOfTables = cursor.rowcount()
# tables = cursor.fetchall()

# fields = {}
# for i in tables:

#     cursor.execute("SHOW COLUMNS FROM %s", i)
#     filedData = cursor.fetchall()
#     # NoOfColumns = cursor.rowcount()
#     filedNames = []
#     for j in fieldData:
#         filedNames.append(i[0])
    
#     field[i] = filedNames
#     filedData = []




class mainGUI:
    def __init__(self,data):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Air Monitoring system")
        self.root.resizable(0,0)

        self.data = data

        self.rowCount = 0

        self.root.columnconfigure(0, weight = 3)
        self.root.columnconfigure(1, weight = 1)

        for i in self.data:
            for j in self.data[i][1:]:
                cursor.execute("Select avg(%s) from %s ", (j,i[0]))
                dispData = cursor.fetchone()

                self.label = tk.Label(self.root, text = dispData[0], font = ('Ariel', 18))
                self.label.grid(row= rowCount, column= 0, sticky = tk.W + tk.E)

                self.button = tk.Button(self.root, text= "expand", font= ('Ariel', 18), command= functools.partial(self.expand, j, dispData))
                self.button.grid(row= rowCount, column= 1, sticky= tk.W + tk.E)
                
                self.rowCount += 1
                dispData = []

        self.root.mainloop()
    
    def expand(self, table, field):
        # CHECK IF THE dispData IS IN ACCEPTABLE RANGE
        pass
    
        

