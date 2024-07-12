# 2. Hangman: Implement the wordguessing game with visual
# progress and hints.

# Word Selection using the random module
import random as rd

# function for selecting word
def select_word(word_list):
    # generating word with random module
    return rd.choice(word_list)

# function for game setup
def initialize_game():
    # getting word list
    word_list = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yellowfruit",
    "zucchini", "apricot", "blackberry", "blueberry", "cantaloupe", "dragonfruit",
    "gooseberry", "grapefruit", "jackfruit", "kumquat", "lime", "lychee", "mulberry",
    "olive", "peach", "pear", "persimmon", "pineapple", "plum", "pomegranate",
    "starfruit", "tomato", "coconut", "durian", "elderberry", "feijoa", "guava",
    "kiwano", "longan", "loquat", "mangosteen", "passionfruit", "plantain", "rambutan",
    "sapodilla", "soursop", "tamarind", "yuzu", "bilberry", "cloudberry", "currant",
    "elderflower", "fig", "goji", "huckleberry", "jostaberry", "kiwi", "lingonberry",
    "medlar", "miraclefruit", "mulberry", "nance", "pitanga", "salmonberry", "saskatoon",
    "sea-buckthorn", "snowberry", "sugar-apple", "tayberry", "whitecurrant",
    "yellowpassionfruit", "ackee", "abiu", "açaí", "araça", "balsamapple", "barbadine",
    "bilimbi", "blackcurrant", "calabash", "capuli", "carambola", "cashewapple", 
    "cherimoya", "chokeberry", "clementine", "corneliancherry", "damson", "elderberry",
    "fingerlime", "galia", "garcinia", "genip", "greengage", "hornedmelon", "jabuticaba",
    "jujube", "kaffirlime", "kepel", "keule", "kousa", "langsat", "lucuma", "mahaleb",
    "mammeeapple", "mango", "mangosteen", "maqui", "maypop", "medlar", "muscadine",
    "naranjilla", "neem", "nutmeg", "pecan", "pequi", "pindo", "pistachio", "pulasan",
    "santol", "sapote", "serviceberry", "shaddock", "sloe", "sorb", "strawberry",
    "surinamcherry", "tamarillo", "tamarind", "thimbleberry", "ubajay", "voavanga",
    "wampee", "whitebark", "wineberry", "wolfberry", "yangmei", "yewberry", "yumberry",
    "zzulú", "acerola", "allspice", "ambarella", "amla", "americanpersimmon", "arbutus",
    "bael", "batuan", "bellapple", "bignay", "blackhaw", "bloodorange", "cacao",
    "canistel", "cedarbaycherry", "chayote", "chenet", "chequers", "cherryplum", "coastaljackfruit",
    "crabapple", "crowberry", "cucamelon", "damsonplum", "dekopon", "desertlime",
    "diospyros", "douglasfir", "elephantapple", "figs", "gamboge", "goumi", "grosella",
    "hackberry", "hawthorn", "hogplum", "icaco", "ilama", "indianfig", "indianplum",
    "inkberry", "jamfruit", "jackfruit", "javaapple", "jellypalm", "jocote", "kaffirplum",
    "kaizuka", "kalabasa", "kale", "kamias", "kapok", "karanda", "kea", "kereru",
    "keulefruit", "kinkiliba", "kitchenmint", "kurrajong", "kurrakindi", "ladyslime",
    "lemonadeberry", "lemonaspen", "libyan", "lichen", "lippia", "logwood", "longanberry",
    "lotusfruit", "lycium", "macadamia", "madrono", "malayapple", "mammeeapple", "mamoncillo",
    "mandarins", "mangaba", "mangosteen", "manilkara", "marang", "mari", "marula", "mascot",
    "medlar", "melicoccus", "metasequoia", "monstera", "montezuma", "morinda", "mountainapple",
    "muscadine", "nashi", "natalplum", "nauclea", "neem", "nopal", "nutmegapple", "ohelo",
    "olae", "ollalieberry", "opuntia", "orangeberry", "oroblanco", "ovenbird", "paepae",
    "panama", "papaw", "patepata", "pawpaw", "peachpalm", "pequi", "persimmon", "peumo",
    "physalis", "pigeonplum", "pineberry", "pistachio", "pitanga", "pitaya", "pitos", "plumcot",
    "pomegranate", "pommet", "pomato", "pomelo", "pricklypear", "pulasan", "quandong", "quena",
    "quince", "rambai", "ramontchi", "rangpur", "redbanana", "redcurrant", "rengas", "riberry",
    "rockmelon", "rosehip", "rowan", "safou", "salak", "santol", "saskatoon", "satsuma",
    "serviceberry", "shaddock", "shepherdia", "sloe", "snowberry", "solanum", "soursop",
    "starapple", "strawberry", "sugarapple", "surinamcherry", "syzygium", "tamarillo",
    "tamarind", "tapereba", "tawa", "tayberry", "teaberry", "ubajay", "ucuuba", "ugli",
    "ujujube", "ulexeberry", "umber", "vaccinium", "vi", "voavanga", "wampi", "waxapple",
    "waxberry", "whitebeam", "wildcherry", "wildfig", "wineberry", "wintercherry", "wolfberry",
    "woodapple", "woodberry", "wormwood", "xigua", "yamamomo", "yantok", "yellowfruit", "yewberry",
    "youngberry", "yumberry", "zante", "zhe", "zinfandelgrape", "ziziphus", "zuccotto", "zucchini"
]
    # getting the chosen selected words
    chosenWord = select_word(word_list)

    # setting a guess letter to empty
    wordGuessed = []

    # setting incorrect guesses and maximum attempts
    incorrectGuesses = 0
    maxGuesses = 3
    
    return chosenWord, wordGuessed, incorrectGuesses, maxGuesses

