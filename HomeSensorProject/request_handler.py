import re
from login_request_validation.request_validation import check_key, check_value
from check_login.check_auth import checkusr
from read_latest_state.read_latest import readLatestState

def handle_read_latest(jsonfile):
  readLatestState(jsonfile)

def handle_check_user(jsondata):
  return checkusr(jsondata)

def handle_validate_input(params):
  if check_key(params) and check_value(params):
    return True
  else:
    return False