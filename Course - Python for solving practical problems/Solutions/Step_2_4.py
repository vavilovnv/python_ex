# Текст задания: https://stepik.org/lesson/245299/step/2?unit=217525

# Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью, у него
# сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить зарплатную ведомость.
# Архив с расчётными листками доступен по ссылке https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip (вы
# можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).
# Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его
# зарплата. Сотрудники должны быть упорядочены по алфавиту.

import xlrd, wget, os, zipfile

zipname, zipfolder, payroll = 'rogaikopyta.zip', 'xlsxfiles', {}
if not os.access(zipname, os.F_OK):
    wget.download('https://stepik.org/media/attachments/lesson/245299/' + zipname)
if zipfolder not in os.listdir():
    zipfile = zipfile.ZipFile(zipname)
    zipfile.extractall(zipfolder)
    zipfile.close()
path = os.getcwd() + "\\" + zipfolder + "\\"
for file in os.listdir(zipfolder):
    wb = xlrd.open_workbook(path + file)
    sh = wb.sheet_by_name(wb.sheet_names()[0])
    payroll[sh.row_values(1)[1]] = int(sh.row_values(1)[3])
with open("out.txt", 'w', encoding='utf-8') as f:
    [f.write(i[0] + " " + str(i[1]) + "\n") for i in sorted(payroll.items(), key= lambda item: item[0])]




