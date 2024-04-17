# ==================================================================================================================================================================== #
# SITE CONECTIVITY REQUEST.
# IMPORT URLLIB.
# USE urllib.request TO GET THE DATA FROM THE URL
# WRITE A FUNCTION THAT TAKES A URL.
# RETURN A RESPONSE.
# ==================================================================================================================================================================== #

import urllib.request as urllib

def main(url):
    print("Checking connectivity ")
    
    response = urllib.urlopen(url)
    print("Conected to", url, "succesfully")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the URL of the site you want to check: ")

main(input_url)