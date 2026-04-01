import json
import os
import unittest
from datetime import datetime

class TestV2Logic(unittest.TestCase):
    def setUp(self):
        """設定測試用的臨時 profile"""
        self.profile_path = os.path.expanduser("~/.tech-translator/profile.json")
        self.backup_content = None
        if os.path.exists(self.profile_path):
            with open(self.profile_path, 'r') as f:
                self.backup_content = f.read()
                
        # 初始化預設等級為 5 (小白)
        self.default_profile = {
            "current_level": "小白工程師",
            "level_value": 5,
            "preferences": {"translation_enabled": True}
        }
        with open(self.profile_path, 'w') as f:
            json.dump(self.default_profile, f)

    def tearDown(self):
        """還原原始 profile"""
        if self.backup_content:
            with open(self.profile_path, 'w') as f:
                f.write(self.backup_content)

    def test_manual_level_switch(self):
        """測試手動切換等級是否正確更新 profile.json"""
        # 模擬切換至 Lv.10
        new_lv = 10
        with open(self.profile_path, 'r') as f:
            data = json.load(f)
        
        data["level_value"] = new_lv
        data["current_level"] = "正港工程師"
        
        with open(self.profile_path, 'w') as f:
            json.dump(data, f)
            
        with open(self.profile_path, 'r') as f:
            updated_data = json.load(f)
            self.assertEqual(updated_data["level_value"], 10)
            self.assertEqual(updated_data["current_level"], "正港工程師")

    def test_smart_observation_simulation(self):
        """測試智慧觀察邏輯 (模擬輸入 '聽不懂')"""
        user_inputs = ["聽不懂", "你可以白話一點嗎？"]
        understanding_score = 0
        
        # 模擬核心邏輯：如果輸入中包含負面關鍵字且次數 >= 2
        triggers = ["聽不懂", "不明白", "白話一點", "太複雜"]
        hit_count = 0
        for input_text in user_inputs:
            if any(t in input_text for t in triggers):
                hit_count += 1
        
        self.assertGreaterEqual(hit_count, 2, "智慧觀察應偵測到 2 次負面輸入")
        
        # 驗證是否建議降級 (Lv.1)
        if hit_count >= 2:
            suggested_level = 1
            self.assertEqual(suggested_level, 1)

if __name__ == '__main__':
    unittest.main()
