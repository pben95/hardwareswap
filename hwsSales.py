import csv
from tkinter import *
def newSale():
    try:
        sale = []
        for i in range(len(entries)):
            sale.append(entries[i].get())
            entries[i].delete(0, END)
        profit = round(float(sale[4]) - (float(sale[2]) + float(sale[3])), 3)
        margin = round((round(float(sale[4]) - (float(sale[2]) + float(sale[3])), 3) / float(sale[2])) * 100, 3)
        sale.extend([profit, margin])
        with open('HWS_Sales.csv', 'a', newline='') as csvfile:
            hwsWriter = csv.writer(csvfile)
            hwsWriter.writerow(sale)
        entries[0].focus()
        print("Success!")
    except (IndexError, ValueError):
        print("Error!")
master = Tk()
master.geometry('280x180')
header, entries = ["Item Name", "Type of Part", "Item Cost", "Shipping Cost", "Selling Price", "Buyer Email", "Username"], []
for i in range(len(header)):
    label = Label(master, text=header[i]).grid(row=i)
    if i == 2 or i == 3 or i == 4:
        entry = Entry(master, textvariable=DoubleVar(), width=30)
    else:
        entry = Entry(master, width=30)
    entries.append(entry)
    entry.grid(row=i, column=1)
Button(master, text='Quit', command=master.quit).grid(row=7, column=0, sticky=W, pady=4)
Button(master, text='Submit', command=newSale).grid(row=7, column=1, sticky=W, pady=4)
mainloop()