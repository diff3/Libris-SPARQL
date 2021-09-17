# Libris SPARQL



## Desciption



**Nu är det möjligt att utforska data i Libris med hjälp av SPARQL**

Genom [Libris SPARQL-gränssnitt](https://libris.kb.se/sparql) går det att göra specifika sökningar i Libris och hämta Libris data, till exempel för underlag till statistik.

SPARQL (SPARQL Protocol and RDF Query Language) är ett kraftfullt frågespråk som möjliggör mycket avancerade sökningar i data. Resultaten kan dock kräva en del kunskap om hur data och praxis har ändrats genom tiderna och om vokabulären som används för att kunna tolkas korrekt.

För att komma igång med SPARQL finns [exempelsökfrågor](https://github.com/libris/librisxl/blob/develop/SPARQL-example-queries.md) framtagna som stöd.

Det finns allmänna exempelfrågor såsom "Hur många böcker ges ut i Sverige totalt varje år?". Det finns även mer specifika exempelfrågor såsom "Hur många böcker gavs ut på ett annat språk än svenska av svenska utgivare 2019?" eller "Vilka titlar har getts ut om coronapandemin 2019-2020 och coronaviruset?"

Genom att justera exempelfrågorna och klistra in dem i Libris SPARQL-gränssnittet kan du söka i Libris data och hämta datauttag.

Syftet med Libris SPARQL är att underlätta både avancerade sökningar och statistikuttag. Libris SPARQL kan användas av alla som är intresserade av att undersöka Librisdata.



## Install



On Mac Big Sur 11.6, start by open terminal

```Bash
# Install brew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install git python@3.9
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

git clone https://github.com/diff3/Libris-SPARQL
cd Libris-SPARQL
pip3 install -r requirements.txt
python3 main.py
```



##  Links



**Libris:** https://www.kb.se/samverkan-och-utveckling/nytt-fran-kb/nyheter-samverkan-och-utveckling/2021-09-15-libris-sparql.html

**Libris example queries:** https://github.com/libris/librisxl/blob/develop/SPARQL-example-queries.md

**Libris SPARQL page:** https://libris.kb.se/sparql/

**Libris SPARQL/Marc:** https://id.kb.se/vocab/

**Python3 SPARQL example:** https://rebeccabilbro.github.io/sparql-from-python/

**Pretty Print:** https://www.delftstack.com/howto/python/python-pretty-print-dictionary/

**W3C Python3 SPARQL:** https://www.w3.org/2009/Talks/0615-qbe/

**W3C SPARQL:** https://www.w3.org/TR/sparql11-query/






**Python program and examples by**

**Magnus Pettersson @2021**
