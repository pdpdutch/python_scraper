import download as D
import asyncio, os, shutil, click
from consolemenu import *
from consolemenu.items import *

# # Create the menu
# menu = ConsoleMenu("Do you want to delete the old scraped folder?", "(1) Yes or (0) No")

# # Create some items

# delete = False
# # MenuItem is the base class for all items, it doesn't do anything when selected

def setDelete(i):
    global delete
    if i == 0:
        delete = True
    else:
        delete = False

# # A FunctionItem runs a Python function when selected
# function_item1 = MenuItem("Delete the old scraped folder", should_exit=True)
# function_item2 = MenuItem("Don't delete the old scraped folder", should_exit=True)



# # Once we're done creating them, we just add the items to the menu
# menu.append_item(function_item1)
# menu.append_item(function_item2)

# # Finally, we call show to show the menu and allow the user to interact
# menu.show()

# option = menu.selected_option

# setDelete(option)
setDelete(1)




def deleteFiles():
    try:
        main_path = os.getcwd() + '\scraped'
        shutil.rmtree(main_path)
        print(f"{main_path} was removed")
    except:
        print("There was nothing to delete")
        
    

if delete:
    deleteFiles()
else:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(D.main())
    loop.close()


print("Done")


