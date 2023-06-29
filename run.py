from BuyItems import BuyItems

with BuyItems() as test_samsung:
    username = "testikayttaja7"
    password = "salasana"

    test_samsung.land_first_page()
    test_samsung.sign_up(username,password)
    test_samsung.login(username,password)
    test_samsung.select_item("Samsung galaxy s6")
    test_samsung.purchase_item(["Miika","Suomi","Oulu","445 534 434 54","12","2033"])

with BuyItems() as test_nexus:
    username = "testikayttaja8"
    password = "salasana"

    test_nexus.land_first_page()
    test_nexus.sign_up(username,password)
    test_nexus.login(username,password)
    test_nexus.select_item("Nexus 6")
    test_nexus.purchase_item(["Petteri","Suomi","Rovaniemi","45 53344 434 54","12","2035"])


