# gen_txt

DNS文件存储解决方案    
~~不会真的有人用TXT存文件吧？ 不会吧不会吧不会吧~~


### 上传文件

```bash
$ python tool.py
file slice to b64 txt records
    python tool.py add <prefix> <file> [key]

delete records with prefix and key
    python tool.py delete <prefix>
    
$ python tool.py add test GetPic.png test
[*] generate base64 payloads
[*] 45 records will be create
[*] start to create TXT records
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 45/45 [00:16<00:00,  2.80it/s] 
[!] done. file url: 098f6bcd4621d373cade4e832627b4f6.test.b477ery.cc
```

### 下载文件

```bash
$ python downloader.py
download file uploaded by gen_txt
    python downloader.py <url> [out_file_name]
example:
    python downloader.py 4464014eislkfjxsb5642451fea512a4.test.b477ery.cc
    
$ python downloader.py 098f6bcd4621d373cade4e832627b4f6.test.b477ery.cc getpic.png
[*] download 098f6bcd4621d373cade4e832627b4f6.test.b477ery.cc
[*] download f5fa42d1d705a49c30297917812c534f.test.b477ery.cc
[*] download 2ee72896ac849eca54c2249f5897056d.test.b477ery.cc
[*] download 3868c36e5965fb8a2fc849633a99edeb.test.b477ery.cc
.......
[*] download 9d9d9fc17220b7317f92274ba6e53f99.test.b477ery.cc
[*] out file to getpic.png
```

### 删除文件

```bash
$ python tool.py delete test
[*] delete 098f6bcd4621d373cade4e832627b4f6.test
[*] delete f5fa42d1d705a49c30297917812c534f.test
[*] delete 2ee72896ac849eca54c2249f5897056d.test
[*] delete 3868c36e5965fb8a2fc849633a99edeb.test
.......
[*] delete 16510c5bfcf66202789fe10b19e98143.test
[!] done.
```
