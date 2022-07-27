def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix


def get_seating_map():
    bus_map = [['0']*4 for row in range(12)]
    with open ("reservations.txt" , "r") as file:
        for line in file:
            string  = line.split
            a = int(string[1])
            b = int(string[2])
            bus_map[a][b] = 'X'
        file.close()
        return bus_map

def total_sales(bus_map,cost_matrix):
    total = 0
    for a in range(12):
        for b in range(4):
            if bus_map[a][b] == 'X':
                total += cost_matrix[a][b]
    return total