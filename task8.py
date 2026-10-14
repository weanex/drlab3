# task8_car_wash.py

import random
from task4_structures import Queue


def simulate_car_wash(
    total_minutes=120,
    arrival_prob=0.3,
    wash_time_min=3,
    wash_time_max=8,
    seed=42,
):
    random.seed(seed)

    wash_queue = Queue()
    time_left = 0
    total_wait = 0
    max_wait = 0
    cars_served = 0
    cars_arrived = 0

    queue_len_sum = 0
    minutes_counted = 0

    for minute in range(1, total_minutes + 1):
        if random.random() < arrival_prob:
            wash_queue.enqueue({"arrival": minute})
            cars_arrived += 1

        if time_left == 0 and not wash_queue.is_empty():
            car = wash_queue.dequeue()
            wait = minute - car["arrival"]
            total_wait += wait
            max_wait = max(max_wait, wait)
            time_left = random.randint(wash_time_min, wash_time_max)

        if time_left > 0:
            time_left -= 1
            if time_left == 0:
                cars_served += 1

        queue_len_sum += wash_queue.size()
        minutes_counted += 1

    avg_wait = total_wait / cars_served if cars_served else 0
    avg_queue_len = queue_len_sum / minutes_counted if minutes_counted else 0

    return {
        "cars_arrived": cars_arrived,
        "cars_served": cars_served,
        "cars_left_in_queue": wash_queue.size(),
        "avg_wait_min": round(avg_wait, 2),
        "max_wait_min": max_wait,
        "avg_queue_len": round(avg_queue_len, 2),
    }


if __name__ == "__main__":
    print(" Задание №8:")

    print("Сценарий: автомойка с 1 постом, 120 минут наблюдения.")
    print("Предположения:")
    print("  - вероятность приезда машины за минуту: 0.3")
    print("  - время мойки: равномерно 3..8 минут")
    print("  - обслуживание FIFO, одна машина за раз\n")

    stats = simulate_car_wash(total_minutes=120, arrival_prob=0.3,
                              wash_time_min=3, wash_time_max=8, seed=42)

    for k, v in stats.items():
        print(f"  {k}: {v}")

    assert stats["cars_arrived"] > 0
    assert stats["cars_served"] > 0
    assert stats["cars_served"] <= stats["cars_arrived"]

    print("\n Прогон с разными seed")
    for s in [1, 2, 3, 4, 5]:
        st = simulate_car_wash(seed=s)
        print(f"  seed={s}: приехало={st['cars_arrived']}, обслужено={st['cars_served']}, "
              f"среднее ожидание={st['avg_wait_min']}, макс. ожидание={st['max_wait_min']}")