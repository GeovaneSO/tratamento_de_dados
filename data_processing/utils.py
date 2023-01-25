import ipdb
import os


def handle_uploaded_file(file):
    # for key, value in file.items():
        # print(str(value))
        # a = open(str(file['file']), 'r').readlines()
    for line in file["file"].readlines():

        print(line.decode("utf-8"))
        # ipdb.set_trace()
