import rawpy
import imageio
from os import walk


path = 'photos/'
f = []
counter = 0
for (dirpath, dirnames, filenames) in walk(path):
    for filename in filenames:
        counter += 1
        if '.NEF' in filename:
            with rawpy.imread(path + filename) as raw:
                rgb = raw.postprocess()
            new_filename = filename[:len(filename) - 4] + '.jpg'
            imageio.imsave(path + new_filename, rgb)
            f.append(new_filename)
            print(str(100 * counter / len(filenames)) + '% Converting... ' + new_filename)

print(path + ' >>> ' + str(len(f)) + ' Photos exported as jpg:' + str(f))