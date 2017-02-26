import sys
import time
import os
from zipfile import ZipFile
from urllib.request import urlopen 
import webbrowser
from io import BytesIO

'''
A curative dictionary of web frameworks boilerplates 
for kick starting any application
'''

frameworks = {
    
    # Front end frameworks like jQuery, Foundation, etc..
    
    "jquery" : "https://github.com/websanova/boilerplate/archive/master.zip",
    "foundation6" : "https://github.com/zurb/foundation-sites/archive/master.zip",
    "bootsrap" : "https://github.com/wanasit/boilerplate/archive/master.zip",
    "react" : "https://github.com/buckyroberts/React-Boilerplate/archive/master.zip",
    "angular2" : "https://github.com/buckyroberts/angular-2-template/archive/master.zip",
    
    # Backend frameworks like PHP 
    
    "codeigniter" : "https://github.com/bcit-ci/CodeIgniter/archive/3.1.3.zip", 
    "backbone" : "https://github.com/tbranyen/backbone-boilerplate/archive/master.zip",
    "vue2" : "https://github.com/petervmeijgaard/vue-2.0-boilerplate/archive/master.zip",
    "fuelphp" : "https://github.com/fuelphp/fuelphp/archive/master.zip"
    
}


'''
Python ZipAsset class to help download any of
the asset from the internet and then unzip it
to the local directory.
'''

class ZipAsset:
    
    def __init__(self, url, name='default-project-name'):
        self.url = url
        self.name = name
        print("[+] Project name set to: " + name)
        
    def download_zip(self):        
        data_service = self.url
        print("[+] Downloading zip file from " + data_service)
        content = urlopen(data_service)
        print("[+] Creating a zip file ")
        self.zipfile = ZipFile(BytesIO(content.read()))
        
    def unzip_file(self):
        dest = self.name
        print("[+] Unpacking asset... ")
        self.zipfile.extractall(dest)
        
    def documentation_url(self):
        offset = len(self.url) - 18
        doc_url = self.url[:offset]
        return doc_url
    
    def show_browser_documentaion(self):
        documentation = self.documentation_url()
        if os.name == "nt":
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s"
            webbrowser.get(chrome_path).open(documentation)
        
        
    def kick_start(self):
        self.download_zip()
        self.unzip_file()
        print("[+] Created succesfully at : " + self.name)    
        print("[+] Documentation at : " + self.documentation_url())
        time.sleep(1)
        self.show_browser_documentaion()
        
        
'''
The main programme starts here that includes parsing 
user input validation in terminal and execution - 18 character
'''

if len(sys.argv) == 4:
    
    if sys.argv[1] == '--start':
        
        project = sys.argv[2]
        name = sys.argv[3]
        
        if project in frameworks:
            spidy = ZipAsset(frameworks[project], name)            
            spidy.kick_start()              
            sys.exit(0)
            
        else:
            print("[-] No such key")
            print("Following are avialable ")
            
            for abbr, val in frameworks.items():
                print(abbr)
                
            sys.exit(0)
        
    else:
        
        print(sys.argv[1] + " not recognized. use only --start")
        sys.exit(-1)
        
        
else:
    
    print("USAGE:\n")
    print("python ./" + __file__ + " --start <project> <name> \n")
    print("Following options are avialable \n")
            
    for abbr, val in frameworks.items():
        print("->" + abbr)

    sys.exit(0)
        
    


        

        
        