import hibpwned

my_app = hibpwned.Pwned("wiest@hm.edu", "My_App", "apikey")

my_breaches = my_app.search_all_breaches()
breaches = my_app.all_breaches()
adobe = my_app.single_breach("adobe")
data = my_app.data_classes()
my_pastes = my_app.search_pastes()
password = my_app.search_password("BadPassword")
my_hashes = my_app.search_hashes("21BD1")
