import input
import time
import model
import os
import sys

def main():
    denoFrame = 0
    while True:
        if input.quit():
            break
        os.system("cls" if sys.platform == "win32" else "clear")
        deno = model.build_deno(False, denoFrame)
        for line in deno:
            print(line)
        denoFrame += 1
        time.sleep(0.1)

if __name__ == "__main__":
    main()