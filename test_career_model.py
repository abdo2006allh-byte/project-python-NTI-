import unittest
from career_model import parse_skills, match_jobs, model_info

class TestModel(unittest.TestCase):
    def test_aliases(self):
        s=parse_skills("Python, JS, TS, ML, Postgres, React.js")
        for x in ("python","javascript","typescript","machine learning","postgresql","react"):
            self.assertIn(x,s)
    def test_index(self):
        i=model_info()
        self.assertEqual(i["fields_evaluated"],18)
        self.assertGreaterEqual(i["roles_evaluated"],78)
    def test_backend(self):
        r=match_jobs("Python, SQL, Git, REST, APIs, Docker","Backend Engineer",5)
        self.assertGreater(r["results"][0]["score"],40)
    def test_gaps(self):
        r=match_jobs("SQL, Excel","Data Analyst",1)["results"][0]
        self.assertGreater(len(r["missing"]),0)

if __name__=="__main__":
    unittest.main()
