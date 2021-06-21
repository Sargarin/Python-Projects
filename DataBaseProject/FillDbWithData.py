class insertData():

    def __init__(self, conn) -> None:
        self.conn = conn

    def insertDataIntoGunCategory(self, idNumber, categoryName):
        cur = self.conn.cursor()
        cur.execute(f"INSERT OR REPLACE INTO gun_category (category_id,category_name) VALUES ({idNumber},'{categoryName}')")

    def insertDataIntoProducent(self, idNumber, producent_country):
        cur = self.conn.cursor()
        cur.execute(f"INSERT OR REPLACE  INTO producent (producent_id,producent_country) VALUES ({idNumber},'{producent_country}')")

    def insertDataIntoAmmoType(self, idNumber, ammo_type_type):
        cur = self.conn.cursor()
        cur.execute(f"INSERT OR REPLACE INTO ammo_type (ammo_type_id,ammo_type_type) VALUES ({idNumber},'{ammo_type_type}')")

    def insertDataIntoGuns(self, idNumber, gun_name, gun_category_category_id, producent_producent_id,
                           ammo_type_ammo_type_id):
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT OR REPLACE INTO guns (gun_id,gun_name,gun_category_category_id,producent_producent_id,ammo_type_ammo_type_id) "
            f"VALUES ({idNumber},'{gun_name}','{gun_category_category_id}','{producent_producent_id}','{ammo_type_ammo_type_id}')")

    def insertDataIntoFrontGrips(self, front_grips_id, front_grips_name):
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT OR REPLACE INTO front_grips (front_grips_id,front_grips_name) VALUES ({front_grips_id},'{front_grips_name}')")

    def insertDataIntoMuzzleDevices(self, muzzle_id, muzzle_devices_name):
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT OR REPLACE INTO muzzle_devices (muzzle_id,muzzle_devices_name) VALUES ({muzzle_id},'{muzzle_devices_name}')")

    def insertDataIntoGunMuzzleRelation(self, guns_gun_id, muzzle_devices_muzzle_id):
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT OR REPLACE INTO gun_muz_rel (guns_gun_id,muzzle_devices_muzzle_id) VALUES ({guns_gun_id},'{muzzle_devices_muzzle_id}')")

    def insertDataIntoGunGripRelation(self, guns_gun_id, front_grips_front_grips_id):
        cur = self.conn.cursor()
        cur.execute(
            f"INSERT OR REPLACE INTO gun_gri_rel (guns_gun_id,front_grips_front_grips_id) VALUES ({guns_gun_id},'{front_grips_front_grips_id}')")


