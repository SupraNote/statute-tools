from bs4 import BeautifulSoup
from stat_tools.html_templates import Templates
from stat_tools.cleaner import clean_source
import requests
import re


def compose_section(path, section_url, designator_tag, catchline_tag):
    raw_statute = requests.get(section_url).text
    clean_statute = re.sub("′", "&prime;", raw_statute)
    parsed_statute = BeautifulSoup(clean_statute, "html.parser")
    full_statute = parsed_statute.find("div", "statute")
    
    # <header>
    designator = full_statute.find(designator_tag).get_text().strip() + " "
    catchline = full_statute.find(catchline_tag).get_text().strip()
    
    # initialize file
    file = path + designator.strip() + "html"
    f = open(file, "a")
    f.write(Templates.uniform_start.format(clean_source(designator.strip()), clean_source(designator),
                                           clean_source(catchline)))
    
    # <main>
    main_p = full_statute.find_all("p", "text-justify", recursive=False)
    if len(main_p) == 0:
        pass
    else:
        f.write(Templates.main_start)
        i = 1
        for p in main_p:
            table = p.find("table")
            if table is not None:
                f.write(Templates.table_start.format(i))
                rows = table.find_all("tr")
                f.write(Templates.thead_start)
                f.write(Templates.thead_row_start)
                ths = rows[0].find_all("td")
                for th in ths:
                    clean_th = re.sub("\n", " ", th.get_text())
                    f.write(Templates.th.format(clean_th))
                f.write(Templates.thead_row_end)
                f.write(Templates.thead_end)
                rows.pop(0)
                f.write(Templates.tbody_start)
                for row in rows:
                    f.write(Templates.tr_start)
                    tds = row.find_all("td")
                    for td in tds:
                        clean_td = re.sub("\n", " ", td.get_text())
                        f.write(Templates.td.format(clean_td))
                    f.write(Templates.tr_end)
                f.write(Templates.tbody_end)
                f.write(Templates.table_end)
            elif table is None:
                f.write(Templates.paragraph.format(i, clean_source(str(p))))
            i += 1
        f.write(Templates.main_end)
    
    # <footer>
    footer_divs = full_statute.find_all("div", recursive=False)
    footer_sections = []
    for div in footer_divs:
        footer_sections.append(div.find("h2").get_text())
    
    if len(footer_sections) == 0:
        pass
    else:
        f.write(Templates.footer_start)
        for section in footer_divs:
            if section.find("h2").get_text() == "Source":
                # <section id="source">
                f.write(Templates.footer_section_start.format("source"))
                f.write(Templates.footer_heading.format("Source"))
                f.write(Templates.footer_list_start)
                amendments = section.find_all("li")
                for amendment in amendments:
                    link = amendment.find("a")
                    if link is None:
                        f.write(Templates.list_item.format(clean_source(amendment.get_text())))
                    else:
                        line = clean_source(
                            Templates.source.format(Templates.base_url.format(link.get("href")),
                                                    amendment.get_text().strip())
                        )
                        f.write(Templates.source_list_item.format(line))
                f.write(Templates.footer_list_end)
                f.write(Templates.footer_section_end)
            elif section.find("h2").get_text() == "Cross References":
                # <section id="xrefs">
                f.write(Templates.footer_section_start.format("xrefs"))
                f.write(Templates.footer_heading.format("Cross References"))
                f.write(Templates.footer_list_start)
                xrefs = section.find_all("li")
                for xref in xrefs:
                    act = xref.find("span").get_text()
                    anchor = xref.find("a")
                    if anchor is None:
                        f.write(Templates.xref_list_item.format(xref.get_text().strip()))
                    else:
                        href = anchor.get("href")
                        anchor_text = anchor.get_text()
                        full_url = Templates.base_url.format(href)
                        line = Templates.cross_reference.format(act, full_url, anchor_text)
                        f.write(Templates.xref_list_item.format(line))
                f.write(Templates.footer_list_end)
                f.write(Templates.footer_section_end)
            elif section.find("h2").get_text() == "Annotations":
                # <section id="annotations">
                f.write(Templates.footer_section_start.format("annotations"))
                f.write(Templates.footer_heading.format("Annotations"))
                f.write(Templates.footer_list_start)
                annotations = section.find_all("li")
                for annotation in annotations:
                    paragraph = annotation.find("p").get_text()
                    f.write(Templates.annotation_list_item.format(paragraph))
                f.write(Templates.footer_list_end)
                f.write(Templates.footer_section_end)
        
        f.write(Templates.footer_end)
    
    f.write(Templates.uniform_end)


