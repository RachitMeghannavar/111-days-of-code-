for i in range(1, 5):
    print(f"{i} inside the block")

#PYTHON IS NOT BLOCK SCOPED
#THAT MEANS YOU CAN ACCESS THE VARIABLES FROM THE OUTSIDE OF BLOCK
#IT APPLIES FOR 'for,while,if,else' statements
print(f"{i} outside the block")