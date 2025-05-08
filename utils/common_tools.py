import random
import string
import subprocess
import base64
import hashlib

''' run commands'''
def get_connected_uuid():
    try:
        result = subprocess.run(["xcrun", "xctrace", "list", "devices"], capture_output=True, text=True, check=True)
        output = result.stdout
        udids = []
        for line in output.splitlines():
            if '(' in line and ')' in line and 'iPhone'.lower() in line.lower():
                parts = line.split('(')
                if len(parts) >= 3:
                    udid_candidate = parts[2].strip(') ')
                    if len(udid_candidate) >= 20:
                        udids.append(udid_candidate)
        if not udids:
            raise RuntimeError("No physical iOS devices detected. Please connect your device via USB.")
        return udids[0]
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to retrieve UDID. Error: {e.stderr.strip()}")


'''Handle Login Api Flow'''
def remove_non_base64_characters(s):
    base64_only = s.replace("_", "/")
    base64_only = base64_only.replace("-", "+")
    base64_only = base64_only.replace("=", "")
    return base64_only

def base64_url_encoded_string(data):
    base64_encoded = base64.b64encode(data)
    base64_url_encoded = base64_encoded.rstrip(b'=').replace(b'+', b'-').replace(b'/', b'_')
    return base64_url_encoded.decode('utf-8')


def generateCodeChallenge(serverNonce, clientNonce):
    server_nonce_cleaned = remove_non_base64_characters(serverNonce)
    server_nonce_data = base64.b64decode(remove_non_base64_characters(server_nonce_cleaned))
    client_nonce_data = base64.b64decode(clientNonce)

    sha256 = hashlib.sha256()
    sha256.update(server_nonce_data)
    sha256.update(client_nonce_data)

    hash_data = sha256.digest()
    code_challenge = base64_url_encoded_string(hash_data)
    return code_challenge

# serverNonce = 'filnp84qW5Ha20Bn0thzAN8DbXCqSC_qqB-gadrISRXdc-M9'
# clientNonce = 'fTXSfzCIZLskDIF1rxyINcKx1/gdVk2p2qLKF12I+huR'
# print(generateCodeChallenge(serverNonce, clientNonce))


'''Handle Data'''

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


def get_random_username():
    random_string = ''
    for i in range(15):
        random_string = generate_random_string(15)
    return random_string


def generate_random_text(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choices(characters + " ", k=length))
    return random_string


def get_random_text():
    random_string = ''
    for i in range(50):
        random_string = generate_random_text(50)
    return random_string


def get_expected_interests(a, b):
    new_list = a
    for item in b:
        if item not in new_list:
            new_list.append(item)
        else:
            new_list.remove(item)

    return new_list


def get_file_direction(name):
    result = subprocess.run(['which', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return result.stdout.decode('utf-8').strip()
    else:
        return f"can't find {name}"


def kill_appium():
    output = subprocess.check_output(['ps', 'ax']).decode('utf-8')
    for line in output.splitlines():
        if 'appium' in line:
            pid = line.split()[0]
            name = line.split()[-1]
            print(f'find process：PID={pid}，name={name}')
            subprocess.call(['kill', pid])
            print(f'process {name} is killed')

    if 'appium' not in output:
        print('no running Appium process')



