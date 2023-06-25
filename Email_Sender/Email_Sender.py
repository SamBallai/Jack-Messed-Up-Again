import smtplib
import email_listener
import re
import fabric
from discord import SyncWebhook
from tkinter.tix import INTEGER
from email.message import EmailMessage

email_sender = 'sam@ballai.net'
email_pass = 'PRIVATE'
folder = "Inbox"
attachment_dir = r"C:\Users\Sam\Downloads"

def listen_for_email():
    #basic email listener ripped from email_listener documentation, listens ~forever~
    el = email_listener.EmailListener(email_sender, email_pass, folder, attachment_dir)
    messages = el.scrape()
    print(messages)
    heat_death_of_universe = INTEGER.MAX_VALUE
    el.timeout(heat_death_of_universe)

def jack_messed_up(message):
    #searches for jack's favorite words
    #if his email says the world is on fire
    if re.search('^(?:ker(?:dricked|f(?:rick|uckl)ed)|meltdown|burning)$', message):
        reset_server()
        send_email()
        ping_discord("Jack is taken care of")
    #in every other scenario Jack needs actual help
    else:
        ping_discord("Jack needs real help")

def ping_discord(ping):
    #Let me know that something happened
    #faster than email
    webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1122634167163830282/oylTqtvEVIVlMSreogRhF3Xga-oNk4p29VPYG7daf5_xLeTPZsJv0NHolNOCkTZsMybB")
    webhook.send(ping)

def send_email():
    #Basic email reset script ripped from smtp docs
    email = EmailMessage()
    email['from'] = 'Sam Ballai'
    email['to'] = 'jack@business.com'
    email['subject'] = 'no problem'

    email.set_content('No problem Jack, everything should be working again. Let me know if there are any issues.\n\nThanks,\nSam Ballai')

    with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email_sender, email_pass)
        smtp.send_message(email)

def reset_server():
    #Hacky, bad way to do this but I'm pretty sure this is
    #how I used to have it work
    #Instantiate a fabric connection, put a bash file
    #on his machine and run it to restart it
    c = Connection('jack@foobar.com:22')
    c.put('reset.sh', '/hidden')
    c.run('/hidden/reset.sh')
