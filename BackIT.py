"""
    A python program that backs up all important document in the you system

"""
import shutil, os, datetime, sys
import time
import logging
import zipfile
import win32api
from shutil import copytree
from twilio.rest import TwilioRestClient

base_path = os.path.expandvars('%userprofile%')
backup_date = datetime.datetime.now().strftime('%d-%b-%Y')
backup_destination = 'C:\\BackUp'

desktop_original  =  base_path  + '\\Desktop'
download_original =  base_path  + '\\Downloads\\Print 2016'
document_original =  base_path + '\\Documents'

backup_desktop   = backup_destination + '\\Desktop - '  + backup_date
backup_downloads = backup_destination + '\\Downloads - '+ backup_date
backup_documents = backup_destination + '\\Documents' +backup_date


zipped = base_path + '\\Desktop\\Zipped'
print zipped

account_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

user_number = '+000000000000'
twilio_number = '+0000000000'

#original_source = ["Desktop", "Documents", "Downloads"] # TO DO MORE OPTIMIZATION

def usage():
    
    """This funciton shows how to use the program"""
                                                                                                                                                                                                                     
    print """
              ____             _    ___ _____ 
             | __ )  __ _  ___| | _|_ _|_   _|
             |  _ \ / _` |/ __| |/ /| |  | |  
             | |_) | (_| | (__|   < | |  | |  
             |____/ \__,_|\___|_|\_\___| |_|"""                                     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        

    print

    print " Menu : \n"
    print "[*] List all the options --------------------- 0"
    print "[*] Back up Desktop -------------------------- 1"
    print "[*] Back up Downloads ------------------------ 2"
    print "[*] Back up Documents ------------------------ 3"
    print "[*] List all dirves -------------------------- 4"
    print "[*] List all the folders --------------------- 5"
    print
    print "* Press q to quit the program"
  

def back_up(source_directory, destination_directory):

    """This function copies all folders, sub folders
        and files from sources directory"""

    try:
        # check if the destination folder exists or not
        if os.path.exists(destination_directory):
            
             # if it exits, remove the old folder
             os.removedirs(destination_directory)
             
        else:
           # if not, create a new folder and copy everythign from the source to destination  
           shutil.copytree(source_directory,destination_directory)

        # print a message after the process is done  
        print "Copying Files is Done ........................................."
        
    except :
        
        print "Files aleady exist"


def create_zip_file(folder):

    """This function creates compresses the files in to a zipfile"""

    folder = os.path.abspath(folder)
    zip_folder = os.path.basename(folder) + ".zip"

    print "Creating %s .................................." % zip_folder 

    # Create the zip file
    backup_zip = zipfile.ZipFile(zip_folder, 'w')

    # Add all the folders, sub folders and files to the zip file
    for folder_names, sub_folders , file_names in os.walk(folder):

         print "Adding files in " + folder_names + "...........\n"
         print
         
         backup_zip.write(folder_names)

         for file_name in file_names:

             new_base_path = os.path.basename(folder)+ '_'

             if file_name.startswith(new_base_path) and file_name.endswith('.zip'):

                 continue

            # Add the files to the zip folder
             backup_zip.write(os.path.join(folder_names,file_name))
        
     # close the zipping
    backup_zip.close()

    print "Done .......................................... "

    # move the file to Zipped folder
    if not os.path.exists(zipped):
        os.mkdir(zipped)
    # moves compressed files there    
    shutil.move(zip_folder, zipped)

def extract_file(zip_file):
    
    """ This function extarcts a seclected zipfile to a specific locatio"""
    pass



def detect_drives():
    
    """This function detects the drives on the host machine"""
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]

    print
    
    print "Primary Drive" , os.getenv("SystemDrive")
    print
    print "Drives" , drives
    

def send_zipfile():
    """This function sends the zipfile by email, 
    or cloud services (Google Drive, DropBox)"""
    pass


def list_all_folers():

    """This function lists all the folders"""
    
    global base_path

    try:
        print
        user_input = raw_input("Enter the directory name: ")
        
        folder_path = base_path + '\\'+ user_input
        print
        folders = os.walk(folder_path).next()[1]

        for i in folders:
            print i  + '\n'

    except:

            print "You entered a wrong command......."
            

def send_message_to_user():

    """This function sends a message to the user
      notifying that the backup is done"""
    
    message = "The backup is done .........."
    twilio_client = TwilioRestClient(account_SID, auth_token)
    twilio_client.messages.create(body=message, from_=twilio_number, to=user_number)


def main():

    # List the menu
    usage()

    while True:
        print 
        options = raw_input("Enter a number to start: ")

        if int(options) == 0:
            usage()
            
        elif int(options) == 1: # desktop
            back_up(desktop_original, backup_desktop)
            create_zip_file(backup_desktop)
            send_message_to_user()
            
        elif int(options) == 2: # download
            back_up(download_original, backup_downloads)
            create_zip_file(backup_downloads)
            send_message_to_user()
            
        elif int(options) == 3: # documents
            back_up(document_original,backup_documents)
            create_zip_file(backup_documents)
            send_message_to_user()
            
        elif int(options) == 4 : # detect all drives on the system
            detect_drives()

        elif int(options) == 5: # list all folder in the directory
            list_all_folers()
            
        elif options == 'q':
            sys.exit()

        else:
            print "Check the Menu"
   
          
if __name__ == "__main__":

    main()
    
