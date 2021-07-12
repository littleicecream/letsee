from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1782134960:AAFIAEXf0eDtG5atyUNgZ4a-qbQgoqqd_XA"
    APP_ID = 2469678
    API_HASH = "d692515312741702751ad5525dbd91c3"
    OWNER_ID = 1317637067
    AUTH_CHANNEL = [-521884514]
    DESTINATION_FOLDER = "Gdrive bot" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[Becky Rich]
type = drive
client_id = 295714881629-ngjl6bv7h8bbbvhd3vd4l2sou9je1kla.apps.googleusercontent.com
client_secret = JdGaTl1CItJl18P9sdZccS_q
scope = drive
token = {"access_token":"ya29.a0AfH6SMC91dnYtSM7T9SNZRLH5YW6lswO-0FYEMfAzaixrBfND9Vj4HA4jMt2XabeTTpgXSoPTFVx1AS9SmPIp_cR55fEYYeCQjN3CEbzOZFSZPSdTeVKA7BOyzROuqSswp5nA7pwzXkSbB0SX4svcjElWXnxdZ8","token_type":"Bearer","refresh_token":"1//0gBcLuo7cOjNgCgYIARAAGBASNwF-L9IrAg3gmFe8N3wRdRNfZJgdNou_i1N1P2giJsFODHAhd2zy7trVtH_-r5IXNsa6ktt64Wc","expiry":"2021-05-29T10:20:17.9315975+06:00"}
root_folder_id = 1iSFRvg7XsaGvTiuOmbYB9LmYdLBn7dts
"""
