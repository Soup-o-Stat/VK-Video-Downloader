import yt_dlp
import termcolor

logo=r'''
 __     __  __              __     __  __        __                            _______                                     __                            __                     
|  \   |  \|  \            |  \   |  \|  \      |  \                          |       \                                   |  \                          |  \                    
| $$   | $$| $$   __       | $$   | $$ \$$  ____| $$  ______    ______        | $$$$$$$\  ______   __   __   __  _______  | $$  ______    ______    ____| $$  ______    ______  
| $$   | $$| $$  /  \      | $$   | $$|  \ /      $$ /      \  /      \       | $$  | $$ /      \ |  \ |  \ |  \|       \ | $$ /      \  |      \  /      $$ /      \  /      \ 
 \$$\ /  $$| $$_/  $$       \$$\ /  $$| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\      | $$  | $$|  $$$$$$\| $$ | $$ | $$| $$$$$$$\| $$|  $$$$$$\  \$$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$\
  \$$\  $$ | $$   $$         \$$\  $$ | $$| $$  | $$| $$    $$| $$  | $$      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$  | $$ /      $$| $$  | $$| $$    $$| $$   \$$
   \$$ $$  | $$$$$$\          \$$ $$  | $$| $$__| $$| $$$$$$$$| $$__/ $$      | $$__/ $$| $$__/ $$| $$_/ $$_/ $$| $$  | $$| $$| $$__/ $$|  $$$$$$$| $$__| $$| $$$$$$$$| $$      
    \$$$   | $$  \$$\          \$$$   | $$ \$$    $$ \$$     \ \$$    $$      | $$    $$ \$$    $$ \$$   $$   $$| $$  | $$| $$ \$$    $$ \$$    $$ \$$    $$ \$$     \| $$      
     \$     \$$   \$$           \$     \$$  \$$$$$$$  \$$$$$$$  \$$$$$$        \$$$$$$$   \$$$$$$   \$$$$$\$$$$  \$$   \$$ \$$  \$$$$$$   \$$$$$$$  \$$$$$$$  \$$$$$$$ \$$      
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
'''

def main():
    try:
        link = input("Enter video or clip URL: ").strip()
        output_path = get_output_path()
        ydl_opts = {
            'format': "mp4",
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'postprocessors': []
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        termcolor.cprint("Done!", "green")
        print()
    except Exception as e:
        print(f"Error: {e}")

def get_output_path():
    path = input("Enter path to output file (or leave empty for current folder): ").strip()
    return path if path else '.'

if __name__ == '__main__':
    termcolor.cprint(logo, "blue")
    while True:
        main()