# function for interface display for chosenWord, wordGuessed, incorrectGuesses, maxGuesses
def display_interface(chosenWord, wordGuessed, incorrectGuesses, maxGuesses):
    # printing the incorrect guesses
    print(f"Guessed Incorrectly: {incorrectGuesses}")

    #getting reserved words
    words_remained = ""

    for letter in chosenWord:
        if letter in wordGuessed:
            words_remained += letter + " "
        else:
            words_remained += "_ "
    
    # displaying reserved words
    print(f"Words Remained: {words_remained.strip()}")

    # displaying word and maximum guesses
    print(f"Word Guesses: {wordGuessed}")
    print(f"Maximum Attempts: {maxGuesses}")


# function for user input
def get_user_input():
    while True:
        #Ensure lowercase and remove any extra spaces
        guess = input("Guess a word: ").strip().lower()

        # validation conditions for guessing word alphabetically
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a word.")
        else:
            return guess 
    
# function for checking chosen word, word guessed and guess input
def check_guess(chosenWord, wordGuessed, guess):
    # condition for checking guesses
    if guess in wordGuessed:
        print("You already guessed that word")
    else:
        wordGuessed.append(guess)
        if guess not in chosenWord:
            return False # for incorrect word guess
    return True # correct guess

# function for win/loss conditions for chosenWord, wordGuessed, incorrectGuesses, maxGuesses
def win_loss(chosenWord, wordGuessed, incorrectGuesses, maxGuesses):
    # lost for incorrect guesses greater than maximum attempts
    if incorrectGuesses >= maxGuesses:
        print(f"You lost! The word was: {chosenWord}")
        return True
    else:
        for alpha in chosenWord:
            if alpha not in wordGuessed:
                return False
        print(f"You won! The word is: {chosenWord}")
        return True
    
# function for game loop
def play_game():
    chosenWord, wordGuessed, incorrectGuesses, maxGuesses = initialize_game()
    game_over = False
       # initializing attempt counter

    while not game_over and incorrectGuesses < maxGuesses:
        display_interface(chosenWord, wordGuessed, incorrectGuesses, maxGuesses)

        guess = get_user_input()

        if not check_guess(chosenWord, wordGuessed, guess):
            incorrectGuesses += 1

        game_over = win_loss(chosenWord, wordGuessed, incorrectGuesses, maxGuesses)
    
    print(f"Number of word guessed: {len(wordGuessed)}")
    print(f"Number of incorrect guesses: {incorrectGuesses}")

# function for play again
def main():
    play_again = True

    while play_again:
        play_game()

        # asking for play again
        play = input("Do you want play again? (yes/no): ").lower()

        if play != "yes":
            play_again = False
            print("Thanks for playing")

        else:
            print("Starting new game...")

if __name__ == "__main__":
    main()