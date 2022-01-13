# 課題2
パブリッシャを1つもつノードcount.pyが数字を一ずつカウントしていく。

サブスクライバを1つもつノードtwice.pyを作成する。

count.pyで数字が１ずつカウントされていく中で、twice.pyを同時に動かし、素数だけを除外して画面に出力させる。


# 実行方法
端末を3つ用意し、それぞれ以下のコマンドを入力する

端末1

    roscore

端末2

    rosrun mypkg count.py    

端末3

    rosrun mypkg twice.py
    

# 実行例
![実行例](https://github.com/szkkt/robosys2/blob/main/%E3%82%B9%E3%82%AF%E3%82%B7%E3%83%A7.png)

89、97、101、103、107、109などといった素数が除外されて出力されいます。

# 実行動画

https://youtu.be/maSiojf-RwA
