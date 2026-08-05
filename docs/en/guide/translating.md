# Translating

AeroLiners Set achieves multilingual support through the `.lng` files in the `lang/` directory. All interface text — GRF name, parameter descriptions, model names, livery names — comes from the `STR_*` strings in these files.

There are currently 15 built-in languages: catalan, chinese_simplified, chinese_traditional, croatian, czech, dutch, english, finnish, german, indonesian, italian, korean, polish, russian, spanish.

## Translation file format

Each `.lng` file starts with a language ID, followed by `string_id : localized_text` key-value pairs:

```text
##grflangid 0x01
STR_GRF_NAME                 :AeroLiners
STR_GRF_DESCRIPTION          :{ORANGE}AeroLiners Set{}...
STR_PARAM_BCOSTS_NAME        :Base cost factor
STR_AIRV_AIRBUS_A300_600R    :Airbus A300-600R
...
```

::: warning Notes
- **Do not use Tab indentation** in `.lng` files — use spaces only.
- Placeholders (such as `{VERSION}`, `{ORANGE}`, `{SILVER}`) must be preserved verbatim.
:::

## Adding a new language

1. Copy `lang/english.lng` and name it `{lang_id}_{lang_name}.lng` (refer to the upstream legacy flow `sprites/nfo/00strings`).
2. Look up your language ID at <http://wiki.ttdpatch.net/tiki-index.php?page=Action4#language_id>.
3. Change every `english` in the file to your language name, and fill the corresponding language constant after `#define LANG .` (valid values are in `docs/readme.txt` section 6, e.g. `CHINESE_SIMPLIFIED`, `KOREAN`).
4. Translate everything inside `"..."`; **prefix untranslated lines with `U`** to save NewGRF size and memory.

## Updating an existing language

Simply edit the corresponding `lang/*.lng`, keeping the string IDs unchanged and only updating the right-hand text. After adding models / liveries, don't forget to add translations for the new `STR_AIRV_*` / `STR_VLIV_*` strings.

Back: [Liveries & Graphics →](/guide/liveries) ｜ Next: [Contributing →](/guide/contributing)
