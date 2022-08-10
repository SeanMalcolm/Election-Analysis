import os

import pandas as pd



class Voter:
    
    relevant_parties = [
        'D:Liberal/The Nationals',
        'K:Australian Labor Party',
        'U:The Greens'                                                    
        ]
    
    def __init__(self, senate_ballot : pd.Series, division : str, collection_point : str):
        
        self.division = division
        self.collection_point = collection_point
        self.ballot = self.convert_ballot(senate_ballot)
        
        
    def convert_ballot(self, ballot : pd.Series):
        
        ballot = ballot.sort_values()
        return(list(ballot.index))
        
    
def generate_voters(senate_votes : pd.DataFrame):
    
    voters = []
    for index, row in senate_votes.iterrows():
        division = row['Division']
        collection_point = row['Vote Collection Point Name']
        ballot = row[Voter.relevant_parties]
        new_voter = Voter(senate_ballot = ballot, division=division, collection_point=collection_point)
        voters.append(new_voter)
    return(voters)


def read_senate_data():
    
    data_folder = os.path.join(os.path.dirname(os.getcwd()), 'data')
    senate_votes = pd.read_csv(f"{data_folder}/aec-senate-formalpreferences-27966-VIC.csv", nrows=100)
    return senate_votes


if __name__ == '__main__':
    

    senate_votes = read_senate_data()
    generate_voters(senate_votes)