from datetime import datetime
expenses=[]
income=0
history=[]
credit_categories=["Salary","Pocket Money","Scholarship","Other"]
delete_categories = ["Shopping", "Grocery", "Fuel", "Food", "Recharge", "Rent", "Medical", "Others"]
def add_income():
    global income
    print("Choose income source:")
    for i, source in enumerate(credit_categories, 1):
        print(f"{i}. {source}")

    try:
        choice = int(input("Enter category number: ").strip())
        source = credit_categories[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Defaulting to 'Other'")
        source = "Other"
    amount=float(input("Enter the Amount:₹").strip())
    income=income+amount
    history.append(f"Credited ₹{amount} from {source} on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
def delete_income():
    global income
    if(income==0):
        print("Zero Balance")
        return
    print("Choose a category:".strip())
    for i, category in enumerate(delete_categories, 1):
        print(f"{i}. {category}")
    
    try:
        choice = int(input("Enter category number: ").strip())
        reason = delete_categories[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Defaulting to 'Others'")
        reason = "Others"
    d=float(input("Enter the amount to be debited:₹").strip())
    if d > income:
        print("Insufficient Balance")
        return
    income=income-d
    history.append(f"Debited -₹{d} for {reason} on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"Account Balance ₹{income}")

def view_income():
    global income
    print(f"Account Balance is ₹{income} ")
def transcation_history():
    if history:
        print("-------Transcation History-------")
        for entry in history:
            print(entry)
    else:
        print("No transcation Yet")

def search_history():
    keyword = input("Enter a keyword to search (e.g., Grocery): ").strip().lower()
    results = [entry for entry in history if keyword in entry.lower()]
    if results:
        print("---- Search Results ----")
        for r in results:
            print(r)
    else:
        print("No matching transactions found.")

def exit_app():
    print("Thank You")
    exit()
commands={ "Credit":add_income,"Debit":delete_income,"View":view_income,"History":transcation_history,"Search":search_history,"Exit":exit_app}
while True:
    command = input("\nEnter Command (Credit / Debit / View / History / Search / Exit): ").strip().title()
    try:
        commands[command]()
    except KeyError:
        print("Invalid command. Try again.")