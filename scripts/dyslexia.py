with open("algebre-II-notes.tex", "r") as f:
    lines = f.readlines()
    lines.insert(3, "\\usepackage{fontspec}\n")
    lines.insert(4, "\\setmainfont{OpenDyslexic}\n")
with open("algebre-II-notes-dyslexia.tex", "w") as f:
    f.writelines(lines)
