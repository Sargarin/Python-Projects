import sqlite3
import time


def connect(name):
    try:
        conn = sqlite3.connect(name)
    except:
        print("Error")
        conn.close()
    else:
        print("Connection succesful: ", name)
    return conn


class Queries:
    def __init__(self, conn):
        self.conn = conn
        self.curr = self.conn.cursor()

    def query1(self):
        start = time.perf_counter()
        print(
            "Starting query1, this query is able to create a compare table between witch front grip attachments are used by witch guns ")
        self.curr.execute(
            f"SELECT front_grips_name,guns.gun_name FROM front_grips INNER JOIN gun_gri_rel ON "
            f"front_grips.front_grips_id = gun_gri_rel.front_grips_front_grips_id "
            f"INNER JOIN guns ON gun_gri_rel.guns_gun_id = guns.gun_id ORDER BY front_grips.front_grips_name")
        end = time.perf_counter() - start

    def query2(self):
        start = time.perf_counter()
        print(
            "Starting query2, this query is able to create a compare table between witch muzzle attachments are used by witch guns ")
        self.curr.execute(
            f"SELECT muzzle_devices_name, guns.gun_name FROM muzzle_devices "
            f"INNER JOIN gun_muz_rel ON muzzle_devices.muzzle_id = gun_muz_rel.muzzle_devices_muzzle_id "
            f"INNER JOIN guns ON gun_muz_rel.guns_gun_id = guns.gun_id ORDER BY muzzle_devices.muzzle_devices_name")
        end = time.perf_counter() - start

    def query3(self):
        start = time.perf_counter()
        print(
            "Starting query3, this query is able to create Full information table about guns in DB ")
        self.curr.execute(
            f"SELECT gun_name,category_name,producent_country,ammo_type_type FROM guns "
            f"INNER JOIN producent ON guns.producent_producent_id = producent.producent_id "
            f"INNER JOIN ammo_type ON guns.ammo_type_ammo_type_id = ammo_type.ammo_type_id "
            f"INNER JOIN gun_category ON guns.gun_category_category_id = gun_category.category_id "
            f"ORDER BY guns.gun_name")
        end = time.perf_counter() - start

    def query4(self):
        start = time.perf_counter()
        print("Starting query4, this query is able to create table of gun models produced in russia ")
        self.curr.execute(
            f"SELECT guns.gun_name FROM guns WHERE guns.producent_producent_id "
            f"IN (SELECT producent.producent_id FROM producent WHERE producent.producent_id = 1)")
        end = time.perf_counter() - start

    def query5(self):
        start = time.perf_counter()
        print("Starting query5, this query is able to create table of gun models produced in russia via diffrent query")
        self.curr.execute(
            f"SELECT guns.gun_name FROM guns INNER JOIN producent "
            f"ON guns.producent_producent_id = producent.producent_id WHERE producent_producent_id = 1")
        end = time.perf_counter() - start

    def query1E(self):
        start = time.perf_counter()
        print(
            "Starting query1 with EXPLAIN and show, this query is able to create a compare table between witch front grip attachments are used by witch guns ")
        testTable = self.curr.execute(
            f"EXPLAIN SELECT front_grips_name,guns.gun_name FROM front_grips INNER JOIN gun_gri_rel ON "
            f"front_grips.front_grips_id = gun_gri_rel.front_grips_front_grips_id "
            f"INNER JOIN guns ON gun_gri_rel.guns_gun_id = guns.gun_id ORDER BY front_grips.front_grips_name")
        end = time.perf_counter() - start
        for row in testTable:
            print(row)

    def query2E(self):
        start = time.perf_counter()
        print(
            "Starting query2 with EXPLAIN and show , this query is able to create a compare table between witch muzzle attachments are used by witch guns ")
        testTable = self.curr.execute(
            f"EXPLAIN SELECT muzzle_devices_name, guns.gun_name FROM muzzle_devices "
            f"INNER JOIN gun_muz_rel ON muzzle_devices.muzzle_id = gun_muz_rel.muzzle_devices_muzzle_id "
            f"INNER JOIN guns ON gun_muz_rel.guns_gun_id = guns.gun_id ORDER BY muzzle_devices.muzzle_devices_name")
        end = time.perf_counter() - start
        for row in testTable:
            print(row)

    def query3E(self):
        start = time.perf_counter()
        print(
            "Starting query3 with EXPLAIN and show ,this query is able to create Full information table about guns in DB")
        testTable = self.curr.execute(
            f"EXPLAIN SELECT gun_name,category_name,producent_country,ammo_type_type FROM guns "
            f"INNER JOIN producent ON guns.producent_producent_id = producent.producent_id "
            f"INNER JOIN ammo_type ON guns.ammo_type_ammo_type_id = ammo_type.ammo_type_id "
            f"INNER JOIN gun_category ON guns.gun_category_category_id = gun_category.category_id "
            f"ORDER BY guns.gun_name")
        end = time.perf_counter() - start
        for row in testTable:
            print(row)

    def query4E(self):
        start = time.perf_counter()
        print(
            "Starting query4 with EXPLAIN, this query is able to create table of gun models produced in russia ")
        testTable = self.curr.execute(
            f"EXPLAIN SELECT guns.gun_name FROM guns WHERE guns.producent_producent_id "
            f"IN (SELECT producent.producent_id FROM producent WHERE producent.producent_id = 1)")
        end = time.perf_counter() - start
        for row in testTable:
            print(row)

    def query5E(self):
        start = time.perf_counter()
        print(
            "Starting query5 with EXPLAIN, this query is able to create table of gun models produced in russia via diffrent query")
        testTable = self.curr.execute(
            f"EXPLAIN SELECT guns.gun_name FROM guns INNER JOIN producent "
            f"ON guns.producent_producent_id = producent.producent_id WHERE producent_producent_id = 1")
        end = time.perf_counter() - start
        for row in testTable:
            print(row)
