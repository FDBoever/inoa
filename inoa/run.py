import tempfile
import os
import inoa.utils as utils


#def get_temp_directory_path():
#    return tempfile.mkdtemp()


def run_prodigal(fasta_file_path, output_dir):
        out_genes_path = os.path.join(output_dir, 'prodigal.genes')
        out_proteins_path = os.path.join(output_dir, 'prodigal.proteins')
        log_file_path = os.path.join(output_dir, 'prodigal.log')

        cmd_line = ('prodigal -i "%s" -o "%s" -a "%s" -p meta >> "%s" 2>&1' % (fasta_file_path,
                                                                               out_genes_path,
                                                                               out_proteins_path,
                                                                               log_file_path))

        with open(log_file_path, "a") as myfile: myfile.write('CMD: ' + cmd_line + '\n')
        utils.run_command(cmd_line)

        return out_proteins_path

