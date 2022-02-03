import os
import dropbox
from dropbox.files import WriteMode

class TranferData:
       def_init_(self,access_token):
       self.access_token = access_token 



       def upload_files(self,file-from,file_to):
           dbx = dropbox.Dropbox(self.access_token)


           for root,dirs,files in os.walk(file_from):
               for filename in files:
                   local_path = os.path.join(root,filename)

                   relative_path = os.path.relpath(local_path,file_from)
                   dropbox_path = os.path.join(file_to,relative_path)

                   with open(local_path ,"rb")as f:
                       dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))


def main():
    access_token = "sl.BBW_nmHGpBsQR8akE6g_B3WNd9uWn0DH9-sUYu_ONgfoGJQbxy2wDvy9shqrALwoEbg3Fs0_225XAccU1fYAnLgYNv6J_GMeY34xyVCjN9tQ12cpA54SgahF_anQZwyiurFGauOa8qs"
    transferData =transferData(access_token)

    file_from = star(input("Enter the folder path to transfer:-"))
    file_to = input (" enter the full path to upload to g=dropbox:-")

    transferData.upload_file(file_from,file_to) 
    print("file has been moved !!!")

    main()
