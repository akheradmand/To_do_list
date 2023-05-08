import sqlite3


class Database:
    def __init__(self):
        self.con=sqlite3.connect("todo_list.db")
        self.cursor=self.con.cursor()

    def get_tasks(self):
        query="SELECT * FROM tasks ORDER BY is_done ASC"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks
    
    def add_new_task(self,new_title,new_description,priority,new_date,new_time):
        # khali nabudan e title؟؟؟؟؟
        try:
            query=f"INSERT INTO tasks(title, description, priority, date, time) VALUES('{new_title}','{new_description}','{priority}','{new_date}','{new_time}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def remove_task(self,id):
        try:
            query=f"DELETE FROM tasks WHERE id='{id}'"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def task_done(self,id):
        query=f"UPDATE tasks SET is_done=1 WHERE id='{id}'"
        self.cursor.execute(query)
        self.con.commit()