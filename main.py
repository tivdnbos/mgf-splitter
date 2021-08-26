mgf_path = "C:\\Users\\tvdbo\\Documents\\Projecten\\ms2rescore-idrates\\mgf\\151222_NJ_Felipe_Y1a.mgf"

with open(mgf_path, "r") as mgf_in:
    mgf_counter = 0

    f_out = open(mgf_path.replace(".mgf", "_{}.mgf".format(str(mgf_counter).zfill(2))), "w")
    spectrum_count = 0
    for line in mgf_in:
        if "BEGIN IONS" in line:
            spectrum_count += 1

            if spectrum_count == 50001:
                f_out.close()
                spectrum_count = 0
                mgf_counter += 1
                f_out = open(mgf_path.replace(".mgf", "_{}.mgf".format(str(mgf_counter).zfill(2))), "w")
                print(spectrum_count)

        print(line.rstrip(), file=f_out)

f_out.close()
print(spectrum_count)
