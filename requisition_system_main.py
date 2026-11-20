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
        if total == int(total):
            total = int(total)
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
            self.status = "Not approved"
        else:
            print("No decision made made. Status stays PENDING.")

    def display_requisition(self):
        print("\nDate: ", self.date)
        print("Requisition ID:",self.req_id)
        print("Staff ID:",self.staff_id)
        print("Staff Name:",self.staff_name)
        print("Total: $",str(self.total))
        print("Status: ",self.status)
        if self.approval_ref != "":
            print("Approval Reference Number: ", self.approval_ref)
        else:
            print("Approval reference Number: Not Available")

    def display_requisitions(self):
        for req in all_requisitions:
            req.display_requisition()

    def requisition_statistics(self):
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
        print("The total number of requisitions submitted:",len(all_requisitions))
        print("The total number of approved requisitions: ",approved)
        print("The total number of pending requisitions: ",pending)
        print("The total number of not approved requisitions: ",not_approved)
        return len(all_requisitions),approved,pending,not_approved
    
#----------------PROGRAMME---------------------------------

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
                item_price = float(input("Item Price:" ))
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

def manager_response():
    pending = []
    for req in all_requisitions:
        if req.status == "Pending":
            pending.append(req)

    if len(pending) == 0:
        print("\nNo Pending Requisitions. No Manager's Decision Required.")
        return

    print("\nThere are pending Requisitions. Manager's decision required")
    tries = 0
    while True:
        code = input("Enter Manager's Code: ")
        if code == "Manager+123+admin":
            break
        tries = tries+1
        print("Wrong code. Try again.")
        if tries == 3:
            print("Too many wrong attempts. Requisitions Stay PENDING...")
            return

    for req in pending:
        print ("\nDate: ", req.date)
        print("Requisition ID: ", req.req_id)
        print("Staff ID: ",req.staff_id)
        print("Total: $",str(req.total))
        decision = input("Do you approve "+req.staff_name+"'s requisition? (yes/no): ").lower().strip()
        req.respond_to_requisition(decision)
        print("Status: ",req.status)

while True:
    if len(all_requisitions) == 0:
        print("\n1.Submit Requisition")
    else:
        print("\n1.Add another requisition")
    print("2.Exit")
    choice = input("Choose: ")
    if choice == "1":
        submit_requisition()
    elif choice == "2":
        break
    else:
        print("Please Choose 1 or 2.")

if len(all_requisitions)>0:
    manager_response()
    print("\n------- Requisition--------")
    first_req= all_requisitions[0]
    first_req.display_requisitions()
    first_req.requisition_statistics()
