from crypto_utils import encrypt_data, decrypt_data

VAULT_FILE = "vault.db"

def save_entry(site, username, password, master_password):
    data = f"{site}|{username}|{password}"
    encrypted = encrypt_data(data, master_password)

    with open(VAULT_FILE, "ab") as file:
        file.write(encrypted + b"\n")

def read_entries(master_password):
    entries = []

    try:
        with open(VAULT_FILE, "rb") as file:
            for line in file:
                try:
                    decrypted = decrypt_data(line.strip(), master_password)
                    entries.append(decrypted)
                except:
                    pass
    except FileNotFoundError:
        pass

    return entries

def delete_entry(index, master_password):
    entries = read_entries(master_password)

    if index < 0 or index >= len(entries):
        return False

    entries.pop(index)

    # rewrite vault
    with open(VAULT_FILE, "wb") as file:
        for entry in entries:
            encrypted = encrypt_data(entry, master_password)
            file.write(encrypted + b"\n")

    return True
