import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title('U.S.A. States Games')

# Load an image as a new shape
image = '/Users/macintosh/Downloads/day-25-us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('/Users/macintosh/Downloads/day-25-us-states-game-start/50_states.csv')
states_list = data['state'].to_list()

guessed_states = []
states_correct = 0
continue_game = True

while continue_game:
    answer = screen.textinput(f'{states_correct}/50 States Correct', 'Guess the name of a state: ').title()
    print(answer)
    
    if answer in states_list:
        t = turtle.Turtle()
        t.hideturtle() # Hides turtle icon
        t.penup() # Doesn't draw anything
        
        state_data = data[data['state'] == answer]
        x = state_data['x'].item()
        y = state_data['y'].item()
        t.goto(x,y)
        t.write(state_data['state'].item())
        
        guessed_states.append(answer)
        states_correct += 1
    
    elif answer == 'Exit':
        continue_game = False
        
    if states_correct == 50:
        print('Good job!')
        continue_game = False
       
states_to_learn = []

for state in states_list:
    if state not in guessed_states:
        states_to_learn.append(state)
        
data_dict = {
    'state': states_to_learn
    }

new_data = pd.DataFrame(data_dict)
new_data.to_csv('/Users/macintosh/Desktop/states_to_learn.csv')
