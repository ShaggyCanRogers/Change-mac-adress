import subprocess
import optparse
import re

def get_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac_adress", help="new mac")

    return parse_object.parse_args()

def mac_adress_change(user_interface,user_mac_adress):

    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig1 = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig1))

    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("started")

(user_input,arguments) = get_input()
mac_adress_change(user_input.interface,user_input.mac_adress)
final_mac = control_new_mac(str(user_input.interface))

if final_mac == user_input.mac_adress:
    print("Succesfull!")
else:
    print("Error>")
