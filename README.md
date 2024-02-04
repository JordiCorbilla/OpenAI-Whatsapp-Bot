# OpenAI-Whatsapp-Bot
OpenAI-Whatsapp-Bot

## Setup environment:

- Windows 11 PRO (Mini Server x64 Intel Celeron 12 Gb)
- Python 3.12.1
- Sql Server Express v15
- Twilio Account
- Ngrok
- OpenAPI Key
- Whatsapp (local phone)

## 1) Setting up your Twilio Account

- Create a free account with Twilio here -> https://www.twilio.com/en-us
- Setup the WhatsApp messaging using the Twilio Sandbox, you'll be given a `+1` phone number to interact with:

![image](https://github.com/JordiCorbilla/OpenAI-Whatsapp-Bot/assets/7347994/56613b5e-f5fb-4e8d-9f5c-1fc57e89ea15)

## 2) Install Python and create your development environment

I've done this using the latest python available **3.12.1** (https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe) at the time of this writing. 

- Clone this repo: https://github.com/JordiCorbilla/OpenAI-Whatsapp-Bot.git

- Create the dev environment:

```bash
C:\repo\OpenAI-Whatsapp-Bot> python -m venv venv;
```

- Enable the dev environment:
```bash
C:\repo\OpenAI-Whatsapp-Bot\venv\Scripts>activate.bat
```

- Upgrade pip

```bash
(venv) C:\repo\OpenAI-Whatsapp-Bot\venv\Scripts>python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\repo\openai-whatsapp-bot\venv\lib\site-packages (23.2.1)
Collecting pip
  Obtaining dependency information for pip from https://files.pythonhosted.org/packages/15/aa/3f4c7bcee2057a76562a5b33ecbd199be08cdb4443a02e26bd2c3cf6fc39/pip-23.3.2-py3-none-any.whl.metadata
  Using cached pip-23.3.2-py3-none-any.whl.metadata (3.5 kB)
Using cached pip-23.3.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.2.1
    Uninstalling pip-23.2.1:
      Successfully uninstalled pip-23.2.1
Successfully installed pip-23.3.2
```

- Install Microsoft C++ Build Tools
![image](https://github.com/JordiCorbilla/OpenAI-Whatsapp-Bot/assets/7347994/c6487430-625a-44f3-b614-8acecffdb378)

- Install the requirements file using `pip install -r requirements.txt`:

```bash
aiohttp==3.9.1
aiohttp-retry==2.8.3
aiosignal==1.3.1
annotated-types==0.6.0
anyio==3.7.1
attrs==23.2.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
distro==1.9.0
fastapi==0.109.0
frozenlist==1.4.1
greenlet==3.0.3
h11==0.14.0
httpcore==1.0.2
httpx==0.26.0
idna==3.6
iniconfig==2.0.0
multidict==6.0.4
openai==0.28.0
packaging==23.2
pluggy==1.3.0
psycopg2-binary==2.9.9
pydantic==2.5.3
pydantic_core==2.14.6
PyJWT==2.8.0
pyngrok==7.0.5
pyodbc==5.0.1
pytest==7.4.4
python-decouple==3.8
python-multipart==0.0.6
PyYAML==6.0.1
requests==2.31.0
sniffio==1.3.0
SQLAlchemy==2.0.25
starlette==0.35.1
tqdm==4.66.1
twilio==8.11.1
typing_extensions==4.9.0
urllib3==2.1.0
uvicorn==0.26.0
yarl==1.9.4
```

```bash
(venv) C:\repo\OpenAI-Whatsapp-Bot>pip install -r requirements.txt
Collecting fastapi (from -r requirements.txt (line 1))
  Using cached fastapi-0.109.0-py3-none-any.whl.metadata (24 kB)
Collecting uvicorn (from -r requirements.txt (line 2))
  Using cached uvicorn-0.26.0-py3-none-any.whl.metadata (6.4 kB)
Collecting twilio (from -r requirements.txt (line 3))
  Using cached twilio-8.11.1-py2.py3-none-any.whl.metadata (12 kB)
Collecting openai (from -r requirements.txt (line 4))
  Using cached openai-1.9.0-py3-none-any.whl.metadata (18 kB)
Collecting python-decouple (from -r requirements.txt (line 5))
  Using cached python_decouple-3.8-py3-none-any.whl (9.9 kB)
Collecting sqlalchemy (from -r requirements.txt (line 6))
  Using cached SQLAlchemy-2.0.25-cp312-cp312-win_amd64.whl.metadata (9.8 kB)
Collecting psycopg2-binary (from -r requirements.txt (line 7))
  Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl.metadata (4.6 kB)
Collecting python-multipart (from -r requirements.txt (line 8))
  Using cached python_multipart-0.0.6-py3-none-any.whl (45 kB)
Collecting pyngrok (from -r requirements.txt (line 9))
  Using cached pyngrok-7.0.5-py3-none-any.whl.metadata (6.2 kB)
Collecting pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 (from fastapi->-r requirements.txt (line 1))
  Using cached pydantic-2.5.3-py3-none-any.whl.metadata (65 kB)
Collecting starlette<0.36.0,>=0.35.0 (from fastapi->-r requirements.txt (line 1))
  Using cached starlette-0.35.1-py3-none-any.whl.metadata (5.8 kB)
Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
  Using cached typing_extensions-4.9.0-py3-none-any.whl.metadata (3.0 kB)
Collecting click>=7.0 (from uvicorn->-r requirements.txt (line 2))
  Using cached click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting h11>=0.8 (from uvicorn->-r requirements.txt (line 2))
  Using cached h11-0.14.0-py3-none-any.whl (58 kB)
Collecting requests>=2.0.0 (from twilio->-r requirements.txt (line 3))
  Using cached requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
Collecting PyJWT<3.0.0,>=2.0.0 (from twilio->-r requirements.txt (line 3))
  Using cached PyJWT-2.8.0-py3-none-any.whl.metadata (4.2 kB)
Collecting aiohttp>=3.8.4 (from twilio->-r requirements.txt (line 3))
  Using cached aiohttp-3.9.1-cp312-cp312-win_amd64.whl.metadata (7.6 kB)
Collecting aiohttp-retry>=2.8.3 (from twilio->-r requirements.txt (line 3))
  Using cached aiohttp_retry-2.8.3-py3-none-any.whl (9.8 kB)
Collecting anyio<5,>=3.5.0 (from openai->-r requirements.txt (line 4))
  Using cached anyio-4.2.0-py3-none-any.whl.metadata (4.6 kB)
Collecting distro<2,>=1.7.0 (from openai->-r requirements.txt (line 4))
  Using cached distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting httpx<1,>=0.23.0 (from openai->-r requirements.txt (line 4))
  Using cached httpx-0.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting sniffio (from openai->-r requirements.txt (line 4))
  Using cached sniffio-1.3.0-py3-none-any.whl (10 kB)
Collecting tqdm>4 (from openai->-r requirements.txt (line 4))
  Using cached tqdm-4.66.1-py3-none-any.whl.metadata (57 kB)
Collecting greenlet!=0.4.17 (from sqlalchemy->-r requirements.txt (line 6))
  Using cached greenlet-3.0.3-cp312-cp312-win_amd64.whl.metadata (3.9 kB)
Collecting PyYAML (from pyngrok->-r requirements.txt (line 9))
  Using cached PyYAML-6.0.1-cp312-cp312-win_amd64.whl.metadata (2.1 kB)
Collecting attrs>=17.3.0 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 3))
  Using cached attrs-23.2.0-py3-none-any.whl.metadata (9.5 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 3))
  Using cached multidict-6.0.4.tar.gz (51 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Collecting yarl<2.0,>=1.0 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 3))
  Using cached yarl-1.9.4-cp312-cp312-win_amd64.whl.metadata (32 kB)
Collecting frozenlist>=1.1.1 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 3))
  Using cached frozenlist-1.4.1-cp312-cp312-win_amd64.whl.metadata (12 kB)
Collecting aiosignal>=1.1.2 (from aiohttp>=3.8.4->twilio->-r requirements.txt (line 3))
  Using cached aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Collecting idna>=2.8 (from anyio<5,>=3.5.0->openai->-r requirements.txt (line 4))
  Using cached idna-3.6-py3-none-any.whl.metadata (9.9 kB)
Collecting colorama (from click>=7.0->uvicorn->-r requirements.txt (line 2))
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting certifi (from httpx<1,>=0.23.0->openai->-r requirements.txt (line 4))
  Using cached certifi-2023.11.17-py3-none-any.whl.metadata (2.2 kB)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->openai->-r requirements.txt (line 4))
  Using cached httpcore-1.0.2-py3-none-any.whl.metadata (20 kB)
Collecting annotated-types>=0.4.0 (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi->-r requirements.txt (line 1))
  Using cached annotated_types-0.6.0-py3-none-any.whl.metadata (12 kB)
Collecting pydantic-core==2.14.6 (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi->-r requirements.txt (line 1))
  Using cached pydantic_core-2.14.6-cp312-none-win_amd64.whl.metadata (6.6 kB)
Collecting charset-normalizer<4,>=2 (from requests>=2.0.0->twilio->-r requirements.txt (line 3))
  Using cached charset_normalizer-3.3.2-cp312-cp312-win_amd64.whl.metadata (34 kB)
Collecting urllib3<3,>=1.21.1 (from requests>=2.0.0->twilio->-r requirements.txt (line 3))
  Using cached urllib3-2.1.0-py3-none-any.whl.metadata (6.4 kB)
Using cached fastapi-0.109.0-py3-none-any.whl (92 kB)
Using cached uvicorn-0.26.0-py3-none-any.whl (60 kB)
Using cached twilio-8.11.1-py2.py3-none-any.whl (1.7 MB)
Using cached openai-1.9.0-py3-none-any.whl (223 kB)
Using cached SQLAlchemy-2.0.25-cp312-cp312-win_amd64.whl (2.1 MB)
Using cached psycopg2_binary-2.9.9-cp312-cp312-win_amd64.whl (1.2 MB)
Using cached pyngrok-7.0.5-py3-none-any.whl (21 kB)
Using cached aiohttp-3.9.1-cp312-cp312-win_amd64.whl (362 kB)
Using cached anyio-4.2.0-py3-none-any.whl (85 kB)
Using cached click-8.1.7-py3-none-any.whl (97 kB)
Using cached distro-1.9.0-py3-none-any.whl (20 kB)
Using cached greenlet-3.0.3-cp312-cp312-win_amd64.whl (293 kB)
Using cached httpx-0.26.0-py3-none-any.whl (75 kB)
Using cached httpcore-1.0.2-py3-none-any.whl (76 kB)
Using cached pydantic-2.5.3-py3-none-any.whl (381 kB)
Using cached pydantic_core-2.14.6-cp312-none-win_amd64.whl (1.9 MB)
Using cached PyJWT-2.8.0-py3-none-any.whl (22 kB)
Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Using cached starlette-0.35.1-py3-none-any.whl (71 kB)
Using cached tqdm-4.66.1-py3-none-any.whl (78 kB)
Using cached typing_extensions-4.9.0-py3-none-any.whl (32 kB)
Using cached PyYAML-6.0.1-cp312-cp312-win_amd64.whl (138 kB)
Using cached annotated_types-0.6.0-py3-none-any.whl (12 kB)
Using cached attrs-23.2.0-py3-none-any.whl (60 kB)
Using cached certifi-2023.11.17-py3-none-any.whl (162 kB)
Using cached charset_normalizer-3.3.2-cp312-cp312-win_amd64.whl (100 kB)
Using cached frozenlist-1.4.1-cp312-cp312-win_amd64.whl (50 kB)
Using cached idna-3.6-py3-none-any.whl (61 kB)
Using cached urllib3-2.1.0-py3-none-any.whl (104 kB)
Using cached yarl-1.9.4-cp312-cp312-win_amd64.whl (76 kB)
Building wheels for collected packages: multidict
  Building wheel for multidict (pyproject.toml) ... done
  Created wheel for multidict: filename=multidict-6.0.4-cp312-cp312-win_amd64.whl size=28182 sha256=ec4f815cc6a33c1f931ddf3bdfd1ae03acb6868b33a27ed22107bfeb83367e7e
  Stored in directory: c:\users\jordi\appdata\local\pip\cache\wheels\f6\d8\ff\3c14a64b8f2ab1aa94ba2888f5a988be6ab446ec5c8d1a82da
Successfully built multidict
Installing collected packages: python-decouple, urllib3, typing-extensions, sniffio, PyYAML, python-multipart, PyJWT, psycopg2-binary, multidict, idna, h11, greenlet, frozenlist, distro, colorama, charset-normalizer, certifi, attrs, annotated-types, yarl, tqdm, sqlalchemy, requests, pyngrok, pydantic-core, httpcore, click, anyio, aiosignal, uvicorn, starlette, pydantic, httpx, aiohttp, openai, fastapi, aiohttp-retry, twilio
Successfully installed PyJWT-2.8.0 PyYAML-6.0.1 aiohttp-3.9.1 aiohttp-retry-2.8.3 aiosignal-1.3.1 annotated-types-0.6.0 anyio-4.2.0 attrs-23.2.0 certifi-2023.11.17 charset-normalizer-3.3.2 click-8.1.7 colorama-0.4.6 distro-1.9.0 fastapi-0.109.0 frozenlist-1.4.1 greenlet-3.0.3 h11-0.14.0 httpcore-1.0.2 httpx-0.26.0 idna-3.6 multidict-6.0.4 openai-1.9.0 psycopg2-binary-2.9.9 pydantic-2.5.3 pydantic-core-2.14.6 pyngrok-7.0.5 python-decouple-3.8 python-multipart-0.0.6 requests-2.31.0 sniffio-1.3.0 sqlalchemy-2.0.25 starlette-0.35.1 tqdm-4.66.1 twilio-8.11.1 typing-extensions-4.9.0 urllib3-2.1.0 uvicorn-0.26.0 yarl-1.9.4
```

- Install SQL Server Express (https://www.microsoft.com/en-GB/sql-server/sql-server-downloads) and SQL Server Management Studio (https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16): 

- Create a sample DB

```sql
CREATE TABLE Conversations(
    id int identity(1,1) primary key,
    sender varchar(max) null,
    message varchar(max) null,
    response varchar(max) null
)
```

- Setting up FAST API

Set a barebone API (bot.py):

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "running"}
```

Run the API using `uvicorn bot:app --reload` in you virtual environment:

```
(venv) C:\repo\OpenAI-Whatsapp-Bot>uvicorn bot:app --reload
INFO:     Will watch for changes in these directories: ['C:\\repo\\OpenAI-Whatsapp-Bot']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [248] using StatReload
INFO:     Started server process [7056]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

![image](https://github.com/JordiCorbilla/OpenAI-Whatsapp-Bot/assets/7347994/b8c2f61f-f070-4b04-bbeb-7fbfd71d1bbf)
  
## Final result
![image](https://github.com/JordiCorbilla/OpenAI-Whatsapp-Bot/assets/7347994/9374ef31-880d-46a0-89cb-09b3b7ebfa54)
![image](https://github.com/JordiCorbilla/OpenAI-Whatsapp-Bot/assets/7347994/6ab97bb7-58af-4299-b573-d99d522b0293)

![image](https://github.com/JordiCorbilla/OpenAI-Whatsapp-Bot/assets/7347994/88d71253-7afa-4c78-868f-628c13c6ee24)

