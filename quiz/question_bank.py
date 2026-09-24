import random


DIFFICULTIES = ("easy", "medium", "hard")

DISTRICTS = [
    "Kathmandu", "Lalitpur", "Bhaktapur", "Kaski", "Chitwan", "Morang",
    "Sunsari", "Jhapa", "Banke", "Bardiya", "Dang", "Surkhet", "Kailali",
    "Kanchanpur", "Rupandehi", "Dolakha", "Syangja", "Ilam", "Dhankuta",
    "Gorkha", "Parsa", "Rautahat", "Sarlahi", "Mahottari", "Saptari",
    "Siraha", "Nuwakot", "Sindhupalchok", "Kavrepalanchok", "Makwanpur",
    "Ramechhap", "Solukhumbu", "Lamjung", "Tanahun", "Baglung", "Parbat",
    "Myagdi", "Mustang", "Manang", "Rolpa", "Rukum", "Jajarkot", "Kalikot",
    "Mugu", "Humla", "Dolpa", "Salyan", "Pyuthan", "Gulmi", "Arghakhanchi",
    "Palpa", "Nawalpur", "Kapilvastu", "Dailekh", "Bajura", "Bajhang",
    "Achham", "Doti", "Darchula", "Baitadi",
]

WORLD_CAPITALS = {
    "India": "New Delhi",
    "China": "Beijing",
    "United States": "Washington DC",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Russia": "Moscow",
    "Brazil": "Brasilia",
    "Egypt": "Cairo",
    "Italy": "Rome",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Bangladesh": "Dhaka",
    "Bhutan": "Thimphu",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Pakistan": "Islamabad",
    "Afghanistan": "Kabul",
    "South Korea": "Seoul",
    "Thailand": "Bangkok",
    "Vietnam": "Hanoi",
    "Indonesia": "Jakarta",
    "Turkey": "Ankara",
    "Mexico": "Mexico City",
    "Nigeria": "Abuja",
    "Argentina": "Buenos Aires",
    "South Africa": "Pretoria",
    "New Zealand": "Wellington",
    "Malaysia": "Kuala Lumpur",
}

COMPUTER_ABBREVS = {
    "HTTP": "HyperText Transfer Protocol",
    "FTP": "File Transfer Protocol",
    "SMTP": "Simple Mail Transfer Protocol",
    "SSH": "Secure Shell",
    "DNS": "Domain Name System",
    "IP": "Internet Protocol",
    "SQL": "Structured Query Language",
    "ROM": "Read-Only Memory",
    "GPU": "Graphics Processing Unit",
    "URL": "Uniform Resource Locator",
    "LAN": "Local Area Network",
    "WAN": "Wide Area Network",
    "VPN": "Virtual Private Network",
    "GUI": "Graphical User Interface",
    "CLI": "Command Line Interface",
    "IDE": "Integrated Development Environment",
    "WYSIWYG": "What You See Is What You Get",
    "FOSS": "Free and Open Source Software",
}

PROTOCOL_PORTS = {
    "HTTP": 80,
    "HTTPS": 443,
    "FTP": 21,
    "SSH": 22,
    "SMTP": 25,
    "DNS": 53,
}

SHORTCUTS = {
    "copy": "Ctrl+C",
    "paste": "Ctrl+V",
    "cut": "Ctrl+X",
    "undo": "Ctrl+Z",
    "redo": "Ctrl+Y",
    "select all": "Ctrl+A",
    "save": "Ctrl+S",
    "find": "Ctrl+F",
    "print": "Ctrl+P",
    "bold": "Ctrl+B",
    "italic": "Ctrl+I",
    "underline": "Ctrl+U",
    "open a new tab": "Ctrl+T",
    "close the current tab": "Ctrl+W",
}

TECH_TYPES = {
    "web browser": ["Chrome", "Firefox", "Edge", "Safari"],
    "operating system": ["Linux", "Windows", "macOS", "Android"],
    "programming language": ["Python", "Java", "C++", "Go"],
    "relational database": ["PostgreSQL", "MySQL", "Oracle", "SQLite"],
    "web framework": ["Django", "React", "Flask", "Laravel"],
    "version control tool": ["Git", "SVN", "Mercurial"],
    "cloud platform": ["AWS", "Azure", "Google Cloud", "Heroku"],
    "container tool": ["Docker", "Kubernetes"],
}

WORLD_HISTORY_EVENTS = [
    ("World War II ended", 1945),
    ("World War I began", 1914),
    ("the Berlin Wall fell", 1989),
    ("the Titanic sank", 1912),
    ("the first human landed on the Moon", 1969),
    ("the Soviet Union dissolved", 1991),
    ("the French Revolution began", 1789),
    ("Napoleon was defeated at Waterloo", 1815),
    ("the American Revolution began", 1775),
    ("the Great Depression began", 1929),
    ("Nepal's democracy was restored", 1990),
    ("Nepal became a republic", 2008),
    ("Nepal's constitution was promulgated", 2015),
    ("the United Nations was founded", 1945),
    ("World War II began", 1939),
    ("the Titanic was launched", 1911),
    ("the European Union was formed", 1993),
    ("the Space Shuttle first launched", 1981),
    ("the first email was sent", 1971),
    ("Sputnik was launched", 1957),
    ("the first iPhone was released", 2007),
    ("the Cold War ended", 1991),
    ("India gained independence", 1947),
    ("the Berlin Wall was built", 1961),
    ("the internet (ARPANET) was created", 1969),
    ("the Reformation started", 1517),
    ("the Magna Carta was signed", 1215),
    ("the Black Death reached Europe", 1347),
    ("Columbus reached the Americas", 1492),
    ("the steam engine was improved by Watt", 1769),
    ("the first railway locomotive ran", 1804),
    ("the telephone was patented", 1876),
    ("the airplane first flew", 1903),
    ("the first computer (ENIAC) was built", 1945),
    ("Nepal was declared a federal republic", 2008),
]

WORLD_CURRENCY = {
    "the United States": "the Dollar",
    "the United Kingdom": "the Pound Sterling",
    "Japan": "the Yen",
    "India": "the Rupee",
    "China": "the Yuan",
    "Bhutan": "the Ngultrum",
    "Bangladesh": "the Taka",
    "most of Europe": "the Euro",
    "Sri Lanka": "the Rupee",
    "Nepal": "the Rupee",
}

NATIONAL_ANIMALS = {
    "Nepal": "the Cow",
    "India": "the Bengal Tiger",
    "Bhutan": "the Takin",
    "Australia": "the Kangaroo",
    "the United States": "the Bald Eagle",
    "China": "the Giant Panda",
    "France": "the Gallic Rooster",
    "the United Kingdom": "the Lion",
}

VISHNU_AVATARS = [
    "Matsya",
    "Kurma",
    "Varaha",
    "Narasimha",
    "Vamana",
    "Parashurama",
    "Rama",
    "Krishna",
]

TEMPLES = [
    ("Pashupatinath", "Shiva"),
    ("Muktinath", "Vishnu"),
    ("Manakamana", "Bhagwati"),
    ("Pathibhara", "Durga"),
    ("Janaki Temple", "Sita"),
    ("Changunarayan", "Vishnu"),
    ("Dakshinkali", "Kali"),
    ("Bindabasini", "Durga"),
    ("Gorakhnath", "Gorakhnath"),
    ("Palanchowk Bhagwati", "Bhagwati"),
    ("Sankata", "Sankata"),
    ("Gokarneshwor", "Shiva"),
]

NON_AVATAR_DEITIES = ["Shiva", "Ganesh", "Laxmi", "Indra", "Surya", "Agni", "Kali", "Saraswati"]


def _option_pack(correct, wrong_options):
    options = [{"text": str(correct), "is_correct": True}]
    shuffled = list(set(str(w) for w in wrong_options))
    shuffled = [w for w in shuffled if w != str(correct)]
    random.shuffle(shuffled)
    for w in shuffled[:3]:
        options.append({"text": w, "is_correct": False})
    random.shuffle(options)
    return options


def _rows_from(entries):
    rows = []
    for text, correct, wrong, difficulty in entries:
        rows.append(
            {
                "text": text.strip(),
                "options": _option_pack(correct, wrong),
                "difficulty": difficulty,
            }
        )
    return rows


