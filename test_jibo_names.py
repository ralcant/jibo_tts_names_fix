from jibo_commands import jibo_commands 
from time import sleep
import json
import glob 
def main():
    """
    Will play the audio from students_correct file and will make Jibo say it
    """
    jibo = jibo_commands()
    jibo.start_robot_publisher()

    jsons = glob.glob(.json")
    jsons = sorted(jsons)
    while True:

    #####
    pass
if __name__ == "__main__":
    main()