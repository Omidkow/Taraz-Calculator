darsad_riaziat_karbar = float(input("Riaziat: "))
darsad_fizik_karbar = float(input("Fizik: "))
darsad_shimi_karbar = float(input("Shimi: "))

# اطلاعات دروس
doroos = {
    "riaziat": {"darsad_shakhes": 100, "taraz_shakhes": 13114, "miangin": 23.88, "darsad_karbar": darsad_riaziat_karbar, "weight": 12},
    "fizik":   {"darsad_shakhes": 100, "taraz_shakhes": 12738, "miangin": 26.9, "darsad_karbar": darsad_fizik_karbar, "weight": 9},
    "shimi":   {"darsad_shakhes": 100, "taraz_shakhes": 14290, "miangin": 17.26, "darsad_karbar": darsad_shimi_karbar, "weight": 7},
}

# فرمول محاسبه تراز (T = Ax + B)
# ماز
A , B = 2000, 7850
# مدارس برتر
# A , B = 2000, 5000

def tarazDars(miangin, taraz_shakhes , darsad_shakhes, darsad_karbar, **kwargs):
    z = (taraz_shakhes - B)/A
    s = (darsad_shakhes - miangin)/z
    taraz_karbar = ((darsad_karbar - miangin)/s)*A + B
    return int(taraz_karbar)

# محاسبه تراز تک‌تک دروس
for name, info in doroos.items():
    info["taraz"] = tarazDars(**info)
    print(f'taraz e shoma dar dars {name}: {info["taraz"]}')

# محاسبه تراز کل
sum_weights = sum(info["weight"] for info in doroos.values())
weighted_taraz = sum(info["taraz"] * info["weight"] for info in doroos.values())
taraz_kol = int(weighted_taraz / sum_weights)

print(f'Taraz kol: {taraz_kol}')


#  بخش رسم نمودار با matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))

for name, info in doroos.items():
    x = np.linspace(0, 100, 101)  # درصد از 0 تا 100
    y = [tarazDars(info["miangin"], info["taraz_shakhes"], info["darsad_shakhes"], d, weight=info["weight"]) for d in x]
    plt.plot(x, y, label=name)

plt.xlabel("درصد")
plt.ylabel("تراز")
plt.title("رابطه درصد و تراز در هر درس")
plt.legend()
plt.grid(True)
plt.show()