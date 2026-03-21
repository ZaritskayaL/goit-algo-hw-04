import sys
from pathlib import Path

from colorama import init, Fore, Style


def list_directory_recursive(path: Path, indent: int = 0):
    '''Recursively prints the contents of a directory of any depth.'''
    prefix = ' ' * indent
    
    for item in path.iterdir():
        if item.is_dir():
            print(prefix + Fore.BLUE + '[DIR] ' + Style.RESET_ALL + ' ' + item.name)
            list_directory_recursive(item, indent + 4)
        else: 
            print(prefix + Fore.BLUE + '[DIR]' + Style.RESET_ALL + ' ' + item.name)
            
            
def main():
    init(autoreset=True)
    
    if len(sys.argv) < 2:
       print(Fore.RED + 'Error: no directory path provided')
       print(Fore.YELLOW + 'Example usage:')
       print(Fore.CYAN + r'  python colorama_module.py C:\My_repo\goit_algo_hw_03')
       return 
   
    dir_path_str = sys.argv[1]
    dir_path = Path(dir_path_str)
    
    if not dir_path.exists():
        print(Fore.RED + f'Path does not exist: {dir_path}')
        return
    
    if not dir_path.is_dir():
        print(Fore.RED + f'Not the directory: {dir_path}')
        return 
    
    print(Fore.GREEN + f'Directory contents: {dir_path}')
    print(Style.DIM + '-' * 50)
    
    list_directory_recursive(dir_path)
    

if __name__ == '__main__':
    main()