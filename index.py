import glob

with open('index.md', 'a') as out:
    for path in glob.glob('./Labs/AZ-204_*_lab.md'):
        with open(path, 'r', encoding="utf8") as file:
            file.readline()
            file.readline()
            lab = file.readline().split(':')[2][1:-2]
            module = file.readline().split(':')
            out.write("| " + module[1][2:] + " | ")
            out.write(module[2][1:-2] + " | ")
            out.write("[{}]({}) |\n".format(lab, path.replace('\\', '/')))
