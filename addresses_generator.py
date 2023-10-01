
# Creating a file to store these addresses
def generate_text_file():
    print("executing generate_text_file...")
    addresses = [
        "LexLive\n301 S Broadway\nLexington, KY 40508",
        "Mr. Ray L. Hyatt Jr.\n300 Rose Street Room 102 Hardymon Building\nLexington, KY 40506",
        "Mr. Ray L. Hyatt Jr.\n301 Hilltop Avenue, Room 102\nLexington, KY 40506",
        "John Wick\n82 Beaver Street Room 1301\nNew York, NY 10005",
        "Tony Stark\n200 Park Avenue, Penthouse\nNew York, NY 10001",
        "Dr. Stephen Strange\n117A Bleecker Street\nNew York, NY 10001",
        "Bob C. Smith\n200 Park Avenue, Apartment 221\nNew York, NY 10001",
        "Bowman F. Wildcat\n1 Avenue of Champions\nLexington, KY 40506",
        "Bob C. Smith\n200 Park Avenue\nLexington, KY 40507",
        "Bob Porter c/o Intech\n1 Dead End Row, Room 200\nDallas, TX 12347",
        "Mr. Bob Sydell c/o Intech\n1 Dead End Row, Room 200\nDallas, TX 12347"
        "Steve Rogers\n123 Patriot Lane\nBrooklyn, NY 11201",
        "Natasha Romanoff\n400 Spy Ave\nNew York, NY 10012",
        "Bruce Banner\n789 Science Blvd\nDayton, OH 45402",
        "Clint Barton\n321 Archer St\nWaverly, IA 50677",
        "Thor Odinson\n1 Asgardian Way\nAsgard, AS 00001",
        "Stark Industries\n200 Park Avenue\nNew York, NY 10001",
        "Bruce Wayne\n1007 Mountain Drive\nGotham, NY 10007",
        "Wayne Enterprises\n1000 Wayne Tower\nGotham, NY 10007",
        "Diana Prince\nThemyscira Island\nWashington, DC 20004",
        "Clark Kent\n344 Clinton St Apt 3B\nMetropolis, IL 60001",
        "Daily Planet\n1 Planet Plaza\nMetropolis, IL 60001",
        "Barry Allen\n1 Speedster Ln\nCentral City, MO 64106",
        "Oliver Queen\n1 Queen Mansion\nStarling City, CA 90001",
        "S.T.A.R. Labs\n600 Broadway\nCentral City, MO 64106",
        "Peter Parker\n20 Ingram St Apt 4B\nQueens, NY 11375",
        "OsCorp Industries\n1 OsCorp Plaza\nNew York, NY 10001",
        "Tony’s Pizza\n123 Food St\nNew York, NY 10012",
        "Central Perk\n12 Central Park\nNew York, NY 10001",
        "Dunder Mifflin\n1725 Slough Ave\nScranton, PA 18540",
        "Michael Scott\n123 Paper St\nScranton, PA 18540",
        "Sherlock Holmes\n221B Baker St\nLondon, UK W1U 6RJ",
        "John Watson\n221A Baker St\nLondon, UK W1U 6RJ",
        "Hobbiton Cafe\n1 Hobbiton St\nMatamata, NZ 3400",
        "Frodo Baggins\nBag End, Hobbiton\nMatamata, NZ 3400",
        "Luke Skywalker\n1 Tatooine Ln\nOuter Rim, TT 00001",
        "Darth Vader\n1 Death Star\nOuter Rim, DS 00001",
        "Galactic Empire\nDeath Star\nOuter Rim, DS 00001",
        "Rebel Alliance\n1 Yavin St\nOuter Rim, YV 00002",
        "James Bond\n1 Secret Service\nLondon, UK SW1A 1AA",
        "MI6 Headquarters\n85 Albert Embankment\nLondon, UK SE1 7TP"
    ]
    with open("addresses.txt", 'w') as f:
        for address in addresses:
            f.write(address + '\n\n')  # Each address is separated by a new line

if __name__ == "__main__":
    generate_text_file()
