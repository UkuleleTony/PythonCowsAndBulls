#--------------------------------------------------------------------------------------------------
# Purpose            : This is the classic board game Mastermin
#                      The computer generates a random 4 digit number and the player has
#                      to guess the number. After each guess the computer will show how
#                      many digits of the gues were the right digit in the right place (cows)
#                      and how many were the right digit but in the wrong place (Bulls).
#                      The goal is arrive at the answer with the fewest guesses possible.
# Date Created       : 15Jan2023
# Author             : A.S.Harrison
# Amendment History  : Date         Author          Description
#                      15Jan2023    A.S.Harrison    Created
#--------------------------------------------------------------------------------------------------
import random

strAnswer = str(random.randrange(0,10000))                              # Get a 4 digit random number
strAnswer = str('0000' + strAnswer)[-4:]                                # Pad with leading zeroes if necessary

# TODO: Take the following line out, it's only for me
print (strAnswer)   

intAttempts = int(0)
intCow = int(0)

while intCow < 4:                                                       # Keep repeating until the user gets it right
    lstAnswer = list(strAnswer)                                         # Always start with a fresh list of the answer
    intAttempts += 1                                                    # Increment the number of attempts
    strGuess = input('Enter a 4 digit guess (Q to quit): ')             # Ask the user for a guess
    if strGuess == 'Q': break                                           # If the user gives up, break outt he loop
    lstGuess = list(strGuess)                                           # Convert it to a list

    # TODO: Validate that we have been given a valid guess (4 digits, all numeric)

    intCow = int(0)                                                     # Initialise results
    intBull = int(0)

    for i in range(0,4):                                                # Check for Cows (right number, right place)
        if lstGuess[i] == lstAnswer[i]:                                 # If we find a matching digit (in the right place)
            intCow += 1                                                 # Increment the cow count
            lstGuess[i] = 'x'                                           # Replace the digit, in both places, so that they don't get a 'bull' match
            lstAnswer[i] = 'y'

    for i in range(0,4):                                                # Check for Bulls (right number, wrong place)
        for j in range(0,4):
            if lstGuess[i] == lstAnswer[j]:                             # If we found one
                intBull += 1                                            # Increment the bull count

    print(str(intCow) + ' Cow(s) and ' + str(intBull) + ' Bull(s))')    # Display the hint

if intCow != 4: print('Pfft, surrender monkey!')                        # If the user gave up, insult him/her

if intCow == 4:                                                         # If the user got it right
    print ('Got it in ' + str(intAttempts))                             # Show the number of attempts
    if intAttempts == 1 : print('UN-FREAKING-BELEIVABLE')               # And display an appropriate message
    if intAttempts > 1 and intAttempts < 4: print('Pretty damned good')
    if intAttempts > 3 and intAttempts < 6: print('Alright I suppose')
    if intAttempts > 5 and intAttempts < 10: print('Mediocre')
    if intAttempts > 9: print('Less said about that the better')
