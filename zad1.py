'''
Program do przydzielania oceny z testu:

proszę założyć skalę ocen standardową na Uczelni,

proszę stworzyć zmienną zawierającą wynik punktowy z testu, z przedziału 0 – 100 (0.5 pkt),

proszę wypisać na ekranie ocenę z testu, w skali ocen standardowej na Uczelni, np. bardzo dobry, na bazie wartości punktowej z testu (2 pkt),

proszę zweryfikować działanie programu, gdy wprowadzona wartość będzie z przedziału innego niż 0 – 100; jakie powinno być zachowanie programu w tej sytuacji? (1 pkt)
'''

scale_marks = {
    0: "2",
    35: "3",
    40: "3.5",
    50: "4",
    60: "4.5",
    70: "5",
    90: "5.5",
}

while True:
    test_result = float(input("Enter the test score (0-100): "))

    if 0 <= test_result <= 100:
        mark = None
        for points, name_mark in scale_marks.items():
            if test_result >= points:
                mark = name_mark
        print(f"Test grade: {mark}")
    else:
        print("The test score should be in the range of 0-100")