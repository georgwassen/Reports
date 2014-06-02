#!/usr/bin/env python
# vim: set fileencoding=utf8 :

from time import *

class Bootsklasse(object):
    abk = ''
    short = ''
    anz_ruderer = 0
    hat_st = 0
    def __init__(self, abk, short, anz, st):
        self.abk = abk
        self.short = short
        self.anz_ruderer = anz
        self.hat_st = st

bootsklassen = (
        Bootsklasse(u'1x', u'Einer', 1, 0),
        Bootsklasse(u'2x', u'Doppelzweier', 2, 0),
        Bootsklasse(u'2-', u'Zweier o. St.', 2, 0),
        Bootsklasse(u'2+', u'Zweier m. St.', 2, 1),
        Bootsklasse(u'4x', u'Doppelvierer o. St.', 4, 0),
        Bootsklasse(u'4x+', u'Doppelvierer m. St.', 4, 1),
        Bootsklasse(u'4-', u'Vierer o. St.', 4, 0),
        Bootsklasse(u'4+', u'Vierer m. St.', 4, 1),
        Bootsklasse(u'8+', u'Achter m. St.', 8, 1)
        )

class Klasse(object):
    abk = ''
    short = ''
    jhg_von = 0
    jhg_bis = 0
    def __init__(self, abk, short, von, bis):
        self.abk = abk
        self.short = short
        lt = localtime()
        jahr = lt[0]
        self.jhg_von = jahr - bis
        self.jhg_bis = jahr - von

klassen = (
        Klasse(u'JF {b} B', u'Juniorinnen B {b}', 15, 16),
        Klasse(u'JM {b} B', u'Junioren B {b}', 15, 16),
        Klasse(u'JF {b} A', u'Juniorinnen A {b}', 17, 18),
        Klasse(u'JM {b} A', u'Junioren A {b}', 17, 18),
        Klasse(u'SF {b} B', u'Seniorinnen B {b}', 19, 22),
        Klasse(u'SM {b} B', u'Senioren B {b}', 19, 22),
        Klasse(u'SF {b} A', u'Seniorinnen A {b}', 23, 200),
        Klasse(u'SM {b} A', u'Senioren A {b}', 23, 200)
        )

vereinsbezeichnungen = (
        u'ARC',
        u'BSG',
        u'ClfW',
        u'TuS',
        u'Post-SV',
        u'RB',
        u'Rugm.',
        u'RG',
        u'RC',
        u'RK',
        u'Rvg.',
        u'RZ',
        u'Rvg.',
        u'SC',
        u'SG',
        u'SK',
        u'SRR',
        u'SRV',
        u'SV',
        u'Spgm.',
        u'Turn-RV',
        u'WSC',
        u'WSV'
        )

staedte = (
u'Berlin',
u'Hamburg',
u'München',
u'Köln',
u'Frankfurt am Main',
u'Stuttgart',
u'Düsseldorf',
u'Dortmund',
u'Essen',
u'Bremen',
u'Dresden',
u'Leipzig',
u'Hannover',
u'Nürnberg',
u'Duisburg',
u'Bochum',
u'Wuppertal',
u'Bielefeld',
u'Bonn',
u'Münster',
u'Karlsruhe',
u'Mannheim',
u'Augsburg',
u'Wiesbaden',
u'Gelsenkirchen',
u'Mönchengladbach',
u'Braunschweig',
u'Chemnitz',
u'Aachen',
u'Kiel',
u'Halle (Saale)',
u'Magdeburg',
u'Krefeld',
u'Freiburg im Breisgau',
u'Lübeck',
u'Oberhausen',
u'Erfurt',
u'Rostock',
u'Mainz',
u'Kassel',
u'Hagen',
u'Saarbrücken',
u'Hamm',
u'Mülheim an der Ruhr',
u'Ludwigshafen am Rhein',
u'Leverkusen',
u'Potsdam',
u'Oldenburg',
u'Osnabrück',
u'Solingen',
u'Herne',
u'Neuss',
u'Heidelberg',
u'Darmstadt',
u'Paderborn',
u'Regensburg',
u'Ingolstadt',
u'Würzburg',
u'Wolfsburg',
u'Fürth',
u'Ulm',
u'Heilbronn',
u'Offenbach am Main',
u'Göttingen',
u'Bottrop',
u'Pforzheim',
u'Recklinghausen',
u'Reutlingen',
u'Koblenz',
u'Remscheid',
u'Bergisch Gladbach',
u'Bremerhaven',
u'Jena',
u'Trier',
u'Erlangen',
u'Moers')

vornamen_w = (
u'Anna'
u'Lea',
u'Leah',
u'Sarah',
u'Sara',
u'Hannah',
u'Hanna',
u'Michelle',
u'Laura',
u'Lisa',
u'Lara',
u'Lena',
u'Julia',
u'Johanna',
u'Marie',
u'Leonie',
u'Annika',
u'Katharina',
u'Sophie',
u'Sofie',
u'Antonia',
u'Emily',
u'Emilie',
u'Alina',
u'Melina',
u'Jasmin',
u'Yasmin',
u'Nina',
u'Emma',
u'Lina',
u'Celina',
u'Luisa',
u'Louisa',
u'Jacqueline',
u'Alexandra',
u'Carolin',
u'Caroline',
u'Karoline',
u'Kim',
u'Nele',
u'Neele',
u'Sofia',
u'Sophia',
u'Vanessa',
u'Paula',
u'Melissa')

vornamen_m = (
u'Lukas'
u'Lucas',
u'Jan',
u'Tim',
u'Finn',
u'Fynn',
u'Leon',
u'Niklas',
u'Niclas',
u'Tom',
u'Jonas',
u'Jannik',
u'Yannik',
u'Yannick',
u'Yannic',
u'Luca',
u'Luka',
u'Philipp',
u'Alexander',
u'Marvin',
u'Maximilian',
u'Daniel',
u'Julian',
u'Jakob',
u'Jacob',
u'Kevin',
u'Lennard',
u'Lennart',
u'Paul',
u'Florian',
u'Felix',
u'Moritz',
u'Nico',
u'Niko',
u'Simon',
u'Tobias',
u'Jonathan',
u'Max',
u'David',
u'Fabian',
u'Justin',
u'Ole',
u'Marcel',
u'Dominic',
u'Dominik',
u'Nick')

