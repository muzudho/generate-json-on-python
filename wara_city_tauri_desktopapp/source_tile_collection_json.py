def stringify_sea_pattern(tilemap_name):
    return f"""\


    "{tilemap_name}_0" : {{ "top": 0, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_16" : {{ "top": 0, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_32" : {{ "top": 0, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_48" : {{ "top": 0, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_49" : {{ "top": 0, "left": 128, "width": 32, "height": 32 }},
    "{tilemap_name}_64" : {{ "top": 0, "left": 160, "width": 32, "height": 32 }},
    "{tilemap_name}_80" : {{ "top": 32, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_96" : {{ "top": 32, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_98" : {{ "top": 32, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_112" : {{ "top": 32, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_113" : {{ "top": 32, "left": 128, "width": 32, "height": 32 }},
    "{tilemap_name}_114" : {{ "top": 32, "left": 160, "width": 32, "height": 32 }},
    "{tilemap_name}_115" : {{ "top": 64, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_128" : {{ "top": 64, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_144" : {{ "top": 64, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_152" : {{ "top": 64, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_160" : {{ "top": 64, "left": 128, "width": 32, "height": 32 }},
    "{tilemap_name}_176" : {{ "top": 64, "left": 160, "width": 32, "height": 32 }},
    "{tilemap_name}_177" : {{ "top": 96, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_184" : {{ "top": 96, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_185" : {{ "top": 96, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_192" : {{ "top": 96, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_196" : {{ "top": 96, "left": 128, "width": 32, "height": 32 }},
    "{tilemap_name}_208" : {{ "top": 96, "left": 160, "width": 32, "height": 32 }},
    "{tilemap_name}_212" : {{ "top": 128, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_216" : {{ "top": 128, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_220" : {{ "top": 128, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_224" : {{ "top": 128, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_226" : {{ "top": 128, "left": 128, "width": 32, "height": 32 }},
    "{tilemap_name}_228" : {{ "top": 128, "left": 160, "width": 32, "height": 32 }},
    "{tilemap_name}_230" : {{ "top": 160, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_240" : {{ "top": 160, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_241" : {{ "top": 160, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_242" : {{ "top": 160, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_243" : {{ "top": 160, "left": 128, "width": 32, "height": 32 }},
    "{tilemap_name}_244" : {{ "top": 160, "left": 160, "width": 32, "height": 32 }},
    "{tilemap_name}_245" : {{ "top": 192, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_246" : {{ "top": 192, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_247" : {{ "top": 192, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_248" : {{ "top": 192, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_249" : {{ "top": 192, "left": 128, "width": 32, "height": 32 }},
    "{tilemap_name}_250" : {{ "top": 192, "left": 160, "width": 32, "height": 32 }},
    "{tilemap_name}_251" : {{ "top": 224, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_252" : {{ "top": 224, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_253" : {{ "top": 224, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_254" : {{ "top": 224, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_255" : {{ "top": 224, "left": 128, "width": 32, "height": 32 }},
"""


def stringify_sea_border_pattern(tilemap_name):
    return f"""\


    "{tilemap_name}_A0" : {{ "top": 0, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_A16" : {{ "top": 0, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_A32" : {{ "top": 0, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_A48" : {{ "top": 0, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_A64" : {{ "top": 32, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_A80" : {{ "top": 32, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_A96" : {{ "top": 32, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_A112" : {{ "top": 32, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_A128" : {{ "top": 64, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_A144" : {{ "top": 64, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_A160" : {{ "top": 64, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_A176" : {{ "top": 64, "left": 96, "width": 32, "height": 32 }},
    "{tilemap_name}_A192" : {{ "top": 96, "left": 0, "width": 32, "height": 32 }},
    "{tilemap_name}_A208" : {{ "top": 96, "left": 32, "width": 32, "height": 32 }},
    "{tilemap_name}_A224" : {{ "top": 96, "left": 64, "width": 32, "height": 32 }},
    "{tilemap_name}_A240" : {{ "top": 96, "left": 96, "width": 32, "height": 32 }},
"""


text = """\
{
    "#comment" : "このJSONファイルは直接編集せず、次のURLにあるPythonスクリプトを編集して、スクリプトを実行して生成してください。 https://github.com/muzudho/generate-json-on-python/tree/main/wara_city_on_tauri",


    "land_wasteland": { "top": 0, "left": 0, "width": 32, "height": 32 },
    "land_vocantLand": { "top": 0, "left": 32, "width": 32, "height": 32 },
    "land_forest": { "top": 0, "left": 64, "width": 32, "height": 32 },
"""

text += stringify_sea_pattern(tilemap_name="out")
text += stringify_sea_border_pattern(tilemap_name="outBorder")


text += """\


"""

text += stringify_sea_pattern(tilemap_name="sea")
text += stringify_sea_border_pattern(tilemap_name="seaBorder")
text += stringify_sea_pattern(tilemap_name="wastelandRoad")
text += stringify_sea_border_pattern(tilemap_name="wastelandBorder")

# 末尾の［カンマ、改行］を削除
text = text.rstrip(",\n")

# 改行を消しすぎたので追加
text += """\

}\
"""

with open("temp.json","w",encoding="utf-8") as o:
    print(text, file=o)

print("Wrote temp.json")
