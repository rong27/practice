'''
Bulid a smartVCA package and upgrade it to field try camera evey Friday,
So try to use automate way to upgrade package to specific cameras
'''

'''
Use PycURL module
'''

import logging
import pycurl
import os
from io import BytesIO


def auto_upgrade_package(camera_ip, package_path):
    logging.info("Upgrade Package Start")

    buffer = BytesIO() 
    c = pycurl.Curl()
    c.setopt(c.URL, "http://{}/cgi-bin/admin/upload_vadp.cgi".format(camera_ip))
    c.setopt(c.HTTPPOST, [("smartvca_pkg", (c.FORM_FILE, package_path))])
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HTTPAUTH, c.HTTPAUTH_BASIC)
    c.setopt(c.USERNAME, "root")
    c.setopt(c.PASSWORD, "vivo2324")
    c.setopt(pycurl.TIMEOUT, 60)  #second
    c.setopt(pycurl.VERBOSE, 0)  #1: 要顯示執行進度
    c.perform()
    c.close
    
    logging.info("Upgrade package End")
    print(camera_ip + " : Upgrade pkg Done")



field_try_camera = {"TainanFD":"172.20.6.8", "TainanPark":"172.20.20.106", "Taipei":"192.168.21.105", "TaipeiIR":"172.16.0.24"}
pkgpath = "C:\\Users\\joy.lin\\Desktop\\weekly_smartvca_pkg\\20190315\\VCA-6.1.3.81dba-hi3519-smartvca.tar.gz"

# for v in field_try_camera.values():
    # auto_upgrade_package(v, pkgpath)


def auto_upgrade_package_password_not_the_same(camera_ip, package_path):
    logging.info("Upgrade Package Start")

    buffer = BytesIO() 
    c = pycurl.Curl()
    c.setopt(c.URL, "http://{}/cgi-bin/admin/upload_vadp.cgi".format(camera_ip))
    c.setopt(c.HTTPPOST, [("smartvca_pkg", (c.FORM_FILE, package_path))])
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HTTPAUTH, c.HTTPAUTH_BASIC)
    c.setopt(c.USERNAME, "root")
    c.setopt(c.PASSWORD, "Vivo70703897")
    c.setopt(pycurl.TIMEOUT, 60)  #second
    c.setopt(pycurl.VERBOSE, 0)  #1: 要顯示執行進度
    c.perform()
    c.close
    
    logging.info("Upgrade package End")
    print(camera_ip + " : Upgrade pkg Done")

# auto_upgrade_package_password_not_the_same("172.20.6.3", pkgpath)