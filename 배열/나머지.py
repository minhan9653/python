sub_number = set()
for _ in range(9):
    su_number = int(input())
    sub_number.add(su_number)
missing_number = list(set(range(1,11))) - sub_number
missing_number.sort
print(missing_number[0])
print(missing_number[1])