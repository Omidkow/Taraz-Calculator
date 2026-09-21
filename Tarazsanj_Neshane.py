import numpy as np

# ۱. ثابت‌ها
A, B = 2000, 7850  # ماز
# A, B = 2000, 5000  # مدارس برتر

# ۲. دریافت ورودی‌ها
darsad_riaziat_karbar = float(input("Riaziat: "))
darsad_fizik_karbar = float(input("Fizik: "))
darsad_shimi_karbar = float(input("Shimi: "))

# ۳. ساختار داده دروس
doroos = {
    "riaziat": {"darsad_shakhes": 100, "taraz_shakhes": 13114, "miangin": 23.88, "darsad_karbar": darsad_riaziat_karbar, "weight": 12},
    "fizik":   {"darsad_shakhes": 100, "taraz_shakhes": 12738, "miangin": 26.9,  "darsad_karbar": darsad_fizik_karbar,   "weight": 9},
    "shimi":   {"darsad_shakhes": 100, "taraz_shakhes": 14290, "miangin": 17.26, "darsad_karbar": darsad_shimi_karbar,   "weight": 7},
}

# ۴. تابع محاسبه تراز
def calc_taraz(miangin, taraz_shakhes, darsad_shakhes, darsad_karbar):
    z = (taraz_shakhes - B) / A
    s = (darsad_shakhes - miangin) / z
    return ((darsad_karbar - miangin) / s) * A + B

# ۵. محاسبه تراز تک‌تک دروس و تراز کل
sum_weights = 0
weighted_taraz_sum = 0

for name, info in doroos.items():
    taraz = int(calc_taraz(info["miangin"], info["taraz_shakhes"], info["darsad_shakhes"], info["darsad_karbar"]))
    info["taraz"] = taraz
    print(f'taraz e shoma dar dars {name}: {taraz}')
    sum_weights += info["weight"]
    weighted_taraz_sum += taraz * info["weight"]

taraz_kol = int(weighted_taraz_sum / sum_weights)
print(f'Taraz kol: {taraz_kol}')


# ۶. بخش رسم نمودار
PLOT_GRAPH = True

if PLOT_GRAPH:
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        x = np.linspace(0, 100, 101) 

        for name, info in doroos.items():
            y = calc_taraz(info["miangin"], info["taraz_shakhes"], info["darsad_shakhes"], x)
            plt.plot(x, y, label=name)

        plt.xlabel("درصد")
        plt.ylabel("تراز")
        plt.title("رابطه درصد و تراز در هر درس")
        plt.legend()
        plt.grid(True)
        plt.show()

    except ImportError:
        print("\n[راهنما]: کتابخانه matplotlib نصب نیست؛ نمودار رسم نشد.")