import voter_generation

import math


class Election:
    
    
    def __init__(self, voters : list, parties : list):
        
        self.voters = voters
        self.parties = parties
        
        
    def run_election(self):

        current_votes = {party : [] for party in self.parties}
                         
        N = len(self.voters)
        
        stage = 0
        while True:
            if stage == 0:
                for voter in self.voters:
                    current_votes[voter.ballot[0]].append(voter)
            else:
                #Check if over
                if self.get_current_winner(current_votes)['votes'] > N/2:
                    break
                else:
                    eliminated = self.get_current_loser(current_votes)['party']
                    for i, voter in enumerate(current_votes[eliminated]):
                        current = voter.ballot.index(eliminated)
                        i = current + 1
                        while i < len(voter.ballot):
                            next_preferred = voter.ballot[i]
                            if next_preferred in current_votes:
                                current_votes[next_preferred].append(voter)
                                break
                            else:
                                i += 1  
                current_votes[eliminated] = []
                
            for party in current_votes:
                print(f'------Stage {stage}---------')
                print(f'{party} : {len(current_votes[party])}')
            stage += 1
            
    def get_current_winner(self, votes):
        max_i = None
        max_v = 0
        for party in votes:
            if len(votes[party]) > max_v:
                max_i = party
                max_v = len(votes[party])   
        return({'party' : max_i, 'votes' : max_v})
    
    def get_current_loser(self, votes):
        
        min_i = None
        min_v = math.inf
        for party in votes:
            if len(votes[party]) < min_v:
                min_i = party
                min_v = len(votes[party])
        return({'party' : min_i, 'votes' : min_v})
    


if __name__ == '__main__':
    
    
    
    senate_votes = voter_generation.read_senate_data()
    print("data read")
    senate_votes = senate_votes[senate_votes['Division'] == 'Higgins']
    voters = voter_generation.generate_voters(senate_votes)
    print('voters_generated')
    relevant_parties = voter_generation.get_relevant_parties()
    
    election = Election(voters=voters, parties=relevant_parties)
    election.run_election()
    
    