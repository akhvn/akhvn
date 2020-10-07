import zipfile
         
main_zip = zipfile.ZipFile('main.zip','r')
main_zip.extractall('for_main')
main_zip.close()

