import glob
import os

#os.chdir("D:\\WeChatFiles\\wxuser\\FileStorage\\Image\\2021-10")

files = glob.glob('**/*.dat', recursive=True)


for f in files:
    print(f'removing {f}')
    os.remove(f)
