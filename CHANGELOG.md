# 📝 版本變更紀錄 (CHANGELOG.md)

## [3.3.0] - 2026-04-01

### 🚀 品牌重構 (Rebranding & Defaults)

- **專案更名**：正式更名為「小白工程師-AI講人話」，Repo 名稱為 `small-white`。
- **指令更新**：全面捨棄 `xiaobai` 拼音，改用 `/small-white [big|small|off|大白|小白|閉嘴]`。
- **預設小白模式**：安裝後預設啟動 `small` (📄 小白) 模式。
- **隨機提示機制**：操作提示改為隨機出現，減少干擾。

---

## [3.2.0] - 2026-04-01

### 🎨 介面與視覺優化 (UI/UX Alignment)

- **跨工具通用格式**：採用 `---` 與 `> ` (Blockquote) 確保在所有 AI 工具（Claude, ChatGPT, IDE）中渲染一致。
- **圖示更新 (Option C)**：選定大白模式為 📚 (詳盡引導)，小白模式為 📄 (核心精華)。
- **決策輔助 (Decision Support)**：規則更新，翻譯區塊必須主動對技術選擇給予具體建議。

---

## [3.0.0] - 2026-04-01

### 🚀 重大重構 (Major Feature Overhaul)

- **單一指令化 (Unique Command)**：捨棄 `/translate`, `/level` 等指令，統一整合為 `/xiaobai [big|small|off]`。
- **全域指令啟動**：在 `~/.gemini/antigravity/global_workflows/xiaobai.md` 正式註冊系統指令。
- **全程自動補充翻譯 (Auto-Humanize)**：開啟模式後，AI 專業回覆將自動強制附加 `【講人話】` 區塊。
- **回覆格式標準化**：確立「AI 原話」+「【講人話】」的標準輸出格式。
- **配置優化**：`profile.json` 更新為 v3.0 `current_mode` 儲存架構。

### 🔄 改進

- **極簡安裝回饋**：優化 `install.sh` 同步後的提示訊息。
- **移除智慧觀察**：由全程自動補充取代頻繁的調等詢問。

---

## [2.1.0] - 2026-04-01

### 🌍 國際化更新 (Internationalization)

- **指令英文化**：將核心指令改為英文以提升相容性。

---

## [2.0.0] - 2026-04-01

### 🚀 去評測化 (No-Quiz)

- **移除評測功能**：刪除 `quiz.json`。
- **動態調等**：改採實時觀察。

---
