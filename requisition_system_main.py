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
        elif self.total <=1000:
            self.status = "Pending"
        else:
            self.status = "Not approved"

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

    

