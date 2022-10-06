# пример асинхронного исполнения кода
import asyncio


async def waiter():
    task1 = asyncio.create_task(to_cook('Борщ', 80))
    task2 = asyncio.create_task(to_cook('Суп', 40))
    task3 = asyncio.create_task(to_cook('Второе', 150))

    await task1
    await task2
    await task3


async def to_cook(order, time):
    print(f'Новый заказ:{order}')
    await asyncio.sleep(time)
    print(order, '-готово')

asyncio.run(waiter())