nachnamen = (
u'Ablaßmeier',
u'Absatz',
u'Achtelik',
u'Aden',
u'Adler',
u'Adomat',
u'Aff',
u'Affelt',
u'Agnischock',
u'Agunte',
u'Ahmseder',
u'Ahn',
u'Albersmann',
u'Alex',
u'Alten zu',
u'Altena',
u'Altwein',
u'Ambroselling',
u'Amhofer',
u'Ammerschuber',
u'Amon',
u'Anders',
u'Andörfer',
u'Andrejska',
u'Andress',
u'Andreya',
u'Angermeyer',
u'Anna',
u'Appenheimer',
u'Apt',
u'Arbeit',
u'Aretz',
u'Arndt',
u'Arnsbeck',
u'Arntz',
u'Arth',
u'Artzinger',
u'Aschmetkat',
u'Assemin',
u'Assenmacher',
u'Audt',
u'Auerbeck',
u'Autrum',
u'Ax',
u'Ayremhoff',
u'Baber',
u'Bachler',
u'Back',
u'Backzan',
u'Badtke',
u'Badzinski',
u'Baier',
u'Bakus',
u'Bald',
u'Baldes',
u'Baleska',
u'Balg',
u'Balion',
u'Balkartat',
u'Ballweber',
u'Bandrowski',
u'Bangert',
u'Barbaruk',
u'Bärenreiter',
u'Barfuß',
u'Barmführer',
u'Barnfeld',
u'Baron',
u'Bartel',
u'Bartels',
u'Bartetzko',
u'Barthölleck',
u'Bartlewski',
u'Bäsecke',
u'Bathelmes',
u'Baubanz',
u'Bauch',
u'Bauendahl',
u'Bäumert',
u'Bautsch',
u'Baxa',
u'Beren',
u'Begander',
u'Beba',
u'Beer',
u'Begerl',
u'Behl',
u'Behounka',
u'Behrenberg',
u'Behrendt',
u'Behrens',
u'Beierlein',
u'Bein',
u'Beitzer',
u'Belchaus',
u'Bellersen',
u'Bellwon',
u'Belting',
u'Bencka',
u'Bencka',
u'Bender',
u'Bendig',
u'Bendt',
u'Bengsch',
u'Benson',
u'Bente',
u'Benzmann',
u'Berblering',
u'Berghold',
u'Berlejung',
u'Bernecker',
u'Bernet',
u'Bernevuer',
u'Berngard',
u'Bernhardt',
u'Bernotat',
u'Berns',
u'Bertuch',
u'Bestfleisch',
u'Bets',
u'Bet',
u'Bethig',
u'Bettmesser',
u'Beuckmann',
u'Beutenmüller',
u'Beutgen',
u'Beutlrock',
u'Bexel',
u'Beyerbach',
u'Beyschwang',
u'Beÿseihs ',
u'Beythien',
u'Bibersteiner',
u'Bickert',
u'Biebel',
u'Bielmeier',
u'Bienenstein',
u'Bierfreund',
u'Bieringer',
u'Biesold',
u'Biler',
u'Bilska',
u'Bina',
u'Bindernagel',
u'Bisch',
u'Bischleb',
u'Bischofsberger',
u'Bischop',
u'Bisser',
u'Bitte',
u'Bitter',
u'Bittera',
u'Bjeske',
u'Blacha',
u'Blattert',
u'Blaufuss',
u'Bleck',
u'Bleichert',
u'Blem',
u'Blenke',
u'Blison',
u'Bloder',
u'Blödner',
u'Bluhm',
u'Bodai',
u'Böddinghaus',
u'Bodlos',
u'Bohdal',
u'Böhret',
u'Bohsel',
u'Bojorr',
u'Bombas',
u'Bömming',
u'Book',
u'Bordien',
u'Borgemeister',
u'Borgers',
u'Borna',
u'Bornscheuer',
u'Bornstein',
u'Boroch',
u'Boronstein',
u'Borz',
u'Boß',
u'Bossin',
u'Both',
u'Bothmann',
u'Bottenberg',
u'Bötzhöfer',
u'Boullion',
u'Brabänder',
u'Brachem',
u'Bramkamp',
u'Brandis',
u'Brandl',
u'Branz',
u'Brassler',
u'Brauer',
u'Braungart',
u'Brem',
u'Bredfeld',
u'Breinich',
u'Breitenborn',
u'Bremshey',
u'Brenzinger',
u'Breznice',
u'Brocke',
u'Broja',
u'Brokogne ',
u'Brolikowski',
u'Brücker',
u'Bruen ',
u'Brümmer',
u'Brüninghaus',
u'Brunn',
u'Bruse',
u'Brüsemeister',
u'Brüsse',
u'Bruzdewicz',
u'Buba',
u'Bublitz',
u'Bublitz',
u'Büchau',
u'Buchhauser',
u'Buchholz',
u'Buff',
u'Buhleier',
u'Bukal',
u'Bukowski',
u'Büldmann',
u'Bullmann',
u'Bundel',
u'Bürckel',
u'Burgardt',
u'Burschinski',
u'Bürthel',
u'Burzius',
u'Buschmann',
u'Büsing',
u'Bütehorn',
u'Calacuro',
u'Campe',
u'Cardung',
u'Caspar',
u'Caul',
u'Cecalek',
u'Cercevic',
u'Charlier',
u'Chlapek',
u'Chotjewitsch',
u'Christiani',
u'Cicéron',
u'Cichopad',
u'Ciesielcyk',
u'Cimander',
u'Coith',
u'Cokan',
u'Colm',
u'Comblik',
u'Conrad',
u'Constabel',
u'Cöppicus',
u'Coßmann',
u'Courten',
u'Cousin',
u'Csar',
u'Cyrenius',
u'Czarniak',
u'Czenz',
u'Czerwinski',
u'Czuder',
u'Czüschek',
u'Czypowski',
u'Daams',
u'Dabs',
u'Dahlke',
u'Dally',
u'Dambacher',
u'Dannecker',
u'Danowski',
u'Dargies',
u'Darsch',
u'Dassinger',
u'Dato',
u'Dauth',
u'David',
u'Daxl',
u'De Brauin',
u'De Cont',
u'De Greck',
u'De Zolt',
u'Dedi',
u'Defehrden',
u'Degenhardt',
u'Dehning',
u'Deklerski',
u'Delfs',
u'Delle',
u'Dembowski',
u'Demleitner',
u'Dengg',
u'Denzer',
u'Deres',
u'Derrisch',
u'Dertscheny',
u'Deseke',
u'Deser',
u'Desinger',
u'Detert',
u'Deurer',
u'Deußing',
u'Deutsch',
u'Dexheimer',
u'Dexthures',
u'Dhein',
u'Diastocha',
u'Diccas',
u'Dick',
u'Didczuns',
u'Diebschlag',
u'Diemand',
u'Diete',
u'Dietschen',
u'Dipl',
u'Diringer',
u'Distler',
u'Dittberner',
u'Dittmer',
u'Dit',
u'Dobberose',
u'Dobbertin',
u'Dobrowsky',
u'Dobslaf',
u'Dodenhöfft',
u'Döhler',
u'Dolezisch',
u'Döll',
u'Domagalski',
u'Dömel',
u'Domidian',
u'Domurath',
u'Donda',
u'Donder',
u'Dönges',
u'Donnecker',
u'Doppelgatz',
u'Dörenbrak',
u'Doris',
u'Dörken',
u'Dorner',
u'Dorschel',
u'Dorster',
u'Dorwig',
u'Doschek',
u'Dötschel',
u'Dottermosche',
u'Dowolgo',
u'Drausnick',
u'Drax',
u'Dreeßen',
u'Drefahl',
u'Dremel',
u'Drenguis',
u'Dresen',
u'Drewes',
u'Drott',
u'Druckrey',
u'Drumm',
u'Drunse',
u'Dubin',
u'Duchow',
u'Duffel',
u'Dulak',
u'Dulisch',
u'Dullat',
u'Dummermühl',
u'Dummschat',
u'Dums',
u'Dumsky',
u'Dunekacke',
u'Dunk',
u'Dunsche',
u'Dunte',
u'Duppy',
u'Durant',
u'Dusold',
u'Duvenbeck',
u'Dwenger',
u'Dyga ',
u'Dyla',
u'Dylka',
u'Dyllong',
u'Dyllus',
u'Dzubel',
u'Dzielak',
u'Dzietciakowski',
u'Ebeling',
u'Ebelsheuser',
u'Eberius',
u'Ebrecht',
u'Eccarius',
u'Edelmann',
u'Eding',
u'Effenberg',
u'Egen',
u'Eger',
u'Eggers',
u'Ehleiter',
u'Ehlemann',
u'Ehlers',
u'Ehlert',
u'Ehrt',
u'Eichbauer',
u'Eichhorn',
u'Eichinger',
u'Eichoff',
u'Eickhoff',
u'Eiding',
u'Eiffler',
u'Einaus',
u'Eisbrenner',
u'Eisenbeiß',
u'Eisvogel',
u'Eitemüller',
u'Elbers',
u'Elle',
u'Eltze',
u'Emesheymer',
u'Emmer',
u'Endemann',
u'Enenkel',
u'Engelhard',
u'Engels',
u'Englisch',
u'Ennuschat',
u'Ensenbach',
u'Entoch',
u'Erbsmehl',
u'Erde',
u'Erdmann',
u'Erley',
u'Ernst',
u'Ersen',
u'Erth',
u'Ethner',
u'Eulenberger',
u'Eulenfeld',
u'Eulenstein',
u'Ey',
u'Eyfriet',
u'Fabri',
u'Fackiner',
u'Factor',
u'Fah',
u'Fahlenbock',
u'Fahnenschmitt',
u'Fahrun',
u'Falatik',
u'Falckenhagen',
u'Faldix',
u'Falkenberg',
u'Falkus',
u'Famulle',
u'Fantur',
u'Farniok',
u'Farthmann',
u'Fäskorn',
u'Fassonge',
u'Fastabend',
u'Fastenow',
u'Faun',
u'Faust ',
u'Federhen',
u'Fehrtz',
u'Feihel',
u'Feike',
u'Feistkorn',
u'Fekter',
u'Felmet',
u'Ferner',
u'Fernow',
u'Ferring',
u'Fesenmayer',
u'Feuerborn',
u'Feuerherm',
u'Feuersenger',
u'Feuser',
u'Feyl',
u'Feyrsinger',
u'Fiaka',
u'Fibiger',
u'Fichter',
u'Ficker',
u'Fienhold',
u'Fietzek',
u'Figanschek',
u'Figge',
u'Filke',
u'Filler',
u'Fillibrunn',
u'Firnkäs',
u'Fischbaum',
u'Fischer',
u'Fitz',
u'Fitzel',
u'Flamann',
u'Flanner',
u'Flathmann',
u'Fleischfresser',
u'Fliegenschnee',
u'Flore',
u'Foehse',
u'Folta',
u'Forduhn',
u'Forelle',
u'Forthoeffer',
u'Fragner',
u'Frank',
u'Franze',
u'Franzen',
u'Frauenschuh',
u'Frehse',
u'Freihold',
u'Freins',
u'Freisewinkel',
u'Frencking',
u'Freyhold',
u'Freymuth',
u'Fridam',
u'Friebe',
u'Friedacher',
u'Friedewald',
u'Frier',
u'Fritz',
u'Frömbgen',
u'Fuck',
u'Führer',
u'Fulbrecht',
u'Fulfs',
u'Funke',
u'Fürnwallner',
u'Fürst',
u'Fuswinkel',
u'Gäbel',
u'Gabriel',
u'Gailer',
u'Gaisch',
u'Gall',
u'Gallert',
u'Gallitzdörfer',
u'Ganswind',
u'Ganszawski',
u'Ganter',
u'Gapko',
u'Garenfeld',
u'Garenfeld',
u'Garschagen',
u'Gaspur',
u'Gattringer',
u'Gatzsch',
u'Gau',
u'Gautier',
u'Gawe',
u'Gay',
u'Geerds',
u'Geerk',
u'Gehlen',
u'Geil',
u'Geiselbrecht',
u'Geist',
u'Geistert',
u'Geitel',
u'Geiter',
u'Geldschläger',
u'Gelewski',
u'Gelung',
u'Genan',
u'Genzmann',
u'Georg',
u'Georgi',
u'Georgius',
u'Gepken',
u'Gerauch',
u'Gerecke',
u'Gerves',
u'Gesele',
u'Gesemann',
u'Gespan',
u'Geufke',
u'Gewetzki',
u'Gilow',
u'Giar',
u'Gielg',
u'Gieraths',
u'Giesch',
u'Gillmann',
u'Gimbel',
u'Gindera',
u'Girsch',
u'Gitschthaler',
u'Gittelbauer',
u'Glaab',
u'Gleichweit',
u'Gleißenberg',
u'Glettler',
u'Glied',
u'Gligand',
u'Glockengiesser',
u'Glocker',
u'Glogau',
u'Gloger',
u'Glombitza',
u'Gloning',
u'Gmelich',
u'Gnyp',
u'Godein',
u'Gödertz',
u'Goerecke',
u'Goik',
u'Goll',
u'Golonka',
u'Gombach',
u'Gonsior',
u'Gonska',
u'Gooßmann',
u'Görgens',
u'Görn',
u'Görtz',
u'Gössel',
u'Gossen',
u'Göthke',
u'Gottinger',
u'Gottlieb',
u'Gottschlich',
u'Gottwald',
u'Gourgé',
u'Grabenschweiger',
u'Grabosch',
u'Grabow',
u'Grabowski',
u'Graf',
u'Gräfen',
u'Grafwallner',
u'Grapl',
u'Gras',
u'Gras',
u'Gräßer',
u'Grätzer',
u'Grauten',
u'Graw',
u'Greben',
u'Greither',
u'Grellmann',
u'Greß',
u'Greth',
u'Grezella',
u'Grichen',
u'Griessenberger',
u'Grieswald',
u'Grigo',
u'Grillhösl',
u'Groben',
u'Grobarz',
u'Grochalski',
u'Grödler',
u'Groening',
u'Grollm',
u'Gröntgen',
u'Gröschel',
u'Große + FN',
u'Grote',
u'Grotian',
u'Grünhag',
u'Gruppert',
u'Gruszka',
u'Gschweng',
u'Guderian',
u'Guhl',
u'Gühling',
u'Gulau',
u'Güllig',
u'Güllmar',
u'Gülly',
u'Gumpold',
u'Gumprecht',
u'Günnel',
u'Günster',
u'Günther',
u'Gurka',
u'Gürster',
u'Gurzó',
u'Guse',
u'Gustav Adolph',
u'Gutermann',
u'Guthier',
u'Gutkäs',
u'Gyarmath',
u'Hasper',
u'Haasters',
u'Häbler',
u'Habold',
u'Habrich',
u'Hacke',
u'Hadwiger',
u'Haeb',
u'Haesters',
u'Hageböck',
u'Hagler',
u'Haibach',
u'Haipeter',
u'Halas',
u'Halkow',
u'Hallex',
u'Hamfler',
u'Hamig',
u'Hampus',
u'Handerer',
u'Hanf',
u'Hankamer',
u'Hannemann',
u'Hanol',
u'Hanuschek',
u'Harb',
u'Harbart',
u'Harenburg',
u'Harfert',
u'Hargmond',
u'Harksel',
u'Harsing',
u'Hart',
u'Hartema',
u'Hartge',
u'Hartmann',
u'Hascher',
u'Haselier',
u'Hasenbach',
u'Hasenjürgen',
u'Hasiba',
u'Haß',
u'Hässler',
u'Hattwig',
u'Hatzen',
u'Haubold',
u'Haufe',
u'Haug',
u'Hauguth',
u'Haumer',
u'Haun',
u'Hauptvogl',
u'Hausburg',
u'Hausner',
u'Heckner',
u'Hedrischke',
u'Heep',
u'Heeschen',
u'Hehr',
u'Hehrein',
u'Heiligers',
u'Heim',
u'Heimann',
u'Heimbürger',
u'Heimig',
u'Hein',
u'Heinen',
u'Heinitz',
u'Heinsohn',
u'Heise',
u'Hekelmann',
u'Held',
u'Heldt',
u'Helfen',
u'Hellebart',
u'Heller',
u'Hellhammer',
u'Hellingrath',
u'Helm',
u'Helmbold',
u'Helmert',
u'Hemecke',
u'Henczka',
u'Heniau',
u'Henninges',
u'Henß',
u'Hermann',
u'Herbschleb',
u'Herd',
u'Hergert',
u'Herkenrath',
u'Herminghaus',
u'Heród',
u'Herrgott',
u'Herrler',
u'Herrmannsdörfer',
u'Hesch',
u'Hespers',
u'Hess',
u'Hesseler',
u'Hetbreer',
u'Heusner',
u'Hewing',
u'Hibbeln',
u'Hick',
u'Hickisch',
u'Hiemenz',
u'Hilger',
u'Hilgert',
u'Hilsenbeck',
u'Hipke',
u'Hömann',
u'Hobiger',
u'Höcherl',
u'Höckendorf',
u'Hoegen',
u'Hoellger',
u'Hoerner',
u'Hofmann',
u'Hofscheuer',
u'Hofschneider',
u'Hofstadler',
u'Hogetopf',
u'Hohl',
u'Holy',
u'Höllin',
u'Höllmüller',
u'Holschuh',
u'Holtz',
u'Holzbach',
u'Honert',
u'Hönisch',
u'Hörger',
u'Hörich',
u'Horlbogen',
u'Hormes',
u'Horn',
u'Hornbogen',
u'Hörschler',
u'Hörterich',
u'Hösbacher',
u'Hoschek',
u'Hösel',
u'Hoß',
u'Hottmann',
u'Hoyer',
u'Hromada',
u'Huberg',
u'Hübsch',
u'Hübschke',
u'Hubschneider',
u'Hudalla',
u'Hudecek',
u'Hug',
u'Hugel',
u'Huhlgram',
u'Huhnholz',
u'Huiter',
u'Hüllen',
u'Hullmann',
u'Hülsewig',
u'Hülsken',
u'Humel',
u'Hümpfer',
u'Hündgen',
u'Hune',
u'Hunert',
u'Hurnaus',
u'Hüser',
u'Hüsige',
u'Huska',
u'Hutzelsieder',
u'Huzsmann',
u'Hymann',
u'Idler',
u'Iden',
u'Illbruck',
u'Illjes',
u'Ilz',
u'Immilla',
u'In gen. Bremen',
u'Ingenthron',
u'Interholzinger',
u'Irevarim',
u'Isberner',
u'Ischdonat',
u'Ising',
u'Jabin',
u'Jackenkroll',
u'Jacobfeuerborn',
u'Jädicke',
u'Jadke',
u'Jaeckel',
u'Jaggau',
u'Jähnig',
u'Jakob',
u'Janic',
u'Janke',
u'Jantsch',
u'Jantschik',
u'Japmann',
u'Jaraß',
u'Jaskulski',
u'Jasser',
u'Jauck',
u'Jawurek',
u'Jeglorz',
u'Jeitel',
u'Jenderny',
u'Jendral',
u'Jenemann',
u'Jepken',
u'Jerzumbek',
u'Jeschky',
u'Jesko',
u'Jetzinger',
u'Jilke',
u'Jöchlinger',
u'Joczat',
u'Jodokus',
u'Joggau',
u'Jöhler',
u'Joho',
u'Jost',
u'Jugelt',
u'Juhl',
u'Jung',
u'Junghenn',
u'Junglas',
u'Juntke',
u'Jurk',
u'Jüttner',
u'Kalinke',
u'Kaaden',
u'Kaczanowski',
u'Kadatz',
u'Käding',
u'Kadke',
u'Kaeß',
u'Kai',
u'Kalara',
u'Kalka',
u'Kalt',
u'Kaltofen',
u'Kalus',
u'Kalwa',
u'Kaminski',
u'Kämpfe',
u'Kanand',
u'Kandzia',
u'Kanno',
u'Kanutschek',
u'Kanzler',
u'Kaphengst',
u'Kapitza',
u'Karbaumer',
u'Karnstaedt',
u'Karrenbauer',
u'Karun',
u'Karzanowski',
u'Kaschewar',
u'Käsebier',
u'Käßmodel',
u'Kastler',
u'Katt',
u'Katz',
u'Katzenburg',
u'Katzlberger',
u'Kauert',
u'Kauran',
u'Kawohl',
u'Keber',
u'Kehrein',
u'Keidel',
u'Keinitz',
u'Kellner',
u'Kelly',
u'Kemper',
u'Kempe',
u'Kempers',
u'Kerinnes',
u'Kernchen',
u'Kestenus',
u'Kettner',
u'Keuchel',
u'Kichtan',
u'Kieder',
u'Kiehnscherf',
u'Kießelbach',
u'Kilb',
u'Kilgen',
u'Kilian',
u'Killer',
u'Kimpfbeck',
u'Kinateder',
u'Kinnen',
u'Kipcke',
u'Kirchenwitz',
u'Kirschberger',
u'Kirwitsch',
u'Kischel',
u'Kisselat',
u'Kissing',
u'Kissner',
u'Kisson',
u'Kistenfeger',
u'Kiwitz',
u'Kixmöller',
u'Klatt',
u'Klatta',
u'Klaukens',
u'Klaumünzer',
u'Kleemann',
u'Kleimčik',
u'Klein',
u'Kleine + FN',
u'Kleine Gunck',
u'Kleinedowe',
u'Kleinesudeik',
u'Kleinmond',
u'Klenner',
u'Klett',
u'Kleukens',
u'Klimke',
u'Klimmer',
u'Klinkhammer',
u'Klisch',
u'Klix',
u'Klöckner',
u'Klomhus',
u'Klönhammer',
u'Klöpper',
u'Klose',
u'Klubescheid',
u'Klump',
u'Klunkert',
u'Knakowski',
u'Knechtl',
u'Knell',
u'Kneschk',
u'Knieling',
u'Kniepeis',
u'Knieps',
u'Knocke',
u'Knöfel ',
u'Knuffmann',
u'Knußmann',
u'Kok',
u'Koblischke',
u'Koczan',
u'Kogels',
u'Kogerup',
u'Koitsch',
u'Koke',
u'Kokoscha',
u'Koll',
u'Kollenkarn',
u'Koller',
u'Kolodzy',
u'Kompalek',
u'Konang',
u'Konecki',
u'Konietzko',
u'Königsberger',
u'Köplin',
u'Kopp',
u'Koppauner',
u'Koppel',
u'Korgawir',
u'Korjenic',
u'Kornacker',
u'Koroleski',
u'Kortum',
u'Koruhn',
u'Korzec',
u'Kosakatis',
u'Kosca',
u'Koschitz',
u'Koschitzki',
u'Kosgalwies',
u'Kositzke',
u'Koska',
u'Kosmala',
u'Kostas',
u'Köstenbauer',
u'Kothenbeutel',
u'Kothmayer',
u'Kötschau',
u'Kottas',
u'Koytka',
u'Kozanecki',
u'Krahe',
u'Krahfuss',
u'Krail',
u'Krall',
u'Kramb',
u'Krankemann',
u'Kranz',
u'Krapl',
u'Krätschmer',
u'Kraus',
u'Krause',
u'Krausschübel',
u'Kraußewald',
u'Krautwurst',
u'Krautwurst',
u'Krebel',
u'Krempelhuber',
u'Kren',
u'Krenger',
u'Kreß',
u'Kretschmer',
u'Kringler',
u'Krinner',
u'Kripgans',
u'Krischke',
u'Kroich',
u'Kroll',
u'Krön',
u'Kronawetter',
u'Kronseder',
u'Kroth',
u'Kruczek',
u'Krugh',
u'Krullmann',
u'Krumholz',
u'Krümmel',
u'Krüpper',
u'Krzigitzki',
u'Krzossa',
u'Krzywocz',
u'Krzyzak',
u'Kubiak',
u'Kubick',
u'Kubik',
u'Kubitza',
u'Kubo',
u'Kubrat',
u'Küchenhoff',
u'Kugler',
u'Kühl',
u'Kuhlbarsch',
u'Kuhleber',
u'Kuhlmei',
u'Kuhn',
u'Kullinat ',
u'Külzhammer',
u'Kumbartzky',
u'Kumert',
u'Kummer',
u'Kümpell',
u'Kundoch',
u'Kuntscher',
u'Kunz',
u'Kurek auch Kurka',
u'Kurschildgen',
u'Kurz',
u'Küstner',
u'Kusztal',
u'Kutschkow',
u'Küveler',
u'Kuwatsch',
u'Kydala',
u'Kyselo',
u'Labrink',
u'Labatqueen',
u'Lachenit',
u'Lachhein',
u'Lade',
u'Ladinig',
u'Lais',
u'Lampe',
u'Lamprecht',
u'Landes',
u'Landgraf',
u'Landhold',
u'Landhus',
u'Langelot',
u'Langenau',
u'Langenbach',
u'Langhandke',
u'Langmaack',
u'Langner',
u'Lappe',
u'Lappöhn',
u'Larz',
u'Laudahn',
u'Lauer',
u'Lauermann',
u'Laukant',
u'Laun',
u'Lauterbeck',
u'Lavin',
u'Lechner',
u'Lecybil',
u'Lederhoßen',
u'Ledück',
u'Leers',
u'Leesen',
u'Lehmann',
u'Leibniz',
u'Leichenberger',
u'Leidiger',
u'Leiteritz',
u'Leiting',
u'Leitmann',
u'Lemke',
u'Lemonius',
u'Lengler',
u'Lenhardt',
u'Lenski',
u'Leppmeier',
u'Lerat',
u'Lerge',
u'Lerz',
u'Leschke',
u'Leue',
u'Leutbecher',
u'Levin',
u'Leykauf',
u'Lezius',
u'Libera',
u'Lichnofsky',
u'Lichtenfeld',
u'Liebe',
u'Lieber',
u'Liebl',
u'Liebmann',
u'Lieder',
u'Liemanns',
u'Lierschaft',
u'Ließel',
u'Lietz',
u'Limmeroth',
u'Lindau',
u'Link',
u'Lipper',
u'Lippmann',
u'Lipskis',
u'Lischewski',
u'Lisenberg',
u'Lisken',
u'Litzkowy',
u'Lobien',
u'Löcher',
u'Locklair',
u'Loeveling',
u'Löffelbier',
u'Loger',
u'Lohmeier',
u'Lohre',
u'Loipeldinger',
u'Lokowal',
u'Londwiche',
u'Loos',
u'Loose',
u'Lopar',
u'Loquay',
u'Lorleberg',
u'Lory',
u'Loschnat',
u'Löser',
u'Löwenberger',
u'Loy',
u'Loyda',
u'Lubbert',
u'Lübke',
u'Lückel',
u'Lücker',
u'Ludelaufs',
u'Lüge',
u'Lunkenbein',
u'Lünnemann',
u'Lupp',
u'Luppus',
u'Lusatis',
u'Lusczyk',
u'Lüß',
u'Lustig',
u'Luterwald',
u'Lüttermann',
u'Lüttger',
u'Lutzemann',
u'Lzicziarz',
u'Maaß',
u'Mabuse',
u'Mache',
u'Macherndl',
u'Machold',
u'Mackrodt',
u'Madl',
u'Maderdonner',
u'Maetze',
u'Magenschaben',
u'Mahr',
u'Mahrer',
u'Majorkowitsch',
u'Makula',
u'Malak',
u'Malat',
u'Malko',
u'Malm',
u'Malschowsky',
u'Malüge',
u'Malycha',
u'Manlik',
u'Mandalka',
u'-mann',
u'Mannes',
u'Mannes',
u'Mansholt',
u'Marcus',
u'Maria',
u'Marian',
u'Markowski',
u'Markus',
u'Marokko',
u'Maronde',
u'Marsand',
u'Marschewski',
u'Marte',
u'Martio',
u'Marx',
u'Marxen',
u'Marzoch',
u'Marzelin',
u'Mäscher',
u'Mashat',
u'Massengeil',
u'Masser',
u'Massier',
u'Matkay',
u'Mattern',
u'Mattew',
u'Matthies',
u'Matuszewski',
u'Matzeit',
u'Matzerath',
u'Mauksch',
u'Mausehund',
u'Maushake',
u'Max',
u'Mezger',
u'Mechelk',
u'Medrian',
u'Medrow',
u'Meeden',
u'Meerpohl',
u'Meffle',
u'Mehlhase',
u'Meinzer',
u'Meixner',
u'Melkheier',
u'Melles',
u'Menke',
u'Mennenichs',
u'Mergt',
u'Merhof',
u'Merschel',
u'Merten',
u'Merwart',
u'Merzbacher',
u'Mese',
u'Messing',
u'Mettke',
u'Metzgen',
u'Metzler',
u'Metzling',
u'Mex',
u'Mey',
u'Middelborn',
u'Miehlich',
u'Mierswa',
u'Mies',
u'Mieth',
u'Miletzky',
u'Militsch',
u'Milkau',
u'Milker',
u'Milster',
u'Miltkotte',
u'Minges',
u'Miotke',
u'Mirsch',
u'Mirz',
u'Misburger',
u'Mitlacher',
u'Mittemeyer',
u'Mittrach',
u'Mix',
u'Mnilk',
u'Mobius',
u'Modest',
u'Moerser',
u'Moha',
u'Mohr',
u'Mokerl',
u'Moldaschl',
u'Moll',
u'Möller',
u'Mollhoff',
u'Moltke',
u'Molzahn',
u'Mombour',
u'Monick',
u'Morawitz',
u'Morgalla',
u'Morio',
u'Moser',
u'Mößinger',
u'Möstl',
u'Moter',
u'Mottl',
u'Mrozek',
u'Mrugala',
u'Mutz',
u'Mücke',
u'Mühlauer',
u'Mühlbrodt',
u'Mühlich',
u'Muley',
u'Mülk',
u'Müller',
u'Münchow',
u'Mundkowski',
u'Mundweil',
u'Mundwein',
u'Munz',
u'Muschweck',
u'Müser',
u'Müser',
u'Musiol',
u'Müskes',
u'Müssig',
u'Mütze',
u'Mylius',
u'Naab',
u'Nacke',
u'Nackies',
u'Naethe',
u'Naeve',
u'Nagl',
u'Nagorka',
u'Najork',
u'Nake',
u'Nalek',
u'Naskneck ',
u'Nather',
u'Naujoks',
u'Nebendahl',
u'Nebig',
u'Neckar',
u'Nefeling',
u'Neger',
u'Negraszus',
u'Nehmer',
u'Neig',
u'Nell',
u'Nemenyi',
u'Nette',
u'Netter',
u'Neuhold',
u'Neyses',
u'Nickisch',
u'Nickol',
u'Nicolay',
u'Niefanger',
u'Niehues',
u'Nieslony',
u'Nietan',
u'Nillies',
u'Nispel',
u'Nissen',
u'Nißl',
u'Nöggerath',
u'Noltekuhlmann',
u'Nonnenfeind',
u'Norberger',
u'Nosbach',
u'Nothelfer',
u'Nothdurft',
u'Novotny',
u'Noy',
u'Nüchter',
u'Nürnberger',
u'Oberlander',
u'Oberscheuer',
u'Och',
u'Odrig',
u'Oehmig',
u'Ofenloch',
u'Off',
u'Offik',
u'Öhlenbach',
u'Olderdissen',
u'Olding',
u'Olefs',
u'Oliev',
u'Ollenschläger',
u'Ollertz',
u'Omlor',
u'Oortmeijer',
u'Opes',
u'Opp',
u'Orfert',
u'Orlamünder',
u'Orszulok',
u'Ortlein',
u'Osborne',
u'Oschitzki',
u'Osond',
u'Osterhof',
u'Osterloh',
u'Ostermann',
u'Ostermeier',
u'Ostwald',
u'Ott',
u'Ott',
u'Otte im Kampe',
u'Ottelinger',
u'Otten',
u'Otto',
u'Ottolinger',
u'Overschür',
u'Ozepowey',
u'Ozimek',
u'Paar',
u'Pacher',
u'Pachoinig',
u'Paetow',
u'Paetzel',
u'Pagel',
u'Pago',
u'Paierl',
u'Palitzsch',
u'Palluth',
u'Palm',
u'Palmers',
u'Pangerl',
u'Panienka',
u'Panköker',
u'Papkala',
u'Parakenings',
u'Paries',
u'Parlaska',
u'Parotat',
u'Partheimüller',
u'Paschenda',
u'Passon',
u'Pätow',
u'Patzelt',
u'Pätzold',
u'Paulmann',
u'Paulowitsch',
u'Pawelowski',
u'Payer',
u'Payreder',
u'Pechstein',
u'Peckenhawben',
u'Pede',
u'Peege',
u'Peidl',
u'Peischl',
u'Peitz',
u'Peix',
u'Pelzing',
u'Pelikan',
u'Penke',
u'Peper',
u'Perfold',
u'Perner',
u'Persch',
u'Perwas',
u'Peter',
u'Peters',
u'Petras',
u'Petrzik',
u'Peukes',
u'Peylo',
u'Pfannenstiel',
u'Pfarrdrescher',
u'Pfeifroth',
u'Pflaume',
u'Pförtner von der Hölle',
u'Pfuisi',
u'Philen',
u'Philipowski',
u'Phillibrunn',
u'Pilasch',
u'Piasecki',
u'Pichler',
u'Pickert',
u'Piehl',
u'Piehler',
u'Pielmeier',
u'Pieper',
u'Pietruska',
u'Pietruszinski',
u'Pilawa',
u'Pilgram',
u'Pillasch',
u'Pille',
u'Pingel',
u'Pinkernelle',
u'Pionczewski',
u'Pioreck',
u'Pipas',
u'Pirkner',
u'Pirl',
u'Pisula',
u'Pitschmann',
u'Pitter',
u'Plachner',
u'Plaggenmeier',
u'Plagwitz',
u'Planer',
u'Plank',
u'Plankl',
u'Plate',
u'Plattfuss',
u'Platz',
u'Pleß',
u'Pletsch',
u'Ploder',
u'Ploigt',
u'Plotonius',
u'Plotzki',
u'Pluskota ',
u'Plymakers',
u'Pock',
u'Poethig',
u'Pogrzeba',
u'Poindl',
u'Pokorny',
u'Poley',
u'Polidey',
u'Pollnstorfer',
u'Polle',
u'Poller',
u'Pollmächers',
u'Pommer',
u'Pompetzki',
u'Pomplun',
u'Poock',
u'Pophal',
u'Poppenhaeger',
u'Poppensieker',
u'Poppler',
u'Pörtner',
u'Poschen',
u'Pour',
u'Poweleit',
u'Poxhammer',
u'Praetel',
u'Prassek',
u'Prätzler',
u'Pravemann',
u'Prawatky',
u'Preidler',
u'Preikszat',
u'Pressin',
u'Preugszat',
u'Prigger',
u'Primus',
u'Prisel',
u'Priwall',
u'Profittlich',
u'Pröpper',
u'Proquitte',
u'Psota',
u'Puhwein',
u'Pujner',
u'Pujner',
u'Pult',
u'Pung',
u'Pustlauk',
u'Quapp',
u'Quark',
u'Quentin',
u'Quirant',
u'Quirmbach',
u'Raband',
u'Rabiezanka',
u'Rackl',
u'Racky',
u'Raddan',
u'Räder',
u'Raderecht',
u'Radloff',
u'Radons',
u'Radtke',
u'Raedelin',
u'Raffelsiefer',
u'Raimann',
u'Rakos',
u'Rambau',
u'Ramer',
u'Rampe',
u'Ramskogler',
u'Ranft',
u'Ranninger',
u'Rantschigei',
u'Raring',
u'Rasokat',
u'Rassl',
u'Räster',
u'Ratberger',
u'Räthe',
u'Rattelmüller',
u'Raubach',
u'Rauft',
u'Räumschüssel',
u'Rausch',
u'Rauschenbach',
u'Rauter gen. Lichtrauter',
u'Rera',
u'Rebühr',
u'Rechmal',
u'Reckefuß',
u'Reddig',
u'Reeg',
u'Reese',
u'Reichert',
u'Reimler',
u'Reimler',
u'Rein',
u'Reinbold',
u'Reinwarth',
u'Reiser',
u'Reisner',
u'Rejda',
u'Rempe',
u'Remter',
u'Renker',
u'Rennoch',
u'Repke',
u'Requa',
u'Requard',
u'Retzlaff',
u'Reutlinger',
u'Reutlinger',
u'Ribitsch',
u'Richtscheid',
u'Ricksthal',
u'Riemann',
u'Riet',
u'Riffelsen',
u'Rilka',
u'Rillander',
u'Ring',
u'Ringel',
u'Ringelmann',
u'Rinke',
u'Rinschede',
u'Rippensiepe',
u'Ritzenhöfer',
u'Rochalski',
u'Rochow',
u'Röcker',
u'Röckl',
u'Rodermund',
u'Roehrdantz',
u'Roetzel',
u'Röger',
u'Rogosch',
u'Rogoß',
u'Rohirse',
u'Rohlmann',
u'Rohrbach',
u'Röhrmann',
u'Röhtz',
u'Röll',
u'Rolle',
u'Röller',
u'Röllig',
u'Römer',
u'Romeri',
u'Romirer',
u'Römmelt',
u'Roppert',
u'Rosaler',
u'Rösenberg',
u'Rosenhainer',
u'Rosenstetter',
u'Rosenthal',
u'Rösner',
u'Rösnick',
u'Rosowski',
u'Roßdeutscher',
u'Rößler',
u'Rosycka',
u'Rötger auff dem lütgen Gummenich',
u'Rötgers',
u'Rothenberg',
u'Roth-Rothenhorst',
u'Rothweiler',
u'Rottmüller',
u'Rötz',
u'Rötzer',
u'Roubal',
u'Rubbert',
u'Rübenstahl',
u'Ruchay',
u'Ruda',
u'Rüdell',
u'Rüdtlbauch',
u'Ruhl',
u'Rührdich',
u'Ruis',
u'Rumesberger',
u'Rumm',
u'Rung',
u'Runschke',
u'Ruppin',
u'Rüschen',
u'Ruzsar',
u'Ryba',
u'Rybolt',
u'Ryll',
u'Slotawa',
u'Sabeck',
u'Sachsalber',
u'Sachtleber',
u'Saesser',
u'Sajdowski',
u'Sakain',
u'Saladin',
u'Salzbrunn',
u'Samariter',
u'Sandau',
u'Sandberg',
u'Sandführ',
u'Sardison',
u'Sarholz',
u'Sarodnick',
u'Sasse',
u'Säuffert',
u'Saure',
u'Saurugger',
u'Sausmikat',
u'Sax',
u'Schaap',
u'Schack',
u'Schacke',
u'Schadt',
u'Schafzahl',
u'Schakeit',
u'Schambelon',
u'Schantl',
u'Scharff',
u'Schark',
u'Scharlock',
u'Scharwart',
u'Schattauer',
u'Schattkowsky',
u'Schaubitzer',
u'Schaudick',
u'Schaurhofer',
u'Schaurpost',
u'Schavan',
u'Scheewe',
u'Scheffke',
u'Scheib',
u'Scheinkönig',
u'Scheiper',
u'Scheisner',
u'Schemm',
u'Schenetten',
u'Schenner',
u'Scherke',
u'Scherr',
u'Schettek',
u'Scheunstuhl',
u'Scheuchengrab',
u'Schey',
u'Schick',
u'Schidtgabler',
u'Schiebel',
u'Schieberle',
u'Schiepert',
u'Schieske',
u'Schikori',
u'Schikowsky',
u'Schilberg',
u'Schilloks',
u'Schimek',
u'Schirarend',
u'Schirp',
u'Schkuhr',
u'Schlag',
u'Schlage',
u'Schlagie',
u'Schlagin',
u'Schlagindweit',
u'Schlagnitweit',
u'Schleeweiß',
u'Schlemmer',
u'Schlesinger',
u'Schleuter',
u'Schlippes',
u'Schliwinski',
u'Schloack',
u'Schlößin ',
u'Schmäche',
u'Schmallowsky',
u'Schmauk',
u'Schminke',
u'Schmolke',
u'Schmolmüller',
u'Schmuck',
u'Schmuckermeier',
u'Schmuhl',
u'Schnack',
u'Schnappauf',
u'Schneeberger',
u'Schneegaß',
u'Schnegula',
u'Schomburg',
u'Schommertz',
u'Schönbacher',
u'Schönhoff',
u'Schöning',
u'Schooß',
u'Schopp',
u'Schott',
u'Schrecksnadl',
u'Schrein',
u'Schröer',
u'Schroll',
u'Schröter',
u'Schrücker',
u'Schubert',
u'Schuckert',
u'Schulwitz',
u'Schum',
u'Schüppscheck',
u'Schuscik',
u'Schužek',
u'Schwabeland',
u'Schwan',
u'Schwarzenberger',
u'Schwebius',
u'Schweigger',
u'Schwellnuss',
u'Schwertfeger',
u'Sckel',
u'Sebestik',
u'Seck',
u'Sedlmeier',
u'Sehn',
u'Sehrin',
u'Seibold',
u'Seidel',
u'Seidenfaden',
u'Sela',
u'Seller',
u'Sellin',
u'Sembries',
u'Semper',
u'Sempf',
u'Senftleben',
u'Senge',
u'Seraphin',
u'Serverin',
u'Setzkegel',
u'Seul',
u'Sewelys',
u'Seyfrizen',
u'Siebel',
u'Siebelist',
u'Siebzehnrübl',
u'Sielmann',
u'Sienen',
u'Sigl',
u'Sill',
u'Siman',
u'Simmank',
u'Sinram',
u'Sinn',
u'Sinz',
u'Siyaks',
u'Skal',
u'Skala',
u'Skeem',
u'Skiera',
u'Skjas ',
u'Sklarski',
u'Skopal',
u'Skorsoba',
u'Skrok',
u'Skuza',
u'Sladoslawek',
u'Sladoslawek',
u'Slany',
u'Slomka',
u'Smarsly',
u'Smers',
u'Smiedoda',
u'Smirnow',
u'Sobe',
u'Sobek',
u'Sobetzki',
u'Sobetzko',
u'Sobietzki',
u'Soddemann',
u'Soesser',
u'Soester',
u'Sohlleder',
u'Sokowski',
u'Soldat',
u'Soltau',
u'Sommer',
u'Sommerburg',
u'Sommerlath',
u'Sondermann',
u'Sonnekalb',
u'Sorg',
u'Sowa',
u'Spangenberg',
u'Spaniol',
u'Späth',
u'Spen',
u'Speen',
u'Speicher',
u'Sperlein',
u'Sperrholz',
u'Spettmann',
u'Spiegelberg',
u'Spilker',
u'Spira',
u'Spitzer',
u'Spitzmacher',
u'Sporkert',
u'Springgorum',
u'Staats',
u'Stadtmann',
u'Staedler',
u'Stanke',
u'Statkus',
u'Stattegger',
u'Stattmann',
u'Stauffen',
u'Steckel',
u'Steckler',
u'Steding',
u'Steffens',
u'Stegh',
u'Stein',
u'Steinbring',
u'Steinemer',
u'Steingraf',
u'Steinicke',
u'Stempliewicz',
u'Stenger',
u'Sternalsky',
u'Sternowsky',
u'Steussloff',
u'Stiebauß',
u'Stiefler',
u'Stindl',
u'Stockert',
u'Stoebloff',
u'Stoisloff',
u'Stölldichvoll',
u'Stolleis',
u'Stollhoff',
u'Stölpe',
u'Stolte',
u'Stomporowski',
u'Stoppa',
u'Stoschek',
u'Stoy',
u'Strack',
u'Straßer',
u'Strehlau',
u'Strehle',
u'Streitz',
u'Streubo',
u'Striegnitz',
u'Strischek',
u'Stritzke',
u'Strniste',
u'Strobuchin',
u'Strohkar',
u'Strzalek',
u'Strzoda',
u'Stubner',
u'Stuckert',
u'Stuecklas',
u'Stüertz',
u'Stumvoll',
u'Stünkel',
u'Suna',
u'Subirge',
u'Suck',
u'Sudik',
u'Sühse',
u'Suittertus',
u'Sult',
u'Sültzle',
u'Sulzer',
u'Süpfle',
u'Suppan',
u'Surek',
u'Surrey',
u'Susemichel',
u'Süßenbach',
u'Süßenberger',
u'Sütterlin',
u'Swientek',
u'Syré',
u'Szablowski',
u'Szechy',
u'Szillat',
u'Szillus',
u'Szuggars',
u'Szusczynski',
u'Tabbert',
u'Tabor',
u'Tadda',
u'Tambe',
u'Tänzer',
u'Tapanila',
u'Taschinger',
u'Tautorat',
u'Tautz',
u'Teibinger',
u'Telaar',
u'Teleu',
u'Telle',
u'Tellegardus',
u'Tellegrades',
u'Teloh',
u'Ter Boven',
u'Terveer',
u'Teubert',
u'Teutschmann',
u'Tham',
u'Theihsen',
u'Thein',
u'Theis',
u'Thielsch',
u'Thiele',
u'Thielicke',
u'Thielsch',
u'Thiemann',
u'Thiermann',
u'Thimm',
u'Thomaschowski',
u'Thome',
u'Thomisch',
u'Thomys',
u'Thormann',
u'Thu',
u'Thuering',
u'Thun',
u'Thur',
u'Tibor',
u'Tibus',
u'Tiedemann',
u'Tiefenthaler',
u'Tiegelhardt',
u'Tiggeloven',
u'Tikal',
u'Tilgier',
u'Tillmanns',
u'Timann',
u'Timmermann',
u'Tippl',
u'Tismar',
u'Tiszauer',
u'Tittes',
u'Tobolka',
u'Todeskino',
u'Tödtenhey',
u'Todtenhöfft',
u'Tokarski',
u'Tolentino',
u'Tölg',
u'Toman',
u'Tomaschewski',
u'Tondock',
u'Tonnis',
u'Torner',
u'Torster',
u'Toschak',
u'Trabitzsch',
u'Trambowsky',
u'Trattner',
u'Traut',
u'Treffeisen',
u'Trefftz',
u'Trem',
u'Trenkler',
u'Triebel',
u'Triebmann',
u'Trinkaus',
u'Trobitzsch',
u'Trojan',
u'Tröll',
u'Trollack',
u'Tropschuh',
u'Trost',
u'Trowe',
u'Troyer',
u'Trubl',
u'Truve',
u'Tschackert',
u'Tscharke',
u'Tschersich',
u'Tschirley',
u'Tschuschner',
u'Tumschat',
u'Turne',
u'Türpe',
u'Tuschl',
u'Tušek',
u'Uerlings',
u'Uhlschmidt',
u'Umbundumb',
u'Unbehend',
u'Ungetüm',
u'Unruhe',
u'Unschlitt',
u'Urbainczyk',
u'Urselmann',
u'Utasch',
u'Utgenannt',
u'Utri',
u'Uttke',
u'Utz',
u'van Riet',
u'Vandersee',
u'Varhelyi',
u'Vasters',
u'Väthbrückner',
u'Vehreschild',
u'Velz',
u'Venediger',
u'Vercelli',
u'Verhoeven',
u'Verhülsdonk',
u'Versüme',
u'Vespermann',
u'Vesseley',
u'Veszeli',
u'Vetterick',
u'Vierling',
u'Villon',
u'Villwock',
u'Vith',
u'Viukh ',
u'Vlijm',
u'Vogel',
u'Vögerl',
u'Vögler',
u'Vohberger',
u'Vollbaum',
u'von Colm',
u'von der Breyschen',
u'von der Hüllen',
u'Von der Megde',
u'von Kroth',
u'Vorthaeffer',
u'Voss',
u'Votruba',
u'Wolek',
u'Wabichler',
u'Wachtmann',
u'Wahl',
u'Waizenegger',
u'Walczak',
u'Waldenmaier',
u'Waldinger',
u'Walkovs',
u'Walkowitz',
u'Walneg',
u'Walter',
u'Waltemate',
u'Walter',
u'Wampera',
u'Wandpflug',
u'Waninger',
u'Wanis',
u'Wannewitz',
u'Wanz',
u'Wäpel',
u'Wardaschka',
u'Warmke',
u'Wartenberg',
u'Warzeschka',
u'Waržilek',
u'Waschitza',
u'Waschulewski',
u'Wasielewski',
u'Wasserberg',
u'Watzl',
u'Wawrzinek',
u'Weber',
u'Weckop',
u'Weezka',
u'Wefer',
u'Wegerich',
u'Wehrspaun',
u'Weischedel',
u'Weibels',
u'Weichelt',
u'Weichert',
u'Weichert',
u'Weickelsdorfer',
u'Weidelt',
u'Weidenstraß',
u'Weigel',
u'Weihmann',
u'Weiland',
u'Weilguni',
u'Weindler',
u'Weinketz',
u'Weinwurm',
u'Weischede',
u'Weisenseel',
u'Weitenhofer',
u'Weitzel',
u'Welzenbach',
u'Wendeborn',
u'Wenn',
u'Werder',
u'Werst',
u'Wesner',
u'Wespatat',
u'Wessels',
u'Westerhüs',
u'Wetzlau',
u'Wetzler',
u'Weusten',
u'Weyhreter',
u'Weyrich',
u'Wickeroth',
u'Wickher',
u'Wiebicke',
u'Wieczorek',
u'Wiederoder',
u'Wieht',
u'Wieker',
u'Wiener',
u'Wienhold',
u'Wienkopp',
u'Wienströer',
u'Wierth',
u'Wiescholek',
u'Wiesenkämper',
u'Wiking',
u'Wild',
u'Wildfeuer',
u'Willimek',
u'Wimbessel',
u'Winsch',
u'Windisch',
u'Wings',
u'Winkelhardt',
u'Winkelmeier',
u'Wippich',
u'Wischheim',
u'Wischtokat',
u'Wisztukat',
u'Withliff',
u'Witte',
u'Wittke',
u'Witz',
u'Wiwianka',
u'Wodstrschil',
u'Wohlguth',
u'Wöhlke',
u'Wohlmuth',
u'Wohlschiess',
u'Wöhrig',
u'Woita',
u'Wölbitsch',
u'Wollbrink',
u'Wollerscheid',
u'Wollesen',
u'Wollitz',
u'Woloszyn',
u'Wortmann',
u'Wösten',
u'Wotruba',
u'Wotschokowsky',
u'Wowarra',
u'Wrabitsch ',
u'Wrede',
u'Wrieth',
u'Wuff',
u'Wülfroth',
u'Wundenberg',
u'Wunder',
u'Wundermann',
u'Wünsch',
u'Würthele',
u'Wutkowski',
u'Wuttgen',
u'Wyder',
u'Wyrowski',
u'Wyssmann',
u'Zabel',
u'Zabelberg',
u'Zach',
u'Zacharias',
u'Zakaroff',
u'Zalter',
u'Zaminczek',
u'Zamsau',
u'Zankolewski',
u'Zarling',
u'Zarske',
u'Zaryuk',
u'Zdrzalek',
u'Zeh',
u'Zejewski',
u'Zeleschke',
u'Zelezny',
u'Zeller',
u'Zemella',
u'Zemla',
u'Zemter',
u'Zens',
u'Zernechel',
u'Zerrein',
u'Zettermann',
u'Zettl',
u'Ziebur',
u'Ziegengeist',
u'Ziegler',
u'Zifling',
u'Zigge',
u'Zilla',
u'Zimmenthal',
u'Zimmerman',
u'Zinhobl',
u'Zink',
u'Zinram',
u'Zintsch',
u'Zitte',
u'Zödlvetz',
u'Zohner',
u'Zoike',
u'Zölfl',
u'Zöller',
u'Zöllkau',
u'Zollstab',
u'Zolondz',
u'Zolt',
u'Zorawski',
u'Zotke',
u'Zötsch',
u'Zschieschang',
u'Zuckerhut',
u'Zude',
u'Zugreif',
u'Zuhlmann',
u'Zumach',
u'Zummack',
u'Zweiniger',
u'Zydek',
u'Zydz')

import random

def get_random_vorname_w():
    return random.choice(vornamen_w)

def get_random_vorname_m():
    return random.choice(vornamen_m)

def get_random_nachname():
    return random.choice(nachnamen)

def get_random_verein():
    return u'{abk} {stadt}'.format(abk=random.choice(vereinsbezeichnungen), stadt=random.choice(staedte))


