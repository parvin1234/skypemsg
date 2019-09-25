import sys
from st2common.runners.base_action import Action
from skpy import Skype


class MyAction(Action):

    def run(self,userName,password,contactName,message):
        sk = Skype(userName, password)
        ch = sk.contacts[contactName].chat
        ch.sendMsg(message) 
        print("message sent!!")
