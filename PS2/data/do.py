import os

for f in ['NIPS_1987-2015.csv', 'hw.tex', 'mars.jpg', 'mnist_train.csv', 'recordings.tar']:

    print('Encoding {} for file {}'.format('bzip2', f))
    os.system('time bzip2 {}'.format(f))
    print('Decoding {} for file {}'.format('bunzip2', f))
    os.system('time bunzip2 {}'.format(f))

    print('Encoding {} for file {}'.format('bzip2 -s', f))
    os.system('time bzip2 -s {}'.format(f))
    print('Decoding {} for file {}'.format('bunzip2', f))
    os.system('time bunzip2 {}'.format(f))

    print('Encoding {} for file {}'.format('gzip', f))
    os.system('time gzip {}'.format(f))
    print('Decoding {} for file {}'.format('gzip', f))
    os.system('time gunzip {}'.format(f))

    print('Encoding {} for file {}'.format('gzip -l', f))
    os.system('time gzip -l {}'.format(f))
    print('Decoding {} for file {}'.format('gunzip', f))
    os.system('time gunzip {}'.format(f))

    print('Encoding {} for file {}'.format('p7zip', f))
    os.system('time p7zip {}'.format(f))
    print('Decoding {} for file {}'.format('p7zip -d', f))
    os.system('time p7zip -d {}.7z'.format(f))

