# coding: cp932
import difflib

timex_chars = []
timex_tags = []
f = open(ARGV[0])
for line in f:
  line.strip()
  [] = line.split("\t")
  line.insert(0,timex_chars)  # TIMEXの文字列
  line.insert(1,timex_tags)   # TIMEX側のタグ情報
end

ud_chars = []
ud_lines = []
f = open(ARGV[1])
for line in f:
  line.strip()
  [] = line.split("\t")
  line.insert(0,ud_chars)     # UD側の文字列
  line.insert(1,ud_lines)     # UD側の行番号
end

timex2ud = {}
d = difflib.Differ()
sdiffs = Diff::LCS.sdiff(timex_chars,ud_chars) #比較結果を１文字ずつ表示する。
for sdiff in sdiffs
  list(range(sdiff))
#  p sdiff_array
  timex2ud[sdiff_array[1][0]] = sdiff_array[2][0] # TIMEX側の文字列番号と UD側の文字列番号の割り当て
end

ud_lines2timex_tags = Hash.new
timex_tags.each_with_index do |tag,i|

  # TIMEX 側のタグ情報　TIMEX側の文字列番号　UD 側の文字列番号　UD側の行番号
  unless tag.nil?
    ud_lines2timex_tags[ud_lines[timex2ud[i]].to_i] = tag
#    puts tag.to_s + "\t" + i.to_s + "\t" + timex2ud[i].to_s + "\t" + ud_lines[timex2ud[i]]
  end
end

linenum = 0
f = open(ARGV[2])
for line in f:
  line.strip()
  linenum += 1
  if ud_lines2timex_tags.key? linenum
    puts line + "\t" + ud_lines2timex_tags[linenum]
  else
    puts line + "\t"
  end
end
