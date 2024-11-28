# CMIP6数据处理笔记

## aria2批量下载CMIP6数据

1. 从CMIP6官方wget.sh文件中抽取下载的所有**url**

   **python脚本处理多个wget.sh文件示例：**

   `import re`

   

   `\# 提取链接的函数`

   `def extract_links_from_file(file_path):`

     `with open(file_path, 'r') as file:`

   ​    `content = file.read()`

   ​    `links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\$\$,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)`

   ​    `return links`

   

   `\# 文件名列表`

   `file_names = ['wget-20240403075821-1.sh', 'wget-20240403075932-2.sh', 'wget-20240403075950-3.sh', 'wget-20240403080017-4.sh', 'wget-20240403080038-5.sh', 'wget-20240403080100-6.sh', 'wget-20240403080116-7.sh', 'wget-20240403080134-8.sh', 'wget-20240403080149-9.sh', 'wget-20240403080204-10.sh', 'wget-20240403080218-11.sh', 'wget-20240403080230-12.sh', 'wget-20240403080243-13.sh']`

   

   `all_links = []`

   `\# 提取每个文件中的链接`

   `for file_name in file_names:`

     `links = extract_links_from_file(file_name)`

     `all_links.extend(links)`

   

   `\# 保存链接到另一个文档中`

   `with open(**'urls.txt**', 'w') as output_file:`

     `for link in all_links:`

   ​    `link = link.replace("'", "")`

   ​    `output_file.write(link + '\n')`

   

2. 去掉重复的行：sort file.txt | uniq > newfile.txt

3. 安装aria2 **(服务器已安装)**：sudo yum install aria2

4. 下载指令：aria2c -i **urls.txt** -j 16 -d **/file/path**

5. 切后台下载：**nohup** aria2c -i **urls.txt** -j 16 -d /file/path **&**

6. 断点续传：aria2c **-c** -i urls.txt -j 16 -d /file/path

7. 下载到当前目录：aria2c -i urls.txt -j 16 -d **./**

8. 保存下载过程log：aria2c -i urls.txt -j 16 -d /file/path **> out**

9. 全家福指令：**nohup aria2c -c -i urls.txt -j 16 -d ./ > out &**

10. 查询下载记录：tail **out**



## 遍历所下载文件

### ncl脚本：

`;批量查询损坏文件`



`setfileoption("nc","Format","NetCDF4Classic")`

`setfileoption("nc", "Format", "NetCDF4")`

`setfileoption("nc", "Format", "LargeFile")`



`;文件夹路径`

`filepath = "/data/nkang/user-nkang/019-CMIP6/04-未来PM25/"`



`;读取所有nc格式文件`

`fils = systemfunc("ls "+filepath+"*nc")`



`;遍历`

`do i = 0,dimsizes(fils)-1,1`

  `f = addfile(fils(i),"r")`

  `print((/i/))`

  `print((/fils(i)/))`

  `;是否读取成功，如文件损坏则输出no`

  `if (ismissing(f))then`

​    `print("NO")`

  `else`

  `;如文件无误可以存放在其他路径`

​    `print("YES")`

​    `system("ln -sf "+fils(i)+" .")`

  `end if`

`end do`



执行：ncl *filename*.ncl



