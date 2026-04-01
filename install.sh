#!/bin/bash

# =====================================
# 🧚‍♂️ 小白工程師-AI講人話 v3.2 - 本地開發與自動安裝腳本
# =====================================
# 使用方式：在專案根目錄執行 ./install.sh
# =====================================

set -e

# 顏色定義
if [ -t 1 ]; then
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    RED='\033[0;31m'
    BLUE='\033[0;34m'
    NC='\033[0m'
else
    GREEN=''
    YELLOW=''
    RED=''
    BLUE=''
    NC=''
fi

echo ""
echo "🧚‍♂️ 小白工程師-AI講人話 v3.2 - 開發者安裝精靈"
echo "========================================"
echo ""

# 取得當前專案目錄 (絕對路徑)
SOURCE_DIR=$(pwd)

# 初始化設定檔 (預設小白模式)
CONFIG_DIR="${HOME}/.small-white"
mkdir -p "$CONFIG_DIR"
if [ ! -f "$CONFIG_DIR/profile.json" ]; then
    echo '{"current_mode": "small"}' > "$CONFIG_DIR/profile.json"
    echo -e "${GREEN}✓${NC} 已初始化設定檔，預設開啟【小白模式】。"
fi

# 安裝函數
install_skill() {
    local tool_name=$1
    local dest_parent_path=$2
    local dest_path="${dest_parent_path}/small-white"
    
    mkdir -p "$dest_parent_path" 2>/dev/null || true
    
    if [ -d "$dest_parent_path" ]; then
        echo -e "${GREEN}✓${NC} 正在安裝至 $tool_name..."
        
        rm -rf "$dest_path"
        mkdir -p "$dest_path"
        
        # 複製必要檔案
        cp "$SOURCE_DIR/README.md" "$dest_path/"
        cp "$SOURCE_DIR/SKILL.md" "$dest_path/"
        cp "$SOURCE_DIR/terms.json" "$dest_path/"
        cp "$SOURCE_DIR/CHANGELOG.md" "$dest_path/"
        cp "$SOURCE_DIR/FILELIST.md" "$dest_path/"
        
        # 複製媒體檔案 (若存在)
        if [ -d "$SOURCE_DIR/docs/media" ]; then
            mkdir -p "$dest_path/docs/media"
            cp -r "$SOURCE_DIR/docs/media/"* "$dest_path/docs/media/"
        fi
        
        echo -e "  ${GREEN}✓${NC} 同步完成！"
        return 0
    fi
    return 1
}

echo "🔍 正在同步 v3.2 (Small-White) 檔案..."
echo ""

installed_count=0
HOME_DIR="${HOME}"

# Antigravity
[ -d "$HOME_DIR/.gemini/antigravity/skills" ] && install_skill "Antigravity" "$HOME_DIR/.gemini/antigravity/skills" && ((installed_count++))

# AI Agents Folder
[ -d "$HOME_DIR/.agents/skills" ] && install_skill "AI Agents Folder (~/.agents)" "$HOME_DIR/.agents/skills" && ((installed_count++))

# Other Tools
[ -d "$HOME_DIR/.continue" ] && install_skill "Continue" "$HOME_DIR/.continue/skills" && ((installed_count++))
[ -d "$HOME_DIR/.codex" ] && install_skill "Codex" "$HOME_DIR/.codex/skills" && ((installed_count++))
[ -d "$HOME_DIR/.cursor" ] && install_skill "Cursor" "$HOME_DIR/.cursor/skills" && ((installed_count++))
[ -d "$HOME_DIR/.windsurf" ] && install_skill "Windsurf" "$HOME_DIR/.windsurf/skills" && ((installed_count++))
[ -d "$HOME_DIR/.roo" ] && install_skill "Roo" "$HOME_DIR/.roo/skills" && ((installed_count++))
[ -d "$HOME_DIR/.trae" ] && install_skill "Trae" "$HOME_DIR/.trae/skills" && ((installed_count++))

echo ""
echo "========================================"
echo ""

if [ $installed_count -eq 0 ]; then
    echo -e "${RED}✗${NC} 找不到任何安裝路徑。"
    exit 1
else
    echo -e "${GREEN}🎉${NC} 小白工程師安裝成功！"
    echo ""
    echo "📝 指令更新：使用 /small-white [大白|小白|閉嘴] 切換模式。"
    echo "提示：翻譯完後會隨機顯示開關提示。"
fi

echo ""
