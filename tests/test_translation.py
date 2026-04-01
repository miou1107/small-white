import json
import os
import re

def simple_translate(text, level, terms):
    """
    簡單模擬 SKILL.md 中定義的翻譯邏輯。
    實際上 AI 工具會使用更複雜的 Prompt 處理，
    這裡僅測試術語庫的替換與串聯。
    """
    translated = text
    # 將術語按長度排序，避免短術語先被替換
    sorted_keys = sorted(terms.keys(), key=len, reverse=True)
    
    found_any = False
    for key in sorted_keys:
        term_data = terms[key]
        raw_term = term_data['term']
        # 簡單不分大小寫的替換
        if re.search(raw_term, translated, re.IGNORECASE):
            found_any = True
            replacement = term_data['translations'].get(level, raw_term)
            translated = re.sub(raw_term, f"『{replacement}』", translated, flags=re.IGNORECASE)
    
    return translated if found_any else text

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    terms_path = os.path.join(base_dir, 'terms.json')
    
    with open(terms_path, 'r', encoding='utf-8') as f:
        terms = json.load(f)
    
    test_cases = [
        "使用 RAG 結合 LLM，可以有效減少 Hallucination。",
        "建議使用 Redis 作為 Cache 減少 Latency。",
        "前端開發需要注意 API 的 HTTP 狀態碼。"
    ]
    
    for text in test_cases:
        print(f"\n原文: {text}")
        print(f"大白: {simple_translate(text, '大白', terms)}")
        print(f"小白: {simple_translate(text, '小白', terms)}")

if __name__ == "__main__":
    main()
