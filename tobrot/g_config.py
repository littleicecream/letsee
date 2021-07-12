from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1545908344:AAGoIRLBfYQ1U-XuAMGYfxoYOos2csB49r0"
    APP_ID = 2289087
    API_HASH = "b772764d3eae0090ca6b1aa6f8ebf159"
    OWNER_ID = 1238033099
    AUTH_CHANNEL = [-1001337003986]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 28dslkgjsdl-fill-your-details-apps.googleusercontent.com
client_secret = 6Tib48-fill-your-details-KuXXDX-eWgnRBYc
scope = drive
root_folder_id =
token = {"access_token":"ya29.a-fill-your-details-af4ychuHswBt8X0nf2oWmczsHg6MYPSE6hXo-PJ-fill-your-details-s06KAecfw_H-tYThBtbs:20:25.430920315Z"}
team_drive = 0AB0q-fill-your-details-sdrgsgsdUk9PVA
"""
