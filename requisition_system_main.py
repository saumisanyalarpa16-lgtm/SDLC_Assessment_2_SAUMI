req_counter = 10000
all_requisitions = []

class Requisition:
    def __init__(self,date,staff_id,staff_name):
        global req_counter
        req_counter = req_counter + 1
        self.req_id = req_counter
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.total = 0
        self.status = "Pending"
        self.approval_ref = ""
        all_requisitions.append(self)

    def add_requisition(self, items):
        total = 0
        for name, price in items:
            total = total + price
        if total == int(total) or float(total):
            total = float(total)
        self.total = total
        return total
    
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.staff_id + str(self.req_id)[-3:]
        else:
            self.status = "Pending"

    def respond_to_requisition(self, decision):
        if self.status != "Pending":
            print("This Requisition is NOT PENDING")
        elif decision =="yes":
            self.status = "Approved"
            self.approval_ref = self.staff_id + str(self.req_id)[-3:]
        elif decision == "no":
            self.status = "Not Approved"
        else:
            print("No decision made made. Status stays PENDING.")

    def display_requisition(self):
        print("\nDate: ", self.date)
        print("Requisition ID:",self.req_id)
        print("Staff ID:",self.staff_id)
        print("Staff Name:",self.staff_name)
        print("Total: $",self.total)
        print("Status: ",self.status)
        if self.approval_ref != "":
            print("Approval Reference Number: ", self.approval_ref)
        else:
            print("Approval reference Number: Not Available")

    def display_requisitions():
        for req in all_requisitions:
            req.display_requisition()

    def requisition_statistics():
        approved = 0
        pending = 0
        not_approved = 0
        for req in all_requisitions:
            if req.status == "Approved":
                approved +=1
            elif req.status == "Pending":
                pending +=1
            else:
                not_approved = not_approved + 1
        print("\nDisplaying the Requisition Statistics")
        print("The total number of requisition submitted:",len(all_requisitions))
        print("The total number of approved requisitions: ",approved)
        print("The total number of pensing requisitions: ",pending)
        print("The total number of not approved requisitions: ",not_approved)
        return len(all_requisitions),approved,pending,not_approved
        def submit_requisition(): 
    date = input("Date (dd/mm/yyyy): ")
    staff_id = input("Staff ID: ")
    staff_name= input("Staff Name: ")
    req= Requisition(date, staff_id, staff_name)
    print("Requisition ID: ",req.req_id)

    items = []
    while True:
        item_name = input("Item Name: ")
        while True:
            try:
                item_price = input("Item Price:" )
                break
            except ValueError:
                print("Please enter a number.")
            items.append((item_name,item_price))
            another = input("Add another item (Yes/No)? ").lower().strip()
            if another != "yes":
                break

    print("Total: $"+ str(req.add_requisition(items)))
    req.approve_requisition()
    print("Status: ",req.status)
