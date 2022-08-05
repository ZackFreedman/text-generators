import math
import random
import time

insultingAdjectives = [
    "sweaty",
    "big",
    "fat",
    "dumb",
    "stupid",
    "goddamn",
    "moist",
    "mega-",
    "turbo-",
    "hyper-",
    "idiotic",
    "worthless",
    "flesh-covered",
    "uptight",
    "poop flinging",
    "diseased",
    "hairy",
    "miserable",
    "lonely",
    "sad",
    "brain-damaged",
    "stupendous",
    "terminally-online",
    "millennial",
    "broke-ass",
    "braindead",
    "fetal alcohol",
    "underdeveloped",
    "talentless",
    "ignorant",
    "son-of-a-",
    "store-brand",
    "irrelevant",
    "giant",
    "deformed",
    "wannabe",
    "obsolete",
    "old",
    "infantile",
    "unfunny",
    "greasy",
    "degenerate",
    "lazy",
    "slovenly",
    "buck-toothed",
    "pathetic",
    "reptilian",
    "absolute",
    "feeble-minded",
    "effeminate",
    "lumpy",
    "low-IQ",
    "sticky",
    "cringey",
    "stinky",
    "phallic",
    "second-class",
    "corporate",
    "anime-watching",
    "wrinkly",
    "fugly",
    "disposable",
    "v-tuber simping",
    "desperate",
    "sleazy",
    "lowly",
]

adjectivesThatTurnNounsIntoAdjectives = [
    "-obsessed",
    "-infested",
    "-ass",
    "-like",
    "-esque",
    "-face",
    "-bag",
    "-sack",
    "-shaped",
    "-head",
    "-smelling",
    "-covered",
    "-filled",
    "-looking-ass",
    "less",
    "-tuber",
]

insultingNouns = [
    "egg",
    "glue",
    "fart",
    "diarrhea",
    "hair",
    "poop",
    "doo-doo",
    "mother",
    "daddy",
    "granny",
    "pizza",
    "baby",
    "sewer",
    "keeb",
    "crotch",
    "frog",
    "bong",
    "3D-printer",
    "puppy",
    "Funko Pop",
    "diaper",
    "moustache",
    "octopus",
    "kitten",
    "banana",
    "Quagsire",
    "pony",
    "garbage",
    "finger",
    "watermelon",
    "Bionicle",
    "RGB-LED",
    "robot",
    "sausage",
    "uncle",
    "goop",
    "hobo",
    "cigar",
    "vape",
    "cat",
    "spoon",
    "nugget",
    "taint",
    "beer",
    "hamster",
]

nouns_for_you = [
    "meat sack",
    "millennial",
    "loser",
    "peasant",
    "oxygen thief",
    "waste of space",
    "dork",
    "nerd",
    "dweeb",
    "ignoramus",
    "knucklehead",
    "moron",
    "hack",
    "psychopath",
    "mama's boy",
    "virgin",
    "disappointment",
    "wimp",
    "so-and-so",
    "degenerate",
    "charlatan",
    "hack",
    "drain on society",
    "parasite",
    "stain",
    "weeaboo",
    "creep",
    "redneck",
    "phony",
    "future divorcee",
    "sellout",
    "noob",
]

versatile_nouns = [
    "worm",
    "douche",
    "monkey",
    "orangutan",
    "wildebeest",
    "boomer",
    "dog",
    "bitch",
    "turd",
    "booger",
    "goblin",
    "ass",
    "penis",
    "hoo-ha",
    "sphinchter",
    "rodent",
    "reptile",
    "dipstick",
    "neanderthal",
    "wiener",
    "dingus",
    "scum",
    "snake",
    "weasel",
    "donkey",
    "bum",
    "butt",
    "pimple",
    "pustule",
    "boob",
    "amogus",
    "corncob",
    "nut",
    "nozzle",
    "redacted",
    "donut",
]

insultingVerbs = [
    "suck",
    "lick",
    "kick",
    "punch",
    "cuddl",
    "slapp",
    "fapp",
    "tugg",
    "blast",
    "snort",
    "defil",
    "snuggl",
    "hump",
    "eat",
    "lov",
    "sniff",
    "touch",
    "look",
    "slurp",
    "ogl",
    "fondl",
    "huff",
    "chew",
    "spew",
    "punt",
    "tast",
    "grabb",
    "strok",
    "pucker",
    "smooch",
    "disappoint",
    "hat",
    "hoard",
    "guzzl",
    "pinch",
]


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


if __name__ == '__main__':
    last_insult = ''

    while True:
        last_insult = hit_me(3, exclusions=last_insult, odds_of_adding_another_word=0.75)
        print(last_insult)
        time.sleep(0.5)
