n = int(input())
people_tickets = [0]*n
tickets = []
for pupil in range(n):
    ticket = list(map(int, input().split()))
    tickets.append(ticket)
print(tickets)
if n == 1:
    print(tickets[0][0])
elif n == 2:
    print(min(tickets[0][0] + tickets[1][0], tickets[0][1]))
else:
    people_tickets[0] = tickets[0][0]
    people_tickets[1] = min(people_tickets[0]+tickets[1][0], tickets[0][1])
    people_tickets[2] = min(people_tickets[1]+tickets[2][0], people_tickets[0]+tickets[1][1], tickets[0][2])

    for index in range(3, n):
        people_tickets[index] = min(people_tickets[index-1]+tickets[index][0],
                                    people_tickets[index-2]+tickets[index][1],
                                    people_tickets[index-3]+tickets[index][2])
    print(people_tickets)