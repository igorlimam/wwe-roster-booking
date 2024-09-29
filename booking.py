import random

def refresh_roster():
    custom = ["Akane", "Demon", "Harnage", "Michelle", "Rock", "Sharon", "Storm", "Yamamoto"]
    superstars = [
    "Alexa Bliss", "Alicia Fox", "Alundra Blaze", "Asuka",
    "Bayley", "Becky Lynch", "Beth Phoenix", "Bianca Belair",
    "Billie Kay", "Brie Bela", "Candice Lerae", "Carmella",
    "Charlotte Flair", "Dakota Kai", "Dana Brooke", "Ember Moon",
    "Ivory", "Jacqueline", "Kairi Sane", "Lacey Evans",
    "Lana", "Lita", "Liv Morgan", "Mandy Rose",
    "Maria Kanellis", "Maryse", "Mickie James", "Naomi",
    "Natalya", "Nia Jax", "Nikki Bella", "Paige",
    "Peyton Royce", "Ronda Rousey", "Ruby Riott", "Sarah Logan",
    "Sasha Banks", "Shayna Baszler", "Sonya Deville", "Stephanie McMahon",
    "Tamina", "Trish Stratus"
    ]
    roster = superstars + custom
    random.shuffle(roster)
    return roster

def resolve_promo():
    promo_people = refresh_roster()
    promo_kind = ["No Promo", "No Promo", "No Promo" , "No Promo", "No Promo", "No Promo", "Self-promo", "Self-promo", "Self-promo", "Call out", "Turn"]
    promo_code = random.randint(0, len(promo_kind) - 2) if random.randint(0,100) != 100 else len(promo_kind) - 1 #for turn
    if promo_code == len(promo_kind) - 2:
        return f"Promo {promo_kind[promo_code]}: {promo_people.pop()} calls out {promo_people.pop()}"
    return f"Promo {promo_kind[promo_code]}: {promo_people.pop()}"

def resolve_match(roster):
    #only non-paperview one on one to simplify
    match_kind = [
        "Normal",
        "Falls Count Anywhere",
        "Backstage Brawl",
        "Ladder",
        "Table",
        "Steel Cage",
        "Iron Man",
        "Last Man Standing",
        "No Holds Barred",
        "Submission",
    ]

    code = random.randint(0, len(match_kind) - 1)
    kind = "Normal" if random.randint(0,20) != 20 else match_kind[code]
    match_announced = f"{kind} Match: {roster.pop()} x {roster.pop()}"
    return match_announced



shows = ["Raw", "Smackdown", "NXT", "205"]
qtd_matches = {
    "Raw": 7,
    "Smackdown": 7,
    "NXT": 6,
    "205": 5,
}
#RAW = 7; Smackdown = 7; NXT = 7; 205 = 7
roster = refresh_roster()
#print(len(roster))
while roster != []:
    for show in shows:
        print(f"-----{show}-----")
        #n/2 for promo
        print(f'Going for {show} with a roster of {len(roster)}')
        #if show == "205": print(resolve_match(roster))
        for event in range((2 * qtd_matches[show])):
            if event&1 == 0:
                #if show == "205": continue
                print(resolve_promo())
            else:
                print(resolve_match(roster))