import os
import logging

IGNORED_WORDS = os.getenv("IGNORED_WORDS", "uh,umm,hmm,haan").split(",")

class InterruptHandler:
    def __init__(self):
        self.ignored_words = {w.strip().lower() for w in IGNORED_WORDS}

    def is_filler_only(self, text):
        words = [w.lower() for w in text.split()]
        return all(w in self.ignored_words for w in words)

    def should_interrupt(self, text, agent_is_speaking):
        """Return True only if real interruption"""
        if not text.strip():
            return False

        if not agent_is_speaking:
            return True  # Always register when agent is silent

        # If agent is speaking:
        if self.is_filler_only(text):
            logging.info(f"Ignored filler while speaking: {text}")
            return False

        logging.info(f"Valid interruption detected: {text}")
        return True
