import tkinter
from tkinter import ttk
from tkinter import *
import requests
# noinspection PyUnresolvedReferences
from bs4 import BeautifulSoup as bs
import re
# noinspection PyUnresolvedReferences
from googlesearch import search


# Creates the whole application
class tkinterApp(tkinter.Tk):
    # __init__ function (don't understand fully. got from geeksforgeeks)
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        # Creating a container
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting of the different page layouts
        for F in (StartPage, StatsPage, AddDataPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Start page - finished but not pretty
class StartPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Startpage", font=("Courier", 44))
        label.grid(row=0, column=4, padx=325, pady=10, sticky="news")

        button1 = ttk.Button(self, text="Stats Page", command=lambda: controller.show_frame(StatsPage))
        button1.grid(row=1, column=750, padx=10, pady=10, sticky="news")

        button2 = ttk.Button(self, text="Add Data Page", command=lambda: controller.show_frame(AddDataPage))
        button2.grid(row=1, column=1, padx=10, pady=10, sticky="news")


# Stats Page - Unfinished (not linked with sql)
class StatsPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Stats Page", font=("Courier", 44))
        label.grid(row=0, column=4, padx=325, pady=10, sticky="news")

        button1 = ttk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=750, padx=10, pady=10, sticky="news")

        button2 = ttk.Button(self, text="Add Data Page", command=lambda: controller.show_frame(AddDataPage))
        button2.grid(row=1, column=1, padx=10, pady=10, sticky="news")


