from fastapi import FastAPI

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
  ]
}


app = FastAPI()

@app.get('/')
def fetch_villagers():
    villagers = list(villagers.values())
    return villagers
