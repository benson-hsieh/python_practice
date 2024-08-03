檔案狀態:
U - 新建檔案
A - 加入追蹤
M - 檔案相對上個commit版本有所變更

Git追蹤的是檔案的變化，而非檔案本身，所以若有刪除某些檔案，一樣須下指令1和指令2
gitignore file可以避免無關的檔案或是不需要進行版控的檔案混入到檔案紀錄(ex:有些私人圖檔或檔案)

git常用指令:
1. git add . : 把當前目錄中所有的變更都放到暫存區(Staging Area)，也可以不用. 直接打指定檔案名稱
2. git commit -m "訊息內容" : 執行過1.即可提交新的版本紀錄
3. git log --oneline : 查看commit紀錄/版本紀錄(oneline可簡化log內容)
4. git push : 若本地的檔案有存到遠端repository，commit後下push指令，即可將本地的變更推送github
5. git pull : 從github下載最新的變更
6. git diff : 查看版本差異
7. git checkout 目標還原點ID -- 檔案 : 還原到特定版本 => 接續commit指令才會變更版本
8. git reset --hard 目標還原點ID : 同7，但7會保留先前的版本紀錄，安全性較高，8是直接重設
9. git status : 查看當前檔案狀態
10. git clone url : 可把自己或他人的儲存庫複製到自己的本地端電腦(下載好的儲存庫會變成子資料夾)
11. 新開分支，在合併前的所有變更不會影響到其他分支，在自己的分支內進行編輯: 
    git checkout        -b          branch2 
        切換分支  建立並切換至新分支  新分支名稱 
12. 若有在自己所在的新分支做檔案變更，需下指令1、2和以下指令:
    git push origin branch2

在github新增repository有提供三個指令協助開發者將本地端的檔案推送到雲端儲存庫:
1. 用來連結本地和遠端的儲存庫
git remote   add      origin         url
     遠端    新增  遠端儲存庫名稱 遠端儲存庫網址

2. 把原來的主線分支從master(主人)改為較中性的詞語main(主要)
git  branch    -M      main
    分支管理 重新命名 新的分支名

3. 把本地端位於main分支的資料推送到雲端儲存庫
git  push    -u     origin     main
     推送  建立關聯  遠端名稱  本地名稱