# Add Data Page - not linked with sql
class AddDataPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Add Data Page", font=("Courier", 44))  # Header
        label.grid(row=0, column=1, padx=300, pady=10, sticky="news", columnspan=4)

        global playerrow  # For manual entry
        global playercount  # For manual entry
        global playerdictionary  # For manual entry
        playerrow = 9  # To allow for multiple players
        playercount = 0  # Number of players so far
        playerdictionary = {}  # Used with the submit function

        button1 = ttk.Button(self, text="Stats Page", command=lambda: controller.show_frame(StatsPage))  # Stats pg
        button1.grid(row=4, column=4, pady=10)

        button2 = ttk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))  # Start pg
        button2.grid(row=4, column=1, pady=10)

        advancedbutton = ttk.Button(self, text="Advanced", command=lambda: showadvanced())  # shows the manual input options
        advancedbutton.grid(row=3, column=1)

        hideadvancedbutton = ttk.Button(self, text="Hide Advanced", command=lambda: hideadvanced())  # Hides manual entry

        textbarmessage = StringVar()  # Says status of google search
        # noinspection PyUnusedLocal
        instruction = Label(self,
                            text='Input the team Spurs played and the date in the format dd.mm.yyyy e.g. "Chelsea '
                                 '01.04.2018"').grid(row=1, column=1, pady=10, columnspan=2, sticky="nsew")  # How to enter google search
        # noinspection PyUnusedLocal
        textbar = Label(self, textvariable=textbarmessage).grid(row=2, column=1, columnspan=4)
        entry_google = tkinter.Entry(self)  # input box for google search
        entry_google.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        # Advanced buttons
        datetextbar = Label(self, text='Date (dd/mm/yyyy)')  # Instructions for date input
        dateinput = tkinter.Entry(self)  # input box for date
        hometeamtextbar = Label(self, text='Home Team')  # Instructions for the home team
        hometeaminput = tkinter.Entry(self)  # Input box for home team
        homescoretextbar = Label(self, text='Home Score')  # Instructions for home score
        homescoreinput = tkinter.Entry(self)  # Input for home score
        awayteamtextbar = Label(self, text='Away Team')  # Instructions for the away team
        awayteaminput = tkinter.Entry(self)  # Input for away team
        awayscoretextbar = Label(self, text='Away Score')  # Instructions for away score
        awayscoreinput = tkinter.Entry(self)  # Input for away score
        submitbutton = ttk.Button(self, text="Submit", command=lambda: submitadvanced())  # Submit manual input
        addnewplayerbutton = ttk.Button(self, text="New Player", command=lambda: addnewplayer())  # Adds new player line
        advancedinstructions = Label(self, text='Please input the game details manually')  # Manual instructions

        # Checkboxes Instructions
        checkboxhomeoraway = Label(self, text='Home Team')
        checkboxog = Label(self, text='Own Goal')

        # Players button
        def addnewplayer():
            global playerrow
            global playercount
            global playerdictionary
            playercount = playercount + 1  # Adds how many players

            # Player name instructions and input box (variable will go up by 1 each time e.g. playername1, playername2)
            globals()['playernameinstruction%s' % playercount] = Label(self, text="Player Name (e.g Kane)")
            globals()['playernameinstruction%s' % playercount].grid(row=playerrow, column=1)
            globals()['playername%s' % playercount] = tkinter.Entry(self)
            globals()['playername%s' % playercount].grid(row=playerrow, column = 2)

            # Player goal minutes instructions and input box (variable will go up by 1 each time)
            globals()['playergoalinstruction%s' % playercount] = Label(self, text="Minutes of goals scored (e.g. 58, 62, 78)")
            globals()['playergoalinstruction%s' % playercount].grid(row=playerrow, column=3)
            globals()['playergoal%s' % playercount] = tkinter.Entry(self)
            globals()['playergoal%s' % playercount].grid(row=playerrow, column=4)

            # Checkboxes for home team/away team and own goal (variable will go up by 1 each time)
            globals()['homeoraway%s' % playercount] = Checkbutton(self)
            globals()['homeoraway%s' % playercount].grid(row=playerrow, column=5)
            globals()['owngoal%s' % playercount] = Checkbutton(self)
            globals()['owngoal%s' % playercount].grid(row=playerrow, column=6)

            # Changing positions of submit button, add new player button, and the different pages buttons
            submitbutton.grid(row=playerrow + 2, column=2, columnspan=2)
            addnewplayerbutton.grid(row=playerrow + 1, column=2, columnspan=2)
            button1.grid(row = playerrow + 2, column=4)
            button2.grid(row=playerrow+2, column=1)
            playerrow = playerrow + 1

        # Hides advanced menu
        def hideadvanced():
            hideplayer = 1  # Used for the multiple variables for player goals
            advancedinstructions.grid_remove()
            datetextbar.grid_remove()
            dateinput.grid_remove()
            hometeamtextbar.grid_remove()
            hometeaminput.grid_remove()
            homescoretextbar.grid_remove()
            homescoreinput.grid_remove()
            awayteamtextbar.grid_remove()
            awayteaminput.grid_remove()
            awayscoretextbar.grid_remove()
            awayscoreinput.grid_remove()
            submitbutton.grid_remove()
            addnewplayerbutton.grid_remove()

            # Removes each player variable (e.g. playername1, playername2 etc.)
            while hideplayer <= playercount:
                globals()['playernameinstruction%s' % hideplayer].grid_remove()
                globals()['playername%s' % hideplayer].grid_remove()
                globals()['playergoalinstruction%s' % hideplayer].grid_remove()
                globals()['playergoal%s' % hideplayer].grid_remove()
                globals()['homeoraway%s' % hideplayer].grid_remove()
                globals()['owngoal%s' % hideplayer].grid_remove()
                hideplayer = hideplayer + 1

            hideadvancedbutton.grid_remove()  # Removes hide advanced button
            advancedbutton.grid(row=3, column=1)  # Shows advanced button

        # Searches google for game
        def google_entry():  #
            try:
                textbarmessage.set('Loading...')  # Doesn't work for some reason???
                srch = entry_google.get()  # Gets input box text
                query = 'Sky Sports Tottenham Hotspur ' + str(srch)  # The search term for google (date must be dd.mm.yyyy)
                entry_google.delete(0, 'end')  # Empties input box
                count = 0  # For later on, number of urls its searched through
                for j in search(query, tld="com", num=2, stop=2, pause=2):  # Gets top two results
                    url = j
                    article = requests.get(url)  # Connects to the URL
                    soup = bs(article.content, 'html.parser')  # Makes the HTML more readable and easy to iterate

                    try:  # In case article not correct
                        # Gets the main body of text with scores and teams and goal scorers
                        body = soup.findAll("div", "sdc-site-match-header__teams")

                        # Getting home and away team names
                        teamshtml = body[0].findAll("h4", "sdc-site-match-header__team")  # Gets solely team names and score
                        hometeamhtml = teamshtml[0].findAll("span",
                                                            "sdc-site-match-header__team-name-block-target")  # home html
                        hometeam = re.findall('>([A-Za-z ]*)', str(hometeamhtml[0]))[0]  # Gets team name
                        awayteamhtml = teamshtml[1].findAll("span",
                                                            "sdc-site-match-header__team-name-block-target")  # away html
                        awayteam = re.findall('>([A-Za-z ]*)', str(awayteamhtml[0]))[0]  # gets team name

                        # Getting goals scored by home and away teams for checking later on
                        homescorehtml = teamshtml[0].findAll("span",
                                                             "sdc-site-match-header__team-score-block")  # home score html
                        homescore = re.findall('>([0-9]*)', str(homescorehtml[0]))[0]  # Gets home score
                        awayscorehtml = teamshtml[1].findAll("span",
                                                             "sdc-site-match-header__team-score-block")  # away score html
                        awayscore = re.findall('>([0-9]*)', str(awayscorehtml[0]))[0]
                        textbarmessage.set(
                            f'{hometeam} scored {homescore} goal. {awayteam} scored {awayscore} goals')  # Print check

                        # Getting goal scorers
                        scorershtml = body[0].findAll("ul",
                                                      "sdc-site-match-header__team-synopsis")  # Returns list, 0 home 1 away
                        homescorershtml = scorershtml[0].findAll("li",
                                                                 "sdc-site-match-header__team-synopsis-line")  # Get scorers
                        homescorers = dict()  # Dictionary for the scorer, and the time of the goals they scored
                        for item in homescorershtml:  # Iterates through the home scorers, each scorer has 1 item
                            homescorerregex = re.findall('([A-Za-z]*).\(<span class="sdc-site-match-header__event-time">',
                                                         str(item))  # Gets name
                            homegoalregex = re.findall('"true">([0-9]*)',
                                                       str(item))  # List of the time of goals they scored (minutes)
                            homescorers.update(
                                {homescorerregex[0]: homegoalregex})  # Updates dictionary, creates new entry if not there
                        awayscorershtml = scorershtml[1].findAll("li",
                                                                 "sdc-site-match-header__team-synopsis-line")  # Get scorers
                        awayscorers = dict()  # Dictionary for the scorer, and the time of the goals they scored
                        for item in awayscorershtml:  # Iterates through the away scorers, each scorer has 1 item
                            awayscorerregex = re.findall('([A-Za-z]*).\(<span class="sdc-site-match-header__event-time">',
                                                         str(item))  # Gets name
                            awaygoalregex = re.findall('"true">([0-9]*)',
                                                       str(item))  # List of the time of goals they scored
                            if '<title>red card' in str(item):
                                continue
                            else:
                                awayscorers.update({awayscorerregex[
                                                        0]: awaygoalregex})  # Updates dictionary or creates new value
                        break  # Gets out of for loop
                    except IndexError:  # If it cannot get info from article
                        count = count + 1
                        if count == 2:
                            textbarmessage.set(
                                'Error finding this game. Please enter details manually.')  # lets user know error
                        continue  # Continues onto second article
            except:
                textbarmessage.set('Error. Please enter details manually.')

        searchgoogle = ttk.Button(self, text="Search", command=lambda: google_entry())  # The search button for google
        searchgoogle.grid(row=1, column=4, columnspan=1)

        # Shows advanced menu
        def showadvanced():
            global playercount
            global playerrow
            playercount = 0
            playerrow = 9

            # Shows all advanced manual options
            advancedinstructions.grid(row=4, column=2, columnspan=2)
            datetextbar.grid(row=5, column=1, columnspan=1 )
            dateinput.grid(row=5, column=2)
            hometeamtextbar.grid(row=6, column=1)
            hometeaminput.grid(row=6, column=2)
            homescoretextbar.grid(row=6, column=3)
            homescoreinput.grid(row=6, column=4)
            awayteamtextbar.grid(row=7, column=1)
            awayteaminput.grid(row=7, column=2)
            awayscoretextbar.grid(row=7, column=3)
            awayscoreinput.grid(row=7, column=4)
            addnewplayer()  # Gets first new player button
            advancedbutton.grid_remove()
            hideadvancedbutton.grid(row=3, column=1)
        def submitadvanced():
            print('unfinished submit button')




# Driver Code
app = tkinterApp()
app.mainloop()
