#python imports
import sys
import os
import subprocess
from termcolor import colored

#third-party imports
#No third-party imports

#programmer generated imports
from logger import logger
from fileio import fileio

'''
***BEGIN DESCRIPTION***
Type: Info - Description: Executes a grep against the abuse.ch ransomware domains feed.
***END DESCRIPTION***
'''
def POE(POE):

    if (POE.logging == True): 
        LOG = logger() 
    newlogentry = ''
    alx_output_data = ''

    if (POE.domain == False):
        print colored('\r\n[-] Unable to execute abuse.ch ransomware domain grep - target must be a domain - skipping.', 'yellow', attrs=['bold']) 
        if (POE.logging == True):
            newlogentry = 'Unable to execute abuse.ch ransomware domain grep - target must be a domain - skipping.'
            LOG.WriteLog(POE.logdir, POE.target, newlogentry)
            POE.csv_line += 'N/A,'
        return -1

    FI = fileio()

    print '\r\n[*] Running abuse.ch ransomware domain grep against: ' + POE.target

    subproc = subprocess.Popen('grep ' + POE.target + ' /opt/mirage/feeds/RW_DOMBL.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for alx_data in subproc.stdout.readlines():
        if (alx_data != ''):
            print colored('[-] Target appears in the abuse.ch Ransomware Domains feed', 'red', attrs=['bold'])
        if (POE.debug == True):
            print '[DEBUG]: ' + alx_data 
        alx_output_data += alx_data 
    
    if (alx_output_data != ''):                           
        if (POE.logging == True):
            newlogentry = '<strong>abuse.ch: Target appears in the abuse.ch Ransomware Domains feed</strong>'
            LOG.WriteLog(POE.logdir, POE.target, newlogentry)
            POE.csv_line += 'True,'
    else:
        print colored('[-] Target does not appear in the abuse.ch ransomware domains feed', 'yellow', attrs=['bold'])    
        print colored('[x] abuse.ch ransomware domain data not written to file', 'red', attrs=['bold'])
        POE.csv_line += 'False,'

    return 0
