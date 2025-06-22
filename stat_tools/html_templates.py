class Templates:
    
    uniform_start = """
    <html>
      <head>
        <meta charset=\"UTF-8\">
        <link rel=\"stylesheet\" href=\"statute-stylesheet.css\">
        <title>N.R.S. &sect;&nbsp;{}</title>
      </head>
      <body>
        <header>
          <h1 id=\"header-heading\">{}{}</h1>
        </header>"""
    main_start = """
        <main>"""
    paragraph = """
          <p id=\"{}\">{}</p>"""
    table_start = """
          <p id=\"{}\">
            <table>"""
    thead_start = """
              <thead>"""
    thead_row_start = """
                <tr>"""
    th = """
                  <th>{}</th>"""
    td = """
                  <td>{}</td>"""
    thead_row_end = """
                </tr>"""
    tr_start = """
                <tr>"""
    tr_end = """
                </tr>"""
    thead_end = """
              </thead>"""
    tbody_start = """
              <tbody>"""
    tbody_end = """
              </tbody>"""
    table_end = """
            </table>
          </p>"""
    main_end = """
        </main>"""
    footer_start = """
        <footer>"""
    footer_section_start = """
          <section id=\"{}\">"""
    footer_heading = """
            <h2 class=\"footer-heading\">{}</h2>"""
    footer_list_start = """
            <ul>"""
    list_item = """
              <li>{}</li>"""
    source_list_item = """
              <li class=\"source\">{}</li>"""
    source = "<a href=\"{}\">{}</a>"
    xref_list_item = """
              <li class=\"xref\">{}</li>"""
    xref = "<a href=\"{}\">{}</a>"
    cross_reference = "<b>{}</b> see section <a href=\"{}\">{}</a>."
    annotation_list_item = """
              <li class=\"annotation\"><p>{}</p></li>"""
    footer_list_end = """
            </ul>"""
    footer_section_end = """
          </section>"""
    footer_end = """
        </footer>"""
    uniform_end = """
      </body>
    </html>"""
    
    link = "<a href=\"{}\">{}</a>"
    base_url = "https://www.nebraskalegislature.gov{}"
