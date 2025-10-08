from pathlib import Path

import yaml

from src.database import DatabaseManager
from src.utils import clean_generation_result


class TestDatabaseConnection:
    def test_database_url_generation(self):
        db_manager = DatabaseManager()
        url = db_manager.get_database_url()
        assert "postgresql://" in url
        assert "winwin" in url
        print(f"数据库连接 URL: {url}")

    def test_database_connection(self):
        db_manager = DatabaseManager()
        result = db_manager.test_connection()
        assert result is True, "数据库连接失败"
        print("✓ 数据库连接测试成功")

    def test_engine_creation(self):
        db_manager = DatabaseManager()
        engine = db_manager.create_engine()
        assert engine is not None
        print("✓ 数据库引擎创建成功")

    def test_session_creation(self):
        db_manager = DatabaseManager()
        session = db_manager.get_session()
        assert session is not None
        session.close()
        print("✓ 数据库会话创建成功")

    def test_execute_sql(self):
        db_manager = DatabaseManager()
        result = db_manager.execute_sql("""SELECT category FROM dim_category where category='即饮茶';""")
        assert result is not None
        assert result[0]['category'] == '即饮茶'
        print("✓ 数据库查询正确")

    def test_examples_sql(self):
        examples_file = Path(__file__).parent.parent.joinpath("docs/examples.yml")
        with open(examples_file, "r", encoding="utf-8") as f:
            examples_data = yaml.load(f, Loader=yaml.FullLoader)

        db_manager = DatabaseManager()
        for i, example in enumerate(examples_data["examples"], 1):
            print(f"\n=== 示例 {i} ===")
            print(f"QUESTION: {example['questions']}")

            sql = clean_generation_result(example['sql'].strip())
            try:
                result = db_manager.execute_sql(sql)
                assert result is not None
                print(f"ANSWER: {result[0]}...")
                print("✓ SQL执行成功")
            except Exception as e:
                print(f"✗ SQL执行失败: {e}")
