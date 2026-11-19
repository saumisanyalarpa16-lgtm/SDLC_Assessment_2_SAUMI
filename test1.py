class Requisition:
    _counter=10000

    def __init__(self, date, staff_id, staff_name, items):
        Requisition._counter +=1
        self.requisition_id = Requisition._counter

        self.date= date
        self.staff_id= staff_id
        self.staff_name = staff_name
        self.items = items

        self.total = 0
        for item in items:
            if isinstance(item, (list,tuple)):
                self.total += item[1]
            else:
                self.total += float(item)

        self.status= "Pending"
        self.approval_ref= "Not available"
        self.approve_requisition()

    def approve_requisition(self):
        if self.total<500:
            self.status = "Approved"
            last_three = str(self.requisition_id)[-3:]
            self.approval_ref= f"{self.staff_id}{last_three}"
        else:
            self.status = "Pending"
            self.approval_ref="Not available"

    def manager_response(self, decision):

        if self.status == "Pending":
            if decision.lower() == "approved":
                self.status = "Approved"
                last_three = str(self.requisition_id)[-3:]
                self.approval_ref= f"{self.staff_id}{last_three}"

            elif decision.lower() in ["not allowed","not approved","notapproved","rejected"]:
                self.status = "Not approved"
                self.approval_ref="Not available"

    def display_requisition(self):
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: {self.total : .0f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_ref}")
        print("_" * 40)

    @staticmethod
    def display_statistics(requisitions_list):
        """Display overall statistics of all requisitions"""
        total_submitted = len(requisitions_list)
        total_approved = sum(1 for r in requisitions_list if r.status == "Approved")
        total_pending = sum(1 for r in requisitions_list if r.status == "Pending")
        total_not_approved = sum(1 for r in requisitions_list if r.status == "Not approved")

        print("\n"+"="*50)
        print("Displaying the Requisition Statistics")
        print("="*50)
        print(f"The total number of requisitions submitted: {total_submitted}")
        print(f"The total number of requisitions of approved: {total_approved}")
        print(f"The total number of requisitions of pending: {total_pending}")
        print(f"The total number of requisitions of not approved: {total_not_approved}")
        print("="*50)

#========= Testing Section =========
if __name__ == "__main__":
    all_requisitions = []
    print("=== Creating Requisition Instances ===\n")

    req1 = Requisition("05/11/2026", "FN19", "John Paul", [("Coffee",20),("Burger",30),("Pen",15)])
    all_requisitions.append(req1)

    
    req2 = Requisition("08/11/2026", "FN25", "Christian Bandt", [("Mouse",200),("Charger",250),("Laptop",1500)])
    all_requisitions.append(req2)

    
    req3 = Requisition("12/11/2026", "FN15", "Tracy Brown", [("Monitor",300),("Keyboard",120),("Pendrive",60)])
    all_requisitions.append(req3)

    
    req4 = Requisition("10/11/2026", "FN09", "Emma Wellington", [("Books",120),("Printer",630),("Pen",15)])
    all_requisitions.append(req4)

    
    req5 = Requisition("13/11/2026", "FN11", "Catline Payne", [("Stationaries",80),("Supplies",130),("Fruits",150)])
    all_requisitions.append(req5)

    
    req6 = Requisition("15/11/2026", "FN22", "Lily Martha", [("Carpet",499),("Burger",30),("Pen",15)])
    all_requisitions.append(req6)

    Requisition.display_statistics(all_requisitions)

    print("\nPrinting Requisitions: ")
    print("="*50)
    for req in all_requisitions:
        req.display_requisition()

print("\n=== Manager's Responding to the Pending Requisition ===\n")

req2.manager_response("Not approved")
req4.manager_response("Approved")
req6.manager_response("Approved")
print("Printing Requisition after manager Review")
print("="*50)
for req in all_requisitions:
    req.display_requisition()

Requisition.display_statistics(all_requisitions)

