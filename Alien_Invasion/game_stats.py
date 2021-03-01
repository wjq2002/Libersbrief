import pickle

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.load_high_score()

    def save_high_score(self):
        f = open("D:\high_score.pkl", 'wb')
        pickle.dump(str(self.high_score), f, 0)
        f.close()

    def load_high_score(self):
        f = open("D:\high_score.pkl", 'rb')
        try:
            str_high_score = pickle.load(f)
            self.high_score = int(str_high_score)
        except EOFError:
            self.high_score = 0
        finally:
            f.close()