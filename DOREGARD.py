import random  # برای تولید اعداد تصادفی
import math    # برای استفاده از توابع ریاضی
import numpy as np  # برای کار با آرایه‌ها و محاسبات عددی بهینه‌تر
import matplotlib.pyplot as plt  # برای رسم گرافیکی

# محاسبه فاصله بین دو شهر که به صورت دو نقطه در فضای دو بعدی تعریف شده‌اند
def MASAFAT(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# تولید شهرهای تصادفی و ذخیره به صورت تاپل بین بازه 0 تا 100
def TOLID_SHAHR(num_cities):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]

# محاسبه مجموع فاصله‌ها در یک مسیر
def TAMAME_MASIR(route, distances):
    return sum(distances[route[i], route[i + 1]] for i in range(-1, len(route) - 1))

# تابع شبیه‌ساز الگوریتم تبرید
def ALGORITHM_TABRID(cities, initial_temp, cooling_rate):
    num_cities = len(cities)
    current_route = list(range(num_cities))
    random.shuffle(current_route)  # تولید مسیر اولیه به صورت تصادفی
    current_distance = TAMAME_MASIR(current_route, distances)

    best_route = current_route[:]
    best_distance = current_distance

    temperature = initial_temp

    while temperature > 1:
        # انتخاب دو شهر به صورت تصادفی برای جابجایی
        i, j = random.sample(range(num_cities), 2)
        new_route = current_route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]  # جابجایی دو شهر
        new_distance = TAMAME_MASIR(new_route, distances)

        # پذیرش مسیر جدید بر اساس شرایط الگوریتم تبرید
        if new_distance < current_distance or random.uniform(0, 1) < math.exp((current_distance - new_distance) / temperature):
            current_route = new_route
            current_distance = new_distance

        # به‌روزرسانی بهترین مسیر و فاصله
        if current_distance < best_distance:
            best_distance = current_distance
            best_route = current_route[:]

        # کاهش دما
        temperature *= cooling_rate

    return best_route, best_distance

# تنظیمات اولیه
num_cities = 50
cities = TOLID_SHAHR(num_cities)

# محاسبه فاصله‌ها بین شهرها
distances = np.array([[MASAFAT(city1, city2) for city2 in cities] for city1 in cities])

# پارامترهای الگوریتم
initial_temp = 1000
cooling_rate = 0.995

# اجرای الگوریتم
best_route, best_distance = ALGORITHM_TABRID(cities, initial_temp, cooling_rate)

# نمایش نتایج
print("BEHTARIN MASAFAT(TAGHRIBI):", best_route)
print("TAMAME MASAFAT:", best_distance)

# رسم گرافیکی
plt.figure(figsize=(10, 6))
# رسم نقاط شهرها
x, y = zip(*cities)
plt.scatter(x, y, color='blue', label='Cities')

# رسم مسیر بهینه
best_route_coords = [cities[i] for i in best_route] + [cities[best_route[0]]]  # اضافه کردن اولین شهر برای بستن مسیر
x_route, y_route = zip(*best_route_coords)
plt.plot(x_route, y_route, color='red', linewidth=2, label='Best Route')

# تنظیمات گراف
plt.title('Best Route for Traveling Salesman Problem')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid()
plt.show()