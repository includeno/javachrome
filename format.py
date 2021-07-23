filename="config"

outfile = open(filename, "r", encoding='utf-8')
lines=outfile.readlines()
outfile.close()

outfile = open(filename, "w", encoding='utf-8')
for line in lines:
    outfile.write(line.replace(":","-"))
outfile.close()