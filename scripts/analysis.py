import os

import pandas as pd







if __name__ == '__main__':
    

    
    
    data_folder = os.path.join(os.path.dirname(os.getcwd()), 'data')
    print(data_folder)
    
    df = pd.read_csv(f"{data_folder}/aec-senate-formalpreferences-27966-VIC.csv")