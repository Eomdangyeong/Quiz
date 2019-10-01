# Quiz

```
Microsoft Windows [Version 10.0.17134.950]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\IME40>cd C:\PatternRecognition //폴더 만들기

C:\PatternRecognition>git config --global user.name Eomdangyeong 

C:\PatternRecognition>git config --global user.email eksrud2587@gmail.com

C:\PatternRecognition>git clone https://github.com/Eomdangyeong/Quiz.git
Cloning into 'Quiz'...
warning: You appear to have cloned an empty repository.//Quiz라는 깃 만들어서 내컴퓨터로 클론해오기


C:\PatternRecognition>cd Quiz //클론해오면 Quiz라는 폴더가 PatternRecongition에 생기고 거기로 이동

C:\PatternRecognition\Quiz>git add . //미리 만들어놓은 20190924_Quiz1.py와 20190930_Quiz2_solution.py add

C:\PatternRecognition\Quiz>git commit -m "Add 1" //마스터 브랜치로 커밋
[master (root-commit) 3ed8591] Add 1
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 20190924_Quiz1.py
 create mode 100644 20190924_Quiz2_solution.py

C:\PatternRecognition\Quiz>git branch
* master

C:\PatternRecognition\Quiz>git branch solution //솔루션 브랜치 추가 생성


C:\PatternRecognition\Quiz>git checkout master
Already on 'master'
D       20190924_Quiz1.py
A       20190924_Quiz1_solution.py
Your branch is based on 'origin/master', but the upstream is gone.
  (use "git branch --unset-upstream" to fixup)

C:\PatternRecognition\Quiz>git add .

C:\PatternRecognition\Quiz>git commit -m "Add1" //문제 2번에서 마스터 브랜치로 파일 두개 add
[master 9324716] Add1
 2 files changed, 39 insertions(+)
 delete mode 100644 20190924_Quiz1.py
 create mode 100644 20190924_Quiz1_solution.py


C:\PatternRecognition\Quiz>git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.01 KiB | 345.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/Eomdangyeong/Quiz.git
 * [new branch]      master -> master

C:\PatternRecognition\Quiz>git add .

C:\PatternRecognition\Quiz>git commit -m "add quiz"
[master 249ecc4] add quiz
 2 files changed, 39 deletions(-)
 create mode 100644 20190924_Quiz1.py
 delete mode 100644 20190924_Quiz1_solution.py

C:\PatternRecognition\Quiz>git push
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 259 bytes | 129.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0)
To https://github.com/Eomdangyeong/Quiz.git
   9324716..249ecc4  master -> master


C:\PatternRecognition\Quiz>git checkout solution
Switched to branch 'solution'
D       20190924_Quiz1.py



C:\PatternRecognition\Quiz>git add 20190924_Quiz1_solution.py

C:\PatternRecognition\Quiz>git commit -m "add solution"
[solution c1252cf] add solution
 1 file changed, 39 insertions(+)
 create mode 100644 20190924_Quiz1_solution.py

C:\PatternRecognition\Quiz>git push origin solution
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 843 bytes | 421.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'solution' on GitHub by visiting:
remote:      https://github.com/Eomdangyeong/Quiz/pull/new/solution
remote:
To https://github.com/Eomdangyeong/Quiz.git
 * [new branch]      solution -> solution



C:\PatternRecognition\Quiz>git checkout master
Switched to branch 'master'
D       20190924_Quiz1.py
Your branch is up to date with 'origin/master'.


C:\PatternRecognition\Quiz>git branch
* master

C:\PatternRecognition\Quiz>git branch solution

C:\PatternRecognition\Quiz>git checkout solution //솔루션 브랜치에 올리기 위해 solution을 master브랜치로 
Switched to branch 'solution'
D       20190924_Quiz1.py

C:\PatternRecognition\Quiz>git add 20190924_Quiz1_solution.py

C:\PatternRecognition\Quiz>git commit -m "add solution2"
On branch solution
Changes not staged for commit:
        deleted:    20190924_Quiz1.py

no changes added to commit

C:\PatternRecognition\Quiz>git push
fatal: The current branch solution has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin solution


C:\PatternRecognition\Quiz>git push origin solution
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 975 bytes | 975.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
remote:
remote: Create a pull request for 'solution' on GitHub by visiting:
remote:      https://github.com/Eomdangyeong/Quiz/pull/new/solution
remote:
To https://github.com/Eomdangyeong/Quiz.git
 * [new branch]      solution -> solution

C:\PatternRecognition\Quiz>git checkout master //솔루션에서 마스터로 마스터 브랜치 변경해주고
Switched to branch 'master'
D       20190924_Quiz1.py
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

C:\PatternRecognition\Quiz>git merge solution //merge됬는지 다시 확인
Already up to date.


git branch -d solution
git oush origin --delete solution //브랜치 삭제하는 코드



```
