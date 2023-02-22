import os

the_dir = './data/__groupfolders/1/'
all_txt_files = filter(lambda x: x.endswith('.pdp'), os.listdir(the_dir))
print(all_txt_files)
