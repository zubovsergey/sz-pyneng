# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('dhcp_shooping.db')

print('Creating schema...')
with open('dhcp_snooping_schema.sql', 'r') as f:
    schema = f.read()
    conn.executescript(schema)
print("Done")

conn.close()