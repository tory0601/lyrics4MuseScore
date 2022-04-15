import os
import glob
from pykakasi import kakasi

def conv4MuseScore(text_file):
    """
    テキストファイルの中身をMuseScoreに貼り付けられる形に変換する。\n
    Args:
        text_file : 読み込む歌詞ファイル（.txt）
    Returns:
        convert_file : 変換後の歌詞ファイル（.txt）
    """
    # 変換クラスの生成
    kaka = kakasi()

    # テキストファイル読み込み
    with open(text_file, "r", encoding="utf-8") as f:
        lyrics = [s.strip() for s in f.readlines()] # 改行ごとにリスト化
        lyrics = [i for i in lyrics if i != ""] # 空欄を削除
    
    # 全単語を統合する文字列
    all_str = ""
    
    # 1行ごとに変換
    for lyric in lyrics:
        lyric = lyric.replace(" ", "").replace("　", "") # 半角&全角スペースを削除
        sentence = kaka.convert(lyric)

        for word in sentence:
            all_str += word["hira"] # 1単語ずつ統合
    
    # MuseScore用の文字列
    ms_str = ""

    # 半角スペースの挿入
    for char in list(all_str):
        if char in ["ゃ", "ゅ", "ょ"]:
            ms_str += char
        else:
            ms_str += " " + char
    
    # 最初の半角スペースを削除
    ms_str = ms_str[1:]

    # ファイル名取得
    file_name = os.path.splitext(os.path.basename(text_file))[0]

    # 変換ファイルに書き込み
    with open("./02_converted_data/" + file_name + "_converted.txt", "w", encoding="utf-8") as f:
        f.write(ms_str)
    
    return "./02_converted_data/" + file_name + "_converted.txt"

def main():
    text_list = glob.glob("./01_text_data/*.txt")

    for tl in text_list:
        conv4MuseScore(tl)
    
    return 0

if __name__ == '__main__':
    print("--main start--")

    main()

    print("--main end--")
