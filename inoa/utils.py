# import os
# import sys
# import multiprocessing
import subprocess
import gzip
import shutil

def run_cmd(command_line):
    try:
        if subprocess.call(command_line, shell=True) < 0:
            print("command was terminated")
    except OSError as e:
        print("command was failed for the following reason: '%s' ('%s')")


def run_rscript(script, parsed_arguments):
    # cmd_line = (f'Rscript "{script}" "{input_dir}" "{output_dir}" >> "{log_file_path}" 2>&1')
    # cmd_line = (f'Rscript "{script}" "{input_dir}" "{output_dir}"')

    cmd_line = ('Rscript "%s" "%s"' % (script,
                                       parsed_arguments))

    run_cmd(cmd_line)


# FILE CHECKERS
# Check if file exists (return True or False)
def f_exists(path_to_file):
    if os.path.isfile(path_to_file) and os.access(path_to_file, os.R_OK):
        print("File exists and is readable")
        return True
    else:
        print("Either the input file is missing or not readable")
        return False


# Check whether a file is properly gunzipped
def is_gz_file(path_to_file):
    if f_exists(path_to_file):
        with gzip.open(path_to_file, 'r') as fh:
            try:
                fh.read(1)
                return True
            except gzip.BadGzipFile:
                print('path_to_file is not a valid gzip file by BadGzipFile')
                return False
    else:
        print('The file does not exist, so can not check whether it is gunzipped or not!')
        return False


# function to gunzip the content of an existing file
def gzip_file(path_to_file):
    if is_gz_file(path_to_file):
       print('File is already gunzipped')
    else:
        gz_path = "%s.gz" % path_to_file
        f = open(gz_path , 'wb')
        with open(path_to_file, 'rb') as f_in:
            with gzip.open(gz_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)



