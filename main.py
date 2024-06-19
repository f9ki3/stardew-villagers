from fastapi import FastAPI, HTTPException

app = FastAPI()

villagers = {
    "bachelors": [
        {
            "name": "Alex",
            "description": "He's a confident, athletic young man with a love for sports.",
            "birthday": "Summer 13",
            "likes": ["Complete Breakfast", "Salmon Dinner", "Salmonberry", "All Eggs", "All Milk"],
            "dislikes": ["Quartz", "Holly", "Wild Horseradish", "Winter Root"],
            "address": "1 Willow Lane, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Elliott",
            "description": "A sensitive poet who dreams of one day writing a magnificent novel.",
            "birthday": "Fall 5",
            "likes": ["Crab Cakes", "Duck Feather", "Lobster", "Pomegranate", "All Foraged Minerals"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "2 Beach Road, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Harvey",
            "description": "A dedicated and caring doctor who enjoys helping others.",
            "birthday": "Winter 14",
            "likes": ["Coffee", "Pickles", "Super Meal", "Truffle Oil", "Wine"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "3 Harvey's Clinic, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Sam",
            "description": "A friendly and outgoing musician who loves to play guitar.",
            "birthday": "Summer 17",
            "likes": ["Cactus Fruit", "Maple Bar", "Pizza", "Tigerseye", "All Fruit"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "4 Cindersap Forest, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Sebastian",
            "description": "He's a mysterious loner who spends most of his time programming.",
            "birthday": "Winter 10",
            "likes": ["Frozen Tear", "Obsidian", "Pumpkin Soup", "Sashimi", "All Fish"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "5 Mountain Road, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Shane",
            "description": "A troubled young man struggling with his past, trying to find his place in the world.",
            "birthday": "Spring 20",
            "likes": ["Beer", "Hot Pepper", "Pepper Poppers", "Pizza", "All Pickles"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "6 Marnie's Ranch, Pelican Town",
            "location": "Pelican Town"
        }
    ],
    "bachelorettes": [
        {
            "name": "Abigail",
            "description": "An adventurous and energetic girl who loves to explore the caves.",
            "birthday": "Fall 13",
            "likes": ["Amethyst", "Blackberry Cobbler", "Pufferfish", "Spicy Eel", "All Pumpkins"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "7 Mountain Road, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Emily",
            "description": "A free spirit who enjoys expressing herself through art and fashion.",
            "birthday": "Spring 27",
            "likes": ["Amethyst", "Aquamarine", "Cloth", "Emerald", "Wool"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "8 Emily's House, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Haley",
            "description": "A fashionable and sometimes snobby young woman who loves photography.",
            "birthday": "Spring 14",
            "likes": ["Coconut", "Fruit Salad", "Pink Cake", "Sunflower", "All Flowers"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "9 2 Willow Lane, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Leah",
            "description": "A talented artist who finds inspiration in the beauty of nature.",
            "birthday": "Winter 23",
            "likes": ["Goat Cheese", "Poppyseed Muffin", "Salad", "Stir Fry", "All Foraged Fruit"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "10 Leah's Cottage, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Maru",
            "description": "A brilliant scientist who is fascinated by technology and space exploration.",
            "birthday": "Summer 10",
            "likes": ["Battery Pack", "Diamond", "Gold Bar", "Iridium Bar", "All Refined Quartz"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "11 Carpenter's Shop, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Penny",
            "description": "A kind-hearted and nurturing teacher who loves to help others learn.",
            "birthday": "Fall 2",
            "likes": ["Melon", "Poppy", "Red Plate", "Roots Platter", "All Milk"],
            "dislikes": ["Quartz", "Clay", "Holly", "Winter Root"],
            "address": "12 Trailer, Pelican Town",
            "location": "Pelican Town"
        }
    ],
    "none_marriage_candidates": [
        {
            "name": "Caroline",
            "description": "A kind and gentle woman who runs the local general store with her husband Pierre.",
            "birthday": "Winter 7",
            "likes": ["Green Tea", "Summer Spangle", "Tropical Curry"],
            "dislikes": ["All Artisan Goods"],
            "address": "2 Willow Lane, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Clint",
            "description": "The local blacksmith who is shy and reserved but has a good heart.",
            "birthday": "Winter 26",
            "likes": ["Amethyst", "Artichoke Dip", "Emerald"],
            "dislikes": ["Wild Horseradish"],
            "address": "Blacksmith, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Demetrius",
            "description": "A scientist and father of Maru and Sebastian who studies the local wildlife.",
            "birthday": "Summer 19",
            "likes": ["Bean Hotpot", "Ice Cream", "Rice Pudding"],
            "dislikes": ["Fish"],
            "address": "Carpenter's Shop, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Dwarf",
            "description": "A mysterious creature that lives in the caves and sells rare items.",
            "birthday": "Summer 22",
            "likes": ["Amethyst", "Cave Carrot", "Omni Geode"],
            "dislikes": ["Milk"],
            "address": "The Mines, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Evelyn",
            "description": "A sweet elderly woman who loves to bake and tends to the town's flowers.",
            "birthday": "Winter 20",
            "likes": ["Beet", "Chocolate Cake", "Stuffing"],
            "dislikes": ["Fish"],
            "address": "1 River Road, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "George",
            "description": "An elderly man who is grumpy but has a soft spot for his wife Evelyn.",
            "birthday": "Fall 24",
            "likes": ["Leek", "Fried Mushroom"],
            "dislikes": ["Dandelion"],
            "address": "1 River Road, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Gus",
            "description": "The owner of the Stardrop Saloon who is always ready to lend a helping hand.",
            "birthday": "Summer 8",
            "likes": ["Diamond", "Escargot", "Orange"],
            "dislikes": ["Coleslaw"],
            "address": "Stardrop Saloon, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Jas",
            "description": "A young girl who is shy but loves animals and playing with her friends.",
            "birthday": "Summer 4",
            "likes": ["Fairy Rose", "Plum Pudding"],
            "dislikes": ["Cranberries"],
            "address": "Marnie's Ranch, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Jodi",
            "description": "A caring mother who looks after her two sons, Sam and Vincent.",
            "birthday": "Fall 11",
            "likes": ["Chocolate Cake", "Crispy Bass", "Diamond"],
            "dislikes": ["Dandelion"],
            "address": "1 Willow Lane, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Kent",
            "description": "A soldier who has returned home from war and is trying to adjust to civilian life.",
            "birthday": "Spring 4",
            "likes": ["Fiddlehead Risotto", "Roasted Hazelnuts"],
            "dislikes": ["Daffodil"],
            "address": "1 Willow Lane, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Krobus",
            "description": "A friendly shadow creature who lives in the sewers and sells rare items.",
            "birthday": "Winter 1",
            "likes": ["Pumpkin", "Void Egg"],
            "dislikes": ["Daffodil"],
            "address": "The Sewers, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Leo",
            "description": "A young boy who was raised on Ginger Island and loves the wildlife there.",
            "birthday": "Summer 26",
            "likes": ["Duck Feather", "Mango"],
            "dislikes": ["Squid"],
            "address": "Ginger Island",
            "location": "Ginger Island"
        },
        {
            "name": "Lewis",
            "description": "The mayor of Pelican Town who is kind-hearted and cares deeply for the town.",
            "birthday": "Spring 7",
            "likes": ["Autumn's Bounty", "Green Tea"],
            "dislikes": ["Maki Roll"],
            "address": "Mayor's Manor, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Linus",
            "description": "A kind man who lives in a tent and prefers to live off the land.",
            "birthday": "Winter 3",
            "likes": ["Blueberry Tart", "Cactus Fruit"],
            "dislikes": ["Spring Onion"],
            "address": "Tent, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Marnie",
            "description": "The owner of Marnie's Ranch who cares for a variety of animals.",
            "birthday": "Fall 18",
            "likes": ["Diamond", "Pink Cake"],
            "dislikes": ["Wild Horseradish"],
            "address": "Marnie's Ranch, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Pam",
            "description": "A tough, no-nonsense woman who drives the bus and loves to fish.",
            "birthday": "Spring 18",
            "likes": ["Cactus Fruit", "Mead"],
            "dislikes": ["Parsnip"],
            "address": "Trailer, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Pierre",
            "description": "The owner of the General Store and a hardworking businessman.",
            "birthday": "Spring 26",
            "likes": ["Fried Calamari", "No Name"],
            "dislikes": ["Dandelion"],
            "address": "General Store, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Robin",
            "description": "The local carpenter who is always busy working on new projects.",
            "birthday": "Fall 21",
            "likes": ["Goat Cheese", "Peach"],
            "dislikes": ["Wild Horseradish"],
            "address": "Carpenter's Shop, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Sandy",
            "description": "The owner of the Oasis shop in the desert.",
            "birthday": "Fall 15",
            "likes": ["Crocus", "Sweet Pea"],
            "dislikes": ["All Fish"],
            "address": "Oasis, Calico Desert",
            "location": "Calico Desert"
        },
        {
            "name": "Vincent",
            "description": "A young boy who loves to play and is always full of energy.",
            "birthday": "Spring 10",
            "likes": ["Cranberry Candy", "Snail"],
            "dislikes": ["Grape"],
            "address": "1 Willow Lane, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Willy",
            "description": "The local fisherman who has a deep love for the sea and everything in it.",
            "birthday": "Summer 24",
            "likes": ["Catfish", "Octopus"],
            "dislikes": ["Amaranth"],
            "address": "Fish Shop, Pelican Town",
            "location": "Pelican Town"
        },
        {
            "name": "Wizard",
            "description": "A mysterious figure who lives in the tower and studies magic.",
            "birthday": "Winter 17",
            "likes": ["Purple Mushroom", "Solar Essence"],
            "dislikes": ["Fish"],
            "address": "Wizard's Tower, Pelican Town",
            "location": "Pelican Town"
        }
    ],
    "none_giftable_npcs": [
        {
            "name": "Bouncer",
            "description": "A silent guard who blocks access to the casino until you earn his trust.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Stardrop Saloon",
            "location": "Pelican Town"
        },
        {
            "name": "Gil",
            "description": "An old adventurer who spends his days at the Adventurer's Guild.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Adventurer's Guild",
            "location": "Pelican Town"
        },
        {
            "name": "Governor",
            "description": "The governor who visits Pelican Town every year for the Luau festival.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Unknown",
            "location": "Pelican Town"
        },
        {
            "name": "Grandpa",
            "description": "The spirit of your grandfather who evaluates your progress in Stardew Valley.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Your Farm",
            "location": "Stardew Valley"
        },
        {
            "name": "Gunther",
            "description": "The curator of the Pelican Town museum, in charge of collecting and displaying artifacts and minerals.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Museum",
            "location": "Pelican Town"
        },
        {
            "name": "Henchman",
            "description": "A servant of the Witch, guarding the Witch's Hut.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Witch's Hut",
            "location": "Pelican Town"
        },
        {
            "name": "Marlon",
            "description": "A grizzled, no-nonsense adventurer who runs the Adventurer's Guild.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Adventurer's Guild",
            "location": "Pelican Town"
        },
        {
            "name": "Morris",
            "description": "The manager of JojaMart, focused on sales and expanding the Joja corporation.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "JojaMart",
            "location": "Pelican Town"
        },
        {
            "name": "Mr. Qi",
            "description": "A mysterious figure who provides challenges and quests to test your skills.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Calico Desert Casino",
            "location": "Calico Desert"
        },
        {
            "name": "Professor Snail",
            "description": "A researcher who studies the wildlife and fossils of Ginger Island.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Ginger Island",
            "location": "Ginger Island"
        },
        {
            "name": "Birdie",
            "description": "An old sailor woman living on Ginger Island who is mourning her late husband.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Ginger Island",
            "location": "Ginger Island"
        },
        {
            "name": "Fizz",
            "description": "A mysterious character with unknown intentions and a penchant for alchemy.",
            "birthday": "Unknown",
            "likes": ["None"],
            "dislikes": ["None"],
            "address": "Secret Woods",
            "location": "Pelican Town"
        }
    ]
}

@app.get('/villagers')
def query_villagers(limit: int = 46):
    villagers_all = [villager for sublist in villagers.values() for villager in sublist]
    return villagers_all[:limit]

@app.get('/villagers/{type}')
def get_villagers_type(type: str):
    if type not in villagers:
        raise HTTPException(status_code=404, detail="Type not found")
    return villagers[type]

@app.get('/villagers/{type}/{id}')
def get_villagers_id(type: str, id: int):
    if type not in villagers:
        raise HTTPException(status_code=404, detail="Type not found")
    if id < 0 or id >= len(villagers[type]):
        raise HTTPException(status_code=404, detail="Villager not found")
    return villagers[type][id]
