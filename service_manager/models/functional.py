import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from service_manager.db_models import get_orders_with_details
from functools import reduce

orders = get_orders_with_details()

active = list(filter(lambda o: o['status'] == 'Created' or o['status'] =="In Progress" , orders))

for order in active:
    print(dict(order))


completed = list(filter(lambda o: o['status'] == 'Completed', orders))

for order in completed:
    print(dict(order))

total_revenue = reduce(lambda acc, o: acc + o['total_price'], completed, 0.0)

print(total_revenue)

active_summaries = list(
    map(
        lambda o: f"{o['client_name']} - {o['service_name']} - {o['total_price']} грн",
        active
    )
)

print(active_summaries)

sorted_completed = sorted(
    completed,
    key=lambda o: o["created_at"],
    reverse=True
)

for order in sorted_completed:
    print(dict(order))

client_name = "Sofia"

client_orders = list(
    filter(
        lambda o: o["client_name"] == client_name,
        orders
    )
)

for order in client_orders:
    print(dict(order))

print("\nПідсумок:")
print(f"Активних замовлень: {len(active)}")
print(f"Завершених замовлень: {len(completed)}")
print(f"Загальна виручка: {total_revenue:.2f} грн")