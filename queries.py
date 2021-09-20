#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
All example queries from Libris
https://github.com/libris/librisxl/blob/develop/SPARQL-example-queries.md

Written by Magnus Pettersson @2021
"""

query = list()

# 0. Hur många romaner gavs ut under 2019?
query.append("""
    SELECT COUNT(DISTINCT ?novel) AS ?count {
        ?novel bf2:instanceOf/bf2:genreForm/(owl:sameAs|skos:exactMatch)* marc:Novel ; # noqa
        kbv:publication/kbv:year "2019"
    }
""")

# 1. Vilka språk finns Selma Lagerlöf översatt till?
query.append("""
    SELECT DISTINCT ?language ?langName {
        [] bf2:contribution [
            a kbv:PrimaryContribution ;
            bf2:role rel:author ;
            bf2:agent <https://libris.kb.se/qn247n18248vs58#it>
        ] ;
        bf2:translationOf/a bf2:Work ;
        bf2:language ?language .
        ?language skos:prefLabel ?langName
        FILTER(lang(?langName) = 'sv')
    }
""")

# 2. Vilka språk har svensk utgivning översatts till mellan åren 2000-2010?
query.append("""
    SELECT DISTINCT ?language ?langName {
        [] bf2:instanceOf [
            bf2:language ?language ;
            bf2:translationOf/bf2:language lge:swe
        ] ;
        kbv:publication/kbv:year ?year .
        ?language skos:prefLabel ?langName
        FILTER(str(?year) >= "2000" && str(?year) < "2010")
        FILTER(lang(?langName) = 'sv')
    }
 """)

# 3. Vilka svenska skönlitterära titlar har översatts till spanska 1990?
query.append("""
    SELECT ?spanishInstance ?spanishTitle ?swedishTitle {
        VALUES ?genre {
            marc:FictionNotFurtherSpecified
            marc:Drama
            marc:Essay
            marc:Novel
            marc:HumorSatiresEtc
            marc:Letter
            marc:ShortStory
            marc:MixedForms
            marc:Poetry
        }
        ?spanishInstance kbv:publication/kbv:year "1990" ;
        bf2:instanceOf ?work .
        ?work bf2:genreForm/(owl:sameAs|skos:exactMatch)* ?genre ;
        bf2:language lge:spa ;
        bf2:translationOf [
            a bf2:Work ;
            bf2:language lge:swe
        ]
        OPTIONAL {
            ?spanishInstance bf2:title [
                a bf2:Title ;
                bf2:mainTitle ?spanishTitle
            ]
        }
        OPTIONAL {
            ?work bf2:title [ a bf2:Title ;
                    bf2:mainTitle ?swedishTitle ]
        }
    }
""")

# 4. Vilka serietecknare har översatts till svenska under 1980-2020?
query.append("""
    SELECT DISTINCT ?cartoonist CONCAT(?givenName, " ", ?familyName) {
        VALUES ?genre {
            marc:ComicStrip
            marc:ComicOrGraphicNovel
        }
        [] bf2:instanceOf [ bf2:genreForm/(owl:sameAs|skos:exactMatch)* ?genre ; # noqa
                bf2:language lge:swe ;
                bf2:translationOf/a bf2:Work ;
                bf2:contribution [ a kbv:PrimaryContribution ;
                        bf2:agent ?cartoonist ] ] ;
            kbv:publication/kbv:year ?year
        OPTIONAL {
            ?cartoonist foaf:givenName ?givenName ;
                foaf:familyName ?familyName
        }
        FILTER(str(?year) >= "1980" && str(?year) < "2020")
        FILTER(!isBlank(?cartoonist))
    }
""")

# 5. Hur många franska barnböcker översättes till svenska under 1980-2020?
query.append("""
    SELECT COUNT(DISTINCT ?book) AS ?count {
        ?book bf2:issuance kbv:Monograph ;
        bf2:instanceOf [ a bf2:Text ;
        bf2:intendedAudience/(owl:sameAs|skos:exactMatch)* marc:Juvenile ;
        bf2:language lge:swe ;
        bf2:translationOf [ a bf2:Work ;
        bf2:language lge:fre ] ] ;
        kbv:publication/kbv:year ?year
        FILTER(str(?year) >= "1980" && str(?year) < "2020")
    }
""")

# 6. Hur många böcker gavs ut på samiska utifrån aspekterna genre, målgrupp och utgivningsår? # noqa
query.append("""
    SELECT ?year ?audience ?genre COUNT(?book) AS ?count {
        VALUES ?language {
            lge:smi
            lge:smj
            lge:sme
            lge:sjd
            lge:sju
            lge:sma
            lge:smn
            lge:sje
            lge:sia
            lge:sjt
            lge:sms
            lge:sjk
        }

        ?book bf2:issuance kbv:Monograph ;
        bf2:instanceOf [
            a bf2:Text ;
            bf2:language ?language ;
            bf2:intendedAudience ?audience ;
            bf2:genreForm ?genre
        ];
        kbv:publication/kbv:year ?year
        FILTER(!isBlank(?genre))
    }
    ORDER BY ?year ?audience ?genre
