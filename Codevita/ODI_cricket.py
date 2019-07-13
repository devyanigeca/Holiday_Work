OVER = 6


rr1 = float(input().strip())
striker, non_striker = list(map(int, input().strip().split()))
prev_deliveries = input().strip().split()
rr2 = float(input().strip())




temp = list(filter(lambda a: a != 'W', prev_deliveries))
temp = list(map(int, temp))

new_runs = sum(temp)

balls = len(prev_deliveries)

b = (balls * rr2 - 6 * new_runs) / (rr1 - rr2)

b = int(b)

score = b * rr1 / OVER
score = int(score)

# print(x, score)
balls = b

is_striker_on_strike = True
is_first_ball = True

for D in prev_deliveries:
    if balls % OVER == 0 and not is_first_ball:
        is_striker_on_strike = not is_striker_on_strike
    balls += 1
    is_first_ball = False
    if D == 'W':
        if is_striker_on_strike:
            striker = 0
        else:
            non_striker = 0
    elif is_striker_on_strike:
        striker += int(D)
        if int(D) % 2 != 0:
            is_striker_on_strike = not is_striker_on_strike
    else:
        non_striker += int(D)
        if int(D) % 2 != 0:
            is_striker_on_strike = not is_striker_on_strike

if balls % OVER == 0:
    is_striker_on_strike = not is_striker_on_strike

final_striker = 0
final_non_striker = 0

if is_striker_on_strike:
    final_striker = striker
    final_non_striker = non_striker
else:
    final_non_striker = striker
    final_striker = non_striker

print(score + new_runs, final_striker, final_non_striker, end='')