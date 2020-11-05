# -*- coding: utf-8 -*-

__version__ = "1.0"

import sqlite3

conexion = sqlite3.connect("DB_SIACLE.db")

cursor = conexion.cursor()

except sqlite3.Error as error:
    print("Error: {}".format(error))

conexion.close()
