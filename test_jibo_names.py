from jibo_commands import jibo_commands 
from time import sleep
import json
import glob 
import codecs
import os
from playsound import playsound
def main():
    jibo = jibo_commands()
    jibo.start_robot_publisher()
    # parsed_json = json.loads()
    # jsons = glob.glob(.json")
    # jsons = sorted(jsons)
    #all_students = raw_decode('all_studfents.json')
    #input_file = os.path/basename(os.path.dirname(all_students.json))
    with codecs.open('all_students_info.json', encoding = 'utf-8') as f:
        all_students = json.load(f)#["students"]  #Import the json file
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
        if student_info["Audio"] in {"y", "Y"}:  #if there is an udio
            sound_path = "audios/{}/{}3.mp3".format(read_group,name)
            if not os.path.exists(sound_path):  #This shouldnt happen
                print("couldnt find audio for {} from {}".format(name, read_group))
            else:
                #playsound(sound_path)
                print("\nChild name: {}".format(name))
                print(" Listen to their pronunciation")
                playsound(sound_path)

                while True:

                    repeat = raw_input("Repeat? [Y\N]: ")

                    if repeat not in {"y", "Y"}:
                        break
                    else:
                        playsound(sound_path)

        else:
            print("Sorry, we don't have an audio for child {}\n".format(name))
        ########## Now try to repeat the pronunciation of Jibo ###########
        print("\n Now, listen to how Jibo pronounces it \n")
        try:
            new_esml = student_info["esml"]
            print("This student seem to already have an esml tag: {} \n".format(new_esml))
        except:
            new_esml = name
            
        while True:
            student_info["esml"] = new_esml            
            #print("Current name:{}".format(new_esml))            
            jibo.send_robot_tts_cmd(new_esml)
            new_esml = raw_input("Enter new esml= ")
            if len(new_esml) > 0:
                pass
            else:
                break    
        print("\nFinal esml tag of {}: {}\n".format(name, student_info["esml"]))
        next_student = raw_input("Continue with next student? [Y/N]: ")
        print("\n################\n")
        if next_student in {"n", "N"}:
            break 

    outf = "all_students_info.json" #just rewrite the file 
    with codecs.open(outf, encoding="utf-8", mode="w") as out_file:
        #new_data = 
        json.dump(all_students, out_file, indent= 4, separators=(",", ": "))
    print("Finished dumnping new data to {}".format(outf))

if __name__ == "__main__":
    main()