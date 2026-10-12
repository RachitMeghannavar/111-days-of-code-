import pandas as pd

red = []
black = []
gray = []

data = pd.read_csv('squirrel_data.csv')
fur_column = data['Primary Fur Color']
for squirrel in fur_column:
    if squirrel == 'Gray':
        gray.append(squirrel)
    elif squirrel == 'Black':
        black.append(squirrel)
    elif squirrel == 'Cinnamon':
        red.append(squirrel)

print(len(gray), len(black), len(red))


df = pd.DataFrame(
    {
        'squirrels': ['red', 'black', 'gray'],
        'numbers': [len(gray), len(black), len(red)]
    }
)
df.to_csv('squirrel_data_analyzed.csv')