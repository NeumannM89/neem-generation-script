import subprocess
import rosnode
import time
import select
import threading


mongo_command = 'docker restart mongo_db'
sandbox_command = 'roslaunch urobosim_ros_config world.launch'
rosbridge_command = 'roslaunch rosbridge_server rosbridge_websocket.launch'
# sandbox_command = 'roslaunch cram_pr2_pick_place_demo sandbox.launch'
knowrob_command = 'roslaunch knowrob knowrob.launch'
giskard_command = 'roslaunch giskardpy giskardpy_pr2_unreal.launch'
generation_command = 'roslaunch cram_sim_log_generator neem-generation.launch'


mongo_process = None
sandbox_process = None
knowrob_process = None
generation_process = None


def start_mongo_db():
  global mongo_process
  print 'Restarting mongo ...'
  mongo_process = subprocess.Popen(mongo_command.split(), bufsize=1, universal_newlines=True)
  mongo_process.wait()
  print 'Restarted mongo'

def start_rosbridge_server():
  global rosbridge_process
  print 'Restarting rosbridge ...'
  rosbridge_process = subprocess.Popen(rosbridge_command.split(), bufsize=1, universal_newlines=True)
  rosbridge_process.wait()
  print 'Restarted rosbridge'

def start_giskard():
  global giskard_process
  print 'Restarting giskard ...'
  giskard_process = subprocess.Popen(giskard_command.split(), bufsize=1, universal_newlines=True)
  time.sleep(20)
  print 'Restarted giskard'

def start_sandbox_():
  global sandbox_process
  print 'Restarting sandbox ...'
  sandbox_process = subprocess.Popen(sandbox_command.split(), bufsize=1, universal_newlines=True)
  time.sleep(1)
  print 'Restarted sandbox'


def start_knowrob_():
  global knowrob_process
  print 'Restarting knowrob ...'
  knowrob_process = subprocess.Popen(knowrob_command.split(), bufsize=1, universal_newlines=True)
  time.sleep(1)
  print 'Restarted knowrob'


def start_neem_process():
  global generation_process
  generation_process = subprocess.Popen(generation_command.split(),bufsize=1, stdout=subprocess.PIPE, universal_newlines=True)
  nice = threading.Timer(3600, generation_process.terminate)
  nice.start()

  for line in iter(generation_process.stdout.readline,''):
    nice.cancel()
    print line.rstrip()
    nice = threading.Timer(360, generation_process.terminate)
    nice.start()


while True:
  try:
    print "start neem process"
    # start_mongo_db()
    # start_rosbridge_server()
    # start_sandbox_()
    start_giskard()
    start_knowrob_()
    start_neem_process()
    print ''
  except Exception as e:
    print "Error occurred"
    print e

print "Finished"

#output, error = process.communicate()
#print output
