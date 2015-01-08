def resolve(command, query):
  import re
  _command = "";
  if re.match("play|add", command) and len(query) > 0 :
    _query = "any " + " any ".join(query.split(" "))
    _command = "/usr/local/bin/mpc search {0} | /usr/local/bin/mpc add".format(_query)
    if re.match("play", command):
      _command = "/usr/local/bin/mpc clear; {0}; /usr/local/bin/mpc play;".format(_command)
  elif re.match("play", command):
    _command = "/usr/local/bin/mpc play"
  elif re.match("next|forward", command):
    _command = "/usr/local/bin/mpc next"
  elif re.match("back|previous", command):
    _command = "/usr/local/bin/mpc prev"
  elif re.match("clear", command):
    _command = "/usr/local/bin/mpc clear"
  elif re.match("stop", command):
    _command = "/usr/local/bin/mpc stop"
  return _command

def results(fields, original_query):
  query = fields.get('~query', '')
  flags = fields.get('~flag', '')
  command = fields['~command']
  resolved = resolve(command, query)
  return {
    "title": "mpc {0} {1} {2}".format(command, query, flags),
    "run_args": [resolved]
  }

def run(command):
  import os
  os.system(command)
