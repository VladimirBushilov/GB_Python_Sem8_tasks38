import json

phonebook_file = "phonebook.json"

def load_phonebook():
    try:
        with open(phonebook_file, "r") as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        phonebook = {}
    
    return phonebook

def save_phonebook(phonebook):
    with open(phonebook_file, "w") as file:
        json.dump(phonebook, file)

def add_contact(name, phone_number):
    phonebook = load_phonebook()
    phonebook[name] = phone_number
    save_phonebook(phonebook)

def remove_contact(name):
    phonebook = load_phonebook()
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
    else:
        print("Контакт не найден")

def update_contact(name, new_phone_number):
    phonebook = load_phonebook()
    if name in phonebook:
        phonebook[name] = new_phone_number
        save_phonebook(phonebook)
    else:
        print("Контакт не найден")

def print_phonebook():
    phonebook = load_phonebook()
    print("Телефонный справочник:")
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")

add_contact("Бушилов", "+7 (999) 123-45-67")
add_contact("Моднов", "+7 (999) 987-65-43")
add_contact("Сидоренко", "+7 (999) 456-12-34")

print_phonebook()

remove_contact("Моднов")

update_contact("Сидоренко", "+7 (999) 111-22-33")

print_phonebook()