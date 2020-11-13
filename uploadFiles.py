import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)    
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.AldXwkENJHEekHqNfyujruW2_1soTqpX5fW3MmQPzPggqT3r38bBhM_vCwPOywmjjhs7UZXPBQc4lOLbjY28dNqNVQ1u497hmBs2UY1f5a879qzYve0cpOcKj5iYwnXlbDAOggvV"
    transferData = TransferData(access_token)

    # for your reference :
    # file_from = "example.txt"
    # file_to = "/class/example.txt"

    file_from = str(input("Enter the path of the folder you want to send : "))
    file_to = str(input("Enter the path name to the dropbox : "))

    transferData.uploadFile(file_from, file_to)
    print("File has been moved")

if __name__ == '__main__':
    main()