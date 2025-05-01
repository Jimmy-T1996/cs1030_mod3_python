import csv

def read_columns(filename):
    titles = []
    usernames = []
    passwords = []

    with open(filename, "r", newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            titles.append(row["Title"])
            usernames.append(row["Username"])
            passwords.append(row["Password"])

    return titles, usernames, passwords

# Example usage:
titles, usernames, passwords = read_columns("Password.csv")

# Print by row
for t, u, p in zip(titles, usernames, passwords):
    print(f"Title: {t} | Username: {u} | Password: {p}")



