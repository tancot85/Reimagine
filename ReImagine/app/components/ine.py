import praw
from praw.reddit import Submission, Subreddit


class INE:
    # __client_id: str
    # __client_secret: str
    # __password: str
    # __user_agent: str
    # __username: str

    # reddit = praw.Reddit(
    #     client_id="",
    #     client_secret="",
    #     password="",
    #     user_agent="",
    #     username="",
    # )

    # def __init__(self, client_id: str, client_secret: str, password: str, user_agent: str, username: str):
    #     self.__client_id = client_id
    #     self.__client_secret = client_secret
    #     self.__password = password
    #     self.__user_agent = user_agent
    #     self.__username = username
    #     self.reddit = praw.Reddit(
    #         client_id=self.__client_id,
    #         client_secret=self.__client_secret,
    #         password=self.__password,
    #         user_agent=self.__user_agent,
    #         username=self.__username,
    #     )
    reddit = praw.Reddit(client_id="CUlMAgLt1nnsCb9-5wEQww",
                         client_secret="d6Q0qATAETX5tmzGM96m9GGdcBq1DA",
                         password="Magha@702",
                         user_agent="testscript by u/RagingBox08",
                         username="RagingBox08"
                         )
    __categorires = ['characters', 'races', 'lands', 'architecture',
                     'monsters', 'technology', 'fandoms', 'misc', 'friends']

    __all_subreddit = {
        'characters': {'ImaginaryArchers',
                       'ImaginaryAssassins',
                       'ImaginaryAstronauts',
                       'ImaginaryBoners',
                       'ImaginaryKnights',
                       'ImaginaryLovers',
                       'ImaginaryMythology',
                       'ImaginaryNobles',
                       'ImaginaryScholars',
                       'ImaginarySoldiers',
                       'ImaginaryWarriors',
                       'ImaginaryWitches',
                       'ImaginaryWizards', },
        'races': {'ImaginaryAngels',
                  'ImaginaryDwarves',
                  'ImaginaryElves',
                  'ImaginaryFaeries',
                  'ImaginaryHumans',
                  'ImaginaryImmortals',
                  'ImaginaryMerfolk',
                  'ImaginaryOrcs',
                  },
        'lands': {'ImaginaryBattlefields',
                  'ImaginaryCityscapes',
                  'ImaginaryHellscapes',
                  'ImaginaryMindscapes',
                  'ImaginaryPathways',
                  'ImaginarySeascapes',
                  'ImaginarySkyscapes',
                  'ImaginaryStarscapes',
                  'ImaginaryWastelands',
                  'ImaginaryWeather',
                  'ImaginaryWildlands',
                  'ImaginaryWorlds', },
        'architecture': {'ImaginaryArchitecture',
                         'ImaginaryCastles',
                         'ImaginaryDwellings',
                         'ImaginaryInteriors',
                         'ImaginaryLibraries', },
        'monsters': {'ImaginaryBeasts',
                     'ImaginaryBehemoths',
                     'ImaginaryCarnage',
                     'ImaginaryDemons',
                     'ImaginaryDragons',
                     'ImaginaryElementals',
                     'ImaginaryHorrors',
                     'ImaginaryHybrids',
                     'ImaginaryLeviathans',
                     'ImaginaryMonsterGirls',
                     'ImaginaryUndead',
                     'ImaginaryWorldEaters', },
        'technology': {'ImaginaryArmor',
                       'ImaginaryCybernetics',
                       'ImaginaryCyberpunk',
                       'ImaginaryFutureWar',
                       'ImaginaryFuturism',
                       'ImaginaryMechs',
                       'ImaginaryPortals',
                       'ImaginaryRobotics',
                       'ImaginaryStarships',
                       'ImaginarySteampunk',
                       'ImaginaryVehicles',
                       'ImaginaryWarships',
                       'ImaginaryWeaponry', },
        'fandoms': {'ImaginaryAzeroth',
                    'ImaginaryDarkSouls',
                    'ImaginaryFallout',
                    'ImaginaryJedi',
                    'ImaginaryKanto',
                    'ImaginaryMarvel',
                    'ImaginaryMiddleEarth',
                    'ImaginaryNecronomicon',
                    'ImaginaryOverwatch',
                    'ImaginaryTamriel',
                    'ImaginaryWarhammer',
                    'ImaginaryWesteros',
                    'ImaginaryWitcher', },
        'misc': {'ImaginaryNetwork',
                 'ImaginaryBestOf',
                 'ImaginaryAww',
                 'ImaginaryColorscapes',
                 'ImaginaryFeels',
                 'ImaginaryMaps',
                 'ImaginaryUnofficial',
                 'ImaginaryPets',
                 'ImaginarySliceOfLife',
                 'ImaginaryTurtleWorlds',
                 'ImaginaryWTF', },
        'friends': {'AdorableDragons',
                    'AlternativeArt',
                    'ApocalypsePorn',
                    'ArmoredWomen',
                    'ArtPorn',
                    'BadAssDragons',
                    'ImpracticalArmour',
                    'INEGentlemanBoners',
                    'Isometric',
                    'Moescape',
                    'mtgporn',
                    'PopArtNouveau',
                    'Pulp',
                    'Raining',
                    'ReasonableFantasy',
                    'SpecArt',
                    'StarshipPorn',
                    'SuperStructures',
                    'SympatheticMonsters',
                    'UnusualArt',
                    'Wallpapers',
                    'ZodiacArt', },
    }

    def getNewPost(self, rslash: str, limit: int = 1):
        all_submissions = []
        # rslash = input("enter the name of the subreddit: ")
        subreddit = INE.reddit.subreddit(rslash)
        # print(subreddit.title)
        for submission in subreddit.new(limit=limit):
            # print(submission.url)
            all_submissions.append((submission.url, submission.title))
            # return submission.url, subreddit.title
        return all_submissions

    def getHotPost(self, rslash: str, limit: int = 2):
        all_submissions = []
        subreddit = INE.__reddit.subreddit(rslash)
        c = 0
        for submission in subreddit.hot(limit=limit):
            if c == 0:
                c += 1
                continue
            all_submissions.append((submission.url, submission.title))
        return all_submissions

    def getTopPost(self, rslash: str, limit: int = 1):
        all_submissions = []
        subreddit = INE.reddit.subreddit(rslash)
        print(subreddit.title)
        for submission in subreddit.top(limit=limit):
            all_submissions.append((submission.url, submission.title))
        return all_submissions

    def get_categories(self):
        return INE.__categorires

    def get_sub_reddit(self, category=None):
        if category == None:
            li = []
            for i in INE.__categorires:
                li += INE.__all_subreddit[i]
            return li
        return list(INE.__all_subreddit[category])
