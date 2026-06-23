
# Question No. 5

def create_account(name, initial_balance):
    account = {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }

    return account


def perform_transaction(account, amount, transaction_type):

    if transaction_type == "deposit":
        account["balance"] += amount

        account["transactions"].append(
            ("Today", "Deposit", amount)
        )

        print("Deposit successful.")

    elif transaction_type == "withdraw":

        if amount > account["balance"]:
            print("Insufficient funds.")

        else:
            account["balance"] -= amount

            account["transactions"].append(
                ("Today", "Withdrawal", amount)
            )

            print("Withdrawal successful.")


def show_transaction_history(account):

    print("\nTRANSACTION HISTORY")

    if len(account["transactions"]) == 0:
        print("No transactions yet.")
        return

    for transaction in account["transactions"]:
        print(transaction)


def monthly_summary(account):

    deposits = 0
    withdrawals = 0

    for transaction in account["transactions"]:

        if transaction[1] == "Deposit":
            deposits += transaction[2]

        elif transaction[1] == "Withdrawal":
            withdrawals += transaction[2]

    print("\nMONTHLY SUMMARY")
    print("Total Deposits   :", deposits)
    print("Total Withdrawals:", withdrawals)
    print("Current Balance  :", account["balance"])


name = input("Enter account name: ")
balance = float(input("Enter initial balance: "))

account = create_account(name, balance)

while True:

    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Transactions")
    print("4. Monthly Summary")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = float(input("Amount to deposit: "))
        perform_transaction(account, amount, "deposit")

    elif choice == "2":
        amount = float(input("Amount to withdraw: "))
        perform_transaction(account, amount, "withdraw")

    elif choice == "3":
        show_transaction_history(account)

    elif choice == "4":
        monthly_summary(account)

    elif choice == "5":
        print("Current Balance:", account["balance"])

    elif choice == "6":
        print("Thank you for banking with us.")
        break

    else:
        print("Invalid choice.")


# Question No. 1

def encrypt_name(full_name, key):
    encrypted = ""

    for char in full_name:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            encrypted += new_char

        elif 'A' <= char <= 'Z':
            new_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            encrypted += new_char

        else:
            encrypted += char

    if key % 2 == 0:
        encrypted = encrypted[::-1]

    return encrypted


def decrypt_name(encrypted_text, key):
    if key % 2 == 0:
        encrypted_text = encrypted_text[::-1]

    decrypted = ""

    for char in encrypted_text:
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            decrypted += new_char

        elif 'A' <= char <= 'Z':
            new_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
            decrypted += new_char

        else:
            decrypted += char

    return decrypted


full_name = "Uzoma Favour Mmesoma"

first_name = full_name.split()[0]
key = len(first_name)

encrypted = encrypt_name(full_name, key)
decrypted = decrypt_name(encrypted, key)

print("Original :", full_name)
print("Key      :", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

# Question No. 3 

def calculate_average(scores_list):
    total = 0

    for score in scores_list:
        total += score

    return total / len(scores_list)


def get_grade(average):
    if average >= 70:
        return "A - Excellent"

    elif average >= 60:
        return "B - Very Good"

    elif average >= 50:
        return "C - Good"

    elif average >= 45:
        return "D - Fair"

    elif average >= 40:
        return "E - Pass"

    else:
        return "F - Fail"


def rank_students(student_data):
    results = []

    for student in student_data:
        name = student[0]
        scores = student[1]

        average = calculate_average(scores)
        grade = get_grade(average)

        results.append([name, average, grade])

    for i in range(len(results)):
        for j in range(i + 1, len(results)):
            if results[j][1] > results[i][1]:
                temp = results[i]
                results[i] = results[j]
                results[j] = temp

    print("\nRANKED STUDENTS")
    print("-" * 50)
    print("Pos\tName\t\tAverage\tGrade")
    print("-" * 50)

    for i in range(len(results)):
        print(
            i + 1,
            "\t",
            results[i][0],
            "\t",
            round(results[i][1], 2),
            "\t",
            results[i][2]
        )


students = [
    ("James", [80, 76, 90, 85]),
    ("Abraham", [65, 70, 60, 68]),
    ("Gabriel", [92, 88, 95, 90]),
    ("Precious", [50, 55, 45, 52]),
    ("Mercy", [72, 74, 78, 80])
]

rank_students(students)

# Question No. 4

def validate_credentials(username, password):
    result = {
        "username_valid": True,
        "password_valid": True,
        "errors": []
    }

    if len(username) < 6:
        result["username_valid"] = False
        result["errors"].append(
            "Username must be at least 6 characters."
        )

    if " " in username:
        result["username_valid"] = False
        result["errors"].append(
            "Username must not contain spaces."
        )

    if not username[0].isalpha():
        result["username_valid"] = False
        result["errors"].append(
            "Username must start with a letter."
        )

    upper = 0
    lower = 0
    digit = 0
    special = 0

    for char in password:

        if char.isupper():
            upper += 1

        else:
            if char.islower():
                lower += 1

            else:
                if char.isdigit():
                    digit += 1

                else:
                    special += 1

    if len(password) < 8:
        result["password_valid"] = False
        result["errors"].append(
            "Password must be at least 8 characters."
        )

    if upper == 0:
        result["password_valid"] = False
        result["errors"].append(
            "Password needs an uppercase letter."
        )

    if lower == 0:
        result["password_valid"] = False
        result["errors"].append(
            "Password needs a lowercase letter."
        )

    if digit == 0:
        result["password_valid"] = False
        result["errors"].append(
            "Password needs a digit."
        )

    if special == 0:
        result["password_valid"] = False
        result["errors"].append(
            "Password needs a special character."
        )

    return result


def generate_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length.")

    if not any(ch.isupper() for ch in password):
        suggestions.append("Add uppercase letters.")

    if not any(ch.islower() for ch in password):
        suggestions.append("Add lowercase letters.")

    if not any(ch.isdigit() for ch in password):
        suggestions.append("Add digits.")

    found_special = False

    for ch in password:
        if not ch.isalnum():
            found_special = True

    if not found_special:
        suggestions.append("Add special characters.")

    return suggestions


tests = [
    ("not", "12345"),
    ("25praise", "Password1!"),
    ("jennyfive", "Password1!"),
    ("student", "password"),
    ("student2", "PASSWORD"),
    ("student529", "StrongPass1!")
]

for username, password in tests:

    print("\nUsername:", username)
    print("Password:", password)

    result = validate_credentials(username, password)

    print("Result:", result)

    if not result["password_valid"]:
        print("Suggestions:")
        for item in generate_suggestions(password):
            print("-", item)


