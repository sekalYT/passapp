import os
import requests

class FileSync:
    def __init__(self, server_url, user_id):
        self.server_url = server_url
        self.user_id = user_id
        self.database_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.db')

    def upload_file(self):
        try:
            with open(self.database_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(
                    f"{self.server_url}/upload/{self.user_id}", 
                    files=files
                )
                if response.status_code == 200:
                    print("File uploaded successfully")
                else:
                    print(f"Upload failed with status code: {response.status_code}")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self):
        try:
            response = requests.get(f"{self.server_url}/download/{self.user_id}")
            if response.status_code == 200:
                with open(self.database_path, 'wb') as file:
                    file.write(response.content)
                print("File downloaded successfully")
            else:
                print(f"Download failed with status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading file: {e}")
