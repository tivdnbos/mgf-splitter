import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("mgf_file", help="Path to single mgf file")
    parser.add_argument("size", help="Max number of spectra per mgf")
    return parser.parse_args()


def main():

    args = parse_args()
    mgf_path = args.mgf_file
    max_size = int(args.size)

    with open(mgf_path, "r") as mgf_in:
        mgf_counter = 0
        f_out = open(mgf_path.replace(".mgf", "_{}.mgf".format(str(mgf_counter).zfill(2))), "w")
        spectrum_count = 0
        for line in mgf_in:
            if "BEGIN IONS" in line:
                spectrum_count += 1
                if spectrum_count == max_size + 1:
                    f_out.close()
                    spectrum_count = 1
                    mgf_counter += 1
                    f_out = open(mgf_path.replace(".mgf", "_{}.mgf".format(str(mgf_counter).zfill(2))), "w")

            print(line.rstrip(), file=f_out)

    f_out.close()


main()
