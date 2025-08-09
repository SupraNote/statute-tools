import re


def sort_stat(stats):
    g4_list = []
    g4 = re.compile(r"\d{2}-\d{4}|\d{2}-\d{4}\.\d{2}|\d{2}-\d{2},\d{3}|\d{2}-\d{2},\d{3}\.\d{2}")
    g3_list = []
    g3 = re.compile(r"\d{2}-\d{3}|\d{2}-\d{3}\.\d{2}|\d{2}-\d,\d{3}|\d{2}-\d,\d{3}\.\d{2}")
    g2_list = []
    g2 = re.compile(r"\d-\d{4}|\d-\d{4}\.\d{2}|\d-\d{2},\d{3}|\d-\d{2},\d{3}\.\d{2}")
    g1_list = []
    g1 = re.compile(r"\d-\d{3}|\d-\d,\d{3}\.\d{2}|\d-\d{3}\.\d{2}|\d-\d,\d{3}")
    
    for stat in stats:
        if re.search(g4, stat):
            if re.search(re.compile(r"\d{2}-\d{2},\d{3}\.\d{2}|\d{2}-\d{2},\d{3}"), stat):
                chapter = int(stat[0:2])
                article = int(stat[3:5])
                section = float(stat[6:])
                g4_tuple_1 = (stat, chapter, article, section)
                g4_list.append(g4_tuple_1)
            elif re.search(re.compile(r"\d{2}-\d{4}\.\d{2}|\d{2}-\d{4}"), stat):
                chapter = int(stat[0:2])
                article = int(stat[3:5])
                section = float(stat[5:])
                g4_tuple_2 = (stat, chapter, article, section)
                g4_list.append(g4_tuple_2)
        elif re.search(g3, stat):
            if re.search(re.compile(r"\d{2}-\d,\d{3}\.\d{2}|\d{2}-\d,\d{3}"), stat):
                chapter = int(stat[0:2])
                article = int(stat[3])
                section = float(stat[5:])
                g3_tuple_1 = (stat, chapter, article, section)
                g3_list.append(g3_tuple_1)
            elif re.search(re.compile(r"\d{2}-\d{3}\.\d{2}|\d{2}-\d{3}"), stat):
                chapter = int(stat[0:2])
                article = int(stat[3])
                section = float(stat[4:])
                g3_tuple_2 = (stat, chapter, article, section)
                g3_list.append(g3_tuple_2)
        elif re.search(g2, stat):
            if re.search(re.compile(r"\d-\d{2},\d{3}\.\d{2}|\d-\d{2},\d{3}"), stat):
                chapter = int(stat[0])
                article = int(stat[2:4])
                section = float(stat[5:])
                g2_tuple_1 = (stat, chapter, article, section)
                g2_list.append(g2_tuple_1)
            elif re.search(re.compile(r"\d-\d{4}\.\d{2}|\d-\d{4}"), stat):
                chapter = int(stat[0])
                article = int(stat[2:4])
                section = float(stat[4:])
                g2_tuple_2 = (stat, chapter, article, section)
                g2_list.append(g2_tuple_2)
        elif re.search(g1, stat):
            if re.search(re.compile(r"\d-\d,\d{3}\.\d{2}|\d-\d,\d{3}"), stat):
                chapter = int(stat[0])
                article = int(stat[2])
                section = float(stat[4:])
                g1_tuple_1 = (stat, chapter, article, section)
                g1_list.append(g1_tuple_1)
            elif re.search(re.compile(r"\d-\d{3}\.\d{2}|\d-\d{3}"), stat):
                chapter = int(stat[0])
                article = int(stat[2])
                section = float(stat[3:])
                g1_tuple_2 = (stat, chapter, article, section)
                g1_list.append(g1_tuple_2)
    
    sorted_tuples = []
    g1_sort = sorted(g1_list, key=lambda item: (item[1], item[2], item[3]))
    sorted_tuples.append(g1_sort)
    g2_sort = sorted(g2_list, key=lambda item: (item[1], item[2], item[3]))
    sorted_tuples.append(g2_sort)
    g3_sort = sorted(g3_list, key=lambda item: (item[1], item[2], item[3]))
    sorted_tuples.append(g3_sort)
    g4_sort = sorted(g4_list, key=lambda item: (item[1], item[2], item[3]))
    sorted_tuples.append(g4_sort)
    print(sorted_tuples)
    
    sorted_stats = []
    
    for stat in g1_sort:
        sorted_stats.append(stat[0])
    
    for stat in g2_sort:
        sorted_stats.append(stat[0])
    
    for stat in g3_sort:
        sorted_stats.append(stat[0])
    
    for stat in g4_sort:
        sorted_stats.append(stat[0])
    
    print(sorted_stats)
    