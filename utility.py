import json
import random as rand

# Path
INVENTORY_FILE = "./IMS using JSON/Records.json"

def create_inventory():
    records = {}
    n = int(input("Enter the number of items in the inventory: "))
    for i in range(n):
        pr_id = rand.randint(1000, 5000)
        req_headers = ["Product name", "Price", "Quantity Available"]
        product_details = {}
        for attr in req_headers:
            s = input(f"Enter {attr}: ")
            if attr == 'Price' or attr == 'Quantity Available':
                s = int(s)
            product_details[attr] = s
        print("\n")
        records[pr_id] = product_details

    with open(INVENTORY_FILE, 'w') as fd:
        json.dump(records, fd, indent=4)

op = input("Do You want to update inventory? (Y/N): ")
if op == 'Y':
    create_inventory()
    
    
# Inventory record
fd = open(INVENTORY_FILE, 'r')
js = fd.read()
records = json.loads(js)
fd.close()


# Displaying inventory items to customer
print("-----------------------MENU----------------------\n")
for key in records.keys() :
    print(f"Code: {key} | Name : {records[key]['Product name']} |  Price : {records[key]['Price']} | Quantity : {records[key]['Quantity Available']} \n")
print("-------------------------------------------------")


# Taking user input
cust_details = {'Name' : 0, 'Phone number' : 0, 'Email address': 0}
cust_purchases = {}
for key in cust_details.keys():
    det = input(f"Enter customer {key}: ")
    if key == 'Phone number':
        det = int(det)
    cust_details[key] = det
    
sum = 0
pr = 1
while(pr):
    pr = int(input("\nEnter 1 to continue adding items or 0 to stop: "))
    if pr:
        ui_prId = str(input("Enter product Id: "))
        ui_qn = int(input("Enter quantity: "))
        
        if(ui_qn > records[ui_prId]['Quantity Available']):
            print("-------------------------------------------------")
            print("Sorry the inventory is low for this product")
            print("Currently only", records[ui_prId]['Quantity Available'], "units available")
            print("Do you want to purchase all", records[ui_prId]['Quantity Available'], "units ?")
            n = input("Enter your response (Yes/No): ")
            print("-------------------------------------------------")
            if n == 'No':
                continue
            else:
                sum += (records[ui_prId]['Quantity Available'] * records[ui_prId]['Price'])
                cust_purchases[records[ui_prId]['Product name']] = [records[ui_prId]['Price'], records[ui_prId]['Quantity Available']]
                records[ui_prId]['Quantity Available'] = 0

        else:
            sum += (ui_qn * records[ui_prId]['Price'])
            cust_purchases[records[ui_prId]['Product name']] = [records[ui_prId]['Price'], ui_qn]
            records[ui_prId]['Quantity Available'] -= ui_qn
    else:
        print("Thank You for shopping with us")

js = json.dumps(records)
fd = open(INVENTORY_FILE, 'w')
fd.write(js)
fd.close()




# Writing sales data into Sales file
transaction_Id = "UTRf" + str(rand.randint(int(1e9), int(2e9)))
sales_data = {'Customer Details': cust_details, 'Purchased Items': cust_purchases, 'Transaction Id': transaction_Id, 'Total amount' : sum}
custom_name = str(str(cust_details['Name']).split(' ')[0] + "_det_trs.json").lower()
filename = f"./IMS using JSON/Sales/{custom_name}"
fs = open(filename, 'w')
js = json.dumps(sales_data, indent=4)
fs.write(js)
fs.close()
print(f"File created: {filename}")



# Printing customer details
print("\n------------------------------BILL--------------------------------\n")
for det in cust_details.keys():
    print(f"{det} : {cust_details[det]}")
for key in cust_purchases.keys():
    print(f"Product Name: {key} | Unit price: {cust_purchases[key][0]} | Quantity: {cust_purchases[key][1]} | Total: Rs {cust_purchases[key][1] * cust_purchases[key][0]}")
print("--------------------------------------------------------------------")
print("Total amount: Rs", sum)
print("--------------------------------------------------------------------")