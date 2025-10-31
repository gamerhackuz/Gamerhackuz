def kalkulyator():
    print("🧮 B poyton kolkulyator")
    print("Amallar: +  -  *  /")
    print("Chiqish uchun 'exit' deb yozing.\n")

    while True:
        amal = input("Amal girit(+, -, *, /) yo 'exit': ")

        if amal.lower() == "exit":
            print("tomom")
            break

        if amal not in ['+', '-', '*', '/']:
            print("❌xoto amal atingiz. Quri +,-,*,: ishlat")
            continue

        try:
            a = float(input("Birinchi sonni kiriting:"))
            b = float(input("Ikkinchi sonni kiriting: "))

            if amal == '+':
                natija = a + b
            elif amal == '-':
                natija = a - b
            elif amal == '*':
                natija = a * b
            elif amal == '/':
                if b == 0:
                    print("❌ Nola bo'lib bomidi")
                    continue
                natija = a / b

            print(f"jovop: {natija}\n")

        except ValueError:
            print("son girit\n")

kalkulyator()
