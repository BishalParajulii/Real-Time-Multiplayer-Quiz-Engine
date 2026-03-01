import random


PROVINCES = [
    ("Koshi", "Biratnagar"),
    ("Madhesh", "Janakpur"),
    ("Bagmati", "Hetauda"),
    ("Gandaki", "Pokhara"),
    ("Lumbini", "Deukhuri"),
    ("Karnali", "Birendranagar"),
    ("Sudurpashchim", "Godawari"),
]

MOUNTAINS = [
    "Sagarmatha (Everest)",
    "Kanchenjunga",
    "Lhotse",
    "Makalu",
    "Cho Oyu",
    "Dhaulagiri",
    "Manaslu",
    "Annapurna I",
]

RIVERS = [
    "Koshi",
    "Gandaki",
    "Karnali",
    "Bagmati",
    "Rapti",
    "Mahakali",
    "Arun",
    "Seti",
]

DISTRICTS = [
    "Kathmandu",
    "Lalitpur",
    "Bhaktapur",
    "Kaski",
    "Chitwan",
    "Morang",
    "Sunsari",
    "Jhapa",
    "Banke",
    "Bardiya",
    "Dang",
    "Surkhet",
    "Kailali",
    "Kanchanpur",
    "Rupandehi",
    "Dolakha",
    "Syangja",
    "Ilam",
    "Dhankuta",
    "Gorkha",
]

TEMPLES = [
    ("Pashupatinath", "Shiva"),
    ("Muktinath", "Vishnu"),
    ("Manakamana", "Bhagwati"),
    ("Pathibhara", "Durga"),
    ("Janaki Temple", "Sita"),
    ("Changunarayan", "Vishnu"),
    ("Dakshinkali", "Kali"),
]

HISTORY_EVENTS = [
    ("Nepal unification campaign began", 1743),
    ("Comprehensive Peace Agreement", 2006),
    ("Nepal declared a federal democratic republic", 2008),
    ("Constitution of Nepal promulgated", 2015),
    ("People's Movement (Jana Andolan I)", 1990),
]


def _pick_wrong(correct, pool, count=3):
    choices = [item for item in pool if item != correct]
    random.shuffle(choices)
    return choices[:count]


def _option_pack(correct, pool):
    options = [{"text": str(correct), "is_correct": True}]
    for w in _pick_wrong(str(correct), [str(p) for p in pool], 3):
        options.append({"text": w, "is_correct": False})
    random.shuffle(options)
    return options


def _math_rows():
    rows = []
    for i in range(1, 140):
        a = (i * 3) % 70 + 10
        b = (i * 5) % 40 + 5
        op = i % 4
        if op == 0:
            ans = a + b
            q = f"A school in Kathmandu has {a} students in section A and {b} in section B. Total students?"
        elif op == 1:
            ans = a - b
            q = f"A trekking group had {a} people, and {b} returned early in Pokhara. How many remained?"
        elif op == 2:
            ans = a * b
            q = f"A tea shop in Ilam sells {a} cups daily for {b} days. How many cups in total?"
        else:
            ans = a
            total = a * b
            q = f"A bus traveled {total} km in {b} equal days across Nepal. Distance per day?"
        options_pool = [ans, ans + 1, ans - 1, ans + 2, ans - 2]
        rows.append({"text": q, "options": _option_pack(ans, options_pool)})
    return rows


def _computer_rows():
    rows = []
    base = [
        ("What does CPU stand for?", "Central Processing Unit", ["Central Program Utility", "Computer Processing Unit", "Core Performance Unit"]),
        ("Which language is used with Django?", "Python", ["Java", "PHP", "C++"]),
        ("What does RAM stand for?", "Random Access Memory", ["Run Access Module", "Read Access Memory", "Rapid Active Memory"]),
        ("Which protocol is used to load websites?", "HTTP", ["FTP", "SMTP", "SSH"]),
        ("Which data structure follows FIFO?", "Queue", ["Stack", "Tree", "Graph"]),
        ("Nepal's country code top-level domain is?", ".np", [".ne", ".npl", ".nt"]),
    ]
    for i in range(120):
        q, correct, wrong = base[i % len(base)]
        text = f"[Computer {i + 1}] {q}"
        options = [{"text": correct, "is_correct": True}] + [
            {"text": w, "is_correct": False} for w in wrong
        ]
        random.shuffle(options)
        rows.append({"text": text, "options": options})
    return rows


