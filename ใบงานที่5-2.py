score = float(input("กรุณากรอกคะแนนของคุณ): "))
if score >= 80:
    print("เกรด A")
elif 70 <= score <= 79:
    print("เกรด B")
elif 60 <= score <= 69:
    print("เกรด C")
elif 50 <= score <= 59:
    print("เกรด D")
else:
    print("เกรด F")
