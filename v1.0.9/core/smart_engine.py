"""
智能规则引擎 - Smart Rules Engine
实现类似AI的文件自动分类功能
"""
import os
import re
import json
from pathlib import Path


class SmartRuleEngine:
    """智能文件分类规则引擎"""

    # 预设的智能分类区域（Apple 标准色系）
    DEFAULT_ZONES = {
        "工作区域": {
            "description": "办公、文档、项目相关",
            "color": "#0A84FF",
            "icon": "💼",
            "rules": [
                {"type": "extension", "value": [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".rtf", ".csv", ".md"]},
                {"type": "extension", "value": [".psd", ".ai", ".fig", ".sketch", ".xd"]},
                {"type": "extension", "value": [".py", ".js", ".ts", ".java", ".cpp", ".c", ".h", ".go", ".rs", ".html", ".css", ".vue", ".jsx", ".tsx"]},
                {"type": "name_keyword", "value": ["工作", "项目", "报告", "方案", "合同", "发票", "报销", "会议", "简历", "面试", "需求", "设计", "需求", "总结"]},
                {"type": "path_keyword", "value": ["work", "project", "工作", "项目"]},
            ]
        },
        "娱乐区域": {
            "description": "游戏、视频、音乐、娱乐",
            "color": "#FF375F",
            "icon": "🎮",
            "rules": [
                {"type": "extension", "value": [".exe", ".msi", ".apk", ".ipa", ".iso", ".rom"]},
                {"type": "extension", "value": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"]},
                {"type": "extension", "value": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"]},
                {"type": "name_keyword", "value": ["游戏", "game", "电影", "movie", "音乐", "music", "视频", "video", "娱乐", "番剧", "动漫", "演唱会", "screenshot", "截图"]},
                {"type": "path_keyword", "value": ["game", "游戏", "steam", "epic", "movie", "电影", "music", "音乐", "videos", "视频"]},
            ]
        },
        "学习区域": {
            "description": "学习资料、教程、书籍",
            "color": "#30D158",
            "icon": "📚",
            "rules": [
                {"type": "extension", "value": [".epub", ".mobi", ".azw", ".azw3", ".pdf"]},
                {"type": "name_keyword", "value": ["教程", "课程", "学习", "考试", "笔记", "作业", "论文", "课件", "课本", "教材", "learn", "course", "tutorial"]},
                {"type": "path_keyword", "value": ["学习", "learn", "course", "教程", "课程"]},
            ]
        },
        "图片区域": {
            "description": "图片、照片、壁纸",
            "color": "#FF9F0A",
            "icon": "🖼️",
            "rules": [
                {"type": "extension", "value": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".ico", ".tiff", ".raw", ".heic"]},
            ]
        },
        "下载区域": {
            "description": "刚下载的文件、安装包",
            "color": "#BF5AF2",
            "icon": "📦",
            "rules": [
                {"type": "extension", "value": [".zip", ".rar", ".7z", ".tar", ".gz"]},
                {"type": "extension", "value": [".exe", ".msi", ".apk", ".dmg", ".pkg"]},
                {"type": "name_keyword", "value": ["download", "下载", "install", "安装", "setup"]},
                {"type": "path_keyword", "value": ["download", "下载"]},
            ]
        },
        "临时文件": {
            "description": "缓存、临时文件、日志",
            "color": "#8E8E93",
            "icon": "🗑️",
            "rules": [
                {"type": "extension", "value": [".tmp", ".temp", ".log", ".crdownload", ".part", ".cache", ".bak", ".old"]},
                {"type": "name_keyword", "value": ["~$", ".tmp", "副本"]},
            ]
        }
    }

    # 扩展名 -> 更智能的判断
    GAME_KEYWORDS = {
        'game', 'games', 'gaming', '游戏', 'steam', 'epic', 'origin', 'uplay',
        'minecraft', 'lol', 'league', '原神', '王者', '吃鸡', 'pubg', 'csgo',
        'cod', '刺客信条', '刺客教條', 'assassin', 'gta', 'need for speed',
        '极品飞车', 'fifa', 'nba', '实况', '模拟', 'sim', 'strategy', '策略'
    }

    WORK_KEYWORDS = {
        'work', 'project', 'report', 'proposal', 'contract', 'invoice',
        'meeting', 'resume', 'cv', 'interview', 'requirement', 'design',
        'spec', 'summary', 'review', 'plan', 'budget', '财务', '报表'
    }

    STUDY_KEYWORDS = {
        'learn', 'study', 'course', 'tutorial', 'exam', 'homework',
        'assignment', 'thesis', 'paper', 'note', 'lecture', 'textbook',
        '英语', '数学', '物理', '化学', '语文', '历史', '地理', '政治'
    }

    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(
                os.path.expanduser('~'), '.nexus_dock', 'smart_rules.json'
            )
        self.config_path = config_path
        self.custom_zones = {}
        self._load_config()

    def _load_config(self):
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.custom_zones = data.get('zones', {})
        except Exception:
            self.custom_zones = {}

    def _save_config(self):
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump({'zones': self.custom_zones}, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def get_all_zones(self):
        """获取所有分类区域（包括自定义）"""
        zones = dict(self.DEFAULT_ZONES)
        zones.update(self.custom_zones)
        return zones

    def add_custom_zone(self, name, description, color, icon, rules):
        """添加自定义分类区域"""
        self.custom_zones[name] = {
            'description': description,
            'color': color,
            'icon': icon,
            'rules': rules
        }
        self._save_config()

    def remove_custom_zone(self, name):
        """删除自定义分类区域"""
        if name in self.custom_zones:
            del self.custom_zones[name]
            self._save_config()

    def classify(self, filepath):
        """
        智能分类文件到对应的区域
        返回: (zone_name, confidence)
        zone_name 为 None 表示无法分类
        confidence 为 0-1 的置信度
        """
        filename = os.path.basename(filepath)
        name_lower = filename.lower()
        ext = os.path.splitext(filename)[1].lower()
        dirpath = os.path.dirname(filepath).lower()

        zones = self.get_all_zones()

        best_zone = None
        best_score = 0

        for zone_name, zone_config in zones.items():
            score = 0
            rules = zone_config.get('rules', [])

            for rule in rules:
                rule_type = rule.get('type')
                rule_value = rule.get('value', [])

                if rule_type == 'extension':
                    if ext in rule_value:
                        score += 3

                elif rule_type == 'name_keyword':
                    for keyword in rule_value:
                        if keyword.lower() in name_lower:
                            score += 2
                            break

                elif rule_type == 'path_keyword':
                    for keyword in rule_value:
                        if keyword.lower() in dirpath:
                            score += 1.5
                            break

            # 额外的智能判断
            extra_score = self._smart_extra_check(filename, ext, zone_name)
            score += extra_score

            if score > best_score:
                best_score = score
                best_zone = zone_name

        # 计算置信度
        if best_score > 0:
            confidence = min(best_score / 8.0, 1.0)
        else:
            confidence = 0

        if best_score >= 1.5:  # 阈值
            return best_zone, confidence
        else:
            return None, 0

    def _smart_extra_check(self, filename, ext, zone_name):
        """额外的智能判断规则"""
        name_lower = filename.lower()
        score = 0

        if zone_name == "娱乐区域":
            # 游戏相关关键词
            for kw in self.GAME_KEYWORDS:
                if kw in name_lower:
                    score += 2
                    break

        elif zone_name == "工作区域":
            for kw in self.WORK_KEYWORDS:
                if kw in name_lower:
                    score += 2
                    break

            # 文件名包含日期格式（如 2024-01-15 报告）
            if re.search(r'\d{4}[-_.]\d{1,2}[-_.]\d{1,2}', name_lower):
                score += 1

        elif zone_name == "学习区域":
            for kw in self.STUDY_KEYWORDS:
                if kw in name_lower:
                    score += 2
                    break

        # 安装包判断
        if zone_name == "下载区域":
            if ext in {'.exe', '.msi', '.apk'}:
                score += 1
            if 'setup' in name_lower or 'install' in name_lower:
                score += 1

        return score

    def classify_batch(self, filepaths):
        """批量分类文件"""
        results = {}
        for filepath in filepaths:
            zone, confidence = self.classify(filepath)
            results[filepath] = {
                'zone': zone,
                'confidence': confidence
            }
        return results

    def get_zone_files(self, zone_name, all_files_info):
        """获取某个区域下的所有文件"""
        result = []
        for filepath, info in all_files_info.items():
            zone, _ = self.classify(filepath)
            if zone == zone_name:
                result.append(info)
        return result

    def suggest_zone_for_file(self, filepath):
        """为文件推荐可能的分类（显示前3个最可能的）"""
        filename = os.path.basename(filepath)
        name_lower = filename.lower()
        ext = os.path.splitext(filename)[1].lower()
        dirpath = os.path.dirname(filepath).lower()

        zones = self.get_all_zones()
        scores = []

        for zone_name, zone_config in zones.items():
            score = 0
            rules = zone_config.get('rules', [])

            for rule in rules:
                rule_type = rule.get('type')
                rule_value = rule.get('value', [])

                if rule_type == 'extension' and ext in rule_value:
                    score += 3
                elif rule_type == 'name_keyword':
                    for keyword in rule_value:
                        if keyword.lower() in name_lower:
                            score += 2
                            break
                elif rule_type == 'path_keyword':
                    for keyword in rule_value:
                        if keyword.lower() in dirpath:
                            score += 1.5
                            break

            score += self._smart_extra_check(filename, ext, zone_name)
            if score > 0:
                scores.append((zone_name, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:3]
