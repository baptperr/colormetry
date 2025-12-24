import random

class Question():
    def __init__(self, text, answers):
        self.text = text
        self.answers = answers

class Answer():
    def __init__(self, text, r, y, b):
        self.text = text
        self.r = r
        self.y = y
        self.b = b

def shuffle(lst):
    random.shuffle(lst)
    return lst

question1 = Question(
    text='When something important fails, what usually feels most true?',
    answers=shuffle([
    Answer(text='The situation was stacked against me',
       r=0,
       y=0,
       b=0),
    Answer(text='I made some mistakes, but it was mostly circumstantial',
       r=1,
       y=0,
       b=0),
    Answer(text='I didn’t yet find the right lever or approach',
       r=2,
       y=0,
       b=0),
    Answer(text='I underestimated my responsibility in the outcome',
       r=3,
       y=0,
       b=0)]
))

question2 = Question(
    text='You’re stuck in a role or situation you dislike. What’s your most likely response?',
    answers=shuffle([
    Answer(text='Wait until conditions change',
       r=0,
       y=0,
       b=0),
    Answer(text='Vent, then adapt emotionally',
       r=1,
       y=0,
       b=0),
    Answer(text='Look for side exits or experiments',
       r=2,
       y=0,
       b=0),
    Answer(text='Actively redesign or leave, even at cost',
       r=3,
       y=0,
       b=0)]
))

question3 = Question(
    text='Which statement feels closest to how you operate?',
    answers=shuffle([
    Answer(text='Most outcomes are determined by forces larger than individuals',
       r=0,
       y=0,
       b=0),
    Answer(text='Individuals can influence outcomes within limits',
       r=1,
       y=0,
       b=0),
    Answer(text='Individuals create disproportionate outcomes by how they act',
       r=3,
       y=0,
       b=0),
    Answer(text='Constraints are real, but rarely decisive',
       r=2,
       y=0,
       b=0)]
))

question4 = Question(
    text='When someone strongly disagrees with you on an important topic, your instinct is to:',
    answers=shuffle([
    Answer(text='Explain your position more clearly',
       r=0,
       y=0,
       b=0),
    Answer(text='Defend your reasoning',
       r=0,
       y=0,
       b=1),
    Answer(text='Probe their assumptions and evidence',
       r=0,
       y=0,
       b=2),
    Answer(text='Look for where your model might be wrong',
       r=0,
       y=0,
       b=3)]
))

question5 = Question(
    text='Which feels more uncomfortable?',
    answers=shuffle([
    Answer(text='Being wrong publicly',
       r=0,
       y=0,
       b=0),
    Answer(text='Being uncertain internally',
       r=0,
       y=0,
       b=1),
    Answer(text='Holding two conflicting explanations',
       r=0,
       y=0,
       b=2),
    Answer(text='Acting on an idea that might later be disproven',
       r=0,
       y=0,
       b=3)]
))

question6 = Question(
    text='What best describes how your opinions change?',
    answers=shuffle([
    Answer(text='Rarely — consistency matters',
       r=0,
       y=0,
       b=0),
    Answer(text='Slowly, after a lot of reflection',
       r=0,
       y=0,
       b=1),
    Answer(text='When new evidence accumulates',
       r=0,
       y=0,
       b=2),
    Answer(text='Quickly, if a better explanation appears',
       r=0,
       y=0,
       b=3)]
))

question7 = Question(
    text='Which trade-off feels most natural to you?',
    answers=shuffle([
    Answer(text='Guaranteed comfort now over uncertain upside later',
       r=0,
       y=0,
       b=0),
    Answer(text='Balanced present stability and future gains',
       r=0,
       y=1,
       b=0),
    Answer(text='Short-term sacrifice for long-term positioning',
       r=0,
       y=2,
       b=0),
    Answer(text='Aggressive long-term bets even if misunderstood now',
       r=0,
       y=3,
       b=0)]
))

question8 = Question(
    text='How do you think about effort?',
    answers=shuffle([
    Answer(text='Most effort resets when circumstances change',
       r=0,
       y=0,
       b=0),
    Answer(text='Some effort carries forward',
       r=0,
       y=1,
       b=0),
    Answer(text='The right effort compounds disproportionately',
       r=0,
       y=2,
       b=0),
    Answer(text='Almost everything I do is chosen for second-order effects',
       r=0,
       y=3,
       b=0)]
))

question9 = Question(
    text='You achieve a goal you worked toward. What happens next?',
    answers=shuffle([
    Answer(text='Relief and rest',
       r=0,
       y=0,
       b=0),
    Answer(text='Enjoyment, then a new goal',
       r=0,
       y=1,
       b=0),
    Answer(text='Reflection on what unlocked it',
       r=0,
       y=2,
       b=0),
    Answer(text='Immediate reinvestment into a longer trajectory',
       r=1,
       y=3,
       b=0)]
))

question10 = Question(
    text='Which best describes your relationship to plans?',
    answers=shuffle([
    Answer(text='Plans are comforting but often unrealistic',
       r=0,
       y=0,
       b=0),
    Answer(text='Plans guide action but change often',
       r=0,
       y=0,
       b=1),
    Answer(text='Plans are hypotheses to be tested',
       r=0,
       y=1,
       b=2),
    Answer(text='I mostly optimize for optionality, not plans',
       r=0,
       y=2,
       b=3)]
))

question11 = Question(
    text='What do you most resent in others?',
    answers=shuffle([
    Answer(text='Arrogance',
       r=0,
       y=0,
       b=1),
    Answer(text='Incompetence',
       r=1,
       y=0,
       b=0),
    Answer(text='Dishonesty',
       r=0,
       y=0,
       b=2),
    Answer(text='Passivity',
       r=3,
       y=0,
       b=0)]
))

question12 = Question(
    text='When you look back on your past decisions, which feels most true?',
    answers=shuffle([
    Answer(text='Most outcomes were determined by circumstances I couldn’t control',
       r=0,
       y=0,
       b=0),
    Answer(text='I made reasonable choices given what I knew at the time',
       r=0,
       y=1,
       b=0),
    Answer(text='A few key decisions disproportionately shaped everything that followed',
       r=1,
       y=2,
       b=0),
    Answer(text='I can clearly trace how my thinking and strategy evolved over time',
       r=1,
       y=3,
       b=1)]
))

q_list = [
    question1,
    question2,
    question3,
    question4,
    question5,
    question6,
    question7,
    question8,
    question9,
    question10,
    question11,
    question12]
