#Task 1
req_counter= 1000
def add_requistion(counter):
    counter=counter+1
    req_id= counter
    print("Enter your Information:")
    date=input("Date:")
    staff_id=input("Staff ID:")
    staff_name=input("Staff Name:")
    print("Requistion ID",req_id)

    print("\nAdd Items:")
    total=0
    while True:
        item_name=input("Item Name:")
        item_price=float(input("Item Price:"))
        total+= item_price
        another_item=input("Add another item(yes/no):").lower().strip()
        if another_item!="yes":
            break
    print("Total: $",total)
    return date,staff_id,staff_name,req_id,total,counter
#Task 2
def requistition_approval(staff_id,req_id,total):
    status = "Pending"
    approval_ref=""
    if total < 500:
        status="Approved"
        last_three = str(req_id)[-3:]
        approval_ref= staff_id +last_three
    return status, approval_ref
#Task 3
def display_requistition(date,staff_id,staff_name,req_id, total, status, approval_ref):
    print("\nPrinting Requistition:")
    print("Date",date)
    print("Requistition ID:",req_id)
    print("Staff ID:",staff_id)
    print("Staff Name:",staff_name)
    print("Total: $",total)
    print("Status:",status)
    if approval_ref != "":
        print("Approval Reference Number:",approval_ref)
date,staff_id,staff_name,req_id,total,requistition_counter=add_requistion(req_counter)
status,approval_ref=requistition_approval(staff_name,req_id,total)
display_requistition(date,staff_id,staff_name,req_id,total,status,approval_ref)

