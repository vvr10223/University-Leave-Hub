import mysql.connector as con
import os
class db:

  def __init__(self):
    self.planetscaledb = con.connect(
      host=os.environ['planetscaledbhost'],
      user=os.environ['planetscaledbuser'],
      password=os.environ['planetscaledbpasswd'],
      database=os.environ['planetscaledbname'])

  def cursorcon(self):
    self.pscur = self.planetscaledb.cursor(dictionary=True)
    return self.pscur

  def fun(self):
    cur = self.cursorcon()
    cur.execute("select * from jobs")
    result = cur.fetchall()
    return result

  def loadjob(self, id):
    cur = self.cursorcon()
    cur.execute(f'select * from jobs where id={id}')
    result = cur.fetchone()

    return result

  def apptodb(self, id, data):
    cur = self.cursorcon()
    text = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    d = list(data.values())
    d.insert(0, id)

    cur.execute(text, d)
    self.planetscaledb.commit()


if __name__ == "__main__":
  d = db()
  a = d.loadjob(2)
  print(a)