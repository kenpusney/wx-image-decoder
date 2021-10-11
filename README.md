# Wechat Image Decoder

Wechat encodes chatting image files into `*.dat` files. You can simply decode them to their original format by detecting the encoding key and target format.

All encoded files located under following directories:

```
<Wechat Files>/<wxid>/FileStorage/Image/<mongth>
```

You can use `os.chdir()` to locate the folder, then run the scripts.

Usually there will be few formats:

- Regular `jpg` and `png` files: decoded images.
- `.<hex>.dec` files: corrupted files, trying to decode using detected key.
- `wxgf` files: suspecious WeChat private format, possibly gif emotions.

Please let me know if you discovered more formats.
