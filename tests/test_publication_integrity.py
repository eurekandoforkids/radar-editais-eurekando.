"""Checks for publication data without network access or production mutation."""
import json
from datetime import date
from pathlib import Path
import unittest
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

class PublicationIntegrity(unittest.TestCase):
    def test_catalogs_are_unique_and_traceable(self):
        items=[]
        for file in ("editais.json","triagem.json"):
            entries=json.loads((ROOT/"data"/file).read_text(encoding="utf-8"))
            self.assertIsInstance(entries,list,file)
            ids=set()
            for item in entries:
                with self.subTest(file=file, id=item.get("id")):
                    self.assertTrue(isinstance(item.get("id"),str) and item["id"].strip())
                    self.assertNotIn(item["id"],ids)
                    ids.add(item["id"])
                    self.assertTrue(isinstance(item.get("title"),str) and item["title"].strip())
                    self.assertTrue(isinstance(item.get("institution"),str) and item["institution"].strip())
                    source=urlparse(item.get("url",""))
                    self.assertEqual(source.scheme,"https")
                    self.assertTrue(source.netloc)
                    if item.get("deadline") is not None:
                        date.fromisoformat(item["deadline"])
            items.extend(entries)
        self.assertEqual(len({x["id"] for x in items}),len(items),"ID duplicado entre triagem e editais")

    def test_fontes_oficiais_maintained(self):
        doc=(ROOT/"docs"/"fontes-oficiais.md").read_text(encoding="utf-8")
        self.assertIn("https://pncp.gov.br/",doc)
        self.assertIn("https://procurement-notices.undp.org/",doc)

if __name__=="__main__":
    unittest.main()
