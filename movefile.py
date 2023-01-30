""" this program will loop through the file on my defort folder and move them to their respective folder"""
import os, shutil

def movefile(pathtomove, filename):
	shutil.move(filename, pathtomove)
	print(f"{filename} moved to {pathtomove}.........")

def writeHistry(hist):
	history = open('C:\\Users\\Abdulwahab\\Desktop\\movefiletext\\record.txt', 'a')
	for h in hist:
		history.write(h)
		print(f"adding {h} to record.txt.........")
	history.close()
	print('all files record are stores')



#file paths;
#videos
videoPath = 'D:\\abdulwahab\\video'
photoPath = 'D:\\abdulwahab\\photos'
pdfPath = 'D:\\abdulwahab\\library\\others'
appPath = 'D:\\abdulwahab\\android app'

filelist = []
for file in os.listdir('D:\\abdulwahab\\deport'):
	file = os.path.join('D:\\abdulwahab\\deport', file)

	#checking pdf
	if file.endswith('.pdf'):
		movefile(pdfPath, file)
		filelist.append(f'\n{os.path.basename(file)} move to {pdfPath}')
	#checking videos
	elif  file.endswith('.mp4'):
		movefile(videoPath, file)
		filelist.append(f'\n{os.path.basename(file)}')
	#checking photos
	elif  file.endswith('.jpg'):
		movefile(photoPath, file)
		filelist.append(f'\n{os.path.basename(file)} move to {photoPath}')
	#checking app
	elif file.endswith('.apk'):
		movefile(appPath, file)
		#filelist.append(f'\n{os.path.basename(file)}')
	else:
		print(f'{os.path.basename(file)} is unknown file')
		#filelist.append(f'\n{os.path.basename(file)}')

writeHistry(filelist)
print('done')