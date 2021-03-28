
########################################### To copy .txt files from one folder to another folder ###############################

import os
import re
import shutil



RegexPattern=re.compile(r'\w+\.+txt$')

for folders,subfolders,files in os.walk('/home/kapil/Desktop/Demo'):
	# checking .txt files in subfolders
	
	for subfolder in subfolders:
		
		os.chdir(os.path.join('/home/kapil/Desktop/Demo',subfolder))
		
		if len(os.listdir())>0:  # If there are files in subfolder
			
			for filename in os.listdir():
				
				if len(RegexPattern.findall(filename))>0:
					os.chdir('/home/kapil/Desktop/textfiles')
			
					
					if filename not in os.listdir(): #Check if file is not present on target folder only then copy
						
						shutil.copy('/home/kapil/Desktop/Demo/'+subfolder+'/'+filename,'/home/kapil/Desktop/textfiles')
						
						os.chdir('/home/kapil/Desktop/Demo')
		
	# Check .txt file in folder		
	for filename in files:
		
		if len(RegexPattern.findall(filename))>0:
			
			os.chdir('/home/kapil/Desktop/textfiles')
			
			if filename not in os.listdir():
			
				shutil.copy('/home/kapil/Desktop/Demo/'+filename,'/home/kapil/Desktop/textfiles')
				
				os.chdir('/home/kapil/Desktop/Demo')
