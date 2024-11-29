#!/usr/bin/env python3
# SPDX-FileCopyrightText: 
# SPDX-License-Identifier: BSD-3-Clause
import sys

def calculate_alcohol_content(whiskey_volume_ml, whiskey_abv, soda_volume_ml):
    total_volume = whiskey_volume_ml + soda_volume_ml
    alcohol_content_whiskey = whiskey_volume_ml * whiskey_abv / 100
    if total_volume == 0:
        raise ValueError("総量がゼロです")
    return (alcohol_content_whiskey / total_volume) * 100

def main():
    try:
        input_data = input().strip().split()
        if len(input_data) == 0:
            print("無効な入力: 入力が空です")
            sys.exit(1)
        if len(input_data) < 2:
            print(f"無効な入力: {' '.join(input_data)}")
            sys.exit(1)

        whiskey_volume_ml = float(input_data[0])
        soda_volume_ml = float(input_data[1])
        whiskey_abv = 40  # 固定値（ウィスキーのアルコール度数）

        highball_abv = calculate_alcohol_content(whiskey_volume_ml, whiskey_abv, soda_volume_ml)
        print(f"ハイボールのアルコール度数: {highball_abv:.2f}%")

    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)
    except IndexError:
        print("無効な入力: 入力の形式が正しくありません")
        sys.exit(1)

if __name__ == "__main__":
    main()