def fillDbWithDataAndRepeat(conn):
    insert = insertData(conn)

    insert.insertDataIntoGunCategory(1, 'Assault carabines')
    insert.insertDataIntoGunCategory(2, 'Assault rifles')
    insert.insertDataIntoGunCategory(3, 'Bolt-action rifles')
    insert.insertDataIntoGunCategory(4, 'Marksman rifles')

    insert.insertDataIntoProducent(1, 'Russia')
    insert.insertDataIntoProducent(2, 'United States')

    insert.insertDataIntoAmmoType(1, '9x39')
    insert.insertDataIntoAmmoType(2, '366TKM')
    insert.insertDataIntoAmmoType(3, '5.45x39')
    insert.insertDataIntoAmmoType(4, '5.56x45')
    insert.insertDataIntoAmmoType(5, '7.62x39')
    insert.insertDataIntoAmmoType(6, '7.62x51')
    insert.insertDataIntoAmmoType(7, '7.62x54R')

    insert.insertDataIntoFrontGrips(1, 'Fortis shift tactical grip')
    insert.insertDataIntoFrontGrips(2, 'Hera arms CQR tactical grip')
    insert.insertDataIntoFrontGrips(3, 'Magpul AFG grip')
    insert.insertDataIntoFrontGrips(4, 'Magpul RVG grip')
    insert.insertDataIntoFrontGrips(5, 'Zenit RK-1 foregrip')

    insert.insertDataIntoMuzzleDevices(1, 'AAC Blackout 51T 5.56x45 flash-hider')
    insert.insertDataIntoMuzzleDevices(2, 'Lantac dragon 7.62x51 muzzle brake')
    insert.insertDataIntoMuzzleDevices(3, 'PWS CQB 5.56X45 muzzle brake')
    insert.insertDataIntoMuzzleDevices(4, 'Rotor 43 6.72x39 muzzle brake')
    insert.insertDataIntoMuzzleDevices(5, 'Thunder beast 30CB Muzzle brake 7.62x51')

    for i in range(0, 10000, 20):

        insert.insertDataIntoGuns(1 + i, 'Adar 2-15 .223 Carabine' + f"Series: {i}", 1, 1, 4)
        insert.insertDataIntoGuns(2 + i, 'Kel-tec RFB 7.62x51' + f"Series: {i}", 1, 2, 6)
        insert.insertDataIntoGuns(3 + i, 'Lone star tx-15 DML rifle' + f"Series: {i}", 1, 2, 4)
        insert.insertDataIntoGuns(4 + i, 'Simonov Semi-Automatic Carabine SKS 7.62x39' + f"Series: {i}", 1, 1, 5)
        insert.insertDataIntoGuns(5 + i, 'Vepr AKM/VPO-209 366TKM carabine' + f"Series: {i}", 1, 1, 2)

        insert.insertDataIntoGuns(6 + i, 'AK-101 5.56x45' + f"Series: {i}", 2, 1, 4)
        insert.insertDataIntoGuns(7 + i, 'AK-103 7.62x39' + f"Series: {i}", 2, 1, 5)
        insert.insertDataIntoGuns(8 + i, 'AK-74M' + f"Series: {i}", 2, 1, 3)
        insert.insertDataIntoGuns(9 + i, 'AS VAL' + f"Series: {i}", 2, 1, 1)
        insert.insertDataIntoGuns(10 + i, 'COLT M4A1 5.56X45' + f"Series: {i}", 2, 2, 4)

        insert.insertDataIntoGuns(11 + i, 'DVL-10 saboteur sniper rifle' + f"Series: {i}", 3, 1, 6)
        insert.insertDataIntoGuns(12 + i, 'Mosin bolt-action sniper rifle' + f"Series: {i}", 3, 1, 7)
        insert.insertDataIntoGuns(13 + i, 'Orsis T-5000 .308' + f"Series: {i}", 3, 1, 6)
        insert.insertDataIntoGuns(14 + i, 'Remington model 700' + f"Series: {i}", 3, 2, 6)
        insert.insertDataIntoGuns(15 + i, 'SV-98 bolt-action sniper rifle' + f"Series: {i}", 3, 1, 7)

        insert.insertDataIntoGuns(16 + i, 'Knight armament company SR-25' + f"Series: {i}", 4, 2, 6)
        insert.insertDataIntoGuns(17 + i, 'Remington R11 RSASS ' + f"Series: {i}", 4, 2, 6)
        insert.insertDataIntoGuns(18 + i, 'SVDS' + f"Series: {i}", 4, 1, 7)
        insert.insertDataIntoGuns(19 + i, 'Special sniper rifle VSS vintorez' + f"Series: {i}", 4, 1, 1)
        insert.insertDataIntoGuns(20 + i, 'Springfield armory M1A' + f"Series: {i}", 4, 2, 6)

        insert.insertDataIntoGunMuzzleRelation(1 + i, 1)
        insert.insertDataIntoGunMuzzleRelation(2 + i, 1)
        insert.insertDataIntoGunMuzzleRelation(6 + i, 1)
        insert.insertDataIntoGunMuzzleRelation(2 + i, 2)
        insert.insertDataIntoGunMuzzleRelation(13 + i, 2)
        insert.insertDataIntoGunMuzzleRelation(8 + i, 3)
        insert.insertDataIntoGunMuzzleRelation(7 + i, 3)
        insert.insertDataIntoGunMuzzleRelation(8 + i, 4)
        insert.insertDataIntoGunMuzzleRelation(4 + i, 4)
        insert.insertDataIntoGunMuzzleRelation(20 + i, 5)
        insert.insertDataIntoGunMuzzleRelation(6 + i, 5)
        insert.insertDataIntoGunMuzzleRelation(10 + i, 5)
        insert.insertDataIntoGunMuzzleRelation(1 + i, 5)

        insert.insertDataIntoGunGripRelation(1 + i, 2)
        insert.insertDataIntoGunGripRelation(10 + i, 2)
        insert.insertDataIntoGunGripRelation(17 + i, 2)

        for j in range(1, 21):
            insert.insertDataIntoGunGripRelation(j + i, 1)
            insert.insertDataIntoGunGripRelation(j + i, 3)
            insert.insertDataIntoGunGripRelation(j + i, 4)
            insert.insertDataIntoGunGripRelation(j + i, 5)

    conn.commit()
