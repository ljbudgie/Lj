"""
Biblical Quotes Database
A collection of teachings and quotes from Jesus Christ
"""

# Teachings of Jesus from the Gospels
JESUS_TEACHINGS = [
    # The Beatitudes (Matthew 5:3-12)
    "Blessed are the poor in spirit, for theirs is the kingdom of heaven. - Matthew 5:3",
    "Blessed are those who mourn, for they will be comforted. - Matthew 5:4",
    "Blessed are the meek, for they will inherit the earth. - Matthew 5:5",
    "Blessed are those who hunger and thirst for righteousness, for they will be filled. - Matthew 5:6",
    "Blessed are the merciful, for they will be shown mercy. - Matthew 5:7",
    "Blessed are the pure in heart, for they will see God. - Matthew 5:8",
    "Blessed are the peacemakers, for they will be called children of God. - Matthew 5:9",
    
    # The Great Commandments
    "Love the Lord your God with all your heart and with all your soul and with all your mind. - Matthew 22:37",
    "Love your neighbor as yourself. - Matthew 22:39",
    
    # Famous Teachings
    "I am the way and the truth and the life. No one comes to the Father except through me. - John 14:6",
    "I am the light of the world. Whoever follows me will never walk in darkness, but will have the light of life. - John 8:12",
    "I am the resurrection and the life. The one who believes in me will live, even though they die. - John 11:25",
    "I am the good shepherd. The good shepherd lays down his life for the sheep. - John 10:11",
    "I am the bread of life. Whoever comes to me will never go hungry. - John 6:35",
    
    # On Love and Forgiveness
    "Love your enemies and pray for those who persecute you. - Matthew 5:44",
    "If you forgive other people when they sin against you, your heavenly Father will also forgive you. - Matthew 6:14",
    "Do to others as you would have them do to you. - Luke 6:31",
    "Let him who is without sin cast the first stone. - John 8:7",
    
    # On Faith and Prayer
    "Ask and it will be given to you; seek and you will find; knock and the door will be opened to you. - Matthew 7:7",
    "If you believe, you will receive whatever you ask for in prayer. - Matthew 21:22",
    "Have faith in God. Truly I tell you, if you have faith as small as a mustard seed, you can move mountains. - Matthew 17:20",
    "Come to me, all you who are weary and burdened, and I will give you rest. - Matthew 11:28",
    
    # On Humility and Service
    "Whoever wants to become great among you must be your servant. - Matthew 20:26",
    "The greatest among you will be your servant. For those who exalt themselves will be humbled. - Matthew 23:11-12",
    "Let the little children come to me, and do not hinder them, for the kingdom of heaven belongs to such as these. - Matthew 19:14",
    
    # On Worry and Trust
    "Do not worry about tomorrow, for tomorrow will worry about itself. - Matthew 6:34",
    "Look at the birds of the air; they do not sow or reap or store away in barns, and yet your heavenly Father feeds them. - Matthew 6:26",
    "Peace I leave with you; my peace I give you. Do not let your hearts be troubled and do not be afraid. - John 14:27",
    
    # On the Kingdom of God
    "The kingdom of God is within you. - Luke 17:21",
    "Seek first the kingdom of God and his righteousness, and all these things will be given to you. - Matthew 6:33",
    "Unless you change and become like little children, you will never enter the kingdom of heaven. - Matthew 18:3",
    
    # On Truth and Light
    "You are the light of the world. A town built on a hill cannot be hidden. - Matthew 5:14",
    "Let your light shine before others, that they may see your good deeds and glorify your Father in heaven. - Matthew 5:16",
    "The truth will set you free. - John 8:32",
    
    # The Lord's Prayer
    "Our Father in heaven, hallowed be your name, your kingdom come, your will be done, on earth as it is in heaven. - Matthew 6:9-10",
    
    # Parables
    "I am the vine; you are the branches. If you remain in me and I in you, you will bear much fruit. - John 15:5",
    "A good tree cannot bear bad fruit, and a bad tree cannot bear good fruit. - Matthew 7:18",
    
    # On Following Jesus
    "If anyone would come after me, let him deny himself and take up his cross and follow me. - Matthew 16:24",
    "No one can serve two masters. Either you will hate the one and love the other. - Matthew 6:24",
    "What good is it for someone to gain the whole world, yet forfeit their soul? - Mark 8:36",
    
    # Final Commands
    "Go and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit. - Matthew 28:19",
    "Peace be with you! As the Father has sent me, I am sending you. - John 20:21",
]


def get_random_quote():
    """Get a random teaching from Jesus"""
    import random
    return random.choice(JESUS_TEACHINGS)


def get_all_quotes():
    """Get all teachings"""
    return JESUS_TEACHINGS.copy()


def get_beatitudes():
    """Get the Beatitudes"""
    return [q for q in JESUS_TEACHINGS if "Blessed are" in q]


def get_quotes_by_theme(theme: str):
    """
    Get quotes by theme
    
    Args:
        theme: Theme keyword (e.g., 'love', 'faith', 'forgiveness')
    
    Returns:
        List of relevant quotes
    """
    theme_lower = theme.lower()
    return [q for q in JESUS_TEACHINGS if theme_lower in q.lower()]


def save_quotes_to_file(filename: str, quotes: list = None):
    """
    Save quotes to a file
    
    Args:
        filename: Output filename
        quotes: List of quotes (default: all quotes)
    """
    if quotes is None:
        quotes = JESUS_TEACHINGS
    
    with open(filename, 'w') as f:
        for quote in quotes:
            f.write(quote + '\n')
    
    print(f"Saved {len(quotes)} quotes to {filename}")


if __name__ == '__main__':
    # Example usage
    print("Biblical Quotes Database")
    print("=" * 50)
    print(f"\nTotal quotes: {len(JESUS_TEACHINGS)}")
    print(f"\nRandom quote:\n{get_random_quote()}")
    print(f"\nBeatitudes count: {len(get_beatitudes())}")
    print(f"\nQuotes about 'love': {len(get_quotes_by_theme('love'))}")
