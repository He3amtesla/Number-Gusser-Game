class score:
    def __init__(self, initial_score=10):
        self.score = initial_score
    
    def decrement_score(self, penalty = 1):
        self.score -= penalty
        self.score = max(0, self.score)
        
    def get_score(self):
        return self.score