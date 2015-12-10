#!/bin/env python
#!coding: utf-8
import os 

user_file = "user.txt"
if not os.path.exists(user_file):
    f = open(user_file,'w')
    f.close
def htmlgener(table):
  html_str = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title> Reboot  </title>
  </head>
  <body>
    <form action="/add">
        username: <input name="username" type="text">
        password: <input name="password" type="password">
        <input type="submit" value="add">
    </form>
    <table border="1">
      <tr>
        <td>user <td>
        <td>pwd <td>
        <td>oprate <td>
      </tr>
        %s
    </table>

  </body>
</html>
''' % table
  return html_str 


def show():
  user_dict = {}
  try:
      f = open(user_file,'r')
  except IOError,e:
      print "user_file does not exist, check the filename or permission."
  try:
      user_lines = f.xreadlines()
  except:
      print user_lines,"error"
      f.close()
  for usr in user_lines:
      usr = usr.split()
      #print usr[0],usr[1] 
      print usr
      if len(usr) == 0:
        continue 
      user_dict[usr[0]] = usr[1]
  f.close()
  return user_dict

def add(username,password):
  users = show()
  if users.has_key(username):
    return False
  try: 
      f = open(user_file,'a')
  except IOError,e:
      print "user_file does not exist, check the filename or permission."
      f.close()
  try:
      user_input = '\n' + username + ' ' + password 
      user_lines = f.write(user_input)
  except:
      print user_lines,"error"
  f.close()
  return True

def userdel(username):
  user_dict = show()
  with open(user_file,'w') as f:
      del user_dict[username]
      usr_list = []
      for name_list in user_dict.items():
          usr_list.append(name_list)
      f.write('\n'.join([ ' '.join(i) for i in usr_list ]))
  return True
