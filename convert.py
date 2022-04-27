from PIL import Image, ImageDraw, ImageFont

menu_btn = [1,2,3,4,5,6,7,8,9,10,27,28,29,30]
passcode_btn = list(range(12, 20))
profile = [20,21]

def resize_menubtn():
    try:
        for number in menu_btn:
            #iosの方の画像ファイル名
            ios_filename = f"i_{str(number).zfill(2)}.png"
            #androidの方の画像ファイル名
            android_filename = f"a_{str(number).zfill(2)}.png"

            #画像読み込み
            img = Image.open(ios_filename)
            # 横128、縦112に変換
            (width, height) = (128, 112)
            # 画像をリサイズする
            img_resized = img.resize((96, height))
            im = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            im.paste(img_resized, (0,0))
            # ファイルを保存
            im.save(android_filename, quality=90)
    except FileNotFoundError:
        print("メイン画像のファイルが足りていないようです！途中終了しました！")


def resize_passcodebtn():
    try:
        for number in passcode_btn:
            #iosの方の画像ファイル名
            ios_filename = f"i_{str(number).zfill(2)}.png"
            #androidの方の画像ファイル名
            android_filename = f"a_{str(number).zfill(2)}.png"

            #画像読み込み
            img = Image.open(ios_filename)
            # 横116、縦116に変換
            (width, height) = (116, 116)
            # 画像をリサイズする
            img_resized = img.resize((width, height))
            # ファイルを保存
            img_resized.save(android_filename, quality=90)
    except FileNotFoundError:
        print("パスコード画像のファイルが足りていないようです！途中終了しました！")

def resize_profileimg():
    try:
        for number in profile:
            #iosの方の画像ファイル名
            ios_filename = f"i_{str(number).zfill(2)}.png"
            #androidの方の画像ファイル名
            android_filename = f"a_{str(number).zfill(2)}.png"

            #画像読み込み
            img = Image.open(ios_filename)
            # 横247、縦247に変換
            (width, height) = (247, 247)
            # 画像をリサイズする
            img_resized = img.resize((width, height))
            # ファイルを保存
            img_resized.save(android_filename, quality=90)
    except FileNotFoundError:
        print("プロフィール画像のファイルが足りていないようです！途中終了しました！")

def main():
    resize_menubtn()
    resize_passcodebtn()
    resize_profileimg()

if __name__ == "__main__":
    main()