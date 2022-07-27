global seating_chart
seating_chart = [['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['0', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O'],
                ['O', 'O', '0', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O']]
rows = len(seating_chart)
lista = []
reservations = []
with open("reservations.txt", "r") as text:
    lines = text.readlines()
for l in lines:
    temp = []
    as_list = l.split("," " ")
    index1 = int(as_list[1])
    index2 = int(as_list[2])
    seating_chart[index1][index2] = 'X'
print(seating_chart)