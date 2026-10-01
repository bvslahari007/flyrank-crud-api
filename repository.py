import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class TaskRepository:
    def get_all_tasks(self):
        pass

    def get_task_by_id(self, task_id):
        pass

    def create_task(self, task_create):
        pass

    def update_task(self, task_id, up_task):
        pass

    def delete_task(self, task_id):
        pass


class PostgresRepository(TaskRepository):
    def __init__(self):  # this is used to assign values to object vars
        self.conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )

    def get_all_tasks(self):
        cur = self.conn.cursor()
        query = "SELECT * FROM tasks"
        cur.execute(query)
        res = cur.fetchall()
        cur.close()

        tasks = []
        for i in res:
            s = dict()
            s['id'] = i[0]
            s['title'] = i[1]
            s['done'] = i[2]
            tasks.append(s)
        return tasks

    def get_task_by_id(self, task_id):
        cur = self.conn.cursor()
        query = "SELECT * FROM tasks WHERE id = %s;"
        cur.execute(query, (task_id,))
        res = cur.fetchone()
        cur.close()

        if res is None:
            return None

        s = dict()
        s['id'] = res[0]
        s['title'] = res[1]
        s['done'] = res[2]
        return s

    def create_task(self, task_create):
        cur = self.conn.cursor()
        query = "INSERT INTO tasks (title) VALUES (%s) RETURNING id;"
        cur.execute(query, (task_create.title,))
        new_id = cur.fetchone()[0]
        self.conn.commit()
        cur.close()

        return {
            "id": new_id,
            "title": task_create.title,
            "done": False
        }
	
    def update_task(self, task_id, up_task):
        cur = self.conn.cursor()
        existing = self.get_task_by_id(task_id)

        if existing is None:
            cur.close()
            return None

        new_title = up_task.title if up_task.title is not None else existing["title"]
        new_done = up_task.done if up_task.done is not None else existing["done"]

        query = "UPDATE tasks SET title = %s, done = %s WHERE id = %s;"
        cur.execute(query, (new_title, new_done, task_id))
        self.conn.commit()
        cur.close()

        return {"id": task_id, "title": new_title, "done": new_done}

    def delete_task(self, task_id):
        exist = self.get_task_by_id(task_id)
        if exist is None:
            return None
        cur = self.conn.cursor()
        query = "DELETE FROM tasks WHERE id = %s;"
        cur.execute(query, (task_id,))
        self.conn.commit()
        cur.close()
        return {"deleted_id": task_id}
