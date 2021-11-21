def Run_Help():
    help_command = """
Usage: hashcracker.py [--format] [file with hash] [wordlist]

Example: ./hashcracker.py --format=md5 hash.txt rockyou.txt
        ./hashcracker.py --format-list

optional arguments:
-h, --help  show this help message and exit
--format=NAME     specify type of hash algorithm
--format-list         list available formats
    """
    print(help_command)

def List_Formats():
    format_list = """
Currently available formats:

md5
sha1
sha256
"""
    print(format_list)