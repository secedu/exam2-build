# Exam 2 - Build (6443 only)

## Instructions

- Clone the repository and go into the folder of the domain you were assigned. 
- There will be the 5 subdomains from Exam 1.
- For each subdomain we have given you the source code and a writeup of the vulnerability in SOLUTION.md.
- Your task is to patch the vulnerability such that the exploit used in `SOLUTION.md` no longer works.
- Only modify what is necessary to fix the vulnerability.

**NOTE**: The flags you find may be different from what you saw in Exam 1. They may also be different from what you see in `SOLUTION.md`

**NOTE**: For the SQLi exploits, you may have to modify them from using mysql comments: `#` to sqlite comments: `--` if you choose to stick with a sqlite database

**NOTE**: Due to the nature of the XSS challenges, you might not always be able to get the JS bot to post a flag, however it is enought to identify the content injection location and verify it has been fixed with a different payload (non XSS based)

**NOTE**: If you feel as though you cannot accurately express how to mitigate the vulnerability through code alone, feel free to add comments discussing your analysis of the situtation and what additional steps you might take to fix the vulnerability

## Swapping between mysql and sqlite

In the challenges that use a database we have set them all to use sqlite - however, for some challenges you may prefer to use mysql instead. To faciliate this you need to:

1 .Uncomment the first line and comment out the second line in `flaskr/app.py`

```
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}/db'.format(SQL_ROOT_PASSWORD, DB_HOST)
SQLALCHEMY_DATABASE_URI = "sqlite://"
```

2. Run mysql `docker run -p 3306:3306 d11wtq/mysql`

## Running

1. install python 3.6
2. `virtualenv venv -p python3.6`
3. `source ./venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python run.py`
6. Check run.py to see what port its being run off
7. Visit `http://127.0.0.1:<port>`

## Submission

1. Make your changes
2. `git add` and `git commit`
3. Create a git tag: `git tag fixed`
4. Create a git diff: `git diff init fixed > patch.diff`
5. Submit your diff: `give cs6443 exam patch.diff`
