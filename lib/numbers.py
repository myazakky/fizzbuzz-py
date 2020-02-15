"""create numbers"""

INT_0 = int()

INT_1 = len(str(int()))

STR_100 = str(INT_1) + str(INT_0) + str(INT_0)
INT_100 = int(STR_100)

INT_3 = INT_1 + INT_1 + INT_1

INT_5 = INT_3 + INT_1 + INT_1

INT_15 = INT_3 * INT_5
