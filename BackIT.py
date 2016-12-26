"""
    A python program that backs up all important document in the you system

"""
import shutil, os, datetime
import time
import logging
import zipfile
from shutil import copytree


base_path = os.path.expandvars('%userprofile%')
backup_date = datetime.datetime.now().strftime('%d-%b-%Y')
backup_destination = 'C:\\BackUp'

desktop_original  =  base_path  + '\\Desktop'
download_original =  base_path  + '\\Downloads\\Print 2016'

backup_desktop   = backup_destination + '\\Desktop - '  + backup_date
backup_downloads = backup_destination + '\\Downloads - '+ backup_date

zipped = base_path + '\\Desktop\\Zipped'



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
    print "[*] Copy files ------------------------------- 1"
    print "[*] Compress to a Zipfile -------------------- 2"
    print "[*] Lisr drives on the host machine ---------- 3"
    print "[*] Send files by email ---------------------- 4"
    print "[*] Send files to a Google Drive ------------- 5"
    print "[*] Send files to USB ------------------------ 6"
    print "\n\n"
    
    options = input("Enter a number to start: ")
    

  

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


def extract_file(zip_file):
    
    """ This function extarcts a seclected zipfile to a specific locatio"""
    pass




def detect_drives():
    
    """This function detects the drives on the host machine"""
    pass


def send_zipfile():
    """This function sends the zipfile by email, 
    or cloud services (Google Drive, DropBox)"""
    pass



def main():

    # TODO: create the menu 
    #usage()
    
    back_up(desktop_original, backup_desktop)  # Backup Desktop

    create_zip_file(backup_desktop) # Zipfile
   
          
if __name__ == "__main__":

    main()
    