def _question_rows(text, correct, wrong_pool, count, difficulty):
    wrong = [str(w) for w in wrong_pool if str(w) != str(correct)]
    random.shuffle(wrong)
    return {"text": text, "options": _option_pack(correct, wrong), "difficulty": difficulty}


def _capital_rows():
    rows = []
    capitals = list(WORLD_CAPITALS.values())
    for country, capital in WORLD_CAPITALS.items():
        rows.append(_question_rows(f"What is the capital of {country}?", capital, capitals, None, "medium"))
        rows.append(
            _question_rows(
                f"Which country has {capital} as its capital city?",
                country,
                list(WORLD_CAPITALS.keys()),
                None,
                "hard",
            )
        )
    return rows


def _computer_extras():
    rows = []
    expansions = list(COMPUTER_ABBREVS.values())
    for abbr, expansion in COMPUTER_ABBREVS.items():
        rows.append(
            _question_rows(f"What does {abbr} stand for?", expansion, expansions, None, "medium")
        )
    ports = list(PROTOCOL_PORTS.values())
    for protocol, port in PROTOCOL_PORTS.items():
        rows.append(
            _question_rows(f"Which port number is used by {protocol}?", port, ports, None, "hard")
        )
    shortcuts = list(SHORTCUTS.values())
    for action, shortcut in SHORTCUTS.items():
        rows.append(
            _question_rows(f"Which keyboard shortcut is used to {action}?", shortcut, shortcuts, None, "medium")
        )
    tech_wrong_pool = []
    for members in TECH_TYPES.values():
        tech_wrong_pool.extend(members)
    for tech_type, members in TECH_TYPES.items():
        for member in members:
            rows.append(
                _question_rows(
                    f"Which of these is a {tech_type}?",
                    member,
                    [m for m in tech_wrong_pool if m != member],
                    None,
                    "easy",
                )
            )
    return rows


