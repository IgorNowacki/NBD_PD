printjson(db.people.find({"birth_date":{"$gte": ISODate('2000-12-31T00:00:00Z').toISOString()}},{"first_name":1,"last_name":1}).toArray())
