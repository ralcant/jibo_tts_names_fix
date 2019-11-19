import os
import glob
def format_name(audio_file):
	"""
	Assumes
	file extension = .mp3
	"""
	all_lower_but_type = audio_file[:-3].lower()
	first_upper = all_lower_but_type[0].upper()
	return "{}{}{}".format(first_upper, all_lower_but_type[1:-1], ".mp3")
def change_format_audios():
	root = "students_correct"
	for reading_group in os.listdir(root):
		path_to_read_group = "{}/{}".format(root, reading_group)
		if os.path.isdir(path_to_read_group): # excluding the.csv files 
						    				   # in this folder

			for student_audio_file in os.listdir(path_to_read_group):
				if student_audio_file.endswith(".mp3"): #just check if valid audio
					#print("Previous:", student_audio_file)
					good_format_name = format_name(student_audio_file)
					#print("Changed:",good_format_name)
					if student_audio_file != good_format_name:
						print("Formatting filename form {} to {}".format(student_audio_file, good_format_name))
						os.rename("{}/{}".format(path_to_read_group,student_audio_file), "{}/{}".format(path_to_read_group, good_format_name))
						
			"""
			only_audio_files = "{}/*.mp3".format(path_to_read_group)
			for student_audio_file in glob.glob(only_audio_files):
				print(student_audio)
			"""

if __name__ == "__main__":
	change_format_audios()