# Voidstar Stupid Text Generator(s)
*Your infinite supply of procedural stupidity!*

These* are idiotic, yet worthless algorithms to generate semi-random text. They're useful for... nothing really, but I use them in various projects like the Somatic and Christopher the Robot Quagsire. They're written in Python, but should be trivial to port. The whole may be more offensive than its parts, so don't use this in live demos!

**insult_generator.py**: Produces *ad hominem* attacks of the form `adjective [...more adjectives] noun [maybe another noun]`, such as 'hairy fart-filled creep weasel' and 'corncob-tugging egg-shaped sleazy son-of-a-boomer.' 

## How to use:
1) Ruminate on the poor decisions that led you here
2) Add the thing to your thing
3) Import it: `from insult_generator import hit_me`
4) Run it: `yo_mama = hit_me()` and add optional params `maximum_words`, `odds_of_adding_another_word`, and/or `exclusions`... *if you dare*

Parameters:
* `maximum_words`: The maximum number of tokens to select. They're not really words per se, since some tokens like `future divorcee` are phrases. Anything less than 1 means you're dumb. Default: 3
* `exclusions`: Tokens that should be rerolled. **One string, not a collection!** For instance, `yo_mama = hit_me(exclusions="mama's boy Bionicle moist")` because yo mama is not cool enough to be a Bionicle, probably not male enough to be a boy, and certainly not moist in my experience, hey-o! Default: Nothing
* `odds_of_adding_another_word`: Probability from 0.0 to 1.0 of adding an additional word - affects variance, basically. A value of 1.0 means every output is `maximum_words` long. A value of 0.75 means there's a 75% chance of getting more than one word, a 75% * 75% = 56% chance of getting more than two words, etc. A value of 0.0 means you're super duper dumb. *Generation always stops when `maximum_words` have been produced!* Default: 0.5


\*I'll add more later, I promise!