# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('new_db.db')

cursor = connection.cursor()

cursor.executescript('''
                         create table switches(
                             hostname     text not NULL primary key,
                             location     text
                         );
                    
                         create table dhcp(
                             mac          text not NULL primary key,
                             ip           text,
                             vlan         text,
                             interface    text,
                             switch       text not null references switches(hostname)
                         );
                     ''')