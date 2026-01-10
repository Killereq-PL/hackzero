from datetime import datetime
import sqlite3
import json
import os

class AppsDB():
    def __init__(self, path='apps/app.db', schema_path='schema/app_schema.sql'):
        self.conn = sqlite3.connect(path)  # Creates a new database file if it doesn’t exist
        self.cursor = self.conn.cursor()
        self._db_setup(schema_path)
    
    def _db_setup(self, schema_path):
        """Initialize db schema"""
        with open(schema_path, 'r') as f:
            self.cursor.executescript(f.read())
        self.conn.commit()
    
    def install_app(self, name, description, category, path, author="Unknown", version="1.0", icon_path=None):
        """Install application to db"""
        sql = """
        INSERT INTO apps (name, description, category, author, version, icon_path, path, updated_at, last_used_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        now = datetime.now().isoformat()
        self.cursor.execute(sql, (name, description, category, author, version, icon_path, path, now, now))
        self.conn.commit()
        return self.cursor.lastrowid

    def store_executable(self, app_id, option_name=None, path=None, execution_type=None, instructions=None):
        """Store executable information"""
        sql = """
        INSERT INTO executable_info 
        (app_id, option_name, path, execution_type, instructions)
        VALUES (?, ?, ?, ?, ?)
        """
        now = datetime.now().isoformat()
        self.cursor.execute(sql, (
            app_id, option_name, path, execution_type, instructions
        ))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_app_info(self, app_id):
        """Get app information"""
        sql = "SELECT * FROM apps WHERE id = ?"
        self.cursor.execute(sql, (app_id,))
        return self.cursor.fetchone()

    def get_executable_info(self, app_id):
        """Get executable information"""
        sql = "SELECT * FROM executable_info WHERE app_id = ?"
        self.cursor.execute(sql, (app_id,))
        return self.cursor.fetchone()
    
    def get_apps(self):
        """Get all apps"""
        sql = "SELECT * FROM apps"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def install_app_from_manifest(self, path):
        """Install app from manifest file"""
        try:
            with open(path, 'r') as f:
                manifest: dict = json.load(f)
                m_app: dict = manifest.get("app", {})
                app_id = self.install_app(
                    name=m_app.get("name", "Unnamed App"),
                    description=m_app.get("description", ""),
                    category=m_app.get("category", None),
                    author=m_app.get("author", "Unknown"),
                    version=m_app.get("version", "1.0"),
                    icon_path=m_app.get("icon_path", None),
                    path=os.path.dirname(path)
                )
                m_exes: list = manifest.get("executables", [])
                for m_exe in m_exes:
                    self.store_executable(
                        app_id=app_id,
                        option_name=m_exe.get("option_name", None),
                        path=m_exe.get("path", "/"),
                        execution_type=m_exe.get("execution_type", "shell"),
                        instructions=m_exe.get("instructions", "")
                    )
                return app_id
        except OSError as e:
            print(f"Manifest missing <{e}>")

if __name__ == "__main__":
    db = AppsDB('D:/Github/hackzero/apps/app.db', 'D:/Github/hackzero/schema/app_schema.sql')
    
    i = input("Install Timer app? (y/n): ")
    
    if i.lower() == 'y':
        app_id = db.install_app_from_manifest('D:/Github/hackzero/apps/Timer/manifest.json')
        print(f"Installed Timer app with ID: {app_id}")
    else:
        app_id = int(input("Enter app ID to fetch: "))
        app_info = db.get_app_info(app_id)
        exec_info = db.get_executable_info(app_id)
        print("App Info:", app_info)
        print("Executable Info:", exec_info)