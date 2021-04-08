#!/usr/bin/env python3

## std library impports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue

def main():
  ## create session object
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
  
  ## create SSH connection
  sshsession.connect(hostname='10.10.2.3', username='bender', pkey=mykey)
  

  #challenge 1: create function that returns list of commands
  def getCommands():
      our_commands = []
      while True:
          command = input("What command would you like to issue? Enter 'done' when done ").lower()
          if command == "done":
              return our_commands
          else:
              our_commands.append(command)
              

  
  for x in getCommands():
    ## call our imported function and save the value returned
    resp = cmdissue(x, sshsession)
    ## if returned response is not null, print it out
    if resp != "":
      print(resp)
  
  ## end the SSH connection
  sshsession.close()

if __name__ == '__main__':
  main()

