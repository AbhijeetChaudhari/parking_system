#!/usr/bin/env python
# coding: utf-8

# In[12]:


pip install pymysql


# In[1]:


import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Royalassembly@1',
                             database='parkinglots_db')


# In[2]:


cursor = connection.cursor()


# In[3]:


cursor.execute("show tables")


# In[4]:


cursor.fetchall()


# In[6]:


get_ipython().run_line_magic('gui', 'tk')
import tkinter as tk

root = tk.Tk()
root.title("Parking Management System")


# In[10]:


space_label = tk.Label(root, text="PARKING MANAGEMENT SYSTEM ")
space_label.pack()

# Create a frame and pack it into the window
frame = Frame(root, width=200, height=200)
frame.pack()

# Set the background color of the frame to light blue
frame.configure(background='light blue')

tw_label = tk.Label(root, text="Number of 2W:")
tw_label.pack()
tw_entry = tk.Entry(root)
tw_entry.pack()

fw_label = tk.Label(root, text="Number of 4W:")
fw_label.pack()
fw_entry = tk.Entry(root)
fw_entry.pack()

truck_label = tk.Label(root, text="Number of Trucks:")
truck_label.pack()
truck_entry = tk.Entry(root)
truck_entry.pack()

pd_label = tk.Label(root, text="Number of Physically Disabled Spaces:")
pd_label.pack()
pd_entry = tk.Entry(root)
pd_entry.pack()

charges_label = tk.Label(root, text="Charges per hour:")
charges_label.pack()
charges_entry = tk.Entry(root)
charges_entry.pack()


# In[11]:


def save_space():
    # get the values entered in the entry widgets
    num_tw = int(tw_entry.get())
    num_fw = int(fw_entry.get())
    num_truck = int(truck_entry.get())
    num_pd = int(pd_entry.get())
    charges = int(charges_entry.get())

    # save the details to a database or file
    ...
    
save_space_button = tk.Button(root, text="Save Space Details", command=save_space)
save_space_button.pack()


# In[12]:


from tkinter import ttk
notebook = ttk.Notebook(root)
notebook.pack()

# create a tab for the payment section
payment_tab = tk.Frame(notebook)
notebook.add(payment_tab, text="Payment")

# create a tab for the vehicle section
vehicle_tab = tk.Frame(notebook)
notebook.add(vehicle_tab, text="Vehicle")

# create a tab for the user section
user_tab = tk.Frame(notebook)
notebook.add(user_tab, text="User")

# create a tab for the reports section
reports_tab = tk.Frame(notebook)
notebook.add(reports_tab, text="Reports")


# In[13]:


vehicle_type_label = tk.Label(payment_tab, text="Vehicle Type:")
vehicle_type_label.pack()
vehicle_type_combobox = ttk.Combobox(payment_tab, values=["2W", "4W", "Trucks", "Physically Disabled" ])
vehicle_type_combobox.pack()

mode_label = tk.Label(payment_tab, text="Mode:")
mode_label.pack()
mode_combobox = ttk.Combobox(payment_tab, values=["Cash", "Card", "Wallet", "UPI"])
mode_combobox.pack()

charges_label = tk.Label(payment_tab, text="Charges:")
charges_label.pack()
charges_combobox = ttk.Combobox(payment_tab, values=["Hourly", "Daily", "Monthly"])
charges_combobox.pack()

receipt_button = tk.Button(payment_tab, text="Print Receipt")
receipt_button.pack()


# In[ ]:


root.mainloop()


# In[ ]:




