def DbGenFunction():
    statements = [
        '''
        PRAGMA foreign_keys = ON;
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "ammo_properties" (
        "ammo_type_id"           NUMBER NOT NULL,
        "ammo_type_name"        TEXT NOT NULL,
        "ammo_type_penetration"  NUMBER(2),
        "ammo_type_damage"       NUMBER(3),
        PRIMARY KEY("ammo_type_id")
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "ammo_type" (
        "ammo_type_id"    NUMBER NOT NULL,
        "ammo_type_type"  TEXT NOT NULL,
        PRIMARY KEY("ammo_type_id")
        );
        ''',

        '''
        DROP TABLE ammo_properties;
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "ammo_properties" (
        "ammo_type_id"           NUMBER NOT NULL,
        "ammo_type_name"        TEXT NOT NULL,
        "ammo_type_penetration"  NUMBER(2),
        "ammo_type_damage"       NUMBER(3),
        PRIMARY KEY("ammo_type_id"),
        FOREIGN KEY("ammo_type_id") REFERENCES "ammo_type" ("ammo_type_id")
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "front_grips" (
        "front_grips_id"   NUMBER NOT NULL,
        "front_grips_name"  TEXT NOT NULL,
        PRIMARY KEY("front_grips_id")
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "gun_category" (
        "category_id"    NUMBER NOT NULL,
        "category_name"  TEXT NOT NULL,
        PRIMARY KEY("category_id")
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "gun_gri_rel" (
        "guns_gun_id"                 NUMBER NOT NULL,
        "front_grips_front_grips_id"  NUMBER NOT NULL,
        PRIMARY KEY("guns_gun_id","front_grips_front_grips_id")
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "gun_muz_rel" (
        "guns_gun_id"               NUMBER NOT NULL,
        "muzzle_devices_muzzle_id"  NUMBER NOT NULL,
        PRIMARY KEY("guns_gun_id","muzzle_devices_muzzle_id")
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "guns" (
        "gun_id"                    NUMBER NOT NULL,
        "gun_name"                  TEXT NOT NULL,
        "gun_category_category_id"  NUMBER NOT NULL,
        "producent_producent_id"    NUMBER NOT NULL,
        "ammo_type_ammo_type_id"    NUMBER NOT NULL,
        PRIMARY KEY(gun_id)
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "muzzle_devices" (
        "muzzle_id"            NUMBER NOT NULL,
        "muzzle_devices_name"  TEXT NOT NULL,
        PRIMARY KEY("muzzle_id")
        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "producent" (
        "producent_id"       NUMBER NOT NULL,
        "producent_country"  TEXT NOT NULL NOT NULL,
        PRIMARY KEY ("producent_id")
        );
        ''',

        '''
        DROP TABLE gun_gri_rel;
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "gun_gri_rel" (
        "guns_gun_id"                 NUMBER NOT NULL,
        "front_grips_front_grips_id"  NUMBER NOT NULL,
        PRIMARY KEY("guns_gun_id","front_grips_front_grips_id"),
        FOREIGN KEY("front_grips_front_grips_id") REFERENCES "front_grips" ("front_grips_id"),
        FOREIGN KEY("guns_gun_id") REFERENCES "guns" ("gun_id")
        );
        ''',

        '''
        DROP TABLE gun_muz_rel;
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "gun_muz_rel" (
        "guns_gun_id"               NUMBER NOT NULL,
        "muzzle_devices_muzzle_id"  NUMBER NOT NULL,
        PRIMARY KEY("guns_gun_id","muzzle_devices_muzzle_id"),
        FOREIGN KEY("guns_gun_id") REFERENCES "guns" ("gun_id"),
        FOREIGN KEY("muzzle_devices_muzzle_id") REFERENCES "muzzle_devices" ("muzzle_id")
        );
        ''',

        '''
        DROP TABLE guns;
        ''',

        '''
        CREATE TABLE IF NOT EXISTS "guns" (
        "gun_id"                    NUMBER NOT NULL,
        "gun_name"                  TEXT NOT NULL,
        "gun_category_category_id"  NUMBER NOT NULL,
        "producent_producent_id"    NUMBER NOT NULL,
        "ammo_type_ammo_type_id"    NUMBER NOT NULL,
        PRIMARY KEY(gun_id),
        FOREIGN KEY("ammo_type_ammo_type_id") REFERENCES "ammo_type" ("ammo_type_id"),
        FOREIGN KEY("gun_category_category_id") REFERENCES "gun_category" ("category_id"),
        FOREIGN KEY("producent_producent_id") REFERENCES "producent" ("producent_id")
        );
        ''']
    return statements
