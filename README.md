# 心情音乐推荐网站

一款基于 Python Flask 开发的简易心情音乐推荐网站，用户可以根据当前心情选择对应分类，系统会自动推荐适配的歌曲列表并支持在线播放。

## 功能特点

- 🎭 **心情选择**：支持治愈、热血、安静、欢快四种心情分类
- 🎧 **智能推荐**：根据心情自动匹配内置歌单
- ▶️ **在线播放**：内嵌音乐播放器，支持在线听歌
- 📤 **歌曲上传**：用户可自主添加歌曲至对应心情分类
- 🌐 **云端部署**：支持部署至 Railway 平台

## 技术栈

- 后端：Python 3.x + Flask
- 前端：HTML + CSS
- 部署平台：Railway
- 代码管理：Git + GitHub

## 项目结构

```
Music Website/
├── app.py              # 主程序（路由、数据、逻辑）
├── requirements.txt    # 依赖配置
├── Procfile            # Railway 部署配置
├── .gitignore          # Git 忽略文件
└── templates/
    ├── index.html      # 首页
    └── result.html     # 推荐结果页
```

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务器
python app.py

# 访问地址
http://127.0.0.1:5000
```

## 部署至 Railway

1. 将代码推送到 GitHub 仓库
2. 在 Railway 平台新建项目，选择 GitHub 仓库导入
3. Railway 会自动检测 Procfile 和 requirements.txt
4. 部署完成后获取公网访问链接

## 注意事项

- 歌曲数据存储在内存中，服务器重启后用户上传的歌曲会丢失
- 内置歌曲使用网易云音乐外链，可能存在跨域限制
- 如需持久化存储，可添加 SQLite 数据库