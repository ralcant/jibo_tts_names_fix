from jibo_commands import jibo_commands 
from time import sleep
import json
import glob 
import codecs
import os
from playsound import playsound
def main():
    # """
    # Will play the audio from students_correct file and will make Jibo say it
    # """
    jibo = jibo_commands()
    jibo.start_robot_publisher()
    # parsed_json = json.loads()
    # jsons = glob.glob(.json")
    # jsons = sorted(jsons)
    #all_students = raw_decode('all_studfents.json')
    #input_file = os.path/basename(os.path.dirname(all_students.json))
    with codecs.open('data.json', encoding = 'utf-8') as f:
        all_students = json.load(f)["students"]  #Import the json file
    for student_info in all_students:
        """
        student_info has the following format:
        {
          "Image Taken": "y",
          "Media Release": "N",
          "Home Room Code": 1,
          "Audio": "y",
          "Reading Group Code": "Granger",
          "Reading Group": "SPELHOUSE",
          "F_Name": "Dallas ",
          "Participant Number": "c008",
          "School Code": 1
        },
        """
        read_group = student_info["Reading Group"].replace(" ","").upper()
        name = student_info["F_Name"].replace(" ", "")
        if student_info["Audio"] in {"y", "Y"}:
            if not os.path.exists("students_correct/{}/{}3.mp3".format(read_group,name)):
                print("couldnt find for {} from {}".format(name, read_group))
                #raise ValueError
        else:
            if os.path.exists("students_correct/{}/{}3.mp3".format(read_group,name)):
                print("Shouldnt happen D: {} from {}".format(name, read_group))
            

        """
        if not os.path.exists("students\")
        playsound("students_correct/{}/{}".format("GASOUTHERN", "Andre3.mp3")) 
        break
        if not os.path.exists("students_correct/{}".format(folder)): 
            print("NO found for {}".format(student_info["Reading Group"]))
            pass
        else:
            pass
            #print("FOUND for {}".format(student_info["Reading Group"]))
        """
    print(len(all_students))
    # while True:

    #####
    # pass
if __name__ == "__main__":
    main()