Studies Database project

part 1. Create Relational DataBase show and explain all of the relations
part 2. Simulate Traffic in Database, test it and write what problems are encountered. Use multiple users using difrent things in the same time ( Threads.py)
part 3. Create Big Queries on database. Test which of them are performing better than others while doing the same thing ( QueriesAndOptimization.py)


For my Database i have used informations about various guns that i know from game Escape From Tarkov, then for testing i've multiplied them.

Data statistics:

gun categories (1:M)
ountires that produce guns (1:M)
guns (Core data)
ammunitiontypes that these guns use (1:M)
front grips that some of these guns use (M:N)
muzzle devices that some of these guns use (M:N)

also implemented table "ammo_properties" for futher expansion of DB

