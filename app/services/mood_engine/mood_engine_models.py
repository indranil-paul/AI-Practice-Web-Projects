from pydantic import BaseModel
from enum import Enum


# =================
# Mood Models 
# =================

DEFAULT_FACE = "(?_?)"


class Mood(str, Enum):
    AFRAID = "afraid"
    CONFUSED = "confused"
    CRY = "cry"
    DIZZY = "dizzy"
    ERROR = "error"
    FAIL = "fail"
    HAPPY = "happy"
    NEUTRAL = "neutral"
    SAD = "sad"
    SLEEPY = "sleepy"
    SMILE = "smile"
    THINKING = "thinking"
    UNIMPRESSED = "unimpressed"
    VERY_HAPPY = "very_happy"
    VERY_TIRED = "very_tired"
    WINK = "wink"
    WOW = "wow"

    @property
    def face(self) -> str:
        return {
            Mood.AFRAID: "(o_o)",
            Mood.CONFUSED: "(?_?)",
            Mood.CRY: "(;_;)",
            Mood.DIZZY: "(@_@)",
            Mood.ERROR: "(>_<)",
            Mood.FAIL: "(x_x)",
            Mood.HAPPY: "(^_^)",
            Mood.NEUTRAL: "('_')",
            Mood.SAD: "(T_T)",
            Mood.SLEEPY: "(-_-)",
            Mood.SMILE: "(^.^)",
            Mood.THINKING: "(o_O)",
            Mood.UNIMPRESSED: "(e_e)",
            Mood.VERY_HAPPY: "(^o^)",
            Mood.VERY_TIRED: "(=_=)",
            Mood.WINK: "(^_~)",
            Mood.WOW: "(O_O)",
        }.get(self, DEFAULT_FACE)


class MoodResponse(BaseModel):
    mood: Mood
