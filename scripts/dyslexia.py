with open("algebre-II-notes.tex", "r") as f:
    lines = f.readlines()
    lines.insert(3, "\\usepackage{fontspec}\n")
    lines.insert(4, "\\setmainfont{Open Dyslexic}\n")
with open("algebre-II-notes-dyslexic.tex", "w") as f:
    f.writelines(lines)
