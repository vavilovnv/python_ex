# Условие задачи https://stepik.org/lesson/13238/step/10?unit=3424

# Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака
# 0≤W≤2⋅10^6. Каждая из следующих n строк задаёт стоимость 0≤c≤2⋅10^6 и объём
# 0<w≤2⋅10^6 предмета (n, W, c_i, w_i — целые числа). Выведите максимальную
# стоимость частей предметов (от каждого предмета можно отделить любую часть,
# стоимость и объём при этом пропорционально уменьшатся), помещающихся в
# данный рюкзак, с точностью не менее трёх знаков после запятой.

def backpack_filling(capacity: int, goods: list) -> str:
    """Применение жадного алгоритма для расчета максимальной стоимости
    товаров, которые могут поместиться в рюкзак определенного объема.
    За достоверный шаг берется выбор самого дорогого товара в переданном
    отсортированном списке."""
    
    price = 0
    for cost, weight in goods:
        if capacity >= weight:
            capacity -= weight
            price += cost
        else:
            price += cost / weight * capacity
            break
    return price


if __name__ == '__main__':
    goods_amount, capacity = list(map(int, input().split()))
    goods = sorted(
        [[int(i) for i in input().split()] for _ in range(goods_amount)],
        key=lambda x: x[0] / x[1],
        reverse=True
    )
    print(f'{backpack_filling(capacity, goods):.3f}')
