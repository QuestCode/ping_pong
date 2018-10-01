class GameStats():
    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ai_settings.left_paddle_score = 0
        self.ai_settings.right_paddle_score = 0
