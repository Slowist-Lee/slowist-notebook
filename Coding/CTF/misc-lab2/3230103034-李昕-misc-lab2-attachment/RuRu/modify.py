def modifyfile(file_path):
    try:
        # 读取文件内容
        with open(file_path, 'rb') as f:
            content = f.read()
        hex_content=list(content)
        for i in range(len(hex_content)):
            hex_content[i]=hex(hex_content[i])[2:]
        print(hex_content)
        i=0
        while i<len(hex_content)-3:
            if hex_content[i]=='50' and hex_content[i+1]=='4b' and hex_content[i+2]=='3' and hex_content[i+3]=='4':
                # print(i,hex_content[i:i+7],hex_content[i+6])
                hex_content[i+6]='0'
            elif hex_content[i]=='50' and hex_content[i+1]=='4b' and hex_content[i+2]=='1' and hex_content[i+3]=='2':
                # print(i,hex_content[i:i+7],hex_content[i+6])
                hex_content[i+8]='0'
            i+=1      
        for i in range(len(hex_content)):
            hex_content[i]=int(hex_content[i],16)
        with open('D:/MyRepository/slowist-notebook/docs/Coding/new.zip','wb') as f:
            f.write(bytes(hex_content))
    except Exception as e:
        print(f"An error occurred: {e}")

# 调用函数修改文件
file_path = 'D:/MyRepository/slowist-notebook/docs/Coding/999_0061c023.zip'
modifyfile(file_path)
