# はじめに
思いの外覚えていなかったので、ざっくりとした説明になります

# 手順

## taka
- たぶんこれがDCTの情報抽出のプログラム
- 一昨年(わたしが3年生)に他の人がプレ卒研で作成したもの

## time_conll
### BCCWJ-TIMEX
- git上にはデータは置きませんでしたが、time_conllの下に作成してください
- time_conll/BCCWJ-TIMEX/*.xml という感じです
- 昨年の時点では連番で54個あったと思います
### E2E
- correct内のpythonファイルを動かして、tsvファイルを作成
- event1内のfirst_event内のpythonファイルを動かして、txtファイルを取得
- event1内のsecond_event内のpythonファイルを動かして、txtファイルを取得
- event2内も上記と同様
- evento_to_event.Rを動かして、input内のようなtsvファイルを作成

  これは今まで作ってきたファイルをそれぞれ合体させた感じ

- all_combine_e2e.Rを動かして、54個すべてのファイルを結合

  all_e2e.tsvという全部の情報がまとまったファイルができる

### MAT
E2Eとほば同じ

### T2E
E2Eとほぼ同じ

### DCT
- xml_dct.pyを動かして、イベントidを取得
- もしかしたらこのままだと、イベントidだけ取得になってるかもしれない

# 参考
- [R インストール](https://qiita.com/hujuu/items/ddd66ae8e6f3f989f2c0)