def _history_extras():
    rows = []
    event_names = [name for name, _ in WORLD_HISTORY_EVENTS]
    years = [year for _, year in WORLD_HISTORY_EVENTS]
    for name, year in WORLD_HISTORY_EVENTS:
        nearby = [y for y in years if abs(y - year) <= 2]
        rows.append(
            _question_rows(f"In which year did {name} happen?", year, nearby + [year - 3, year + 3], None, "hard")
        )
    for i in range(len(event_names) // 2):
        name, year = WORLD_HISTORY_EVENTS[i]
        other_names = [n for n in event_names if n != name]
        rows.append(
            _question_rows(
                f"Which event happened in {year}?",
                name,
                other_names[:3],
                None,
                "medium",
            )
        )
    return rows


def _geography_extras():
    rows = []
    for district in DISTRICTS:
        rows.append(
            _question_rows(
                f"{district} is a district in which country?",
                "Nepal",
                ["India", "Bhutan", "Bangladesh", "Pakistan"],
                None,
                "easy",
            )
        )
    provinces = ["Koshi", "Madhesh", "Bagmati", "Gandaki", "Lumbini", "Karnali", "Sudurpashchim"]
    for province in provinces:
        rows.append(
            _question_rows(
                f"Which province of Nepal is {province}?",
                province,
                provinces,
                None,
                "easy",
            )
        )
    return rows


def _mythology_extras():
    rows = []
    for avatar in VISHNU_AVATARS:
        rows.append(
            _question_rows(
                f"Which of these is an avatar of Vishnu?",
                avatar,
                NON_AVATAR_DEITIES + [a for a in VISHNU_AVATARS if a != avatar],
                None,
                "medium",
            )
        )
    for avatar in VISHNU_AVATARS:
        others = [a for a in VISHNU_AVATARS if a != avatar]
        rows.append(
            _question_rows(
                f"According to Hindu mythology, {avatar} is an avatar of which god?",
                "Vishnu",
                ["Shiva", "Brahma", "Indra", "Agni"],
                None,
                "easy",
            )
        )
    for temple, deity in TEMPLES:
        temple_names = [t for t, _ in TEMPLES]
        rows.append(
            _question_rows(
                f"Which temple in Nepal is dedicated to {deity}?",
                temple,
                [t for t in temple_names if t != temple],
                None,
                "hard",
            )
        )
    return rows


def _gk_extras():
    rows = []
    currencies = list(WORLD_CURRENCY.values())
    for country, currency in WORLD_CURRENCY.items():
        rows.append(
            _question_rows(
                f"Which currency is used in {country}?",
                currency,
                currencies,
                None,
                "medium",
            )
        )
    animals = list(NATIONAL_ANIMALS.values())
    for country, animal in NATIONAL_ANIMALS.items():
        rows.append(
            _question_rows(
                f"Which is the national animal of {country}?",
                animal,
                animals,
                None,
                "medium",
            )
        )
    return rows


def _math_rows():
    rows = []

    for i in range(40):
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        rows.append(
            {
                "text": f"What is {a} + {b}?",
                "options": _option_pack(a + b, [a + b + 1, a + b - 1, a + b + 2, a + b - 2]),
                "difficulty": "easy",
            }
        )
        rows.append(
            {
                "text": f"What is {a} × {b}?",
                "options": _option_pack(a * b, [a * b + 1, a * b - 1, a * b + 2, a * b - 2]),
                "difficulty": "easy",
            }
        )
        rows.append(
            {
                "text": f"What is {a * 2} − {b}?",
                "options": _option_pack(a * 2 - b, [a * 2 - b + 1, a * 2 - b - 1, a * 2 - b + 2]),
                "difficulty": "easy",
            }
        )

    for i in range(30):
        a = random.randint(15, 60)
        b = random.randint(5, 15)
        rows.append(
            {
                "text": f"What is {a} ÷ {b}?",
                "options": _option_pack(a // b, [a // b + 1, a // b - 1, a // b + 2]),
                "difficulty": "medium",
            }
        )
        rows.append(
            {
                "text": f"What is {a * b} ÷ {a}?",
                "options": _option_pack(b, [b + 1, b - 1, b + 2]),
                "difficulty": "medium",
            }
        )
        rows.append(
            {
                "text": f"What is {a + b} × {3}?",
                "options": _option_pack((a + b) * 3, [(a + b) * 3 + 1, (a + b) * 3 - 1, (a + b) * 3 + 3]),
                "difficulty": "medium",
            }
        )

    for i in range(104):
        a = random.randint(1, 20)
        n = random.randint(2, 4)
        rows.append(
            {
                "text": f"What is {a}²?",
                "options": _option_pack(a * a, [(a + 1) ** 2, (a - 1) ** 2, a * a + 1]),
                "difficulty": "hard",
            }
        )
        pct = random.choice([10, 20, 25, 50])
        base = random.choice([40, 60, 80, 120, 200])
        rows.append(
            {
                "text": f"25% of {base * 4}",
                "options": _option_pack(base, [base + 1, base - 1, base * 2]),
                "difficulty": "hard",
            }
        )
        x, y = random.randint(3, 9), random.randint(3, 9)
        rows.append(
            {
                "text": f"If {x} × {y} = ?",
                "options": _option_pack(x * y, [x * y + 1, (x + 1) * y, x * (y - 1)]),
                "difficulty": "hard",
            }
        )

    entries = [
        ("Which is the only even prime number?", "2", ["4", "6", "8"], "easy"),
        ("What is the sum of angles in a triangle?", "180 degrees", ["90 degrees", "270 degrees", "360 degrees"], "easy"),
        ("How many sides does a hexagon have?", "6", ["5", "7", "8"], "easy"),
        ("What is 10 × 10?", "100", ["90", "110", "1000"], "easy"),
        ("What is half of 50?", "25", ["20", "30", "45"], "easy"),
        ("How many days are in a leap year?", "366", ["365", "364", "360"], "easy"),
        ("What is the square root of 144?", "12", ["14", "11", "10"], "medium"),
        ("A triangle with all sides equal is called?", "Equilateral", ["Isosceles", "Scalene", "Right"], "medium"),
        ("What is 15% of 200?", "30", ["25", "35", "40"], "medium"),
        ("The value of pi (π) rounded to two decimals?", "3.14", ["3.41", "3.04", "2.14"], "medium"),
        ("What comes next: 2, 4, 8, 16, ?", "32", ["24", "20", "18"], "easy"),
        ("What is the LCM of 4 and 6?", "12", ["8", "10", "14"], "medium"),
        ("What is the HCF of 12 and 18?", "6", ["3", "9", "12"], "medium"),
        ("How many vertices does a cube have?", "8", ["6", "4", "12"], "hard"),
        ("What is 7! (7 factorial)?", "5040", ["720", "504", "2520"], "hard"),
        ("If x + 5 = 12, then x = ?", "7", ["5", "6", "8"], "easy"),
        ("What is the slope of y = 2x + 1?", "2", ["1", "3", "0"], "hard"),
        ("What is the derivative of x²?", "2x", ["x", "2", "x²"], "hard"),
        ("Pi is best defined as?", "Ratio of circumference to diameter", ["Ratio of area to radius", "Ratio of diameter to radius", "Number of degrees in a circle"], "medium"),
        ("A number divisible by 2 and 3 is also divisible by?", "6", ["9", "5", "7"], "medium"),
    ]
    rows.extend(_rows_from(entries))
    return rows


COMPUTER_ENTRIES = [
        ("Which language is used with Django?", "Python", ["Java", "PHP", "C++"], "easy"),
        ("What does RAM stand for?", "Random Access Memory", ["Run Access Module", "Read Access Memory", "Rapid Active Memory"], "easy"),
        ("Which protocol is used to load websites?", "HTTP", ["FTP", "SMTP", "SSH"], "easy"),
        ("Which device is called the brain of a computer?", "CPU", ["Monitor", "Keyboard", "Hard disk"], "easy"),
        ("What does HTML stand for?", "HyperText Markup Language", ["HyperText Machine Language", "HighText Markup Language", "Hyperlink Markup Language"], "easy"),
        ("Which of these is an input device?", "Keyboard", ["Monitor", "Printer", "Speaker"], "easy"),
        ("Which of these is an output device?", "Monitor", ["Mouse", "Scanner", "Microphone"], "easy"),
        ("Which unit measures data in binary?", "Bit", ["Byte", "Nibble", "Grid"], "easy"),
        ("Which company developed Windows?", "Microsoft", ["Apple", "Google", "IBM"], "easy"),
        ("What does 'Wi-Fi' primarily enable?", "Wireless internet connection", ["Wired phone calls", "Satellite TV", "GPS tracing"], "easy"),
        ("Which of these is an operating system?", "Linux", ["Excel", "Chrome", "Photoshop"], "easy"),
        ("What does 'Wi-Fi' primarily enable?", "Wireless internet", ["Wired phone calls", "Satellite TV", "GPS tracing"], "easy"),
        ("Which symbol is used for comments in Python?", "#", ["//", "/*", "--"], "easy"),
        ("Bootstrap is used for?", "Styling and responsive design", ["Database management", "Server hosting", "Compiling code"], "easy"),
        ("What is a web browser used for?", "Viewing websites", ["Writing code", "Managing databases", "Designing hardware"], "easy"),
        ("Which file extension denotes a Python file?", ".py", [".pt", ".pyt", ".pyth"], "easy"),
        ("What does a printer produce?", "Hard copy output", ["Soft copy output", "Audio output", "Network packets"], "easy"),
        ("Which shortcut is typically used to copy?", "Ctrl+C", ["Ctrl+V", "Ctrl+X", "Ctrl+P"], "easy"),
        ("Which shortcut is typically used to paste?", "Ctrl+V", ["Ctrl+C", "Ctrl+X", "Ctrl+B"], "easy"),
        ("Which of these is social media?", "Facebook", ["Photoshop", "Windows", "MySQL"], "easy"),
        ("What does 'URL' stand for?", "Uniform Resource Locator", ["Universal Read Link", "Uniform Routing Language", "User Resource Loop"], "medium"),
        ("What does CSS stand for?", "Cascading Style Sheets", ["Computer Style Sheets", "Creative Style System", "Cascading Simple Sheets"], "medium"),
        ("Which data structure follows FIFO?", "Queue", ["Stack", "Tree", "Graph"], "medium"),
        ("Which data structure follows LIFO?", "Stack", ["Queue", "Array", "Heap"], "medium"),
        ("Which protocol is used to send email?", "SMTP", ["HTTP", "FTP", "SSH"], "medium"),
        ("Which protocol is used to transfer files?", "FTP", ["SMTP", "HTTP", "UDP"], "medium"),
        ("What is an IP address?", "Unique identifier for a device on a network", ["A website password", "A file format", "A type of cable"], "medium"),
        ("What does SQL stand for?", "Structured Query Language", ["Simple Question Language", "System Query Language", "Sequential Query Lines"], "medium"),
        ("Which one is a NoSQL database?", "MongoDB", ["PostgreSQL", "MySQL", "Oracle"], "medium"),
        ("Router is used to?", "Route data between networks", ["Store data", "Print documents", "Cool the CPU"], "medium"),
        ("GB stands for?", "Gigabyte", ["Gigabit", "Gigahertz", "Gigapixel"], "medium"),
        ("1 KB equals how many bytes?", "1024", ["1000", "512", "2048"], "medium"),
        ("Which of these is a programming paradigm?", "Object-Oriented", ["PostScript", "Hypertext", "Analog"], "medium"),
        ("What is 'cloud computing'?", "Delivering computing services over the internet", ["Computing using rain sensors", "Offline calculation", "A type of AI chip"], "medium"),
        ("Which language is known for web page interactivity?", "JavaScript", ["HTML", "CSS", "SQL"], "medium"),
        ("Which port is commonly used for HTTPS?", "443", ["80", "21", "25"], "medium"),
        ("Which port is commonly used for HTTP?", "80", ["443", "22", "3306"], "medium"),
        ("What is Git used for?", "Version control", ["Image editing", "Game development", "Networking"], "medium"),
        ("Which database engine is SQLite by default in Django?", "SQLite", ["PostgreSQL", "MySQL", "MongoDB"], "medium"),
        ("What does AI stand for?", "Artificial Intelligence", ["Automated Interface", "Advanced Internet", "Applied Integral"], "medium"),
        ("Which of these is a machine learning library?", "TensorFlow", ["Bootstrap", "Photoshop", "MySQL"], "medium"),
        ("What is the main purpose of a firewall?", "Block unauthorized network access", ["Speed up the processor", "Convert data to binary", "Improve monitor brightness"], "medium"),
        ("Which layer shows the actual pages in a web app?", "Frontend", ["Backend", "Database", "Middleware"], "medium"),
        ("Which is a relational database?", "PostgreSQL", ["MongoDB", "Redis", "Cassandra"], "medium"),
        ("Which of these is a web server?", "Nginx", ["Excel", "VLC", "Thunderbird"], "medium"),
        ("What does 'OOP' stand for?", "Object-Oriented Programming", ["Orderly Output Processing", "Open Object Protocol", "Operator Order Priority"], "hard"),
        ("Which Python function converts a list to its length?", "len()", ["size()", "count()", "length()"], "hard"),
        ("What is a binary tree?", "Data structure with at most two children per node", ["A file system tree", "A network topology", "A sorting algorithm"], "hard"),
        ("Time complexity of binary search?", "O(log n)", ["O(n)", "O(n²)", "O(1)"], "hard"),
        ("Time complexity of linear search in worst case?", "O(n)", ["O(log n)", "O(n²)", "O(1)"], "hard"),
        ("What is TCP?", "Transmission Control Protocol", ["Transfer Control Process", "Total Communication Protocol", "Transmission Carried Packets"], "hard"),
        ("What is DNS used for?", "Resolving domain names to IP addresses", ["Encrypting data", "Storing files", "Compressing video"], "hard"),
        ("What does 'ORM' do?", "Maps database rows to objects", ["Renders frontend pages", "Compiles source code", "Routes network packets"], "hard"),
        ("Which of these is a compiled language?", "C", ["Python", "JavaScript", "Ruby"], "hard"),
        ("Which Python data structure is immutable?", "Tuple", ["List", "Dict", "Set"], "hard"),
        ("What is recursion?", "A function calling itself", ["A type of loop in CSS", "A database join", "A network retry"], "hard"),
        ("What does 'API' stand for?", "Application Programming Interface", ["Applied Program Integration", "Automatic Processor Interface", "Active Packet Interchange"], "hard"),
        ("What is a 'byte' made of?", "8 bits", ["4 bits", "16 bits", "10 bits"], "hard"),
        ("Which sorting algorithm is fastest in average case?", "Merge/Quick sort", ["Bubble sort", "Selection sort", "Insertion sort"], "hard"),
        ("What does 'migration' do in Django?", "Applies database schema changes", ["Moves servers", "Renames files", "Renders templates"], "hard"),
        ("What is a 'virtual environment' in Python?", "An isolated Python environment", ["A cloud server", "A web framework", "A syntax error fixer"], "medium"),
        ("What is the full form of 'PDF'?", "Portable Document Format", ["Printable Data File", "Programmed Document Format", "Personal Data File"], "easy"),
        ("Which tag creates a hyperlink in HTML?", "<a>", ["<link>", "<href>", "<p>"], "medium"),
        ("Which CSS property changes text color?", "color", ["font-size", "background", "text-align"], "medium"),
        ("Which HTML tag makes the text bold?", "<strong>", ["<italic>", "<big>", "<em>"], "medium"),
        ("Kubernetes is used for?", "Container orchestration", ["Email marketing", "Logo design", "Database backups"], "hard"),
    ]


def _computer_rows():
    rows = _rows_from(COMPUTER_ENTRIES)
    rows.extend(_computer_extras())
    return rows


def _history_rows():
    entries = [
        ("Who is known for unifying modern Nepal?", "Prithvi Narayan Shah", ["Jung Bahadur Rana", "Bhimsen Thapa", "Tribhuvan"], "medium"),
        ("In which year did Nepal become a federal democratic republic?", "2008", ["2006", "2010", "2015"], "easy"),
        ("In which year was Nepal's current constitution promulgated?", "2015", ["2008", "2012", "2017"], "easy"),
        ("Who was the first President of Nepal?", "Ram Baran Yadav", ["Bidhya Devi Bhandari", "Girija Prasad Koirala", "Pushpa Kamal Dahal"], "easy"),
        ("Who was the first woman President of Nepal?", "Bidhya Devi Bhandari", ["Sushila Karki", "Onsari Gharti Magar", "Anuradha Koirala"], "easy"),
        ("In which year did the People's Movement (Jana Andolan II) take place?", "2006", ["1990", "2008", "2015"], "easy"),
        ("Which conflict ended with the Comprehensive Peace Agreement of 2006?", "Nepali Civil War", ["Kargil War", "World War II", "Sino-Nepal War"], "easy"),
        ("Who was the last King of Nepal?", "Gyanendra Shah", ["Birendra Shah", "Mahendra Shah", "Tribhuvan Shah"], "easy"),
        ("Who was King Birendra's father?", "Mahendra", ["Tribhuvan", "Dipendra", "Gyanendra"], "medium"),
        ("In which year did the royal family massacre occur?", "2001", ["1999", "2003", "2006"], "easy"),
        ("In which year did Nepal's first democratic elections after democracy restoration happen?", "1991", ["1990", "1995", "1999"], "medium"),
        ("Who was the first Prime Minister of Nepal?", "Bhimsen Thapa", ["Jung Bahadur Rana", "B.P. Koirala", "Girija Prasad Koirala"], "hard"),
        ("Who is called the 'Father of Nepali Democracy'?", "B.P. Koirala", ["Prithvi Narayan Shah", "Ganesh Man Singh", "Krishna Prasad Bhattarai"], "medium"),
        ("In which year was Nepal's first multi-party democracy Panchayat abolished?", "1990", ["1950", "1960", "2006"], "medium"),
        ("Who founded the Gorkha kingdom?", "Dravya Shah", ["Prithvi Narayan Shah", "Ram Shah", "Jayasthiti Malla"], "hard"),
        ("Which treaty were Nepal's border disputes with India about in the modern era?", "Sugauli Treaty", ["Treaty of Thapathali", "Treaty of Versailles", "Treaty of Sagauli"], "hard"),
        ("In which year was the Sugauli Treaty signed?", "1816", ["1810", "1820", "1846"], "hard"),
        ("Who is the descendant line of Rana rulers known for?", "Hereditary Prime Ministers", ["Kings of Nepal", "Military Generals", "Religious leaders"], "medium"),
        ("Which dynasty ruled Kathmandu Valley before unification?", "Malla", ["Shah", "Rana", "Lichchhavi"], "medium"),
        ("The Lichchhavi dynasty ruled which area?", "Kathmandu Valley", ["Terai", "Pokhara", "Mustang"], "hard"),
        ("Who was the first woman speaker of Nepal's parliament?", "Onsari Gharti Magar", ["Sushila Karki", "Anuradha Koirala", "Bidhya Devi Bhandari"], "hard"),
        ("Who led the 1950 revolution against the Ranas?", "King Tribhuvan", ["King Birendra", "Gyanendra", "Mahendra"], "medium"),
        ("Who founded Nepal's first political party, Nepal Praja Parishad?", "Tanka Prasad Acharya", ["B.P. Koirala", "Ganesh Man Singh", "K.I. Singh"], "hard"),
        ("Which year did Nepal join the United Nations?", "1955", ["1945", "1950", "1960"], "medium"),
        ("Nepal is secular and multi-ethnic. Its official name in 2015 was changed to?", "Federal Democratic Republic of Nepal", ["Kingdom of Nepal", "Democratic People's Republic of Nepal", "Republic of Nepal"], "medium"),
        ("Which king built the Kathmandu to Tribhuvan era's 'Dharahara'?", "Bhimsen Thapa", ["Prithvi Narayan Shah", "Jang Bahadur", "Man Mohan Adhikari"], "hard"),
        ("Which king divided Nepal into four Chaubiase states?", "Various regional kings", ["Prithvi Narayan Shah", "Ashoka", "Birendra"], "hard"),
        ("The Battle of Nalapani was fought against which power?", "British", ["Chinese", "Mughal", "Gurkha rebels"], "hard"),
        ("Who was the legendary soldier of Anglo-Nepal war remembered for courage?", "Balbhadra Kunwar", ["Amar Singh Thapa", "Amar Singh Thapa II", "Bhimsen Thapa"], "hard"),
        ("King Mahendra introduced which political system in 1962?", "Panchayat", ["Democracy", "Monarchy absolute", "Federalism"], "medium"),
        ("Who was the architect of the Panchayat system?", "King Mahendra", ["King Birendra", "Jang Bahadur", "Tribhuvan"], "hard"),
        ("In which year was Panchayat introduced?", "1962", ["1950", "1972", "1990"], "medium"),
        ("Who was the king during the signing of Sugauli Treaty?", "Girvan Yuddha Bikram Shah", ["Prithvi Narayan Shah", "Bahadur Shah", "Rana Bahadur Shah"], "hard"),
        ("Which historic agreement recognized the autonomy of feudal lords in Nepal in 1846?", "Kot Massacre", ["Sugauli", "Bargain of Baisakh", "India-Nepal Peace Treaty"], "hard"),
        ("Which year was the Nepal Civil War (Maoist insurgency) formally declared?", "1996", ["2001", "2006", "1990"], "medium"),
        ("Who led the 2015 earthquake reconstruction?", "Nepal government", ["UNESCO", "India", "China"], "easy"),
        ("Which ancient writer/physician came from Lumbini?", "Gautama Buddha", ["Ashoka", "Araniko", "Mahatma Gandhi"], "easy"),
        ("The state emblem shows mount Everest, a white map and two crossed weapons of which era?", "Modern Nepal", ["Ancient Greece", "Roman Empire", "British Raj"], "hard"),
        ("The name of the national flower of Nepal is?", "Rhododendron arboreum", ["Lotus", "Tulip", "Sunflower"], "medium"),
        ("Which dynasty is known as the golden age of Nepali art?", "Malla", ["Shah", "Rana", "Kirat"], "medium"),
        ("Who was the first elected Prime Minister of Nepal (from a political party)?", "Bishweshwar Prasad Koirala", ["Girija Prasad Koirala", "KP Sharma Oli", "Sher Bahadur Deuba"], "hard"),
        ("In which year did Nepal abolish the monarchy?", "2008", ["2006", "1990", "2015"], "easy"),
        ("Who was Nepal's first woman Chief Justice?", "Sushila Karki", ["Anuradha Koirala", "Bidhya Devi Bhandari", "Kalyani Rana"], "hard"),
        ("The 'Cotton Mill' established by Bir Shumsher was in which era?", "Rana period", ["Shah period", "Malla period", "Lichchhavi era"], "hard"),
        ("Which king of Kantipur built the Kathmandu Durbar Square's Taleju Temple?", "King Pratap Malla", ["King Jayasthiti Malla", "King Mahendra Malla", "Jaya Prakash Malla"], "hard"),
        ("The Gorkha king who ruled during unification of the east was?", "Prithvi Narayan Shah", ["Ran Bahadur Shah", "Dravya Shah", "Ram Shah"], "medium"),
        ("Which treaty ended the Anglo-Nepal war in 1816, losing Nepal's Kumaon–Garhwal?", "Sugauli Treaty", ["Treaty of Sagauli", "Treaty of Thapathali", "Treaty of Lhasa"], "medium"),
        ("Which Nepali army division fought at the Battle of Makawanpur?", "The Gorkha army under Prithvi Narayan Shah", ["The British East India", "The Mughal", "The Lichchhavi"], "hard"),
        ("Which prime minister of Nepal signed the Sugauli Treaty?", "Bhimsen Thapa", ["Jung Bahadur Rana", "Ranoddip Singh", "Deva Shumsher"], "medium"),
    ]
    rows = _rows_from(entries)
    rows.extend(_history_extras())
    return rows


def _geography_rows():
    entries = [
        ("What is the capital city of Nepal?", "Kathmandu", ["Pokhara", "Biratnagar", "Lalitpur"], "easy"),
        ("How many provinces does Nepal have?", "7", ["5", "6", "8"], "easy"),
        ("Which is the highest mountain in the world?", "Mount Everest (Sagarmatha)", ["K2", "Kanchenjunga", "Lhotse"], "easy"),
        ("Which ocean lies to the south of Nepal?", "Indian Ocean", ["Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "easy"),
        ("What is the capital of Province 1?", "Biratnagar", ["Janakpur", "Pokhara", "Hetauda"], "medium"),
        ("What is the capital of Bagmati Province?", "Hetauda", ["Kathmandu", "Pokhara", "Janakpur"], "medium"),
        ("What is the capital of Gandaki Province?", "Pokhara", ["Hetauda", "Biratnagar", "Godawari"], "medium"),
        ("What is the capital of Lumbini Province?", "Deukhuri", ["Butwal", "Nepalgunj", "Siddharthanagar"], "medium"),
        ("What is the capital of Karnali Province?", "Birendranagar", ["Jumla", "Surkhet", "Dhangadhi"], "medium"),
        ("What is the capital of Sudurpashchim Province?", "Godawari", ["Dhangadhi", "Mahendranagar", "Birendranagar"], "medium"),
        ("What is the capital of Madhesh Province?", "Janakpur", ["Biratnagar", "Simara", "Butwal"], "medium"),
        ("Which nation borders Nepal to the north?", "China", ["India", "Bhutan", "Bangladesh"], "easy"),
        ("Which nations border Nepal to the south?", "India", ["China", "Bhutan", "Myanmar"], "easy"),
        ("Which is the largest lake in Nepal?", "Rara Lake", ["Phewa Lake", "Begnas Lake", "Tilicho Lake"], "medium"),
        ("Lumbini is located in which province?", "Lumbini", ["Karnali", "Bagmati", "Madhesh"], "medium"),
        ("Which river is called the 'lifeline of Terai' in Nepal?", "Koshi", ["Bagmati", "Trishuli", "Bheri"], "hard"),
        ("Which is the deepest lake in Nepal?", "Phoksundo Lake", ["Rara Lake", "Phewa Lake", "Gokyo Lake"], "hard"),
        ("Which national park is known for one-horned rhinoceros in Nepal?", "Chitwan National Park", ["Sagarmatha National Park", "Rara National Park", "Bardia National Park"], "medium"),
        ("Sagarmatha National Park protects which mountain?", "Mount Everest", ["Annapurna", "Makalu", "Dhaulagiri"], "easy"),
        ("Which is the highest point in Nepal?", "Mount Everest", ["K2", "Kanchenjunga", "Makalu"], "easy"),
        ("Which is a famous lake for boating in Pokhara?", "Phewa Lake", ["Rara Lake", "Tilicho Lake", "Gokyo Lake"], "easy"),
        ("Which Himalayan pass connects Mustang to Tibet?", "Korala", ["Thorung La", "Rasuwa", "Tatopani"], "hard"),
        ("Which region of Nepal is famous for the Yak and Tungna pastures?", "High Himalaya", ["Terai", "Mahabharat Range", "Kathmandu Valley"], "medium"),
        ("Which is the highest waterfall in Nepal?", "Hyatung Falls", ["Dev's Fall", "Sundarijal Falls", "Rani Jamara"], "hard"),
        ("Which river flows through the Kathmandu Valley?", "Bagmati", ["Koshi", "Karnali", "Seti"], "easy"),
        ("Which country is famous for fjords?", "Norway", ["Nepal", "Brazil", "Egypt"], "hard"),
        ("Which is the largest desert in the world?", "Sahara", ["Gobi", "Thar", "Atacama"], "medium"),
        ("Which is the longest river in the world?", "Nile", ["Amazon", "Yangtze", "Mississippi"], "medium"),
        ("Which is the largest continent by area?", "Asia", ["Africa", "North America", "Europe"], "medium"),
        ("Which is the smallest continent by area?", "Australia", ["Europe", "Antarctica", "South America"], "medium"),
        ("Which country has the largest population as of 2023?", "India", ["China", "USA", "Indonesia"], "easy"),
        ("Which is the wettest place on Earth?", "Mawsynram, India", ["Kathmandu", "London", "Sahara"], "hard"),
        ("Which is the coldest continent?", "Antarctica", ["Arctic", "Europe", "Asia"], "easy"),
        ("Which is the driest continent?", "Antarctica", ["Australia", "Africa", "South America"], "hard"),
        ("Which mountain range separates Nepal and Tibet?", "Himalayas", ["Andes", "Alps", "Rockies"], "easy"),
        ("Mount Makalu is part of which range?", "Himalayas", ["Andes", "Alps", "Carpathians"], "medium"),
        ("Which is the capital of Lumbini Province's seat in the Terai city?", "Deukhuri", ["Butwal", "Nepalgunj", "Ghorahi"], "hard"),
        ("Which Nepali city is called the 'City of Temples'?", "Kathmandu", ["Pokhara", "Bhaktapur", "Patna"], "easy"),
        ("Ethansin (Stupa) is located in which city?", "Kathmandu", ["Lumbini", "Pokhara", "Janakpur"], "medium"),
        ("Which city is famous for Begnas Lake?", "Pokhara", ["Kathmandu", "Dharan", "Biratnagar"], "easy"),
        ("Which is the easternmost district of Nepal?", "Taplejung", ["Ilam", "Jhapa", "Panchthar"], "hard"),
        ("Which is the westernmost district of Nepal?", "Darchula", ["Kanchanpur", "Baitadi", "Bajhang"], "hard"),
        ("Which district does Rara lake fall in?", "Mugu", ["Jumla", "Humla", "Dolpa"], "hard"),
    ]
    rows = _rows_from(entries)
    rows.extend(_geography_extras())
    rows.extend(_capital_rows())
    return rows


def _mythology_rows():
    entries = [
        ("Pashupatinath temple is associated with which deity?", "Shiva", ["Vishnu", "Brahma", "Durga"], "easy"),
        ("Muktinath temple is associated with which deity?", "Vishnu", ["Shiva", "Ganesh", "Saraswati"], "easy"),
        ("Janaki Temple in Janakpur is dedicated to whom?", "Sita", ["Laxmi", "Parvati", "Radha"], "easy"),
        ("Dakshinkali temple is dedicated to which goddess?", "Kali", ["Saraswati", "Laxmi", "Parvati"], "medium"),
        ("Manakamana temple is dedicated to which goddess?", "Bhagwati/Bindu Basini", ["Saraswati", "Laxmi", "Durga"], "medium"),
        ("Changu Narayan temple is dedicated to?", "Vishnu", ["Shiva", "Brahma", "Krishna"], "medium"),
        ("Which avatar of Vishnu appeared as a boar?", "Varaha", ["Narasimha", "Rama", "Kurma"], "hard"),
        ("Who is the god of creation in Hindu mythology?", "Brahma", ["Vishnu", "Shiva", "Indra"], "easy"),
        ("Who is the goddess of wisdom in Hindu mythology?", "Saraswati", ["Laxmi", "Durga", "Kali"], "easy"),
        ("Who is the goddess of wealth?", "Laxmi", ["Saraswati", "Parvati", "Durga"], "easy"),
        ("Which festival lights oil lamps to welcome Laxmi?", "Tihar", ["Dashain", "Holi", "Maha Shivaratri"], "easy"),
        ("Dashain is celebrated for the victory of?", "Durga over Mahishasura", ["Rama over Ravana", "Krishna over Kansa", "Indra over Vritra"], "medium"),
        ("Which god has Ganesh as his son?", "Shiva", ["Vishnu", "Brahma", "Indra"], "easy"),
        ("Ganesh is depicted with the head of?", "Elephant", ["Lion", "Tiger", "Horse"], "easy"),
        ("The river Ganga is said to flow out of which god's hair?", "Shiva", ["Indra", "Vishnu", "Agni"], "hard"),
        ("Krishna is the avatar of which god?", "Vishnu", ["Shiva", "Brahma", "Rama"], "easy"),
        ("Ravana had how many heads according to legend?", "10", ["3", "5", "7"], "medium"),
        ("Who wrote the Ramayana?", "Valmiki", ["Ved Vyasa", "Tulsidas", "Kalidasa"], "medium"),
        ("Who is considered the author of the Mahabharata?", "Ved Vyasa", ["Valmiki", "Tulsidas", "Bharat"], "hard"),
        ("Which king is a central figure of the Mahabharata war?", "Yudhishthira", ["Arjuna", "Bhima", "Nakula"], "medium"),
        ("Which God rode the Garuda?", "Vishnu", ["Shiva", "Indra", "Agni"], "medium"),
        ("Who is the goddess of destruction in some traditions?", "Kali", ["Laxmi", "Saraswati", "Vasundhara"], "medium"),
        ("The temple of Bindabasini is located in?", "Pokhara", ["Kathmandu", "Janakpur", "Hetauda"], "hard"),
        ("Maistol temple in Nepal is a sacred site for which religion?", "Kiratism", ["Islam", "Christianity", "Buddhism"], "hard"),
        ("Swyambhu Stupa is associated with which religion?", "Buddhism", ["Hinduism", "Islam", "Jainism"], "easy"),
        ("Bouddhanath Stupa is located in?", "Kathmandu", ["Pokhara", "Lumbini", "Bhaktapur"], "easy"),
        ("The great Buddha set for enlightenment at?", "Bodh Gaya (India)", ["Lumbini", "Sarnath", "Kushinagar"], "easy"),
        ("Which deity is the patron of Pasupati zone?", "Shiva (Pashupatinath)", ["Vishnu", "Ganesh", "Kali"], "easy"),
        ("In Hindu tradition, who is the moon god?", "Chandra", ["Surya", "Agni", "Varuna"], "medium"),
        ("Who is the sun god in Hindu mythology?", "Surya", ["Chandra", "Agni", "Indra"], "easy"),
        ("Which demon king ruled Lanka in Ramayana?", "Ravana", ["Mahishasura", "Kumbhakarna", "Hiranyakashipu"], "easy"),
        ("Which is the vehicle (vahana) of Goddess Durga?", "Lion", ["Peacock", "Eagle", "Bull"], "medium"),
        ("Which is the vehicle of Lord Shiva?", "Nandi (Bull)", ["Garuda", "Lion", "Horse"], "medium"),
        ("Which weapon did Lord Shiva use (Trishul)?", "Trident", ["Bow", "Sword", "Axe"], "medium"),
        ("Surya's chariot is pulled by how many horses?", "7", ["4", "8", "6"], "hard"),
        ("Who is the god of fire in Hindu mythology?", "Agni", ["Vayu", "Varuna", "Indra"], "hard"),
        ("Who is the god of wind?", "Vayu", ["Agni", "Indra", "Chandra"], "hard"),
        ("Which festival marks the return of Lord Rama to Ayodhya?", "Tihar/Deepawali", ["Holi", "Dashain", "Makar Sankranti"], "medium"),
        ("Which pilgrimage site in Nepal is believed to be where 108 temples exist at Janakpur?", "Janaki Mandir", ["Pashupatinath", "Muktinath", "Manakamana"], "hard"),
        ("According to legend, which goddess visited Manakamana temple every night?", "Bhagwati", ["Kali", "Durga", "Parvati"], "hard"),
        ("In which Himalayan region is the Kailash mountain (associated with Shiva)?", "Tibet, China", ["Nepal", "India", "Bhutan"], "medium"),
        ("Which deity is believed to meditate on Mount Kailash?", "Shiva", ["Vishnu", "Brahma", "Indra"], "medium"),
        ("Which god carries the conch (Shankha) in Hindu mythology?", "Vishnu", ["Shiva", "Ganesh", "Hanuman"], "hard"),
        ("Which weapon did Indra use (Vajra)?", "Thunderbolt", ["Trident", "Bow", "Sword"], "hard"),
        ("Who is the wife of Lord Shiva?", "Parvati", ["Sita", "Radha", "Laxmi"], "easy"),
        ("Who is the consort of Goddess Saraswati?", "Brahma", ["Vishnu", "Shiva", "Indra"], "hard"),
        ("Who is the son of Laxmi and Vishnu?", "Kamadeva/Madana", ["Ganesh", "Kartikeya", "Hanuman"], "hard"),
        ("Which deity is known to ride a peacock?", "Kartikeya (Murugan)", ["Ganesh", "Shiva", "Indra"], "hard"),
        ("Which demon was slain by Goddess Durga?", "Mahishasura", ["Ravana", "Hiranyakashipu", "Kamsa"], "medium"),
        ("Which king was saved by Varaha avatar?", "Bhumi (Earth)", ["Harishchandra", "Rama", "Yudhishthira"], "hard"),
        ("Which is the tenth avatar of Vishnu?", "Kalki", ["Krishna", "Buddha", "Rama"], "medium"),
        ("Who is the older brother of Lakshmana?", "Rama", ["Bharata", "Shatrughna", "Yudhishthira"], "medium"),
        ("Hanuman is a devotee of which god?", "Rama", ["Krishna", "Shiva", "Ganesh"], "easy"),
        ("Which god is known as the destroyer of the universe?", "Shiva", ["Vishnu", "Brahma", "Indra"], "easy"),
        ("Which of these is the river of the gods in Hindu mythology?", "Ganga", ["Yamuna", "Godavari", "Koshi"], "medium"),
        ("Who is the god of the underworld in Hindu mythology?", "Yama", ["Varuna", "Kubera", "Agni"], "medium"),
        ("Which deity holds a noose (Pasha) for souls?", "Yama", ["Varuna", "Shiva", "Kali"], "hard"),
        ("Which festival is celebrated for 15 days, ending with Dashami?", "Dashain", ["Tihar", "Holi", "Teej"], "easy"),
        ("Which Nepali festival worships the crow, dog, and cow on separate days?", "Tihar", ["Dashain", "Holi", "Maghe Sankranti"], "medium"),
        ("Which festival celebrates brother-sister love in Nepal?", "Bhai Tika (during Tihar)", ["Dashain", "Teej", "Holi"], "easy"),
        ("Which festival do Nepali women celebrate by fasting for their husbands?", "Teej", ["Tihar", "Dashain", "Krishna Janmashtami"], "medium"),
        ("In which month of the Nepali calendar is Dashain celebrated?", "Ashwin", ["Baisakh", "Mangsir", "Push"], "medium"),
        ("Which goddess rides a tiger?", "Durga", ["Saraswati", "Laxmi", "Kali"], "medium"),
        ("Which deity is worshipped with leaves called 'Akshata'?", "Various (rice used in puja)", ["Only Shiva", "Only Kali", "Only Ganesh"], "hard"),
        ("The Simpus (pagoda) style of architecture is associated with which deity?", "Shiva temples", ["Mosques", "Churches", "Synagogues"], "hard"),
        ("Which god dressed as a dwarf tricked King Bali?", "Vamana", ["Varaha", "Kurma", "Narasimha"], "hard"),
        ("Which demon was killed by the Narasimha avatar?", "Hiranyakashipu", ["Ravana", "Kamsa", "Mahishasura"], "hard"),
        ("Which avatar of Vishnu appeared as a fish?", "Matsya", ["Kurma", "Varaha", "Kalki"], "hard"),
        ("Which avatar of Vishnu appeared as a turtle?", "Kurma", ["Matsya", "Varaha", "Parashurama"], "hard"),
        ("Which avatar of Vishnu is associated with Lord Rama's father lineage?", "Parashurama", ["Vamana", "Kalki", "Kurma"], "hard"),
        ("Who is the patron deity of Gurkha soldiers?", "Gorakhnath", ["Pashupatinath", "Muktinath", "Annapurna"], "medium"),
        ("Which region is sacred to both Hindus and Buddhists, with a famous temple complex?", "Muktinath", ["Kathmandu", "Pokhara", "Biratnagar"], "medium"),
        ("Which deity is often depicted with a mouse as his vehicle?", "Ganesh", ["Shiva", "Kartikeya", "Durga"], "easy"),
        ("Which of these is a symbol of Shiva?", "Trishul and Damaru", ["Conch and Chakra", "Bow and arrow", "Sword and shield"], "medium"),
        ("Which deity is associated with the crescent moon?", "Shiva", ["Chandra alone", "Surya", "Indra"], "medium"),
        ("According to legend, what material is Ganesh made of?", "Turmeric (sandalwood paste)", ["Gold", "Stone", "Wood"], "hard"),
    ]
    rows = _rows_from(entries)
    rows.extend(_mythology_extras())
    return rows


def _gk_rows():
    entries = [
        ("Which is Nepal's national animal?", "Cow", ["Tiger", "Elephant", "Rhino"], "easy"),
        ("Which is Nepal's national bird?", "Danphe (Himalayan Monal)", ["Peacock", "Sparrow", "Eagle"], "medium"),
        ("Which is Nepal's national flower?", "Rhododendron arboreum", ["Lotus", "Hibiscus", "Tulip"], "medium"),
        ("Which is Nepal's national tree?", "Rhododendron arboreum", ["Sal", "Peepal", "Banyan"], "hard"),
        ("Which is Nepal's national color?", "Crimson red", ["Blue", "Green", "Yellow"], "hard"),
        ("Nepal's flag is the only national flag that is not?", "Rectangular", ["Red", "Triangular overall", "Colourful"], "medium"),
        ("What is the capital of Australia?", "Canberra", ["Sydney", "Melbourne", "Perth"], "medium"),
        ("What is the capital of Canada?", "Ottawa", ["Toronto", "Vancouver", "Montreal"], "medium"),
        ("What is the capital of Japan?", "Tokyo", ["Kyoto", "Osaka", "Nagoya"], "easy"),
        ("What is the capital of the USA?", "Washington D.C.", ["New York", "Los Angeles", "Chicago"], "easy"),
        ("Which planet is known as the Red Planet?", "Mars", ["Venus", "Jupiter", "Saturn"], "easy"),
        ("Which planet is known as the Blue Planet?", "Earth", ["Neptune", "Uranus", "Mars"], "easy"),
        ("Which is the largest planet in our solar system?", "Jupiter", ["Saturn", "Neptune", "Earth"], "easy"),
        ("Which is the smallest planet in our solar system?", "Mercury", ["Mars", "Venus", "Pluto"], "medium"),
        ("Which is the fastest animal on land?", "Cheetah", ["Lion", "Horse", "Gazelle"], "easy"),
        ("Which is the largest animal on Earth?", "Blue whale", ["Elephant", "Giraffe", "Shark"], "easy"),
        ("Which is the largest living reptile?", "Saltwater crocodile", ["Komodo dragon", "Python", "Tortoise"], "hard"),
        ("Which gas do plants absorb during photosynthesis?", "Carbon dioxide", ["Oxygen", "Nitrogen", "Hydrogen"], "easy"),
        ("Which gas do humans need to breathe?", "Oxygen", ["Carbon dioxide", "Nitrogen", "Helium"], "easy"),
        ("Which is the most common gas in Earth's atmosphere?", "Nitrogen", ["Oxygen", "Carbon dioxide", "Argon"], "medium"),
        ("How many continents are there?", "7", ["5", "6", "8"], "easy"),
        ("How many oceans are there?", "5", ["3", "4", "6"], "medium"),
        ("Which is the smallest country in the world?", "Vatican City", ["Monaco", "Nauru", "San Marino"], "medium"),
        ("Which is the largest country by area?", "Russia", ["Canada", "China", "USA"], "medium"),
        ("Which is the longest river in South Asia?", "Brahmaputra", ["Ganges", "Indus", "Koshi"], "hard"),
        ("Which is the official language of Nepal?", "Nepali", ["Hindi", "Newari", "English"], "easy"),
        ("Which festival is known as the festival of colors?", "Holi", ["Dashain", "Tihar", "Eid"], "easy"),
        ("Which festival is the biggest in Nepal?", "Dashain", ["Tihar", "Holi", "Lhosar"], "easy"),
        ("What is the currency of Nepal?", "Nepalese Rupee", ["Nepali Dollar", "Nepal Rupia", "Rufiyaa"], "easy"),
        ("How many rupees make one Nepali 'paisa' fraction? (1 rupee = ?)", "100 paisa", ["50", "10", "25"], "easy"),
        ("Which famous Nepali leader is known for democracy movements?", "B.P. Koirala", ["King Mahendra", "Pushpa Kamal Dahal", "Man Mohan Adhikari"], "medium"),
        ("Which is the national game of Nepal?", "Volleyball", ["Cricket", "Football", "Kabaddi"], "medium"),
        ("Which sport is most followed in Nepal?", "Cricket", ["Volleyball", "Football", "Basketball"], "easy"),
        ("Which Nepali national is the first woman to summit Everest?", "Pasang Lhamu Sherpa", ["Junko Tabei", "Nivedita", "Lakpa Sherpa"], "medium"),
        ("Who was the first person to summit Mount Everest?", "Edmund Hillary", ["Tenzing Norgay", "Reinhold Messner", "Chris Bonington"], "medium"),
        ("Which Nepali climber holds the record for most Everest summits (as of 2024)?", "Kami Rita Sherpa", ["Tenzing Norgay", "Edmund Hillary", "Apa Sherpa"], "hard"),
        ("Which is the official currency of the United Kingdom?", "Pound Sterling", ["Euro", "Dollar", "Franc"], "easy"),
        ("Which is the currency used in most of Europe?", "Euro", ["Pound", "Dollar", "Franc"], "medium"),
        ("Which is the world's largest democracy?", "India", ["USA", "Indonesia", "Nepal"], "medium"),
        ("Which is the world's smallest continent?", "Australia", ["Europe", "Antarctica", "Africa"], "medium"),
        ("Which is the highest award in the Olympics?", "Gold medal", ["Silver medal", "Platinum medal", "Crown"], "easy"),
        ("Which is the largest lake in the world by area?", "Caspian Sea", ["Lake Superior", "Baikal", "Rara"], "hard"),
        ("Which is the deepest lake in the world?", "Lake Baikal", ["Caspian Sea", "Rara", "Titikaka"], "hard"),
        ("The mountain K2 is known as the mountain of which range?", "Karakoram", ["Himalayas", "Andes", "Alps"], "medium"),
        ("Which is the national anthem of Nepal called?", "Sayaun Thunga Phool Ka", ["Rastriya Gaan", "Sujukamma", "Mero Bal Nepal"], "medium"),
        ("Who wrote Nepal's national anthem?", "Pradeep Kumar Rai (Byakul Maila)", ["Balkrishna Sama", "Laxmi Prasad Devkota", "Madhav Prasad Ghimire"], "hard"),
        ("Which is the highest statue in the world?", "Statue of Unity (India)", ["Statue of Liberty", "Christ Redeemer", "Great Buddha"], "hard"),
        ("Which is the official currency of India?", "Rupee", ["Taka", "Rupia", "Peso"], "easy"),
        ("Which is the highest peak in South Asia?", "Everest", ["K2", "Kangchenjunga", "Makalu"], "easy"),
        ("Which country has a flag with a lion?", "Sri Lanka", ["Nepal", "India", "Bhutan"], "hard"),
        ("Which country's flag is the dragon of Bhutan?", "Bhutan", ["Nepal", "China", "Sri Lanka"], "medium"),
        ("Which is the largest mammal in the world?", "Blue whale", ["Elephant", "Hippopotamus", "Giraffe"], "easy"),
        ("Which is the tallest animal on Earth?", "Giraffe", ["Elephant", "Camel", "Ostrich"], "easy"),
        ("Which bird is the national symbol of courage in Nepal's folklore?", "Danphe", ["Crow", "Sparrow", "Eagle"], "hard"),
        ("Which day is celebrated as Constitution Day in Nepal?", "Asoj 3 (Sep 19-20)", ["Magh 1", "Baisakh 1", "Dashain"], "hard"),
        ("How many federal provinces did Nepal adopt in 2015?", "7", ["5", "6", "8"], "easy"),
        ("Which is the highest civilian award of Nepal?", "Order of Nepal", ["Bharat Ratna", "Nishan-e-Pakistan", "Padma Shree"], "hard"),
        ("Which is the largest district of Nepal by area?", "Dolpa", ["Kathmandu", "Jhapa", "Surkhet"], "hard"),
        ("Which is the smallest district of Nepal?", "Bhaktapur", ["Lalitpur", "Kathmandu", "Ilam"], "hard"),
        ("Which grass is the state source of health in Nepal known to treat many diseases?", "Yarshagumba (Himalayan Viagra)", ["Basil", "Aloe", "Mint"], "hard"),
        ("What is the approximate population of Nepal?", "About 30 million", ["10 million", "50 million", "100 million"], "medium"),
        ("Which Nepali city is known as the 'City of Lakes'?", "Pokhara", ["Kathmandu", "Lumbini", "Biratnagar"], "easy"),
        ("Which is the oldest university of Nepal?", "Tribhuvan University", ["Kathmandu University", "Purbanchal University", "Pokhara University"], "medium"),
        ("Which is the tallest statue in Nepal?", "Kirtipur Buddha", ["Shiva Statue Kailashkut", "Statue of Unity", "Manakamana"], "hard"),
        ("Which payment method is widespread among Nepali teenagers to businessmen? (digital)", "eSewa", ["PayPal", "Apple Pay", "Paytm"], "medium"),
        ("Which is the longest highway in Nepal?", "East-West Highway (Mahendra Rajmarg)", ["Araniko Highway", "Kathmandu-Pokhara", "Siddhartha Highway"], "medium"),
        ("Which is Nepal's biggest trading partner?", "India", ["China", "USA", "Japan"], "easy"),
        ("Which country shares the longest border with Nepal?", "India", ["China", "Bhutan", "Bangladesh"], "easy"),
        ("Which festival of Nepal marks the beginning of the Nepali New Year?", "Bisket Jatra", ["Dashain", "Tihar", "Holi"], "hard"),
        ("Which is the busiest airport in Nepal?", "Tribhuvan International Airport", ["Pokhara International", "Bharatpur Airport", "Biratnagar Airport"], "medium"),
        ("Which is the second tallest mountain in the world?", "K2", ["Everest", "Kangchenjunga", "Lhotse"], "easy"),
        ("Which bird can fly backwards?", "Hummingbird", ["Eagle", "Sparrow", "Pigeon"], "hard"),
        ("Which planet is the largest in our solar system?", "Jupiter", ["Saturn", "Neptune", "Earth"], "easy"),
        ("Which planet is nearest to the Sun?", "Mercury", ["Venus", "Mars", "Earth"], "easy"),
        ("Which is the moon of our Earth?", "Moon", ["Io", "Titan", "Phobos"], "easy"),
        ("Which is the official currency of the USA?", "US Dollar", ["Euro", "Pound", "Yen"], "easy"),
        ("Which is the currency of China?", "Yuan", ["Yen", "Won", "Taka"], "easy"),
        ("Which is the currency of Japan?", "Yen", ["Yuan", "Won", "Ringgit"], "easy"),
        ("Which language is most widely spoken in the world by native speakers?", "Mandarin Chinese", ["English", "Spanish", "Hindi"], "medium"),
        ("Which is the most spoken language in Nepal?", "Nepali", ["Maithili", "Bhojpuri", "Newari"], "easy"),
        ("How many letters are in the English alphabet?", "26", ["24", "25", "27"], "easy"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci", ["Vincent van Gogh", "Pablo Picasso", "Michelangelo"], "medium"),
        ("Which is the largest ocean?", "Pacific Ocean", ["Atlantic", "Indian", "Arctic"], "easy"),
        ("Which is the largest country by population in the world (as of 2024)?", "India", ["China", "USA", "Indonesia"], "easy"),
        ("Which is the largest freshwater lake?", "Lake Superior", ["Baikal", "Caspian", "Victoria"], "hard"),
        ("Which is the largest coral reef system?", "Great Barrier Reef", ["Maldives", "Red Sea Coral", "Florida Reef"], "hard"),
        ("Which is the strongest muscle (relative to size) in the human body?", "Masseter (jaw)", ["Biceps", "Heart", "Gluteus maximus"], "hard"),
        ("Which part of the human body has the most bones?", "Hands", ["Feet", "Skull", "Spine"], "medium"),
    ]
    rows = _rows_from(entries)
    rows.extend(_gk_extras())
    return rows


def generate_nepal_questions(category_key, count=100):
    key = (category_key or "gk").lower()
    if key == "math":
        rows = _math_rows()
    elif key == "computer":
        rows = _computer_rows()
    elif key == "history":
        rows = _history_rows()
    elif key == "geography":
        rows = _geography_rows()
    elif key == "mythology":
        rows = _mythology_rows()
    else:
        rows = _gk_rows()

    random.shuffle(rows)

    def normalize(row):
        text = row.get("text", "").strip()
        options = []
        correct_count = 0
        for option in row.get("options", [])[:5]:
            t = str(option.get("text", "")).strip()[:200]
            c = bool(option.get("is_correct", False))
            if not t:
                continue
            correct_count += 1 if c else 0
            options.append({"text": t, "is_correct": c})
        if not text or len(options) < 2 or correct_count < 1:
            return None
        difficulty = row.get("difficulty", "medium")
        if difficulty not in DIFFICULTIES:
            difficulty = "medium"
        return {"text": text, "options": options, "difficulty": difficulty}

    easy_rows = []
    medium_rows = []
    hard_rows = []
    used = set()
    for row in rows:
        normalized = normalize(row)
        if normalized is None or normalized["text"] in used:
            continue
        used.add(normalized["text"])
        if normalized["difficulty"] == "easy":
            easy_rows.append(normalized)
        elif normalized["difficulty"] == "medium":
            medium_rows.append(normalized)
        else:
            hard_rows.append(normalized)

    random.shuffle(easy_rows)
    random.shuffle(medium_rows)
    random.shuffle(hard_rows)

    easy_n = min(len(easy_rows), max(10, count // 3))
    remaining = count - easy_n
    medium_n = min(len(medium_rows), max(0, remaining // 2))
    hard_n = min(len(hard_rows), remaining - medium_n)

    selected = easy_rows[:easy_n] + medium_rows[:medium_n] + hard_rows[:hard_n]
    if len(selected) < count:
        rest = easy_rows[easy_n:] + medium_rows[medium_n:] + hard_rows[hard_n:]
        random.shuffle(rest)
        selected.extend(rest[: count - len(selected)])

    return selected