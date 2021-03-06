from pygame.sprite import Group

class GameStatus(object):
    """Current status of the game: game activity, score, best score,
       level and remaining lives"""

    def __init__(self, settings):
        self.best_score = 0
        self.score_per_alien = settings.score_per_alien
        self.score_per_level = settings.score_per_level
        self.restart()

    def restart(self):
        self.score = 0
        self.latest_score = 0
        self.level = 1
        self.lives = 3
        self.isRunning = False
        self.isPaused = False

    def updateScore(self, aliensDestroyed):
        """More aliens destroyed"""
        self.score += aliensDestroyed * self.score_per_alien

    def levelCompleted(self):
        """The level has been completed correctly"""
        self.score += self.score_per_level
        self.latest_score = self.score
        self.level += 1

    def restartLevelIfPossible(self):
        """Ship destroyed or aliens reached the bottom of the screen"""
        self.lives -= 1
        if self.lives == 0:
            if self.score > self.best_score:
                self.best_score = self.score
            self.restart()
        else:
            self.score = self.latest_score

