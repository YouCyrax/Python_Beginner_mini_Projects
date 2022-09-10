import random
# rock > scissors, scissors > paper, paper > rock
def play():
    user = input("What is you choice ? 'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice((['r', 'p', 's']))
    if user == computer:
        return 'It is a tie'
    if is_win(user, computer):
        return "You win the game!"
    return "You loose the game!"

def is_win(player, opponent):
    # this function return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())