import asyncio
import random
from typing import List

#нагуглилим решение на stackoverflow

# Разделяемое между запросами состояние сервера
class SharedState:
    items: List[int]

    def __init__(self):
        self.items = []

    # функция, модифицирующая состояние сервера
    # asyncio.sleep используется для имитации долгой работы функции
    async def modify(self, value: int):
        await asyncio.sleep(random.randint(1, 2))
        self.items.append(value)

# Имитация сервера, обрабатывающего запросы
# В нашем случае "запросы" модифицируют состояние сервера
# добавляя элементы в конец списка 'items'
class Server:
    state: SharedState
    semaphore: asyncio.Semaphore   #используем lock

    def __init__(self, state: SharedState):
        self.state = state
        self.semaphore = asyncio.Semaphore(1) #corutines на 1


    async def handle_request(self, value: int):
        async with self.semaphore: #синхронизируем с lockom
            await self.state.modify(value)


async def main():
    state = SharedState()
    server = Server(state)

    # имитируем запуск 10 запросов к серверу
    requests = [server.handle_request(value) for value in range(10)]
    await asyncio.gather(*requests)

    '''
    !!! В данной задаче нельзя модифицировать код - только добавлять новый !!!

    задача заключается в том, чтобы только средствами asyncio
    заставить запросы работать последовательно (исключить data race)
    state в результате обработки запросов должен удовлетворять следующему условию:
    '''
    print(state.items == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    for item in state.items:
        print(item)

if __name__ == '__main__':
    asyncio.run(main())
    # --> [True, 0...9]