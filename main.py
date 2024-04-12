from send_mail import send_mail
import csv


def main():
    contacts = csv_to_lst_tuples('list.csv')
    subject = "Subjecto tekstas"
    message_body = "Tai sveikinimas su gera diena"

    send_mail(contacts, message_body, subject)


def csv_to_lst_tuples(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return [(row[1], row[0]) for row in reader]


if __name__ == "__main__":
    main()



