import itertools
import glob
import os

def take(n, iterable):
    return list(itertools.islice(iterable, n))

HEADERS = {
        'jpg': [ 0xFF, 0xD8 ],
        'png': [ 0x89, 0x50 ],
        'gif': [ 0x47, 0x49 ],
        'wxgf': [ 0x77, 0x78 ],
    }


def detect_key(original):
    for ext, header in HEADERS.items():
        if original[0] == original[1]:
            return (f'{hex(original[0])}.dec', original[0]);
        first_key = header[0] ^ original[0]
        second_key = header[1] ^ original[1]
        if first_key == second_key:
            return (ext, first_key)
    raise Exception(f'Unknown extension. File digest:{list(original[0:6])}')


def decode_file(original):
    try:
        with open(original, 'rb') as dat:
            first_line = take(1, dat)[0];
            (ext, key) = detect_key(first_line)
            print(f'File: {original}, Found match ext: {ext}, key: {hex(key)}, File digest:{list(first_line[0:6])}')
            with open(f'{original}.{ext}', 'wb') as img:
                img.write(bytes(b ^ key for b in first_line))
                for buf in dat:
                    decoded = bytes(b ^ key for b in buf)
                    img.write(decoded)
    except Exception as e:
        print(f'file name: {original}, ex {e}')

#os.chdir("D:\\WeChatFiles\\wxuser\\FileStorage\\Image\\2021-10")

for f in glob.glob('**/*.dat', recursive=True):
    decode_file(f)
