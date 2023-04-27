import random

def choose_options():
  options = ('rock', 'paper', 'scissors')
  user_option = input('Choose An Option: Rock, Paper or Scissor => \n')
  user_option = user_option.lower()

  if not user_option in options:
    print("that's option is not Valid")
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("It's was a Tie!")
  elif user_option == 'rock':
    if computer_option == 'scissors':
      print('Rock Wins to Scissors')
      print('User Win!')
      user_wins += 1
    else:
      print('Paper Win to Rock')
      print('Computer Win!')
      computer_wins += 1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('Paper Win to Rock')
      print('User Win')
      user_wins += 1
    else:
      print('Scissors Win to Paper')
      print('Computer Win!')
      computer_wins += 1
  elif user_option == 'scissors':
    if computer_option == 'paper':
      print('Scissors Win to Paper')
      print('User Win!')
      user_wins += 1
    else:
      print('Rock Win to Scissors')
      print('Computer Win!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('The Winner Is The Computer!!!')
      break

    if user_wins == 2:
      print('The Winner is the User!!!')
      break

run_game()