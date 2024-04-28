import csv
import os
import genanki

def import_to_anki(csv_file_path, deck_name):
    # Define the Anki model with CSS
    model = genanki.Model(
        1607392319,  # Random model ID
        'Japanese Word Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Word_Reading'},
            {'name': 'Example Sentence 1'},
            {'name': 'Example Sentence 2'},
            {'name': 'Translation'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '''
                    <div class="card">
                        <div id="front">
                            <h1>{{Example Sentence 1}}</h1>
                            <hr>
                            <h1 id="word"><i>{{Word}}</i></h1>
                            <hr>
                        </div>
                    </div>
                ''',
                'afmt': '''
                    <div class="card">
                        <div id="back">
                            <h1 id="word"><i>{{Word}} | {{Word_Reading}}</i></h1>
                            <hr>
                            <h2>1.{{Example Sentence 1}}</h2>
                            <h2>2.{{Example Sentence 2}}</h2>
                            <hr>
                            <h2>{{Translation}}</h2>
                        </div>
                    </div>
                '''
            }
        ],
        css='''
            .card {
                font-family: MS PMincho;
            }

            #front {
            
              text-align: center;
            }

            #back {
                
                text-align: left;
                padding: 20px;
            }

            #word {
                color: #0000FF;
                font-size: 42px !important;
            @charset "utf-8";

@charset "utf-8";

@media screen and (min-width: 900px) {

    /* Limit font loading to wide screens to avoid performance hits on mobile. */
    @font-face {
        font-family: "KanjiStrokeOrders";
        src: local("KanjiStrokeOrders"), url("_kso.ttf");
    }

    @font-face {
        font-family: "Yu Mincho";
        src: local("Yu Mincho"), local("游明朝"), url("_yumin.ttf");
    }

    @font-face {
        font-family: "Yu Mincho";
        src: local("Yu Mincho Demibold"), local("游明朝 Demibold"), url("_yumindb.ttf");
        font-weight: 600;
    }

    b {
        font-weight: 600;
    }
}

* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}

.card {
    background-color: #fffaf0;
    color: #2a1b0a;
    font-family: "Noto Serif", "Noto Serif CJK JP", Yu Mincho, "Liberation Serif", "Times New Roman", Times, Georgia,
        Serif;
    font-size: 24px;
    text-align: left;
    line-height: 1.4;
    margin: 0 auto;
}

.card1 {
    color: inherit;
}

.card2 .jpsentence ruby rt {
    opacity: 0;
}

.card2 .jpsentence:hover ruby rt {
    opacity: 1;
}

@media screen and (min-width: 820px) {
    .card {
        background-color: #e5d7c9;
        display: flex;
        justify-content: center;
    }

    .wrap {
        width: 800px;
        padding: 0 5px 0;
        background-color: #fffaf0;
        border-left: 1px solid #c9bcbc;
        border-right: 1px solid #c9bcbc;
        min-height: 100vh;
    }

    .wrap .wrap {
        width: auto;
        padding: 0;
        min-height: 0;
        border: 0;
    }
}

hr {
    margin: 2px 0;
    clear: both;
    border: 0;
    border-top: 1px solid #c9bcbc;
}

/* links */
a {
    color: #532f2f;
}

a:hover {
    color: #722a2a;
}

a.hint {
    text-decoration: none;
    text-align: center;
    display: block;
}

/* Hide furigana on front */
nokana ruby rt {
    opacity: 0;
    font-size: 0;
    display: none;
}

notext b {
    background-color: black;
    color: transparent;
}

/* Top */
header {
    display: flex;
    clear: both;
}

header .tags {
    border-radius: 0px 0px 3px 3px;
}

header>div:not(:last-child) {
    margin-right: 3px;
}

/* Space between elements */

.sent-center {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-flow: column nowrap;
}

/* Japanese sentence */

.jpsentence {
    font-size: 35px;
}

/* Hide front side when the back is shown. */

.fside .jpsentence {
    display: none;
}

/* English */

div.ensentence>a.hint {
    color: #555;
    font-size: 14px;
    display: block;
    border: 1px solid #ccc;
    border-radius: 2.2px;
    padding: 2px 10px;
    margin: 4px 0;
}

div.ensentence>a.hint:hover {
    color: #111;
    background-color: rgba(0, 0, 0, 0.03);
}

/* Tags */

.tags {
    font-family: "Noto Sans", "Noto Sans CJK JP", "Liberation Sans", Arial, Sans, sans-serif;
    text-align: center;
    display: inline-block;
    text-transform: lowercase;
    background-color: #333;
    color: #fffaf0;
    font-weight: bold;
    padding: 1px 3px;
    margin: 0;
    cursor: pointer;
    border-radius: 3px;
    font-size: 12px;
    line-height: 14px;
}

/* AnkiDroid replay button */

.replaybutton {
    margin: 0;
    margin-right: 3px;
    text-decoration: none;
}

.replaybutton span {
    padding: 0;
    font-size: 16px;
}

.replaybutton span svg {
    fill: #fffaf0;
    background: #333;
    border-radius: 3px;
    vertical-align: top;
    min-width: 16px;
    min-height: 16px;
}

/* PC replay button */

a.replay-button {
    top: -0.125em;
    position: relative;
    margin: 0;
}

a.replay-button svg {
    height: 1em;
    width: 1em;
}

a.replay-button svg path {
    fill: #fffaf0;
}

a.replay-button svg circle {
    fill: #333;
}

/* Footer and links */

footer {
    font-size: 16px;
    text-align: center;
}

footer>a {
    text-decoration: none;
}

footer>a:after {
    content: "·";
    color: brown;
    display: inline-block;
    width: 6px;
}

footer>a:last-child:after {
    content: "";
    width: 0;
}

/* Vocab */

.vocab {
    margin-top: 16px;
}

.vocab div {
    display: inline-block;
}

.vocab br {
    display: none;
}

.vocab>.tags {
    vertical-align: top;
}

.notes>.tags {
    vertical-align: bottom;
}

/* Images */

.images {
    margin: 10px 0;
    display: grid;
    justify-items: center;
    align-items: start;
    align-content: start;
    justify-content: space-around;
    gap: 5px;
    grid-auto-columns: minmax(100px, 1fr);
    grid-auto-rows: minmax(100px, auto);
}
.images br, .images > * {
    display: none;
}
.images img {
    display: block;
    border-radius: 4px;
    filter: sepia(33%);
    max-width: 100%;
    max-height: 95vh;
}
.images img:nth-child(3n+1) {
  grid-column: 1;
}
.images img:nth-child(3n+2) {
  grid-column: 2;
}
.images img:nth-child(3n+3) {
  grid-column: 3;
}

/* Production cards */

.production b {
    visibility: hidden;
}

.strokeorder {
    text-align: center;
    font-size: 150px;
    font-family: KanjiStrokeOrders;
}

/* Morphman coloring */

.fside .jpsentence:hover [mtype="unknown"] {
    background-color: #ffff99;
}

.fside .jpsentence:hover [mtype="seen"] {
    background-color: #ffd1b3;
}

.fside .jpsentence:hover [mtype="known"] {
    background-color: #b3e6cc;
}

.fside .jpsentence:hover [mtype="mature"] {
    background-color: transparent;
}

.fside .jpsentence:hover [priority="true"] {
    color: inherit;
}

.fside .jpsentence:hover [frequency="true"] {
    color: inherit;
}

del.MorphManHide,
del.morphmanhide {
    display: none;
}

/* Fix for Yomichan defs */

ul,
ol {
    list-style-type: none;
    display: inline;
    margin: 0px;
    padding: 0px;
}

/* Fix for Yomichan pitch accents */

.vocab ol>li {
    display: inline;
}

.vocab ol>li:after {
    content: "・";
}

.vocab ol>li:last-child:after {
    content: "";
}

/* Night Mode */

.nightMode.card {
    background-color: #2F2F31;
}

.nightMode .wrap {
    color: #FFFFFF;
    background-color: inherit;
}

.nightMode .tags {
    background-color: #FFFFFF;
    color: #2F2F31;
}

.nightMode a.replay-button svg path {
    fill: #2F2F31;
}

.nightMode a.replay-button svg circle {
    fill: #FFFFFF;
}

.nightMode .replaybutton span svg {
    fill: #2F2F31;
    background: #FFFFFF;
}

.nightMode a {
    color: #c7493a;
}

.nightMode a:hover {
    color: #a33327;
}

.nightMode .jpsentence b {
    color: gray;
}

.nightMode .images>img {
    filter: sepia(0%);
}

.nightMode div.ensentence>a.hint {
    color: #FFFFFF;
    border: 1px solid #FFFFFF;
}

.nightMode div.ensentence>a.hint:hover {
    color: gray;
    background-color: rgba(0, 0, 0, 0.20);
}

/* Don't select furigana */

.jpsentence ruby rt {
    user-select: none;
}

* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
}

.card {
    background-color: #fffaf0;
    color: #2a1b0a;
    font-family: "Noto Serif", "Noto Serif CJK JP", Yu Mincho, "Liberation Serif", "Times New Roman", Times, Georgia,
        Serif;
    font-size: 24px;
    text-align: left;
    line-height: 1.4;
    margin: 0 auto;
}


            
           
        '''
    )


    # Create a new Anki deck
    deck = genanki.Deck(
        2059400110,  # Random deck ID
        deck_name)

    # Read data from CSV and add to Anki deck
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            note = genanki.Note(
                model=model,
                fields=[
                    row['Word'],
                    row['Word_Reading'],
                    row['Example Sentence 1'],
                    row['Example Sentence 2'],
                    row['Translation'],
                ])
            deck.add_note(note)

    # Create Anki package
    package = genanki.Package(deck)
    package.write_to_file(f'{deck_name}.apkg')

    # move the apkg file to the correct directory ./files
    os.rename(f'{deck_name}.apkg', f'./files/{deck_name}.apkg')

    print(f'Anki package "{deck_name}.apkg" created successfully.')

# Replace 'Japanese_Word_Examples.csv' with the path to your CSV file
csv_file_path = './files/Japanese_Word_Examples.csv'

#log csv file path
print(csv_file_path)

# Replace 'Japanese Words' with the desired name for your Anki deck
deck_name = 'Japanese_AI_Vocab_Deck'

import_to_anki(csv_file_path, deck_name)
