import re

class validation:
    def __init__(self) -> None:
        pass

    def is_valid_mood(self, mood: str) -> bool:
        return bool(mood and mood.strip())
    
    def is_valid_log(self, log: str) -> bool:
        return bool(log and log.strip())