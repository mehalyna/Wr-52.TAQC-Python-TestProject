import configparser
import os

# Get the path to the credentials.ini file
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources', 'credentials.ini')

config = configparser.ConfigParser()
config.read(file_path)

# Get values from the IRINA section
irina_email = config.get('IRINA', 'IRINA_EMAIL')
irina_password = config.get('IRINA', 'IRINA_PASSWORD')
irina_account_name = config.get('IRINA', 'IRINA_ACCOUNT_NAME')

# Print the values to verify they were retrieved correctly
print(type(irina_email))
print(irina_password)
print(irina_account_name)

# Get values from the wrong section
wrong_email = config.get('INVALID', 'INVALID_EMAIL')
wrong_password = config.get('INVALID', 'INVALID_PASSWORD')
