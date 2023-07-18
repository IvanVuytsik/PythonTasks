import os, re

# в папке test найти все файлы filenames вывести количество
def task1(filenames):
    # счет файлов
    folder_path = 'test'
    file_count = 0
    # emails
    emails = set()
    symbols = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    for root, _, files in os.walk(folder_path):
        #print(root, _, files)
        for filename in files:
            #print(filename)
            for name_to_find in filenames:
                  #print(name_to_find, root, _, files)
                  if name_to_find in filename:
                     file_count += 1
                     #break
            #ищем имеил в текущем файле
            file_path = os.path.join(root, filename)
            with open(file_path) as f:
                file_content = f.read()

                found_emails = re.findall(symbols, file_content)
                emails.update(found_emails)

    print(f"Number of files / emails: {file_count}, {emails}")

    if emails:
        for email in emails:
            print(email)
    else:
        print("No emails")


def task2():
    # в папке test найти все email адреса записанные в файлы
    pass

def main():
    task1(["filenames"])
    #task2()
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)


if __name__ == '__main__':
    main()