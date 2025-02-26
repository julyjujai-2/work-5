income = float(input("กรุณากรอกขนาดหน้าอกของคุณ (ซม.): "))
if income <= 34:
    print("ขนาดเสื้อ: XS")
elif income <= 36:
    print("ขนาดเสื้อ: S")
elif income <= 38:
    print("ขนาดเสื้อ: M")
elif income <= 40:
    print("ขนาดเสื้อ: L")
else:
    print("ขนาดเสื้อ: XL")
