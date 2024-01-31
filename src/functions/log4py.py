#/bin/bash python3
import os

log_file_path = "./../logs/grandet.log"


def print_log(info: str):
    
    log_str = f"log: {info}"
    print(log_str)
    if os.path.exists(log_file_path):
        with open(log_file_path, 'a') as f:
            f.write(f"{log_str}\n")
    else:
        pass
    