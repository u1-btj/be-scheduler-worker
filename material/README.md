# Data Processing and Integration

## Prequisite
```
1. Python: Loop, data type, file manipulation, class-method
2. Database sql
3. Docker installation
```

## Definisi
Proses menarik data dari sumber menjadi informasi pada penyimpanan

## ETL (Extract Transform Load)

- Extract: Menarik Data dari sumber
- Transform: Mengubah Data mentah sehingga sesuai dengan kebutuhan
- Load: Menempatkan data pada penyimpanan, sehingga bisa lgsg diakses dalam proses internal server

### Extract
3 Hal utama yg perlu diperhatikan:
1. 
2. Akses
    - butuh izin akses seperti vpn?
    - tipe akses: api, ssh, sftp, database, file

Contoh:

```python 
# API
import requests
url = "https://api.publicapis.org/entries"
res_data = requests.get(url, params={},data={}).json()

# database
import MySQLdb
conn = MySQLdb.connect(
    host='',
    user='',
    passwd='',
    db='',
)
cursor = conn.cursor()
stmt = """
select * from tabel
"""
cursor.execute()
res_data = cursor.fetchall()

# ssh
import pysftp
hostname = ''
user_name = ''
pwd = ''
filename = ''
with pysftp.Connection(hostname, username=user_name, password=pwd) as sftp:
    sftp.get(filename)

# file
import csv
with open(filename) as file:
    res_data = csv.reader(file, delimiter=',')

```

### Transform
Jenis-jenis transformasi data 
- Pembersihan data: data tidak terpakai, dan duplikasi data
- Penyesuaian kebutuhan data: penggabungan, pemisahan, dll
- Pengubahan tipe data
Contoh :

```python
def reduce(data): # menghilang kan 2 jenis data, co: IPA dan IPS
    if type(data) is dict:
        if 'IPA' in data:
            del data['IPA']
        if 'IPS' in data:
            del data['IPS']
        res = data 
    elif type(data) is list:
        # uji peserta
        res = data 
    else:
        res = data 
    return res

def combine(data1, data2): # menggabung kan 2 data yang bersifat dict
    if (type(data1) is dict) and (type(data2) is dict):
        res = {}
        for key in data1:
            res[key] = data1[key]
        for key in data2:
            if key not in res:
                res[key] = data2[key]
    else:
        None
    
    return res

def convert(data_json): # ubah dari json of list, jadi list of json: Test!
    if not (type(data_json) is dict):
        return None

    data_list = []
    key_0 = list(data_json)[0]
    len_data = len(data_json[key_0]) # asumsi seluruh data panjangnya sama
    for i in range(len_data):
        res_elm = {}
        for key in data_json:
            res_elm[key] = data_json[key][i]
        data_list.append(res_elm)

    return data_list
```

### Load
Hal yang perlu diperhatikan:
- Model penyimpanan data: Umumnya adalah database sql, terdapat hadoop, file (csv, excel, json, xml)
- Perlu nya perencanaan pada struktur penyimpanan: ERD, setup primary dan foreign key.


### Scheduler - Task - Worker
1. Scheduler: Penjadwalan jalan nya suatu program (job).
Hal yang perlu diperhatikan:
- Cron
- Interval
- External Trigger

2. Task: istilah untuk program yang ditujukan untuk mencapai suatu tujuan. Bisa berupa Method atau Fungsi

3. Worker: Program yang bertugas menampung dan menjalankan task

    Contoh scheduler-task:
    ```python
    from apscheduler.schedulers.background import BlockingScheduler

    # Creates a default Background Scheduler
    sched = BlockingScheduler()

    def prompt(): # worker task
        print("Executing Task...")


    sched.add_job(prompt,'interval', seconds=5) # scheduler jalan setiap 5 detik (interval)
    sched.start()
    ```

    -   Skema Worker
    
    Run Broker: 
    Menggunakan RabbitMQ

    run in docker: ```docker run -d -p 5672:5672 rabbitmq```

    Contoh Worker:
    ```python
    from celery import Celery

    app = Celery('tasks', broker='pyamqp://guest@localhost//')

    @app.task
    def add(x, y):
        print('Berhasil masuk ke worker')
        return x + y
    ```

    Run in terminal
    ```
    celery -A tasks worker --loglevel=INFO
    ```

    Panggil task pada worker
    ```python 
    from tasks import add
    add.delay(4, 4)
    ```