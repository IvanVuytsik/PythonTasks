import os

def black_book(page: int) -> bool:
    status_code = os.system(f"./black-book -n {page}")
    return status_code == 0

# тупо
def no_algo_find_last_page(min_page, max_page):

    while min_page < max_page:
        mid_page = (min_page + max_page) // 2

        if black_book(min_page):
            print(f"The last page is: {min_page}")
            break
        elif black_book(max_page):
            print(f"The last page is: {max_page}")
            break
        elif black_book(mid_page):
            print(f"The last page is: {mid_page}")
            break
        else:
            min_page += 1
            max_page -= 1
            print(min_page, max_page)

# лучше
def find_last_page():
    min_page = 1
    #используем binary search и разобьем на куски
    while min_page < 10000000 and not black_book(min_page):
        min_page *= 2
    # binary search
    left, right = min_page // 2, min(min_page, 10000000)
    while left <= right:
        mid = (left + right) // 2
        if black_book(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right

def main():
    #min_page = 1
    #max_page = 10000000
    # no_algo_find_last_page(min_page, max_page)

    last_page = find_last_page()
    print(f'Last page: {last_page}')
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.

    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    
    black_book возвращает True, если страница последняя
              возвращает False, если страница не последняя.
 
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # тут явно нужен алгоритм.


if __name__ == '__main__':
    main()