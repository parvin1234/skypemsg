import sys
from st2common.runners.base_action import Action
from skpy import Skype
from getpass import getpass # You probably don't want your password shown in plain text!

class MyAction(Action):

    def run(self, userName,password,contactName,message):
        sk = Skype(userName, getpass(password))
        ch = sk.contacts[contactName].chat
        ch.sendMsg(message) 
        print("message sent!!")
