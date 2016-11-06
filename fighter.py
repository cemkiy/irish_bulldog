class fighter:

    """Fighter
    following properties:

    Attributes:
        id:
        first_name:
        last_name:
        link:
        wins:
        losses:
        draw:
        weight_class:
        age = 18
        reach:
        leg_reach:
        height:
        weight:
        submission_rate:
        striking_rate:
        takedowns_rate:
        striking_succesful_rate:
        grappling_succesful_rate:
        fights = []
    """



    def __init__:
        self.id = ""
        self.first_name = ""
        self.last_name = ""
        self.link = ""
        self.wins = 0
        self.losses = 0
        self.draw = 0
        self.weight_class = ""
        self.age = 18
        self.title_holder = False
        self.reach = 0
        self.leg_reach = 0
        self.height = 0.0
        self.weight = 0.0
        self.submission_rate = 0
        self.striking_rate = 0
        self.takedowns_rate = 0
        self.striking_succesful_rate = 0
        self.grappling_succesful_rate = 0
        self.fights = []

    def download_fighter_data(self):
        self.link = "http://www.ufc.com/fighter/"+ self.first_name + "-" + self.first_name  +"?id="
        fighterResponse = urlopen(self.link).read()
        soup = BeautifulSoup(fighterResponse, 'html.parser')
        fighter_body = soup.find("td", {"id": "fighter-age"}).getText()
        self.age = soup.find("td", {"id": "fighter-age"}).getText()
        self.height = float(soup.find("td", {"id": "fighter-height"}).getText().replace(" ", "").split("(")[1].replace("cm)", ""))
        self.weight = float(soup.find("td", {"id": "fighter-weight"}).getText().replace(" ", "").split("(")[1].replace("kg)", ""))


    def get_fighter_data_from_ufc_api(fighters):
        for fighter in fighters:
            if self.last_name == fighter.last_name:
                self.first_name = fighter.first_name
                self.weight_class= fighter.weight_class
                self.title_holder= fighter.title_holder
                self.wins = fighter.wins
                self.losses = fighter.losses
                self.draw = fighter.draw
                break
