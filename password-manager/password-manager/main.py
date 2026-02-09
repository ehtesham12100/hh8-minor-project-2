from storage import save_entry, read_entries, delete_entry
import pyperclip
import time

print("🔐 PASSWORD MANAGER")

master_password = input("Enter Master Password: ")

def add_password():
    site = input("Website/App: ")
    username = input("Username: ")
    password = input("Password: ")

    save_entry(site, username, password, master_password)
    print("✅ Password saved securely!")

def view_passwords():
    entries = read_entries(master_password)

    if not entries:
        print("❌ No entries found.")
        return

    print("\nSaved Credentials:")
    for i, entry in enumerate(entries, start=1):
        site, user, pwd = entry.split("|")
        print(f"{i}. {site} | {user} | {pwd}")

    choice = input("\nEnter number to copy password (or press Enter to skip): ")
    if choice.isdigit():
        index = int(choice) - 1
        pwd = entries[index].split("|")[2]
        copy_to_clipboard(pwd)

def delete_password():
    entries = read_entries(master_password)

    if not entries:
        print("❌ No entries to delete.")
        return

    print("\nSaved Credentials:")
    for i, entry in enumerate(entries, start=1):
        site, user, pwd = entry.split("|")
        print(f"{i}. {site} | {user}")

    choice = input("\nEnter number to delete: ")

    if choice.isdigit():
        success = delete_entry(int(choice) - 1, master_password)
        if success:
            print("🗑️ Password deleted successfully!")
        else:
            print("❌ Invalid selection.")

def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("📋 Password copied! Will clear in 10 seconds...")
    time.sleep(10)
    pyperclip.copy("")
    print("🧹 Clipboard cleared!")

while True:
    print("\n1. Add Password")
    print("2. View Passwords")
    print("3. Delete Password")
    print("4. Exit")

    option = input("Choose option: ")

    if option == "1":
        add_password()
    elif option == "2":
        view_passwords()
    elif option == "3":
        delete_password()
    elif option == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option.")
