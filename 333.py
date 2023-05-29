with open("output.txt", "w") as f, open('input2.txt', 'r') as f_in:  # открыть файл на запись заранее
    f.write("")  # записать пустую строку, чтобы очистить файл
    lines = f_in.readlines()
    n = 56  # задайте количество строк, которые нужно записать
    i = 0
    with open('output.txt', 'w') as f_out_temp:
        for line_temp in lines:
            if i >= n:
                break  # достигли нужного количества строк
            f_out_temp.write(line_temp)
            i += 1

with open('input2.txt', 'r') as f_in, open('output2.txt', 'w') as f_out:
    # читаем исходный файл и разделяем его на строки
    lines = f_in.readlines()

    for line in lines:
    # остальные строки обрабатываем и записываем в файл output2.txt
        new_line = line.replace("DB", "DBD").replace("DW", "DBW").replace("DD", "DBD")
        if new_line.find("DBW")>-1 and new_line.rfind("in  Word D")>-1:
            nam=new_line[new_line.rfind("in  Word D")-2]
            nam=int(nam)
            if nam >= 8 and nam <= 15:
                p2=new_line.find("DBW")
                p=new_line[new_line.find("DBW")-7:new_line.find("DBW")-1]
                num=int(p[3:6])*2
                p2=p.replace(p[3:6],str(num))
                new_line=new_line.replace(p,p2)
            elif nam >= 0 and nam <= 8:
                p2=new_line.find("DBW")
                p=new_line[new_line.find("DBW")-7:new_line.find("DBW")-1]
                num=int(p[3:6])*2+1
                p2=p.replace(p[3:6],str(num))
                new_line=new_line.replace(p,p2)

            # заменяем оставшиеся запятые на точки
        new_line = new_line.replace(",", ".")

            # записываем обработанную строку в новый файл
        f_out.write(new_line)
