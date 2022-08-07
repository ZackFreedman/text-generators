import math
import random
import time
from main_insults import *
from shakespearean_insults import *

def pick_candidate(words, exclusions):
    if random.random() < 0.02:
        # print('hee hee I broke the rules')
        return random.choice(words)

    candidates = [word for word in words if word not in exclusions]

    if len(candidates) == 0:
        print('Ran out of words! Reusing one.')
        return random.choice(words)

    return random.choice(candidates)


def gimme_a_verb(exclusions=""):
    return pick_candidate(insultingVerbs, exclusions)


def noun_yourself(compound_words_allowed=False, exclusions=""):
    dice_roll = random.random()

    if not compound_words_allowed or dice_roll < 0.8:
        return pick_candidate(nouns_for_you + versatile_nouns, exclusions)

    elif dice_roll < 0.9:
        first_noun = pick_candidate(insultingNouns + versatile_nouns, exclusions)
        second_noun = pick_candidate(insultingNouns + versatile_nouns, exclusions + first_noun)

        return f'{first_noun} ' f'{second_noun}'

    else:
        noun = noun_something_else(exclusions)
        verb = gimme_a_verb(exclusions + noun)
        return f'{noun}-{verb}er'


def noun_something_else(exclusions=""):
    return pick_candidate(insultingNouns + versatile_nouns, exclusions)


def get_an_adjective(next_word_is_a_noun, exclusions=""):
    if random.random() < 0.75:
        if next_word_is_a_noun:
            return pick_candidate([word for word in insultingAdjectives if word[-1] != '-'], exclusions)
        else:
            return pick_candidate(insultingAdjectives, exclusions)

    else:
        noun = noun_something_else(exclusions)

        dice_roll = random.randint(0, len(insultingVerbs) + len(adjectivesThatTurnNounsIntoAdjectives))

        if dice_roll < len(insultingVerbs):
            verb = pick_candidate(insultingVerbs, exclusions)
            return f'{noun}-{verb}ing'

        else:
            adjective = pick_candidate(adjectivesThatTurnNounsIntoAdjectives, exclusions)
            return noun + adjective


def hit_me(maximum_words=math.inf, exclusions="", odds_of_adding_another_word=0.5):
    output = ''
    word_count = 1  # Includes the noun

    dice_roll = random.random()

    while word_count < maximum_words and dice_roll < odds_of_adding_another_word:
        dice_roll = random.random()

        output += get_an_adjective(dice_roll < odds_of_adding_another_word, exclusions=(output + exclusions))
        if output[-1] is not '-':
            output += ' '

        word_count += 1

    hyphenated = len(output) > 0 and output[-1] == '-'
    output += noun_yourself(compound_words_allowed=(not hyphenated), exclusions=(output + exclusions))

    return output


def shake_me():
    return random.choice(shakey_one) + " " + random.choice(shakey_two) + " " + random.choice(shakey_three)


if __name__ == '__main__':
    last_insult = ''

    while True:
        last_insult = hit_me(3, exclusions=last_insult, odds_of_adding_another_word=0.75)
        # last_insult = shake_me()
        print(last_insult)
        time.sleep(0.5)
