import csv as csv

# csv file name
CSV_FILE = "expense.csv"


def sep():
    print('=' * 65)


def setup_csv():
    pass


def add_expense():
    with open(CSV_FILE, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def view_expense():
    with open(CSV_FILE, newline='') as f:

        exp_reader = csv.reader(f, delimiter=' ', quotechar='|')

    for row in exp_reader:

        print(', '.join(row))


def main():
    add_expense()
    sep()
    print('--- Task Complete ---')
    sep()


# Entry point of the script
if __name__ == "__main__":
    main()