""")

# 7. Hur många facklitterära böcker gav förlaget Natur och Kultur ut mellan åren 1920-2000? # noqa
query.append("""
    SELECT COUNT(DISTINCT ?book) AS ?count {
        ?book bf2:issuance kbv:Monograph ;
        bf2:instanceOf [
            a bf2:Text ;
            bf2:genreForm/(owl:sameAs|skos:exactMatch)* marc:NotFictionNotFurtherSpecified # noqa
        ] ;
        kbv:publication [
            a kbv:PrimaryPublication ;
            bf2:agent/rdfs:label ?agent ;
            kbv:year ?year
        ]
        FILTER(regex(?agent, "Natur (&|och) Kultur|^N&K$", "i"))
        FILTER(str(?year) >= "1920" && str(?year) < "2000")
    }
""")

# 8. Hur många böcker ges ut av egenutgivare varje år?
query.append("""
    SELECT ?year COUNT(DISTINCT ?book) AS ?count {
        ?book bf2:issuance kbv:Monograph ;
        bf2:instanceOf/a bf2:Text ;
        kbv:publication [
            a kbv:PrimaryPublication ;
            kbv:year ?year
        ] ;
        ^bf2:itemOf/kbv:cataloguersNote "nbegenutg"
    }
    ORDER BY ?year
""")

# 9. Hur många böcker har det getts ut inom barnlitteratur i Sverige varje år?
query.append("""
    SELECT ?year COUNT(DISTINCT ?book) AS ?count {
        ?book bf2:issuance kbv:Monograph ;
        bf2:instanceOf [
            a bf2:Text ;
            bf2:intendedAudience/(owl:sameAs|skos:exactMatch)* marc:Juvenile
        ] ;
        kbv:publication [
            a kbv:PrimaryPublication ;
            kbv:country ctry:sw ;
            kbv:year ?year
        ]
    }
    ORDER BY ?year
""")

# 10. Hur många böcker ges ut i Sverige totalt varje år?
query.append("""
    SELECT ?year COUNT(DISTINCT ?book) AS ?count {
      ?book bf2:issuance kbv:Monograph ;
          bf2:instanceOf/a bf2:Text ;
          kbv:publication [
            a kbv:PrimaryPublication ;
            kbv:country ctry:sw ;
            kbv:year ?year
        ]
    }
    ORDER BY ?year
""")

# 11. Hur många böcker har digitaliserats under 2020?
query.append("""
    SELECT COUNT(DISTINCT ?digiBook) AS ?count {
        ?digiBook bf2:issuance kbv:Monograph ;
        bf2:instanceOf/a bf2:Text ;
        kbv:publication/kbv:year "2020" ;
        ^foaf:primaryTopic/kbv:bibliography <https://libris.kb.se/library/DIGI>
    }
""")

# 12. Vilka titlar digitaliserades 2019?
query.append("""
    SELECT ?digi ?title {
        ?digi kbv:publication/kbv:year "2019" ;
        ^foaf:primaryTopic/kbv:bibliography <https://libris.kb.se/library/DIGI> . # noqa
        OPTIONAL {
            ?digi bf2:title [
                a bf2:Title ;
                bf2:mainTitle ?title
            ]
        }
    }
    ORDER BY ?title
""")

# 13. Hur många svenska utgivare fanns det 1970?
query.append("""
    SELECT COUNT(DISTINCT ?publisher) AS ?count {
        [] a kbv:PrimaryPublication ;
        kbv:country ctry:sw ;
        kbv:year "1970" ;
        bf2:agent/rdfs:label ?publisher
    }
""")

# 14. Hur många barnböcker gavs ut på ett annat språk än svenska av svenska utgivare 2019? # noqa
query.append("""
    SELECT COUNT(DISTINCT ?book) AS ?count {
        ?book bf2:issuance kbv:Monograph ;
        bf2:instanceOf [
            a bf2:Text ;
            bf2:intendedAudience/(owl:sameAs|skos:exactMatch)* marc:Juvenile ;
            bf2:language ?language
        ] ;
        kbv:publication [
            a kbv:PrimaryPublication ;
            kbv:country ctry:sw ;
            kbv:year "2019"
        ]
        FILTER(?language != lge:swe)
    }
""")

# 15. Vilka titlar har getts ut om coronapandemin 2019-2020 och coronaviruset?
query.append("""
     SELECT DISTINCT ?instance ?title {
        VALUES ?subject {
            sao:Covid-19
            sao:Coronapandemin%202019-2020%20
            sao:Coronavirus
        }
        ?instance bf2:instanceOf/bf2:subject ?subject
        OPTIONAL {
            ?instance bf2:title [
                a bf2:Title ;
                bf2:mainTitle ?title
            ]
        }
    }
""")

# 16. Hur många titlar har getts ut om coronapandemin 2019-2020 och coronaviruset? # noqa
query.append("""
    SELECT COUNT(DISTINCT ?instance) {
        VALUES ?subject {
            sao:Covid-19
            sao:Coronapandemin%202019-2020%20
            sao:Coronavirus
        }
        ?instance bf2:instanceOf/bf2:subject ?subject
    }
""")
