# 🧚‍♂️ 小白工程師-AI講人話 (small-white) v3.3.1

將 AI 專業內容自動轉化成生活化表達。**全程自動化回覆補完，讓技術不再冷冰冰。**

---

## ✨ 核心特色 (Strict Auto-Humanize)

| 功能 | 說明 |
| :--- | :--- |
| **一鍵啟動** | 唯一指令：`/small-white` 即可切換所有模式，支援中文參數。 |
| **全程自動** | 只要開啟，所有 AI 專業回覆自動附加【跨工具通用翻譯】補充。 |
| **保留精確** | 原汁原味保留 AI 專業回覆，技術與理解並存。 |
| **決策輔助** | 翻譯區塊會主動提供技術決策建議，協助你快速拍板。 |

---

## 📥 安裝指引 (Quick Install)

### 方法 A：全自動（推薦）
直接複製以下內容到對話框：
> 「請從 `https://github.com/miou1107/small-white` clone 專案，並執行 `./install.sh`。成功後請回報！」

### 方法 B：手動 CLI
```bash
git clone https://github.com/miou1107/small-white.git
cd small-white
chmod +x install.sh
./install.sh
```

---

## 🎮 使用方式 (Unique Command)

> [!IMPORTANT]
> 本 Skill 僅支援唯一指令 `/small-white`。

| Command | Parameter | Function |
| :--- | :--- | :--- |
| **`/small-white`** | **`big`** / **`大白`** | **啟動：大白模式** (📚 詳盡比喻、生活化說明) |
| **`/small-white`** | **`small`** / **`小白`** | **啟動：小白模式** (📄 核心總結、精煉懶人包) |
| **`/small-white`** | **`off`** / **`閉嘴`** | **關閉：原始回覆** (恢復 AI 精確原文輸出) |

---

---

## 🛡️ 模式演示 (User Interface Examples)

### 📚 大白模式 (Big White Mode)
適合技術啟蒙與決策解釋，提供詳盡的比喻與具體的執行建議。
![大白模式演示圖](docs/media/demo-big.png)

---

### 📄 小白模式 (Small White Mode)
適合開發衝刺期，只給懶人包核心重點，絕不廢話。
![小白模式演示圖](docs/media/demo-small.png)

---

### 🚫 關閉模式 (Off Mode)
恢復 AI 最專業、無任何修飾的純技術原文回覆。
![關閉模式演示圖](docs/media/demo-off.png)

---

## 🎯 輸出範例 (v3.3.1 跨工具格式)

**AI 原話**：
> 「建議從 MySQL 去 INSERT 一段 status 紀錄，並確保使用了 Transaction 以維持數據一致性。」

---
> ### 📚 講大白話：
> 
> 簡單來說，我們要到 **資料庫 (MySQL)** 去 **新增 (INSERT)** 一個「狀態紀錄」。
> 
> **具體比喻**：就像你在 App 上點了「一碗牛肉麵並付了錢」。
> 
> **我的決策建議**：請務必開啟 **Transaction (交易機制)**。這就像確保你「口袋的錢扣掉 150 元」跟「廚房顯示有新訂單要煮」這兩件事必須同時成立。如果你付了錢但廚房沒跳單，你就只能餓肚子；如果廚房煮了但你沒付錢，老闆就虧大了。所以我們要用連動鎖死，保證這兩件事「同生共死」。

*(提示：輸入 「/small-white 閉嘴」/「/small-white 小白」/「/small-white 大白」 可開關此說明)*

---

## 📁 檔案結構

```text
small-white/
├── SKILL.md          # 小白工程師 Skill (v3.3.1)
├── install.sh        # 自動安裝、同步與初始化
├── CHANGELOG.md      # 版本紀錄
└── README.md         # 本文檔
```

---

## 📜 授權

MIT License
