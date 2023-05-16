import pandas as pd
import random

def data_handle():
    """Read the dictionary
    Get the number of row and then create random number
    to select the word."""
    #read the verb dictionary
    df = pd.read_excel('data/verb.xlsx', )
    number_of_row = len(df.index)
    random_number = random.randint(0, number_of_row)
    word = df['word'][random_number]
    meaning = df['meaning'][random_number]
    print(f"{word} : {meaning}")




