#!/usr/bin/env python2.7
__author__ = "Bartlomiej Mika"
__copyright__ = "Copyright (c) 2015 by Bartlomiej Mika.  All Rights Reserved"
__license__ = "MIT"
__version__ = "1.0"
import xmlrpclib
import json
import datetime
import sys
import base64


# Enter the address that you would like to run this answering service on.
MY_BITMESSAGE_ADDRESS = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Enter the URL to the BitMesssage server instance.
MY_BITMESSAGE_SERVER = "http://username:password@127.0.0.1:8442/"


def stringToBase64(s):
    return s.encode("base64")  # Python 2.x


def base64ToString(b):
    return b.decode("base64")  # Python 2.x


def get_message(filename):
    lines = tuple(open(filename, 'r'))  # Python 2.x

    message = ""
    for line in lines:
        message += line
    return message


def save_message(filename, subject, body, senders_address):
    # Open our file which handles saving our messages and append the latest
    # message sent from client.
    with open(filename, "a") as myfile:
        now = datetime.datetime.now()
        myfile.write("---------------------------------------------------\n\n")
        myfile.write("FROM: " + senders_address + "\n\n")
        myfile.write("SUBJECT: " + subject + "\n\n")
        myfile.write("DATE: " + now.isoformat() + "\n\n")
        myfile.write("BODY:\n")
        myfile.write(body + "\n\n")
        myfile.write("---------------------------------------------------\n\n\n")


def send_message(api, subject, body, senders_address):
    try:
        subject = stringToBase64(subject)
        body = stringToBase64(body)
        api.sendMessage(senders_address, MY_BITMESSAGE_ADDRESS, subject, body)
    except Exception as e:
        print("Error trying to send message")
        print(e)


def main():
    api = None
    try:
        api = xmlrpclib.ServerProxy(MY_BITMESSAGE_SERVER)
    except:
        e = sys.exc_info()[0]
        print("Error connecting to Bitmessage %s" % e)
        sys.exit()

    try:
        inboxMessages = json.loads(api.getAllInboxMessages())
        for message in inboxMessages['inboxMessages']:
            msgid = str(message['msgid'])
            senders_address = str(message['fromAddress'])
            to_address = str(message['toAddress'])

            # Only perform this answering machine service on the specific address.
            if to_address in MY_BITMESSAGE_ADDRESS:
                # This is how you get the message body & subject.
                subject = base64ToString(message['subject'])
                body = base64ToString(message['message'])

                # Record our message locally into our answering machine
                save_message('inbox_tape.txt', subject, body, senders_address)

                # Get the message we will send back to our sender.
                answering_machine_messsage = get_message('outbox_tape.txt')

                # Send our recorded message to the sender.
                send_message(api, "Hi", answering_machine_messsage, senders_address)

                # Delete the message when finished
                api.trashMessage(msgid)
    except Exception as e:
        print(e)
        print("Deleting invalid message")
        api.trashMessage(msgid)


if __name__ =="__main__":
    main()
