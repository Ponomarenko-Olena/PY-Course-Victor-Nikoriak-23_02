import json

'''Завантаження телефонної книги з файлу.'''
def load_phonebook(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

'''Збереження телефонної книги у файл.'''
def save_phonebook(filename, phonebook):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(phonebook, f, ensure_ascii=False, indent=4)

'''Додавання нового контакту.'''
def add_contact(phonebook):
    first_name = input("Ім'я: ").strip().capitalize()
    if len(first_name) < 2:
        print("Ім\'я має містити 2 та більше букв")
        return

    last_name = input('Прізвище: ').strip().capitalize()
    if len(last_name) < 2:
        print("Прізвище має містити 2 та більше букв")
        return

    phone = input('Номер телефону: ').strip()
    if not phone.isdigit():
        print("Номер має містити тільки цифри")
        return

    if len(phone) != 12:
        print("Номер має містити 12 цифр")
        return

    for contact in phonebook:
        if contact["phone"] == phone:
            print("Такий номер вже існує")
            return

    city = input('Місто: ').strip().capitalize()
    if len(city) < 2:
        print("Місто має містити 2 та більше букв")
        return

    state = input('Область: ').strip().capitalize()
    if len(state) < 2:
        print("Область має містити 2 та більше букв")
        return

    new_contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "city": city,
        "state": state
    }

    phonebook.append(new_contact)
    print("Контакт додано")

'''Пошук за ім'ям'''
def search_by_first_name(phonebook):
    first_name = input('Яке ім\'я шукаєте? ').strip()
    found_contacts = []

    for contact in phonebook:
        if first_name.lower() == contact["first_name"].lower():
            found_contacts.append(contact)

    if found_contacts:
        for contact in found_contacts:
            print(contact)

    else:
        print("Контакт не знайдено")

'''Пошук за прізвищем'''
def search_by_last_name(phonebook):
    last_name = input('Яке прізвище шукаєте? ').strip()
    found_contacts = []

    for contact in phonebook:
        if last_name.lower() == contact["last_name"].lower():
            found_contacts.append(contact)

    if found_contacts:
        for contact in found_contacts:
            print(contact)

    else:
        print("Контакт не знайдено")

'''Пошук за повним ім'ям'''
def search_by_full_name(phonebook):
    first_name = input('Яке ім\'я шукаєте? ').strip()
    last_name = input('Яке прізвище шукаєте? ').strip()
    found_contacts = []

    for contact in phonebook:
        if first_name.lower() == contact["first_name"].lower() and last_name.lower() == contact["last_name"].lower():
                found_contacts.append(contact)

    if found_contacts:
        for contact in found_contacts:
            print(contact)

    else:
        print("Контакт не знайдено")

'''Пошук за номером телефону'''
def search_by_phone(phonebook):
    phone = input('Який номер телефону шукаєте? ').strip()
    found_contacts = []

    for contact in phonebook:
        if phone == contact["phone"]:
            found_contacts.append(contact)

    if found_contacts:
        for contact in found_contacts:
            print(contact)

    else:
        print("Контакт не знайдено")

'''Пошук за містом або областю'''
def search_by_city_or_state(phonebook):
    city = input('Яке місто шукаєте? ').strip()
    state = input('Яку область шукаєте? ').strip()
    found_contacts = []

    if not city and not state:
        print('Треба ввести дані')
        return

    for contact in phonebook:
        if city and state:
            if city.lower() == contact["city"].lower() and state.lower() == contact["state"].lower():
                found_contacts.append(contact)

        elif city:
            if city.lower() == contact["city"].lower():
                found_contacts.append(contact)

        elif state:
            if state.lower() == contact["state"].lower():
                found_contacts.append(contact)

    if found_contacts:
        for contact in found_contacts:
            print(contact)

    else:
        print("Контакт не знайдено")

'''Видалити контакт за номером телефону'''
def delete_by_phone(phonebook):
    phone = input('Який номер телефону хочете видалити? ').strip()
    delete_contact = None

    for contact in phonebook:
        if phone == contact["phone"]:
            delete_contact = contact
            break

    if delete_contact is not None:
            phonebook.remove(delete_contact)
            print('Контакт знайдено та видалено')

    else:
        print("Контакт не знайдено")

'''Оновлення даних за номером телефону'''
def update_by_phone(phonebook):
    phone = input('Дані за яким номером хочете оновити? ').strip()
    found_contact = None

    for contact in phonebook:
        if phone == contact["phone"]:
            found_contact = contact
            break


    if found_contact is not None:
        print(found_contact)
        updated = False


        new_first_name = input("Ім'я: ").strip().capitalize()
        if len(new_first_name) >= 2:
            found_contact["first_name"] = new_first_name
            updated = True


        new_last_name = input("Прізвище: ").strip().capitalize()
        if len(new_last_name) >= 2:
            found_contact["last_name"] = new_last_name
            updated = True


        new_phone = input("Номер телефону: ").strip()
        if new_phone:
            if not new_phone.isdigit():
                print("Номер має містити тільки цифри")
                return

            if len(new_phone) != 12:
                print("Номер має містити 12 цифр")
                return

            for contact in phonebook:
                if contact["phone"] == new_phone and contact != found_contact:
                    print("Такий номер вже існує")
                    return

            found_contact["phone"] = new_phone
            updated = True


        new_city = input("Місто: ").strip().capitalize()
        if len(new_city) >= 2:
            found_contact["city"] = new_city
            updated = True


        new_state = input("Область: ").strip().capitalize()
        if len(new_state) >= 2:
            found_contact["state"] = new_state
            updated = True


        if updated:
            print("Контакт оновлено")
        else:
            print("Зміни не внесено")


    else:
        print("Контакт не знайдено")

'''Меню'''
def show_menu():
    print(
        '1 - Додати новий контакт\n',
        '2 - Пошук контакту за ім\'ям\n',
        '3 - Пошук контакту за прізвищем\n',
        '4 - Пошук контакту за повним ім\'ям\n',
        '5 - Пошук контакту за номером телефону\n',
        '6 - Пошук контакту за містом або областю\n',
        '7 - Видалити контакт за номером телефону\n',
        '8 - Оновлення даних за номером телефону\n',
        '0 - Вийти з програми\n'
         )

    answer = input('Введіть число: ').strip()
    return answer

import sys
def main():
    if len(sys.argv) < 2:
        print("Потрібно вказати назву файлу")
        return

    filename = sys.argv[1]

    try:
        phonebook = load_phonebook(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Файл не знайдено, створюю новий")
        phonebook = []


    while True:
        choice = show_menu()

        if choice == '1':
            add_contact(phonebook)

        elif choice == '2':
            search_by_first_name(phonebook)

        elif choice == '3':
            search_by_last_name(phonebook)

        elif choice == '4':
            search_by_full_name(phonebook)

        elif choice == '5':
            search_by_phone(phonebook)

        elif choice == '6':
            search_by_city_or_state(phonebook)

        elif choice == '7':
            delete_by_phone(phonebook)

        elif choice == '8':
            update_by_phone(phonebook)

        elif choice == '0':
            save_phonebook(filename, phonebook)
            print('Дані збережено')
            break

        else:
            print('Обери число з наявних в меню')

if __name__ == "__main__":
    main()