import os

class ScoreManager:
    def __init__(self, filename="highscore.txt"):
        self.filename = filename

    def load_highscore(self):
        """Reads the high score from the text file safely using exception handling."""
        try:
            if not os.path.exists(self.filename):
                return 0
            with open(self.filename, "r") as file:
                content = file.read().strip()
                return int(content) if content else 0
        except (IOError, ValueError):
            # Fallback if file is corrupted or unreadable
            return 0

    def save_highscore(self, new_score):
        """Saves the high score to the text file if the new score is higher."""
        current_high = self.load_highscore()
        if new_score > current_high:
            try:
                with open(self.filename, "w") as file:
                    file.write(str(new_score))
                return new_score
            except IOError:
                pass
        return current_high