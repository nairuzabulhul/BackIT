"""
    A python program that backs up all important document in the you system

"""
import shutil, os, datetime
import time
import logging
from shutil import copytree


backup_date = datetime.datetime.now().strftime('%d-%b-%Y')
backup_destination = 'C:\\BackUp - ' + backup_date

desktop_original = os.path.join(os.path.expandvars("%userprofile%\Desktop"))
download_original = os.path.join(os.path.expandvars("%userprofile%\Downloads"))

backup_desktop = backup_destination +'\\Desktop - '+ backup_date
backup_downloads = backup_destination + '\\Downloads'+ backup_date


def usage():
    """This funciton shows how to use the program"""

    pass
  

def back_up(source_directory, destination_directory):

    """This function copies all folders, sub folders
        and files from sources directory"""

    # check if the destination folder exists or not
    if os.path.isdir(destination_directory):

         # if it exits, remove the old folder
         shutil.rmtree(destination_directory)
         
    else:

       # if not, create a new folder and copy everythign from the source to destination  
       shutil.copytree(source_directory,destination_directory)

    # print a message after the process is done  
    print "Copying Files is Done ........................................."
     

def main():

   # Copy Desktop
   back_up(desktop_original, backup_desktop)

      
if __name__ == "__main__":

    main()
    
#TODO:

# create a back up with date stamps (DONE)

# Creat a menu for the tasks that asks users to choose what to back up
# back_up_desktop

# The new copied backup has "backup" tag at the end and time when the file was created
# back_up_ebooks

# back_up_images

# back_up_documents

# back_up_downloads

# CAREFUL: if the file exists , create a new one with tag copy 

# List all the drives on the host machine

# print a message for the user for confirmation

# send the file to trash when the user choose to delete

# Add option of delete permenantaly

# Add size of the folders

# Add list of contents

# send to email or USB , detects of usb is on or off, dropbox, google drive

# Note: becareful where to back up your information, if they sensitive DO NOT USE THE CLOUD

# Add Progress Bar for the copying funtion 

##
##import shutil, os
##
##
##back_up_desktop = 'C:\\Users\\geek_xx\\Desktop\sec'
##
###shutil.copytree(back_up_desktop, 'C:\\bacon_backup')
##
###shutil.move(back_up_desktop, 'C:\\bacon_backup')
##
##for folder_name, sub_folder, fileNames in os.walk('C:\\'):
##
##    print ('curent folder' + folder_name)
##
##    for sub_folder in sub_folder:
##        print('sub folder' + sub_folder)
##
##    for fileNames in fileNames:
##        print 'files' + fileNames
##
##    print('')
