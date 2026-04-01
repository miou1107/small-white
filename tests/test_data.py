import json
import os
import unittest

class TestDataIntegrity(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.terms_path = os.path.join(self.base_dir, 'terms.json')
        self.quiz_path = os.path.join(self.base_dir, 'quiz.json')

    def test_terms_json_syntax(self):
        """檢查 terms.json 是否為有效的 JSON 且結構正確"""
        with open(self.terms_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.assertIsInstance(data, dict, "terms.json 應為物件格式")
            
            for key, entry in data.items():
                self.assertIn('term', entry, f"術語 '{key}' 缺少 'term' 欄位")
                self.assertIn('translations', entry, f"術語 '{key}' 缺少 'translations' 欄位")
                trans = entry['translations']
                self.assertIn('大白', trans, f"術語 '{key}' 缺少 '大白' 翻譯")
                self.assertIn('小白', trans, f"術語 '{key}' 缺少 '小白' 翻譯")
                # 範例非強制但建議要有
                if '範例' not in trans:
                    print(f"提示: 術語 '{key}' 建議補齊 '範例' 以提升翻譯品質")

    def test_quiz_json_syntax(self):
        """檢查 quiz.json 是否為有效的 JSON 且結構正確"""
        with open(self.quiz_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.assertIsInstance(data, list, "quiz.json 應為陣列格式")
            
            for i, item in enumerate(data):
                self.assertIn('id', item, f"題目 #{i} 缺少 'id'")
                self.assertIn('question', item, f"題目 #{i} 缺少 'question'")
                self.assertIn('options', item, f"題目 #{i} 缺少 'options'")
                self.assertIn('correct_level', item, f"題目 #{i} 缺少 'correct_level'")
                self.assertEqual(len(item['options']), 4, f"題目 #{i} 的選項數量應為 4 個")

if __name__ == '__main__':
    unittest.main()
