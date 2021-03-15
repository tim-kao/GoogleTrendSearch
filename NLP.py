# Import the modules
import text2emotion as te

text = "I was asked to sign a third party contract a week out from stay. " \
       "If it wasn't an 8 person group that took a lot of wrangling I would have cancelled the booking straight away. " \
       "Bathrooms - there are no stand alone bathrooms. " \
       "Please consider this - you have to clear out the main bedroom to use that bathroom. " \
       "Other option is you walk through a different bedroom to get to its en-suite. Signs all over the apartment - " \
       "there are signs everywhere - some helpful - some telling you rules. Perhaps some people like this " \
       "but It negatively affected our enjoyment of the accommodation. Stairs - lots of them - some had slightly " \
       "bending wood which caused a minor injury."

text2 = "I’m thinking Tesla lowered their prices recently to challenge their competitors, not to increase demand. " \
        "And of course to fulfill their stated “accelerate” mission. " \
        "It’s a battle of first principles versus “corporate analogous thinking”." \
        "Analogous-thinking (oxymoron alert!) competitors are risk adverse because they have to be. " \
        "It’s like driving with blinders on. There’s a lot less risk when you’re actually thinking from the ground up." \
        "Full disclosure: Not a significant amount of money yet, but at any time I have Tesla stock and/or calls. " \
        "Never short or puts. Also preordered a CT, about 270k in line, " \
        "but willing to pick up the CT in Austin (need to change from dual motor to tri motor)."

text3 = "The Gig Economy Is Coming for Millions of American Jobs - California’s vote to classify Uber and Lyft drivers " \
        "as contractors has emboldened other employers to eliminate salaried positions—and has become a cornerstone of " \
        "bigger plans to “Uberize” the U.S. workforce."

res = te.get_emotion(text3)

print(res)