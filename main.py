import csv as csv

# csv file name
CSV_FILE = "expense.csv"
FIELDNAMES = ['Date', 'Description', 'Category', 'Amount']


def sep():
    print('=' * 65)


def setup_csv():
    # TODO: NEED TO FIX THIS, OVERWRITING EXPENSE FILE, JUST NEED TO GET
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a writer object and write the header row
        writer = csv.writer(csvfile)
        writer.writerow(FIELDNAMES)


def add_expense():

    print("\n--- Add New Expense ---")

    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description: ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))

    with open(CSV_FILE, 'w', newline='') as csvfile:
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # write the new expense record to the file
            writer.writerow([date, description, category, amount])
    sep()
    print("Expense added successfully!")


def view_expense():

    print("\n--- All Expenses ---")

    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # skip the header row
        header = next(reader)
        print(
            f"{header[0]:<12} | {header[1]:<25} | {header[2]:<15} | {header[3]:>10}")
        print("-" * 65)

        # keep track if any records are found
        found_records = False
        # iterate over each row in the file and print it
        for row in reader:
            found_records = True
            print(
                f"{row[0]:<12} | {row[1]:<25} | {row[2]:<15} | {float(row[3]):>10.2f}")

        if not found_records:
            print("No expenses found.")


def main():
    # ensure the CSV file is set up
    setup_csv()

    while True:
        # display the menu
        print("\n--- Expense Tracker Menu ---")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


# entry point
if __name__ == "__main__":
    main()
