# はじめに
思いの外覚えていなかったので、ざっくりとした説明になります

# 手順

## time_conll
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