def _history_rows():
    rows = []
    for i in range(120):
        ev1, y1 = HISTORY_EVENTS[i % len(HISTORY_EVENTS)]
        ev2, y2 = HISTORY_EVENTS[(i + 1) % len(HISTORY_EVENTS)]
        diff = abs(y2 - y1)
        q = f"How many years between '{ev1}' ({y1}) and '{ev2}' ({y2}) in Nepal's history?"
        options = [diff, diff + 1, max(1, diff - 1), diff + 2]
        rows.append({"text": q, "options": _option_pack(diff, options)})

    fixed = [
        ("Who is known for unifying modern Nepal?", "Prithvi Narayan Shah", ["Jung Bahadur Rana", "Bhimsen Thapa", "Tribhuvan"]),
        ("In which year did Nepal become a federal democratic republic?", "2008", ["2006", "2010", "2015"]),
        ("In which year was Nepal's current constitution promulgated?", "2015", ["2008", "2012", "2017"]),
    ]
    for q, c, wrong in fixed:
        options = [{"text": c, "is_correct": True}] + [{"text": w, "is_correct": False} for w in wrong]
        random.shuffle(options)
        rows.append({"text": q, "options": options})
    return rows


def _geography_rows():
    rows = []
    for i in range(120):
        prov, cap = PROVINCES[i % len(PROVINCES)]
        q = f"What is the provincial capital of {prov} Province in Nepal?"
        pool = [c for _, c in PROVINCES]
        options = _option_pack(cap, pool)
        rows.append({"text": q, "options": options})

    for i in range(60):
        mountain = MOUNTAINS[i % len(MOUNTAINS)]
        q = f"Which of these is a mountain peak located in Nepal/Himalayan region?"
        wrong = ["Sahara", "Amazon", "Danube"]
        options = [{"text": mountain, "is_correct": True}] + [
            {"text": w, "is_correct": False} for w in wrong
        ]
        random.shuffle(options)
        rows.append({"text": q, "options": options})
    return rows


def _mythology_rows():
    rows = []
    for i in range(120):
        temple, deity = TEMPLES[i % len(TEMPLES)]
        q = f"In Nepal, the temple '{temple}' is primarily associated with which deity/figure?"
        pool = [d for _, d in TEMPLES]
        options = _option_pack(deity, pool)
        rows.append({"text": q, "options": options})
    return rows


def _gk_rows():
    rows = []
    fixed = [
        ("What is the capital city of Nepal?", "Kathmandu", ["Pokhara", "Biratnagar", "Lalitpur"]),
        ("How many provinces does Nepal have?", "7", ["5", "6", "8"]),
        ("Which is Nepal's official language?", "Nepali", ["Hindi", "English", "Newari"]),
        ("Lumbini is famous as the birthplace of whom?", "Gautama Buddha", ["King Janak", "Prithvi Narayan Shah", "Araniko"]),
    ]
    for i in range(120):
        q, c, wrong = fixed[i % len(fixed)]
        text = f"[GK {i + 1}] {q}"
        options = [{"text": c, "is_correct": True}] + [{"text": w, "is_correct": False} for w in wrong]
        random.shuffle(options)
        rows.append({"text": text, "options": options})

    for i in range(80):
        district = DISTRICTS[i % len(DISTRICTS)]
        q = f"{district} is a district of Nepal. Which country is it in?"
        options = [
            {"text": "Nepal", "is_correct": True},
            {"text": "India", "is_correct": False},
            {"text": "Bhutan", "is_correct": False},
            {"text": "Bangladesh", "is_correct": False},
        ]
        random.shuffle(options)
        rows.append({"text": q, "options": options})
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

    cleaned = []
    used = set()
    for row in rows:
        text = row.get("text", "").strip()
        options = row.get("options", [])
        if not text or text in used or len(options) < 2:
            continue
        used.add(text)

        normalized_options = []
        correct_count = 0
        for option in options[:4]:
            t = str(option.get("text", "")).strip()[:200]
            c = bool(option.get("is_correct", False))
            if not t:
                continue
            correct_count += 1 if c else 0
            normalized_options.append({"text": t, "is_correct": c})

        if len(normalized_options) >= 2 and correct_count >= 1:
            cleaned.append({"text": text, "options": normalized_options})

        if len(cleaned) >= count:
            break

    return cleaned
