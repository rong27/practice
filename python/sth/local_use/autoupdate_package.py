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

    #print message
    return_string = os.linesep + str(buffer.getvalue())
    return_string = return_string.replace("<script language=\\'javaScript\\'>document.write(\\'.\\')</script>", "")
    return_string = return_string.replace("<script language=\\'javaScript\\'>document.write(\\'<BR>\\')</script>", "")
    return_string = return_string.replace("<script language=\\'javaScript\\'>", "")
    return_string = return_string.replace("</script>", os.linesep)
    return_string = return_string.replace("\\n",  os.linesep)

    replace_list = ["<html>", "<head>", "</head>", "<pre>", "</pre>", '<script type="text/javascript">',
                    "<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' /></script>",
                    "<script type=\\'text/javascript\\' src=\\'/include/common.js\\'></script>",
                    "<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' /><script "
                    "type=\\'text/javascript\\' src=\\'/include/common.js\\'>",
                    "b'<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' />",
                    "<script type=\\'text/javascript\\' src=\\'/include/common.js\\'>"
                    ]
    for text in replace_list:
        return_string = return_string.replace(text, "")

    print(return_string)

    
    logging.info("Upgrade package End")
    print(camera_ip + " : Upgrade pkg Done")




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

    #print message
    return_string = os.linesep + str(buffer.getvalue())
    return_string = return_string.replace("<script language=\\'javaScript\\'>document.write(\\'.\\')</script>", "")
    return_string = return_string.replace("<script language=\\'javaScript\\'>document.write(\\'<BR>\\')</script>", "")
    return_string = return_string.replace("<script language=\\'javaScript\\'>", "")
    return_string = return_string.replace("</script>", os.linesep)
    return_string = return_string.replace("\\n",  os.linesep)

    replace_list = ["<html>", "<head>", "</head>", "<pre>", "</pre>", '<script type="text/javascript">',
                    "<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' /></script>",
                    "<script type=\\'text/javascript\\' src=\\'/include/common.js\\'></script>",
                    "<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' /><script "
                    "type=\\'text/javascript\\' src=\\'/include/common.js\\'>",
                    "b'<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' />",
                    "<script type=\\'text/javascript\\' src=\\'/include/common.js\\'>"
                    ]
    for text in replace_list:
        return_string = return_string.replace(text, "")

    print(return_string)

    
    logging.info("Upgrade package End")
    print(camera_ip + " : Upgrade pkg Done")


def auto_upgrade_package_password_forVU(camera_ip, package_path):
    logging.info("Upgrade Package Start")

    buffer = BytesIO() 
    c = pycurl.Curl()
    c.setopt(c.URL, "http://{}/cgi-bin/admin/upload_vadp.cgi".format(camera_ip))
    c.setopt(c.HTTPPOST, [("smartvca_pkg", (c.FORM_FILE, package_path))])
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.HTTPAUTH, c.HTTPAUTH_BASIC)
    c.setopt(c.USERNAME, "admin")
    c.setopt(c.PASSWORD, "admin2050")
    c.setopt(pycurl.TIMEOUT, 60)  #second
    c.setopt(pycurl.VERBOSE, 0)  #1: 要顯示執行進度
    c.perform()
    c.close
    
    #print message
    return_string = os.linesep + str(buffer.getvalue())
    return_string = return_string.replace("<script language=\\'javaScript\\'>document.write(\\'.\\')</script>", "")
    return_string = return_string.replace("<script language=\\'javaScript\\'>document.write(\\'<BR>\\')</script>", "")
    return_string = return_string.replace("<script language=\\'javaScript\\'>", "")
    return_string = return_string.replace("</script>", os.linesep)
    return_string = return_string.replace("\\n",  os.linesep)

    replace_list = ["<html>", "<head>", "</head>", "<pre>", "</pre>", '<script type="text/javascript">',
                    "<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' /></script>",
                    "<script type=\\'text/javascript\\' src=\\'/include/common.js\\'></script>",
                    "<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' /><script "
                    "type=\\'text/javascript\\' src=\\'/include/common.js\\'>",
                    "b'<meta http-equiv=\\'Content-Type\\' content=\\'text/html; charset=utf-8\\' />",
                    "<script type=\\'text/javascript\\' src=\\'/include/common.js\\'>"
                    ]
    for text in replace_list:
        return_string = return_string.replace(text, "")

    print(return_string)


    logging.info("Upgrade package End")
    print(camera_ip + " : Upgrade pkg Done")



field_try_camera = {"TainanPark":"172.20.20.106", "Tainan_FD":"172.20.6.8", "Taipei":"192.168.21.105", "TaipeiIR":"172.16.10.24"}
pkgpath = "C:\\Users\\joy.lin\\Desktop\\weekly_smartvca_pkg\\20190419\\VCA-6.1.5.faa13-hi3519-smartvca.tar.gz"

# auto_upgrade_package_password_not_the_same("172.20.6.3", pkgpath)

# auto_upgrade_package_password_forVU("64.41.218.17", pkgpath)


for v in field_try_camera.values():
    # print(v)
    auto_upgrade_package(v, pkgpath)

