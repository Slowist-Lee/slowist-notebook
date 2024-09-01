def read_file(input_file,start_line,end_line):
    with open(input_file,'r',encoding='utf-16') as input:
        alllines=input.readlines()
        lines=alllines[start_line:end_line]
    print("readed {} to {}".format(start_line,end_line))
    return lines
def write_file(lines,output_file):
    with open(output_file,'w',encoding='utf-16') as output:
        output.writelines(lines)
    print("written")


start_line=627
end_line=711
lines=read_file('D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/data.txt',start_line,end_line)
k=0
pre_line='http://172.16.80.11/index.php?act=news&id=1%20and%20ascii(substr(((select%20concat_ws(char(94),%20flag)%20%20from%20db_flag.tb_flag%20%20limit%200,1)),%201,%201))>100'
flag=''
for line in lines:
    if int(line[154])==int(k)+1:
        # print(pre_line)
        flag+=chr(int(pre_line[163:]))
        # print(pre_line[163:],chr(int(pre_line[163:])))
    k=line[154]
    pre_line=line
    # print(k)
flag+=chr(int(pre_line[163:]))
start_line=711
end_line=972
lines=read_file('D:/MyRepository/slowist-notebook/docs/Coding/CTF/misc-lec3/data.txt',start_line,end_line)
for line in lines:
    if int(line[154:156])==int(k)+1:
        # print(pre_line)
        flag+=chr(int(pre_line[164:]))
        # print(pre_line[163:],chr(int(pre_line[163:])))
    k=line[154:156]
    pre_line=line
    # print(k)
flag+=chr(int(pre_line[164:]))
print(flag)

