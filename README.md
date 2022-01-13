# 課題2
パブリッシャを1つもつノードcount.pyが数字を一ずつカウントしていく。

サブスクライバを1つもつノードtwice.pyを作成する。

count.pyで数字が１ずつカウントされていく中でtwice.pyを同時に動かし、素数だけを除外して画面に出力させる。


# 実行方法
端末を3つ用意し、それぞれ以下のコマンドを入力する

端末1

    roscore

端末2

    rosrun mypkg count.py    

端末3

    rosrun mypkg twice.py
    

# 実行動画

https://youtu.be/maSiojf-RwA
