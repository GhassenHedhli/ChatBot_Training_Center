from flask import Flask, render_template, request

app = Flask(__name__)

def conjugate_verbs(verb, tense):
    conjugations = {   

  "être": {
    "Présent": {
      "Je": "suis",
      "Tu": "es",
      "Il/Elle/On": "est",
      "Nous": "sommes",
      "Vous": "êtes",
      "Ils/Elles": "sont"
    },
    "Imparfait": {
      "Je": "étais",
      "Tu": "étais",
      "Il/Elle/On": "était",
      "Nous": "étions",
      "Vous": "étiez",
      "Ils/Elles": "étaient"
    },
    "Passé Composé": {
      "Je": "ai été",
      "Tu": "as été",
      "Il/Elle/On": "a été",
      "Nous": "avons été",
      "Vous": "avez été",
      "Ils/Elles": "ont été"
    },
    "Futur": {
      "Je": "serai",
      "Tu": "seras",
      "Il/Elle/On": "sera",
      "Nous": "serons",
      "Vous": "serez",
      "Ils/Elles": "seront"
    },
    "Plus-que-parfait": {
      "Je": "avais été",
      "Tu": "avais été",
      "Il/Elle/On": "avait été",
      "Nous": "avions été",
      "Vous": "aviez été",
      "Ils/Elles": "avaient été"
    },
    "Futur Simple": {
      "Je": "serai",
      "Tu": "seras",
      "Il/Elle/On": "sera",
      "Nous": "serons",
      "Vous": "serez",
      "Ils/Elles": "seront"
    },
    "Futur Antérieur": {
      "Je": "aurai été",
      "Tu": "auras été",
      "Il/Elle/On": "aura été",
      "Nous": "aurons été",
      "Vous": "aurez été",
      "Ils/Elles": "auront été"
    },
    "Conditionnel Présent": {
      "Je": "serais",
      "Tu": "serais",
      "Il/Elle/On": "serait",
      "Nous": "serions",
      "Vous": "seriez",
      "Ils/Elles": "seraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais été",
      "Tu": "aurais été",
      "Il/Elle/On": "aurait été",
      "Nous": "aurions été",
      "Vous": "auriez été",
      "Ils/Elles": "auraient été"
    },
    "Subjonctif Présent": {
      "Je": "sois",
      "Tu": "sois",
      "Il/Elle/On": "soit",
      "Nous": "soyons",
      "Vous": "soyez",
      "Ils/Elles": "soient"
    },
    "Subjonctif Passé": {
      "Je": "aie été",
      "Tu": "aies été",
      "Il/Elle/On": "ait été",
      "Nous": "ayons été",
      "Vous": "ayez été",
      "Ils/Elles": "aient été"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse été",
      "Tu": "eusses été",
      "Il/Elle/On": "eût été",
      "Nous": "eussions été",
      "Vous": "eussiez été",
      "Ils/Elles": "eussent été"
    },
    "Subjonctif Imparfait": {
      "Je": "fusse",
      "Tu": "fusses",
      "Il/Elle/On": "fût",
      "Nous": "fussions",
      "Vous": "fussiez",
      "Ils/Elles": "fussent"
    },
    "Impératif Présent": {
      "Tu": "sois",
      "Nous": "soyons",
      "Vous": "soyez"
    },
    "Impératif Passé": {
      "Tu": "aie été",
      "Nous": "ayons été",
      "Vous": "ayez été"
    },
    "Infinitif Présent": "être",
    "Infinitif Passé": "avoir été",
    "Participe Présent": "étant",
    "Participe Passé": "été",
    "Gérondif Présent": "en étant",
    "Gérondif Passé": "en ayant été"
  },
  
  "avoir": {
    "Présent": {
      "Je": "ai",
      "Tu": "as",
      "Il/Elle/On": "a",
      "Nous": "avons",
      "Vous": "avez",
      "Ils/Elles": "ont"
    },
    "Imparfait": {
      "Je": "avais",
      "Tu": "avais",
      "Il/Elle/On": "avait",
      "Nous": "avions",
      "Vous": "aviez",
      "Ils/Elles": "avaient"
    },
    "Passé Composé": {
      "Je": "ai eu",
      "Tu": "as eu",
      "Il/Elle/On": "a eu",
      "Nous": "avons eu",
      "Vous": "avez eu",
      "Ils/Elles": "ont eu"
    },
    "Futur": {
      "Je": "aurai",
      "Tu": "auras",
      "Il/Elle/On": "aura",
      "Nous": "aurons",
      "Vous": "aurez",
      "Ils/Elles": "auront"
    },
    "Plus-que-parfait": {
      "Je": "avais eu",
      "Tu": "avais eu",
      "Il/Elle/On": "avait eu",
      "Nous": "avions eu",
      "Vous": "aviez eu",
      "Ils/Elles": "avaient eu"
    },
    "Futur Simple": {
      "Je": "aurai",
      "Tu": "auras",
      "Il/Elle/On": "aura",
      "Nous": "aurons",
      "Vous": "aurez",
      "Ils/Elles": "auront"
    },
    "Futur Antérieur": {
      "Je": "aurai eu",
      "Tu": "auras eu",
      "Il/Elle/On": "aura eu",
      "Nous": "aurons eu",
      "Vous": "aurez eu",
      "Ils/Elles": "auront eu"
    },
    "Conditionnel Présent": {
      "Je": "aurais",
      "Tu": "aurais",
      "Il/Elle/On": "aurait",
      "Nous": "aurions",
      "Vous": "auriez",
      "Ils/Elles": "auraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais eu",
      "Tu": "aurais eu",
      "Il/Elle/On": "aurait eu",
      "Nous": "aurions eu",
      "Vous": "auriez eu",
      "Ils/Elles": "auraient eu"
    },
    "Subjonctif Présent": {
      "Je": "aie",
      "Tu": "aies",
      "Il/Elle/On": "ait",
      "Nous": "ayons",
      "Vous": "ayez",
      "Ils/Elles": "aient"
    },
    "Subjonctif Passé": {
      "Je": "aie eu",
      "Tu": "aies eu",
      "Il/Elle/On": "ait eu",
      "Nous": "ayons eu",
      "Vous": "ayez eu",
      "Ils/Elles": "aient eu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse eu",
      "Tu": "eusses eu",
      "Il/Elle/On": "eût eu",
      "Nous": "eussions eu",
      "Vous": "eussiez eu",
      "Ils/Elles": "eussent eu"
    },
    "Subjonctif Imparfait": {
      "Je": "eusse",
      "Tu": "eusses",
      "Il/Elle/On": "eût",
      "Nous": "eussions",
      "Vous": "eussiez",
      "Ils/Elles": "eussent"
    },
    "Impératif Présent": {
      "Tu": "aie",
      "Nous": "ayons",
      "Vous": "ayez"
    },
    "Impératif Passé": {
      "Tu": "aie eu",
      "Nous": "ayons eu",
      "Vous": "ayez eu"
    },
    "Infinitif Présent": "avoir",
    "Infinitif Passé": "avoir eu",
    "Participe Présent": "ayant",
    "Participe Passé": "eu",
    "Gérondif Présent": "en ayant",
    "Gérondif Passé": "en ayant eu"
  },

  "aller": {
    "Présent": {
      "Je": "vais",
      "Tu": "vas",
      "Il/Elle/On": "va",
      "Nous": "allons",
      "Vous": "allez",
      "Ils/Elles": "vont"
    },
    "Imparfait": {
      "Je": "allais",
      "Tu": "allais",
      "Il/Elle/On": "allait",
      "Nous": "allions",
      "Vous": "alliez",
      "Ils/Elles": "allaient"
    },
    "Passé Composé": {
      "Je": "suis allé(e)",
      "Tu": "es allé(e)",
      "Il/Elle/On": "est allé(e)",
      "Nous": "sommes allé(e)s",
      "Vous": "êtes allé(e)(s)",
      "Ils/Elles": "sont allé(e)s"
    },
    "Futur": {
      "Je": "irai",
      "Tu": "iras",
      "Il/Elle/On": "ira",
      "Nous": "irons",
      "Vous": "irez",
      "Ils/Elles": "iront"
    },
    "Plus-que-parfait": {
      "Je": "étais allé(e)",
      "Tu": "étais allé(e)",
      "Il/Elle/On": "était allé(e)",
      "Nous": "étions allé(e)s",
      "Vous": "étiez allé(e)(s)",
      "Ils/Elles": "étaient allé(e)s"
    },
    "Futur Simple": {
      "Je": "irai",
      "Tu": "iras",
      "Il/Elle/On": "ira",
      "Nous": "irons",
      "Vous": "irez",
      "Ils/Elles": "iront"
    },
    "Futur Antérieur": {
      "Je": "serai allé(e)",
      "Tu": "seras allé(e)",
      "Il/Elle/On": "sera allé(e)",
      "Nous": "serons allé(e)s",
      "Vous": "serez allé(e)(s)",
      "Ils/Elles": "seront allé(e)s"
    },
    "Conditionnel Présent": {
      "Je": "irais",
      "Tu": "irais",
      "Il/Elle/On": "irait",
      "Nous": "irions",
      "Vous": "iriez",
      "Ils/Elles": "iraient"
    },
    "Conditionnel Passé": {
      "Je": "serais allé(e)",
      "Tu": "serais allé(e)",
      "Il/Elle/On": "serait allé(e)",
      "Nous": "serions allé(e)s",
      "Vous": "seriez allé(e)(s)",
      "Ils/Elles": "seraient allé(e)s"
    },
    "Subjonctif Présent": {
      "Je": "aille",
      "Tu": "ailles",
      "Il/Elle/On": "aille",
      "Nous": "allions",
      "Vous": "alliez",
      "Ils/Elles": "aillent"
    },
    "Subjonctif Passé": {
      "Je": "sois allé(e)",
      "Tu": "sois allé(e)",
      "Il/Elle/On": "soit allé(e)",
      "Nous": "soyons allé(e)s",
      "Vous": "soyez allé(e)(s)",
      "Ils/Elle": "soient allé(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse allé(e)",
      "Tu": "fusses allé(e)",
      "Il/Elle/On": "fût allé(e)",
      "Nous": "fussions allé(e)s",
      "Vous": "fussiez allé(e)(s)",
      "Ils/Elles": "fussent allé(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "allasse",
      "Tu": "allasses",
      "Il/Elle/On": "allât",
      "Nous": "allassions",
      "Vous": "allassiez",
      "Ils/Elles": "allassent"
    },
    "Impératif Présent": {
      "Tu": "va",
      "Nous": "allons",
      "Vous": "allez"
    },
    "Impératif Passé": {
      "Tu": "sois allé(e)",
      "Nous": "soyons allé(e)s",
      "Vous": "soyez allé(e)(s)"
    },
    "Infinitif Présent": "aller",
    "Infinitif Passé": "être allé(e)",
    "Participe Présent": "allant",
    "Participe Passé": "allé(e)",
    "Gérondif Présent": "en allant",
    "Gérondif Passé": "en étant allé(e)"
  },
  "absoudre": {
    "Présent": {
      "Je": "absous",
      "Tu": "absous",
      "Il/Elle/On": "absout",
      "Nous": "absolvons",
      "Vous": "absolvez",
      "Ils/Elles": "absolvent"
    },
    "Imparfait": {
      "Je": "absolvais",
      "Tu": "absolvais",
      "Il/Elle/On": "absolvait",
      "Nous": "absolvions",
      "Vous": "absolviez",
      "Ils/Elles": "absolvaient"
    },
    "Passé Composé": {
      "Je": "ai absous",
      "Tu": "as absous",
      "Il/Elle/On": "a absous",
      "Nous": "avons absous",
      "Vous": "avez absous",
      "Ils/Elles": "ont absous"
    },
    "Futur": {
      "Je": "absoudrai",
      "Tu": "absoudras",
      "Il/Elle/On": "absoudra",
      "Nous": "absoudrons",
      "Vous": "absoudrez",
      "Ils/Elles": "absoudront"
    },
    "Plus-que-parfait": {
      "Je": "avais absous",
      "Tu": "avais absous",
      "Il/Elle/On": "avait absous",
      "Nous": "avions absous",
      "Vous": "aviez absous",
      "Ils/Elles": "avaient absous"
    },
    "Futur Simple": {
      "Je": "absoudrai",
      "Tu": "absoudras",
      "Il/Elle/On": "absoudra",
      "Nous": "absoudrons",
      "Vous": "absoudrez",
      "Ils/Elles": "absoudront"
    },
    "Futur Antérieur": {
      "Je": "aurai absous",
      "Tu": "auras absous",
      "Il/Elle/On": "aura absous",
      "Nous": "aurons absous",
      "Vous": "aurez absous",
      "Ils/Elles": "auront absous"
    },
    "Conditionnel Présent": {
      "Je": "absoudrais",
      "Tu": "absoudrais",
      "Il/Elle/On": "absoudrait",
      "Nous": "absoudrions",
      "Vous": "absoudriez",
      "Ils/Elle": "absoudraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais absous",
      "Tu": "aurais absous",
      "Il/Elle/On": "aurait absous",
      "Nous": "aurions absous",
      "Vous": "auriez absous",
      "Ils/Elle": "auraient absous"
    },
    "Subjonctif Présent": {
      "Je": "absolve",
      "Tu": "absolves",
      "Il/Elle/On": "absolve",
      "Nous": "absolvions",
      "Vous": "absolviez",
      "Ils/Elles": "absolvent"
    },
    "Subjonctif Passé": {
      "Je": "aie absous",
      "Tu": "aies absous",
      "Il/Elle/On": "ait absous",
      "Nous": "ayons absous",
      "Vous": "ayez absous",
      "Ils/Elle": "aient absous"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse absous",
      "Tu": "eusses absous",
      "Il/Elle/On": "eût absous",
      "Nous": "eussions absous",
      "Vous": "eussiez absous",
      "Ils/Elle": "eussent absous"
    },
    "Subjonctif Imparfait": {
      "Je": "absolusse",
      "Tu": "absolusses",
      "Il/Elle/On": "absolût",
      "Nous": "absolussions",
      "Vous": "absolussiez",
      "Ils/Elle": "absolussent"
    },
    "Impératif Présent": {
      "Tu": "absous",
      "Nous": "absolvons",
      "Vous": "absolvez"
    },
    "Impératif Passé": {
      "Tu": "aie absous",
      "Nous": "ayons absous",
      "Vous": "ayez absous"
    },
    "Infinitif Présent": "absoudre",
    "Infinitif Passé": "avoir absous",
    "Participe Présent": "absolvant",
    "Participe Passé": "absous",
    "Gérondif Présent": "en absolvant",
    "Gérondif Passé": "en ayant absous"
  },
  "acquérir": {
    "Présent": {
      "Je": "acquiers",
      "Tu": "acquiers",
      "Il/Elle/On": "acquiert",
      "Nous": "acquérons",
      "Vous": "acquérez",
      "Ils/Elle": "acquièrent"
    },
    "Imparfait": {
      "Je": "acquérais",
      "Tu": "acquérais",
      "Il/Elle/On": "acquérait",
      "Nous": "acquérions",
      "Vous": "acquériez",
      "Ils/Elle": "acquéraient"
    },
    "Passé Composé": {
      "Je": "ai acquis",
      "Tu": "as acquis",
      "Il/Elle/On": "a acquis",
      "Nous": "avons acquis",
      "Vous": "avez acquis",
      "Ils/Elle": "ont acquis"
    },
    "Futur": {
      "Je": "acquerrai",
      "Tu": "acquerras",
      "Il/Elle/On": "acquerra",
      "Nous": "acquerrons",
      "Vous": "acquerrez",
      "Ils/Elle": "acquerront"
    },
    "Plus-que-parfait": {
      "Je": "avais acquis",
      "Tu": "avais acquis",
      "Il/Elle/On": "avait acquis",
      "Nous": "avions acquis",
      "Vous": "aviez acquis",
      "Ils/Elle": "avaient acquis"
    },
    "Futur Simple": {
      "Je": "acquerrai",
      "Tu": "acquerras",
      "Il/Elle/On": "acquerra",
      "Nous": "acquerrons",
      "Vous": "acquerrez",
      "Ils/Elle": "acquerront"
    },
    "Futur Antérieur": {
      "Je": "aurai acquis",
      "Tu": "auras acquis",
      "Il/Elle/On": "aura acquis",
      "Nous": "aurons acquis",
      "Vous": "aurez acquis",
      "Ils/Elle": "auront acquis"
    },
    "Conditionnel Présent": {
      "Je": "acquerrais",
      "Tu": "acquerrais",
      "Il/Elle/On": "acquerrait",
      "Nous": "acquerrions",
      "Vous": "acquerriez",
      "Ils/Elle": "acquerraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais acquis",
      "Tu": "aurais acquis",
      "Il/Elle/On": "aurait acquis",
      "Nous": "aurions acquis",
      "Vous": "auriez acquis",
      "Ils/Elle": "auraient acquis"
    },
    "Subjonctif Présent": {
      "Je": "acquière",
      "Tu": "acquières",
      "Il/Elle/On": "acquière",
      "Nous": "acquérions",
      "Vous": "acquériez",
      "Ils/Elle": "acquièrent"
    },
    "Subjonctif Passé": {
      "Je": "aie acquis",
      "Tu": "aies acquis",
      "Il/Elle/On": "ait acquis",
      "Nous": "ayons acquis",
      "Vous": "ayez acquis",
      "Ils/Elle": "aient acquis"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse acquis",
      "Tu": "eusses acquis",
      "Il/Elle/On": "eût acquis",
      "Nous": "eussions acquis",
      "Vous": "eussiez acquis",
      "Ils/Elle": "eussent acquis"
    },
    "Subjonctif Imparfait": {
      "Je": "acquisse",
      "Tu": "acquisses",
      "Il/Elle/On": "acquît",
      "Nous": "acquissions",
      "Vous": "acquissiez",
      "Ils/Elle": "acquissent"
    },
    "Impératif Présent": {
      "Tu": "acquiers",
      "Nous": "acquérons",
      "Vous": "acquérez"
    },
    "Impératif Passé": {
      "Tu": "aie acquis",
      "Nous": "ayons acquis",
      "Vous": "ayez acquis"
    },
    "Infinitif Présent": "acquérir",
    "Infinitif Passé": "avoir acquis",
    "Participe Présent": "acquérant",
    "Participe Passé": "acquis",
    "Gérondif Présent": "en acquérant",
    "Gérondif Passé": "en ayant acquis"
  },
  "aimer": {
    "Présent": {
      "Je": "aime",
      "Tu": "aimes",
      "Il/Elle/On": "aime",
      "Nous": "aimons",
      "Vous": "aimez",
      "Ils/Elle": "aiment"
    },
    "Imparfait": {
      "Je": "aimais",
      "Tu": "aimais",
      "Il/Elle/On": "aimait",
      "Nous": "aimions",
      "Vous": "aimiez",
      "Ils/Elle": "aimaient"
    },
    "Passé Composé": {
      "Je": "ai aimé",
      "Tu": "as aimé",
      "Il/Elle/On": "a aimé",
      "Nous": "avons aimé",
      "Vous": "avez aimé",
      "Ils/Elle": "ont aimé"
    },
    "Futur": {
      "Je": "aimerai",
      "Tu": "aimeras",
      "Il/Elle/On": "aimera",
      "Nous": "aimerons",
      "Vous": "aimerez",
      "Ils/Elle": "aimeront"
    },
    "Plus-que-parfait": {
      "Je": "avais aimé",
      "Tu": "avais aimé",
      "Il/Elle/On": "avait aimé",
      "Nous": "avions aimé",
      "Vous": "aviez aimé",
      "Ils/Elle": "avaient aimé"
    },
    "Futur Simple": {
      "Je": "aimerai",
      "Tu": "aimeras",
      "Il/Elle/On": "aimera",
      "Nous": "aimerons",
      "Vous": "aimerez",
      "Ils/Elle": "aimeront"
    },
    "Futur Antérieur": {
      "Je": "aurai aimé",
      "Tu": "auras aimé",
      "Il/Elle/On": "aura aimé",
      "Nous": "aurons aimé",
      "Vous": "aurez aimé",
      "Ils/Elle": "auront aimé"
    },
    "Conditionnel Présent": {
      "Je": "aimerais",
      "Tu": "aimerais",
      "Il/Elle/On": "aimerait",
      "Nous": "aimerions",
      "Vous": "aimeriez",
      "Ils/Elle": "aimeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais aimé",
      "Tu": "aurais aimé",
      "Il/Elle/On": "aurait aimé",
      "Nous": "aurions aimé",
      "Vous": "auriez aimé",
      "Ils/Elle": "auraient aimé"
    },
    "Subjonctif Présent": {
      "Je": "aime",
      "Tu": "aimes",
      "Il/Elle/On": "aime",
      "Nous": "aimions",
      "Vous": "aimiez",
      "Ils/Elle": "aiment"
    },
    "Subjonctif Passé": {
      "Je": "aie aimé",
      "Tu": "aies aimé",
      "Il/Elle/On": "ait aimé",
      "Nous": "ayons aimé",
      "Vous": "ayez aimé",
      "Ils/Elle": "aient aimé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse aimé",
      "Tu": "eusses aimé",
      "Il/Elle/On": "eût aimé",
      "Nous": "eussions aimé",
      "Vous": "eussiez aimé",
      "Ils/Elle": "eussent aimé"
    },
    "Subjonctif Imparfait": {
      "Je": "aimasse",
      "Tu": "aimasses",
      "Il/Elle/On": "aimât",
      "Nous": "aimassions",
      "Vous": "aimassiez",
      "Ils/Elle": "aimassent"
    },
    "Impératif Présent": {
      "Tu": "aime",
      "Nous": "aimons",
      "Vous": "aimez"
    },
    "Impératif Passé": {
      "Tu": "aie aimé",
      "Nous": "ayons aimé",
      "Vous": "ayez aimé"
    },
    "Infinitif Présent": "aimer",
    "Infinitif Passé": "avoir aimé",
    "Participe Présent": "aimant",
    "Participe Passé": "aimé",
    "Gérondif Présent": "en aimant",
    "Gérondif Passé": "en ayant aimé"
  },
  "apprécier": {
    "Présent": {
      "Je": "apprécie",
      "Tu": "apprécies",
      "Il/Elle/On": "apprécie",
      "Nous": "apprécions",
      "Vous": "appréciez",
      "Ils/Elle": "apprécient"
    },
    "Imparfait": {
      "Je": "appréciais",
      "Tu": "appréciais",
      "Il/Elle/On": "appréciait",
      "Nous": "appréciions",
      "Vous": "appréciiez",
      "Ils/Elle": "appréciaient"
    },
    "Passé Composé": {
      "Je": "ai apprécié",
      "Tu": "as apprécié",
      "Il/Elle/On": "a apprécié",
      "Nous": "avons apprécié",
      "Vous": "avez apprécié",
      "Ils/Elle": "ont apprécié"
    },
    "Futur": {
      "Je": "apprécierai",
      "Tu": "apprécieras",
      "Il/Elle/On": "appréciera",
      "Nous": "apprécierons",
      "Vous": "apprécierez",
      "Ils/Elle": "apprécieront"
    },
    "Plus-que-parfait": {
      "Je": "avais apprécié",
      "Tu": "avais apprécié",
      "Il/Elle/On": "avait apprécié",
      "Nous": "avions apprécié",
      "Vous": "aviez apprécié",
      "Ils/Elle": "avaient apprécié"
    },
    "Futur Simple": {
      "Je": "apprécierai",
      "Tu": "apprécieras",
      "Il/Elle/On": "appréciera",
      "Nous": "apprécierons",
      "Vous": "apprécierez",
      "Ils/Elle": "apprécieront"
    },
    "Futur Antérieur": {
      "Je": "aurai apprécié",
      "Tu": "auras apprécié",
      "Il/Elle/On": "aura apprécié",
      "Nous": "aurons apprécié",
      "Vous": "aurez apprécié",
      "Ils/Elle": "auront apprécié"
    },
    "Conditionnel Présent": {
      "Je": "apprécierais",
      "Tu": "apprécierais",
      "Il/Elle/On": "apprécierait",
      "Nous": "apprécierions",
      "Vous": "apprécieriez",
      "Ils/Elle": "apprécieraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais apprécié",
      "Tu": "aurais apprécié",
      "Il/Elle/On": "aurait apprécié",
      "Nous": "aurions apprécié",
      "Vous": "auriez apprécié",
      "Ils/Elle": "auraient apprécié"
    },
    "Subjonctif Présent": {
      "Je": "apprécie",
      "Tu": "apprécies",
      "Il/Elle/On": "apprécie",
      "Nous": "appréciions",
      "Vous": "appréciiez",
      "Ils/Elle": "apprécient"
    },
    "Subjonctif Passé": {
      "Je": "aie apprécié",
      "Tu": "aies apprécié",
      "Il/Elle/On": "ait apprécié",
      "Nous": "ayons apprécié",
      "Vous": "ayez apprécié",
      "Ils/Elle": "aient apprécié"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse apprécié",
      "Tu": "eusses apprécié",
      "Il/Elle/On": "eût apprécié",
      "Nous": "eussions apprécié",
      "Vous": "eussiez apprécié",
      "Ils/Elle": "eussent apprécié"
    },
    "Subjonctif Imparfait": {
      "Je": "appréciasse",
      "Tu": "appréciasses",
      "Il/Elle/On": "appréciât",
      "Nous": "appréciassions",
      "Vous": "appréciassiez",
      "Ils/Elle": "appréciassent"
    },
    "Impératif Présent": {
      "Tu": "apprécie",
      "Nous": "apprécions",
      "Vous": "appréciez"
    },
    "Impératif Passé": {
      "Tu": "aie apprécié",
      "Nous": "ayons apprécié",
      "Vous": "ayez apprécié"
    },
    "Infinitif Présent": "apprécier",
    "Infinitif Passé": "avoir apprécié",
    "Participe Présent": "appréciant",
    "Participe Passé": "apprécié",
    "Gérondif Présent": "en appréciant",
    "Gérondif Passé": "en ayant apprécié"
  },
  "assaillir": {
    "Présent": {
      "Je": "assaille",
      "Tu": "assaillis",
      "Il/Elle/On": "assaille",
      "Nous": "assaillons",
      "Vous": "assaillez",
      "Ils/Elle": "assaillent"
    },
    "Imparfait": {
      "Je": "assaillais",
      "Tu": "assaillais",
      "Il/Elle/On": "assaillait",
      "Nous": "assaillions",
      "Vous": "assailliez",
      "Ils/Elle": "assaillaient"
    },
    "Passé Composé": {
      "Je": "ai assailli",
      "Tu": "as assailli",
      "Il/Elle/On": "a assailli",
      "Nous": "avons assailli",
      "Vous": "avez assailli",
      "Ils/Elle": "ont assailli"
    },
    "Futur": {
      "Je": "assaillirai",
      "Tu": "assailliras",
      "Il/Elle/On": "assaillira",
      "Nous": "assaillirons",
      "Vous": "assaillirez",
      "Ils/Elle": "assailliront"
    },
    "Plus-que-parfait": {
      "Je": "avais assailli",
      "Tu": "avais assailli",
      "Il/Elle/On": "avait assailli",
      "Nous": "avions assailli",
      "Vous": "aviez assailli",
      "Ils/Elle": "avaient assailli"
    },
    "Futur Simple": {
      "Je": "assaillirai",
      "Tu": "assailliras",
      "Il/Elle/On": "assaillira",
      "Nous": "assaillirons",
      "Vous": "assaillirez",
      "Ils/Elle": "assailliront"
    },
    "Futur Antérieur": {
      "Je": "aurai assailli",
      "Tu": "auras assailli",
      "Il/Elle/On": "aura assailli",
      "Nous": "aurons assailli",
      "Vous": "aurez assailli",
      "Ils/Elle": "auront assailli"
    },
    "Conditionnel Présent": {
      "Je": "assaillirais",
      "Tu": "assaillirais",
      "Il/Elle/On": "assaillirait",
      "Nous": "assaillirions",
      "Vous": "assailliriez",
      "Ils/Elle": "assailliraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais assailli",
      "Tu": "aurais assailli",
      "Il/Elle/On": "aurait assailli",
      "Nous": "aurions assailli",
      "Vous": "auriez assailli",
      "Ils/Elle": "auraient assailli"
    },
    "Subjonctif Présent": {
      "Je": "assaillisse",
      "Tu": "assaillisses",
      "Il/Elle/On": "assaillisse",
      "Nous": "assaillissions",
      "Vous": "assaillissiez",
      "Ils/Elle": "assaillissent"
    },
    "Subjonctif Passé": {
      "Je": "aie assailli",
      "Tu": "aies assailli",
      "Il/Elle/On": "ait assailli",
      "Nous": "ayons assailli",
      "Vous": "ayez assailli",
      "Ils/Elle": "aient assailli"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse assailli",
      "Tu": "eusses assailli",
      "Il/Elle/On": "eût assailli",
      "Nous": "eussions assailli",
      "Vous": "eussiez assailli",
      "Ils/Elle": "eussent assailli"
    },
    "Subjonctif Imparfait": {
      "Je": "assaillisse",
      "Tu": "assaillisses",
      "Il/Elle/On": "assaillît",
      "Nous": "assaillissions",
      "Vous": "assaillissiez",
      "Ils/Elle": "assaillissent"
    },
    "Impératif Présent": {
      "Tu": "assaille",
      "Nous": "assaillons",
      "Vous": "assaillez"
    },
    "Impératif Passé": {
      "Tu": "aie assailli",
      "Nous": "ayons assailli",
      "Vous": "ayez assailli"
    },
    "Infinitif Présent": "assaillir",
    "Infinitif Passé": "avoir assailli",
    "Participe Présent": "assaillant",
    "Participe Passé": "assailli",
    "Gérondif Présent": "en assaillant",
    "Gérondif Passé": "en ayant assailli"
  },
  "asseoir": {
    "Présent": {
      "Je": "assieds",
      "Tu": "assieds",
      "Il/Elle/On": "assied",
      "Nous": "asseyons",
      "Vous": "asseyez",
      "Ils/Elle": "asseyent"
    },
    "Imparfait": {
      "Je": "asseyais",
      "Tu": "asseyais",
      "Il/Elle/On": "asseyait",
      "Nous": "asseyions",
      "Vous": "asseyiez",
      "Ils/Elle": "asseyait"
    },
    "Passé Composé": {
      "Je": "ai assis",
      "Tu": "as assis",
      "Il/Elle/On": "a assis",
      "Nous": "avons assis",
      "Vous": "avez assis",
      "Ils/Elle": "ont assis"
    },
    "Futur": {
      "Je": "assiérai",
      "Tu": "assiéras",
      "Il/Elle/On": "assiéra",
      "Nous": "assiérons",
      "Vous": "assiérez",
      "Ils/Elle": "assiéront"
    },
    "Plus-que-parfait": {
      "Je": "avais assis",
      "Tu": "avais assis",
      "Il/Elle/On": "avait assis",
      "Nous": "avions assis",
      "Vous": "aviez assis",
      "Ils/Elle": "avaient assis"
    },
    "Futur Simple": {
      "Je": "assiérai",
      "Tu": "assiéras",
      "Il/Elle/On": "assiéra",
      "Nous": "assiérons",
      "Vous": "assiérez",
      "Ils/Elle": "assiéront"
    },
    "Futur Antérieur": {
      "Je": "aurai assis",
      "Tu": "auras assis",
      "Il/Elle/On": "aura assis",
      "Nous": "aurons assis",
      "Vous": "aurez assis",
      "Ils/Elle": "auront assis"
    },
    "Conditionnel Présent": {
      "Je": "assiérais",
      "Tu": "assiérais",
      "Il/Elle/On": "assiérerait",
      "Nous": "assiérons",
      "Vous": "assiéreriez",
      "Ils/Elle": "assiéreraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais assis",
      "Tu": "aurais assis",
      "Il/Elle/On": "aurait assis",
      "Nous": "aurions assis",
      "Vous": "auriez assis",
      "Ils/Elle": "auraient assis"
    },
    "Subjonctif Présent": {
      "Je": "asseye",
      "Tu": "asseyes",
      "Il/Elle/On": "asseye",
      "Nous": "asseyions",
      "Vous": "asseyiez",
      "Ils/Elle": "asseyent"
    },
    "Subjonctif Passé": {
      "Je": "aie assis",
      "Tu": "aies assis",
      "Il/Elle/On": "ait assis",
      "Nous": "ayons assis",
      "Vous": "ayez assis",
      "Ils/Elle": "aient assis"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse assis",
      "Tu": "eusses assis",
      "Il/Elle/On": "eût assis",
      "Nous": "eussions assis",
      "Vous": "eussiez assis",
      "Ils/Elle": "eussent assis"
    },
    "Subjonctif Imparfait": {
      "Je": "assisse",
      "Tu": "assisses",
      "Il/Elle/On": "assît",
      "Nous": "assissions",
      "Vous": "assissiez",
      "Ils/Elle": "assissent"
    },
    "Impératif Présent": {
      "Tu": "assieds",
      "Nous": "asseyons",
      "Vous": "asseyez"
    },
    "Impératif Passé": {
      "Tu": "aie assis",
      "Nous": "ayons assis",
      "Vous": "ayez assis"
    },
    "Infinitif Présent": "asseoir",
    "Infinitif Passé": "avoir assis",
    "Participe Présent": "asseyant",
    "Participe Passé": "assis",
    "Gérondif Présent": "en asseyant",
    "Gérondif Passé": "en ayant assis"
  },
  "assiégir": {
    "Présent": {
      "Je": "assiège",
      "Tu": "assièges",
      "Il/Elle/On": "assiège",
      "Nous": "assiégeons",
      "Vous": "assiégez",
      "Ils/Elle": "assiègent"
    },
    "Imparfait": {
      "Je": "assiégeais",
      "Tu": "assiégeais",
      "Il/Elle/On": "assiégeait",
      "Nous": "assiégions",
      "Vous": "assiégiez",
      "Ils/Elle": "assiégeaient"
    },
    "Passé Composé": {
      "Je": "ai assiégé",
      "Tu": "as assiégé",
      "Il/Elle/On": "a assiégé",
      "Nous": "avons assiégé",
      "Vous": "avez assiégé",
      "Ils/Elle": "ont assiégé"
    },
    "Futur": {
      "Je": "assiégerai",
      "Tu": "assiégeras",
      "Il/Elle/On": "assiégera",
      "Nous": "assiégerons",
      "Vous": "assiégerez",
      "Ils/Elle": "assiégeront"
    },
    "Plus-que-parfait": {
      "Je": "avais assiégé",
      "Tu": "avais assiégé",
      "Il/Elle/On": "avait assiégé",
      "Nous": "avions assiégé",
      "Vous": "aviez assiégé",
      "Ils/Elle": "avaient assiégé"
    },
    "Futur Simple": {
      "Je": "assiégerai",
      "Tu": "assiégeras",
      "Il/Elle/On": "assiégera",
      "Nous": "assiégerons",
      "Vous": "assiégerez",
      "Ils/Elle": "assiégeront"
    },
    "Futur Antérieur": {
      "Je": "aurai assiégé",
      "Tu": "auras assiégé",
      "Il/Elle/On": "aura assiégé",
      "Nous": "aurons assiégé",
      "Vous": "aurez assiégé",
      "Ils/Elle": "auront assiégé"
    },
    "Conditionnel Présent": {
      "Je": "assiégerais",
      "Tu": "assiégerais",
      "Il/Elle/On": "assiégerait",
      "Nous": "assiégerions",
      "Vous": "assiégeriez",
      "Ils/Elle": "assiégeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais assiégé",
      "Tu": "aurais assiégé",
      "Il/Elle/On": "aurait assiégé",
      "Nous": "aurions assiégé",
      "Vous": "auriez assiégé",
      "Ils/Elle": "auraient assiégé"
    },
    "Subjonctif Présent": {
      "Je": "assiège",
      "Tu": "assièges",
      "Il/Elle/On": "assiège",
      "Nous": "assiégions",
      "Vous": "assiégiez",
      "Ils/Elle": "assiègent"
    },
    "Subjonctif Passé": {
      "Je": "aie assiégé",
      "Tu": "aies assiégé",
      "Il/Elle/On": "ait assiégé",
      "Nous": "ayons assiégé",
      "Vous": "ayez assiégé",
      "Ils/Elle": "aient assiégé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse assiégé",
      "Tu": "eusses assiégé",
      "Il/Elle/On": "eût assiégé",
      "Nous": "eussions assiégé",
      "Vous": "eussiez assiégé",
      "Ils/Elle": "eussent assiégé"
    },
    "Subjonctif Imparfait": {
      "Je": "assiégeasse",
      "Tu": "assiégeasses",
      "Il/Elle/On": "assiégeât",
      "Nous": "assiégeassions",
      "Vous": "assiégeassiez",
      "Ils/Elle": "assiégeassent"
    },
    "Impératif Présent": {
      "Tu": "assiège",
      "Nous": "assiégeons",
      "Vous": "assiégez"
    },
    "Impératif Passé": {
      "Tu": "aie assiégé",
      "Nous": "ayons assiégé",
      "Vous": "ayez assiégé"
    },
    "Infinitif Présent": "assiéger",
    "Infinitif Passé": "avoir assiégé",
    "Participe Présent": "assiégeant",
    "Participe Passé": "assiégé",
    "Gérondif Présent": "en assiégeant",
    "Gérondif Passé": "en ayant assiégé"
  },
  "battre": {
    "Présent": {
      "Je": "bats",
      "Tu": "bats",
      "Il/Elle/On": "bat",
      "Nous": "battons",
      "Vous": "battez",
      "Ils/Elle": "battent"
    },
    "Imparfait": {
      "Je": "battais",
      "Tu": "battais",
      "Il/Elle/On": "battait",
      "Nous": "battions",
      "Vous": "battiez",
      "Ils/Elle": "battaient"
    },
    "Passé Composé": {
      "Je": "ai battu",
      "Tu": "as battu",
      "Il/Elle/On": "a battu",
      "Nous": "avons battu",
      "Vous": "avez battu",
      "Ils/Elle": "ont battu"
    },
    "Futur": {
      "Je": "battrai",
      "Tu": "battras",
      "Il/Elle/On": "battra",
      "Nous": "battrons",
      "Vous": "battrez",
      "Ils/Elle": "battront"
    },
    "Plus-que-parfait": {
      "Je": "avais battu",
      "Tu": "avais battu",
      "Il/Elle/On": "avait battu",
      "Nous": "avions battu",
      "Vous": "aviez battu",
      "Ils/Elle": "avaient battu"
    },
    "Futur Simple": {
      "Je": "battrai",
      "Tu": "battras",
      "Il/Elle/On": "battra",
      "Nous": "battrons",
      "Vous": "battrez",
      "Ils/Elle": "battront"
    },
    "Futur Antérieur": {
      "Je": "aurai battu",
      "Tu": "auras battu",
      "Il/Elle/On": "aura battu",
      "Nous": "aurons battu",
      "Vous": "aurez battu",
      "Ils/Elle": "auront battu"
    },
    "Conditionnel Présent": {
      "Je": "battrais",
      "Tu": "battrais",
      "Il/Elle/On": "battrait",
      "Nous": "battrions",
      "Vous": "battriez",
      "Ils/Elle": "battraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais battu",
      "Tu": "aurais battu",
      "Il/Elle/On": "aurait battu",
      "Nous": "aurions battu",
      "Vous": "auriez battu",
      "Ils/Elle": "auraient battu"
    },
    "Subjonctif Présent": {
      "Je": "batte",
      "Tu": "battes",
      "Il/Elle/On": "batte",
      "Nous": "battions",
      "Vous": "battiez",
      "Ils/Elle": "battent"
    },
    "Subjonctif Passé": {
      "Je": "aie battu",
      "Tu": "aies battu",
      "Il/Elle/On": "ait battu",
      "Nous": "ayons battu",
      "Vous": "ayez battu",
      "Ils/Elle": "aient battu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse battu",
      "Tu": "eusses battu",
      "Il/Elle/On": "eût battu",
      "Nous": "eussions battu",
      "Vous": "eussiez battu",
      "Ils/Elle": "eussent battu"
    },
    "Subjonctif Imparfait": {
      "Je": "battisse",
      "Tu": "battisses",
      "Il/Elle/On": "battît",
      "Nous": "battissions",
      "Vous": "battissiez",
      "Ils/Elle": "battissent"
    },
    "Impératif Présent": {
      "Tu": "bats",
      "Nous": "battons",
      "Vous": "battez"
    },
    "Impératif Passé": {
      "Tu": "aie battu",
      "Nous": "ayons battu",
      "Vous": "ayez battu"
    },
    "Infinitif Présent": "battre",
    "Infinitif Passé": "avoir battu",
    "Participe Présent": "battant",
    "Participe Passé": "battu",
    "Gérondif Présent": "en battant",
    "Gérondif Passé": "en ayant battu"
  },
  "boitiller": {
    "Présent": {
      "Je": "boitille",
      "Tu": "boitilles",
      "Il/Elle/On": "boitille",
      "Nous": "boitillons",
      "Vous": "boitillez",
      "Ils/Elle": "boitillent"
    },
    "Imparfait": {
      "Je": "boitillais",
      "Tu": "boitillais",
      "Il/Elle/On": "boitillait",
      "Nous": "boitillions",
      "Vous": "boitilliez",
      "Ils/Elle": "boitillaient"
    },
    "Passé Composé": {
      "Je": "ai boitillé",
      "Tu": "as boitillé",
      "Il/Elle/On": "a boitillé",
      "Nous": "avons boitillé",
      "Vous": "avez boitillé",
      "Ils/Elle": "ont boitillé"
    },
    "Futur": {
      "Je": "boitillerai",
      "Tu": "boitilleras",
      "Il/Elle/On": "boitillera",
      "Nous": "boitillerons",
      "Vous": "boitillerez",
      "Ils/Elle": "boitilleront"
    },
    "Plus-que-parfait": {
      "Je": "avais boitillé",
      "Tu": "avais boitillé",
      "Il/Elle/On": "avait boitillé",
      "Nous": "avions boitillé",
      "Vous": "aviez boitillé",
      "Ils/Elle": "avaient boitillé"
    },
    "Futur Simple": {
      "Je": "boitillerai",
      "Tu": "boitilleras",
      "Il/Elle/On": "boitillera",
      "Nous": "boitillerons",
      "Vous": "boitillerez",
      "Ils/Elle": "boitilleront"
    },
    "Futur Antérieur": {
      "Je": "aurai boitillé",
      "Tu": "auras boitillé",
      "Il/Elle/On": "aura boitillé",
      "Nous": "aurons boitillé",
      "Vous": "aurez boitillé",
      "Ils/Elle": "auront boitillé"
    },
    "Conditionnel Présent": {
      "Je": "boitillerais",
      "Tu": "boitillerais",
      "Il/Elle/On": "boitillerait",
      "Nous": "boitillerions",
      "Vous": "boitilleriez",
      "Ils/Elle": "boitilleraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais boitillé",
      "Tu": "aurais boitillé",
      "Il/Elle/On": "aurait boitillé",
      "Nous": "aurions boitillé",
      "Vous": "auriez boitillé",
      "Ils/Elle": "auraient boitillé"
    },
    "Subjonctif Présent": {
      "Je": "boitille",
      "Tu": "boitilles",
      "Il/Elle/On": "boitille",
      "Nous": "boitillions",
      "Vous": "boitilliez",
      "Ils/Elle": "boitillent"
    },
    "Subjonctif Passé": {
      "Je": "aie boitillé",
      "Tu": "aies boitillé",
      "Il/Elle/On": "ait boitillé",
      "Nous": "ayons boitillé",
      "Vous": "ayez boitillé",
      "Ils/Elle": "aient boitillé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse boitillé",
      "Tu": "eusses boitillé",
      "Il/Elle/On": "eût boitillé",
      "Nous": "eussions boitillé",
      "Vous": "eussiez boitillé",
      "Ils/Elle": "eussent boitillé"
    },
    "Subjonctif Imparfait": {
      "Je": "boitillasse",
      "Tu": "boitillasses",
      "Il/Elle/On": "boitillât",
      "Nous": "boitillassions",
      "Vous": "boitillassiez",
      "Ils/Elle": "boitillassent"
    },
    "Impératif Présent": {
      "Tu": "boitille",
      "Nous": "boitillons",
      "Vous": "boitillez"
    },
    "Impératif Passé": {
      "Tu": "aie boitillé",
      "Nous": "ayons boitillé",
      "Vous": "ayez boitillé"
    },
    "Infinitif Présent": "boitiller",
    "Infinitif Passé": "avoir boitillé",
    "Participe Présent": "boitillant",
    "Participe Passé": "boitillé",
    "Gérondif Présent": "en boitillant",
    "Gérondif Passé": "en ayant boitillé"
  },
  "bouillir": {
    "Présent": {
      "Je": "bouis",
      "Tu": "bouis",
      "Il/Elle/On": "bouit",
      "Nous": "bouillissons",
      "Vous": "bouillissez",
      "Ils/Elle": "bouillissent"
    },
    "Imparfait": {
      "Je": "bouillais",
      "Tu": "bouillais",
      "Il/Elle/On": "bouillait",
      "Nous": "bouillions",
      "Vous": "bouilliez",
      "Ils/Elle": "bouillaient"
    },
    "Passé Composé": {
      "Je": "ai bouilli",
      "Tu": "as bouilli",
      "Il/Elle/On": "a bouilli",
      "Nous": "avons bouilli",
      "Vous": "avez bouilli",
      "Ils/Elle": "ont bouilli"
    },
    "Futur": {
      "Je": "bouillirai",
      "Tu": "bouilliras",
      "Il/Elle/On": "bouillira",
      "Nous": "bouillirons",
      "Vous": "bouillirez",
      "Ils/Elle": "bouilliront"
    },
    "Plus-que-parfait": {
      "Je": "avais bouilli",
      "Tu": "avais bouilli",
      "Il/Elle/On": "avait bouilli",
      "Nous": "avions bouilli",
      "Vous": "aviez bouilli",
      "Ils/Elle": "avaient bouilli"
    },
    "Futur Simple": {
      "Je": "bouillirai",
      "Tu": "bouilliras",
      "Il/Elle/On": "bouillira",
      "Nous": "bouillirons",
      "Vous": "bouillirez",
      "Ils/Elle": "bouilliront"
    },
    "Futur Antérieur": {
      "Je": "aurai bouilli",
      "Tu": "auras bouilli",
      "Il/Elle/On": "aura bouilli",
      "Nous": "aurons bouilli",
      "Vous": "aurez bouilli",
      "Ils/Elle": "auront bouilli"
    },
    "Conditionnel Présent": {
      "Je": "bouillirais",
      "Tu": "bouillirais",
      "Il/Elle/On": "bouillirait",
      "Nous": "bouillirions",
      "Vous": "bouilliriez",
      "Ils/Elle": "bouilliraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais bouilli",
      "Tu": "aurais bouilli",
      "Il/Elle/On": "aurait bouilli",
      "Nous": "aurions bouilli",
      "Vous": "auriez bouilli",
      "Ils/Elle": "auraient bouilli"
    },
    "Subjonctif Présent": {
      "Je": "bouille",
      "Tu": "bouilles",
      "Il/Elle/On": "bouille",
      "Nous": "bouillions",
      "Vous": "bouilliez",
      "Ils/Elle": "bouillent"
    },
    "Subjonctif Passé": {
      "Je": "aie bouilli",
      "Tu": "aies bouilli",
      "Il/Elle/On": "ait bouilli",
      "Nous": "ayons bouilli",
      "Vous": "ayez bouilli",
      "Ils/Elle": "aient bouilli"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse bouilli",
      "Tu": "eusses bouilli",
      "Il/Elle/On": "eût bouilli",
      "Nous": "eussions bouilli",
      "Vous": "eussiez bouilli",
      "Ils/Elle": "eussent bouilli"
    },
    "Subjonctif Imparfait": {
      "Je": "bouillisse",
      "Tu": "bouillisses",
      "Il/Elle/On": "bouillît",
      "Nous": "bouillissions",
      "Vous": "bouillissiez",
      "Ils/Elle": "bouillissent"
    },
    "Impératif Présent": {
      "Tu": "bouis",
      "Nous": "bouillissons",
      "Vous": "bouillissez"
    },
    "Impératif Passé": {
      "Tu": "aie bouilli",
      "Nous": "ayons bouilli",
      "Vous": "ayez bouilli"
    },
    "Infinitif Présent": "bouillir",
    "Infinitif Passé": "avoir bouilli",
    "Participe Présent": "bouillant",
    "Participe Passé": "bouilli",
    "Gérondif Présent": "en bouillant",
    "Gérondif Passé": "en ayant bouilli"
  },
  "broyer": {
    "Présent": {
      "Je": "broie",
      "Tu": "broies",
      "Il/Elle/On": "broie",
      "Nous": "broyons",
      "Vous": "broiez",
      "Ils/Elle": "broient"
    },
    "Imparfait": {
      "Je": "broyais",
      "Tu": "broyais",
      "Il/Elle/On": "broyait",
      "Nous": "broyions",
      "Vous": "broyiez",
      "Ils/Elle": "broyaient"
    },
    "Passé Composé": {
      "Je": "ai broyé",
      "Tu": "as broyé",
      "Il/Elle/On": "a broyé",
      "Nous": "avons broyé",
      "Vous": "avez broyé",
      "Ils/Elle": "ont broyé"
    },
    "Futur": {
      "Je": "broierai",
      "Tu": "broieras",
      "Il/Elle/On": "broiera",
      "Nous": "broierons",
      "Vous": "broyerez",
      "Ils/Elle": "broieront"
    },
    "Plus-que-parfait": {
      "Je": "avais broyé",
      "Tu": "avais broyé",
      "Il/Elle/On": "avait broyé",
      "Nous": "avions broyé",
      "Vous": "aviez broyé",
      "Ils/Elle": "avaient broyé"
    },
    "Futur Simple": {
      "Je": "broierai",
      "Tu": "broieras",
      "Il/Elle/On": "broiera",
      "Nous": "broierons",
      "Vous": "broyerez",
      "Ils/Elle": "broieront"
    },
    "Futur Antérieur": {
      "Je": "aurai broyé",
      "Tu": "auras broyé",
      "Il/Elle/On": "aura broyé",
      "Nous": "aurons broyé",
      "Vous": "aurez broyé",
      "Ils/Elle": "auront broyé"
    },
    "Conditionnel Présent": {
      "Je": "broierais",
      "Tu": "broierais",
      "Il/Elle/On": "broierait",
      "Nous": "broierions",
      "Vous": "broieriez",
      "Ils/Elle": "broieraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais broyé",
      "Tu": "aurais broyé",
      "Il/Elle/On": "aurait broyé",
      "Nous": "aurions broyé",
      "Vous": "auriez broyé",
      "Ils/Elle": "auraient broyé"
    },
    "Subjonctif Présent": {
      "Je": "broie",
      "Tu": "broies",
      "Il/Elle/On": "broie",
      "Nous": "broyions",
      "Vous": "broyiez",
      "Ils/Elle": "broient"
    },
    "Subjonctif Passé": {
      "Je": "aie broyé",
      "Tu": "aies broyé",
      "Il/Elle/On": "ait broyé",
      "Nous": "ayons broyé",
      "Vous": "ayez broyé",
      "Ils/Elle": "aient broyé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse broyé",
      "Tu": "eusses broyé",
      "Il/Elle/On": "eût broyé",
      "Nous": "eussions broyé",
      "Vous": "eussiez broyé",
      "Ils/Elle": "eussent broyé"
    },
    "Subjonctif Imparfait": {
      "Je": "broyasse",
      "Tu": "broyasses",
      "Il/Elle/On": "broyât",
      "Nous": "broyassions",
      "Vous": "broyassiez",
      "Ils/Elle": "broyassent"
    },
    "Impératif Présent": {
      "Tu": "broie",
      "Nous": "broyons",
      "Vous": "broiez"
    },
    "Impératif Passé": {
      "Tu": "aie broyé",
      "Nous": "ayons broyé",
      "Vous": "ayez broyé"
    },
    "Infinitif Présent": "broyer",
    "Infinitif Passé": "avoir broyé",
    "Participe Présent": "broyant",
    "Participe Passé": "broyé",
    "Gérondif Présent": "en broyant",
    "Gérondif Passé": "en ayant broyé"
  },
  "céder": {
    "Présent": {
      "Je": "cède",
      "Tu": "cèdes",
      "Il/Elle/On": "cède",
      "Nous": "cédons",
      "Vous": "cédez",
      "Ils/Elle": "cèdent"
    },
    "Imparfait": {
      "Je": "cédais",
      "Tu": "cédais",
      "Il/Elle/On": "cédait",
      "Nous": "cédions",
      "Vous": "cédiez",
      "Ils/Elle": "cédaient"
    },
    "Passé Composé": {
      "Je": "ai cédé",
      "Tu": "as cédé",
      "Il/Elle/On": "a cédé",
      "Nous": "avons cédé",
      "Vous": "avez cédé",
      "Ils/Elle": "ont cédé"
    },
    "Futur": {
      "Je": "céderai",
      "Tu": "céderas",
      "Il/Elle/On": "cédera",
      "Nous": "céderons",
      "Vous": "céderez",
      "Ils/Elle": "céderont"
    },
    "Plus-que-parfait": {
      "Je": "avais cédé",
      "Tu": "avais cédé",
      "Il/Elle/On": "avait cédé",
      "Nous": "avions cédé",
      "Vous": "aviez cédé",
      "Ils/Elle": "avaient cédé"
    },
    "Futur Simple": {
      "Je": "céderai",
      "Tu": "céderas",
      "Il/Elle/On": "cédera",
      "Nous": "céderons",
      "Vous": "céderez",
      "Ils/Elle": "céderont"
    },
    "Futur Antérieur": {
      "Je": "aurai cédé",
      "Tu": "auras cédé",
      "Il/Elle/On": "aura cédé",
      "Nous": "aurons cédé",
      "Vous": "aurez cédé",
      "Ils/Elle": "auront cédé"
    },
    "Conditionnel Présent": {
      "Je": "céderais",
      "Tu": "céderais",
      "Il/Elle/On": "céderait",
      "Nous": "céderions",
      "Vous": "céderiez",
      "Ils/Elle": "céderaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais cédé",
      "Tu": "aurais cédé",
      "Il/Elle/On": "aurait cédé",
      "Nous": "aurions cédé",
      "Vous": "auriez cédé",
      "Ils/Elle": "auraient cédé"
    },
    "Subjonctif Présent": {
      "Je": "cède",
      "Tu": "cèdes",
      "Il/Elle/On": "cède",
      "Nous": "cédions",
      "Vous": "cédiez",
      "Ils/Elle": "cèdent"
    },
    "Subjonctif Passé": {
      "Je": "aie cédé",
      "Tu": "aies cédé",
      "Il/Elle/On": "ait cédé",
      "Nous": "ayons cédé",
      "Vous": "ayez cédé",
      "Ils/Elle": "aient cédé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse cédé",
      "Tu": "eusses cédé",
      "Il/Elle/On": "eût cédé",
      "Nous": "eussions cédé",
      "Vous": "eussiez cédé",
      "Ils/Elle": "eussent cédé"
    },
    "Subjonctif Imparfait": {
      "Je": "cedasse",
      "Tu": "cedasses",
      "Il/Elle/On": "cedât",
      "Nous": "cedassions",
      "Vous": "cedassiez",
      "Ils/Elle": "cedassent"
    },
    "Impératif Présent": {
      "Tu": "cède",
      "Nous": "cédons",
      "Vous": "cédez"
    },
    "Impératif Passé": {
      "Tu": "aie cédé",
      "Nous": "ayons cédé",
      "Vous": "ayez cédé"
    },
    "Infinitif Présent": "céder",
    "Infinitif Passé": "avoir cédé",
    "Participe Présent": "cédant",
    "Participe Passé": "cédé",
    "Gérondif Présent": "en cédant",
    "Gérondif Passé": "en ayant cédé"
  },
  "choir": {
    "Présent": {
      "Je": "chois",
      "Tu": "chois",
      "Il/Elle/On": "choit",
      "Nous": "choyons",
      "Vous": "choyez",
      "Ils/Elle": "choient"
    },
    "Imparfait": {
      "Je": "choyais",
      "Tu": "choyais",
      "Il/Elle/On": "choyait",
      "Nous": "choyions",
      "Vous": "choyiez",
      "Ils/Elle": "choyaient"
    },
    "Passé Composé": {
      "Je": "ai chu",
      "Tu": "as chu",
      "Il/Elle/On": "a chu",
      "Nous": "avons chu",
      "Vous": "avez chu",
      "Ils/Elle": "ont chu"
    },
    "Futur": {
      "Je": "choirai",
      "Tu": "choiras",
      "Il/Elle/On": "choira",
      "Nous": "choirons",
      "Vous": "choirez",
      "Ils/Elle": "choiront"
    },
    "Plus-que-parfait": {
      "Je": "avais chu",
      "Tu": "avais chu",
      "Il/Elle/On": "avait chu",
      "Nous": "avions chu",
      "Vous": "aviez chu",
      "Ils/Elle": "avaient chu"
    },
    "Futur Simple": {
      "Je": "choirai",
      "Tu": "choiras",
      "Il/Elle/On": "choira",
      "Nous": "choirons",
      "Vous": "choirez",
      "Ils/Elle": "choiront"
    },
    "Futur Antérieur": {
      "Je": "aurai chu",
      "Tu": "auras chu",
      "Il/Elle/On": "aura chu",
      "Nous": "aurons chu",
      "Vous": "aurez chu",
      "Ils/Elle": "auront chu"
    },
    "Conditionnel Présent": {
      "Je": "choirais",
      "Tu": "choirais",
      "Il/Elle/On": "choirait",
      "Nous": "choirions",
      "Vous": "choiriez",
      "Ils/Elle": "choiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais chu",
      "Tu": "aurais chu",
      "Il/Elle/On": "aurait chu",
      "Nous": "aurions chu",
      "Vous": "auriez chu",
      "Ils/Elle": "auraient chu"
    },
    "Subjonctif Présent": {
      "Je": "choie",
      "Tu": "choies",
      "Il/Elle/On": "choie",
      "Nous": "choyions",
      "Vous": "choyiez",
      "Ils/Elle": "choient"
    },
    "Subjonctif Passé": {
      "Je": "aie chu",
      "Tu": "aies chu",
      "Il/Elle/On": "ait chu",
      "Nous": "ayons chu",
      "Vous": "ayez chu",
      "Ils/Elle": "aient chu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse chu",
      "Tu": "eusses chu",
      "Il/Elle/On": "eût chu",
      "Nous": "eussions chu",
      "Vous": "eussiez chu",
      "Ils/Elle": "eussent chu"
    },
    "Subjonctif Imparfait": {
      "Je": "chusse",
      "Tu": "chusses",
      "Il/Elle/On": "chût",
      "Nous": "chussions",
      "Vous": "chussiez",
      "Ils/Elle": "chussent"
    },
    "Impératif Présent": {
      "Tu": "chois",
      "Nous": "choyons",
      "Vous": "choyez"
    },
    "Impératif Passé": {
      "Tu": "aie chu",
      "Nous": "ayons chu",
      "Vous": "ayez chu"
    },
    "Infinitif Présent": "choir",
    "Infinitif Passé": "avoir chu",
    "Participe Présent": "choyant",
    "Participe Passé": "chu",
    "Gérondif Présent": "en choyant",
    "Gérondif Passé": "en ayant chu"
  },
  "clore": {
    "Présent": {
      "Je": "clos",
      "Tu": "clos",
      "Il/Elle/On": "clôt",
      "Nous": "clôturons",
      "Vous": "clôturez",
      "Ils/Elle": "clôturent"
    },
    "Imparfait": {
      "Je": "clôturais",
      "Tu": "clôturais",
      "Il/Elle/On": "clôturait",
      "Nous": "clôturions",
      "Vous": "clôturiez",
      "Ils/Elle": "clôturaient"
    },
    "Passé Composé": {
      "Je": "ai clos",
      "Tu": "as clos",
      "Il/Elle/On": "a clos",
      "Nous": "avons clos",
      "Vous": "avez clos",
      "Ils/Elle": "ont clos"
    },
    "Futur": {
      "Je": "clorai",
      "Tu": "cloras",
      "Il/Elle/On": "clora",
      "Nous": "clorons",
      "Vous": "clorerez",
      "Ils/Elle": "cloront"
    },
    "Plus-que-parfait": {
      "Je": "avais clos",
      "Tu": "avais clos",
      "Il/Elle/On": "avait clos",
      "Nous": "avions clos",
      "Vous": "aviez clos",
      "Ils/Elle": "avaient clos"
    },
    "Futur Simple": {
      "Je": "clorai",
      "Tu": "cloras",
      "Il/Elle/On": "clora",
      "Nous": "clorons",
      "Vous": "clorerez",
      "Ils/Elle": "cloront"
    },
    "Futur Antérieur": {
      "Je": "aurai clos",
      "Tu": "auras clos",
      "Il/Elle/On": "aura clos",
      "Nous": "aurons clos",
      "Vous": "aurez clos",
      "Ils/Elle": "auront clos"
    },
    "Conditionnel Présent": {
      "Je": "clorais",
      "Tu": "clorais",
      "Il/Elle/On": "clorait",
      "Nous": "clorions",
      "Vous": "cloriez",
      "Ils/Elle": "cloraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais clos",
      "Tu": "aurais clos",
      "Il/Elle/On": "aurait clos",
      "Nous": "aurions clos",
      "Vous": "auriez clos",
      "Ils/Elle": "auraient clos"
    },
    "Subjonctif Présent": {
      "Je": "close",
      "Tu": "closes",
      "Il/Elle/On": "close",
      "Nous": "closions",
      "Vous": "closiez",
      "Ils/Elle": "closent"
    },
    "Subjonctif Passé": {
      "Je": "aie clos",
      "Tu": "aies clos",
      "Il/Elle/On": "ait clos",
      "Nous": "ayons clos",
      "Vous": "ayez clos",
      "Ils/Elle": "aient clos"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse clos",
      "Tu": "eusses clos",
      "Il/Elle/On": "eût clos",
      "Nous": "eussions clos",
      "Vous": "eussiez clos",
      "Ils/Elle": "eussent clos"
    },
    "Subjonctif Imparfait": {
      "Je": "clorasse",
      "Tu": "clorasses",
      "Il/Elle/On": "clorât",
      "Nous": "clorassions",
      "Vous": "clorassiez",
      "Ils/Elle": "clorassent"
    },
    "Impératif Présent": {
      "Tu": "clos",
      "Nous": "clôturons",
      "Vous": "clôturez"
    },
    "Impératif Passé": {
      "Tu": "aie clos",
      "Nous": "ayons clos",
      "Vous": "ayez clos"
    },
    "Infinitif Présent": "clore",
    "Infinitif Passé": "avoir clos",
    "Participe Présent": "clorant",
    "Participe Passé": "clos",
    "Gérondif Présent": "en clorant",
    "Gérondif Passé": "en ayant clos"
  },
  
  "aborder": {
    "Présent": {
      "Je": "abord",
      "Tu": "abordes",
      "Il/Elle/On": "aborde",
      "Nous": "abordons",
      "Vous": "abordez",
      "Ils/Elle": "abordent"
    },
    "Imparfait": {
      "Je": "abordais",
      "Tu": "abordais",
      "Il/Elle/On": "abordait",
      "Nous": "abordions",
      "Vous": "abordiez",
      "Ils/Elle": "abordaient"
    },
    "Passé Composé": {
      "Je": "ai abordé",
      "Tu": "as abordé",
      "Il/Elle/On": "a abordé",
      "Nous": "avons abordé",
      "Vous": "avez abordé",
      "Ils/Elle": "ont abordé"
    },
    "Futur": {
      "Je": "aborderai",
      "Tu": "aborderas",
      "Il/Elle/On": "abordera",
      "Nous": "aborderons",
      "Vous": "aborderez",
      "Ils/Elle": "aborderont"
    },
    "Plus-que-parfait": {
      "Je": "avais abordé",
      "Tu": "avais abordé",
      "Il/Elle/On": "avait abordé",
      "Nous": "avions abordé",
      "Vous": "aviez abordé",
      "Ils/Elle": "avaient abordé"
    },
    "Futur Simple": {
      "Je": "aborderai",
      "Tu": "aborderas",
      "Il/Elle/On": "abordera",
      "Nous": "aborderons",
      "Vous": "aborderez",
      "Ils/Elle": "aborderont"
    },
    "Futur Antérieur": {
      "Je": "aurai abordé",
      "Tu": "auras abordé",
      "Il/Elle/On": "aura abordé",
      "Nous": "aurons abordé",
      "Vous": "aurez abordé",
      "Ils/Elle": "auront abordé"
    },
    "Conditionnel Présent": {
      "Je": "aborderais",
      "Tu": "aborderais",
      "Il/Elle/On": "aborderait",
      "Nous": "aborderions",
      "Vous": "aborderiez",
      "Ils/Elle": "aborderaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais abordé",
      "Tu": "aurais abordé",
      "Il/Elle/On": "aurait abordé",
      "Nous": "aurions abordé",
      "Vous": "auriez abordé",
      "Ils/Elle": "auraient abordé"
    },
    "Subjonctif Présent": {
      "Je": "aborde",
      "Tu": "abordes",
      "Il/Elle/On": "aborde",
      "Nous": "abordions",
      "Vous": "abordiez",
      "Ils/Elle": "abordent"
    },
    "Subjonctif Passé": {
      "Je": "aie abordé",
      "Tu": "aies abordé",
      "Il/Elle/On": "ait abordé",
      "Nous": "ayons abordé",
      "Vous": "ayez abordé",
      "Ils/Elle": "aient abordé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse abordé",
      "Tu": "eusses abordé",
      "Il/Elle/On": "eût abordé",
      "Nous": "eussions abordé",
      "Vous": "eussiez abordé",
      "Ils/Elle": "eussent abordé"
    },
    "Subjonctif Imparfait": {
      "Je": "abordasse",
      "Tu": "abordasses",
      "Il/Elle/On": "abordât",
      "Nous": "abordassions",
      "Vous": "abordassiez",
      "Ils/Elle": "abordassent"
    },
    "Impératif Présent": {
      "Tu": "aborde",
      "Nous": "abordons",
      "Vous": "abordez"
    },
    "Impératif Passé": {
      "Tu": "aie abordé",
      "Nous": "ayons abordé",
      "Vous": "ayez abordé"
    },
    "Infinitif Présent": "aborder",
    "Infinitif Passé": "avoir abordé",
    "Participe Présent": "abordant",
    "Participe Passé": "abordé",
    "Gérondif Présent": "en abordant",
    "Gérondif Passé": "en ayant abordé"
  },
"aboutir": {
    "Présent": {
      "Je": "aboutis",
      "Tu": "aboutis",
      "Il/Elle/On": "aboutit",
      "Nous": "aboutissons",
      "Vous": "aboutissez",
      "Ils/Elle": "aboutissent"
    },
    "Imparfait": {
      "Je": "aboutissais",
      "Tu": "aboutissais",
      "Il/Elle/On": "aboutissait",
      "Nous": "aboutissions",
      "Vous": "aboutissiez",
      "Ils/Elle": "aboutissaient"
    },
    "Passé Composé": {
      "Je": "ai abouti",
      "Tu": "as abouti",
      "Il/Elle/On": "a abouti",
      "Nous": "avons abouti",
      "Vous": "avez abouti",
      "Ils/Elle": "ont abouti"
    },
    "Futur": {
      "Je": "aboutirai",
      "Tu": "aboutiras",
      "Il/Elle/On": "aboutira",
      "Nous": "aboutirons",
      "Vous": "aboutirez",
      "Ils/Elle": "aboutiront"
    },
    "Plus-que-parfait": {
      "Je": "avais abouti",
      "Tu": "avais abouti",
      "Il/Elle/On": "avait abouti",
      "Nous": "avions abouti",
      "Vous": "aviez abouti",
      "Ils/Elle": "avaient abouti"
    },
    "Futur Simple": {
      "Je": "aboutirai",
      "Tu": "aboutiras",
      "Il/Elle/On": "aboutira",
      "Nous": "aboutirons",
      "Vous": "aboutirez",
      "Ils/Elle": "aboutiront"
    },
    "Futur Antérieur": {
      "Je": "aurai abouti",
      "Tu": "auras abouti",
      "Il/Elle/On": "aura abouti",
      "Nous": "aurons abouti",
      "Vous": "aurez abouti",
      "Ils/Elle": "auront abouti"
    },
    "Conditionnel Présent": {
      "Je": "aboutirais",
      "Tu": "aboutirais",
      "Il/Elle/On": "aboutirait",
      "Nous": "aboutirions",
      "Vous": "aboutiriez",
      "Ils/Elle": "aboutiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais abouti",
      "Tu": "aurais abouti",
      "Il/Elle/On": "aurait abouti",
      "Nous": "aurions abouti",
      "Vous": "auriez abouti",
      "Ils/Elle": "auraient abouti"
    },
    "Subjonctif Présent": {
      "Je": "aboutisse",
      "Tu": "aboutisses",
      "Il/Elle/On": "aboutisse",
      "Nous": "aboutissions",
      "Vous": "aboutissiez",
      "Ils/Elle": "aboutissent"
    },
    "Subjonctif Passé": {
      "Je": "aie abouti",
      "Tu": "aies abouti",
      "Il/Elle/On": "ait abouti",
      "Nous": "ayons abouti",
      "Vous": "ayez abouti",
      "Ils/Elle": "aient abouti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse abouti",
      "Tu": "eusses abouti",
      "Il/Elle/On": "eût abouti",
      "Nous": "eussions abouti",
      "Vous": "eussiez abouti",
      "Ils/Elle": "eussent abouti"
    },
    "Subjonctif Imparfait": {
      "Je": "aboutisse",
      "Tu": "aboutisses",
      "Il/Elle/On": "aboutît",
      "Nous": "aboutissions",
      "Vous": "aboutissiez",
      "Ils/Elle": "aboutissent"
    },
    "Impératif Présent": {
      "Tu": "aboutis",
      "Nous": "aboutissons",
      "Vous": "aboutissez"
    },
    "Impératif Passé": {
      "Tu": "aie abouti",
      "Nous": "ayons abouti",
      "Vous": "ayez abouti"
    },
    "Infinitif Présent": "aboutir",
    "Infinitif Passé": "avoir abouti",
    "Participe Présent": "aboutissant",
    "Participe Passé": "abouti",
    "Gérondif Présent": "en aboutissant",
    "Gérondif Passé": "en ayant abouti"
  },
  
  "accourir": {
    "Présent": {
      "Je": "accours",
      "Tu": "accours",
      "Il/Elle/On": "accourt",
      "Nous": "accourons",
      "Vous": "accourez",
      "Ils/Elle": "accourent"
    },
    "Imparfait": {
      "Je": "accourais",
      "Tu": "accourais",
      "Il/Elle/On": "accourait",
      "Nous": "accourions",
      "Vous": "accouriez",
      "Ils/Elle": "accouraient"
    },
    "Passé Composé": {
      "Je": "ai accouru",
      "Tu": "as accouru",
      "Il/Elle/On": "a accouru",
      "Nous": "avons accouru",
      "Vous": "avez accouru",
      "Ils/Elle": "ont accouru"
    },
    "Futur": {
      "Je": "accourrai",
      "Tu": "accourras",
      "Il/Elle/On": "accourra",
      "Nous": "accourrons",
      "Vous": "accourrez",
      "Ils/Elle": "accourront"
    },
    "Plus-que-parfait": {
      "Je": "avais accouru",
      "Tu": "avais accouru",
      "Il/Elle/On": "avait accouru",
      "Nous": "avions accouru",
      "Vous": "aviez accouru",
      "Ils/Elle": "avaient accouru"
    },
    "Futur Simple": {
      "Je": "accourrai",
      "Tu": "accourras",
      "Il/Elle/On": "accourra",
      "Nous": "accourrons",
      "Vous": "accourrez",
      "Ils/Elle": "accourront"
    },
    "Futur Antérieur": {
      "Je": "aurai accouru",
      "Tu": "auras accouru",
      "Il/Elle/On": "aura accouru",
      "Nous": "aurons accouru",
      "Vous": "aurez accouru",
      "Ils/Elle": "auront accouru"
    },
    "Conditionnel Présent": {
      "Je": "accourrais",
      "Tu": "accourrais",
      "Il/Elle/On": "accourrait",
      "Nous": "accourrions",
      "Vous": "accourriez",
      "Ils/Elle": "accourraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais accouru",
      "Tu": "aurais accouru",
      "Il/Elle/On": "aurait accouru",
      "Nous": "aurions accouru",
      "Vous": "auriez accouru",
      "Ils/Elle": "auraient accouru"
    },
    "Subjonctif Présent": {
      "Je": "accoure",
      "Tu": "accoures",
      "Il/Elle/On": "accoure",
      "Nous": "accourions",
      "Vous": "accouriez",
      "Ils/Elle": "accourent"
    },
    "Subjonctif Passé": {
      "Je": "aie accouru",
      "Tu": "aies accouru",
      "Il/Elle/On": "ait accouru",
      "Nous": "ayons accouru",
      "Vous": "ayez accouru",
      "Ils/Elle": "aient accouru"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse accouru",
      "Tu": "eusses accouru",
      "Il/Elle/On": "eût accouru",
      "Nous": "eussions accouru",
      "Vous": "eussiez accouru",
      "Ils/Elle": "eussent accouru"
    },
    "Subjonctif Imparfait": {
      "Je": "accourusse",
      "Tu": "accourusses",
      "Il/Elle/On": "accourût",
      "Nous": "accourussions",
      "Vous": "accourussiez",
      "Ils/Elle": "accourussent"
    },
    "Impératif Présent": {
      "Tu": "accours",
      "Nous": "accourons",
      "Vous": "accourez"
    },
    "Impératif Passé": {
      "Tu": "aie accouru",
      "Nous": "ayons accouru",
      "Vous": "ayez accouru"
    },
    "Infinitif Présent": "accourir",
    "Infinitif Passé": "avoir accouru",
    "Participe Présent": "accourant",
    "Participe Passé": "accouru",
    "Gérondif Présent": "en accourant",
    "Gérondif Passé": "en ayant accouru"
  },
  "accroître": {
    "Présent": {
      "Je": "accrois",
      "Tu": "accrois",
      "Il/Elle/On": "accroît",
      "Nous": "accroissons",
      "Vous": "accroissez",
      "Ils/Elle": "accroissent"
    },
    "Imparfait": {
      "Je": "accroissais",
      "Tu": "accroissais",
      "Il/Elle/On": "accroissait",
      "Nous": "accroissions",
      "Vous": "accroissiez",
      "Ils/Elle": "accroissaient"
    },
    "Passé Composé": {
      "Je": "ai accru",
      "Tu": "as accru",
      "Il/Elle/On": "a accru",
      "Nous": "avons accru",
      "Vous": "avez accru",
      "Ils/Elle": "ont accru"
    },
    "Futur": {
      "Je": "accroîtrai",
      "Tu": "accroîtras",
      "Il/Elle/On": "accroîtra",
      "Nous": "accroîtrons",
      "Vous": "accroîtrez",
      "Ils/Elle": "accroîtront"
    },
    "Plus-que-parfait": {
      "Je": "avais accru",
      "Tu": "avais accru",
      "Il/Elle/On": "avait accru",
      "Nous": "avions accru",
      "Vous": "aviez accru",
      "Ils/Elle": "avaient accru"
    },
    "Futur Simple": {
      "Je": "accroîtrai",
      "Tu": "accroîtras",
      "Il/Elle/On": "accroîtra",
      "Nous": "accroîtrons",
      "Vous": "accroîtrez",
      "Ils/Elle": "accroîtront"
    },
    "Futur Antérieur": {
      "Je": "aurai accru",
      "Tu": "auras accru",
      "Il/Elle/On": "aura accru",
      "Nous": "aurons accru",
      "Vous": "aurez accru",
      "Ils/Elle": "auront accru"
    },
    "Conditionnel Présent": {
      "Je": "accroîtrais",
      "Tu": "accroîtrais",
      "Il/Elle/On": "accroîtrait",
      "Nous": "accroîtrions",
      "Vous": "accroîtriez",
      "Ils/Elle": "accroîtraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais accru",
      "Tu": "aurais accru",
      "Il/Elle/On": "aurait accru",
      "Nous": "aurions accru",
      "Vous": "auriez accru",
      "Ils/Elle": "auraient accru"
    },
    "Subjonctif Présent": {
      "Je": "accroisse",
      "Tu": "accroisses",
      "Il/Elle/On": "accroisse",
      "Nous": "accroissions",
      "Vous": "accroissiez",
      "Ils/Elle": "accroissent"
    },
    "Subjonctif Passé": {
      "Je": "aie accru",
      "Tu": "aies accru",
      "Il/Elle/On": "ait accru",
      "Nous": "ayons accru",
      "Vous": "ayez accru",
      "Ils/Elle": "aient accru"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse accru",
      "Tu": "eusses accru",
      "Il/Elle/On": "eût accru",
      "Nous": "eussions accru",
      "Vous": "eussiez accru",
      "Ils/Elle": "eussent accru"
    },
    "Subjonctif Imparfait": {
      "Je": "accrûsse",
      "Tu": "accrûsses",
      "Il/Elle/On": "accrût",
      "Nous": "accrussions",
      "Vous": "accrussiez",
      "Ils/Elle": "accrussent"
    },
    "Impératif Présent": {
      "Tu": "accrois",
      "Nous": "accroissons",
      "Vous": "accroissez"
    },
    "Impératif Passé": {
      "Tu": "aie accru",
      "Nous": "ayons accru",
      "Vous": "ayez accru"
    },
    "Infinitif Présent": "accroître",
    "Infinitif Passé": "avoir accru",
    "Participe Présent": "accroissant",
    "Participe Passé": "accru",
    "Gérondif Présent": "en accroissant",
    "Gérondif Passé": "en ayant accru"
  },
  "alunir": {
    "Présent": {
      "Je": "alunis",
      "Tu": "alunis",
      "Il/Elle/On": "alunit",
      "Nous": "alunissons",
      "Vous": "alunissez",
      "Ils/Elle": "alunissent"
    },
    "Imparfait": {
      "Je": "alunissais",
      "Tu": "alunissais",
      "Il/Elle/On": "alunissait",
      "Nous": "alunissions",
      "Vous": "alunissiez",
      "Ils/Elle": "alunissaient"
    },
    "Passé Composé": {
      "Je": "ai aluni",
      "Tu": "as aluni",
      "Il/Elle/On": "a aluni",
      "Nous": "avons aluni",
      "Vous": "avez aluni",
      "Ils/Elle": "ont aluni"
    },
    "Futur": {
      "Je": "alunirai",
      "Tu": "aluniras",
      "Il/Elle/On": "alunira",
      "Nous": "alunirons",
      "Vous": "alunirez",
      "Ils/Elle": "aluniront"
    },
    "Plus-que-parfait": {
      "Je": "avais aluni",
      "Tu": "avais aluni",
      "Il/Elle/On": "avait aluni",
      "Nous": "avions aluni",
      "Vous": "aviez aluni",
      "Ils/Elle": "avaient aluni"
    },
    "Futur Simple": {
      "Je": "alunirai",
      "Tu": "aluniras",
      "Il/Elle/On": "alunira",
      "Nous": "alunirons",
      "Vous": "alunirez",
      "Ils/Elle": "aluniront"
    },
    "Futur Antérieur": {
      "Je": "aurai aluni",
      "Tu": "auras aluni",
      "Il/Elle/On": "aura aluni",
      "Nous": "aurons aluni",
      "Vous": "aurez aluni",
      "Ils/Elle": "auront aluni"
    },
    "Conditionnel Présent": {
      "Je": "alunirais",
      "Tu": "alunirais",
      "Il/Elle/On": "alunirait",
      "Nous": "alunirions",
      "Vous": "aluniriez",
      "Ils/Elle": "aluniraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais aluni",
      "Tu": "aurais aluni",
      "Il/Elle/On": "aurait aluni",
      "Nous": "aurions aluni",
      "Vous": "auriez aluni",
      "Ils/Elle": "auraient aluni"
    },
    "Subjonctif Présent": {
      "Je": "alunisse",
      "Tu": "alunisses",
      "Il/Elle/On": "alunisse",
      "Nous": "alunissions",
      "Vous": "alunissiez",
      "Ils/Elle": "alunissent"
    },
    "Subjonctif Passé": {
      "Je": "aie aluni",
      "Tu": "aies aluni",
      "Il/Elle/On": "ait aluni",
      "Nous": "ayons aluni",
      "Vous": "ayez aluni",
      "Ils/Elle": "aient aluni"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse aluni",
      "Tu": "eusses aluni",
      "Il/Elle/On": "eût aluni",
      "Nous": "eussions aluni",
      "Vous": "eussiez aluni",
      "Ils/Elle": "eussent aluni"
    },
    "Subjonctif Imparfait": {
      "Je": "alunisse",
      "Tu": "alunisses",
      "Il/Elle/On": "alunît",
      "Nous": "alunissions",
      "Vous": "alunissiez",
      "Ils/Elle": "alunissent"
    },
    "Impératif Présent": {
      "Tu": "alunis",
      "Nous": "alunissons",
      "Vous": "alunissez"
    },
    "Impératif Passé": {
      "Tu": "aie aluni",
      "Nous": "ayons aluni",
      "Vous": "ayez aluni"
    },
    "Infinitif Présent": "alunir",
    "Infinitif Passé": "avoir aluni",
    "Participe Présent": "alunissant",
    "Participe Passé": "aluni",
    "Gérondif Présent": "en alunissant",
    "Gérondif Passé": "en ayant aluni"
  },
  "amerrir": {
    "Présent": {
      "Je": "amerris",
      "Tu": "amerris",
      "Il/Elle/On": "amerrit",
      "Nous": "amerrissons",
      "Vous": "amerrissez",
      "Ils/Elle": "amerrissent"
    },
    "Imparfait": {
      "Je": "amerrissais",
      "Tu": "amerrissais",
      "Il/Elle/On": "amerrissait",
      "Nous": "amerrissions",
      "Vous": "amerrissiez",
      "Ils/Elle": "amerrissaient"
    },
    "Passé Composé": {
      "Je": "ai amerris",
      "Tu": "as amerris",
      "Il/Elle/On": "a amerris",
      "Nous": "avons amerris",
      "Vous": "avez amerris",
      "Ils/Elle": "ont amerris"
    },
    "Futur": {
      "Je": "amerrirai",
      "Tu": "amerriras",
      "Il/Elle/On": "amerrira",
      "Nous": "amerrirons",
      "Vous": "amerrirez",
      "Ils/Elle": "amerriront"
    },
    "Plus-que-parfait": {
      "Je": "avais amerris",
      "Tu": "avais amerris",
      "Il/Elle/On": "avait amerris",
      "Nous": "avions amerris",
      "Vous": "aviez amerris",
      "Ils/Elle": "avaient amerris"
    },
    "Futur Simple": {
      "Je": "amerrirai",
      "Tu": "amerriras",
      "Il/Elle/On": "amerrira",
      "Nous": "amerrirons",
      "Vous": "amerrirez",
      "Ils/Elle": "amerriront"
    },
    "Futur Antérieur": {
      "Je": "aurai amerris",
      "Tu": "auras amerris",
      "Il/Elle/On": "aura amerris",
      "Nous": "aurons amerris",
      "Vous": "aurez amerris",
      "Ils/Elle": "auront amerris"
    },
    "Conditionnel Présent": {
      "Je": "amerrirais",
      "Tu": "amerrirais",
      "Il/Elle/On": "amerrirait",
      "Nous": "amerririons",
      "Vous": "amerririez",
      "Ils/Elle": "amerriraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais amerris",
      "Tu": "aurais amerris",
      "Il/Elle/On": "aurait amerris",
      "Nous": "aurions amerris",
      "Vous": "auriez amerris",
      "Ils/Elle": "auraient amerris"
    },
    "Subjonctif Présent": {
      "Je": "amerrisse",
      "Tu": "amerrisses",
      "Il/Elle/On": "amerrisse",
      "Nous": "amerrissions",
      "Vous": "amerrissiez",
      "Ils/Elle": "amerrissent"
    },
    "Subjonctif Passé": {
      "Je": "aie amerris",
      "Tu": "aies amerris",
      "Il/Elle/On": "ait amerris",
      "Nous": "ayons amerris",
      "Vous": "ayez amerris",
      "Ils/Elle": "aient amerris"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse amerris",
      "Tu": "eusses amerris",
      "Il/Elle/On": "eût amerris",
      "Nous": "eussions amerris",
      "Vous": "eussiez amerris",
      "Ils/Elle": "eussent amerris"
    },
    "Subjonctif Imparfait": {
      "Je": "amerrisse",
      "Tu": "amerrisses",
      "Il/Elle/On": "amerrît",
      "Nous": "amerrissions",
      "Vous": "amerrissiez",
      "Ils/Elle": "amerrissent"
    },
    "Impératif Présent": {
      "Tu": "amerris",
      "Nous": "amerrissons",
      "Vous": "amerrissez"
    },
    "Impératif Passé": {
      "Tu": "aie amerris",
      "Nous": "ayons amerris",
      "Vous": "ayez amerris"
    },
    "Infinitif Présent": "amerrir",
    "Infinitif Passé": "avoir amerris",
    "Participe Présent": "amerrissant",
    "Participe Passé": "amerris",
    "Gérondif Présent": "en amerrissant",
    "Gérondif Passé": "en ayant amerris"
  },
   "apparaître": {
    "Présent": {
      "Je": "apparais",
      "Tu": "apparais",
      "Il/Elle/On": "apparaît",
      "Nous": "apparaissons",
      "Vous": "apparaissez",
      "Ils/Elle": "apparaissent"
    },
    "Imparfait": {
      "Je": "apparaissais",
      "Tu": "apparaissais",
      "Il/Elle/On": "apparaissait",
      "Nous": "apparaissions",
      "Vous": "apparaissiez",
      "Ils/Elle": "apparaissaient"
    },
    "Passé Composé": {
      "Je": "ai apparu",
      "Tu": "as apparu",
      "Il/Elle/On": "a apparu",
      "Nous": "avons apparu",
      "Vous": "avez apparu",
      "Ils/Elle": "ont apparu"
    },
    "Futur": {
      "Je": "apparaîtrai",
      "Tu": "apparaîtras",
      "Il/Elle/On": "apparaîtra",
      "Nous": "apparaîtrons",
      "Vous": "apparaîtrez",
      "Ils/Elle": "apparaîtront"
    },
    "Plus-que-parfait": {
      "Je": "avais apparu",
      "Tu": "avais apparu",
      "Il/Elle/On": "avait apparu",
      "Nous": "avions apparu",
      "Vous": "aviez apparu",
      "Ils/Elle": "avaient apparu"
    },
    "Futur Simple": {
      "Je": "apparaîtrai",
      "Tu": "apparaîtras",
      "Il/Elle/On": "apparaîtra",
      "Nous": "apparaîtrons",
      "Vous": "apparaîtrez",
      "Ils/Elle": "apparaîtront"
    },
    "Futur Antérieur": {
      "Je": "aurai apparu",
      "Tu": "auras apparu",
      "Il/Elle/On": "aura apparu",
      "Nous": "aurons apparu",
      "Vous": "aurez apparu",
      "Ils/Elle": "auront apparu"
    },
    "Conditionnel Présent": {
      "Je": "apparaîtrais",
      "Tu": "apparaîtrais",
      "Il/Elle/On": "apparaîtrait",
      "Nous": "apparaîtrions",
      "Vous": "apparaîtriez",
      "Ils/Elle": "apparaîtraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais apparu",
      "Tu": "aurais apparu",
      "Il/Elle/On": "aurait apparu",
      "Nous": "aurions apparu",
      "Vous": "auriez apparu",
      "Ils/Elle": "auraient apparu"
    },
    "Subjonctif Présent": {
      "Je": "apparaisse",
      "Tu": "apparaisses",
      "Il/Elle/On": "apparaisse",
      "Nous": "apparaissions",
      "Vous": "apparaissiez",
      "Ils/Elle": "apparaissent"
    },
    "Subjonctif Passé": {
      "Je": "aie apparu",
      "Tu": "aies apparu",
      "Il/Elle/On": "ait apparu",
      "Nous": "ayons apparu",
      "Vous": "ayez apparu",
      "Ils/Elle": "aient apparu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse apparu",
      "Tu": "eusses apparu",
      "Il/Elle/On": "eût apparu",
      "Nous": "eussions apparu",
      "Vous": "eussiez apparu",
      "Ils/Elle": "eussent apparu"
    },
    "Subjonctif Imparfait": {
      "Je": "apparusse",
      "Tu": "apparusses",
      "Il/Elle/On": "apparût",
      "Nous": "apparussions",
      "Vous": "apparussiez",
      "Ils/Elle": "apparussent"
    },
    "Impératif Présent": {
      "Tu": "apparais",
      "Nous": "apparaissons",
      "Vous": "apparaissez"
    },
    "Impératif Passé": {
      "Tu": "aie apparu",
      "Nous": "ayons apparu",
      "Vous": "ayez apparu"
    },
    "Infinitif Présent": "apparaître",
    "Infinitif Passé": "avoir apparu",
    "Participe Présent": "apparaissant",
    "Participe Passé": "apparu",
    "Gérondif Présent": "en apparaissant",
    "Gérondif Passé": "en ayant apparu"
  },
"atterrir": {
  "Présent": {
    "Je": "atterris",
    "Tu": "atterris",
    "Il/Elle/On": "atterrit",
    "Nous": "atterrissons",
    "Vous": "atterrissez",
    "Ils/Elle": "atterrissent"
  },
  "Imparfait": {
    "Je": "atterrissais",
    "Tu": "atterrissais",
    "Il/Elle/On": "atterrissait",
    "Nous": "atterrissions",
    "Vous": "atterrissiez",
    "Ils/Elle": "atterrissaient"
  },
  "Passé Composé": {
    "Je": "ai atterri",
    "Tu": "as atterri",
    "Il/Elle/On": "a atterri",
    "Nous": "avons atterri",
    "Vous": "avez atterri",
    "Ils/Elle": "ont atterri"
  },
  "Futur": {
    "Je": "atterrirai",
    "Tu": "atterriras",
    "Il/Elle/On": "atterrira",
    "Nous": "atterrirons",
    "Vous": "atterrirez",
    "Ils/Elle": "atterriront"
  },
  "Plus-que-parfait": {
    "Je": "avais atterri",
    "Tu": "avais atterri",
    "Il/Elle/On": "avait atterri",
    "Nous": "avions atterri",
    "Vous": "aviez atterri",
    "Ils/Elle": "avaient atterri"
  },
  "Futur Simple": {
    "Je": "atterrirai",
    "Tu": "atterriras",
    "Il/Elle/On": "atterrira",
    "Nous": "atterrirons",
    "Vous": "atterrirez",
    "Ils/Elle": "atterriront"
  },
  "Futur Antérieur": {
    "Je": "aurai atterri",
    "Tu": "auras atterri",
    "Il/Elle/On": "aura atterri",
    "Nous": "aurons atterri",
    "Vous": "aurez atterri",
    "Ils/Elle": "auront atterri"
  },
  "Conditionnel Présent": {
    "Je": "atterrirais",
    "Tu": "atterrirais",
    "Il/Elle/On": "atterrirait",
    "Nous": "atterririons",
    "Vous": "atterririez",
    "Ils/Elle": "atterriraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais atterri",
    "Tu": "aurais atterri",
    "Il/Elle/On": "aurait atterri",
    "Nous": "aurions atterri",
    "Vous": "auriez atterri",
    "Ils/Elle": "auraient atterri"
  },
  "Subjonctif Présent": {
    "Je": "atterrisse",
    "Tu": "atterrisses",
    "Il/Elle/On": "atterrisse",
    "Nous": "atterrissions",
    "Vous": "atterrissiez",
    "Ils/Elle": "atterrissent"
  },
  "Subjonctif Passé": {
    "Je": "aie atterri",
    "Tu": "aies atterri",
    "Il/Elle/On": "ait atterri",
    "Nous": "ayons atterri",
    "Vous": "ayez atterri",
    "Ils/Elle": "aient atterri"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse atterri",
    "Tu": "eusses atterri",
    "Il/Elle/On": "eût atterri",
    "Nous": "eussions atterri",
    "Vous": "eussiez atterri",
    "Ils/Elle": "eussent atterri"
  },
  "Subjonctif Imparfait": {
    "Je": "atterrisse",
    "Tu": "atterrisses",
    "Il/Elle/On": "atterrît",
    "Nous": "atterrissions",
    "Vous": "atterrissiez",
    "Ils/Elle": "atterrissent"
  },
  "Impératif Présent": {
    "Tu": "atterris",
    "Nous": "atterrissons",
    "Vous": "atterrissez"
  },
  "Impératif Passé": {
    "Tu": "aie atterri",
    "Nous": "ayons atterri",
    "Vous": "ayez atterri"
  },
  "Infinitif Présent": "atterrir",
  "Infinitif Passé": "avoir atterri",
  "Participe Présent": "atterrissant",
  "Participe Passé": "atterri",
  "Gérondif Présent": "en atterrissant",
  "Gérondif Passé": "en ayant atterri"
},
"augmenter": {
  "Présent": {
    "Je": "augmente",
    "Tu": "augmentes",
    "Il/Elle/On": "augmente",
    "Nous": "augmentons",
    "Vous": "augmentez",
    "Ils/Elle": "augmentent"
  },
  "Imparfait": {
    "Je": "augmentais",
    "Tu": "augmentais",
    "Il/Elle/On": "augmentait",
    "Nous": "augmentions",
    "Vous": "augmentiez",
    "Ils/Elle": "augmentaient"
  },
  "Passé Composé": {
    "Je": "ai augmenté",
    "Tu": "as augmenté",
    "Il/Elle/On": "a augmenté",
    "Nous": "avons augmenté",
    "Vous": "avez augmenté",
    "Ils/Elle": "ont augmenté"
  },
  "Futur": {
    "Je": "augmenterai",
    "Tu": "augmenteras",
    "Il/Elle/On": "augmentera",
    "Nous": "augmenterons",
    "Vous": "augmenterez",
    "Ils/Elle": "augmenteront"
  },
  "Plus-que-parfait": {
    "Je": "avais augmenté",
    "Tu": "avais augmenté",
    "Il/Elle/On": "avait augmenté",
    "Nous": "avions augmenté",
    "Vous": "aviez augmenté",
    "Ils/Elle": "avaient augmenté"
  },
  "Futur Simple": {
    "Je": "augmenterai",
    "Tu": "augmenteras",
    "Il/Elle/On": "augmentera",
    "Nous": "augmenterons",
    "Vous": "augmenterez",
    "Ils/Elle": "augmenteront"
  },
  "Futur Antérieur": {
    "Je": "aurai augmenté",
    "Tu": "auras augmenté",
    "Il/Elle/On": "aura augmenté",
    "Nous": "aurons augmenté",
    "Vous": "aurez augmenté",
    "Ils/Elle": "auront augmenté"
  },
  "Conditionnel Présent": {
    "Je": "augmenterais",
    "Tu": "augmenterais",
    "Il/Elle/On": "augmenterait",
    "Nous": "augmenterions",
    "Vous": "augmenteriez",
    "Ils/Elle": "augmenteraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais augmenté",
    "Tu": "aurais augmenté",
    "Il/Elle/On": "aurait augmenté",
    "Nous": "aurions augmenté",
    "Vous": "auriez augmenté",
    "Ils/Elle": "auraient augmenté"
  },
  "Subjonctif Présent": {
    "Je": "augmente",
    "Tu": "augmentes",
    "Il/Elle/On": "augmente",
    "Nous": "augmentions",
    "Vous": "augmentiez",
    "Ils/Elle": "augmentent"
  },
  "Subjonctif Passé": {
    "Je": "aie augmenté",
    "Tu": "aies augmenté",
    "Il/Elle/On": "ait augmenté",
    "Nous": "ayons augmenté",
    "Vous": "ayez augmenté",
    "Ils/Elle": "aient augmenté"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse augmenté",
    "Tu": "eusses augmenté",
    "Il/Elle/On": "eût augmenté",
    "Nous": "eussions augmenté",
    "Vous": "eussiez augmenté",
    "Ils/Elle": "eussent augmenté"
  },
  "Subjonctif Imparfait": {
    "Je": "augmentasse",
    "Tu": "augmentasses",
    "Il/Elle/On": "augmentât",
    "Nous": "augmentassions",
    "Vous": "augmentassiez",
    "Ils/Elle": "augmentassent"
  },
  "Impératif Présent": {
    "Tu": "augmente",
    "Nous": "augmentons",
    "Vous": "augmentez"
  },
  "Impératif Passé": {
    "Tu": "aie augmenté",
    "Nous": "ayons augmenté",
    "Vous": "ayez augmenté"
  },
  "Infinitif Présent": "augmenter",
  "Infinitif Passé": "avoir augmenté",
  "Participe Présent": "augmentant",
  "Participe Passé": "augmenté",
  "Gérondif Présent": "en augmentant",
  "Gérondif Passé": "en ayant augmenté"
},
"avorter": {
  "Présent": {
    "Je": "avorte",
    "Tu": "avortes",
    "Il/Elle/On": "avorte",
    "Nous": "avortons",
    "Vous": "avortez",
    "Ils/Elle": "avortent"
  },
  "Imparfait": {
    "Je": "avortais",
    "Tu": "avortais",
    "Il/Elle/On": "avortait",
    "Nous": "avortions",
    "Vous": "avortiez",
    "Ils/Elle": "avortaient"
  },
  "Passé Composé": {
    "Je": "ai avorté",
    "Tu": "as avorté",
    "Il/Elle/On": "a avorté",
    "Nous": "avons avorté",
    "Vous": "avez avorté",
    "Ils/Elle": "ont avorté"
  },
  "Futur": {
    "Je": "avorterai",
    "Tu": "avorteras",
    "Il/Elle/On": "avortera",
    "Nous": "avorterons",
    "Vous": "avorterez",
    "Ils/Elle": "avorteront"
  },
  "Plus-que-parfait": {
    "Je": "avais avorté",
    "Tu": "avais avorté",
    "Il/Elle/On": "avait avorté",
    "Nous": "avions avorté",
    "Vous": "aviez avorté",
    "Ils/Elle": "avaient avorté"
  },
  "Futur Simple": {
    "Je": "avorterai",
    "Tu": "avorteras",
    "Il/Elle/On": "avortera",
    "Nous": "avorterons",
    "Vous": "avorterez",
    "Ils/Elle": "avorteront"
  },
  "Futur Antérieur": {
    "Je": "aurai avorté",
    "Tu": "auras avorté",
    "Il/Elle/On": "aura avorté",
    "Nous": "aurons avorté",
    "Vous": "aurez avorté",
    "Ils/Elle": "auront avorté"
  },
  "Conditionnel Présent": {
    "Je": "avorterais",
    "Tu": "avorterais",
    "Il/Elle/On": "avorterait",
    "Nous": "avorterions",
    "Vous": "avorteriez",
    "Ils/Elle": "avorteraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais avorté",
    "Tu": "aurais avorté",
    "Il/Elle/On": "aurait avorté",
    "Nous": "aurions avorté",
    "Vous": "auriez avorté",
    "Ils/Elle": "auraient avorté"
  },
  "Subjonctif Présent": {
    "Je": "avorte",
    "Tu": "avortes",
    "Il/Elle/On": "avorte",
    "Nous": "avortions",
    "Vous": "avortiez",
    "Ils/Elle": "avortent"
  },
  "Subjonctif Passé": {
    "Je": "aie avorté",
    "Tu": "aies avorté",
    "Il/Elle/On": "ait avorté",
    "Nous": "ayons avorté",
    "Vous": "ayez avorté",
    "Ils/Elle": "aient avorté"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse avorté",
    "Tu": "eusses avorté",
    "Il/Elle/On": "eût avorté",
    "Nous": "eussions avorté",
    "Vous": "eussiez avorté",
    "Ils/Elle": "eussent avorté"
  },
  "Subjonctif Imparfait": {
    "Je": "avortasse",
    "Tu": "avortasses",
    "Il/Elle/On": "avortât",
    "Nous": "avortassions",
    "Vous": "avortassiez",
    "Ils/Elle": "avortassent"
  },
  "Impératif Présent": {
    "Tu": "avorte",
    "Nous": "avortons",
    "Vous": "avortez"
  },
  "Impératif Passé": {
    "Tu": "aie avorté",
    "Nous": "ayons avorté",
    "Vous": "ayez avorté"
  },
  "Infinitif Présent": "avorter",
  "Infinitif Passé": "avoir avorté",
  "Participe Présent": "avortant",
  "Participe Passé": "avorté",
  "Gérondif Présent": "en avortant",
  "Gérondif Passé": "en ayant avorté"
},
"baisser": {
  "Présent": {
    "Je": "baisse",
    "Tu": "baisses",
    "Il/Elle/On": "baisse",
    "Nous": "baissons",
    "Vous": "baissez",
    "Ils/Elle": "baissent"
  },
  "Imparfait": {
    "Je": "baisais",
    "Tu": "baisais",
    "Il/Elle/On": "baisait",
    "Nous": "baissions",
    "Vous": "baissez",
    "Ils/Elle": "baisaient"
  },
  "Passé Composé": {
    "Je": "ai baissé",
    "Tu": "as baissé",
    "Il/Elle/On": "a baissé",
    "Nous": "avons baissé",
    "Vous": "avez baissé",
    "Ils/Elle": "ont baissé"
  },
  "Futur": {
    "Je": "baisserai",
    "Tu": "baisseras",
    "Il/Elle/On": "baissera",
    "Nous": "baisserons",
    "Vous": "baissez",
    "Ils/Elle": "baisseront"
  },
  "Plus-que-parfait": {
    "Je": "avais baissé",
    "Tu": "avais baissé",
    "Il/Elle/On": "avait baissé",
    "Nous": "avions baissé",
    "Vous": "aviez baissé",
    "Ils/Elle": "avaient baissé"
  },
  "Futur Simple": {
    "Je": "baisserai",
    "Tu": "baisseras",
    "Il/Elle/On": "baissera",
    "Nous": "baisserons",
    "Vous": "baissez",
    "Ils/Elle": "baisseront"
  },
  "Futur Antérieur": {
    "Je": "aurai baissé",
    "Tu": "auras baissé",
    "Il/Elle/On": "aura baissé",
    "Nous": "aurons baissé",
    "Vous": "aurez baissé",
    "Ils/Elle": "auront baissé"
  },
  "Conditionnel Présent": {
    "Je": "baisserais",
    "Tu": "baisserais",
    "Il/Elle/On": "baisserait",
    "Nous": "baisserions",
    "Vous": "baisseriez",
    "Ils/Elle": "baisseraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais baissé",
    "Tu": "aurais baissé",
    "Il/Elle/On": "aurait baissé",
    "Nous": "aurions baissé",
    "Vous": "auriez baissé",
    "Ils/Elle": "auraient baissé"
  },
  "Subjonctif Présent": {
    "Je": "baisse",
    "Tu": "baisses",
    "Il/Elle/On": "baisse",
    "Nous": "baissions",
    "Vous": "baissez",
    "Ils/Elle": "baissent"
  },
  "Subjonctif Passé": {
    "Je": "aie baissé",
    "Tu": "aies baissé",
    "Il/Elle/On": "ait baissé",
    "Nous": "ayons baissé",
    "Vous": "ayez baissé",
    "Ils/Elle": "aient baissé"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse baissé",
    "Tu": "eusses baissé",
    "Il/Elle/On": "eût baissé",
    "Nous": "eussions baissé",
    "Vous": "eussiez baissé",
    "Ils/Elle": "eussent baissé"
  },
  "Subjonctif Imparfait": {
    "Je": "baissasse",
    "Tu": "baissasses",
    "Il/Elle/On": "baissât",
    "Nous": "baissassions",
    "Vous": "baissassiez",
    "Ils/Elle": "baissassent"
  },
  "Impératif Présent": {
    "Tu": "baisse",
    "Nous": "baissons",
    "Vous": "baissez"
  },
  "Impératif Passé": {
    "Tu": "aie baissé",
    "Nous": "ayons baissé",
    "Vous": "ayez baissé"
  },
  "Infinitif Présent": "baisser",
  "Infinitif Passé": "avoir baissé",
  "Participe Présent": "baissant",
  "Participe Passé": "baissé",
  "Gérondif Présent": "en baissant",
  "Gérondif Passé": "en ayant baissé"
},
"changer": {
  "Présent": {
    "Je": "change",
    "Tu": "changes",
    "Il/Elle/On": "change",
    "Nous": "changeons",
    "Vous": "changez",
    "Ils/Elle": "changent"
  },
  "Imparfait": {
    "Je": "changeais",
    "Tu": "changeais",
    "Il/Elle/On": "changeait",
    "Nous": "changions",
    "Vous": "changiez",
    "Ils/Elle": "changeaient"
  },
  "Passé Composé": {
    "Je": "ai changé",
    "Tu": "as changé",
    "Il/Elle/On": "a changé",
    "Nous": "avons changé",
    "Vous": "avez changé",
    "Ils/Elle": "ont changé"
  },
  "Futur": {
    "Je": "changerai",
    "Tu": "changeras",
    "Il/Elle/On": "changera",
    "Nous": "changerons",
    "Vous": "changerez",
    "Ils/Elle": "changeront"
  },
  "Plus-que-parfait": {
    "Je": "avais changé",
    "Tu": "avais changé",
    "Il/Elle/On": "avait changé",
    "Nous": "avions changé",
    "Vous": "aviez changé",
    "Ils/Elle": "avaient changé"
  },
  "Futur Simple": {
    "Je": "changerai",
    "Tu": "changeras",
    "Il/Elle/On": "changera",
    "Nous": "changerons",
    "Vous": "changerez",
    "Ils/Elle": "changeront"
  },
  "Futur Antérieur": {
    "Je": "aurai changé",
    "Tu": "auras changé",
    "Il/Elle/On": "aura changé",
    "Nous": "aurons changé",
    "Vous": "aurez changé",
    "Ils/Elle": "auront changé"
  },
  "Conditionnel Présent": {
    "Je": "changerais",
    "Tu": "changerais",
    "Il/Elle/On": "changerait",
    "Nous": "changerions",
    "Vous": "changeriez",
    "Ils/Elle": "changeraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais changé",
    "Tu": "aurais changé",
    "Il/Elle/On": "aurait changé",
    "Nous": "aurions changé",
    "Vous": "auriez changé",
    "Ils/Elle": "auraient changé"
  },
  "Subjonctif Présent": {
    "Je": "change",
    "Tu": "changes",
    "Il/Elle/On": "change",
    "Nous": "changions",
    "Vous": "changiez",
    "Ils/Elle": "changent"
  },
  "Subjonctif Passé": {
    "Je": "aie changé",
    "Tu": "aies changé",
    "Il/Elle/On": "ait changé",
    "Nous": "ayons changé",
    "Vous": "ayez changé",
    "Ils/Elle": "aient changé"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse changé",
    "Tu": "eusses changé",
    "Il/Elle/On": "eût changé",
    "Nous": "eussions changé",
    "Vous": "eussiez changé",
    "Ils/Elle": "eussent changé"
  },
  "Subjonctif Imparfait": {
    "Je": "changeasse",
    "Tu": "changeasses",
    "Il/Elle/On": "changeât",
    "Nous": "changeassions",
    "Vous": "changeassiez",
    "Ils/Elle": "changeassent"
  },
  "Impératif Présent": {
    "Tu": "change",
    "Nous": "changeons",
    "Vous": "changez"
  },
  "Impératif Passé": {
    "Tu": "aie changé",
    "Nous": "ayons changé",
    "Vous": "ayez changé"
  },
  "Infinitif Présent": "changer",
  "Infinitif Passé": "avoir changé",
  "Participe Présent": "changeant",
  "Participe Passé": "changé",
  "Gérondif Présent": "en changeant",
  "Gérondif Passé": "en ayant changé"
},
"commencer": {
  "Présent": {
    "Je": "commence",
    "Tu": "commences",
    "Il/Elle/On": "commence",
    "Nous": "commençons",
    "Vous": "commencez",
    "Ils/Elle": "commencent"
  },
  "Imparfait": {
    "Je": "commençais",
    "Tu": "commençais",
    "Il/Elle/On": "commençait",
    "Nous": "commencions",
    "Vous": "commenciez",
    "Ils/Elle": "commençaient"
  },
  "Passé Composé": {
    "Je": "ai commencé",
    "Tu": "as commencé",
    "Il/Elle/On": "a commencé",
    "Nous": "avons commencé",
    "Vous": "avez commencé",
    "Ils/Elle": "ont commencé"
  },
  "Futur": {
    "Je": "commencerai",
    "Tu": "commenceras",
    "Il/Elle/On": "commencera",
    "Nous": "commencerons",
    "Vous": "commencerez",
    "Ils/Elle": "commenceront"
  },
  "Plus-que-parfait": {
    "Je": "avais commencé",
    "Tu": "avais commencé",
    "Il/Elle/On": "avait commencé",
    "Nous": "avions commencé",
    "Vous": "aviez commencé",
    "Ils/Elle": "avaient commencé"
  },
  "Futur Simple": {
    "Je": "commencerai",
    "Tu": "commenceras",
    "Il/Elle/On": "commencera",
    "Nous": "commencerons",
    "Vous": "commencerez",
    "Ils/Elle": "commenceront"
  },
  "Futur Antérieur": {
    "Je": "aurai commencé",
    "Tu": "auras commencé",
    "Il/Elle/On": "aura commencé",
    "Nous": "aurons commencé",
    "Vous": "aurez commencé",
    "Ils/Elle": "auront commencé"
  },
  "Conditionnel Présent": {
    "Je": "commencerais",
    "Tu": "commencerais",
    "Il/Elle/On": "commencerait",
    "Nous": "commencerions",
    "Vous": "commenceriez",
    "Ils/Elle": "commenceraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais commencé",
    "Tu": "aurais commencé",
    "Il/Elle/On": "aurait commencé",
    "Nous": "aurions commencé",
    "Vous": "auriez commencé",
    "Ils/Elle": "auraient commencé"
  },
  "Subjonctif Présent": {
    "Je": "commence",
    "Tu": "commences",
    "Il/Elle/On": "commence",
    "Nous": "commencions",
    "Vous": "commenciez",
    "Ils/Elle": "commencent"
  },
  "Subjonctif Passé": {
    "Je": "aie commencé",
    "Tu": "aies commencé",
    "Il/Elle/On": "ait commencé",
    "Nous": "ayons commencé",
    "Vous": "ayez commencé",
    "Ils/Elle": "aient commencé"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse commencé",
    "Tu": "eusses commencé",
    "Il/Elle/On": "eût commencé",
    "Nous": "eussions commencé",
    "Vous": "eussiez commencé",
    "Ils/Elle": "eussent commencé"
  },
  "Subjonctif Imparfait": {
    "Je": "commençasse",
    "Tu": "commençasses",
    "Il/Elle/On": "commençât",
    "Nous": "commençassions",
    "Vous": "commençassiez",
    "Ils/Elle": "commençassent"
  },
  "Impératif Présent": {
    "Tu": "commence",
    "Nous": "commençons",
    "Vous": "commencez"
  },
  "Impératif Passé": {
    "Tu": "aie commencé",
    "Nous": "ayons commencé",
    "Vous": "ayez commencé"
  },
  "Infinitif Présent": "commencer",
  "Infinitif Passé": "avoir commencé",
  "Participe Présent": "commençant",
  "Participe Passé": "commencé",
  "Gérondif Présent": "en commençant",
  "Gérondif Passé": "en ayant commencé"
},
"crever": {
  "Présent": {
    "Je": "crève",
    "Tu": "crèves",
    "Il/Elle/On": "crève",
    "Nous": "crevons",
    "Vous": "crevez",
    "Ils/Elle": "crèvent"
  },
  "Imparfait": {
    "Je": "crevais",
    "Tu": "crevais",
    "Il/Elle/On": "crevait",
    "Nous": "crevions",
    "Vous": "creviez",
    "Ils/Elle": "crevaient"
  },
  "Passé Composé": {
    "Je": "ai crevé",
    "Tu": "as crevé",
    "Il/Elle/On": "a crevé",
    "Nous": "avons crevé",
    "Vous": "avez crevé",
    "Ils/Elle": "ont crevé"
  },
  "Futur": {
    "Je": "crèverai",
    "Tu": "crèveras",
    "Il/Elle/On": "crèvera",
    "Nous": "crèverons",
    "Vous": "crèverez",
    "Ils/Elle": "crèveront"
  },
  "Plus-que-parfait": {
    "Je": "avais crevé",
    "Tu": "avais crevé",
    "Il/Elle/On": "avait crevé",
    "Nous": "avions crevé",
    "Vous": "aviez crevé",
    "Ils/Elle": "avaient crevé"
  },
  "Futur Simple": {
    "Je": "crèverai",
    "Tu": "crèveras",
    "Il/Elle/On": "crèvera",
    "Nous": "crèverons",
    "Vous": "crèverez",
    "Ils/Elle": "crèveront"
  },
  "Futur Antérieur": {
    "Je": "aurai crevé",
    "Tu": "auras crevé",
    "Il/Elle/On": "aura crevé",
    "Nous": "aurons crevé",
    "Vous": "aurez crevé",
    "Ils/Elle": "auront crevé"
  },
  "Conditionnel Présent": {
    "Je": "crèverais",
    "Tu": "crèverais",
    "Il/Elle/On": "crèverait",
    "Nous": "crèverions",
    "Vous": "crèveriez",
    "Ils/Elle": "crèveraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais crevé",
    "Tu": "aurais crevé",
    "Il/Elle/On": "aurait crevé",
    "Nous": "aurions crevé",
    "Vous": "auriez crevé",
    "Ils/Elle": "auraient crevé"
  },
  "Subjonctif Présent": {
    "Je": "crève",
    "Tu": "crèves",
    "Il/Elle/On": "crève",
    "Nous": "crevions",
    "Vous": "creviez",
    "Ils/Elle": "crèvent"
  },
  "Subjonctif Passé": {
    "Je": "aie crevé",
    "Tu": "aies crevé",
    "Il/Elle/On": "ait crevé",
    "Nous": "ayons crevé",
    "Vous": "ayez crevé",
    "Ils/Elle": "aient crevé"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse crevé",
    "Tu": "eusses crevé",
    "Il/Elle/On": "eût crevé",
    "Nous": "eussions crevé",
    "Vous": "eussiez crevé",
    "Ils/Elle": "eussent crevé"
  },
  "Subjonctif Imparfait": {
    "Je": "crèvasse",
    "Tu": "crèvasses",
    "Il/Elle/On": "crèvât",
    "Nous": "crèvassions",
    "Vous": "crèvassiez",
    "Ils/Elle": "crèvassent"
  },
  "Impératif Présent": {
    "Tu": "crève",
    "Nous": "crevons",
    "Vous": "crevez"
  },
  "Impératif Passé": {
    "Tu": "aie crevé",
    "Nous": "ayons crevé",
    "Vous": "ayez crevé"
  },
  "Infinitif Présent": "crever",
  "Infinitif Passé": "avoir crevé",
  "Participe Présent": "crevant",
  "Participe Passé": "crevé",
  "Gérondif Présent": "en crevant",
  "Gérondif Passé": "en ayant crevé"
},
"croitre": {
  "Présent": {
    "Je": "crois",
    "Tu": "crois",
    "Il/Elle/On": "croît",
    "Nous": "croissons",
    "Vous": "croissez",
    "Ils/Elle": "croissent"
  },
  "Imparfait": {
    "Je": "croissais",
    "Tu": "croissais",
    "Il/Elle/On": "croissait",
    "Nous": "croissions",
    "Vous": "croissiez",
    "Ils/Elle": "croissaient"
  },
  "Passé Composé": {
    "Je": "ai crû",
    "Tu": "as crû",
    "Il/Elle/On": "a crû",
    "Nous": "avons crû",
    "Vous": "avez crû",
    "Ils/Elle": "ont crû"
  },
  "Futur": {
    "Je": "croîtrai",
    "Tu": "croîtras",
    "Il/Elle/On": "croîtra",
    "Nous": "croîtrons",
    "Vous": "croîtrez",
    "Ils/Elle": "croîtront"
  },
  "Plus-que-parfait": {
    "Je": "avais crû",
    "Tu": "avais crû",
    "Il/Elle/On": "avait crû",
    "Nous": "avions crû",
    "Vous": "aviez crû",
    "Ils/Elle": "avaient crû"
  },
  "Futur Simple": {
    "Je": "croîtrai",
    "Tu": "croîtras",
    "Il/Elle/On": "croîtra",
    "Nous": "croîtrons",
    "Vous": "croîtrez",
    "Ils/Elle": "croîtront"
  },
  "Futur Antérieur": {
    "Je": "aurai crû",
    "Tu": "auras crû",
    "Il/Elle/On": "aura crû",
    "Nous": "aurons crû",
    "Vous": "aurez crû",
    "Ils/Elle": "auront crû"
  },
  "Conditionnel Présent": {
    "Je": "croîtrais",
    "Tu": "croîtrais",
    "Il/Elle/On": "croîtrait",
    "Nous": "croîtrions",
    "Vous": "croîtriez",
    "Ils/Elle": "croîtraient"
  },
  "Conditionnel Passé": {
    "Je": "aurais crû",
    "Tu": "aurais crû",
    "Il/Elle/On": "aurait crû",
    "Nous": "aurions crû",
    "Vous": "auriez crû",
    "Ils/Elle": "auraient crû"
  },
  "Subjonctif Présent": {
    "Je": "croisse",
    "Tu": "croisses",
    "Il/Elle/On": "croisse",
    "Nous": "croissions",
    "Vous": "croissiez",
    "Ils/Elle": "croissent"
  },
  "Subjonctif Passé": {
    "Je": "aie crû",
    "Tu": "aies crû",
    "Il/Elle/On": "ait crû",
    "Nous": "ayons crû",
    "Vous": "ayez crû",
    "Ils/Elle": "aient crû"
  },
  "Subjonctif Plus-que-parfait": {
    "Je": "eusse crû",
    "Tu": "eusses crû",
    "Il/Elle/On": "eût crû",
    "Nous": "eussions crû",
    "Vous": "eussiez crû",
    "Ils/Elle": "eussent crû"
  },
  "Subjonctif Imparfait": {
    "Je": "crûsse",
    "Tu": "crûsses",
    "Il/Elle/On": "crût",
    "Nous": "crussions",
    "Vous": "crussiez",
    "Ils/Elle": "crussent"
  },
  "Impératif Présent": {
    "Tu": "crois",
    "Nous": "croissons",
    "Vous": "croissez"
  },
  "Impératif Passé": {
    "Tu": "aie crû",
    "Nous": "ayons crû",
    "Vous": "ayez crû"
  },
  "Infinitif Présent": "croître",
  "Infinitif Passé": "avoir crû",
  "Participe Présent": "croissant",
  "Participe Passé": "crû",
  "Gérondif Présent": "en croissant",
  "Gérondif Passé": "en ayant crû"
},
"déborder": {
    "Présent": {
      "Je": "déborde",
      "Tu": "débordes",
      "Il/Elle/On": "déborde",
      "Nous": "débordons",
      "Vous": "débordez",
      "Ils/Elle": "débordent"
    },
    "Imparfait": {
      "Je": "débordais",
      "Tu": "débordais",
      "Il/Elle/On": "débordait",
      "Nous": "débordions",
      "Vous": "débordiez",
      "Ils/Elle": "débordaient"
    },
    "Passé Composé": {
      "Je": "ai débordé",
      "Tu": "as débordé",
      "Il/Elle/On": "a débordé",
      "Nous": "avons débordé",
      "Vous": "avez débordé",
      "Ils/Elle": "ont débordé"
    },
    "Futur": {
      "Je": "déborderai",
      "Tu": "déborderas",
      "Il/Elle/On": "débordera",
      "Nous": "déborderons",
      "Vous": "déborderez",
      "Ils/Elle": "déborderont"
    },
    "Plus-que-parfait": {
      "Je": "avais débordé",
      "Tu": "avais débordé",
      "Il/Elle/On": "avait débordé",
      "Nous": "avions débordé",
      "Vous": "aviez débordé",
      "Ils/Elle": "avaient débordé"
    },
    "Futur Simple": {
      "Je": "déborderai",
      "Tu": "déborderas",
      "Il/Elle/On": "débordera",
      "Nous": "déborderons",
      "Vous": "déborderez",
      "Ils/Elle": "déborderont"
    },
    "Futur Antérieur": {
      "Je": "aurai débordé",
      "Tu": "auras débordé",
      "Il/Elle/On": "aura débordé",
      "Nous": "aurons débordé",
      "Vous": "aurez débordé",
      "Ils/Elle": "auront débordé"
    },
    "Conditionnel Présent": {
      "Je": "déborderais",
      "Tu": "déborderais",
      "Il/Elle/On": "déborderait",
      "Nous": "déborderions",
      "Vous": "déborderiez",
      "Ils/Elle": "déborderaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais débordé",
      "Tu": "aurais débordé",
      "Il/Elle/On": "aurait débordé",
      "Nous": "aurions débordé",
      "Vous": "auriez débordé",
      "Ils/Elle": "auraient débordé"
    },
    "Subjonctif Présent": {
      "Je": "déborde",
      "Tu": "débordes",
      "Il/Elle/On": "déborde",
      "Nous": "débordions",
      "Vous": "débordiez",
      "Ils/Elle": "débordent"
    },
    "Subjonctif Passé": {
      "Je": "aie débordé",
      "Tu": "aies débordé",
      "Il/Elle/On": "ait débordé",
      "Nous": "ayons débordé",
      "Vous": "ayez débordé",
      "Ils/Elle": "aient débordé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse débordé",
      "Tu": "eusses débordé",
      "Il/Elle/On": "eût débordé",
      "Nous": "eussions débordé",
      "Vous": "eussiez débordé",
      "Ils/Elle": "eussent débordé"
    },
    "Subjonctif Imparfait": {
      "Je": "débordasse",
      "Tu": "débordasses",
      "Il/Elle/On": "débordât",
      "Nous": "débordassions",
      "Vous": "débordassiez",
      "Ils/Elle": "débordassent"
    },
    "Impératif Présent": {
      "Tu": "déborde",
      "Nous": "débordons",
      "Vous": "débordez"
    },
    "Impératif Passé": {
      "Tu": "aie débordé",
      "Nous": "ayons débordé",
      "Vous": "ayez débordé"
    },
    "Infinitif Présent": "déborder",
    "Infinitif Passé": "avoir débordé",
    "Participe Présent": "débordant",
    "Participe Passé": "débordé",
    "Gérondif Présent": "en débordant",
    "Gérondif Passé": "en ayant débordé"
},
"déchoir": {
    "Présent": {
      "Je": "déchois",
      "Tu": "déchois",
      "Il/Elle/On": "déchoit",
      "Nous": "déchoyons",
      "Vous": "déchoyez",
      "Ils/Elle": "déchoient"
    },
    "Imparfait": {
      "Je": "déchoyais",
      "Tu": "déchoyais",
      "Il/Elle/On": "déchoyait",
      "Nous": "déchoyions",
      "Vous": "déchoyiez",
      "Ils/Elle": "déchoyaient"
    },
    "Passé Composé": {
      "Je": "ai déchu",
      "Tu": "as déchu",
      "Il/Elle/On": "a déchu",
      "Nous": "avons déchu",
      "Vous": "avez déchu",
      "Ils/Elle": "ont déchu"
    },
    "Futur": {
      "Je": "déchoirai",
      "Tu": "déchoiras",
      "Il/Elle/On": "déchoira",
      "Nous": "déchoirons",
      "Vous": "déchoirez",
      "Ils/Elle": "déchoiront"
    },
    "Plus-que-parfait": {
      "Je": "avais déchu",
      "Tu": "avais déchu",
      "Il/Elle/On": "avait déchu",
      "Nous": "avions déchu",
      "Vous": "aviez déchu",
      "Ils/Elle": "avaient déchu"
    },
    "Futur Simple": {
      "Je": "déchoirai",
      "Tu": "déchoiras",
      "Il/Elle/On": "déchoira",
      "Nous": "déchoirons",
      "Vous": "déchoirez",
      "Ils/Elle": "déchoiront"
    },
    "Futur Antérieur": {
      "Je": "aurai déchu",
      "Tu": "auras déchu",
      "Il/Elle/On": "aura déchu",
      "Nous": "aurons déchu",
      "Vous": "aurez déchu",
      "Ils/Elle": "auront déchu"
    },
    "Conditionnel Présent": {
      "Je": "déchoirais",
      "Tu": "déchoirais",
      "Il/Elle/On": "déchoirait",
      "Nous": "déchoirions",
      "Vous": "déchoiriez",
      "Ils/Elle": "déchoiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais déchu",
      "Tu": "aurais déchu",
      "Il/Elle/On": "aurait déchu",
      "Nous": "aurions déchu",
      "Vous": "auriez déchu",
      "Ils/Elle": "auraient déchu"
    },
    "Subjonctif Présent": {
      "Je": "déchoie",
      "Tu": "déchoies",
      "Il/Elle/On": "déchoie",
      "Nous": "déchoyions",
      "Vous": "déchoyiez",
      "Ils/Elle": "déchoient"
    },
    "Subjonctif Passé": {
      "Je": "aie déchu",
      "Tu": "aies déchu",
      "Il/Elle/On": "ait déchu",
      "Nous": "ayons déchu",
      "Vous": "ayez déchu",
      "Ils/Elle": "aient déchu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse déchu",
      "Tu": "eusses déchu",
      "Il/Elle/On": "eût déchu",
      "Nous": "eussions déchu",
      "Vous": "eussiez déchu",
      "Ils/Elle": "eussent déchu"
    },
    "Subjonctif Imparfait": {
      "Je": "déchusse",
      "Tu": "déchusses",
      "Il/Elle/On": "déchût",
      "Nous": "déchussions",
      "Vous": "déchussiez",
      "Ils/Elle": "déchussent"
    },
    "Impératif Présent": {
      "Tu": "déchois",
      "Nous": "déchoyons",
      "Vous": "déchoyez"
    },
    "Impératif Passé": {
      "Tu": "aie déchu",
      "Nous": "ayons déchu",
      "Vous": "ayez déchu"
    },
    "Infinitif Présent": "déchoir",
    "Infinitif Passé": "avoir déchu",
    "Participe Présent": "déchoyant",
    "Participe Passé": "déchu",
    "Gérondif Présent": "en déchoyant",
    "Gérondif Passé": "en ayant déchu"
  },
  "décroître": {
    "Présent": {
      "Je": "décrois",
      "Tu": "décrois",
      "Il/Elle/On": "décroît",
      "Nous": "décroissons",
      "Vous": "décroissez",
      "Ils/Elle": "décroissent"
    },
    "Imparfait": {
      "Je": "décroissais",
      "Tu": "décroissais",
      "Il/Elle/On": "décroissait",
      "Nous": "décroissions",
      "Vous": "décroissiez",
      "Ils/Elle": "décroissaient"
    },
    "Passé Composé": {
      "Je": "ai décru",
      "Tu": "as décru",
      "Il/Elle/On": "a décru",
      "Nous": "avons décru",
      "Vous": "avez décru",
      "Ils/Elle": "ont décru"
    },
    "Futur": {
      "Je": "décroîtrai",
      "Tu": "décroîtras",
      "Il/Elle/On": "décroîtra",
      "Nous": "décroîtrons",
      "Vous": "décroîtrez",
      "Ils/Elle": "décroîtront"
    },
    "Plus-que-parfait": {
      "Je": "avais décru",
      "Tu": "avais décru",
      "Il/Elle/On": "avait décru",
      "Nous": "avions décru",
      "Vous": "aviez décru",
      "Ils/Elle": "avaient décru"
    },
    "Futur Simple": {
      "Je": "décroîtrai",
      "Tu": "décroîtras",
      "Il/Elle/On": "décroîtra",
      "Nous": "décroîtrons",
      "Vous": "décroîtrez",
      "Ils/Elle": "décroîtront"
    },
    "Futur Antérieur": {
      "Je": "aurai décru",
      "Tu": "auras décru",
      "Il/Elle/On": "aura décru",
      "Nous": "aurons décru",
      "Vous": "aurez décru",
      "Ils/Elle": "auront décru"
    },
    "Conditionnel Présent": {
      "Je": "décroîtrais",
      "Tu": "décroîtrais",
      "Il/Elle/On": "décroîtrait",
      "Nous": "décroîtrions",
      "Vous": "décroîtriez",
      "Ils/Elle": "décroîtraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais décru",
      "Tu": "aurais décru",
      "Il/Elle/On": "aurait décru",
      "Nous": "aurions décru",
      "Vous": "auriez décru",
      "Ils/Elle": "auraient décru"
    },
    "Subjonctif Présent": {
      "Je": "décroisse",
      "Tu": "décroisses",
      "Il/Elle/On": "décroisse",
      "Nous": "décroissions",
      "Vous": "décroissiez",
      "Ils/Elle": "décroissent"
    },
    "Subjonctif Passé": {
      "Je": "aie décru",
      "Tu": "aies décru",
      "Il/Elle/On": "ait décru",
      "Nous": "ayons décru",
      "Vous": "ayez décru",
      "Ils/Elle": "aient décru"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse décru",
      "Tu": "eusses décru",
      "Il/Elle/On": "eût décru",
      "Nous": "eussions décru",
      "Vous": "eussiez décru",
      "Ils/Elle": "eussent décru"
    },
    "Subjonctif Imparfait": {
      "Je": "décrusse",
      "Tu": "décrusses",
      "Il/Elle/On": "décrût",
      "Nous": "décrussions",
      "Vous": "décrussiez",
      "Ils/Elle": "décrussent"
    },
    "Impératif Présent": {
      "Tu": "décrois",
      "Nous": "décroissons",
      "Vous": "décroissez"
    },
    "Impératif Passé": {
      "Tu": "aie décru",
      "Nous": "ayons décru",
      "Vous": "ayez décru"
    },
    "Infinitif Présent": "décroître",
    "Infinitif Passé": "avoir décru",
    "Participe Présent": "décroissant",
    "Participe Passé": "décru",
    "Gérondif Présent": "en décroissant",
    "Gérondif Passé": "en ayant décru"
  },
  "dégénérer": {
    "Présent": {
      "Je": "dégénère",
      "Tu": "dégénères",
      "Il/Elle/On": "dégénère",
      "Nous": "dégénérons",
      "Vous": "dégénérez",
      "Ils/Elle": "dégénèrent"
    },
    "Imparfait": {
      "Je": "dégénérais",
      "Tu": "dégénérais",
      "Il/Elle/On": "dégénérait",
      "Nous": "dégénérions",
      "Vous": "dégénériez",
      "Ils/Elle": "dégénéraient"
    },
    "Passé Composé": {
      "Je": "ai dégénéré",
      "Tu": "as dégénéré",
      "Il/Elle/On": "a dégénéré",
      "Nous": "avons dégénéré",
      "Vous": "avez dégénéré",
      "Ils/Elle": "ont dégénéré"
    },
    "Futur": {
      "Je": "dégénérerai",
      "Tu": "dégénéreras",
      "Il/Elle/On": "dégénérera",
      "Nous": "dégénérerons",
      "Vous": "dégénérerez",
      "Ils/Elle": "dégénéreront"
    },
    "Plus-que-parfait": {
      "Je": "avais dégénéré",
      "Tu": "avais dégénéré",
      "Il/Elle/On": "avait dégénéré",
      "Nous": "avions dégénéré",
      "Vous": "aviez dégénéré",
      "Ils/Elle": "avaient dégénéré"
    },
    "Futur Simple": {
      "Je": "dégénérerai",
      "Tu": "dégénéreras",
      "Il/Elle/On": "dégénérera",
      "Nous": "dégénérerons",
      "Vous": "dégénérerez",
      "Ils/Elle": "dégénéreront"
    },
    "Futur Antérieur": {
      "Je": "aurai dégénéré",
      "Tu": "auras dégénéré",
      "Il/Elle/On": "aura dégénéré",
      "Nous": "aurons dégénéré",
      "Vous": "aurez dégénéré",
      "Ils/Elle": "auront dégénéré"
    },
    "Conditionnel Présent": {
      "Je": "dégénérerais",
      "Tu": "dégénérerais",
      "Il/Elle/On": "dégénérerait",
      "Nous": "dégénérerions",
      "Vous": "dégénéreriez",
      "Ils/Elle": "dégénéreraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais dégénéré",
      "Tu": "aurais dégénéré",
      "Il/Elle/On": "aurait dégénéré",
      "Nous": "aurions dégénéré",
      "Vous": "auriez dégénéré",
      "Ils/Elle": "auraient dégénéré"
    },
    "Subjonctif Présent": {
      "Je": "dégénère",
      "Tu": "dégénères",
      "Il/Elle/On": "dégénère",
      "Nous": "dégénérions",
      "Vous": "dégénériez",
      "Ils/Elle": "dégénèrent"
    },
    "Subjonctif Passé": {
      "Je": "aie dégénéré",
      "Tu": "aies dégénéré",
      "Il/Elle/On": "ait dégénéré",
      "Nous": "ayons dégénéré",
      "Vous": "ayez dégénéré",
      "Ils/Elle": "aient dégénéré"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse dégénéré",
      "Tu": "eusses dégénéré",
      "Il/Elle/On": "eût dégénéré",
      "Nous": "eussions dégénéré",
      "Vous": "eussiez dégénéré",
      "Ils/Elle": "eussent dégénéré"
    },
    "Subjonctif Imparfait": {
      "Je": "dégénérasse",
      "Tu": "dégénérasses",
      "Il/Elle/On": "dégénérât",
      "Nous": "dégénérassions",
      "Vous": "dégénérassiez",
      "Ils/Elle": "dégénérassent"
    },
    "Impératif Présent": {
      "Tu": "dégénère",
      "Nous": "dégénérons",
      "Vous": "dégénérez"
    },
    "Impératif Passé": {
      "Tu": "aie dégénéré",
      "Nous": "ayons dégénéré",
      "Vous": "ayez dégénéré"
    },
    "Infinitif Présent": "dégénérer",
    "Infinitif Passé": "avoir dégénéré",
    "Participe Présent": "dégénérant",
    "Participe Passé": "dégénéré",
    "Gérondif Présent": "en dégénérant",
    "Gérondif Passé": "en ayant dégénéré"
  },
  "déménager": {
    "Présent": {
      "Je": "déménage",
      "Tu": "déménages",
      "Il/Elle/On": "déménage",
      "Nous": "déménageons",
      "Vous": "déménagez",
      "Ils/Elle": "déménagent"
    },
    "Imparfait": {
      "Je": "déménageais",
      "Tu": "déménageais",
      "Il/Elle/On": "déménageait",
      "Nous": "déménagions",
      "Vous": "déménagiez",
      "Ils/Elle": "déménageaient"
    },
    "Passé Composé": {
      "Je": "ai déménagé",
      "Tu": "as déménagé",
      "Il/Elle/On": "a déménagé",
      "Nous": "avons déménagé",
      "Vous": "avez déménagé",
      "Ils/Elle": "ont déménagé"
    },
    "Futur": {
      "Je": "déménagerai",
      "Tu": "déménageras",
      "Il/Elle/On": "déménagera",
      "Nous": "déménagerons",
      "Vous": "déménagerez",
      "Ils/Elle": "déménageront"
    },
    "Plus-que-parfait": {
      "Je": "avais déménagé",
      "Tu": "avais déménagé",
      "Il/Elle/On": "avait déménagé",
      "Nous": "avions déménagé",
      "Vous": "aviez déménagé",
      "Ils/Elle": "avaient déménagé"
    },
    "Futur Simple": {
      "Je": "déménagerai",
      "Tu": "déménageras",
      "Il/Elle/On": "déménagera",
      "Nous": "déménagerons",
      "Vous": "déménagerez",
      "Ils/Elle": "déménageront"
    },
    "Futur Antérieur": {
      "Je": "aurai déménagé",
      "Tu": "auras déménagé",
      "Il/Elle/On": "aura déménagé",
      "Nous": "aurons déménagé",
      "Vous": "aurez déménagé",
      "Ils/Elle": "auront déménagé"
    },
    "Conditionnel Présent": {
      "Je": "déménagerais",
      "Tu": "déménagerais",
      "Il/Elle/On": "déménagerait",
      "Nous": "déménagerions",
      "Vous": "déménageriez",
      "Ils/Elle": "déménageraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais déménagé",
      "Tu": "aurais déménagé",
      "Il/Elle/On": "aurait déménagé",
      "Nous": "aurions déménagé",
      "Vous": "auriez déménagé",
      "Ils/Elle": "auraient déménagé"
    },
    "Subjonctif Présent": {
      "Je": "déménage",
      "Tu": "déménages",
      "Il/Elle/On": "déménage",
      "Nous": "déménagions",
      "Vous": "déménagiez",
      "Ils/Elle": "déménagent"
    },
    "Subjonctif Passé": {
      "Je": "aie déménagé",
      "Tu": "aies déménagé",
      "Il/Elle/On": "ait déménagé",
      "Nous": "ayons déménagé",
      "Vous": "ayez déménagé",
      "Ils/Elle": "aient déménagé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse déménagé",
      "Tu": "eusses déménagé",
      "Il/Elle/On": "eût déménagé",
      "Nous": "eussions déménagé",
      "Vous": "eussiez déménagé",
      "Ils/Elle": "eussent déménagé"
    },
    "Subjonctif Imparfait": {
      "Je": "déménageasse",
      "Tu": "déménageasses",
      "Il/Elle/On": "déménageât",
      "Nous": "déménageassions",
      "Vous": "déménageassiez",
      "Ils/Elle": "déménageassent"
    },
    "Impératif Présent": {
      "Tu": "déménage",
      "Nous": "déménageons",
      "Vous": "déménagez"
    },
    "Impératif Passé": {
      "Tu": "aie déménagé",
      "Nous": "ayons déménagé",
      "Vous": "ayez déménagé"
    },
    "Infinitif Présent": "déménager",
    "Infinitif Passé": "avoir déménagé",
    "Participe Présent": "déménageant",
    "Participe Passé": "déménagé",
    "Gérondif Présent": "en déménageant",
    "Gérondif Passé": "en ayant déménagé"
  },
  "dénicher": {
    "Présent": {
      "Je": "déniche",
      "Tu": "déniches",
      "Il/Elle/On": "déniche",
      "Nous": "dénichons",
      "Vous": "dénichez",
      "Ils/Elle": "dénichent"
    },
    "Imparfait": {
      "Je": "dénichais",
      "Tu": "dénichais",
      "Il/Elle/On": "dénichait",
      "Nous": "dénichions",
      "Vous": "dénichiez",
      "Ils/Elle": "dénichaient"
    },
    "Passé Composé": {
      "Je": "ai déniché",
      "Tu": "as déniché",
      "Il/Elle/On": "a déniché",
      "Nous": "avons déniché",
      "Vous": "avez déniché",
      "Ils/Elle": "ont déniché"
    },
    "Futur": {
      "Je": "dénicherai",
      "Tu": "dénicheras",
      "Il/Elle/On": "dénichera",
      "Nous": "dénicherons",
      "Vous": "dénicherez",
      "Ils/Elle": "dénicheront"
    },
    "Plus-que-parfait": {
      "Je": "avais déniché",
      "Tu": "avais déniché",
      "Il/Elle/On": "avait déniché",
      "Nous": "avions déniché",
      "Vous": "aviez déniché",
      "Ils/Elle": "avaient déniché"
    },
    "Futur Simple": {
      "Je": "dénicherai",
      "Tu": "dénicheras",
      "Il/Elle/On": "dénichera",
      "Nous": "dénicherons",
      "Vous": "dénicherez",
      "Ils/Elle": "dénicheront"
    },
    "Futur Antérieur": {
      "Je": "aurai déniché",
      "Tu": "auras déniché",
      "Il/Elle/On": "aura déniché",
      "Nous": "aurons déniché",
      "Vous": "aurez déniché",
      "Ils/Elle": "auront déniché"
    },
    "Conditionnel Présent": {
      "Je": "dénicherais",
      "Tu": "dénicherais",
      "Il/Elle/On": "dénicherait",
      "Nous": "dénicherions",
      "Vous": "dénicheriez",
      "Ils/Elle": "dénicheraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais déniché",
      "Tu": "aurais déniché",
      "Il/Elle/On": "aurait déniché",
      "Nous": "aurions déniché",
      "Vous": "auriez déniché",
      "Ils/Elle": "auraient déniché"
    },
    "Subjonctif Présent": {
      "Je": "déniche",
      "Tu": "déniches",
      "Il/Elle/On": "déniche",
      "Nous": "dénichions",
      "Vous": "dénichiez",
      "Ils/Elle": "dénichent"
    },
    "Subjonctif Passé": {
      "Je": "aie déniché",
      "Tu": "aies déniché",
      "Il/Elle/On": "ait déniché",
      "Nous": "ayons déniché",
      "Vous": "ayez déniché",
      "Ils/Elle": "aient déniché"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse déniché",
      "Tu": "eusses déniché",
      "Il/Elle/On": "eût déniché",
      "Nous": "eussions déniché",
      "Vous": "eussiez déniché",
      "Ils/Elle": "eussent déniché"
    },
    "Subjonctif Imparfait": {
      "Je": "dénichasse",
      "Tu": "dénichasses",
      "Il/Elle/On": "dénichât",
      "Nous": "dénichassions",
      "Vous": "dénichassiez",
      "Ils/Elle": "dénichassent"
    },
    "Impératif Présent": {
      "Tu": "déniche",
      "Nous": "dénichons",
      "Vous": "dénichez"
    },
    "Impératif Passé": {
      "Tu": "aie déniché",
      "Nous": "ayons déniché",
      "Vous": "ayez déniché"
    },
    "Infinitif Présent": "dénicher",
    "Infinitif Passé": "avoir déniché",
    "Participe Présent": "dénichant",
    "Participe Passé": "déniché",
    "Gérondif Présent": "en dénichant",
    "Gérondif Passé": "en ayant déniché"
},
"descendre": {
    "Présent": {
      "Je": "descends",
      "Tu": "descends",
      "Il/Elle/On": "descend",
      "Nous": "descendons",
      "Vous": "descendez",
      "Ils/Elle": "descendent"
    },
    "Imparfait": {
      "Je": "descendais",
      "Tu": "descendais",
      "Il/Elle/On": "descendait",
      "Nous": "descendions",
      "Vous": "descendiez",
      "Ils/Elle": "descendaient"
    },
    "Passé Composé": {
      "Je": "ai descendu",
      "Tu": "as descendu",
      "Il/Elle/On": "a descendu",
      "Nous": "avons descendu",
      "Vous": "avez descendu",
      "Ils/Elle": "ont descendu"
    },
    "Futur": {
      "Je": "descendrai",
      "Tu": "descendras",
      "Il/Elle/On": "descendra",
      "Nous": "descendrons",
      "Vous": "descendrez",
      "Ils/Elle": "descendront"
    },
    "Plus-que-parfait": {
      "Je": "avais descendu",
      "Tu": "avais descendu",
      "Il/Elle/On": "avait descendu",
      "Nous": "avions descendu",
      "Vous": "aviez descendu",
      "Ils/Elle": "avaient descendu"
    },
    "Futur Simple": {
      "Je": "descendrai",
      "Tu": "descendras",
      "Il/Elle/On": "descendra",
      "Nous": "descendrons",
      "Vous": "descendrez",
      "Ils/Elle": "descendront"
    },
    "Futur Antérieur": {
      "Je": "aurai descendu",
      "Tu": "auras descendu",
      "Il/Elle/On": "aura descendu",
      "Nous": "aurons descendu",
      "Vous": "aurez descendu",
      "Ils/Elle": "auront descendu"
    },
    "Conditionnel Présent": {
      "Je": "descendrais",
      "Tu": "descendrais",
      "Il/Elle/On": "descendrait",
      "Nous": "descendrions",
      "Vous": "descendriez",
      "Ils/Elle": "descendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais descendu",
      "Tu": "aurais descendu",
      "Il/Elle/On": "aurait descendu",
      "Nous": "aurions descendu",
      "Vous": "auriez descendu",
      "Ils/Elle": "auraient descendu"
    },
    "Subjonctif Présent": {
      "Je": "descende",
      "Tu": "descendes",
      "Il/Elle/On": "descende",
      "Nous": "descendions",
      "Vous": "descendiez",
      "Ils/Elle": "descendent"
    },
    "Subjonctif Passé": {
      "Je": "aie descendu",
      "Tu": "aies descendu",
      "Il/Elle/On": "ait descendu",
      "Nous": "ayons descendu",
      "Vous": "ayez descendu",
      "Ils/Elle": "aient descendu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse descendu",
      "Tu": "eusses descendu",
      "Il/Elle/On": "eût descendu",
      "Nous": "eussions descendu",
      "Vous": "eussiez descendu",
      "Ils/Elle": "eussent descendu"
    },
    "Subjonctif Imparfait": {
      "Je": "descendisse",
      "Tu": "descendisses",
      "Il/Elle/On": "descendît",
      "Nous": "descendissions",
      "Vous": "descendissiez",
      "Ils/Elle": "descendissent"
    },
    "Impératif Présent": {
      "Tu": "descends",
      "Nous": "descendons",
      "Vous": "descendez"
    },
    "Impératif Passé": {
      "Tu": "aie descendu",
      "Nous": "ayons descendu",
      "Vous": "ayez descendu"
    },
    "Infinitif Présent": "descendre",
    "Infinitif Passé": "avoir descendu",
    "Participe Présent": "descendant",
    "Participe Passé": "descendu",
    "Gérondif Présent": "en descendant",
    "Gérondif Passé": "en ayant descendu"
},
"redescendre": {
    "Présent": {
      "Je": "redescends",
      "Tu": "redescends",
      "Il/Elle/On": "redescend",
      "Nous": "redescendons",
      "Vous": "redescendez",
      "Ils/Elle": "redescendent"
    },
    "Imparfait": {
      "Je": "redescendais",
      "Tu": "redescendais",
      "Il/Elle/On": "redescendait",
      "Nous": "redescendions",
      "Vous": "redescendiez",
      "Ils/Elle": "redescendaient"
    },
    "Passé Composé": {
      "Je": "ai redescendu",
      "Tu": "as redescendu",
      "Il/Elle/On": "a redescendu",
      "Nous": "avons redescendu",
      "Vous": "avez redescendu",
      "Ils/Elle": "ont redescendu"
    },
    "Futur": {
      "Je": "redescendrai",
      "Tu": "redescendras",
      "Il/Elle/On": "redescendra",
      "Nous": "redescendrons",
      "Vous": "redescendrez",
      "Ils/Elle": "redescendront"
    },
    "Plus-que-parfait": {
      "Je": "avais redescendu",
      "Tu": "avais redescendu",
      "Il/Elle/On": "avait redescendu",
      "Nous": "avions redescendu",
      "Vous": "aviez redescendu",
      "Ils/Elle": "avaient redescendu"
    },
    "Futur Simple": {
      "Je": "redescendrai",
      "Tu": "redescendras",
      "Il/Elle/On": "redescendra",
      "Nous": "redescendrons",
      "Vous": "redescendrez",
      "Ils/Elle": "redescendront"
    },
    "Futur Antérieur": {
      "Je": "aurai redescendu",
      "Tu": "auras redescendu",
      "Il/Elle/On": "aura redescendu",
      "Nous": "aurons redescendu",
      "Vous": "aurez redescendu",
      "Ils/Elle": "auront redescendu"
    },
    "Conditionnel Présent": {
      "Je": "redescendrais",
      "Tu": "redescendrais",
      "Il/Elle/On": "redescendrait",
      "Nous": "redescendrions",
      "Vous": "redescendriez",
      "Ils/Elle": "redescendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais redescendu",
      "Tu": "aurais redescendu",
      "Il/Elle/On": "aurait redescendu",
      "Nous": "aurions redescendu",
      "Vous": "auriez redescendu",
      "Ils/Elle": "auraient redescendu"
    },
    "Subjonctif Présent": {
      "Je": "redescende",
      "Tu": "redescendes",
      "Il/Elle/On": "redescende",
      "Nous": "redescendions",
      "Vous": "redescendiez",
      "Ils/Elle": "redescendent"
    },
    "Subjonctif Passé": {
      "Je": "aie redescendu",
      "Tu": "aies redescendu",
      "Il/Elle/On": "ait redescendu",
      "Nous": "ayons redescendu",
      "Vous": "ayez redescendu",
      "Ils/Elle": "aient redescendu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse redescendu",
      "Tu": "eusses redescendu",
      "Il/Elle/On": "eût redescendu",
      "Nous": "eussions redescendu",
      "Vous": "eussiez redescendu",
      "Ils/Elle": "eussent redescendu"
    },
    "Subjonctif Imparfait": {
      "Je": "redescendisse",
      "Tu": "redescendisses",
      "Il/Elle/On": "redescendît",
      "Nous": "redescendissions",
      "Vous": "redescendissiez",
      "Ils/Elle": "redescendissent"
    },
    "Impératif Présent": {
      "Tu": "redescends",
      "Nous": "redescendons",
      "Vous": "redescendez"
    },
    "Impératif Passé": {
      "Tu": "aie redescendu",
      "Nous": "ayons redescendu",
      "Vous": "ayez redescendu"
    },
    "Infinitif Présent": "redescendre",
    "Infinitif Passé": "avoir redescendu",
    "Participe Présent": "redescendant",
    "Participe Passé": "redescendu",
    "Gérondif Présent": "en redescendant",
    "Gérondif Passé": "en ayant redescendu"
},
"diminuer": {
    "Présent": {
      "Je": "diminue",
      "Tu": "diminues",
      "Il/Elle/On": "diminue",
      "Nous": "diminuons",
      "Vous": "diminuez",
      "Ils/Elle": "diminuent"
    },
    "Imparfait": {
      "Je": "diminuais",
      "Tu": "diminuais",
      "Il/Elle/On": "diminuait",
      "Nous": "diminuions",
      "Vous": "diminuiez",
      "Ils/Elle": "diminuaient"
    },
    "Passé Composé": {
      "Je": "ai diminué",
      "Tu": "as diminué",
      "Il/Elle/On": "a diminué",
      "Nous": "avons diminué",
      "Vous": "avez diminué",
      "Ils/Elle": "ont diminué"
    },
    "Futur": {
      "Je": "diminuerai",
      "Tu": "diminueras",
      "Il/Elle/On": "diminuera",
      "Nous": "diminuerons",
      "Vous": "diminuerez",
      "Ils/Elle": "diminueront"
    },
    "Plus-que-parfait": {
      "Je": "avais diminué",
      "Tu": "avais diminué",
      "Il/Elle/On": "avait diminué",
      "Nous": "avions diminué",
      "Vous": "aviez diminué",
      "Ils/Elle": "avaient diminué"
    },
    "Futur Simple": {
      "Je": "diminuerai",
      "Tu": "diminueras",
      "Il/Elle/On": "diminuera",
      "Nous": "diminuerons",
      "Vous": "diminuerez",
      "Ils/Elle": "diminueront"
    },
    "Futur Antérieur": {
      "Je": "aurai diminué",
      "Tu": "auras diminué",
      "Il/Elle/On": "aura diminué",
      "Nous": "aurons diminué",
      "Vous": "aurez diminué",
      "Ils/Elle": "auront diminué"
    },
    "Conditionnel Présent": {
      "Je": "diminuerais",
      "Tu": "diminuerais",
      "Il/Elle/On": "diminuerait",
      "Nous": "diminuerions",
      "Vous": "diminueriez",
      "Ils/Elle": "diminueraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais diminué",
      "Tu": "aurais diminué",
      "Il/Elle/On": "aurait diminué",
      "Nous": "aurions diminué",
      "Vous": "auriez diminué",
      "Ils/Elle": "auraient diminué"
    },
    "Subjonctif Présent": {
      "Je": "diminue",
      "Tu": "diminues",
      "Il/Elle/On": "diminue",
      "Nous": "diminuions",
      "Vous": "diminuiez",
      "Ils/Elle": "diminuent"
    },
    "Subjonctif Passé": {
      "Je": "aie diminué",
      "Tu": "aies diminué",
      "Il/Elle/On": "ait diminué",
      "Nous": "ayons diminué",
      "Vous": "ayez diminué",
      "Ils/Elle": "aient diminué"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse diminué",
      "Tu": "eusses diminué",
      "Il/Elle/On": "eût diminué",
      "Nous": "eussions diminué",
      "Vous": "eussiez diminué",
      "Ils/Elle": "eussent diminué"
    },
    "Subjonctif Imparfait": {
      "Je": "diminuasse",
      "Tu": "diminuasses",
      "Il/Elle/On": "diminuât",
      "Nous": "diminuassions",
      "Vous": "diminuassiez",
      "Ils/Elle": "diminuassent"
    },
    "Impératif Présent": {
      "Tu": "diminue",
      "Nous": "diminuons",
      "Vous": "diminuez"
    },
    "Impératif Passé": {
      "Tu": "aie diminué",
      "Nous": "ayons diminué",
      "Vous": "ayez diminué"
    },
    "Infinitif Présent": "diminuer",
    "Infinitif Passé": "avoir diminué",
    "Participe Présent": "diminuant",
    "Participe Passé": "diminué",
    "Gérondif Présent": "en diminuant",
    "Gérondif Passé": "en ayant diminué"
},
"disconvenir": {
    "Présent": {
      "Je": "disconviens",
      "Tu": "disconviens",
      "Il/Elle/On": "disconvient",
      "Nous": "disconvenons",
      "Vous": "disconvenez",
      "Ils/Elle": "disconviennent"
    },
    "Imparfait": {
      "Je": "disconvenais",
      "Tu": "disconvenais",
      "Il/Elle/On": "disconvenait",
      "Nous": "disconvenions",
      "Vous": "disconveniez",
      "Ils/Elle": "disconvenaient"
    },
    "Passé Composé": {
      "Je": "ai disconvenu",
      "Tu": "as disconvenu",
      "Il/Elle/On": "a disconvenu",
      "Nous": "avons disconvenu",
      "Vous": "avez disconvenu",
      "Ils/Elle": "ont disconvenu"
    },
    "Futur": {
      "Je": "disconviendrai",
      "Tu": "disconviendras",
      "Il/Elle/On": "disconviendra",
      "Nous": "disconviendrons",
      "Vous": "disconviendrez",
      "Ils/Elle": "disconviendront"
    },
    "Plus-que-parfait": {
      "Je": "avais disconvenu",
      "Tu": "avais disconvenu",
      "Il/Elle/On": "avait disconvenu",
      "Nous": "avions disconvenu",
      "Vous": "aviez disconvenu",
      "Ils/Elle": "avaient disconvenu"
    },
    "Futur Simple": {
      "Je": "disconviendrai",
      "Tu": "disconviendras",
      "Il/Elle/On": "disconviendra",
      "Nous": "disconviendrons",
      "Vous": "disconviendrez",
      "Ils/Elle": "disconviendront"
    },
    "Futur Antérieur": {
      "Je": "aurai disconvenu",
      "Tu": "auras disconvenu",
      "Il/Elle/On": "aura disconvenu",
      "Nous": "aurons disconvenu",
      "Vous": "aurez disconvenu",
      "Ils/Elle": "auront disconvenu"
    },
    "Conditionnel Présent": {
      "Je": "disconviendrais",
      "Tu": "disconviendrais",
      "Il/Elle/On": "disconviendrait",
      "Nous": "disconviendrions",
      "Vous": "disconviendriez",
      "Ils/Elle": "disconviendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais disconvenu",
      "Tu": "aurais disconvenu",
      "Il/Elle/On": "aurait disconvenu",
      "Nous": "aurions disconvenu",
      "Vous": "auriez disconvenu",
      "Ils/Elle": "auraient disconvenu"
    },
    "Subjonctif Présent": {
      "Je": "disconvienne",
      "Tu": "disconviennes",
      "Il/Elle/On": "disconvienne",
      "Nous": "disconvenions",
      "Vous": "disconveniez",
      "Ils/Elle": "disconviiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie disconvenu",
      "Tu": "aies disconvenu",
      "Il/Elle/On": "ait disconvenu",
      "Nous": "ayons disconvenu",
      "Vous": "ayez disconvenu",
      "Ils/Elle": "aient disconvenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse disconvenu",
      "Tu": "eusses disconvenu",
      "Il/Elle/On": "eût disconvenu",
      "Nous": "eussions disconvenu",
      "Vous": "eussiez disconvenu",
      "Ils/Elle": "eussent disconvenu"
    },
    "Subjonctif Imparfait": {
      "Je": "disconvinisse",
      "Tu": "disconvinisses",
      "Il/Elle/On": "disconvinît",
      "Nous": "disconvinissions",
      "Vous": "disconvinissiez",
      "Ils/Elle": "disconvinissent"
    },
    "Impératif Présent": {
      "Tu": "disconviens",
      "Nous": "disconvenons",
      "Vous": "disconvenez"
    },
    "Impératif Passé": {
      "Tu": "aie disconvenu",
      "Nous": "ayons disconvenu",
      "Vous": "ayez disconvenu"
    },
    "Infinitif Présent": "disconvenir",
    "Infinitif Passé": "avoir disconvenu",
    "Participe Présent": "disconvenant",
    "Participe Passé": "disconvenu",
    "Gérondif Présent": "en disconvenant",
    "Gérondif Passé": "en ayant disconvenu"
},
"disparaitre": {
    "Présent": {
      "Je": "disparais",
      "Tu": "disparais",
      "Il/Elle/On": "disparait",
      "Nous": "disparaissons",
      "Vous": "disparaissez",
      "Ils/Elle": "disparaissent"
    },
    "Imparfait": {
      "Je": "disparaissais",
      "Tu": "disparaissais",
      "Il/Elle/On": "disparaissait",
      "Nous": "disparaissions",
      "Vous": "disparaissiez",
      "Ils/Elle": "disparaissaient"
    },
    "Passé Composé": {
      "Je": "ai disparu",
      "Tu": "as disparu",
      "Il/Elle/On": "a disparu",
      "Nous": "avons disparu",
      "Vous": "avez disparu",
      "Ils/Elle": "ont disparu"
    },
    "Futur": {
      "Je": "disparaitrai",
      "Tu": "disparaitras",
      "Il/Elle/On": "disparaitra",
      "Nous": "disparaitrons",
      "Vous": "disparaitrez",
      "Ils/Elle": "disparaitront"
    },
    "Plus-que-parfait": {
      "Je": "avais disparu",
      "Tu": "avais disparu",
      "Il/Elle/On": "avait disparu",
      "Nous": "avions disparu",
      "Vous": "aviez disparu",
      "Ils/Elle": "avaient disparu"
    },
    "Futur Simple": {
      "Je": "disparaitrai",
      "Tu": "disparaitras",
      "Il/Elle/On": "disparaitra",
      "Nous": "disparaitrons",
      "Vous": "disparaitrez",
      "Ils/Elle": "disparaitront"
    },
    "Futur Antérieur": {
      "Je": "aurai disparu",
      "Tu": "auras disparu",
      "Il/Elle/On": "aura disparu",
      "Nous": "aurons disparu",
      "Vous": "aurez disparu",
      "Ils/Elle": "auront disparu"
    },
    "Conditionnel Présent": {
      "Je": "disparaitrais",
      "Tu": "disparaitrais",
      "Il/Elle/On": "disparaitrait",
      "Nous": "disparaitrions",
      "Vous": "disparaitriez",
      "Ils/Elle": "disparaitraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais disparu",
      "Tu": "aurais disparu",
      "Il/Elle/On": "aurait disparu",
      "Nous": "aurions disparu",
      "Vous": "auriez disparu",
      "Ils/Elle": "auraient disparu"
    },
    "Subjonctif Présent": {
      "Je": "disparaisse",
      "Tu": "disparaisses",
      "Il/Elle/On": "disparaisse",
      "Nous": "disparaissions",
      "Vous": "disparaissiez",
      "Ils/Elle": "disparaissent"
    },
    "Subjonctif Passé": {
      "Je": "aie disparu",
      "Tu": "aies disparu",
      "Il/Elle/On": "ait disparu",
      "Nous": "ayons disparu",
      "Vous": "ayez disparu",
      "Ils/Elle": "aient disparu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse disparu",
      "Tu": "eusses disparu",
      "Il/Elle/On": "eût disparu",
      "Nous": "eussions disparu",
      "Vous": "eussiez disparu",
      "Ils/Elle": "eussent disparu"
    },
    "Subjonctif Imparfait": {
      "Je": "disparusse",
      "Tu": "disparusses",
      "Il/Elle/On": "disparût",
      "Nous": "disparussions",
      "Vous": "disparussiez",
      "Ils/Elle": "disparussent"
    },
    "Impératif Présent": {
      "Tu": "disparais",
      "Nous": "disparaissons",
      "Vous": "disparaissez"
    },
    "Impératif Passé": {
      "Tu": "aie disparu",
      "Nous": "ayons disparu",
      "Vous": "ayez disparu"
    },
    "Infinitif Présent": "disparaitre",
    "Infinitif Passé": "avoir disparu",
    "Participe Présent": "disparaissant",
    "Participe Passé": "disparu",
    "Gérondif Présent": "en disparissant",
    "Gérondif Passé": "en ayant disparu"
},
"divorcer": {
    "Présent": {
      "Je": "divorce",
      "Tu": "divorces",
      "Il/Elle/On": "divorce",
      "Nous": "divorçons",
      "Vous": "divorcez",
      "Ils/Elle": "divorcent"
    },
    "Imparfait": {
      "Je": "divorçais",
      "Tu": "divorçais",
      "Il/Elle/On": "divorçait",
      "Nous": "divorcions",
      "Vous": "divorciez",
      "Ils/Elle": "divorçaient"
    },
    "Passé Composé": {
      "Je": "ai divorcé",
      "Tu": "as divorcé",
      "Il/Elle/On": "a divorcé",
      "Nous": "avons divorcé",
      "Vous": "avez divorcé",
      "Ils/Elle": "ont divorcé"
    },
    "Futur": {
      "Je": "divorcerai",
      "Tu": "divorceras",
      "Il/Elle/On": "divorcera",
      "Nous": "divorcerons",
      "Vous": "divorcerez",
      "Ils/Elle": "divorceront"
    },
    "Plus-que-parfait": {
      "Je": "avais divorcé",
      "Tu": "avais divorcé",
      "Il/Elle/On": "avait divorcé",
      "Nous": "avions divorcé",
      "Vous": "aviez divorcé",
      "Ils/Elle": "avaient divorcé"
    },
    "Futur Simple": {
      "Je": "divorcerai",
      "Tu": "divorceras",
      "Il/Elle/On": "divorcera",
      "Nous": "divorcerons",
      "Vous": "divorcerez",
      "Ils/Elle": "divorceront"
    },
    "Futur Antérieur": {
      "Je": "aurai divorcé",
      "Tu": "auras divorcé",
      "Il/Elle/On": "aura divorcé",
      "Nous": "aurons divorcé",
      "Vous": "aurez divorcé",
      "Ils/Elle": "auront divorcé"
    },
    "Conditionnel Présent": {
      "Je": "divorcerais",
      "Tu": "divorcerais",
      "Il/Elle/On": "divorcerait",
      "Nous": "divorcerions",
      "Vous": "divorceriez",
      "Ils/Elle": "divorceraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais divorcé",
      "Tu": "aurais divorcé",
      "Il/Elle/On": "aurait divorcé",
      "Nous": "aurions divorcé",
      "Vous": "auriez divorcé",
      "Ils/Elle": "auraient divorcé"
    },
    "Subjonctif Présent": {
      "Je": "divorce",
      "Tu": "divorces",
      "Il/Elle/On": "divorce",
      "Nous": "divorcions",
      "Vous": "divorciez",
      "Ils/Elle": "divorcent"
    },
    "Subjonctif Passé": {
      "Je": "aie divorcé",
      "Tu": "aies divorcé",
      "Il/Elle/On": "ait divorcé",
      "Nous": "ayons divorcé",
      "Vous": "ayez divorcé",
      "Ils/Elle": "aient divorcé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse divorcé",
      "Tu": "eusses divorcé",
      "Il/Elle/On": "eût divorcé",
      "Nous": "eussions divorcé",
      "Vous": "eussiez divorcé",
      "Ils/Elle": "eussent divorcé"
    },
    "Subjonctif Imparfait": {
      "Je": "divorçasse",
      "Tu": "divorçasses",
      "Il/Elle/On": "divorçât",
      "Nous": "divorçassions",
      "Vous": "divorçassiez",
      "Ils/Elle": "divorçassent"
    },
    "Impératif Présent": {
      "Tu": "divorce",
      "Nous": "divorçons",
      "Vous": "divorcez"
    },
    "Impératif Passé": {
      "Tu": "aie divorcé",
      "Nous": "ayons divorcé",
      "Vous": "ayez divorcé"
    },
    "Infinitif Présent": "divorcer",
    "Infinitif Passé": "avoir divorcé",
    "Participe Présent": "divorçant",
    "Participe Passé": "divorcé",
    "Gérondif Présent": "en divorçant",
    "Gérondif Passé": "en ayant divorcé"
},
"échapper": {
    "Présent": {
      "Je": "échappe",
      "Tu": "échappes",
      "Il/Elle/On": "échappe",
      "Nous": "échappons",
      "Vous": "échappez",
      "Ils/Elle": "échappent"
    },
    "Imparfait": {
      "Je": "échappais",
      "Tu": "échappais",
      "Il/Elle/On": "échappait",
      "Nous": "échappions",
      "Vous": "échappiez",
      "Ils/Elle": "échappaient"
    },
    "Passé Composé": {
      "Je": "ai échappé",
      "Tu": "as échappé",
      "Il/Elle/On": "a échappé",
      "Nous": "avons échappé",
      "Vous": "avez échappé",
      "Ils/Elle": "ont échappé"
    },
    "Futur": {
      "Je": "échapperai",
      "Tu": "échapperas",
      "Il/Elle/On": "échappera",
      "Nous": "échapperons",
      "Vous": "échapperez",
      "Ils/Elle": "échapperont"
    },
    "Plus-que-parfait": {
      "Je": "avais échappé",
      "Tu": "avais échappé",
      "Il/Elle/On": "avait échappé",
      "Nous": "avions échappé",
      "Vous": "aviez échappé",
      "Ils/Elle": "avaient échappé"
    },
    "Futur Simple": {
      "Je": "échapperai",
      "Tu": "échapperas",
      "Il/Elle/On": "échappera",
      "Nous": "échapperons",
      "Vous": "échapperez",
      "Ils/Elle": "échapperont"
    },
    "Futur Antérieur": {
      "Je": "aurai échappé",
      "Tu": "auras échappé",
      "Il/Elle/On": "aura échappé",
      "Nous": "aurons échappé",
      "Vous": "aurez échappé",
      "Ils/Elle": "auront échappé"
    },
    "Conditionnel Présent": {
      "Je": "échapperais",
      "Tu": "échapperais",
      "Il/Elle/On": "échapperait",
      "Nous": "échapperions",
      "Vous": "échapperiez",
      "Ils/Elle": "échapperaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais échappé",
      "Tu": "aurais échappé",
      "Il/Elle/On": "aurait échappé",
      "Nous": "aurions échappé",
      "Vous": "auriez échappé",
      "Ils/Elle": "auraient échappé"
    },
    "Subjonctif Présent": {
      "Je": "échappe",
      "Tu": "échappes",
      "Il/Elle/On": "échappe",
      "Nous": "échappions",
      "Vous": "échappiez",
      "Ils/Elle": "échappent"
    },
    "Subjonctif Passé": {
      "Je": "aie échappé",
      "Tu": "aies échappé",
      "Il/Elle/On": "ait échappé",
      "Nous": "ayons échappé",
      "Vous": "ayez échappé",
      "Ils/Elle": "aient échappé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse échappé",
      "Tu": "eusses échappé",
      "Il/Elle/On": "eût échappé",
      "Nous": "eussions échappé",
      "Vous": "eussiez échappé",
      "Ils/Elle": "eussent échappé"
    },
    "Subjonctif Imparfait": {
      "Je": "échappasse",
      "Tu": "échappasses",
      "Il/Elle/On": "échappât",
      "Nous": "échappassions",
      "Vous": "échappassiez",
      "Ils/Elle": "échappassent"
    },
    "Impératif Présent": {
      "Tu": "échappe",
      "Nous": "échappons",
      "Vous": "échappez"
    },
    "Impératif Passé": {
      "Tu": "aie échappé",
      "Nous": "ayons échappé",
      "Vous": "ayez échappé"
    },
    "Infinitif Présent": "échapper",
    "Infinitif Passé": "avoir échappé",
    "Participe Présent": "échappant",
    "Participe Passé": "échappé",
    "Gérondif Présent": "en échappant",
    "Gérondif Passé": "en ayant échappé"
},
"échouer": {
    "Présent": {
      "Je": "échoue",
      "Tu": "échoues",
      "Il/Elle/On": "échoue",
      "Nous": "échouons",
      "Vous": "échouez",
      "Ils/Elle": "échouent"
    },
    "Imparfait": {
      "Je": "échouais",
      "Tu": "échouais",
      "Il/Elle/On": "échouait",
      "Nous": "échouions",
      "Vous": "échouiez",
      "Ils/Elle": "échouaient"
    },
    "Passé Composé": {
      "Je": "ai échoué",
      "Tu": "as échoué",
      "Il/Elle/On": "a échoué",
      "Nous": "avons échoué",
      "Vous": "avez échoué",
      "Ils/Elle": "ont échoué"
    },
    "Futur": {
      "Je": "échouerai",
      "Tu": "échoueras",
      "Il/Elle/On": "échouera",
      "Nous": "échouerons",
      "Vous": "échouerez",
      "Ils/Elle": "échoueront"
    },
    "Plus-que-parfait": {
      "Je": "avais échoué",
      "Tu": "avais échoué",
      "Il/Elle/On": "avait échoué",
      "Nous": "avions échoué",
      "Vous": "aviez échoué",
      "Ils/Elle": "avaient échoué"
    },
    "Futur Simple": {
      "Je": "échouerai",
      "Tu": "échoueras",
      "Il/Elle/On": "échouera",
      "Nous": "échouerons",
      "Vous": "échouerez",
      "Ils/Elle": "échoueront"
    },
    "Futur Antérieur": {
      "Je": "aurai échoué",
      "Tu": "auras échoué",
      "Il/Elle/On": "aura échoué",
      "Nous": "aurons échoué",
      "Vous": "aurez échoué",
      "Ils/Elle": "auront échoué"
    },
    "Conditionnel Présent": {
      "Je": "échouerais",
      "Tu": "échouerais",
      "Il/Elle/On": "échouerait",
      "Nous": "échouerions",
      "Vous": "échoueriez",
      "Ils/Elle": "échoueraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais échoué",
      "Tu": "aurais échoué",
      "Il/Elle/On": "aurait échoué",
      "Nous": "aurions échoué",
      "Vous": "auriez échoué",
      "Ils/Elle": "auraient échoué"
    },
    "Subjonctif Présent": {
      "Je": "échoue",
      "Tu": "échoues",
      "Il/Elle/On": "échoue",
      "Nous": "échouions",
      "Vous": "échouiez",
      "Ils/Elle": "échouent"
    },
    "Subjonctif Passé": {
      "Je": "aie échoué",
      "Tu": "aies échoué",
      "Il/Elle/On": "ait échoué",
      "Nous": "ayons échoué",
      "Vous": "ayez échoué",
      "Ils/Elle": "aient échoué"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse échoué",
      "Tu": "eusses échoué",
      "Il/Elle/On": "eût échoué",
      "Nous": "eussions échoué",
      "Vous": "eussiez échoué",
      "Ils/Elle": "eussent échoué"
    },
    "Subjonctif Imparfait": {
      "Je": "échouasse",
      "Tu": "échouasses",
      "Il/Elle/On": "échouât",
      "Nous": "échouassions",
      "Vous": "échouassiez",
      "Ils/Elle": "échouassent"
    },
    "Impératif Présent": {
      "Tu": "échoue",
      "Nous": "échouons",
      "Vous": "échouez"
    },
    "Impératif Passé": {
      "Tu": "aie échoué",
      "Nous": "ayons échoué",
      "Vous": "ayez échoué"
    },
    "Infinitif Présent": "échouer",
    "Infinitif Passé": "avoir échoué",
    "Participe Présent": "échouant",
    "Participe Passé": "échoué",
    "Gérondif Présent": "en échouant",
    "Gérondif Passé": "en ayant échoué"
},
"éclater": {
    "Présent": {
      "Je": "éclate",
      "Tu": "éclates",
      "Il/Elle/On": "éclate",
      "Nous": "éclatons",
      "Vous": "éclatez",
      "Ils/Elle": "éclatent"
    },
    "Imparfait": {
      "Je": "éclatais",
      "Tu": "éclatais",
      "Il/Elle/On": "éclatait",
      "Nous": "éclations",
      "Vous": "éclatiez",
      "Ils/Elle": "éclataient"
    },
    "Passé Composé": {
      "Je": "ai éclaté",
      "Tu": "as éclaté",
      "Il/Elle/On": "a éclaté",
      "Nous": "avons éclaté",
      "Vous": "avez éclaté",
      "Ils/Elle": "ont éclaté"
    },
    "Futur": {
      "Je": "éclaterai",
      "Tu": "éclateras",
      "Il/Elle/On": "éclatera",
      "Nous": "éclaterons",
      "Vous": "éclaterez",
      "Ils/Elle": "éclateront"
    },
    "Plus-que-parfait": {
      "Je": "avais éclaté",
      "Tu": "avais éclaté",
      "Il/Elle/On": "avait éclaté",
      "Nous": "avions éclaté",
      "Vous": "aviez éclaté",
      "Ils/Elle": "avaient éclaté"
    },
    "Futur Simple": {
      "Je": "éclaterai",
      "Tu": "éclateras",
      "Il/Elle/On": "éclatera",
      "Nous": "éclaterons",
      "Vous": "éclaterez",
      "Ils/Elle": "éclateront"
    },
    "Futur Antérieur": {
      "Je": "aurai éclaté",
      "Tu": "auras éclaté",
      "Il/Elle/On": "aura éclaté",
      "Nous": "aurons éclaté",
      "Vous": "aurez éclaté",
      "Ils/Elle": "auront éclaté"
    },
    "Conditionnel Présent": {
      "Je": "éclaterais",
      "Tu": "éclaterais",
      "Il/Elle/On": "éclaterait",
      "Nous": "éclaterions",
      "Vous": "éclateriez",
      "Ils/Elle": "éclateraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais éclaté",
      "Tu": "aurais éclaté",
      "Il/Elle/On": "aurait éclaté",
      "Nous": "aurions éclaté",
      "Vous": "auriez éclaté",
      "Ils/Elle": "auraient éclaté"
    },
    "Subjonctif Présent": {
      "Je": "éclate",
      "Tu": "éclates",
      "Il/Elle/On": "éclate",
      "Nous": "éclations",
      "Vous": "éclatiez",
      "Ils/Elle": "éclatent"
    },
    "Subjonctif Passé": {
      "Je": "aie éclaté",
      "Tu": "aies éclaté",
      "Il/Elle/On": "ait éclaté",
      "Nous": "ayons éclaté",
      "Vous": "ayez éclaté",
      "Ils/Elle": "aient éclaté"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse éclaté",
      "Tu": "eusses éclaté",
      "Il/Elle/On": "eût éclaté",
      "Nous": "eussions éclaté",
      "Vous": "eussiez éclaté",
      "Ils/Elle": "eussent éclaté"
    },
    "Subjonctif Imparfait": {
      "Je": "éclatasse",
      "Tu": "éclatasses",
      "Il/Elle/On": "éclatât",
      "Nous": "éclatassions",
      "Vous": "éclatassiez",
      "Ils/Elle": "éclatassent"
    },
    "Impératif Présent": {
      "Tu": "éclate",
      "Nous": "éclatons",
      "Vous": "éclatez"
    },
    "Impératif Passé": {
      "Tu": "aie éclaté",
      "Nous": "ayons éclaté",
      "Vous": "ayez éclaté"
    },
    "Infinitif Présent": "éclater",
    "Infinitif Passé": "avoir éclaté",
    "Participe Présent": "éclatant",
    "Participe Passé": "éclaté",
    "Gérondif Présent": "en éclatant",
    "Gérondif Passé": "en ayant éclaté"
},
"éclore": {
    "Présent": {
      "Je": "éclos",
      "Tu": "éclos",
      "Il/Elle/On": "écloît",
      "Nous": "éclosons",
      "Vous": "éclosez",
      "Ils/Elle": "éclosent"
    },
    "Imparfait": {
      "Je": "éclosais",
      "Tu": "éclosais",
      "Il/Elle/On": "éclosait",
      "Nous": "éclosions",
      "Vous": "éclosiez",
      "Ils/Elle": "éclosaient"
    },
    "Passé Composé": {
      "Je": "ai éclos",
      "Tu": "as éclos",
      "Il/Elle/On": "a éclos",
      "Nous": "avons éclos",
      "Vous": "avez éclos",
      "Ils/Elle": "ont éclos"
    },
    "Futur": {
      "Je": "écloreai",
      "Tu": "écloreas",
      "Il/Elle/On": "écloreas",
      "Nous": "écloreons",
      "Vous": "éclorez",
      "Ils/Elle": "éclorent"
    },
    "Plus-que-parfait": {
      "Je": "avais éclos",
      "Tu": "avais éclos",
      "Il/Elle/On": "avait éclos",
      "Nous": "avions éclos",
      "Vous": "aviez éclos",
      "Ils/Elle": "avaient éclos"
    },
    "Futur Simple": {
      "Je": "écloreai",
      "Tu": "écloreas",
      "Il/Elle/On": "écloreas",
      "Nous": "écloreons",
      "Vous": "éclorez",
      "Ils/Elle": "éclorent"
    },
    "Futur Antérieur": {
      "Je": "aurai éclos",
      "Tu": "auras éclos",
      "Il/Elle/On": "aura éclos",
      "Nous": "aurons éclos",
      "Vous": "aurez éclos",
      "Ils/Elle": "auront éclos"
    },
    "Conditionnel Présent": {
      "Je": "écloreais",
      "Tu": "écloreais",
      "Il/Elle/On": "écloreait",
      "Nous": "écloreions",
      "Vous": "écloreiez",
      "Ils/Elle": "écloreiaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais éclos",
      "Tu": "aurais éclos",
      "Il/Elle/On": "aurait éclos",
      "Nous": "aurions éclos",
      "Vous": "auriez éclos",
      "Ils/Elle": "auraient éclos"
    },
    "Subjonctif Présent": {
      "Je": "écloie",
      "Tu": "écloies",
      "Il/Elle/On": "écloie",
      "Nous": "écloiions",
      "Vous": "écloiiez",
      "Ils/Elle": "écloient"
    },
    "Subjonctif Passé": {
      "Je": "aie éclos",
      "Tu": "aies éclos",
      "Il/Elle/On": "ait éclos",
      "Nous": "ayons éclos",
      "Vous": "ayez éclos",
      "Ils/Elle": "aient éclos"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse éclos",
      "Tu": "eusses éclos",
      "Il/Elle/On": "eût éclos",
      "Nous": "eussions éclos",
      "Vous": "eussiez éclos",
      "Ils/Elle": "eussent éclos"
    },
    "Subjonctif Imparfait": {
      "Je": "éclosse",
      "Tu": "éclosses",
      "Il/Elle/On": "éclosât",
      "Nous": "éclossions",
      "Vous": "éclossiez",
      "Ils/Elle": "éclossent"
    },
    "Impératif Présent": {
      "Tu": "éclos",
      "Nous": "éclosons",
      "Vous": "éclosez"
    },
    "Impératif Passé": {
      "Tu": "aie éclos",
      "Nous": "ayons éclos",
      "Vous": "ayez éclos"
    },
    "Infinitif Présent": "éclore",
    "Infinitif Passé": "avoir éclos",
    "Participe Présent": "éclosant",
    "Participe Passé": "éclos",
    "Gérondif Présent": "en éclosant",
    "Gérondif Passé": "en ayant éclos"
  },
  "embellir": {
    "Présent": {
      "Je": "embellis",
      "Tu": "embellis",
      "Il/Elle/On": "embellit",
      "Nous": "embellissons",
      "Vous": "embellissez",
      "Ils/Elle": "embellissent"
    },
    "Imparfait": {
      "Je": "embellissais",
      "Tu": "embellissais",
      "Il/Elle/On": "embellissait",
      "Nous": "embellissions",
      "Vous": "embellissiez",
      "Ils/Elle": "embellissaient"
    },
    "Passé Composé": {
      "Je": "ai embelli",
      "Tu": "as embelli",
      "Il/Elle/On": "a embelli",
      "Nous": "avons embelli",
      "Vous": "avez embelli",
      "Ils/Elle": "ont embelli"
    },
    "Futur": {
      "Je": "embellirai",
      "Tu": "embelliras",
      "Il/Elle/On": "embellira",
      "Nous": "embellirons",
      "Vous": "embellirez",
      "Ils/Elle": "embelliront"
    },
    "Plus-que-parfait": {
      "Je": "avais embelli",
      "Tu": "avais embelli",
      "Il/Elle/On": "avait embelli",
      "Nous": "avions embelli",
      "Vous": "aviez embelli",
      "Ils/Elle": "avaient embelli"
    },
    "Futur Simple": {
      "Je": "embellirai",
      "Tu": "embelliras",
      "Il/Elle/On": "embellira",
      "Nous": "embellirons",
      "Vous": "embellirez",
      "Ils/Elle": "embelliront"
    },
    "Futur Antérieur": {
      "Je": "aurai embelli",
      "Tu": "auras embelli",
      "Il/Elle/On": "aura embelli",
      "Nous": "aurons embelli",
      "Vous": "aurez embelli",
      "Ils/Elle": "auront embelli"
    },
    "Conditionnel Présent": {
      "Je": "embellirais",
      "Tu": "embellirais",
      "Il/Elle/On": "embellirait",
      "Nous": "embellirions",
      "Vous": "embelliriez",
      "Ils/Elle": "embelliraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais embelli",
      "Tu": "aurais embelli",
      "Il/Elle/On": "aurait embelli",
      "Nous": "aurions embelli",
      "Vous": "auriez embelli",
      "Ils/Elle": "auraient embelli"
    },
    "Subjonctif Présent": {
      "Je": "embellisse",
      "Tu": "embellisses",
      "Il/Elle/On": "embellisse",
      "Nous": "embellissions",
      "Vous": "embellissiez",
      "Ils/Elle": "embellissent"
    },
    "Subjonctif Passé": {
      "Je": "aie embelli",
      "Tu": "aies embelli",
      "Il/Elle/On": "ait embelli",
      "Nous": "ayons embelli",
      "Vous": "ayez embelli",
      "Ils/Elle": "aient embelli"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse embelli",
      "Tu": "eusses embelli",
      "Il/Elle/On": "eût embelli",
      "Nous": "eussions embelli",
      "Vous": "eussiez embelli",
      "Ils/Elle": "eussent embelli"
    },
    "Subjonctif Imparfait": {
      "Je": "embellisse",
      "Tu": "embellisses",
      "Il/Elle/On": "embellît",
      "Nous": "embellissions",
      "Vous": "embellissiez",
      "Ils/Elle": "embellissent"
    },
    "Impératif Présent": {
      "Tu": "embellis",
      "Nous": "embellissons",
      "Vous": "embellissez"
    },
    "Impératif Passé": {
      "Tu": "aie embelli",
      "Nous": "ayons embelli",
      "Vous": "ayez embelli"
    },
    "Infinitif Présent": "embellir",
    "Infinitif Passé": "avoir embelli",
    "Participe Présent": "embellissant",
    "Participe Passé": "embelli",
    "Gérondif Présent": "en embellissant",
    "Gérondif Passé": "en ayant embelli"
  },
  "empirer": {
    "Présent": {
      "Je": "empire",
      "Tu": "empires",
      "Il/Elle/On": "empire",
      "Nous": "empirons",
      "Vous": "empirez",
      "Ils/Elle": "empirent"
    },
    "Imparfait": {
      "Je": "empirais",
      "Tu": "empirais",
      "Il/Elle/On": "empirait",
      "Nous": "empirions",
      "Vous": "empiriez",
      "Ils/Elle": "empiraient"
    },
    "Passé Composé": {
      "Je": "ai empiré",
      "Tu": "as empiré",
      "Il/Elle/On": "a empiré",
      "Nous": "avons empiré",
      "Vous": "avez empiré",
      "Ils/Elle": "ont empiré"
    },
    "Futur": {
      "Je": "empirerai",
      "Tu": "empireras",
      "Il/Elle/On": "empirera",
      "Nous": "empirerons",
      "Vous": "empirerez",
      "Ils/Elle": "empireront"
    },
    "Plus-que-parfait": {
      "Je": "avais empiré",
      "Tu": "avais empiré",
      "Il/Elle/On": "avait empiré",
      "Nous": "avions empiré",
      "Vous": "aviez empiré",
      "Ils/Elle": "avaient empiré"
    },
    "Futur Simple": {
      "Je": "empirerai",
      "Tu": "empireras",
      "Il/Elle/On": "empirera",
      "Nous": "empirerons",
      "Vous": "empirerez",
      "Ils/Elle": "empireront"
    },
    "Futur Antérieur": {
      "Je": "aurai empiré",
      "Tu": "auras empiré",
      "Il/Elle/On": "aura empiré",
      "Nous": "aurons empiré",
      "Vous": "aurez empiré",
      "Ils/Elle": "auront empiré"
    },
    "Conditionnel Présent": {
      "Je": "empirerais",
      "Tu": "empirerais",
      "Il/Elle/On": "empirerait",
      "Nous": "empirerions",
      "Vous": "empireriez",
      "Ils/Elle": "empireraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais empiré",
      "Tu": "aurais empiré",
      "Il/Elle/On": "aurait empiré",
      "Nous": "aurions empiré",
      "Vous": "auriez empiré",
      "Ils/Elle": "auraient empiré"
    },
    "Subjonctif Présent": {
      "Je": "empire",
      "Tu": "empire",
      "Il/Elle/On": "empire",
      "Nous": "empirions",
      "Vous": "empiriez",
      "Ils/Elle": "empirent"
    },
    "Subjonctif Passé": {
      "Je": "aie empiré",
      "Tu": "aies empiré",
      "Il/Elle/On": "ait empiré",
      "Nous": "ayons empiré",
      "Vous": "ayez empiré",
      "Ils/Elle": "aient empiré"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse empiré",
      "Tu": "eusses empiré",
      "Il/Elle/On": "eût empiré",
      "Nous": "eussions empiré",
      "Vous": "eussiez empiré",
      "Ils/Elle": "eussent empiré"
    },
    "Subjonctif Imparfait": {
      "Je": "empirasse",
      "Tu": "empirasses",
      "Il/Elle/On": "empirât",
      "Nous": "empirassions",
      "Vous": "empirassiez",
      "Ils/Elle": "empirassent"
    },
    "Impératif Présent": {
      "Tu": "empire",
      "Nous": "empirons",
      "Vous": "empirez"
    },
    "Impératif Passé": {
      "Tu": "aie empiré",
      "Nous": "ayons empiré",
      "Vous": "ayez empiré"
    },
    "Infinitif Présent": "empirer",
    "Infinitif Passé": "avoir empiré",
    "Participe Présent": "empirant",
    "Participe Passé": "empiré",
    "Gérondif Présent": "en empirant",
    "Gérondif Passé": "en ayant empiré"
  },
  "enchérir": {
    "Présent": {
      "Je": "enchéris",
      "Tu": "enchéris",
      "Il/Elle/On": "enchérit",
      "Nous": "enchérissons",
      "Vous": "enchérissez",
      "Ils/Elle": "enchérissent"
    },
    "Imparfait": {
      "Je": "enchérissais",
      "Tu": "enchérissais",
      "Il/Elle/On": "enchérissait",
      "Nous": "enchérissions",
      "Vous": "enchérissiez",
      "Ils/Elle": "enchérissaient"
    },
    "Passé Composé": {
      "Je": "ai enchéri",
      "Tu": "as enchéri",
      "Il/Elle/On": "a enchéri",
      "Nous": "avons enchéri",
      "Vous": "avez enchéri",
      "Ils/Elle": "ont enchéri"
    },
    "Futur": {
      "Je": "enchérirai",
      "Tu": "enchériras",
      "Il/Elle/On": "enchérira",
      "Nous": "enchérirons",
      "Vous": "enchérirez",
      "Ils/Elle": "enchériront"
    },
    "Plus-que-parfait": {
      "Je": "avais enchéri",
      "Tu": "avais enchéri",
      "Il/Elle/On": "avait enchéri",
      "Nous": "avions enchéri",
      "Vous": "aviez enchéri",
      "Ils/Elle": "avaient enchéri"
    },
    "Futur Simple": {
      "Je": "enchérirai",
      "Tu": "enchériras",
      "Il/Elle/On": "enchérira",
      "Nous": "enchérirons",
      "Vous": "enchérirez",
      "Ils/Elle": "enchériront"
    },
    "Futur Antérieur": {
      "Je": "aurai enchéri",
      "Tu": "auras enchéri",
      "Il/Elle/On": "aura enchéri",
      "Nous": "aurons enchéri",
      "Vous": "aurez enchéri",
      "Ils/Elle": "auront enchéri"
    },
    "Conditionnel Présent": {
      "Je": "enchérirais",
      "Tu": "enchérirais",
      "Il/Elle/On": "enchérirait",
      "Nous": "enchéririons",
      "Vous": "enchéririez",
      "Ils/Elle": "enchériraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais enchéri",
      "Tu": "aurais enchéri",
      "Il/Elle/On": "aurait enchéri",
      "Nous": "aurions enchéri",
      "Vous": "auriez enchéri",
      "Ils/Elle": "auraient enchéri"
    },
    "Subjonctif Présent": {
      "Je": "enchérisse",
      "Tu": "enchérisses",
      "Il/Elle/On": "enchérisse",
      "Nous": "enchérissions",
      "Vous": "enchérissiez",
      "Ils/Elle": "enchérissent"
    },
    "Subjonctif Passé": {
      "Je": "aie enchéri",
      "Tu": "aies enchéri",
      "Il/Elle/On": "ait enchéri",
      "Nous": "ayons enchéri",
      "Vous": "ayez enchéri",
      "Ils/Elle": "aient enchéri"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse enchéri",
      "Tu": "eusses enchéri",
      "Il/Elle/On": "eût enchéri",
      "Nous": "eussions enchéri",
      "Vous": "eussiez enchéri",
      "Ils/Elle": "eussent enchéri"
    },
    "Subjonctif Imparfait": {
      "Je": "enchérissse",
      "Tu": "enchérisses",
      "Il/Elle/On": "enchérît",
      "Nous": "enchérissions",
      "Vous": "enchérissiez",
      "Ils/Elle": "enchérissent"
    },
    "Impératif Présent": {
      "Tu": "enchéris",
      "Nous": "enchérissons",
      "Vous": "enchérissez"
    },
    "Impératif Passé": {
      "Tu": "aie enchéri",
      "Nous": "ayons enchéri",
      "Vous": "ayez enchéri"
    },
    "Infinitif Présent": "enchérir",
    "Infinitif Passé": "avoir enchéri",
    "Participe Présent": "enchérissant",
    "Participe Passé": "enchéri",
    "Gérondif Présent": "en enchérissant",
    "Gérondif Passé": "en ayant enchéri"
  },
  "enlaidir": {
    "Présent": {
      "Je": "enlaidis",
      "Tu": "enlaidis",
      "Il/Elle/On": "enlaidit",
      "Nous": "enlaidissons",
      "Vous": "enlaidissez",
      "Ils/Elle": "enlaidissent"
    },
    "Imparfait": {
      "Je": "enlaidissais",
      "Tu": "enlaidissais",
      "Il/Elle/On": "enlaidissait",
      "Nous": "enlaidissions",
      "Vous": "enlaidissiez",
      "Ils/Elle": "enlaidissaient"
    },
    "Passé Composé": {
      "Je": "ai enlaidi",
      "Tu": "as enlaidi",
      "Il/Elle/On": "a enlaidi",
      "Nous": "avons enlaidi",
      "Vous": "avez enlaidi",
      "Ils/Elle": "ont enlaidi"
    },
    "Futur": {
      "Je": "enlaidirai",
      "Tu": "enlaidiras",
      "Il/Elle/On": "enlaidira",
      "Nous": "enlaidirons",
      "Vous": "enlaidirez",
      "Ils/Elle": "enlaidiront"
    },
    "Plus-que-parfait": {
      "Je": "avais enlaidi",
      "Tu": "avais enlaidi",
      "Il/Elle/On": "avait enlaidi",
      "Nous": "avions enlaidi",
      "Vous": "aviez enlaidi",
      "Ils/Elle": "avaient enlaidi"
    },
    "Futur Simple": {
      "Je": "enlaidirai",
      "Tu": "enlaidiras",
      "Il/Elle/On": "enlaidira",
      "Nous": "enlaidirons",
      "Vous": "enlaidirez",
      "Ils/Elle": "enlaidiront"
    },
    "Futur Antérieur": {
      "Je": "aurai enlaidi",
      "Tu": "auras enlaidi",
      "Il/Elle/On": "aura enlaidi",
      "Nous": "aurons enlaidi",
      "Vous": "aurez enlaidi",
      "Ils/Elle": "auront enlaidi"
    },
    "Conditionnel Présent": {
      "Je": "enlaidirais",
      "Tu": "enlaidirais",
      "Il/Elle/On": "enlaidirait",
      "Nous": "enlaidirions",
      "Vous": "enlaidiriez",
      "Ils/Elle": "enlaidiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais enlaidi",
      "Tu": "aurais enlaidi",
      "Il/Elle/On": "aurait enlaidi",
      "Nous": "aurions enlaidi",
      "Vous": "auriez enlaidi",
      "Ils/Elle": "auraient enlaidi"
    },
    "Subjonctif Présent": {
      "Je": "enlaidisse",
      "Tu": "enlaidisses",
      "Il/Elle/On": "enlaidisse",
      "Nous": "enlaidissions",
      "Vous": "enlaidissiez",
      "Ils/Elle": "enlaidissent"
    },
    "Subjonctif Passé": {
      "Je": "aie enlaidi",
      "Tu": "aies enlaidi",
      "Il/Elle/On": "ait enlaidi",
      "Nous": "ayons enlaidi",
      "Vous": "ayez enlaidi",
      "Ils/Elle": "aient enlaidi"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse enlaidi",
      "Tu": "eusses enlaidi",
      "Il/Elle/On": "eût enlaidi",
      "Nous": "eussions enlaidi",
      "Vous": "eussiez enlaidi",
      "Ils/Elle": "eussent enlaidi"
    },
    "Subjonctif Imparfait": {
      "Je": "enlaidisse",
      "Tu": "enlaidisses",
      "Il/Elle/On": "enlaidît",
      "Nous": "enlaidissions",
      "Vous": "enlaidissiez",
      "Ils/Elle": "enlaidissent"
    },
    "Impératif Présent": {
      "Tu": "enlaidis",
      "Nous": "enlaidissons",
      "Vous": "enlaidissez"
    },
    "Impératif Passé": {
      "Tu": "aie enlaidi",
      "Nous": "ayons enlaidi",
      "Vous": "ayez enlaidi"
    },
    "Infinitif Présent": "enlaidir",
    "Infinitif Passé": "avoir enlaidi",
    "Participe Présent": "enlaidissant",
    "Participe Passé": "enlaidi",
    "Gérondif Présent": "en enlaidissant",
    "Gérondif Passé": "en ayant enlaidi"
  },
  "entrer": {
    "Présent": {
      "Je": "entre",
      "Tu": "entres",
      "Il/Elle/On": "entre",
      "Nous": "entrons",
      "Vous": "entrez",
      "Ils/Elle": "entrent"
    },
    "Imparfait": {
      "Je": "entrais",
      "Tu": "entrais",
      "Il/Elle/On": "entrait",
      "Nous": "entrions",
      "Vous": "entriez",
      "Ils/Elle": "entraient"
    },
    "Passé Composé": {
      "Je": "suis entré(e)",
      "Tu": "es entré(e)",
      "Il/Elle/On": "est entré(e)",
      "Nous": "sommes entré(e)s",
      "Vous": "êtes entré(e)(s)",
      "Ils/Elle": "sont entrés(es)"
    },
    "Futur": {
      "Je": "entrerai",
      "Tu": "entreras",
      "Il/Elle/On": "entrera",
      "Nous": "entrerons",
      "Vous": "entrerez",
      "Ils/Elle": "entreront"
    },
    "Plus-que-parfait": {
      "Je": "étais entré(e)",
      "Tu": "étais entré(e)",
      "Il/Elle/On": "était entré(e)",
      "Nous": "étions entré(e)s",
      "Vous": "étiez entré(e)(s)",
      "Ils/Elle": "étaient entrés(es)"
    },
    "Futur Simple": {
      "Je": "entrerai",
      "Tu": "entreras",
      "Il/Elle/On": "entrera",
      "Nous": "entrerons",
      "Vous": "entrerez",
      "Ils/Elle": "entreront"
    },
    "Futur Antérieur": {
      "Je": "serai entré(e)",
      "Tu": "seras entré(e)",
      "Il/Elle/On": "sera entré(e)",
      "Nous": "serons entré(e)s",
      "Vous": "serez entré(e)(s)",
      "Ils/Elle": "seront entrés(es)"
    },
    "Conditionnel Présent": {
      "Je": "entrerais",
      "Tu": "entrerais",
      "Il/Elle/On": "entrerait",
      "Nous": "entrerions",
      "Vous": "entreriez",
      "Ils/Elle": "entreraient"
    },
    "Conditionnel Passé": {
      "Je": "serais entré(e)",
      "Tu": "serais entré(e)",
      "Il/Elle/On": "serait entré(e)",
      "Nous": "serions entré(e)s",
      "Vous": "seriez entré(e)(s)",
      "Ils/Elle": "seraient entrés(es)"
    },
    "Subjonctif Présent": {
      "Je": "entre",
      "Tu": "entres",
      "Il/Elle/On": "entre",
      "Nous": "entrions",
      "Vous": "entriez",
      "Ils/Elle": "entrent"
    },
    "Subjonctif Passé": {
      "Je": "sois entré(e)",
      "Tu": "sois entré(e)",
      "Il/Elle/On": "soit entré(e)",
      "Nous": "soyons entré(e)s",
      "Vous": "soyez entré(e)(s)",
      "Ils/Elle": "soient entrés(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse entré(e)",
      "Tu": "fusses entré(e)",
      "Il/Elle/On": "fût entré(e)",
      "Nous": "fussions entré(e)s",
      "Vous": "fussiez entré(e)(s)",
      "Ils/Elle": "fussent entrés(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "entrasse",
      "Tu": "entrasses",
      "Il/Elle/On": "entrât",
      "Nous": "entrassions",
      "Vous": "entrassiez",
      "Ils/Elle": "entrassent"
    },
    "Impératif Présent": {
      "Tu": "entre",
      "Nous": "entrons",
      "Vous": "entrez"
    },
    "Impératif Passé": {
      "Tu": "sois entré(e)",
      "Nous": "soyons entré(e)s",
      "Vous": "soyez entré(e)(s)"
    },
    "Infinitif Présent": "entrer",
    "Infinitif Passé": "être entré(e)",
    "Participe Présent": "entrant",
    "Participe Passé": "entré(e)",
    "Gérondif Présent": "en entrant",
    "Gérondif Passé": "en étant entré(e)"
  },
  "rentrer": {
    "Présent": {
      "Je": "rentre",
      "Tu": "rentres",
      "Il/Elle/On": "rentre",
      "Nous": "rentrons",
      "Vous": "rentrez",
      "Ils/Elle": "rentrent"
    },
    "Imparfait": {
      "Je": "rentrais",
      "Tu": "rentrais",
      "Il/Elle/On": "rentrait",
      "Nous": "rentrions",
      "Vous": "rentriez",
      "Ils/Elle": "rentraient"
    },
    "Passé Composé": {
      "Je": "suis rentré(e)",
      "Tu": "es rentré(e)",
      "Il/Elle/On": "est rentré(e)",
      "Nous": "sommes rentré(e)s",
      "Vous": "êtes rentré(e)(s)",
      "Ils/Elle": "sont rentrés(es)"
    },
    "Futur": {
      "Je": "rentrerai",
      "Tu": "rentreras",
      "Il/Elle/On": "rentrera",
      "Nous": "rentrerons",
      "Vous": "rentrerez",
      "Ils/Elle": "rentreront"
    },
    "Plus-que-parfait": {
      "Je": "étais rentré(e)",
      "Tu": "étais rentré(e)",
      "Il/Elle/On": "était rentré(e)",
      "Nous": "étions rentré(e)s",
      "Vous": "étiez rentré(e)(s)",
      "Ils/Elle": "étaient rentrés(es)"
    },
    "Futur Simple": {
      "Je": "rentrerai",
      "Tu": "rentreras",
      "Il/Elle/On": "rentrera",
      "Nous": "rentrerons",
      "Vous": "rentrerez",
      "Ils/Elle": "rentreront"
    },
    "Futur Antérieur": {
      "Je": "serai rentré(e)",
      "Tu": "seras rentré(e)",
      "Il/Elle/On": "sera rentré(e)",
      "Nous": "serons rentré(e)s",
      "Vous": "serez rentré(e)(s)",
      "Ils/Elle": "seront rentrés(es)"
    },
    "Conditionnel Présent": {
      "Je": "rentrerais",
      "Tu": "rentrerais",
      "Il/Elle/On": "rentrerait",
      "Nous": "rentrerions",
      "Vous": "rentreriez",
      "Ils/Elle": "rentreraient"
    },
    "Conditionnel Passé": {
      "Je": "serais rentré(e)",
      "Tu": "serais rentré(e)",
      "Il/Elle/On": "serait rentré(e)",
      "Nous": "serions rentré(e)s",
      "Vous": "seriez rentré(e)(s)",
      "Ils/Elle": "seraient rentrés(es)"
    },
    "Subjonctif Présent": {
      "Je": "rentre",
      "Tu": "rentres",
      "Il/Elle/On": "rentre",
      "Nous": "rentrions",
      "Vous": "rentriez",
      "Ils/Elle": "rentrent"
    },
    "Subjonctif Passé": {
      "Je": "sois rentré(e)",
      "Tu": "sois rentré(e)",
      "Il/Elle/On": "soit rentré(e)",
      "Nous": "soyons rentré(e)s",
      "Vous": "soyez rentré(e)(s)",
      "Ils/Elle": "soient rentrés(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse rentré(e)",
      "Tu": "fusses rentré(e)",
      "Il/Elle/On": "fût rentré(e)",
      "Nous": "fussions rentré(e)s",
      "Vous": "fussiez rentré(e)(s)",
      "Ils/Elle": "fussent rentrés(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "rentrasse",
      "Tu": "rentrasses",
      "Il/Elle/On": "rentrât",
      "Nous": "rentrassions",
      "Vous": "rentrassiez",
      "Ils/Elle": "rentrassent"
    },
    "Impératif Présent": {
      "Tu": "rentre",
      "Nous": "rentrons",
      "Vous": "rentrez"
    },
    "Impératif Passé": {
      "Tu": "sois rentré(e)",
      "Nous": "soyons rentré(e)s",
      "Vous": "soyez rentré(e)(s)"
    },
    "Infinitif Présent": "rentrer",
    "Infinitif Passé": "être rentré(e)",
    "Participe Présent": "rentrant",
    "Participe Passé": "rentré(e)",
    "Gérondif Présent": "en rentrant",
    "Gérondif Passé": "en étant rentré(e)"
  },
  "déborder": {
    "Présent": {
      "Je": "déborde",
      "Tu": "débordes",
      "Il/Elle/On": "déborde",
      "Nous": "débordons",
      "Vous": "débordez",
      "Ils/Elle": "débordent"
    },
    "Imparfait": {
      "Je": "débordais",
      "Tu": "débordais",
      "Il/Elle/On": "débordait",
      "Nous": "débordions",
      "Vous": "débordiez",
      "Ils/Elle": "débordaient"
    },
    "Passé Composé": {
      "Je": "ai débordé",
      "Tu": "as débordé",
      "Il/Elle/On": "a débordé",
      "Nous": "avons débordé",
      "Vous": "avez débordé",
      "Ils/Elle": "ont débordé"
    },
    "Futur": {
      "Je": "déborderai",
      "Tu": "déborderas",
      "Il/Elle/On": "débordera",
      "Nous": "déborderons",
      "Vous": "déborderez",
      "Ils/Elle": "déborderont"
    },
    "Plus-que-parfait": {
      "Je": "avais débordé",
      "Tu": "avais débordé",
      "Il/Elle/On": "avait débordé",
      "Nous": "avions débordé",
      "Vous": "aviez débordé",
      "Ils/Elle": "avaient débordé"
    },
    "Futur Simple": {
      "Je": "déborderai",
      "Tu": "déborderas",
      "Il/Elle/On": "débordera",
      "Nous": "déborderons",
      "Vous": "déborderez",
      "Ils/Elle": "déborderont"
    },
    "Futur Antérieur": {
      "Je": "aurai débordé",
      "Tu": "auras débordé",
      "Il/Elle/On": "aura débordé",
      "Nous": "aurons débordé",
      "Vous": "aurez débordé",
      "Ils/Elle": "auront débordé"
    },
    "Conditionnel Présent": {
      "Je": "déborderais",
      "Tu": "déborderais",
      "Il/Elle/On": "déborderait",
      "Nous": "déborderions",
      "Vous": "déborderiez",
      "Ils/Elle": "déborderaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais débordé",
      "Tu": "aurais débordé",
      "Il/Elle/On": "aurait débordé",
      "Nous": "aurions débordé",
      "Vous": "auriez débordé",
      "Ils/Elle": "auraient débordé"
    },
    "Subjonctif Présent": {
      "Je": "déborde",
      "Tu": "débordes",
      "Il/Elle/On": "déborde",
      "Nous": "débordions",
      "Vous": "débordiez",
      "Ils/Elle": "débordent"
    },
    "Subjonctif Passé": {
      "Je": "aie débordé",
      "Tu": "aies débordé",
      "Il/Elle/On": "ait débordé",
      "Nous": "ayons débordé",
      "Vous": "ayez débordé",
      "Ils/Elle": "aient débordé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse débordé",
      "Tu": "eusses débordé",
      "Il/Elle/On": "eût débordé",
      "Nous": "eussions débordé",
      "Vous": "eussiez débordé",
      "Ils/Elle": "eussent débordé"
    },
    "Subjonctif Imparfait": {
      "Je": "débordasse",
      "Tu": "débordasses",
      "Il/Elle/On": "débordât",
      "Nous": "débordassions",
      "Vous": "débordassiez",
      "Ils/Elle": "débordassent"
    },
    "Impératif Présent": {
      "Tu": "déborde",
      "Nous": "débordons",
      "Vous": "débordez"
    },
    "Impératif Passé": {
      "Tu": "aie débordé",
      "Nous": "ayons débordé",
      "Vous": "ayez débordé"
    },
    "Infinitif Présent": "déborder",
    "Infinitif Passé": "avoir débordé",
    "Participe Présent": "débordant",
    "Participe Passé": "débordé",
    "Gérondif Présent": "en débordant",
    "Gérondif Passé": "en ayant débordé"
},
"expirer": {
    "Présent": {
      "Je": "expire",
      "Tu": "expires",
      "Il/Elle/On": "expire",
      "Nous": "expirons",
      "Vous": "expirez",
      "Ils/Elle": "expirent"
    },
    "Imparfait": {
      "Je": "expirais",
      "Tu": "expirais",
      "Il/Elle/On": "expirait",
      "Nous": "expirions",
      "Vous": "expiriez",
      "Ils/Elle": "expiraient"
    },
    "Passé Composé": {
      "Je": "ai expiré",
      "Tu": "as expiré",
      "Il/Elle/On": "a expiré",
      "Nous": "avons expiré",
      "Vous": "avez expiré",
      "Ils/Elle": "ont expiré"
    },
    "Futur": {
      "Je": "expirerai",
      "Tu": "expireras",
      "Il/Elle/On": "expirera",
      "Nous": "expirerons",
      "Vous": "expirerez",
      "Ils/Elle": "expireront"
    },
    "Plus-que-parfait": {
      "Je": "avais expiré",
      "Tu": "avais expiré",
      "Il/Elle/On": "avait expiré",
      "Nous": "avions expiré",
      "Vous": "aviez expiré",
      "Ils/Elle": "avaient expiré"
    },
    "Futur Simple": {
      "Je": "expirerai",
      "Tu": "expireras",
      "Il/Elle/On": "expirera",
      "Nous": "expirerons",
      "Vous": "expirerez",
      "Ils/Elle": "expireront"
    },
    "Futur Antérieur": {
      "Je": "aurai expiré",
      "Tu": "auras expiré",
      "Il/Elle/On": "aura expiré",
      "Nous": "aurons expiré",
      "Vous": "aurez expiré",
      "Ils/Elle": "auront expiré"
    },
    "Conditionnel Présent": {
      "Je": "expirerais",
      "Tu": "expirerais",
      "Il/Elle/On": "expirerait",
      "Nous": "expirerions",
      "Vous": "expireriez",
      "Ils/Elle": "expireraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais expiré",
      "Tu": "aurais expiré",
      "Il/Elle/On": "aurait expiré",
      "Nous": "aurions expiré",
      "Vous": "auriez expiré",
      "Ils/Elle": "auraient expiré"
    },
    "Subjonctif Présent": {
      "Je": "expire",
      "Tu": "expires",
      "Il/Elle/On": "expire",
      "Nous": "expirions",
      "Vous": "expiriez",
      "Ils/Elle": "expirent"
    },
    "Subjonctif Passé": {
      "Je": "aie expiré",
      "Tu": "aies expiré",
      "Il/Elle/On": "ait expiré",
      "Nous": "ayons expiré",
      "Vous": "ayez expiré",
      "Ils/Elle": "aient expiré"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse expiré",
      "Tu": "eusses expiré",
      "Il/Elle/On": "eût expiré",
      "Nous": "eussions expiré",
      "Vous": "eussiez expiré",
      "Ils/Elle": "eussent expiré"
    },
    "Subjonctif Imparfait": {
      "Je": "expirasse",
      "Tu": "expirasses",
      "Il/Elle/On": "expirât",
      "Nous": "expirassions",
      "Vous": "expirassiez",
      "Ils/Elle": "expirassent"
    },
    "Impératif Présent": {
      "Tu": "expire",
      "Nous": "expirons",
      "Vous": "expirez"
    },
    "Impératif Passé": {
      "Tu": "ai expiré",
      "Nous": "ayons expiré",
      "Vous": "ayez expiré"
    },
    "Infinitif Présent": "expirer",
    "Infinitif Passé": "avoir expiré",
    "Participe Présent": "expirant",
    "Participe Passé": "expiré",
    "Gérondif Présent": "en expirant",
    "Gérondif Passé": "en ayant expiré"
  },
  "failir": {
    "Présent": {
      "Je": "faille",
      "Tu": "failles",
      "Il/Elle/On": "faille",
      "Nous": "faillons",
      "Vous": "failliez",
      "Ils/Elle": "faillent"
    },
    "Imparfait": {
      "Je": "faillais",
      "Tu": "faillais",
      "Il/Elle/On": "faillait",
      "Nous": "faillions",
      "Vous": "failliez",
      "Ils/Elle": "faillaient"
    },
    "Passé Composé": {
      "Je": "ai failli",
      "Tu": "as failli",
      "Il/Elle/On": "a failli",
      "Nous": "avons failli",
      "Vous": "avez failli",
      "Ils/Elle": "ont failli"
    },
    "Futur": {
      "Je": "faillirai",
      "Tu": "failliras",
      "Il/Elle/On": "faillira",
      "Nous": "faillirons",
      "Vous": "faillirez",
      "Ils/Elle": "failliront"
    },
    "Plus-que-parfait": {
      "Je": "avais failli",
      "Tu": "avais failli",
      "Il/Elle/On": "avait failli",
      "Nous": "avions failli",
      "Vous": "aviez failli",
      "Ils/Elle": "avaient failli"
    },
    "Futur Simple": {
      "Je": "faillirai",
      "Tu": "failliras",
      "Il/Elle/On": "faillira",
      "Nous": "faillirons",
      "Vous": "faillirez",
      "Ils/Elle": "failliront"
    },
    "Futur Antérieur": {
      "Je": "aurai failli",
      "Tu": "auras failli",
      "Il/Elle/On": "aura failli",
      "Nous": "aurons failli",
      "Vous": "aurez failli",
      "Ils/Elle": "auront failli"
    },
    "Conditionnel Présent": {
      "Je": "faillirais",
      "Tu": "faillirais",
      "Il/Elle/On": "faillirait",
      "Nous": "faillirions",
      "Vous": "failliriez",
      "Ils/Elle": "failliraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais failli",
      "Tu": "aurais failli",
      "Il/Elle/On": "aurait failli",
      "Nous": "aurions failli",
      "Vous": "auriez failli",
      "Ils/Elle": "auraient failli"
    },
    "Subjonctif Présent": {
      "Je": "faille",
      "Tu": "failles",
      "Il/Elle/On": "faille",
      "Nous": "faillions",
      "Vous": "failliez",
      "Ils/Elle": "faillent"
    },
    "Subjonctif Passé": {
      "Je": "aie failli",
      "Tu": "aies failli",
      "Il/Elle/On": "ait failli",
      "Nous": "ayons failli",
      "Vous": "ayez failli",
      "Ils/Elle": "aient failli"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse failli",
      "Tu": "eusses failli",
      "Il/Elle/On": "eût failli",
      "Nous": "eussions failli",
      "Vous": "eussiez failli",
      "Ils/Elle": "eussent failli"
    },
    "Subjonctif Imparfait": {
      "Je": "faillisse",
      "Tu": "faillisses",
      "Il/Elle/On": "faillît",
      "Nous": "faillissions",
      "Vous": "faillissiez",
      "Ils/Elle": "faillissent"
    },
    "Impératif Présent": {
      "Tu": "faille",
      "Nous": "faillons",
      "Vous": "failliez"
    },
    "Impératif Passé": {
      "Tu": "ai failli",
      "Nous": "ayons failli",
      "Vous": "ayez failli"
    },
    "Infinitif Présent": "faillir",
    "Infinitif Passé": "avoir failli",
    "Participe Présent": "faillant",
    "Participe Passé": "failli",
    "Gérondif Présent": "en faillant",
    "Gérondif Passé": "en ayant failli"
  },
  "grandir": {
    "Présent": {
      "Je": "grandis",
      "Tu": "grandis",
      "Il/Elle/On": "grandit",
      "Nous": "grandissons",
      "Vous": "grandissez",
      "Ils/Elle": "grandissent"
    },
    "Imparfait": {
      "Je": "grandissais",
      "Tu": "grandissais",
      "Il/Elle/On": "grandissait",
      "Nous": "grandissions",
      "Vous": "grandissiez",
      "Ils/Elle": "grandissaient"
    },
    "Passé Composé": {
      "Je": "ai grandi",
      "Tu": "as grandi",
      "Il/Elle/On": "a grandi",
      "Nous": "avons grandi",
      "Vous": "avez grandi",
      "Ils/Elle": "ont grandi"
    },
    "Futur": {
      "Je": "grandirai",
      "Tu": "grandiras",
      "Il/Elle/On": "grandira",
      "Nous": "grandirons",
      "Vous": "grandirez",
      "Ils/Elle": "grandiront"
    },
    "Plus-que-parfait": {
      "Je": "avais grandi",
      "Tu": "avais grandi",
      "Il/Elle/On": "avait grandi",
      "Nous": "avions grandi",
      "Vous": "aviez grandi",
      "Ils/Elle": "avaient grandi"
    },
    "Futur Simple": {
      "Je": "grandirai",
      "Tu": "grandiras",
      "Il/Elle/On": "grandira",
      "Nous": "grandirons",
      "Vous": "grandirez",
      "Ils/Elle": "grandiront"
    },
    "Futur Antérieur": {
      "Je": "aurai grandi",
      "Tu": "auras grandi",
      "Il/Elle/On": "aura grandi",
      "Nous": "aurons grandi",
      "Vous": "aurez grandi",
      "Ils/Elle": "auront grandi"
    },
    "Conditionnel Présent": {
      "Je": "grandirais",
      "Tu": "grandirais",
      "Il/Elle/On": "grandirait",
      "Nous": "grandirions",
      "Vous": "grandiriez",
      "Ils/Elle": "grandiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais grandi",
      "Tu": "aurais grandi",
      "Il/Elle/On": "aurait grandi",
      "Nous": "aurions grandi",
      "Vous": "auriez grandi",
      "Ils/Elle": "auraient grandi"
    },
    "Subjonctif Présent": {
      "Je": "grandisse",
      "Tu": "grandisses",
      "Il/Elle/On": "grandisse",
      "Nous": "grandissions",
      "Vous": "grandissiez",
      "Ils/Elle": "grandissent"
    },
    "Subjonctif Passé": {
      "Je": "aie grandi",
      "Tu": "aies grandi",
      "Il/Elle/On": "ait grandi",
      "Nous": "ayons grandi",
      "Vous": "ayez grandi",
      "Ils/Elle": "aient grandi"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse grandi",
      "Tu": "eusses grandi",
      "Il/Elle/On": "eût grandi",
      "Nous": "eussions grandi",
      "Vous": "eussiez grandi",
      "Ils/Elle": "eussent grandi"
    },
    "Subjonctif Imparfait": {
      "Je": "grandisse",
      "Tu": "grandisses",
      "Il/Elle/On": "grandît",
      "Nous": "grandissions",
      "Vous": "grandissiez",
      "Ils/Elle": "grandissent"
    },
    "Impératif Présent": {
      "Tu": "grandis",
      "Nous": "grandissons",
      "Vous": "grandissez"
    },
    "Impératif Passé": {
      "Tu": "ai grandi",
      "Nous": "ayons grandi",
      "Vous": "ayez grandi"
    },
    "Infinitif Présent": "grandir",
    "Infinitif Passé": "avoir grandi",
    "Participe Présent": "grandissant",
    "Participe Passé": "grandi",
    "Gérondif Présent": "en grandissant",
    "Gérondif Passé": "en ayant grandi"
  },
  "grossir": {
    "Présent": {
      "Je": "grossis",
      "Tu": "grossis",
      "Il/Elle/On": "grossit",
      "Nous": "grossissons",
      "Vous": "grossissez",
      "Ils/Elle": "grossissent"
    },
    "Imparfait": {
      "Je": "grossissais",
      "Tu": "grossissais",
      "Il/Elle/On": "grossissait",
      "Nous": "grossissions",
      "Vous": "grossissiez",
      "Ils/Elle": "grossissaient"
    },
    "Passé Composé": {
      "Je": "ai grossi",
      "Tu": "as grossi",
      "Il/Elle/On": "a grossi",
      "Nous": "avons grossi",
      "Vous": "avez grossi",
      "Ils/Elle": "ont grossi"
    },
    "Futur": {
      "Je": "grossirai",
      "Tu": "grossiras",
      "Il/Elle/On": "grossira",
      "Nous": "grossirons",
      "Vous": "grossirez",
      "Ils/Elle": "grossiront"
    },
    "Plus-que-parfait": {
      "Je": "avais grossi",
      "Tu": "avais grossi",
      "Il/Elle/On": "avait grossi",
      "Nous": "avions grossi",
      "Vous": "aviez grossi",
      "Ils/Elle": "avaient grossi"
    },
    "Futur Simple": {
      "Je": "grossirai",
      "Tu": "grossiras",
      "Il/Elle/On": "grossira",
      "Nous": "grossirons",
      "Vous": "grossirez",
      "Ils/Elle": "grossiront"
    },
    "Futur Antérieur": {
      "Je": "aurai grossi",
      "Tu": "auras grossi",
      "Il/Elle/On": "aura grossi",
      "Nous": "aurons grossi",
      "Vous": "aurez grossi",
      "Ils/Elle": "auront grossi"
    },
    "Conditionnel Présent": {
      "Je": "grossirais",
      "Tu": "grossirais",
      "Il/Elle/On": "grossirait",
      "Nous": "grossirions",
      "Vous": "grossiriez",
      "Ils/Elle": "grossiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais grossi",
      "Tu": "aurais grossi",
      "Il/Elle/On": "aurait grossi",
      "Nous": "aurions grossi",
      "Vous": "auriez grossi",
      "Ils/Elle": "auraient grossi"
    },
    "Subjonctif Présent": {
      "Je": "grossisse",
      "Tu": "grossisses",
      "Il/Elle/On": "grossisse",
      "Nous": "grossissions",
      "Vous": "grossissiez",
      "Ils/Elle": "grossissent"
    },
    "Subjonctif Passé": {
      "Je": "aie grossi",
      "Tu": "aies grossi",
      "Il/Elle/On": "ait grossi",
      "Nous": "ayons grossi",
      "Vous": "ayez grossi",
      "Ils/Elle": "aient grossi"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse grossi",
      "Tu": "eusses grossi",
      "Il/Elle/On": "eût grossi",
      "Nous": "eussions grossi",
      "Vous": "eussiez grossi",
      "Ils/Elle": "eussent grossi"
    },
    "Subjonctif Imparfait": {
      "Je": "grossisse",
      "Tu": "grossisses",
      "Il/Elle/On": "grossît",
      "Nous": "grossissions",
      "Vous": "grossissiez",
      "Ils/Elle": "grossissent"
    },
    "Impératif Présent": {
      "Tu": "grossis",
      "Nous": "grossissons",
      "Vous": "grossissez"
    },
    "Impératif Passé": {
      "Tu": "ai grossi",
      "Nous": "ayons grossi",
      "Vous": "ayez grossi"
    },
    "Infinitif Présent": "grossir",
    "Infinitif Passé": "avoir grossi",
    "Participe Présent": "grossissant",
    "Participe Passé": "grossi",
    "Gérondif Présent": "en grossissant",
    "Gérondif Passé": "en ayant grossi"
  },
  "jailir": {
    "Présent": {
      "Je": "jaille",
      "Tu": "jailles",
      "Il/Elle/On": "jaille",
      "Nous": "jaillissons",
      "Vous": "jaillez",
      "Ils/Elle": "jaillent"
    },
    "Imparfait": {
      "Je": "jaillissais",
      "Tu": "jaillissais",
      "Il/Elle/On": "jaillissait",
      "Nous": "jaillissions",
      "Vous": "jaillissiez",
      "Ils/Elle": "jaillissaient"
    },
    "Passé Composé": {
      "Je": "ai jailli",
      "Tu": "as jailli",
      "Il/Elle/On": "a jailli",
      "Nous": "avons jailli",
      "Vous": "avez jailli",
      "Ils/Elle": "ont jailli"
    },
    "Futur": {
      "Je": "jaillirai",
      "Tu": "jailliras",
      "Il/Elle/On": "jaillira",
      "Nous": "jaillirons",
      "Vous": "jaillirez",
      "Ils/Elle": "jailliront"
    },
    "Plus-que-parfait": {
      "Je": "avais jailli",
      "Tu": "avais jailli",
      "Il/Elle/On": "avait jailli",
      "Nous": "avions jailli",
      "Vous": "aviez jailli",
      "Ils/Elle": "avaient jailli"
    },
    "Futur Simple": {
      "Je": "jaillirai",
      "Tu": "jailliras",
      "Il/Elle/On": "jaillira",
      "Nous": "jaillirons",
      "Vous": "jaillirez",
      "Ils/Elle": "jailliront"
    },
    "Futur Antérieur": {
      "Je": "aurai jailli",
      "Tu": "auras jailli",
      "Il/Elle/On": "aura jailli",
      "Nous": "aurons jailli",
      "Vous": "aurez jailli",
      "Ils/Elle": "auront jailli"
    },
    "Conditionnel Présent": {
      "Je": "jaillirais",
      "Tu": "jaillirais",
      "Il/Elle/On": "jaillirait",
      "Nous": "jaillirions",
      "Vous": "jailliriez",
      "Ils/Elle": "jailliraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais jailli",
      "Tu": "aurais jailli",
      "Il/Elle/On": "aurait jailli",
      "Nous": "aurions jailli",
      "Vous": "auriez jailli",
      "Ils/Elle": "auraient jailli"
    },
    "Subjonctif Présent": {
      "Je": "jaille",
      "Tu": "jailles",
      "Il/Elle/On": "jaille",
      "Nous": "jaillissions",
      "Vous": "jaillissiez",
      "Ils/Elle": "jaillent"
    },
    "Subjonctif Passé": {
      "Je": "aie jailli",
      "Tu": "aies jailli",
      "Il/Elle/On": "ait jailli",
      "Nous": "ayons jailli",
      "Vous": "ayez jailli",
      "Ils/Elle": "aient jailli"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse jailli",
      "Tu": "eusses jailli",
      "Il/Elle/On": "eût jailli",
      "Nous": "eussions jailli",
      "Vous": "eussiez jailli",
      "Ils/Elle": "eussent jailli"
    },
    "Subjonctif Imparfait": {
      "Je": "jaille",
      "Tu": "jailles",
      "Il/Elle/On": "jaillît",
      "Nous": "jaillissions",
      "Vous": "jaillissiez",
      "Ils/Elle": "jaillent"
    },
    "Impératif Présent": {
      "Tu": "jaille",
      "Nous": "jaillissons",
      "Vous": "jaillez"
    },
    "Impératif Passé": {
      "Tu": "ai jailli",
      "Nous": "ayons jailli",
      "Vous": "ayez jailli"
    },
    "Infinitif Présent": "jaillir",
    "Infinitif Passé": "avoir jailli",
    "Participe Présent": "jaillissant",
    "Participe Passé": "jailli",
    "Gérondif Présent": "en jaillissant",
    "Gérondif Passé": "en ayant jailli"
  },
  "maigrir": {
    "Présent": {
      "Je": "maigris",
      "Tu": "maigris",
      "Il/Elle/On": "maigrit",
      "Nous": "maigrissons",
      "Vous": "maigrissez",
      "Ils/Elle": "maigrissent"
    },
    "Imparfait": {
      "Je": "maigrissais",
      "Tu": "maigrissais",
      "Il/Elle/On": "maigrissait",
      "Nous": "maigrissions",
      "Vous": "maigrissiez",
      "Ils/Elle": "maigrissaient"
    },
    "Passé Composé": {
      "Je": "ai maigri",
      "Tu": "as maigri",
      "Il/Elle/On": "a maigri",
      "Nous": "avons maigri",
      "Vous": "avez maigri",
      "Ils/Elle": "ont maigri"
    },
    "Futur": {
      "Je": "maigrirai",
      "Tu": "maigriras",
      "Il/Elle/On": "maigrira",
      "Nous": "maigrirons",
      "Vous": "maigrirez",
      "Ils/Elle": "maigriront"
    },
    "Plus-que-parfait": {
      "Je": "avais maigri",
      "Tu": "avais maigri",
      "Il/Elle/On": "avait maigri",
      "Nous": "avions maigri",
      "Vous": "aviez maigri",
      "Ils/Elle": "avaient maigri"
    },
    "Futur Simple": {
      "Je": "maigrirai",
      "Tu": "maigriras",
      "Il/Elle/On": "maigrira",
      "Nous": "maigrirons",
      "Vous": "maigrirez",
      "Ils/Elle": "maigriront"
    },
    "Futur Antérieur": {
      "Je": "aurai maigri",
      "Tu": "auras maigri",
      "Il/Elle/On": "aura maigri",
      "Nous": "aurons maigri",
      "Vous": "aurez maigri",
      "Ils/Elle": "auront maigri"
    },
    "Conditionnel Présent": {
      "Je": "maigrirais",
      "Tu": "maigrirais",
      "Il/Elle/On": "maigrirait",
      "Nous": "maigririons",
      "Vous": "maigririez",
      "Ils/Elle": "maigriraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais maigri",
      "Tu": "aurais maigri",
      "Il/Elle/On": "aurait maigri",
      "Nous": "aurions maigri",
      "Vous": "auriez maigri",
      "Ils/Elle": "auraient maigri"
    },
    "Subjonctif Présent": {
      "Je": "maigrisse",
      "Tu": "maigrisses",
      "Il/Elle/On": "maigrisse",
      "Nous": "maigrissions",
      "Vous": "maigrissiez",
      "Ils/Elle": "maigrissent"
    },
    "Subjonctif Passé": {
      "Je": "aie maigri",
      "Tu": "aies maigri",
      "Il/Elle/On": "ait maigri",
      "Nous": "ayons maigri",
      "Vous": "ayez maigri",
      "Ils/Elle": "aient maigri"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse maigri",
      "Tu": "eusses maigri",
      "Il/Elle/On": "eût maigri",
      "Nous": "eussions maigri",
      "Vous": "eussiez maigri",
      "Ils/Elle": "eussent maigri"
    },
    "Subjonctif Imparfait": {
      "Je": "maigrisse",
      "Tu": "maigrisses",
      "Il/Elle/On": "maigrît",
      "Nous": "maigrissions",
      "Vous": "maigrissiez",
      "Ils/Elle": "maigrissent"
    },
    "Impératif Présent": {
      "Tu": "maigris",
      "Nous": "maigrissons",
      "Vous": "maigrissez"
    },
    "Impératif Passé": {
      "Tu": "ai maigri",
      "Nous": "ayons maigri",
      "Vous": "ayez maigri"
    },
    "Infinitif Présent": "maigrir",
    "Infinitif Passé": "avoir maigri",
    "Participe Présent": "maigrissant",
    "Participe Passé": "maigri",
    "Gérondif Présent": "en maigrissant",
    "Gérondif Passé": "en ayant maigri"
  },
  "monter": {
    "Présent": {
      "Je": "monte",
      "Tu": "montes",
      "Il/Elle/On": "monte",
      "Nous": "montons",
      "Vous": "montez",
      "Ils/Elle": "montent"
    },
    "Imparfait": {
      "Je": "montais",
      "Tu": "montais",
      "Il/Elle/On": "montait",
      "Nous": "montions",
      "Vous": "montiez",
      "Ils/Elle": "montaient"
    },
    "Passé Composé": {
      "Je": "ai monté",
      "Tu": "as monté",
      "Il/Elle/On": "a monté",
      "Nous": "avons monté",
      "Vous": "avez monté",
      "Ils/Elle": "ont monté"
    },
    "Futur": {
      "Je": "monterai",
      "Tu": "monteras",
      "Il/Elle/On": "montera",
      "Nous": "monterons",
      "Vous": "monterez",
      "Ils/Elle": "monteront"
    },
    "Plus-que-parfait": {
      "Je": "avais monté",
      "Tu": "avais monté",
      "Il/Elle/On": "avait monté",
      "Nous": "avions monté",
      "Vous": "aviez monté",
      "Ils/Elle": "avaient monté"
    },
    "Futur Simple": {
      "Je": "monterai",
      "Tu": "monteras",
      "Il/Elle/On": "montera",
      "Nous": "monterons",
      "Vous": "monterez",
      "Ils/Elle": "monteront"
    },
    "Futur Antérieur": {
      "Je": "aurai monté",
      "Tu": "auras monté",
      "Il/Elle/On": "aura monté",
      "Nous": "aurons monté",
      "Vous": "aurez monté",
      "Ils/Elle": "auront monté"
    },
    "Conditionnel Présent": {
      "Je": "monterais",
      "Tu": "monterais",
      "Il/Elle/On": "monterait",
      "Nous": "monterions",
      "Vous": "monteriez",
      "Ils/Elle": "monteraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais monté",
      "Tu": "aurais monté",
      "Il/Elle/On": "aurait monté",
      "Nous": "aurions monté",
      "Vous": "auriez monté",
      "Ils/Elle": "auraient monté"
    },
    "Subjonctif Présent": {
      "Je": "monte",
      "Tu": "montes",
      "Il/Elle/On": "monte",
      "Nous": "montions",
      "Vous": "montiez",
      "Ils/Elle": "montent"
    },
    "Subjonctif Passé": {
      "Je": "aie monté",
      "Tu": "aies monté",
      "Il/Elle/On": "ait monté",
      "Nous": "ayons monté",
      "Vous": "ayez monté",
      "Ils/Elle": "aient monté"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse monté",
      "Tu": "eusses monté",
      "Il/Elle/On": "eût monté",
      "Nous": "eussions monté",
      "Vous": "eussiez monté",
      "Ils/Elle": "eussent monté"
    },
    "Subjonctif Imparfait": {
      "Je": "montasse",
      "Tu": "montasses",
      "Il/Elle/On": "montât",
      "Nous": "montassions",
      "Vous": "montassiez",
      "Ils/Elle": "montassent"
    },
    "Impératif Présent": {
      "Tu": "monte",
      "Nous": "montons",
      "Vous": "montez"
    },
    "Impératif Passé": {
      "Tu": "ai monté",
      "Nous": "ayons monté",
      "Vous": "ayez monté"
    },
    "Infinitif Présent": "monter",
    "Infinitif Passé": "avoir monté",
    "Participe Présent": "montant",
    "Participe Passé": "monté",
    "Gérondif Présent": "en montant",
    "Gérondif Passé": "en ayant monté"
  },
  "remonter": {
    "Présent": {
      "Je": "remonte",
      "Tu": "remontes",
      "Il/Elle/On": "remonte",
      "Nous": "remontons",
      "Vous": "remontez",
      "Ils/Elle": "remontent"
    },
    "Imparfait": {
      "Je": "remontais",
      "Tu": "remontais",
      "Il/Elle/On": "remontait",
      "Nous": "remontions",
      "Vous": "remontiez",
      "Ils/Elle": "remontaient"
    },
    "Passé Composé": {
      "Je": "ai remonté",
      "Tu": "as remonté",
      "Il/Elle/On": "a remonté",
      "Nous": "avons remonté",
      "Vous": "avez remonté",
      "Ils/Elle": "ont remonté"
    },
    "Futur": {
      "Je": "remonterai",
      "Tu": "remonteras",
      "Il/Elle/On": "remontera",
      "Nous": "remonterons",
      "Vous": "remonterez",
      "Ils/Elle": "remonteront"
    },
    "Plus-que-parfait": {
      "Je": "avais remonté",
      "Tu": "avais remonté",
      "Il/Elle/On": "avait remonté",
      "Nous": "avions remonté",
      "Vous": "aviez remonté",
      "Ils/Elle": "avaient remonté"
    },
    "Futur Simple": {
      "Je": "remonterai",
      "Tu": "remonteras",
      "Il/Elle/On": "remontera",
      "Nous": "remonterons",
      "Vous": "remonterez",
      "Ils/Elle": "remonteront"
    },
    "Futur Antérieur": {
      "Je": "aurai remonté",
      "Tu": "auras remonté",
      "Il/Elle/On": "aura remonté",
      "Nous": "aurons remonté",
      "Vous": "aurez remonté",
      "Ils/Elle": "auront remonté"
    },
    "Conditionnel Présent": {
      "Je": "remonterais",
      "Tu": "remonterais",
      "Il/Elle/On": "remonterait",
      "Nous": "remonterions",
      "Vous": "remonteriez",
      "Ils/Elle": "remonteraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais remonté",
      "Tu": "aurais remonté",
      "Il/Elle/On": "aurait remonté",
      "Nous": "aurions remonté",
      "Vous": "auriez remonté",
      "Ils/Elle": "auraient remonté"
    },
    "Subjonctif Présent": {
      "Je": "remonte",
      "Tu": "remontes",
      "Il/Elle/On": "remonte",
      "Nous": "remontions",
      "Vous": "remontiez",
      "Ils/Elle": "remontent"
    },
    "Subjonctif Passé": {
      "Je": "aie remonté",
      "Tu": "aies remonté",
      "Il/Elle/On": "ait remonté",
      "Nous": "ayons remonté",
      "Vous": "ayez remonté",
      "Ils/Elle": "aient remonté"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse remonté",
      "Tu": "eusses remonté",
      "Il/Elle/On": "eût remonté",
      "Nous": "eussions remonté",
      "Vous": "eussiez remonté",
      "Ils/Elle": "eussent remonté"
    },
    "Subjonctif Imparfait": {
      "Je": "remontasse",
      "Tu": "remontasses",
      "Il/Elle/On": "remontât",
      "Nous": "remontassions",
      "Vous": "remontassiez",
      "Ils/Elle": "remontassent"
    },
    "Impératif Présent": {
      "Tu": "remonte",
      "Nous": "remontons",
      "Vous": "remontez"
    },
    "Impératif Passé": {
      "Tu": "ai remonté",
      "Nous": "ayons remonté",
      "Vous": "ayez remonté"
    },
    "Infinitif Présent": "remonter",
    "Infinitif Passé": "avoir remonté",
    "Participe Présent": "remontant",
    "Participe Passé": "remonté",
    "Gérondif Présent": "en remontant",
    "Gérondif Passé": "en ayant remonté"
  },
  "paraitre": {
    "Présent": {
      "Je": "parais",
      "Tu": "parais",
      "Il/Elle/On": "parait",
      "Nous": "paraissons",
      "Vous": "paraissez",
      "Ils/Elle": "paraissent"
    },
    "Imparfait": {
      "Je": "paraissais",
      "Tu": "paraissais",
      "Il/Elle/On": "paraissait",
      "Nous": "paraissions",
      "Vous": "paraissiez",
      "Ils/Elle": "paraissaient"
    },
    "Passé Composé": {
      "Je": "ai paru",
      "Tu": "as paru",
      "Il/Elle/On": "a paru",
      "Nous": "avons paru",
      "Vous": "avez paru",
      "Ils/Elle": "ont paru"
    },
    "Futur": {
      "Je": "paraîtrai",
      "Tu": "paraîtras",
      "Il/Elle/On": "paraîtra",
      "Nous": "paraîtrons",
      "Vous": "paraîtrez",
      "Ils/Elle": "paraîtront"
    },
    "Plus-que-parfait": {
      "Je": "avais paru",
      "Tu": "avais paru",
      "Il/Elle/On": "avait paru",
      "Nous": "avions paru",
      "Vous": "aviez paru",
      "Ils/Elle": "avaient paru"
    },
    "Futur Simple": {
      "Je": "paraîtrai",
      "Tu": "paraîtras",
      "Il/Elle/On": "paraîtra",
      "Nous": "paraîtrons",
      "Vous": "paraîtrez",
      "Ils/Elle": "paraîtront"
    },
    "Futur Antérieur": {
      "Je": "aurai paru",
      "Tu": "auras paru",
      "Il/Elle/On": "aura paru",
      "Nous": "aurons paru",
      "Vous": "aurez paru",
      "Ils/Elle": "auront paru"
    },
    "Conditionnel Présent": {
      "Je": "paraîtrais",
      "Tu": "paraîtrais",
      "Il/Elle/On": "paraîtrait",
      "Nous": "paraîtrions",
      "Vous": "paraîtriez",
      "Ils/Elle": "paraîtraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais paru",
      "Tu": "aurais paru",
      "Il/Elle/On": "aurait paru",
      "Nous": "aurions paru",
      "Vous": "auriez paru",
      "Ils/Elle": "auraient paru"
    },
    "Subjonctif Présent": {
      "Je": "paraisse",
      "Tu": "paraisses",
      "Il/Elle/On": "paraisse",
      "Nous": "paraissions",
      "Vous": "paraissiez",
      "Ils/Elle": "paraissent"
    },
    "Subjonctif Passé": {
      "Je": "aie paru",
      "Tu": "aies paru",
      "Il/Elle/On": "ait paru",
      "Nous": "ayons paru",
      "Vous": "ayez paru",
      "Ils/Elle": "aient paru"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse paru",
      "Tu": "eusses paru",
      "Il/Elle/On": "eût paru",
      "Nous": "eussions paru",
      "Vous": "eussiez paru",
      "Ils/Elle": "eussent paru"
    },
    "Subjonctif Imparfait": {
      "Je": "parusse",
      "Tu": "parusses",
      "Il/Elle/On": "parût",
      "Nous": "parussions",
      "Vous": "parussiez",
      "Ils/Elle": "parussent"
    },
    "Impératif Présent": {
      "Tu": "parais",
      "Nous": "paraissons",
      "Vous": "paraissez"
    },
    "Impératif Passé": {
      "Tu": "aie paru",
      "Nous": "ayons paru",
      "Vous": "ayez paru"
    },
    "Infinitif Présent": "paraître",
    "Infinitif Passé": "avoir paru",
    "Participe Présent": "paraissant",
    "Participe Passé": "paru",
    "Gérondif Présent": "en paraissant",
    "Gérondif Passé": "en ayant paru"
  },
  "passer": {
    "Présent": {
      "Je": "passe",
      "Tu": "passes",
      "Il/Elle/On": "passe",
      "Nous": "passons",
      "Vous": "passez",
      "Ils/Elle": "passent"
    },
    "Imparfait": {
      "Je": "passais",
      "Tu": "passais",
      "Il/Elle/On": "passait",
      "Nous": "passions",
      "Vous": "passiez",
      "Ils/Elle": "passaient"
    },
    "Passé Composé": {
      "Je": "ai passé",
      "Tu": "as passé",
      "Il/Elle/On": "a passé",
      "Nous": "avons passé",
      "Vous": "avez passé",
      "Ils/Elle": "ont passé"
    },
    "Futur": {
      "Je": "passerai",
      "Tu": "passeras",
      "Il/Elle/On": "passera",
      "Nous": "passerons",
      "Vous": "passerez",
      "Ils/Elle": "passeront"
    },
    "Plus-que-parfait": {
      "Je": "avais passé",
      "Tu": "avais passé",
      "Il/Elle/On": "avait passé",
      "Nous": "avions passé",
      "Vous": "aviez passé",
      "Ils/Elle": "avaient passé"
    },
    "Futur Simple": {
      "Je": "passerai",
      "Tu": "passeras",
      "Il/Elle/On": "passera",
      "Nous": "passerons",
      "Vous": "passerez",
      "Ils/Elle": "passeront"
    },
    "Futur Antérieur": {
      "Je": "aurai passé",
      "Tu": "auras passé",
      "Il/Elle/On": "aura passé",
      "Nous": "aurons passé",
      "Vous": "aurez passé",
      "Ils/Elle": "auront passé"
    },
    "Conditionnel Présent": {
      "Je": "passerais",
      "Tu": "passerais",
      "Il/Elle/On": "passerait",
      "Nous": "passerions",
      "Vous": "passeriez",
      "Ils/Elle": "passeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais passé",
      "Tu": "aurais passé",
      "Il/Elle/On": "aurait passé",
      "Nous": "aurions passé",
      "Vous": "auriez passé",
      "Ils/Elle": "auraient passé"
    },
    "Subjonctif Présent": {
      "Je": "passe",
      "Tu": "passes",
      "Il/Elle/On": "passe",
      "Nous": "passions",
      "Vous": "passiez",
      "Ils/Elle": "passent"
    },
    "Subjonctif Passé": {
      "Je": "aie passé",
      "Tu": "aies passé",
      "Il/Elle/On": "ait passé",
      "Nous": "ayons passé",
      "Vous": "ayez passé",
      "Ils/Elle": "aient passé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse passé",
      "Tu": "eusses passé",
      "Il/Elle/On": "eût passé",
      "Nous": "eussions passé",
      "Vous": "eussiez passé",
      "Ils/Elle": "eussent passé"
    },
    "Subjonctif Imparfait": {
      "Je": "passasse",
      "Tu": "passasses",
      "Il/Elle/On": "passât",
      "Nous": "passassions",
      "Vous": "passassiez",
      "Ils/Elle": "passassent"
    },
    "Impératif Présent": {
      "Tu": "passe",
      "Nous": "passons",
      "Vous": "passez"
    },
    "Impératif Passé": {
      "Tu": "ai passé",
      "Nous": "ayons passé",
      "Vous": "ayez passé"
    },
    "Infinitif Présent": "passer",
    "Infinitif Passé": "avoir passé",
    "Participe Présent": "passant",
    "Participe Passé": "passé",
    "Gérondif Présent": "en passant",
    "Gérondif Passé": "en ayant passé"
  },
"ressusciter": {
    "Présent": {
      "Je": "ressuscite",
      "Tu": "ressuscites",
      "Il/Elle/On": "ressuscite",
      "Nous": "ressuscitons",
      "Vous": "ressuscitez",
      "Ils/Elle": "ressuscitent"
    },
    "Imparfait": {
      "Je": "ressuscitais",
      "Tu": "ressuscitais",
      "Il/Elle/On": "ressuscitait",
      "Nous": "ressuscitions",
      "Vous": "ressuscitiez",
      "Ils/Elle": "ressuscitaient"
    },
    "Passé Composé": {
      "Je": "ai ressuscité",
      "Tu": "as ressuscité",
      "Il/Elle/On": "a ressuscité",
      "Nous": "avons ressuscité",
      "Vous": "avez ressuscité",
      "Ils/Elle": "ont ressuscité"
    },
    "Futur": {
      "Je": "ressusciterai",
      "Tu": "ressusciteras",
      "Il/Elle/On": "ressuscitera",
      "Nous": "ressusciterons",
      "Vous": "ressusciterez",
      "Ils/Elle": "ressusciteront"
    },
    "Plus-que-parfait": {
      "Je": "avais ressuscité",
      "Tu": "avais ressuscité",
      "Il/Elle/On": "avait ressuscité",
      "Nous": "avions ressuscité",
      "Vous": "aviez ressuscité",
      "Ils/Elle": "avaient ressuscité"
    },
    "Futur Simple": {
      "Je": "ressusciterai",
      "Tu": "ressusciteras",
      "Il/Elle/On": "ressuscitera",
      "Nous": "ressusciterons",
      "Vous": "ressusciterez",
      "Ils/Elle": "ressusciteront"
    },
    "Futur Antérieur": {
      "Je": "aurai ressuscité",
      "Tu": "auras ressuscité",
      "Il/Elle/On": "aura ressuscité",
      "Nous": "aurons ressuscité",
      "Vous": "aurez ressuscité",
      "Ils/Elle": "auront ressuscité"
    },
    "Conditionnel Présent": {
      "Je": "ressusciterais",
      "Tu": "ressusciterais",
      "Il/Elle/On": "ressusciterait",
      "Nous": "ressusciterions",
      "Vous": "ressusciteriez",
      "Ils/Elle": "ressusciteraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais ressuscité",
      "Tu": "aurais ressuscité",
      "Il/Elle/On": "aurait ressuscité",
      "Nous": "aurions ressuscité",
      "Vous": "auriez ressuscité",
      "Ils/Elle": "auraient ressuscité"
    },
    "Subjonctif Présent": {
      "Je": "ressuscite",
      "Tu": "ressuscites",
      "Il/Elle/On": "ressuscite",
      "Nous": "ressuscitions",
      "Vous": "ressuscitiez",
      "Ils/Elle": "ressuscitent"
    },
    "Subjonctif Passé": {
      "Je": "aie ressuscité",
      "Tu": "aies ressuscité",
      "Il/Elle/On": "ait ressuscité",
      "Nous": "ayons ressuscité",
      "Vous": "ayez ressuscité",
      "Ils/Elle": "aient ressuscité"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse ressuscité",
      "Tu": "eusses ressuscité",
      "Il/Elle/On": "eût ressuscité",
      "Nous": "eussions ressuscité",
      "Vous": "eussiez ressuscité",
      "Ils/Elle": "eussent ressuscité"
    },
    "Subjonctif Imparfait": {
      "Je": "ressuscitasse",
      "Tu": "ressuscitasses",
      "Il/Elle/On": "ressuscitât",
      "Nous": "ressuscitassions",
      "Vous": "ressuscitassiez",
      "Ils/Elle": "ressuscitassent"
    },
    "Impératif Présent": {
      "Tu": "ressuscite",
      "Nous": "ressuscitons",
      "Vous": "ressuscitez"
    },
    "Impératif Passé": {
      "Tu": "aie ressuscité",
      "Nous": "ayons ressuscité",
      "Vous": "ayez ressuscité"
    },
    "Infinitif Présent": "ressusciter",
    "Infinitif Passé": "avoir ressuscité",
    "Participe Présent": "ressuscitant",
    "Participe Passé": "ressuscité",
    "Gérondif Présent": "en ressuscitant",
    "Gérondif Passé": "en ayant ressuscité"
  },
  "résulter": {
    "Présent": {
      "Je": "résulte",
      "Tu": "résultes",
      "Il/Elle/On": "résulte",
      "Nous": "résultons",
      "Vous": "résultez",
      "Ils/Elle": "résultent"
    },
    "Imparfait": {
      "Je": "résultais",
      "Tu": "résultais",
      "Il/Elle/On": "résultait",
      "Nous": "résultions",
      "Vous": "résultiez",
      "Ils/Elle": "résultaient"
    },
    "Passé Composé": {
      "Je": "ai résulté",
      "Tu": "as résulté",
      "Il/Elle/On": "a résulté",
      "Nous": "avons résulté",
      "Vous": "avez résulté",
      "Ils/Elle": "ont résulté"
    },
    "Futur": {
      "Je": "résulterai",
      "Tu": "résulteras",
      "Il/Elle/On": "résultera",
      "Nous": "résulterons",
      "Vous": "résulterez",
      "Ils/Elle": "résulteront"
    },
    "Plus-que-parfait": {
      "Je": "avais résulté",
      "Tu": "avais résulté",
      "Il/Elle/On": "avait résulté",
      "Nous": "avions résulté",
      "Vous": "aviez résulté",
      "Ils/Elle": "avaient résulté"
    },
    "Futur Simple": {
      "Je": "résulterai",
      "Tu": "résulteras",
      "Il/Elle/On": "résultera",
      "Nous": "résulterons",
      "Vous": "résulterez",
      "Ils/Elle": "résulteront"
    },
    "Futur Antérieur": {
      "Je": "aurai résulté",
      "Tu": "auras résulté",
      "Il/Elle/On": "aura résulté",
      "Nous": "aurons résulté",
      "Vous": "aurez résulté",
      "Ils/Elle": "auront résulté"
    },
    "Conditionnel Présent": {
      "Je": "résulterais",
      "Tu": "résulterais",
      "Il/Elle/On": "résulterait",
      "Nous": "résulterions",
      "Vous": "résulteriez",
      "Ils/Elle": "résulteraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais résulté",
      "Tu": "aurais résulté",
      "Il/Elle/On": "aurait résulté",
      "Nous": "aurions résulté",
      "Vous": "auriez résulté",
      "Ils/Elle": "auraient résulté"
    },
    "Subjonctif Présent": {
      "Je": "résulte",
      "Tu": "résultes",
      "Il/Elle/On": "résulte",
      "Nous": "résultions",
      "Vous": "résultiez",
      "Ils/Elle": "résultent"
    },
    "Subjonctif Passé": {
      "Je": "aie résulté",
      "Tu": "aies résulté",
      "Il/Elle/On": "ait résulté",
      "Nous": "ayons résulté",
      "Vous": "ayez résulté",
      "Ils/Elle": "aient résulté"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse résulté",
      "Tu": "eusses résulté",
      "Il/Elle/On": "eût résulté",
      "Nous": "eussions résulté",
      "Vous": "eussiez résulté",
      "Ils/Elle": "eussent résulté"
    },
    "Subjonctif Imparfait": {
      "Je": "résultasse",
      "Tu": "résultasses",
      "Il/Elle/On": "résultât",
      "Nous": "résultassions",
      "Vous": "résultassiez",
      "Ils/Elle": "résultassent"
    },
    "Impératif Présent": {
      "Tu": "résulte",
      "Nous": "résultons",
      "Vous": "résultez"
    },
    "Impératif Passé": {
      "Tu": "aie résulté",
      "Nous": "ayons résulté",
      "Vous": "ayez résulté"
    },
    "Infinitif Présent": "résulter",
    "Infinitif Passé": "avoir résulté",
    "Participe Présent": "résultant",
    "Participe Passé": "résulté",
    "Gérondif Présent": "en résultant",
    "Gérondif Passé": "en ayant résulté"
  },
  "retourner": {
    "Présent": {
      "Je": "retourne",
      "Tu": "retournes",
      "Il/Elle/On": "retourne",
      "Nous": "retournons",
      "Vous": "retournez",
      "Ils/Elle": "retournent"
    },
    "Imparfait": {
      "Je": "retournais",
      "Tu": "retournais",
      "Il/Elle/On": "retournait",
      "Nous": "retournions",
      "Vous": "retourniez",
      "Ils/Elle": "retournaient"
    },
    "Passé Composé": {
      "Je": "ai retourné",
      "Tu": "as retourné",
      "Il/Elle/On": "a retourné",
      "Nous": "avons retourné",
      "Vous": "avez retourné",
      "Ils/Elle": "ont retourné"
    },
    "Futur": {
      "Je": "retournerai",
      "Tu": "retourneras",
      "Il/Elle/On": "retournera",
      "Nous": "retournerons",
      "Vous": "retournerez",
      "Ils/Elle": "retourneront"
    },
    "Plus-que-parfait": {
      "Je": "avais retourné",
      "Tu": "avais retourné",
      "Il/Elle/On": "avait retourné",
      "Nous": "avions retourné",
      "Vous": "aviez retourné",
      "Ils/Elle": "avaient retourné"
    },
    "Futur Simple": {
      "Je": "retournerai",
      "Tu": "retourneras",
      "Il/Elle/On": "retournera",
      "Nous": "retournerons",
      "Vous": "retournerez",
      "Ils/Elle": "retourneront"
    },
    "Futur Antérieur": {
      "Je": "aurai retourné",
      "Tu": "auras retourné",
      "Il/Elle/On": "aura retourné",
      "Nous": "aurons retourné",
      "Vous": "aurez retourné",
      "Ils/Elle": "auront retourné"
    },
    "Conditionnel Présent": {
      "Je": "retournerais",
      "Tu": "retournerais",
      "Il/Elle/On": "retournerait",
      "Nous": "retournerions",
      "Vous": "retourneriez",
      "Ils/Elle": "retourneraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais retourné",
      "Tu": "aurais retourné",
      "Il/Elle/On": "aurait retourné",
      "Nous": "aurions retourné",
      "Vous": "auriez retourné",
      "Ils/Elle": "auraient retourné"
    },
    "Subjonctif Présent": {
      "Je": "retourne",
      "Tu": "retournes",
      "Il/Elle/On": "retourne",
      "Nous": "retournions",
      "Vous": "retourniez",
      "Ils/Elle": "retournent"
    },
    "Subjonctif Passé": {
      "Je": "aie retourné",
      "Tu": "aies retourné",
      "Il/Elle/On": "ait retourné",
      "Nous": "ayons retourné",
      "Vous": "ayez retourné",
      "Ils/Elle": "aient retourné"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse retourné",
      "Tu": "eusses retourné",
      "Il/Elle/On": "eût retourné",
      "Nous": "eussions retourné",
      "Vous": "eussiez retourné",
      "Ils/Elle": "eussent retourné"
    },
    "Subjonctif Imparfait": {
      "Je": "retournasse",
      "Tu": "retournasses",
      "Il/Elle/On": "retournât",
      "Nous": "retournassions",
      "Vous": "retournassiez",
      "Ils/Elle": "retournassent"
    },
    "Impératif Présent": {
      "Tu": "retourne",
      "Nous": "retournons",
      "Vous": "retournez"
    },
    "Impératif Passé": {
      "Tu": "aie retourné",
      "Nous": "ayons retourné",
      "Vous": "ayez retourné"
    },
    "Infinitif Présent": "retourner",
    "Infinitif Passé": "avoir retourné",
    "Participe Présent": "retournant",
    "Participe Passé": "retourné",
    "Gérondif Présent": "en retournant",
    "Gérondif Passé": "en ayant retourné"
  },
  "sortir": {
    "Présent": {
      "Je": "sors",
      "Tu": "sors",
      "Il/Elle/On": "sort",
      "Nous": "sortons",
      "Vous": "sortez",
      "Ils/Elle": "sortent"
    },
    "Imparfait": {
      "Je": "sortais",
      "Tu": "sortais",
      "Il/Elle/On": "sortait",
      "Nous": "sortions",
      "Vous": "sortiez",
      "Ils/Elle": "sortaient"
    },
    "Passé Composé": {
      "Je": "suis sorti(e)",
      "Tu": "es sorti(e)",
      "Il/Elle/On": "est sorti(e)",
      "Nous": "sommes sorti(e)s",
      "Vous": "êtes sorti(e)s",
      "Ils/Elle": "sont sorti(e)s"
    },
    "Futur": {
      "Je": "sortirai",
      "Tu": "sortiras",
      "Il/Elle/On": "sortira",
      "Nous": "sortirons",
      "Vous": "sortirez",
      "Ils/Elle": "sortiront"
    },
    "Plus-que-parfait": {
      "Je": "étais sorti(e)",
      "Tu": "étais sorti(e)",
      "Il/Elle/On": "était sorti(e)",
      "Nous": "étions sorti(e)s",
      "Vous": "étiez sorti(e)s",
      "Ils/Elle": "étaient sorti(e)s"
    },
    "Futur Simple": {
      "Je": "sortirai",
      "Tu": "sortiras",
      "Il/Elle/On": "sortira",
      "Nous": "sortirons",
      "Vous": "sortirez",
      "Ils/Elle": "sortiront"
    },
    "Futur Antérieur": {
      "Je": "serai sorti(e)",
      "Tu": "seras sorti(e)",
      "Il/Elle/On": "sera sorti(e)",
      "Nous": "serons sorti(e)s",
      "Vous": "serez sorti(e)s",
      "Ils/Elle": "seront sorti(e)s"
    },
    "Conditionnel Présent": {
      "Je": "sortirais",
      "Tu": "sortirais",
      "Il/Elle/On": "sortirait",
      "Nous": "sortirions",
      "Vous": "sortiriez",
      "Ils/Elle": "sortiraient"
    },
    "Conditionnel Passé": {
      "Je": "serais sorti(e)",
      "Tu": "serais sorti(e)",
      "Il/Elle/On": "serait sorti(e)",
      "Nous": "serions sorti(e)s",
      "Vous": "seriez sorti(e)s",
      "Ils/Elle": "seraient sorti(e)s"
    },
    "Subjonctif Présent": {
      "Je": "sorte",
      "Tu": "sortes",
      "Il/Elle/On": "sorte",
      "Nous": "sortions",
      "Vous": "sortiez",
      "Ils/Elle": "sortent"
    },
    "Subjonctif Passé": {
      "Je": "sois sorti(e)",
      "Tu": "sois sorti(e)",
      "Il/Elle/On": "soit sorti(e)",
      "Nous": "soyons sorti(e)s",
      "Vous": "soyez sorti(e)s",
      "Ils/Elle": "soient sorti(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse sorti(e)",
      "Tu": "fusses sorti(e)",
      "Il/Elle/On": "fût sorti(e)",
      "Nous": "fussions sorti(e)s",
      "Vous": "fussiez sorti(e)s",
      "Ils/Elle": "fussent sorti(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "sortisse",
      "Tu": "sortisses",
      "Il/Elle/On": "sortît",
      "Nous": "sortissions",
      "Vous": "sortissiez",
      "Ils/Elle": "sortissent"
    },
    "Impératif Présent": {
      "Tu": "sors",
      "Nous": "sortons",
      "Vous": "sortez"
    },
    "Impératif Passé": {
      "Tu": "sois sorti(e)",
      "Nous": "soyons sorti(e)s",
      "Vous": "soyez sorti(e)s"
    },
    "Infinitif Présent": "sortir",
    "Infinitif Passé": "être sorti(e)",
    "Participe Présent": "sortant",
    "Participe Passé": {
      "Masculine": "sorti",
      "Feminine": "sortie"
    },
    "Gérondif Présent": "en sortant",
    "Gérondif Passé": {
      "Masculine": "en étant sorti",
      "Feminine": "en étant sortie"
    }
  },
  "ressortir": {
    "Présent": {
      "Je": "ressors",
      "Tu": "ressors",
      "Il/Elle/On": "ressort",
      "Nous": "ressortons",
      "Vous": "ressortez",
      "Ils/Elle": "ressortent"
    },
    "Imparfait": {
      "Je": "ressortais",
      "Tu": "ressortais",
      "Il/Elle/On": "ressortait",
      "Nous": "ressortions",
      "Vous": "ressortiez",
      "Ils/Elle": "ressortaient"
    },
    "Passé Composé": {
      "Je": "suis ressorti(e)",
      "Tu": "es ressorti(e)",
      "Il/Elle/On": "est ressorti(e)",
      "Nous": "sommes ressorti(e)s",
      "Vous": "êtes ressorti(e)s",
      "Ils/Elle": "sont ressorti(e)s"
    },
    "Futur": {
      "Je": "ressortirai",
      "Tu": "ressortiras",
      "Il/Elle/On": "ressortira",
      "Nous": "ressortirons",
      "Vous": "ressortirez",
      "Ils/Elle": "ressortiront"
    },
    "Plus-que-parfait": {
      "Je": "étais ressorti(e)",
      "Tu": "étais ressorti(e)",
      "Il/Elle/On": "était ressorti(e)",
      "Nous": "étions ressorti(e)s",
      "Vous": "étiez ressorti(e)s",
      "Ils/Elle": "étaient ressorti(e)s"
    },
    "Futur Simple": {
      "Je": "ressortirai",
      "Tu": "ressortiras",
      "Il/Elle/On": "ressortira",
      "Nous": "ressortirons",
      "Vous": "ressortirez",
      "Ils/Elle": "ressortiront"
    },
    "Futur Antérieur": {
      "Je": "serai ressorti(e)",
      "Tu": "seras ressorti(e)",
      "Il/Elle/On": "sera ressorti(e)",
      "Nous": "serons ressorti(e)s",
      "Vous": "serez ressorti(e)s",
      "Ils/Elle": "seront ressorti(e)s"
    },
    "Conditionnel Présent": {
      "Je": "ressortirais",
      "Tu": "ressortirais",
      "Il/Elle/On": "ressortirait",
      "Nous": "ressortirions",
      "Vous": "ressortiriez",
      "Ils/Elle": "ressortiraient"
    },
    "Conditionnel Passé": {
      "Je": "serais ressorti(e)",
      "Tu": "serais ressorti(e)",
      "Il/Elle/On": "serait ressorti(e)",
      "Nous": "serions ressorti(e)s",
      "Vous": "seriez ressorti(e)s",
      "Ils/Elle": "seraient ressorti(e)s"
    },
    "Subjonctif Présent": {
      "Je": "ressorte",
      "Tu": "ressortes",
      "Il/Elle/On": "ressorte",
      "Nous": "ressortions",
      "Vous": "ressortiez",
      "Ils/Elle": "ressortent"
    },
    "Subjonctif Passé": {
      "Je": "sois ressorti(e)",
      "Tu": "sois ressorti(e)",
      "Il/Elle/On": "soit ressorti(e)",
      "Nous": "soyons ressorti(e)s",
      "Vous": "soyez ressorti(e)s",
      "Ils/Elle": "soient ressorti(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse ressorti(e)",
      "Tu": "fusses ressorti(e)",
      "Il/Elle/On": "fût ressorti(e)",
      "Nous": "fussions ressorti(e)s",
      "Vous": "fussiez ressorti(e)s",
      "Ils/Elle": "fussent ressorti(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "ressortisse",
      "Tu": "ressortisses",
      "Il/Elle/On": "ressortît",
      "Nous": "ressortissions",
      "Vous": "ressortissiez",
      "Ils/Elle": "ressortissent"
    },
    "Impératif Présent": {
      "Tu": "ressors",
      "Nous": "ressortons",
      "Vous": "ressortez"
    },
    "Impératif Passé": {
      "Tu": "sois ressorti(e)",
      "Nous": "soyons ressorti(e)s",
      "Vous": "soyez ressorti(e)s"
    },
    "Infinitif Présent": "ressortir",
    "Infinitif Passé": "être ressorti(e)",
    "Participe Présent": "ressortant",
    "Participe Passé": {
      "Masculine": "ressorti",
      "Feminine": "ressortie"
    },
    "Gérondif Présent": "en ressortant",
    "Gérondif Passé": {
      "Masculine": "en étant ressorti",
      "Feminine": "en étant ressortie"
    }
  },
  "tomber": {
    "Présent": {
      "Je": "tombe",
      "Tu": "tombes",
      "Il/Elle/On": "tombe",
      "Nous": "tombons",
      "Vous": "tombez",
      "Ils/Elle": "tombent"
    },
    "Imparfait": {
      "Je": "tombais",
      "Tu": "tombais",
      "Il/Elle/On": "tombait",
      "Nous": "tombions",
      "Vous": "tombiez",
      "Ils/Elle": "tombaient"
    },
    "Passé Composé": {
      "Je": "suis tombé(e)",
      "Tu": "es tombé(e)",
      "Il/Elle/On": "est tombé(e)",
      "Nous": "sommes tombé(e)s",
      "Vous": "êtes tombé(e)s",
      "Ils/Elle": "sont tombé(e)s"
    },
    "Futur": {
      "Je": "tomberai",
      "Tu": "tomberas",
      "Il/Elle/On": "tombera",
      "Nous": "tomberons",
      "Vous": "tomberez",
      "Ils/Elle": "tomberont"
    },
    "Plus-que-parfait": {
      "Je": "étais tombé(e)",
      "Tu": "étais tombé(e)",
      "Il/Elle/On": "était tombé(e)",
      "Nous": "étions tombé(e)s",
      "Vous": "étiez tombé(e)s",
      "Ils/Elle": "étaient tombé(e)s"
    },
    "Futur Simple": {
      "Je": "tomberai",
      "Tu": "tomberas",
      "Il/Elle/On": "tombera",
      "Nous": "tomberons",
      "Vous": "tomberez",
      "Ils/Elle": "tomberont"
    },
    "Futur Antérieur": {
      "Je": "serai tombé(e)",
      "Tu": "seras tombé(e)",
      "Il/Elle/On": "sera tombé(e)",
      "Nous": "serons tombé(e)s",
      "Vous": "serez tombé(e)s",
      "Ils/Elle": "seront tombé(e)s"
    },
    "Conditionnel Présent": {
      "Je": "tomberais",
      "Tu": "tomberais",
      "Il/Elle/On": "tomberait",
      "Nous": "tomberions",
      "Vous": "tomberiez",
      "Ils/Elle": "tomberaient"
    },
    "Conditionnel Passé": {
      "Je": "serais tombé(e)",
      "Tu": "serais tombé(e)",
      "Il/Elle/On": "serait tombé(e)",
      "Nous": "serions tombé(e)s",
      "Vous": "seriez tombé(e)s",
      "Ils/Elle": "seraient tombé(e)s"
    },
    "Subjonctif Présent": {
      "Je": "tombre",
      "Tu": "tombres",
      "Il/Elle/On": "tombre",
      "Nous": "tombions",
      "Vous": "tombiez",
      "Ils/Elle": "tombent"
    },
    "Subjonctif Passé": {
      "Je": "sois tombé(e)",
      "Tu": "sois tombé(e)",
      "Il/Elle/On": "soit tombé(e)",
      "Nous": "soyons tombé(e)s",
      "Vous": "soyez tombé(e)s",
      "Ils/Elle": "soient tombé(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse tombé(e)",
      "Tu": "fusses tombé(e)",
      "Il/Elle/On": "fût tombé(e)",
      "Nous": "fussions tombé(e)s",
      "Vous": "fussiez tombé(e)s",
      "Ils/Elle": "fussent tombé(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "tombasse",
      "Tu": "tompasses",
      "Il/Elle/On": "tombât",
      "Nous": "tomabassions",
      "Vous": "tomabassiez",
      "Ils/Elle": "tombassent"
    },
    "Impératif Présent": {
      "Tu": "tombe",
      "Nous": "tombons",
      "Vous": "tombez"
    },
    "Impératif Passé": {
      "Tu": "sois tombé(e)",
      "Nous": "soyons tombé(e)s",
      "Vous": "soyez tombé(e)s"
    },
    "Infinitif Présent": "tomber",
    "Infinitif Passé": "être tombé(e)",
    "Participe Présent": "tombant",
    "Participe Passé": {
      "Masculine": "tombé",
      "Feminine": "tombée"
    },
    "Gérondif Présent": "en tombant",
    "Gérondif Passé": {
      "Masculine": "en étant tombé",
      "Feminine": "en étant tombée"
    }
  },
  "trépasser": {
    "Présent": {
      "Je": "trépasse",
      "Tu": "trépasses",
      "Il/Elle/On": "trépasse",
      "Nous": "trépassons",
      "Vous": "trépassez",
      "Ils/Elle": "trépassent"
    },
    "Imparfait": {
      "Je": "trépassais",
      "Tu": "trépassais",
      "Il/Elle/On": "trépassait",
      "Nous": "trépassions",
      "Vous": "trépassiez",
      "Ils/Elle": "trépassaient"
    },
    "Passé Composé": {
      "Je": "suis trépassé(e)",
      "Tu": "es trépassé(e)",
      "Il/Elle/On": "est trépassé(e)",
      "Nous": "sommes trépassé(e)s",
      "Vous": "êtes trépassé(e)s",
      "Ils/Elle": "sont trépassé(e)s"
    },
    "Futur": {
      "Je": "trépasserai",
      "Tu": "trépasseras",
      "Il/Elle/On": "trépassera",
      "Nous": "trépasserons",
      "Vous": "trépasserez",
      "Ils/Elle": "trépasseront"
    },
    "Plus-que-parfait": {
      "Je": "étais trépassé(e)",
      "Tu": "étais trépassé(e)",
      "Il/Elle/On": "était trépassé(e)",
      "Nous": "étions trépassé(e)s",
      "Vous": "étiez trépassé(e)s",
      "Ils/Elle": "étaient trépassé(e)s"
    },
    "Futur Simple": {
      "Je": "trépasserai",
      "Tu": "trépasseras",
      "Il/Elle/On": "trépassera",
      "Nous": "trépasserons",
      "Vous": "trépasserez",
      "Ils/Elle": "trépasseront"
    },
    "Futur Antérieur": {
      "Je": "serai trépassé(e)",
      "Tu": "seras trépassé(e)",
      "Il/Elle/On": "sera trépassé(e)",
      "Nous": "serons trépassé(e)s",
      "Vous": "serez trépassé(e)s",
      "Ils/Elle": "seront trépassé(e)s"
    },
    "Conditionnel Présent": {
      "Je": "trépasserais",
      "Tu": "trépasserais",
      "Il/Elle/On": "trépasserait",
      "Nous": "trépasserions",
      "Vous": "trépasseriez",
      "Ils/Elle": "trépasseraient"
    },
    "Conditionnel Passé": {
      "Je": "serais trépassé(e)",
      "Tu": "serais trépassé(e)",
      "Il/Elle/On": "serait trépassé(e)",
      "Nous": "serions trépassé(e)s",
      "Vous": "seriez trépassé(e)s",
      "Ils/Elle": "seraient trépassé(e)s"
    },
    "Subjonctif Présent": {
      "Je": "trépasse",
      "Tu": "trépasses",
      "Il/Elle/On": "trépasse",
      "Nous": "trépassions",
      "Vous": "trépassiez",
      "Ils/Elle": "trépassent"
    },
    "Subjonctif Passé": {
      "Je": "sois trépassé(e)",
      "Tu": "sois trépassé(e)",
      "Il/Elle/On": "soit trépassé(e)",
      "Nous": "soyons trépassé(e)s",
      "Vous": "soyez trépassé(e)s",
      "Ils/Elle": "soient trépassé(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse trépassé(e)",
      "Tu": "fusses trépassé(e)",
      "Il/Elle/On": "fût trépassé(e)",
      "Nous": "fussions trépassé(e)s",
      "Vous": "fussiez trépassé(e)s",
      "Ils/Elle": "fussent trépassé(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "trépassasse",
      "Tu": "trépassasses",
      "Il/Elle/On": "trépassât",
      "Nous": "trépassassions",
      "Vous": "trépassassiez",
      "Ils/Elle": "trépassassent"
    },
    "Impératif Présent": {
      "Tu": "trépasse",
      "Nous": "trépassons",
      "Vous": "trépassez"
    },
    "Impératif Passé": {
      "Tu": "sois trépassé(e)",
      "Nous": "soyons trépassé(e)s",
      "Vous": "soyez trépassé(e)s"
    },
    "Infinitif Présent": "trépasser",
    "Infinitif Passé": "être trépassé(e)",
    "Participe Présent": "trépassant",
    "Participe Passé": {
      "Masculine": "trépassé",
      "Feminine": "trépassée"
    },
    "Gérondif Présent": "en trépassant",
    "Gérondif Passé": {
      "Masculine": "en étant trépassé",
      "Feminine": "en étant trépassée"
    }
  },
  "vieiller": {
    "Présent": {
      "Je": "vieille",
      "Tu": "vieilles",
      "Il/Elle/On": "vieille",
      "Nous": "vieillons",
      "Vous": "vieillez",
      "Ils/Elle": "vieillent"
    },
    "Imparfait": {
      "Je": "vieillais",
      "Tu": "vieillais",
      "Il/Elle/On": "vieillait",
      "Nous": "vieillions",
      "Vous": "vieilliez",
      "Ils/Elle": "vieillaient"
    },
    "Passé Composé": {
      "Je": "ai vieilli",
      "Tu": "as vieilli",
      "Il/Elle/On": "a vieilli",
      "Nous": "avons vieilli",
      "Vous": "avez vieilli",
      "Ils/Elle": "ont vieilli"
    },
    "Futur": {
      "Je": "vieillerai",
      "Tu": "vieilleras",
      "Il/Elle/On": "vieillera",
      "Nous": "vieillerons",
      "Vous": "vieillerez",
      "Ils/Elle": "vieilleront"
    },
    "Plus-que-parfait": {
      "Je": "avais vieilli",
      "Tu": "avais vieilli",
      "Il/Elle/On": "avait vieilli",
      "Nous": "avions vieilli",
      "Vous": "aviez vieilli",
      "Ils/Elle": "avaient vieilli"
    },
    "Futur Simple": {
      "Je": "vieillerai",
      "Tu": "vieilleras",
      "Il/Elle/On": "vieillera",
      "Nous": "vieillerons",
      "Vous": "vieillerez",
      "Ils/Elle": "vieilleront"
    },
    "Futur Antérieur": {
      "Je": "aurai vieilli",
      "Tu": "auras vieilli",
      "Il/Elle/On": "aura vieilli",
      "Nous": "aurons vieilli",
      "Vous": "aurez vieilli",
      "Ils/Elle": "auront vieilli"
    },
    "Conditionnel Présent": {
      "Je": "vieillerais",
      "Tu": "vieillerais",
      "Il/Elle/On": "vieillerait",
      "Nous": "vieillerions",
      "Vous": "vieilleriez",
      "Ils/Elle": "vieilleraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais vieilli",
      "Tu": "aurais vieilli",
      "Il/Elle/On": "aurait vieilli",
      "Nous": "aurions vieilli",
      "Vous": "auriez vieilli",
      "Ils/Elle": "auraient vieilli"
    },
    "Subjonctif Présent": {
      "Je": "vieille",
      "Tu": "vieilles",
      "Il/Elle/On": "vieille",
      "Nous": "vieillions",
      "Vous": "vieilliez",
      "Ils/Elle": "vieillent"
    },
    "Subjonctif Passé": {
      "Je": "aie vieilli",
      "Tu": "aies vieilli",
      "Il/Elle/On": "ait vieilli",
      "Nous": "ayons vieilli",
      "Vous": "ayez vieilli",
      "Ils/Elle": "aient vieilli"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse vieilli",
      "Tu": "eusses vieilli",
      "Il/Elle/On": "eût vieilli",
      "Nous": "eussions vieilli",
      "Vous": "eussiez vieilli",
      "Ils/Elle": "eussent vieilli"
    },
    "Subjonctif Imparfait": {
      "Je": "vieillasse",
      "Tu": "vieillasses",
      "Il/Elle/On": "vieillât",
      "Nous": "vieillassions",
      "Vous": "vieillassiez",
      "Ils/Elle": "vieillassent"
    },
    "Impératif Présent": {
      "Tu": "vieille",
      "Nous": "vieillons",
      "Vous": "vieillez"
    },
    "Impératif Passé": {
      "Tu": "aie vieilli",
      "Nous": "ayons vieilli",
      "Vous": "ayez vieilli"
    },
    "Infinitif Présent": "vieiller",
    "Infinitif Passé": "avoir vieilli",
    "Participe Présent": "vieillant",
    "Participe Passé": "vieilli",
    "Gérondif Présent": "en vieillant",
    "Gérondif Passé": "en ayant vieilli"
  },
  "se méfier": {
    "Présent": {
      "Je": "me méfie",
      "Tu": "te méfies",
      "Il/Elle/On": "se méfie",
      "Nous": "nous méfions",
      "Vous": "vous méfiez",
      "Ils/Elle": "se méfient"
    },
    "Imparfait": {
      "Je": "me méfiais",
      "Tu": "te méfiais",
      "Il/Elle/On": "se méfiait",
      "Nous": "nous méfiions",
      "Vous": "vous méfiiez",
      "Ils/Elle": "se méfiaient"
    },
    "Passé Composé": {
      "Je": "me suis méfié",
      "Tu": "t'es méfié",
      "Il/Elle/On": "s'est méfié",
      "Nous": "nous sommes méfiés",
      "Vous": "vous êtes méfiés",
      "Ils/Elle": "se sont méfiés"
    },
    "Futur": {
      "Je": "me méfierai",
      "Tu": "te méfieras",
      "Il/Elle/On": "se méfiera",
      "Nous": "nous méfierons",
      "Vous": "vous méfierez",
      "Ils/Elle": "se méfieront"
    },
    "Plus-que-parfait": {
      "Je": "m'étais méfié",
      "Tu": "t'étais méfié",
      "Il/Elle/On": "s'était méfié",
      "Nous": "nous étions méfiés",
      "Vous": "vous étiez méfiés",
      "Ils/Elle": "s'étaient méfiés"
    },
    "Futur Simple": {
      "Je": "me méfierai",
      "Tu": "te méfieras",
      "Il/Elle/On": "se méfiera",
      "Nous": "nous méfierons",
      "Vous": "vous méfierez",
      "Ils/Elle": "se méfieront"
    },
    "Futur Antérieur": {
      "Je": "me serai méfié",
      "Tu": "te seras méfié",
      "Il/Elle/On": "se sera méfié",
      "Nous": "nous serons méfiés",
      "Vous": "vous serez méfiés",
      "Ils/Elle": "se seront méfiés"
    },
    "Conditionnel Présent": {
      "Je": "me méfierais",
      "Tu": "te méfierais",
      "Il/Elle/On": "se méfierait",
      "Nous": "nous méfierions",
      "Vous": "vous méfieriez",
      "Ils/Elle": "se méfieraient"
    },
    "Conditionnel Passé": {
      "Je": "me serais méfié",
      "Tu": "te serais méfié",
      "Il/Elle/On": "se serait méfié",
      "Nous": "nous serions méfiés",
      "Vous": "vous seriez méfiés",
      "Ils/Elle": "se seraient méfiés"
    },
    "Subjonctif Présent": {
      "Je": "me méfie",
      "Tu": "te méfies",
      "Il/Elle/On": "se méfie",
      "Nous": "nous méfiions",
      "Vous": "vous méfiiez",
      "Ils/Elle": "se méfient"
    },
    "Subjonctif Passé": {
      "Je": "me sois méfié",
      "Tu": "te sois méfié",
      "Il/Elle/On": "se soit méfié",
      "Nous": "nous soyons méfiés",
      "Vous": "vous soyez méfiés",
      "Ils/Elle": "se soient méfiés"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "me fusse méfié",
      "Tu": "te fusses méfié",
      "Il/Elle/On": "se fût méfié",
      "Nous": "nous fussions méfiés",
      "Vous": "vous fussiez méfiés",
      "Ils/Elle": "se fussent méfiés"
    },
    "Subjonctif Imparfait": {
      "Je": "me méfiasse",
      "Tu": "te méfiasse",
      "Il/Elle/On": "se méfiât",
      "Nous": "nous méfiassions",
      "Vous": "vous méfiassiez",
      "Ils/Elle": "se méfiassent"
    },
    "Impératif Présent": {
      "Tu": "méfie-toi",
      "Nous": "méfions-nous",
      "Vous": "méfiez-vous"
    },
    "Impératif Passé": {
      "Tu": "aie eu peur",
      "Nous": "ayons eu peur",
      "Vous": "ayez eu peur"
    },
    "Infinitif Présent": "se méfier",
    "Infinitif Passé": "s'être méfié",
    "Participe Présent": "se méfiant",
    "Participe Passé": "méfié",
    "Gérondif Présent": "en se méfiant",
    "Gérondif Passé": "en s'étant méfié"
  },
  "placer": {
    "Présent": {
      "Je": "place",
      "Tu": "places",
      "Il/Elle/On": "place",
      "Nous": "plaçons",
      "Vous": "placez",
      "Ils/Elle": "placent"
    },
    "Imparfait": {
      "Je": "plaçais",
      "Tu": "plaçais",
      "Il/Elle/On": "plaçait",
      "Nous": "placions",
      "Vous": "placiez",
      "Ils/Elle": "plaçaient"
    },
    "Passé Composé": {
      "Je": "ai placé",
      "Tu": "as placé",
      "Il/Elle/On": "a placé",
      "Nous": "avons placé",
      "Vous": "avez placé",
      "Ils/Elle": "ont placé"
    },
    "Futur": {
      "Je": "placerai",
      "Tu": "placeras",
      "Il/Elle/On": "placera",
      "Nous": "placerons",
      "Vous": "placerez",
      "Ils/Elle": "placeront"
    },
    "Plus-que-parfait": {
      "Je": "avais placé",
      "Tu": "avais placé",
      "Il/Elle/On": "avait placé",
      "Nous": "avions placé",
      "Vous": "aviez placé",
      "Ils/Elle": "avaient placé"
    },
    "Futur Simple": {
      "Je": "placerai",
      "Tu": "placeras",
      "Il/Elle/On": "placera",
      "Nous": "placerons",
      "Vous": "placerez",
      "Ils/Elle": "placeront"
    },
    "Futur Antérieur": {
      "Je": "aurai placé",
      "Tu": "auras placé",
      "Il/Elle/On": "aura placé",
      "Nous": "aurons placé",
      "Vous": "aurez placé",
      "Ils/Elle": "auront placé"
    },
    "Conditionnel Présent": {
      "Je": "placerais",
      "Tu": "placerais",
      "Il/Elle/On": "placerait",
      "Nous": "placerions",
      "Vous": "placeriez",
      "Ils/Elle": "placeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais placé",
      "Tu": "aurais placé",
      "Il/Elle/On": "aurait placé",
      "Nous": "aurions placé",
      "Vous": "auriez placé",
      "Ils/Elle": "auraient placé"
    },
    "Subjonctif Présent": {
      "Je": "place",
      "Tu": "places",
      "Il/Elle/On": "place",
      "Nous": "placions",
      "Vous": "placiez",
      "Ils/Elle": "placent"
    },
    "Subjonctif Passé": {
      "Je": "aie placé",
      "Tu": "aies placé",
      "Il/Elle/On": "ait placé",
      "Nous": "ayons placé",
      "Vous": "ayez placé",
      "Ils/Elle": "aient placé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse placé",
      "Tu": "eusses placé",
      "Il/Elle/On": "eût placé",
      "Nous": "eussions placé",
      "Vous": "eussiez placé",
      "Ils/Elle": "eussent placé"
    },
    "Subjonctif Imparfait": {
      "Je": "plaçasse",
      "Tu": "plaçasses",
      "Il/Elle/On": "plaçât",
      "Nous": "plaçassions",
      "Vous": "plaçassiez",
      "Ils/Elle": "plaçassent"
    },
    "Impératif Présent": {
      "Tu": "place",
      "Nous": "plaçons",
      "Vous": "placez"
    },
    "Impératif Passé": {
      "Tu": "aie placé",
      "Nous": "ayons placé",
      "Vous": "ayez placé"
    },
    "Infinitif Présent": "placer",
    "Infinitif Passé": "avoir placé",
    "Participe Présent": "plaçant",
    "Participe Passé": "placé",
    "Gérondif Présent": "en plaçant",
    "Gérondif Passé": "en ayant placé"
  },
  "manger": {
    "Présent": {
      "Je": "mange",
      "Tu": "manges",
      "Il/Elle/On": "mange",
      "Nous": "mangeons",
      "Vous": "mangez",
      "Ils/Elle": "mangent"
    },
    "Imparfait": {
      "Je": "mangeais",
      "Tu": "mangeais",
      "Il/Elle/On": "mangeait",
      "Nous": "mangions",
      "Vous": "mangiez",
      "Ils/Elle": "mangeaient"
    },
    "Passé Composé": {
      "Je": "ai mangé",
      "Tu": "as mangé",
      "Il/Elle/On": "a mangé",
      "Nous": "avons mangé",
      "Vous": "avez mangé",
      "Ils/Elle": "ont mangé"
    },
    "Futur": {
      "Je": "mangerai",
      "Tu": "mangeras",
      "Il/Elle/On": "mangera",
      "Nous": "mangerons",
      "Vous": "mangerez",
      "Ils/Elle": "mangeront"
    },
    "Plus-que-parfait": {
      "Je": "avais mangé",
      "Tu": "avais mangé",
      "Il/Elle/On": "avait mangé",
      "Nous": "avions mangé",
      "Vous": "aviez mangé",
      "Ils/Elle": "avaient mangé"
    },
    "Futur Simple": {
      "Je": "mangerai",
      "Tu": "mangeras",
      "Il/Elle/On": "mangera",
      "Nous": "mangerons",
      "Vous": "mangerez",
      "Ils/Elle": "mangeront"
    },
    "Futur Antérieur": {
      "Je": "aurai mangé",
      "Tu": "auras mangé",
      "Il/Elle/On": "aura mangé",
      "Nous": "aurons mangé",
      "Vous": "aurez mangé",
      "Ils/Elle": "auront mangé"
    },
    "Conditionnel Présent": {
      "Je": "mangerais",
      "Tu": "mangerais",
      "Il/Elle/On": "mangerait",
      "Nous": "mangerions",
      "Vous": "mangeriez",
      "Ils/Elle": "mangeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais mangé",
      "Tu": "aurais mangé",
      "Il/Elle/On": "aurait mangé",
      "Nous": "aurions mangé",
      "Vous": "auriez mangé",
      "Ils/Elle": "auraient mangé"
    },
    "Subjonctif Présent": {
      "Je": "mange",
      "Tu": "manges",
      "Il/Elle/On": "mange",
      "Nous": "mangions",
      "Vous": "mangiez",
      "Ils/Elle": "mangent"
    },
    "Subjonctif Passé": {
      "Je": "aie mangé",
      "Tu": "aies mangé",
      "Il/Elle/On": "ait mangé",
      "Nous": "ayons mangé",
      "Vous": "ayez mangé",
      "Ils/Elle": "aient mangé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse mangé",
      "Tu": "eusses mangé",
      "Il/Elle/On": "eût mangé",
      "Nous": "eussions mangé",
      "Vous": "eussiez mangé",
      "Ils/Elle": "eussent mangé"
    },
    "Subjonctif Imparfait": {
      "Je": "mangeasse",
      "Tu": "mangeasses",
      "Il/Elle/On": "mangeât",
      "Nous": "mangeassions",
      "Vous": "mangeassiez",
      "Ils/Elle": "mangeassent"
    },
    "Impératif Présent": {
      "Tu": "mange",
      "Nous": "mangeons",
      "Vous": "mangez"
    },
    "Impératif Passé": {
      "Tu": "aie mangé",
      "Nous": "ayons mangé",
      "Vous": "ayez mangé"
    },
    "Infinitif Présent": "manger",
    "Infinitif Passé": "avoir mangé",
    "Participe Présent": "mangeant",
    "Participe Passé": "mangé",
    "Gérondif Présent": "en mangeant",
    "Gérondif Passé": "en ayant mangé"
  },
  "peser": {
    "Présent": {
      "Je": "pèse",
      "Tu": "pèses",
      "Il/Elle/On": "pèse",
      "Nous": "pesons",
      "Vous": "pesez",
      "Ils/Elle": "pèsent"
    },
    "Imparfait": {
      "Je": "pesais",
      "Tu": "pesais",
      "Il/Elle/On": "pesait",
      "Nous": "pesions",
      "Vous": "pesiez",
      "Ils/Elle": "pesaient"
    },
    "Passé Composé": {
      "Je": "ai pesé",
      "Tu": "as pesé",
      "Il/Elle/On": "a pesé",
      "Nous": "avons pesé",
      "Vous": "avez pesé",
      "Ils/Elle": "ont pesé"
    },
    "Futur": {
      "Je": "pèserai",
      "Tu": "pèseras",
      "Il/Elle/On": "pèsera",
      "Nous": "pèserons",
      "Vous": "pèserez",
      "Ils/Elle": "pèseront"
    },
    "Plus-que-parfait": {
      "Je": "avais pesé",
      "Tu": "avais pesé",
      "Il/Elle/On": "avait pesé",
      "Nous": "avions pesé",
      "Vous": "aviez pesé",
      "Ils/Elle": "avaient pesé"
    },
    "Futur Simple": {
      "Je": "pèserai",
      "Tu": "pèseras",
      "Il/Elle/On": "pèsera",
      "Nous": "pèserons",
      "Vous": "pèserez",
      "Ils/Elle": "pèseront"
    },
    "Futur Antérieur": {
      "Je": "aurai pesé",
      "Tu": "auras pesé",
      "Il/Elle/On": "aura pesé",
      "Nous": "aurons pesé",
      "Vous": "aurez pesé",
      "Ils/Elle": "auront pesé"
    },
    "Conditionnel Présent": {
      "Je": "pèserais",
      "Tu": "pèserais",
      "Il/Elle/On": "pèserait",
      "Nous": "pèserions",
      "Vous": "pèseriez",
      "Ils/Elle": "pèseraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais pesé",
      "Tu": "aurais pesé",
      "Il/Elle/On": "aurait pesé",
      "Nous": "aurions pesé",
      "Vous": "auriez pesé",
      "Ils/Elle": "auraient pesé"
    },
    "Subjonctif Présent": {
      "Je": "pèse",
      "Tu": "pèses",
      "Il/Elle/On": "pèse",
      "Nous": "pesions",
      "Vous": "pesiez",
      "Ils/Elle": "pèsent"
    },
    "Subjonctif Passé": {
      "Je": "aie pesé",
      "Tu": "aies pesé",
      "Il/Elle/On": "ait pesé",
      "Nous": "ayons pesé",
      "Vous": "ayez pesé",
      "Ils/Elle": "aient pesé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse pesé",
      "Tu": "eusses pesé",
      "Il/Elle/On": "eût pesé",
      "Nous": "eussions pesé",
      "Vous": "eussiez pesé",
      "Ils/Elle": "eussent pesé"
    },
    "Subjonctif Imparfait": {
      "Je": "pesasse",
      "Tu": "pesasses",
      "Il/Elle/On": "pesât",
      "Nous": "pesassions",
      "Vous": "pesassiez",
      "Ils/Elle": "pesassent"
    },
    "Impératif Présent": {
      "Tu": "pèse",
      "Nous": "pesons",
      "Vous": "pesez"
    },
    "Impératif Passé": {
      "Tu": "aie pesé",
      "Nous": "ayons pesé",
      "Vous": "ayez pesé"
    },
    "Infinitif Présent": "peser",
    "Infinitif Passé": "avoir pesé",
    "Participe Présent": "pesant",
    "Participe Passé": "pesé",
    "Gérondif Présent": "en pesant",
    "Gérondif Passé": "en ayant pesé"
  },
  "céder": {
    "Présent": {
      "Je": "cède",
      "Tu": "cèdes",
      "Il/Elle/On": "cède",
      "Nous": "cédons",
      "Vous": "cédez",
      "Ils/Elle": "cèdent"
    },
    "Imparfait": {
      "Je": "cédais",
      "Tu": "cédais",
      "Il/Elle/On": "cédait",
      "Nous": "cédions",
      "Vous": "cédiez",
      "Ils/Elle": "cédaient"
    },
    "Passé Composé": {
      "Je": "ai cédé",
      "Tu": "as cédé",
      "Il/Elle/On": "a cédé",
      "Nous": "avons cédé",
      "Vous": "avez cédé",
      "Ils/Elle": "ont cédé"
    },
    "Futur": {
      "Je": "céderai",
      "Tu": "céderas",
      "Il/Elle/On": "cédera",
      "Nous": "céderons",
      "Vous": "cédez",
      "Ils/Elle": "céderont"
    },
    "Plus-que-parfait": {
      "Je": "avais cédé",
      "Tu": "avais cédé",
      "Il/Elle/On": "avait cédé",
      "Nous": "avions cédé",
      "Vous": "aviez cédé",
      "Ils/Elle": "avaient cédé"
    },
    "Futur Simple": {
      "Je": "céderai",
      "Tu": "céderas",
      "Il/Elle/On": "cédera",
      "Nous": "céderons",
      "Vous": "cédez",
      "Ils/Elle": "céderont"
    },
    "Futur Antérieur": {
      "Je": "aurai cédé",
      "Tu": "auras cédé",
      "Il/Elle/On": "aura cédé",
      "Nous": "aurons cédé",
      "Vous": "aurez cédé",
      "Ils/Elle": "auront cédé"
    },
    "Conditionnel Présent": {
      "Je": "céderais",
      "Tu": "céderais",
      "Il/Elle/On": "céderait",
      "Nous": "céderions",
      "Vous": "céderiez",
      "Ils/Elle": "céderaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais cédé",
      "Tu": "aurais cédé",
      "Il/Elle/On": "aurait cédé",
      "Nous": "aurions cédé",
      "Vous": "auriez cédé",
      "Ils/Elle": "auraient cédé"
    },
    "Subjonctif Présent": {
      "Je": "cède",
      "Tu": "cèdes",
      "Il/Elle/On": "cède",
      "Nous": "cédions",
      "Vous": "cédiez",
      "Ils/Elle": "cèdent"
    },
    "Subjonctif Passé": {
      "Je": "aie cédé",
      "Tu": "aies cédé",
      "Il/Elle/On": "ait cédé",
      "Nous": "ayons cédé",
      "Vous": "ayez cédé",
      "Ils/Elle": "aient cédé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse cédé",
      "Tu": "eusses cédé",
      "Il/Elle/On": "eût cédé",
      "Nous": "eussions cédé",
      "Vous": "eussiez cédé",
      "Ils/Elle": "eussent cédé"
    },
    "Subjonctif Imparfait": {
      "Je": "cédasse",
      "Tu": "cédasses",
      "Il/Elle/On": "cédât",
      "Nous": "cédassions",
      "Vous": "cédassiez",
      "Ils/Elle": "cédassent"
    },
    "Impératif Présent": {
      "Tu": "cède",
      "Nous": "cédons",
      "Vous": "cédez"
    },
    "Impératif Passé": {
      "Tu": "aie cédé",
      "Nous": "ayons cédé",
      "Vous": "ayez cédé"
    },
    "Infinitif Présent": "céder",
    "Infinitif Passé": "avoir cédé",
    "Participe Présent": "cédant",
    "Participe Passé": "cédé",
    "Gérondif Présent": "en cédant",
    "Gérondif Passé": "en ayant cédé"
  },
  "modeler": {
    "Présent": {
      "Je": "modèle",
      "Tu": "modèles",
      "Il/Elle/On": "modèle",
      "Nous": "modelons",
      "Vous": "modelez",
      "Ils/Elle": "modèlent"
    },
    "Imparfait": {
      "Je": "modelais",
      "Tu": "modelais",
      "Il/Elle/On": "modelait",
      "Nous": "modelions",
      "Vous": "modeliez",
      "Ils/Elle": "modèlaient"
    },
    "Passé Composé": {
      "Je": "ai modelé",
      "Tu": "as modelé",
      "Il/Elle/On": "a modelé",
      "Nous": "avons modelé",
      "Vous": "avez modelé",
      "Ils/Elle": "ont modelé"
    },
    "Futur": {
      "Je": "modelerai",
      "Tu": "modeleras",
      "Il/Elle/On": "modelera",
      "Nous": "modelerons",
      "Vous": "modelerez",
      "Ils/Elle": "modeleront"
    },
    "Plus-que-parfait": {
      "Je": "avais modelé",
      "Tu": "avais modelé",
      "Il/Elle/On": "avait modelé",
      "Nous": "avions modelé",
      "Vous": "aviez modelé",
      "Ils/Elle": "avaient modelé"
    },
    "Futur Simple": {
      "Je": "modelerai",
      "Tu": "modeleras",
      "Il/Elle/On": "modelera",
      "Nous": "modelerons",
      "Vous": "modelerez",
      "Ils/Elle": "modeleront"
    },
    "Futur Antérieur": {
      "Je": "aurai modelé",
      "Tu": "auras modelé",
      "Il/Elle/On": "aura modelé",
      "Nous": "aurons modelé",
      "Vous": "aurez modelé",
      "Ils/Elle": "auront modelé"
    },
    "Conditionnel Présent": {
      "Je": "modelerais",
      "Tu": "modelerais",
      "Il/Elle/On": "modelerait",
      "Nous": "modelerions",
      "Vous": "modeleriez",
      "Ils/Elle": "modeleraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais modelé",
      "Tu": "aurais modelé",
      "Il/Elle/On": "aurait modelé",
      "Nous": "aurions modelé",
      "Vous": "auriez modelé",
      "Ils/Elle": "auraient modelé"
    },
    "Subjonctif Présent": {
      "Je": "modèle",
      "Tu": "modèles",
      "Il/Elle/On": "modèle",
      "Nous": "modelions",
      "Vous": "modeliez",
      "Ils/Elle": "modèlent"
    },
    "Subjonctif Passé": {
      "Je": "aie modelé",
      "Tu": "aies modelé",
      "Il/Elle/On": "ait modelé",
      "Nous": "ayons modelé",
      "Vous": "ayez modelé",
      "Ils/Elle": "aient modelé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse modelé",
      "Tu": "eusses modelé",
      "Il/Elle/On": "eût modelé",
      "Nous": "eussions modelé",
      "Vous": "eussiez modelé",
      "Ils/Elle": "eussent modelé"
    },
    "Subjonctif Imparfait": {
      "Je": "modelasse",
      "Tu": "modelasses",
      "Il/Elle/On": "modelât",
      "Nous": "modelassions",
      "Vous": "modelassiez",
      "Ils/Elle": "modelassent"
    },
    "Impératif Présent": {
      "Tu": "modèle",
      "Nous": "modelons",
      "Vous": "modelez"
    },
    "Impératif Passé": {
      "Tu": "aie modelé",
      "Nous": "ayons modelé",
      "Vous": "ayez modelé"
    },
    "Infinitif Présent": "modeler",
    "Infinitif Passé": "avoir modelé",
    "Participe Présent": "modelant",
    "Participe Passé": "modelé",
    "Gérondif Présent": "en modelant",
    "Gérondif Passé": "en ayant modelé"
  },
  "jeter": {
    "Présent": {
      "Je": "jette",
      "Tu": "jettes",
      "Il/Elle/On": "jette",
      "Nous": "jetons",
      "Vous": "jetez",
      "Ils/Elle": "jettent"
    },
    "Imparfait": {
      "Je": "jetais",
      "Tu": "jetais",
      "Il/Elle/On": "jetait",
      "Nous": "jetions",
      "Vous": "jetiez",
      "Ils/Elle": "jetaient"
    },
    "Passé Composé": {
      "Je": "ai jeté",
      "Tu": "as jeté",
      "Il/Elle/On": "a jeté",
      "Nous": "avons jeté",
      "Vous": "avez jeté",
      "Ils/Elle": "ont jeté"
    },
    "Futur": {
      "Je": "jetterai",
      "Tu": "jetteras",
      "Il/Elle/On": "jettera",
      "Nous": "jetterons",
      "Vous": "jetterez",
      "Ils/Elle": "jetteront"
    },
    "Plus-que-parfait": {
      "Je": "avais jeté",
      "Tu": "avais jeté",
      "Il/Elle/On": "avait jeté",
      "Nous": "avions jeté",
      "Vous": "aviez jeté",
      "Ils/Elle": "avaient jeté"
    },
    "Futur Simple": {
      "Je": "jetterai",
      "Tu": "jetteras",
      "Il/Elle/On": "jettera",
      "Nous": "jetterons",
      "Vous": "jetterez",
      "Ils/Elle": "jetteront"
    },
    "Futur Antérieur": {
      "Je": "aurai jeté",
      "Tu": "auras jeté",
      "Il/Elle/On": "aura jeté",
      "Nous": "aurons jeté",
      "Vous": "aurez jeté",
      "Ils/Elle": "auront jeté"
    },
    "Conditionnel Présent": {
      "Je": "jetterais",
      "Tu": "jetterais",
      "Il/Elle/On": "jetterait",
      "Nous": "jetterions",
      "Vous": "jetteriez",
      "Ils/Elle": "jetteraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais jeté",
      "Tu": "aurais jeté",
      "Il/Elle/On": "aurait jeté",
      "Nous": "aurions jeté",
      "Vous": "auriez jeté",
      "Ils/Elle": "auraient jeté"
    },
    "Subjonctif Présent": {
      "Je": "jette",
      "Tu": "jettes",
      "Il/Elle/On": "jette",
      "Nous": "jetions",
      "Vous": "jetiez",
      "Ils/Elle": "jettent"
    },
    "Subjonctif Passé": {
      "Je": "aie jeté",
      "Tu": "aies jeté",
      "Il/Elle/On": "ait jeté",
      "Nous": "ayons jeté",
      "Vous": "ayez jeté",
      "Ils/Elle": "aient jeté"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse jeté",
      "Tu": "eusses jeté",
      "Il/Elle/On": "eût jeté",
      "Nous": "eussions jeté",
      "Vous": "eussiez jeté",
      "Ils/Elle": "eussent jeté"
    },
    "Subjonctif Imparfait": {
      "Je": "jetasse",
      "Tu": "jetasses",
      "Il/Elle/On": "jetât",
      "Nous": "jetassions",
      "Vous": "jetassiez",
      "Ils/Elle": "jetassent"
    },
    "Impératif Présent": {
      "Tu": "jette",
      "Nous": "jetons",
      "Vous": "jetez"
    },
    "Impératif Passé": {
      "Tu": "aie jeté",
      "Nous": "ayons jeté",
      "Vous": "ayez jeté"
    },
    "Infinitif Présent": "jeter",
    "Infinitif Passé": "avoir jeté",
    "Participe Présent": "jetant",
    "Participe Passé": "jeté",
    "Gérondif Présent": "en jetant",
    "Gérondif Passé": "en ayant jeté"
  },
  "créer": {
    "Présent": {
      "Je": "crée",
      "Tu": "crées",
      "Il/Elle/On": "crée",
      "Nous": "créons",
      "Vous": "créez",
      "Ils/Elle": "créent"
    },
    "Imparfait": {
      "Je": "créais",
      "Tu": "créais",
      "Il/Elle/On": "créait",
      "Nous": "créions",
      "Vous": "créiez",
      "Ils/Elle": "créaient"
    },
    "Passé Composé": {
      "Je": "ai créé",
      "Tu": "as créé",
      "Il/Elle/On": "a créé",
      "Nous": "avons créé",
      "Vous": "avez créé",
      "Ils/Elle": "ont créé"
    },
    "Futur": {
      "Je": "créerai",
      "Tu": "créeras",
      "Il/Elle/On": "créera",
      "Nous": "créerons",
      "Vous": "créerez",
      "Ils/Elle": "créeront"
    },
    "Plus-que-parfait": {
      "Je": "avais créé",
      "Tu": "avais créé",
      "Il/Elle/On": "avait créé",
      "Nous": "avions créé",
      "Vous": "aviez créé",
      "Ils/Elle": "avaient créé"
    },
    "Futur Simple": {
      "Je": "créerai",
      "Tu": "créeras",
      "Il/Elle/On": "créera",
      "Nous": "créerons",
      "Vous": "créerez",
      "Ils/Elle": "créeront"
    },
    "Futur Antérieur": {
      "Je": "aurai créé",
      "Tu": "auras créé",
      "Il/Elle/On": "aura créé",
      "Nous": "aurons créé",
      "Vous": "aurez créé",
      "Ils/Elle": "auront créé"
    },
    "Conditionnel Présent": {
      "Je": "créerais",
      "Tu": "créerais",
      "Il/Elle/On": "créerait",
      "Nous": "créerions",
      "Vous": "créeriez",
      "Ils/Elle": "créeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais créé",
      "Tu": "aurais créé",
      "Il/Elle/On": "aurait créé",
      "Nous": "aurions créé",
      "Vous": "auriez créé",
      "Ils/Elle": "auraient créé"
    },
    "Subjonctif Présent": {
      "Je": "crée",
      "Tu": "crées",
      "Il/Elle/On": "crée",
      "Nous": "créions",
      "Vous": "créiez",
      "Ils/Elle": "créent"
    },
    "Subjonctif Passé": {
      "Je": "aie créé",
      "Tu": "aies créé",
      "Il/Elle/On": "ait créé",
      "Nous": "ayons créé",
      "Vous": "ayez créé",
      "Ils/Elle": "aient créé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse créé",
      "Tu": "eusses créé",
      "Il/Elle/On": "eût créé",
      "Nous": "eussions créé",
      "Vous": "eussiez créé",
      "Ils/Elle": "eussent créé"
    },
    "Subjonctif Imparfait": {
      "Je": "créasse",
      "Tu": "créasses",
      "Il/Elle/On": "créât",
      "Nous": "créassions",
      "Vous": "créassiez",
      "Ils/Elle": "créassent"
    },
    "Impératif Présent": {
      "Tu": "crée",
      "Nous": "créons",
      "Vous": "créez"
    },
    "Impératif Passé": {
      "Tu": "aie créé",
      "Nous": "ayons créé",
      "Vous": "ayez créé"
    },
    "Infinitif Présent": "créer",
    "Infinitif Passé": "avoir créé",
    "Participe Présent": "créant",
    "Participe Passé": "créé",
    "Gérondif Présent": "en créant",
    "Gérondif Passé": "en ayant créé"
  },
  "assiéger": {
    "Présent": {
      "Je": "assiège",
      "Tu": "assièges",
      "Il/Elle/On": "assiège",
      "Nous": "assiégeons",
      "Vous": "assiégez",
      "Ils/Elle": "assiègent"
    },
    "Imparfait": {
      "Je": "assiégeais",
      "Tu": "assiégeais",
      "Il/Elle/On": "assiégeait",
      "Nous": "assiégions",
      "Vous": "assiégiez",
      "Ils/Elle": "assiégeaient"
    },
    "Passé Composé": {
      "Je": "ai assiégé",
      "Tu": "as assiégé",
      "Il/Elle/On": "a assiégé",
      "Nous": "avons assiégé",
      "Vous": "avez assiégé",
      "Ils/Elle": "ont assiégé"
    },
    "Futur": {
      "Je": "assiégerai",
      "Tu": "assiégeras",
      "Il/Elle/On": "assiégera",
      "Nous": "assiégerons",
      "Vous": "assiégerez",
      "Ils/Elle": "assiégeront"
    },
    "Plus-que-parfait": {
      "Je": "avais assiégé",
      "Tu": "avais assiégé",
      "Il/Elle/On": "avait assiégé",
      "Nous": "avions assiégé",
      "Vous": "aviez assiégé",
      "Ils/Elle": "avaient assiégé"
    },
    "Futur Simple": {
      "Je": "assiégerai",
      "Tu": "assiégeras",
      "Il/Elle/On": "assiégera",
      "Nous": "assiégerons",
      "Vous": "assiégerez",
      "Ils/Elle": "assiégeront"
    },
    "Futur Antérieur": {
      "Je": "aurai assiégé",
      "Tu": "auras assiégé",
      "Il/Elle/On": "aura assiégé",
      "Nous": "aurons assiégé",
      "Vous": "aurez assiégé",
      "Ils/Elle": "auront assiégé"
    },
    "Conditionnel Présent": {
      "Je": "assiégerais",
      "Tu": "assiégerais",
      "Il/Elle/On": "assiégerait",
      "Nous": "assiégerions",
      "Vous": "assiégeriez",
      "Ils/Elle": "assiégeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais assiégé",
      "Tu": "aurais assiégé",
      "Il/Elle/On": "aurait assiégé",
      "Nous": "aurions assiégé",
      "Vous": "auriez assiégé",
      "Ils/Elle": "auraient assiégé"
    },
    "Subjonctif Présent": {
      "Je": "assiège",
      "Tu": "assièges",
      "Il/Elle/On": "assiège",
      "Nous": "assiégions",
      "Vous": "assiégiez",
      "Ils/Elle": "assiègent"
    },
    "Subjonctif Passé": {
      "Je": "aie assiégé",
      "Tu": "aies assiégé",
      "Il/Elle/On": "ait assiégé",
      "Nous": "ayons assiégé",
      "Vous": "ayez assiégé",
      "Ils/Elle": "aient assiégé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse assiégé",
      "Tu": "eusses assiégé",
      "Il/Elle/On": "eût assiégé",
      "Nous": "eussions assiégé",
      "Vous": "eussiez assiégé",
      "Ils/Elle": "eussent assiégé"
    },
    "Subjonctif Imparfait": {
      "Je": "assiégeasse",
      "Tu": "assiégeasses",
      "Il/Elle/On": "assiégeât",
      "Nous": "assiégeassions",
      "Vous": "assiégeassiez",
      "Ils/Elle": "assiégeassent"
    },
    "Impératif Présent": {
      "Tu": "assiège",
      "Nous": "assiégeons",
      "Vous": "assiégez"
    },
    "Impératif Passé": {
      "Tu": "aie assiégé",
      "Nous": "ayons assiégé",
      "Vous": "ayez assiégé"
    },
    "Infinitif Présent": "assiéger",
    "Infinitif Passé": "avoir assiégé",
    "Participe Présent": "assiégeant",
    "Participe Passé": "assiégé",
    "Gérondif Présent": "en assiégeant",
    "Gérondif Passé": "en ayant assiégé"
  },
  "apprécier": {
    "Présent": {
      "Je": "apprécie",
      "Tu": "apprécies",
      "Il/Elle/On": "apprécie",
      "Nous": "apprécions",
      "Vous": "appréciez",
      "Ils/Elle": "apprécient"
    },
    "Imparfait": {
      "Je": "appréciais",
      "Tu": "appréciais",
      "Il/Elle/On": "appréciait",
      "Nous": "appréciions",
      "Vous": "appréciiez",
      "Ils/Elle": "appréciaient"
    },
    "Passé Composé": {
      "Je": "ai apprécié",
      "Tu": "as apprécié",
      "Il/Elle/On": "a apprécié",
      "Nous": "avons apprécié",
      "Vous": "avez apprécié",
      "Ils/Elle": "ont apprécié"
    },
    "Futur": {
      "Je": "apprécierai",
      "Tu": "apprécieras",
      "Il/Elle/On": "appréciera",
      "Nous": "apprécierons",
      "Vous": "apprécierez",
      "Ils/Elle": "apprécieront"
    },
    "Plus-que-parfait": {
      "Je": "avais apprécié",
      "Tu": "avais apprécié",
      "Il/Elle/On": "avait apprécié",
      "Nous": "avions apprécié",
      "Vous": "aviez apprécié",
      "Ils/Elle": "avaient apprécié"
    },
    "Futur Simple": {
      "Je": "apprécierai",
      "Tu": "apprécieras",
      "Il/Elle/On": "appréciera",
      "Nous": "apprécierons",
      "Vous": "apprécierez",
      "Ils/Elle": "apprécieront"
    },
    "Futur Antérieur": {
      "Je": "aurai apprécié",
      "Tu": "auras apprécié",
      "Il/Elle/On": "aura apprécié",
      "Nous": "aurons apprécié",
      "Vous": "aurez apprécié",
      "Ils/Elle": "auront apprécié"
    },
    "Conditionnel Présent": {
      "Je": "apprécierais",
      "Tu": "apprécierais",
      "Il/Elle/On": "apprécierait",
      "Nous": "apprécierions",
      "Vous": "apprécieriez",
      "Ils/Elle": "apprécieraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais apprécié",
      "Tu": "aurais apprécié",
      "Il/Elle/On": "aurait apprécié",
      "Nous": "aurions apprécié",
      "Vous": "auriez apprécié",
      "Ils/Elle": "auraient apprécié"
    },
    "Subjonctif Présent": {
      "Je": "apprécie",
      "Tu": "apprécies",
      "Il/Elle/On": "apprécie",
      "Nous": "appréciions",
      "Vous": "appréciiez",
      "Ils/Elle": "apprécient"
    },
    "Subjonctif Passé": {
      "Je": "aie apprécié",
      "Tu": "aies apprécié",
      "Il/Elle/On": "ait apprécié",
      "Nous": "ayons apprécié",
      "Vous": "ayez apprécié",
      "Ils/Elle": "aient apprécié"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse apprécié",
      "Tu": "eusses apprécié",
      "Il/Elle/On": "eût apprécié",
      "Nous": "eussions apprécié",
      "Vous": "eussiez apprécié",
      "Ils/Elle": "eussent apprécié"
    },
    "Subjonctif Imparfait": {
      "Je": "appréciasse",
      "Tu": "appréciasses",
      "Il/Elle/On": "appréciât",
      "Nous": "appréciassions",
      "Vous": "appréciassiez",
      "Ils/Elle": "appréciassent"
    },
    "Impératif Présent": {
      "Tu": "apprécie",
      "Nous": "apprécions",
      "Vous": "appréciez"
    },
    "Impératif Passé": {
      "Tu": "aie apprécié",
      "Nous": "ayons apprécié",
      "Vous": "ayez apprécié"
    },
    "Infinitif Présent": "apprécier",
    "Infinitif Passé": "avoir apprécié",
    "Participe Présent": "appréciant",
    "Participe Passé": "apprécié",
    "Gérondif Présent": "en appréciant",
    "Gérondif Passé": "en ayant apprécié"
  },
  "payer": {
    "Présent": {
      "Je": "paie",
      "Tu": "paies",
      "Il/Elle/On": "paie",
      "Nous": "payons",
      "Vous": "payez",
      "Ils/Elle": "paient"
    },
    "Imparfait": {
      "Je": "payais",
      "Tu": "payais",
      "Il/Elle/On": "payait",
      "Nous": "payions",
      "Vous": "payiez",
      "Ils/Elle": "payaient"
    },
    "Passé Composé": {
      "Je": "ai payé",
      "Tu": "as payé",
      "Il/Elle/On": "a payé",
      "Nous": "avons payé",
      "Vous": "avez payé",
      "Ils/Elle": "ont payé"
    },
    "Futur": {
      "Je": "paierai",
      "Tu": "paieras",
      "Il/Elle/On": "paiera",
      "Nous": "paierons",
      "Vous": "paierez",
      "Ils/Elle": "paieront"
    },
    "Plus-que-parfait": {
      "Je": "avais payé",
      "Tu": "avais payé",
      "Il/Elle/On": "avait payé",
      "Nous": "avions payé",
      "Vous": "aviez payé",
      "Ils/Elle": "avaient payé"
    },
    "Futur Simple": {
      "Je": "paierai",
      "Tu": "paieras",
      "Il/Elle/On": "paiera",
      "Nous": "paierons",
      "Vous": "paierez",
      "Ils/Elle": "paieront"
    },
    "Futur Antérieur": {
      "Je": "aurai payé",
      "Tu": "auras payé",
      "Il/Elle/On": "aura payé",
      "Nous": "aurons payé",
      "Vous": "aurez payé",
      "Ils/Elle": "auront payé"
    },
    "Conditionnel Présent": {
      "Je": "paierais",
      "Tu": "paierais",
      "Il/Elle/On": "paierait",
      "Nous": "paierions",
      "Vous": "paieriez",
      "Ils/Elle": "paieraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais payé",
      "Tu": "aurais payé",
      "Il/Elle/On": "aurait payé",
      "Nous": "aurions payé",
      "Vous": "auriez payé",
      "Ils/Elle": "auraient payé"
    },
    "Subjonctif Présent": {
      "Je": "paie",
      "Tu": "paies",
      "Il/Elle/On": "paie",
      "Nous": "payions",
      "Vous": "payiez",
      "Ils/Elle": "paient"
    },
    "Subjonctif Passé": {
      "Je": "aie payé",
      "Tu": "aies payé",
      "Il/Elle/On": "ait payé",
      "Nous": "ayons payé",
      "Vous": "ayez payé",
      "Ils/Elle": "aient payé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse payé",
      "Tu": "eusses payé",
      "Il/Elle/On": "eût payé",
      "Nous": "eussions payé",
      "Vous": "eussiez payé",
      "Ils/Elle": "eussent payé"
    },
    "Subjonctif Imparfait": {
      "Je": "payasse",
      "Tu": "payasses",
      "Il/Elle/On": "payât",
      "Nous": "payassions",
      "Vous": "payassiez",
      "Ils/Elle": "payassent"
    },
    "Impératif Présent": {
      "Tu": "paie",
      "Nous": "payons",
      "Vous": "payez"
    },
    "Impératif Passé": {
      "Tu": "aie payé",
      "Nous": "ayons payé",
      "Vous": "ayez payé"
    },
    "Infinitif Présent": "payer",
    "Infinitif Passé": "avoir payé",
    "Participe Présent": "payant",
    "Participe Passé": "payé",
    "Gérondif Présent": "en payant",
    "Gérondif Passé": "en ayant payé"
  },
  "broyer": {
    "Présent": {
      "Je": "broie",
      "Tu": "broies",
      "Il/Elle/On": "broie",
      "Nous": "broyons",
      "Vous": "broyez",
      "Ils/Elle": "broient"
    },
    "Imparfait": {
      "Je": "broyais",
      "Tu": "broyais",
      "Il/Elle/On": "broyait",
      "Nous": "broyions",
      "Vous": "broyiez",
      "Ils/Elle": "broyaient"
    },
    "Passé Composé": {
      "Je": "ai broyé",
      "Tu": "as broyé",
      "Il/Elle/On": "a broyé",
      "Nous": "avons broyé",
      "Vous": "avez broyé",
      "Ils/Elle": "ont broyé"
    },
    "Futur": {
      "Je": "broyerai",
      "Tu": "broyeras",
      "Il/Elle/On": "broyera",
      "Nous": "broyerons",
      "Vous": "broyerez",
      "Ils/Elle": "broyeront"
    },
    "Plus-que-parfait": {
      "Je": "avais broyé",
      "Tu": "avais broyé",
      "Il/Elle/On": "avait broyé",
      "Nous": "avions broyé",
      "Vous": "aviez broyé",
      "Ils/Elle": "avaient broyé"
    },
    "Futur Simple": {
      "Je": "broyerai",
      "Tu": "broyeras",
      "Il/Elle/On": "broyera",
      "Nous": "broyerons",
      "Vous": "broyerez",
      "Ils/Elle": "broyeront"
    },
    "Futur Antérieur": {
      "Je": "aurai broyé",
      "Tu": "auras broyé",
      "Il/Elle/On": "aura broyé",
      "Nous": "aurons broyé",
      "Vous": "aurez broyé",
      "Ils/Elle": "auront broyé"
    },
    "Conditionnel Présent": {
      "Je": "broyerais",
      "Tu": "broyerais",
      "Il/Elle/On": "broyerait",
      "Nous": "broyerions",
      "Vous": "broyeriez",
      "Ils/Elle": "broyeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais broyé",
      "Tu": "aurais broyé",
      "Il/Elle/On": "aurait broyé",
      "Nous": "aurions broyé",
      "Vous": "auriez broyé",
      "Ils/Elle": "auraient broyé"
    },
    "Subjonctif Présent": {
      "Je": "broie",
      "Tu": "broies",
      "Il/Elle/On": "broie",
      "Nous": "broyions",
      "Vous": "broyiez",
      "Ils/Elle": "broient"
    },
    "Subjonctif Passé": {
      "Je": "aie broyé",
      "Tu": "aies broyé",
      "Il/Elle/On": "ait broyé",
      "Nous": "ayons broyé",
      "Vous": "ayez broyé",
      "Ils/Elle": "aient broyé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse broyé",
      "Tu": "eusses broyé",
      "Il/Elle/On": "eût broyé",
      "Nous": "eussions broyé",
      "Vous": "eussiez broyé",
      "Ils/Elle": "eussent broyé"
    },
    "Subjonctif Imparfait": {
      "Je": "broyasse",
      "Tu": "broyasses",
      "Il/Elle/On": "broyât",
      "Nous": "broyassions",
      "Vous": "broyassiez",
      "Ils/Elle": "broyassent"
    },
    "Impératif Présent": {
      "Tu": "broie",
      "Nous": "broyons",
      "Vous": "broyez"
    },
    "Impératif Passé": {
      "Tu": "aie broyé",
      "Nous": "ayons broyé",
      "Vous": "ayez broyé"
    },
    "Infinitif Présent": "broyer",
    "Infinitif Passé": "avoir broyé",
    "Participe Présent": "broyant",
    "Participe Passé": "broyé",
    "Gérondif Présent": "en broyant",
    "Gérondif Passé": "en ayant broyé"
  },
  "broyer": {
    "Présent": {
      "Je": "broie",
      "Tu": "broies",
      "Il/Elle/On": "broie",
      "Nous": "broyons",
      "Vous": "broyez",
      "Ils/Elle": "broient"
    },
    "Imparfait": {
      "Je": "broyais",
      "Tu": "broyais",
      "Il/Elle/On": "broyait",
      "Nous": "broyions",
      "Vous": "broyiez",
      "Ils/Elle": "broyaient"
    },
    "Passé Composé": {
      "Je": "ai broyé",
      "Tu": "as broyé",
      "Il/Elle/On": "a broyé",
      "Nous": "avons broyé",
      "Vous": "avez broyé",
      "Ils/Elle": "ont broyé"
    },
    "Futur": {
      "Je": "broyerai",
      "Tu": "broyeras",
      "Il/Elle/On": "broyera",
      "Nous": "broyerons",
      "Vous": "broyerez",
      "Ils/Elle": "broyeront"
    },
    "Plus-que-parfait": {
      "Je": "avais broyé",
      "Tu": "avais broyé",
      "Il/Elle/On": "avait broyé",
      "Nous": "avions broyé",
      "Vous": "aviez broyé",
      "Ils/Elle": "avaient broyé"
    },
    "Futur Simple": {
      "Je": "broyerai",
      "Tu": "broyeras",
      "Il/Elle/On": "broyera",
      "Nous": "broyerons",
      "Vous": "broyerez",
      "Ils/Elle": "broyeront"
    },
    "Futur Antérieur": {
      "Je": "aurai broyé",
      "Tu": "auras broyé",
      "Il/Elle/On": "aura broyé",
      "Nous": "aurons broyé",
      "Vous": "aurez broyé",
      "Ils/Elle": "auront broyé"
    },
    "Conditionnel Présent": {
      "Je": "broyerais",
      "Tu": "broyerais",
      "Il/Elle/On": "broyerait",
      "Nous": "broyerions",
      "Vous": "broyeriez",
      "Ils/Elle": "broyeraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais broyé",
      "Tu": "aurais broyé",
      "Il/Elle/On": "aurait broyé",
      "Nous": "aurions broyé",
      "Vous": "auriez broyé",
      "Ils/Elle": "auraient broyé"
    },
    "Subjonctif Présent": {
      "Je": "broie",
      "Tu": "broies",
      "Il/Elle/On": "broie",
      "Nous": "broyions",
      "Vous": "broyiez",
      "Ils/Elle": "broient"
    },
    "Subjonctif Passé": {
      "Je": "aie broyé",
      "Tu": "aies broyé",
      "Il/Elle/On": "ait broyé",
      "Nous": "ayons broyé",
      "Vous": "ayez broyé",
      "Ils/Elle": "aient broyé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse broyé",
      "Tu": "eusses broyé",
      "Il/Elle/On": "eût broyé",
      "Nous": "eussions broyé",
      "Vous": "eussiez broyé",
      "Ils/Elle": "eussent broyé"
    },
    "Subjonctif Imparfait": {
      "Je": "broyasse",
      "Tu": "broyasses",
      "Il/Elle/On": "broyât",
      "Nous": "broyassions",
      "Vous": "broyassiez",
      "Ils/Elle": "broyassent"
    },
    "Impératif Présent": {
      "Tu": "broie",
      "Nous": "broyons",
      "Vous": "broyez"
    },
    "Impératif Passé": {
      "Tu": "aie broyé",
      "Nous": "ayons broyé",
      "Vous": "ayez broyé"
    },
    "Infinitif Présent": "broyer",
    "Infinitif Passé": "avoir broyé",
    "Participe Présent": "broyant",
    "Participe Passé": "broyé",
    "Gérondif Présent": "en broyant",
    "Gérondif Passé": "en ayant broyé"
  },
"envoyer": {
    "Présent": {
      "Je": "envoie",
      "Tu": "envoies",
      "Il/Elle/On": "envoie",
      "Nous": "envoyons",
      "Vous": "envoyez",
      "Ils/Elle": "envoient"
    },
    "Imparfait": {
      "Je": "envoyais",
      "Tu": "envoyais",
      "Il/Elle/On": "envoyait",
      "Nous": "envoyions",
      "Vous": "envoyiez",
      "Ils/Elle": "envoyaient"
    },
    "Passé Composé": {
      "Je": "ai envoyé",
      "Tu": "as envoyé",
      "Il/Elle/On": "a envoyé",
      "Nous": "avons envoyé",
      "Vous": "avez envoyé",
      "Ils/Elle": "ont envoyé"
    },
    "Futur": {
      "Je": "enverrai",
      "Tu": "enverras",
      "Il/Elle/On": "enverra",
      "Nous": "enverrons",
      "Vous": "enverrez",
      "Ils/Elle": "enverront"
    },
    "Plus-que-parfait": {
      "Je": "avais envoyé",
      "Tu": "avais envoyé",
      "Il/Elle/On": "avait envoyé",
      "Nous": "avions envoyé",
      "Vous": "aviez envoyé",
      "Ils/Elle": "avaient envoyé"
    },
    "Futur Simple": {
      "Je": "enverrai",
      "Tu": "enverras",
      "Il/Elle/On": "enverra",
      "Nous": "enverrons",
      "Vous": "enverrez",
      "Ils/Elle": "enverront"
    },
    "Futur Antérieur": {
      "Je": "aurai envoyé",
      "Tu": "auras envoyé",
      "Il/Elle/On": "aura envoyé",
      "Nous": "aurons envoyé",
      "Vous": "aurez envoyé",
      "Ils/Elle": "auront envoyé"
    },
    "Conditionnel Présent": {
      "Je": "enverrais",
      "Tu": "enverrais",
      "Il/Elle/On": "enverrait",
      "Nous": "enverrions",
      "Vous": "enverriez",
      "Ils/Elle": "enverraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais envoyé",
      "Tu": "aurais envoyé",
      "Il/Elle/On": "aurait envoyé",
      "Nous": "aurions envoyé",
      "Vous": "auriez envoyé",
      "Ils/Elle": "auraient envoyé"
    },
    "Subjonctif Présent": {
      "Je": "envoie",
      "Tu": "envoies",
      "Il/Elle/On": "envoie",
      "Nous": "envoyions",
      "Vous": "envoyiez",
      "Ils/Elle": "envoient"
    },
    "Subjonctif Passé": {
      "Je": "aie envoyé",
      "Tu": "aies envoyé",
      "Il/Elle/On": "ait envoyé",
      "Nous": "ayons envoyé",
      "Vous": "ayez envoyé",
      "Ils/Elle": "aient envoyé"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse envoyé",
      "Tu": "eusses envoyé",
      "Il/Elle/On": "eût envoyé",
      "Nous": "eussions envoyé",
      "Vous": "eussiez envoyé",
      "Ils/Elle": "eussent envoyé"
    },
    "Subjonctif Imparfait": {
      "Je": "envoyasse",
      "Tu": "envoyasses",
      "Il/Elle/On": "envoyât",
      "Nous": "envoyassions",
      "Vous": "envoyassiez",
      "Ils/Elle": "envoyassent"
    },
    "Impératif Présent": {
      "Tu": "envoie",
      "Nous": "envoyons",
      "Vous": "envoyez"
    },
    "Impératif Passé": {
      "Tu": "aie envoyé",
      "Nous": "ayons envoyé",
      "Vous": "ayez envoyé"
    },
    "Infinitif Présent": "envoyer",
    "Infinitif Passé": "avoir envoyé",
    "Participe Présent": "envoyant",
    "Participe Passé": "envoyé",
    "Gérondif Présent": "en envoyant",
    "Gérondif Passé": "en ayant envoyé"
  },
  "finir": {
    "Présent": {
      "Je": "finis",
      "Tu": "finis",
      "Il/Elle/On": "finit",
      "Nous": "finissons",
      "Vous": "finissez",
      "Ils/Elle": "finissent"
    },
    "Imparfait": {
      "Je": "finissais",
      "Tu": "finissais",
      "Il/Elle/On": "finissait",
      "Nous": "finissions",
      "Vous": "finissiez",
      "Ils/Elle": "finissaient"
    },
    "Passé Composé": {
      "Je": "ai fini",
      "Tu": "as fini",
      "Il/Elle/On": "a fini",
      "Nous": "avons fini",
      "Vous": "avez fini",
      "Ils/Elle": "ont fini"
    },
    "Futur": {
      "Je": "finirai",
      "Tu": "finiras",
      "Il/Elle/On": "finira",
      "Nous": "finirons",
      "Vous": "finirez",
      "Ils/Elle": "finiront"
    },
    "Plus-que-parfait": {
      "Je": "avais fini",
      "Tu": "avais fini",
      "Il/Elle/On": "avait fini",
      "Nous": "avions fini",
      "Vous": "aviez fini",
      "Ils/Elle": "avaient fini"
    },
    "Futur Simple": {
      "Je": "finirai",
      "Tu": "finiras",
      "Il/Elle/On": "finira",
      "Nous": "finirons",
      "Vous": "finirez",
      "Ils/Elle": "finiront"
    },
    "Futur Antérieur": {
      "Je": "aurai fini",
      "Tu": "auras fini",
      "Il/Elle/On": "aura fini",
      "Nous": "aurons fini",
      "Vous": "aurez fini",
      "Ils/Elle": "auront fini"
    },
    "Conditionnel Présent": {
      "Je": "finirais",
      "Tu": "finirais",
      "Il/Elle/On": "finirait",
      "Nous": "finirions",
      "Vous": "finiriez",
      "Ils/Elle": "finiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais fini",
      "Tu": "aurais fini",
      "Il/Elle/On": "aurait fini",
      "Nous": "aurions fini",
      "Vous": "auriez fini",
      "Ils/Elle": "auraient fini"
    },
    "Subjonctif Présent": {
      "Je": "finisse",
      "Tu": "finisses",
      "Il/Elle/On": "finisse",
      "Nous": "finissions",
      "Vous": "finissiez",
      "Ils/Elle": "finissent"
    },
    "Subjonctif Passé": {
      "Je": "aie fini",
      "Tu": "aies fini",
      "Il/Elle/On": "ait fini",
      "Nous": "ayons fini",
      "Vous": "ayez fini",
      "Ils/Elle": "aient fini"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse fini",
      "Tu": "eusses fini",
      "Il/Elle/On": "eût fini",
      "Nous": "eussions fini",
      "Vous": "eussiez fini",
      "Ils/Elle": "eussent fini"
    },
    "Subjonctif Imparfait": {
      "Je": "finisse",
      "Tu": "finisses",
      "Il/Elle/On": "finît",
      "Nous": "finissions",
      "Vous": "finissiez",
      "Ils/Elle": "finissent"
    },
    "Impératif Présent": {
      "Tu": "finis",
      "Nous": "finissons",
      "Vous": "finissez"
    },
    "Impératif Passé": {
      "Tu": "aie fini",
      "Nous": "ayons fini",
      "Vous": "ayez fini"
    },
    "Infinitif Présent": "finir",
    "Infinitif Passé": "avoir fini",
    "Participe Présent": "finissant",
    "Participe Passé": "fini",
    "Gérondif Présent": "en finissant",
    "Gérondif Passé": "en ayant fini"
  },
  "hair": {
    "Présent": {
      "Je": "hais",
      "Tu": "hais",
      "Il/Elle/On": "hait",
      "Nous": "haïssons",
      "Vous": "haïssez",
      "Ils/Elle": "haïssent"
    },
    "Imparfait": {
      "Je": "haïssais",
      "Tu": "haïssais",
      "Il/Elle/On": "haïssait",
      "Nous": "haïssions",
      "Vous": "haïssiez",
      "Ils/Elle": "haïssaient"
    },
    "Passé Composé": {
      "Je": "ai haï",
      "Tu": "as haï",
      "Il/Elle/On": "a haï",
      "Nous": "avons haï",
      "Vous": "avez haï",
      "Ils/Elle": "ont haï"
    },
    "Futur": {
      "Je": "hairai",
      "Tu": "hairas",
      "Il/Elle/On": "haira",
      "Nous": "hairons",
      "Vous": "haïrez",
      "Ils/Elle": "hairont"
    },
    "Plus-que-parfait": {
      "Je": "avais haï",
      "Tu": "avais haï",
      "Il/Elle/On": "avait haï",
      "Nous": "avions haï",
      "Vous": "aviez haï",
      "Ils/Elle": "avaient haï"
    },
    "Futur Simple": {
      "Je": "hairai",
      "Tu": "hairas",
      "Il/Elle/On": "haira",
      "Nous": "hairons",
      "Vous": "haïrez",
      "Ils/Elle": "hairont"
    },
    "Futur Antérieur": {
      "Je": "aurai haï",
      "Tu": "auras haï",
      "Il/Elle/On": "aura haï",
      "Nous": "aurons haï",
      "Vous": "aurez haï",
      "Ils/Elle": "auront haï"
    },
    "Conditionnel Présent": {
      "Je": "hairais",
      "Tu": "hairais",
      "Il/Elle/On": "hairait",
      "Nous": "hairions",
      "Vous": "hairiez",
      "Ils/Elle": "hairaient"
    },
    "Conditionnel Passé": {
      "Je": "aurais haï",
      "Tu": "aurais haï",
      "Il/Elle/On": "aurait haï",
      "Nous": "aurions haï",
      "Vous": "auriez haï",
      "Ils/Elle": "auraient haï"
    },
    "Subjonctif Présent": {
      "Je": "haïsse",
      "Tu": "haïsses",
      "Il/Elle/On": "haïsse",
      "Nous": "haïssions",
      "Vous": "haïssiez",
      "Ils/Elle": "haïssent"
    },
    "Subjonctif Passé": {
      "Je": "aie haï",
      "Tu": "aies haï",
      "Il/Elle/On": "ait haï",
      "Nous": "ayons haï",
      "Vous": "ayez haï",
      "Ils/Elle": "aient haï"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse haï",
      "Tu": "eusses haï",
      "Il/Elle/On": "eût haï",
      "Nous": "eussions haï",
      "Vous": "eussiez haï",
      "Ils/Elle": "eussent haï"
    },
    "Subjonctif Imparfait": {
      "Je": "haïsse",
      "Tu": "haïsses",
      "Il/Elle/On": "hât",
      "Nous": "haïssions",
      "Vous": "haïssiez",
      "Ils/Elle": "haïssent"
    },
    "Impératif Présent": {
      "Tu": "hais",
      "Nous": "haïssons",
      "Vous": "haïssez"
    },
    "Impératif Passé": {
      "Tu": "aie haï",
      "Nous": "ayons haï",
      "Vous": "ayez haï"
    },
    "Infinitif Présent": "hair",
    "Infinitif Passé": "avoir haï",
    "Participe Présent": "haïssant",
    "Participe Passé": "haï",
    "Gérondif Présent": "en haïssant",
    "Gérondif Passé": "en ayant haï"
  },
"tenir": {
    "Présent": {
      "Je": "tiens",
      "Tu": "tiens",
      "Il/Elle/On": "tient",
      "Nous": "tenons",
      "Vous": "tenez",
      "Ils/Elle": "tiennent"
    },
    "Imparfait": {
      "Je": "tenais",
      "Tu": "tenais",
      "Il/Elle/On": "tenait",
      "Nous": "tenions",
      "Vous": "teniez",
      "Ils/Elle": "tenaient"
    },
    "Passé Composé": {
      "Je": "ai tenu",
      "Tu": "as tenu",
      "Il/Elle/On": "a tenu",
      "Nous": "avons tenu",
      "Vous": "avez tenu",
      "Ils/Elle": "ont tenu"
    },
    "Futur": {
      "Je": "tiendrai",
      "Tu": "tiendras",
      "Il/Elle/On": "tiendra",
      "Nous": "tiendrons",
      "Vous": "tiendrez",
      "Ils/Elle": "tiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais tenu",
      "Tu": "avais tenu",
      "Il/Elle/On": "avait tenu",
      "Nous": "avions tenu",
      "Vous": "aviez tenu",
      "Ils/Elle": "avaient tenu"
    },
    "Futur Simple": {
      "Je": "tiendrai",
      "Tu": "tiendras",
      "Il/Elle/On": "tiendra",
      "Nous": "tiendrons",
      "Vous": "tiendrez",
      "Ils/Elle": "tiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai tenu",
      "Tu": "auras tenu",
      "Il/Elle/On": "aura tenu",
      "Nous": "aurons tenu",
      "Vous": "aurez tenu",
      "Ils/Elle": "auront tenu"
    },
    "Conditionnel Présent": {
      "Je": "tiendrais",
      "Tu": "tiendrais",
      "Il/Elle/On": "tiendrait",
      "Nous": "tiendrions",
      "Vous": "tiendriez",
      "Ils/Elle": "tiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais tenu",
      "Tu": "aurais tenu",
      "Il/Elle/On": "aurait tenu",
      "Nous": "aurions tenu",
      "Vous": "auriez tenu",
      "Ils/Elle": "auraient tenu"
    },
    "Subjonctif Présent": {
      "Je": "tienne",
      "Tu": "tiennes",
      "Il/Elle/On": "tienne",
      "Nous": "tenions",
      "Vous": "teniez",
      "Ils/Elle": "tiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie tenu",
      "Tu": "aies tenu",
      "Il/Elle/On": "ait tenu",
      "Nous": "ayons tenu",
      "Vous": "ayez tenu",
      "Ils/Elle": "aient tenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse tenu",
      "Tu": "eusses tenu",
      "Il/Elle/On": "eût tenu",
      "Nous": "eussions tenu",
      "Vous": "eussiez tenu",
      "Ils/Elle": "eussent tenu"
    },
    "Subjonctif Imparfait": {
      "Je": "tienne",
      "Tu": "tiennes",
      "Il/Elle/On": "tînt",
      "Nous": "tenions",
      "Vous": "teniez",
      "Ils/Elle": "tiennent"
    },
    "Impératif Présent": {
      "Tu": "tiens",
      "Nous": "tenons",
      "Vous": "tenez"
    },
    "Impératif Passé": {
      "Tu": "aie tenu",
      "Nous": "ayons tenu",
      "Vous": "ayez tenu"
    },
    "Infinitif Présent": "tenir",
    "Infinitif Passé": "avoir tenu",
    "Participe Présent": "tenant",
    "Participe Passé": "tenu",
    "Gérondif Présent": "en tenant",
    "Gérondif Passé": "en ayant tenu"
  },
  "abstenir": {
    "Présent": {
      "Je": "m'abstiens",
      "Tu": "t'abstiens",
      "Il/Elle/On": "s'abstient",
      "Nous": "nous abstenons",
      "Vous": "vous abstenez",
      "Ils/Elle": "s'abstiennent"
    },
    "Imparfait": {
      "Je": "m'abstenais",
      "Tu": "t'abstenais",
      "Il/Elle/On": "s'abstenait",
      "Nous": "nous abstenions",
      "Vous": "vous absteniez",
      "Ils/Elle": "s'abstenaient"
    },
    "Passé Composé": {
      "Je": "me suis abstenu",
      "Tu": "t'es abstenu",
      "Il/Elle/On": "s'est abstenu",
      "Nous": "nous sommes abstenus",
      "Vous": "vous êtes abstenus",
      "Ils/Elle": "se sont abstenus"
    },
    "Futur": {
      "Je": "m'abstiendrai",
      "Tu": "t'abstiendras",
      "Il/Elle/On": "s'abstiendra",
      "Nous": "nous abstiendrons",
      "Vous": "vous abstiendrez",
      "Ils/Elle": "s'abstiendront"
    },
    "Plus-que-parfait": {
      "Je": "m'étais abstenu",
      "Tu": "t'étais abstenu",
      "Il/Elle/On": "s'était abstenu",
      "Nous": "nous étions abstenus",
      "Vous": "vous étiez abstenus",
      "Ils/Elle": "s'étaient abstenus"
    },
    "Futur Simple": {
      "Je": "m'abstiendrai",
      "Tu": "t'abstiendras",
      "Il/Elle/On": "s'abstiendra",
      "Nous": "nous abstiendrons",
      "Vous": "vous abstiendrez",
      "Ils/Elle": "s'abstiendront"
    },
    "Futur Antérieur": {
      "Je": "me serai abstenu",
      "Tu": "te seras abstenu",
      "Il/Elle/On": "se sera abstenu",
      "Nous": "nous serons abstenus",
      "Vous": "vous serez abstenus",
      "Ils/Elle": "se seront abstenus"
    },
    "Conditionnel Présent": {
      "Je": "m'abstiendrais",
      "Tu": "t'abstiendrais",
      "Il/Elle/On": "s'abstiendrait",
      "Nous": "nous abstiendrions",
      "Vous": "vous abstiendriez",
      "Ils/Elle": "s'abstiendraient"
    },
    "Conditionnel Passé": {
      "Je": "me serais abstenu",
      "Tu": "te serais abstenu",
      "Il/Elle/On": "se serait abstenu",
      "Nous": "nous serions abstenus",
      "Vous": "vous seriez abstenus",
      "Ils/Elle": "se seraient abstenus"
    },
    "Subjonctif Présent": {
      "Je": "m'abstienne",
      "Tu": "t'abstiennes",
      "Il/Elle/On": "s'abstienne",
      "Nous": "nous abstenions",
      "Vous": "vous absteniez",
      "Ils/Elle": "s'abstiennent"
    },
    "Subjonctif Passé": {
      "Je": "me sois abstenu",
      "Tu": "te sois abstenu",
      "Il/Elle/On": "se soit abstenu",
      "Nous": "nous soyons abstenus",
      "Vous": "vous soyez abstenus",
      "Ils/Elle": "se soient abstenus"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "me fusse abstenu",
      "Tu": "te fusses abstenu",
      "Il/Elle/On": "se fût abstenu",
      "Nous": "nous fussions abstenus",
      "Vous": "vous fussiez abstenus",
      "Ils/Elle": "se fussent abstenus"
    },
    "Subjonctif Imparfait": {
      "Je": "m'abstinsse",
      "Tu": "t'abstinsse",
      "Il/Elle/On": "s'abstînt",
      "Nous": "nous abstenions",
      "Vous": "vous absteniez",
      "Ils/Elle": "s'abstiennent"
    },
    "Impératif Présent": {
      "Tu": "abstiens-toi",
      "Nous": "abstenons-nous",
      "Vous": "abstenez-vous"
    },
    "Impératif Passé": {
      "Tu": "aie été abstenu",
      "Nous": "ayons été abstenus",
      "Vous": "ayez été abstenus"
    },
    "Infinitif Présent": "s'abstenir",
    "Infinitif Passé": "s'être abstenu",
    "Participe Présent": "s'abstenant",
    "Participe Passé": "abstenu",
    "Gérondif Présent": "en s'abstenant",
    "Gérondif Passé": "en s'étant abstenu"
  },
  "appartenir": {
    "Présent": {
      "Je": "appartiens",
      "Tu": "appartiens",
      "Il/Elle/On": "appartient",
      "Nous": "appartenons",
      "Vous": "appartenez",
      "Ils/Elle": "appartiennent"
    },
    "Imparfait": {
      "Je": "appartenais",
      "Tu": "appartenais",
      "Il/Elle/On": "appartenait",
      "Nous": "appartenions",
      "Vous": "apparteniez",
      "Ils/Elle": "appartenaient"
    },
    "Passé Composé": {
      "Je": "ai appartenu",
      "Tu": "as appartenu",
      "Il/Elle/On": "a appartenu",
      "Nous": "avons appartenu",
      "Vous": "avez appartenu",
      "Ils/Elle": "ont appartenu"
    },
    "Futur": {
      "Je": "appartiendrai",
      "Tu": "appartiendras",
      "Il/Elle/On": "appartiendra",
      "Nous": "appartiendrons",
      "Vous": "appartiendrez",
      "Ils/Elle": "appartiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais appartenu",
      "Tu": "avais appartenu",
      "Il/Elle/On": "avait appartenu",
      "Nous": "avions appartenu",
      "Vous": "aviez appartenu",
      "Ils/Elle": "avaient appartenu"
    },
    "Futur Simple": {
      "Je": "appartiendrai",
      "Tu": "appartiendras",
      "Il/Elle/On": "appartiendra",
      "Nous": "appartiendrons",
      "Vous": "appartiendrez",
      "Ils/Elle": "appartiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai appartenu",
      "Tu": "auras appartenu",
      "Il/Elle/On": "aura appartenu",
      "Nous": "aurons appartenu",
      "Vous": "aurez appartenu",
      "Ils/Elle": "auront appartenu"
    },
    "Conditionnel Présent": {
      "Je": "appartiendrais",
      "Tu": "appartiendrais",
      "Il/Elle/On": "appartiendrait",
      "Nous": "appartiendrions",
      "Vous": "appartiendriez",
      "Ils/Elle": "appartiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais appartenu",
      "Tu": "aurais appartenu",
      "Il/Elle/On": "aurait appartenu",
      "Nous": "aurions appartenu",
      "Vous": "auriez appartenu",
      "Ils/Elle": "auraient appartenu"
    },
    "Subjonctif Présent": {
      "Je": "appartienne",
      "Tu": "appartiennes",
      "Il/Elle/On": "appartienne",
      "Nous": "appartenions",
      "Vous": "apparteniez",
      "Ils/Elle": "appartiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie appartenu",
      "Tu": "aies appartenu",
      "Il/Elle/On": "ait appartenu",
      "Nous": "ayons appartenu",
      "Vous": "ayez appartenu",
      "Ils/Elle": "aient appartenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse appartenu",
      "Tu": "eusses appartenu",
      "Il/Elle/On": "eût appartenu",
      "Nous": "eussions appartenu",
      "Vous": "eussiez appartenu",
      "Ils/Elle": "eussent appartenu"
    },
    "Subjonctif Imparfait": {
      "Je": "appartinsse",
      "Tu": "appartinsses",
      "Il/Elle/On": "appartînt",
      "Nous": "appartinssions",
      "Vous": "appartinssiez",
      "Ils/Elle": "appartinssent"
    },
    "Impératif Présent": {
      "Tu": "appartiens",
      "Nous": "appartenons",
      "Vous": "appartenez"
    },
    "Impératif Passé": {
      "Tu": "aie appartenu",
      "Nous": "ayons appartenu",
      "Vous": "ayez appartenu"
    },
    "Infinitif Présent": "appartenir",
    "Infinitif Passé": "avoir appartenu",
    "Participe Présent": "appartenant",
    "Participe Passé": "appartenu",
    "Gérondif Présent": "en appartenant",
    "Gérondif Passé": "en ayant appartenu"
},
"contenir": {
    "Présent": {
      "Je": "contiens",
      "Tu": "contiens",
      "Il/Elle/On": "contient",
      "Nous": "contenons",
      "Vous": "contenez",
      "Ils/Elle": "contiennent"
    },
    "Imparfait": {
      "Je": "contenais",
      "Tu": "contenais",
      "Il/Elle/On": "contenait",
      "Nous": "contenions",
      "Vous": "conteniez",
      "Ils/Elle": "contenaient"
    },
    "Passé Composé": {
      "Je": "ai contenu",
      "Tu": "as contenu",
      "Il/Elle/On": "a contenu",
      "Nous": "avons contenu",
      "Vous": "avez contenu",
      "Ils/Elle": "ont contenu"
    },
    "Futur": {
      "Je": "contiendrai",
      "Tu": "contiendras",
      "Il/Elle/On": "contiendra",
      "Nous": "contiendrons",
      "Vous": "contiendrez",
      "Ils/Elle": "contiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais contenu",
      "Tu": "avais contenu",
      "Il/Elle/On": "avait contenu",
      "Nous": "avions contenu",
      "Vous": "aviez contenu",
      "Ils/Elle": "avaient contenu"
    },
    "Futur Simple": {
      "Je": "contiendrai",
      "Tu": "contiendras",
      "Il/Elle/On": "contiendra",
      "Nous": "contiendrons",
      "Vous": "contiendrez",
      "Ils/Elle": "contiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai contenu",
      "Tu": "auras contenu",
      "Il/Elle/On": "aura contenu",
      "Nous": "aurons contenu",
      "Vous": "aurez contenu",
      "Ils/Elle": "auront contenu"
    },
    "Conditionnel Présent": {
      "Je": "contiendrais",
      "Tu": "contiendrais",
      "Il/Elle/On": "contiendrait",
      "Nous": "contiendrions",
      "Vous": "contiendriez",
      "Ils/Elle": "contiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais contenu",
      "Tu": "aurais contenu",
      "Il/Elle/On": "aurait contenu",
      "Nous": "aurions contenu",
      "Vous": "auriez contenu",
      "Ils/Elle": "auraient contenu"
    },
    "Subjonctif Présent": {
      "Je": "contienne",
      "Tu": "contiennes",
      "Il/Elle/On": "contienne",
      "Nous": "contenions",
      "Vous": "conteniez",
      "Ils/Elle": "contiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie contenu",
      "Tu": "aies contenu",
      "Il/Elle/On": "ait contenu",
      "Nous": "ayons contenu",
      "Vous": "ayez contenu",
      "Ils/Elle": "aient contenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse contenu",
      "Tu": "eusses contenu",
      "Il/Elle/On": "eût contenu",
      "Nous": "eussions contenu",
      "Vous": "eussiez contenu",
      "Ils/Elle": "eussent contenu"
    },
    "Subjonctif Imparfait": {
      "Je": "continsse",
      "Tu": "continsses",
      "Il/Elle/On": "contînt",
      "Nous": "continssions",
      "Vous": "continssiez",
      "Ils/Elle": "continssent"
    },
    "Impératif Présent": {
      "Tu": "contiens",
      "Nous": "contenons",
      "Vous": "contenez"
    },
    "Impératif Passé": {
      "Tu": "aie contenu",
      "Nous": "ayons contenu",
      "Vous": "ayez contenu"
    },
    "Infinitif Présent": "contenir",
    "Infinitif Passé": "avoir contenu",
    "Participe Présent": "contenant",
    "Participe Passé": "contenu",
    "Gérondif Présent": "en contenant",
    "Gérondif Passé": "en ayant contenu"
},
"détenir": {
    "Présent": {
      "Je": "détiens",
      "Tu": "détiens",
      "Il/Elle/On": "détient",
      "Nous": "détenons",
      "Vous": "détenez",
      "Ils/Elle": "détiennent"
    },
    "Imparfait": {
      "Je": "détenais",
      "Tu": "détenais",
      "Il/Elle/On": "détenait",
      "Nous": "détentions",
      "Vous": "déteniez",
      "Ils/Elle": "détenaient"
    },
    "Passé Composé": {
      "Je": "ai détenu",
      "Tu": "as détenu",
      "Il/Elle/On": "a détenu",
      "Nous": "avons détenu",
      "Vous": "avez détenu",
      "Ils/Elle": "ont détenu"
    },
    "Futur": {
      "Je": "détiendrai",
      "Tu": "détiendras",
      "Il/Elle/On": "détiendra",
      "Nous": "détiendrons",
      "Vous": "détiendrez",
      "Ils/Elle": "détiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais détenu",
      "Tu": "avais détenu",
      "Il/Elle/On": "avait détenu",
      "Nous": "avions détenu",
      "Vous": "aviez détenu",
      "Ils/Elle": "avaient détenu"
    },
    "Futur Simple": {
      "Je": "détiendrai",
      "Tu": "détiendras",
      "Il/Elle/On": "détiendra",
      "Nous": "détiendrons",
      "Vous": "détiendrez",
      "Ils/Elle": "détiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai détenu",
      "Tu": "auras détenu",
      "Il/Elle/On": "aura détenu",
      "Nous": "aurons détenu",
      "Vous": "aurez détenu",
      "Ils/Elle": "auront détenu"
    },
    "Conditionnel Présent": {
      "Je": "détiendrais",
      "Tu": "détiendrais",
      "Il/Elle/On": "détiendrait",
      "Nous": "détiendrions",
      "Vous": "détiendriez",
      "Ils/Elle": "détiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais détenu",
      "Tu": "aurais détenu",
      "Il/Elle/On": "aurait détenu",
      "Nous": "aurions détenu",
      "Vous": "auriez détenu",
      "Ils/Elle": "auraient détenu"
    },
    "Subjonctif Présent": {
      "Je": "détienne",
      "Tu": "détiennes",
      "Il/Elle/On": "détienne",
      "Nous": "détentions",
      "Vous": "déteniez",
      "Ils/Elle": "détiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie détenu",
      "Tu": "aies détenu",
      "Il/Elle/On": "ait détenu",
      "Nous": "ayons détenu",
      "Vous": "ayez détenu",
      "Ils/Elle": "aient détenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse détenu",
      "Tu": "eusses détenu",
      "Il/Elle/On": "eût détenu",
      "Nous": "eussions détenu",
      "Vous": "eussiez détenu",
      "Ils/Elle": "eussent détenu"
    },
    "Subjonctif Imparfait": {
      "Je": "détenisse",
      "Tu": "détenisses",
      "Il/Elle/On": "détenît",
      "Nous": "détenissions",
      "Vous": "détenissiez",
      "Ils/Elle": "détenissent"
    },
    "Impératif Présent": {
      "Tu": "détiens",
      "Nous": "détenons",
      "Vous": "déteniez"
    },
    "Impératif Passé": {
      "Tu": "aie détenu",
      "Nous": "ayons détenu",
      "Vous": "ayez détenu"
    },
    "Infinitif Présent": "détenir",
    "Infinitif Passé": "avoir détenu",
    "Participe Présent": "détenant",
    "Participe Passé": "détenu",
    "Gérondif Présent": "en détenant",
    "Gérondif Passé": "en ayant détenu"
},
"entretenir": {
    "Présent": {
      "Je": "entretiens",
      "Tu": "entretiens",
      "Il/Elle/On": "entretient",
      "Nous": "entretenons",
      "Vous": "entretenez",
      "Ils/Elle": "entretiennent"
    },
    "Imparfait": {
      "Je": "entretenais",
      "Tu": "entretenais",
      "Il/Elle/On": "entretenait",
      "Nous": "entretenions",
      "Vous": "entreteniez",
      "Ils/Elle": "entretenaient"
    },
    "Passé Composé": {
      "Je": "ai entretenu",
      "Tu": "as entretenu",
      "Il/Elle/On": "a entretenu",
      "Nous": "avons entretenu",
      "Vous": "avez entretenu",
      "Ils/Elle": "ont entretenu"
    },
    "Futur": {
      "Je": "entretiendrai",
      "Tu": "entretiendras",
      "Il/Elle/On": "entretiendra",
      "Nous": "entretiendrons",
      "Vous": "entretiendrez",
      "Ils/Elle": "entretiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais entretenu",
      "Tu": "avais entretenu",
      "Il/Elle/On": "avait entretenu",
      "Nous": "avions entretenu",
      "Vous": "aviez entretenu",
      "Ils/Elle": "avaient entretenu"
    },
    "Futur Simple": {
      "Je": "entretiendrai",
      "Tu": "entretiendras",
      "Il/Elle/On": "entretiendra",
      "Nous": "entretiendrons",
      "Vous": "entretiendrez",
      "Ils/Elle": "entretiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai entretenu",
      "Tu": "auras entretenu",
      "Il/Elle/On": "aura entretenu",
      "Nous": "aurons entretenu",
      "Vous": "aurez entretenu",
      "Ils/Elle": "auront entretenu"
    },
    "Conditionnel Présent": {
      "Je": "entretiendrais",
      "Tu": "entretiendrais",
      "Il/Elle/On": "entretiendrait",
      "Nous": "entretiendrions",
      "Vous": "entretiendriez",
      "Ils/Elle": "entretiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais entretenu",
      "Tu": "aurais entretenu",
      "Il/Elle/On": "aurait entretenu",
      "Nous": "aurions entretenu",
      "Vous": "auriez entretenu",
      "Ils/Elle": "auraient entretenu"
    },
    "Subjonctif Présent": {
      "Je": "entretienne",
      "Tu": "entretiennes",
      "Il/Elle/On": "entretienne",
      "Nous": "entretenions",
      "Vous": "entreteniez",
      "Ils/Elle": "entretiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie entretenu",
      "Tu": "aies entretenu",
      "Il/Elle/On": "ait entretenu",
      "Nous": "ayons entretenu",
      "Vous": "ayez entretenu",
      "Ils/Elle": "aient entretenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse entretenu",
      "Tu": "eusses entretenu",
      "Il/Elle/On": "eût entretenu",
      "Nous": "eussions entretenu",
      "Vous": "eussiez entretenu",
      "Ils/Elle": "eussent entretenu"
    },
    "Subjonctif Imparfait": {
      "Je": "entretinsse",
      "Tu": "entretinsses",
      "Il/Elle/On": "entretînt",
      "Nous": "entretinssions",
      "Vous": "entretinssiez",
      "Ils/Elle": "entretinssent"
    },
    "Impératif Présent": {
      "Tu": "entretiens",
      "Nous": "entretenons",
      "Vous": "entretenez"
    },
    "Impératif Passé": {
      "Tu": "aie entretenu",
      "Nous": "ayons entretenu",
      "Vous": "ayez entretenu"
    },
    "Infinitif Présent": "entretenir",
    "Infinitif Passé": "avoir entretenu",
    "Participe Présent": "entretenant",
    "Participe Passé": "entretenu",
    "Gérondif Présent": "en entretenant",
    "Gérondif Passé": "en ayant entretenu"
},
"maintenir": {
    "Présent": {
      "Je": "maintiens",
      "Tu": "maintiens",
      "Il/Elle/On": "maintient",
      "Nous": "maintenons",
      "Vous": "maintenez",
      "Ils/Elle": "maintiennent"
    },
    "Imparfait": {
      "Je": "maintenais",
      "Tu": "maintenais",
      "Il/Elle/On": "maintenait",
      "Nous": "maintenions",
      "Vous": "mainteniez",
      "Ils/Elle": "maintenaient"
    },
    "Passé Composé": {
      "Je": "ai maintenu",
      "Tu": "as maintenu",
      "Il/Elle/On": "a maintenu",
      "Nous": "avons maintenu",
      "Vous": "avez maintenu",
      "Ils/Elle": "ont maintenu"
    },
    "Futur": {
      "Je": "maintiendrai",
      "Tu": "maintiendras",
      "Il/Elle/On": "maintiendra",
      "Nous": "maintiendrons",
      "Vous": "maintiendrez",
      "Ils/Elle": "maintiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais maintenu",
      "Tu": "avais maintenu",
      "Il/Elle/On": "avait maintenu",
      "Nous": "avions maintenu",
      "Vous": "aviez maintenu",
      "Ils/Elle": "avaient maintenu"
    },
    "Futur Simple": {
      "Je": "maintiendrai",
      "Tu": "maintiendras",
      "Il/Elle/On": "maintiendra",
      "Nous": "maintiendrons",
      "Vous": "maintiendrez",
      "Ils/Elle": "maintiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai maintenu",
      "Tu": "auras maintenu",
      "Il/Elle/On": "aura maintenu",
      "Nous": "aurons maintenu",
      "Vous": "aurez maintenu",
      "Ils/Elle": "auront maintenu"
    },
    "Conditionnel Présent": {
      "Je": "maintiendrais",
      "Tu": "maintiendrais",
      "Il/Elle/On": "maintiendrait",
      "Nous": "maintiendrions",
      "Vous": "maintiendriez",
      "Ils/Elle": "maintiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais maintenu",
      "Tu": "aurais maintenu",
      "Il/Elle/On": "aurait maintenu",
      "Nous": "aurions maintenu",
      "Vous": "auriez maintenu",
      "Ils/Elle": "auraient maintenu"
    },
    "Subjonctif Présent": {
      "Je": "maintienne",
      "Tu": "maintiennes",
      "Il/Elle/On": "maintienne",
      "Nous": "maintenions",
      "Vous": "mainteniez",
      "Ils/Elle": "maintiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie maintenu",
      "Tu": "aies maintenu",
      "Il/Elle/On": "ait maintenu",
      "Nous": "ayons maintenu",
      "Vous": "ayez maintenu",
      "Ils/Elle": "aient maintenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse maintenu",
      "Tu": "eusses maintenu",
      "Il/Elle/On": "eût maintenu",
      "Nous": "eussions maintenu",
      "Vous": "eussiez maintenu",
      "Ils/Elle": "eussent maintenu"
    },
    "Subjonctif Imparfait": {
      "Je": "maintinsse",
      "Tu": "maintinsses",
      "Il/Elle/On": "maintînt",
      "Nous": "maintinssions",
      "Vous": "maintinssiez",
      "Ils/Elle": "maintinssent"
    },
    "Impératif Présent": {
      "Tu": "maintiens",
      "Nous": "maintenons",
      "Vous": "maintenez"
    },
    "Impératif Passé": {
      "Tu": "aie maintenu",
      "Nous": "ayons maintenu",
      "Vous": "ayez maintenu"
    },
    "Infinitif Présent": "maintenir",
    "Infinitif Passé": "avoir maintenu",
    "Participe Présent": "maintenant",
    "Participe Passé": "maintenu",
    "Gérondif Présent": "en maintenant",
    "Gérondif Passé": "en ayant maintenu"
},
"obtenir": {
    "Présent": {
      "Je": "obtiens",
      "Tu": "obtiens",
      "Il/Elle/On": "obtient",
      "Nous": "obtenons",
      "Vous": "obtenez",
      "Ils/Elle": "obtiennent"
    },
    "Imparfait": {
      "Je": "obtenais",
      "Tu": "obtenais",
      "Il/Elle/On": "obtenait",
      "Nous": "obtenions",
      "Vous": "obteniez",
      "Ils/Elle": "obtenaient"
    },
    "Passé Composé": {
      "Je": "ai obtenu",
      "Tu": "as obtenu",
      "Il/Elle/On": "a obtenu",
      "Nous": "avons obtenu",
      "Vous": "avez obtenu",
      "Ils/Elle": "ont obtenu"
    },
    "Futur": {
      "Je": "obtiendrai",
      "Tu": "obtiendras",
      "Il/Elle/On": "obtiendra",
      "Nous": "obtiendrons",
      "Vous": "obtiendrez",
      "Ils/Elle": "obtiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais obtenu",
      "Tu": "avais obtenu",
      "Il/Elle/On": "avait obtenu",
      "Nous": "avions obtenu",
      "Vous": "aviez obtenu",
      "Ils/Elle": "avaient obtenu"
    },
    "Futur Simple": {
      "Je": "obtiendrai",
      "Tu": "obtiendras",
      "Il/Elle/On": "obtiendra",
      "Nous": "obtiendrons",
      "Vous": "obtiendrez",
      "Ils/Elle": "obtiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai obtenu",
      "Tu": "auras obtenu",
      "Il/Elle/On": "aura obtenu",
      "Nous": "aurons obtenu",
      "Vous": "aurez obtenu",
      "Ils/Elle": "auront obtenu"
    },
    "Conditionnel Présent": {
      "Je": "obtiendrais",
      "Tu": "obtiendrais",
      "Il/Elle/On": "obtiendrait",
      "Nous": "obtiendrions",
      "Vous": "obtiendriez",
      "Ils/Elle": "obtiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais obtenu",
      "Tu": "aurais obtenu",
      "Il/Elle/On": "aurait obtenu",
      "Nous": "aurions obtenu",
      "Vous": "auriez obtenu",
      "Ils/Elle": "auraient obtenu"
    },
    "Subjonctif Présent": {
      "Je": "obtienne",
      "Tu": "obtiennes",
      "Il/Elle/On": "obtienne",
      "Nous": "obtenions",
      "Vous": "obteniez",
      "Ils/Elle": "obtiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie obtenu",
      "Tu": "aies obtenu",
      "Il/Elle/On": "ait obtenu",
      "Nous": "ayons obtenu",
      "Vous": "ayez obtenu",
      "Ils/Elle": "aient obtenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse obtenu",
      "Tu": "eusses obtenu",
      "Il/Elle/On": "eût obtenu",
      "Nous": "eussions obtenu",
      "Vous": "eussiez obtenu",
      "Ils/Elle": "eussent obtenu"
    },
    "Subjonctif Imparfait": {
      "Je": "obtinsse",
      "Tu": "obtinsses",
      "Il/Elle/On": "obtînt",
      "Nous": "obtinssions",
      "Vous": "obtinssiez",
      "Ils/Elle": "obtinssent"
    },
    "Impératif Présent": {
      "Tu": "obtiens",
      "Nous": "obtenons",
      "Vous": "obtenez"
    },
    "Impératif Passé": {
      "Tu": "aie obtenu",
      "Nous": "ayons obtenu",
      "Vous": "ayez obtenu"
    },
    "Infinitif Présent": "obtenir",
    "Infinitif Passé": "avoir obtenu",
    "Participe Présent": "obtenant",
    "Participe Passé": "obtenu",
    "Gérondif Présent": "en obtenant",
    "Gérondif Passé": "en ayant obtenu"
},
"retenir": {
    "Présent": {
      "Je": "retiens",
      "Tu": "retiens",
      "Il/Elle/On": "retient",
      "Nous": "retenons",
      "Vous": "retenez",
      "Ils/Elle": "retiennent"
    },
    "Imparfait": {
      "Je": "retenais",
      "Tu": "retenais",
      "Il/Elle/On": "retenait",
      "Nous": "retenions",
      "Vous": "reteniez",
      "Ils/Elle": "retenaient"
    },
    "Passé Composé": {
      "Je": "ai retenu",
      "Tu": "as retenu",
      "Il/Elle/On": "a retenu",
      "Nous": "avons retenu",
      "Vous": "avez retenu",
      "Ils/Elle": "ont retenu"
    },
    "Futur": {
      "Je": "retiendrai",
      "Tu": "retiendras",
      "Il/Elle/On": "retiendra",
      "Nous": "retiendrons",
      "Vous": "retiendrez",
      "Ils/Elle": "retiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais retenu",
      "Tu": "avais retenu",
      "Il/Elle/On": "avait retenu",
      "Nous": "avions retenu",
      "Vous": "aviez retenu",
      "Ils/Elle": "avaient retenu"
    },
    "Futur Simple": {
      "Je": "retiendrai",
      "Tu": "retiendras",
      "Il/Elle/On": "retiendra",
      "Nous": "retiendrons",
      "Vous": "retiendrez",
      "Ils/Elle": "retiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai retenu",
      "Tu": "auras retenu",
      "Il/Elle/On": "aura retenu",
      "Nous": "aurons retenu",
      "Vous": "aurez retenu",
      "Ils/Elle": "auront retenu"
    },
    "Conditionnel Présent": {
      "Je": "retiendrais",
      "Tu": "retiendrais",
      "Il/Elle/On": "retiendrait",
      "Nous": "retiendrions",
      "Vous": "retiendriez",
      "Ils/Elle": "retiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais retenu",
      "Tu": "aurais retenu",
      "Il/Elle/On": "aurait retenu",
      "Nous": "aurions retenu",
      "Vous": "auriez retenu",
      "Ils/Elle": "auraient retenu"
    },
    "Subjonctif Présent": {
      "Je": "retienne",
      "Tu": "retiennes",
      "Il/Elle/On": "retienne",
      "Nous": "retenions",
      "Vous": "reteniez",
      "Ils/Elle": "retiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie retenu",
      "Tu": "aies retenu",
      "Il/Elle/On": "ait retenu",
      "Nous": "ayons retenu",
      "Vous": "ayez retenu",
      "Ils/Elle": "aient retenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse retenu",
      "Tu": "eusses retenu",
      "Il/Elle/On": "eût retenu",
      "Nous": "eussions retenu",
      "Vous": "eussiez retenu",
      "Ils/Elle": "eussent retenu"
    },
    "Subjonctif Imparfait": {
      "Je": "retinsse",
      "Tu": "retinsses",
      "Il/Elle/On": "retînt",
      "Nous": "retinssions",
      "Vous": "retinssiez",
      "Ils/Elle": "retinssent"
    },
    "Impératif Présent": {
      "Tu": "retiens",
      "Nous": "retenons",
      "Vous": "retenez"
    },
    "Impératif Passé": {
      "Tu": "aie retenu",
      "Nous": "ayons retenu",
      "Vous": "ayez retenu"
    },
    "Infinitif Présent": "retenir",
    "Infinitif Passé": "avoir retenu",
    "Participe Présent": "retenant",
    "Participe Passé": "retenu",
    "Gérondif Présent": "en retenant",
    "Gérondif Passé": "en ayant retenu"
},
"soutenir": {
    "Présent": {
      "Je": "soutiens",
      "Tu": "soutiens",
      "Il/Elle/On": "soutient",
      "Nous": "soutenons",
      "Vous": "soutenez",
      "Ils/Elle": "soutiennent"
    },
    "Imparfait": {
      "Je": "soutenais",
      "Tu": "soutenais",
      "Il/Elle/On": "soutenait",
      "Nous": "soutenions",
      "Vous": "souteniez",
      "Ils/Elle": "soutenaient"
    },
    "Passé Composé": {
      "Je": "ai soutenu",
      "Tu": "as soutenu",
      "Il/Elle/On": "a soutenu",
      "Nous": "avons soutenu",
      "Vous": "avez soutenu",
      "Ils/Elle": "ont soutenu"
    },
    "Futur": {
      "Je": "soutiendrai",
      "Tu": "soutiendras",
      "Il/Elle/On": "soutiendra",
      "Nous": "soutiendrons",
      "Vous": "soutiendrez",
      "Ils/Elle": "soutiendront"
    },
    "Plus-que-parfait": {
      "Je": "avais soutenu",
      "Tu": "avais soutenu",
      "Il/Elle/On": "avait soutenu",
      "Nous": "avions soutenu",
      "Vous": "aviez soutenu",
      "Ils/Elle": "avaient soutenu"
    },
    "Futur Simple": {
      "Je": "soutiendrai",
      "Tu": "soutiendras",
      "Il/Elle/On": "soutiendra",
      "Nous": "soutiendrons",
      "Vous": "soutiendrez",
      "Ils/Elle": "soutiendront"
    },
    "Futur Antérieur": {
      "Je": "aurai soutenu",
      "Tu": "auras soutenu",
      "Il/Elle/On": "aura soutenu",
      "Nous": "aurons soutenu",
      "Vous": "aurez soutenu",
      "Ils/Elle": "auront soutenu"
    },
    "Conditionnel Présent": {
      "Je": "soutiendrais",
      "Tu": "soutiendrais",
      "Il/Elle/On": "soutiendrait",
      "Nous": "soutiendrions",
      "Vous": "soutiendriez",
      "Ils/Elle": "soutiendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais soutenu",
      "Tu": "aurais soutenu",
      "Il/Elle/On": "aurait soutenu",
      "Nous": "aurions soutenu",
      "Vous": "auriez soutenu",
      "Ils/Elle": "auraient soutenu"
    },
    "Subjonctif Présent": {
      "Je": "soutienne",
      "Tu": "soutiennes",
      "Il/Elle/On": "soutienne",
      "Nous": "soutenions",
      "Vous": "souteniez",
      "Ils/Elle": "soutiennent"
    },
    "Subjonctif Passé": {
      "Je": "aie soutenu",
      "Tu": "aies soutenu",
      "Il/Elle/On": "ait soutenu",
      "Nous": "ayons soutenu",
      "Vous": "ayez soutenu",
      "Ils/Elle": "aient soutenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse soutenu",
      "Tu": "eusses soutenu",
      "Il/Elle/On": "eût soutenu",
      "Nous": "eussions soutenu",
      "Vous": "eussiez soutenu",
      "Ils/Elle": "eussent soutenu"
    },
    "Subjonctif Imparfait": {
      "Je": "soutinsse",
      "Tu": "soutinsses",
      "Il/Elle/On": "soutînt",
      "Nous": "soutinssions",
      "Vous": "soutinssiez",
      "Ils/Elle": "soutinssent"
    },
    "Impératif Présent": {
      "Tu": "soutiens",
      "Nous": "soutenons",
      "Vous": "soutenez"
    },
    "Impératif Passé": {
      "Tu": "aie soutenu",
      "Nous": "ayons soutenu",
      "Vous": "ayez soutenu"
    },
    "Infinitif Présent": "soutenir",
    "Infinitif Passé": "avoir soutenu",
    "Participe Présent": "soutenant",
    "Participe Passé": "soutenu",
    "Gérondif Présent": "en soutenant",
    "Gérondif Passé": "en ayant soutenu"
},
"avenir": {
    "Présent": {
      "Je": "avenir",
      "Tu": "avenir",
      "Il/Elle/On": "avient",
      "Nous": "avenons",
      "Vous": "avenez",
      "Ils/Elle": "avenent"
    },
    "Imparfait": {
      "Je": "avenais",
      "Tu": "avenais",
      "Il/Elle/On": "avenait",
      "Nous": "avenions",
      "Vous": "aveniez",
      "Ils/Elle": "avenaient"
    },
    "Passé Composé": {
      "Je": "suis venu(e)",
      "Tu": "es venu(e)",
      "Il/Elle/On": "est venu(e)",
      "Nous": "sommes venus(es)",
      "Vous": "êtes venus(es)",
      "Ils/Elle": "sont venus(es)"
    },
    "Futur": {
      "Je": "viendrai",
      "Tu": "viendras",
      "Il/Elle/On": "viendra",
      "Nous": "viendrons",
      "Vous": "viendrez",
      "Ils/Elle": "viendront"
    },
    "Plus-que-parfait": {
      "Je": "étais venu(e)",
      "Tu": "étais venu(e)",
      "Il/Elle/On": "était venu(e)",
      "Nous": "étions venus(es)",
      "Vous": "étiez venus(es)",
      "Ils/Elle": "étaient venus(es)"
    },
    "Futur Simple": {
      "Je": "viendrai",
      "Tu": "viendras",
      "Il/Elle/On": "viendra",
      "Nous": "viendrons",
      "Vous": "viendrez",
      "Ils/Elle": "viendront"
    },
    "Futur Antérieur": {
      "Je": "serai venu(e)",
      "Tu": "seras venu(e)",
      "Il/Elle/On": "sera venu(e)",
      "Nous": "serons venus(es)",
      "Vous": "serez venus(es)",
      "Ils/Elle": "seront venus(es)"
    },
    "Conditionnel Présent": {
      "Je": "viendrais",
      "Tu": "viendrais",
      "Il/Elle/On": "viendrait",
      "Nous": "viendrions",
      "Vous": "viendriez",
      "Ils/Elle": "viendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais venu(e)",
      "Tu": "serais venu(e)",
      "Il/Elle/On": "serait venu(e)",
      "Nous": "serions venus(es)",
      "Vous": "seriez venus(es)",
      "Ils/Elle": "seraient venus(es)"
    },
    "Subjonctif Présent": {
      "Je": "vienne",
      "Tu": "viennes",
      "Il/Elle/On": "vienne",
      "Nous": "venions",
      "Vous": "veniez",
      "Ils/Elle": "viennent"
    },
    "Subjonctif Passé": {
      "Je": "sois venu(e)",
      "Tu": "sois venu(e)",
      "Il/Elle/On": "soit venu(e)",
      "Nous": "soyons venus(es)",
      "Vous": "soyez venus(es)",
      "Ils/Elle": "soient venus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse venu(e)",
      "Tu": "fusses venu(e)",
      "Il/Elle/On": "fût venu(e)",
      "Nous": "fussions venus(es)",
      "Vous": "fussiez venus(es)",
      "Ils/Elle": "fussent venus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "vinsse",
      "Tu": "vinsses",
      "Il/Elle/On": "vînt",
      "Nous": "vinssions",
      "Vous": "vinssiez",
      "Ils/Elle": "vinssent"
    },
    "Impératif Présent": {
      "Tu": "viens",
      "Nous": "venons",
      "Vous": "venez"
    },
    "Impératif Passé": {
      "Tu": "sois venu(e)",
      "Nous": "soyons venus(es)",
      "Vous": "soyez venus(es)"
    },
    "Infinitif Présent": "venir",
    "Infinitif Passé": "être venu(e)",
    "Participe Présent": "venant",
    "Participe Passé": "venu(e)",
    "Gérondif Présent": "en venant",
    "Gérondif Passé": "en étant venu(e)"
  },
"advenir": {
    "Présent": {
      "Je": "advient",
      "Tu": "advient",
      "Il/Elle/On": "advient",
      "Nous": "advenons",
      "Vous": "advenez",
      "Ils/Elle": "adviennent"
    },
    "Imparfait": {
      "Je": "advenais",
      "Tu": "advenais",
      "Il/Elle/On": "advenait",
      "Nous": "advenions",
      "Vous": "adveniez",
      "Ils/Elle": "advenaient"
    },
    "Passé Composé": {
      "Je": "suis advenu(e)",
      "Tu": "es advenu(e)",
      "Il/Elle/On": "est advenu(e)",
      "Nous": "sommes advenus(es)",
      "Vous": "êtes advenus(es)",
      "Ils/Elle": "sont advenus(es)"
    },
    "Futur": {
      "Je": "adviendrai",
      "Tu": "adviendras",
      "Il/Elle/On": "adviendra",
      "Nous": "adviendrons",
      "Vous": "adviendrez",
      "Ils/Elle": "adviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais advenu(e)",
      "Tu": "étais advenu(e)",
      "Il/Elle/On": "était advenu(e)",
      "Nous": "étions advenus(es)",
      "Vous": "étiez advenus(es)",
      "Ils/Elle": "étaient advenus(es)"
    },
    "Futur Simple": {
      "Je": "adviendrai",
      "Tu": "adviendras",
      "Il/Elle/On": "adviendra",
      "Nous": "adviendrons",
      "Vous": "adviendrez",
      "Ils/Elle": "adviendront"
    },
    "Futur Antérieur": {
      "Je": "serai advenu(e)",
      "Tu": "seras advenu(e)",
      "Il/Elle/On": "sera advenu(e)",
      "Nous": "serons advenus(es)",
      "Vous": "serez advenus(es)",
      "Ils/Elle": "seront advenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "adviendrais",
      "Tu": "adviendrais",
      "Il/Elle/On": "adviendrait",
      "Nous": "adviendrions",
      "Vous": "adviendriez",
      "Ils/Elle": "adviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais advenu(e)",
      "Tu": "serais advenu(e)",
      "Il/Elle/On": "serait advenu(e)",
      "Nous": "serions advenus(es)",
      "Vous": "seriez advenus(es)",
      "Ils/Elle": "seraient advenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "advienne",
      "Tu": "advienne",
      "Il/Elle/On": "advienne",
      "Nous": "advenions",
      "Vous": "adveniez",
      "Ils/Elle": "advienne"
    },
    "Subjonctif Passé": {
      "Je": "sois advenu(e)",
      "Tu": "sois advenu(e)",
      "Il/Elle/On": "soit advenu(e)",
      "Nous": "soyons advenus(es)",
      "Vous": "soyez advenus(es)",
      "Ils/Elle": "soient advenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse advenu(e)",
      "Tu": "fusses advenu(e)",
      "Il/Elle/On": "fût advenu(e)",
      "Nous": "fussions advenus(es)",
      "Vous": "fussiez advenus(es)",
      "Ils/Elle": "fussent advenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "advinsse",
      "Tu": "advinsse",
      "Il/Elle/On": "advînt",
      "Nous": "advinsse",
      "Vous": "advinsse",
      "Ils/Elle": "advinssent"
    },
    "Impératif Présent": {
      "Tu": "advient",
      "Nous": "advenons",
      "Vous": "advenez"
    },
    "Impératif Passé": {
      "Tu": "sois advenu(e)",
      "Nous": "soyons advenus(es)",
      "Vous": "soyez advenus(es)"
    },
    "Infinitif Présent": "advenir",
    "Infinitif Passé": "être advenu(e)",
    "Participe Présent": "advenant",
    "Participe Passé": "advenu(e)",
    "Gérondif Présent": "en advenant",
    "Gérondif Passé": "en étant advenu(e)"
  },
  "bienvenir": {
    "Présent": {
      "Je": "bienviens",
      "Tu": "bienviens",
      "Il/Elle/On": "bienvient",
      "Nous": "bienvenons",
      "Vous": "bienvenez",
      "Ils/Elle": "bienviennent"
    },
    "Imparfait": {
      "Je": "bienvenais",
      "Tu": "bienvenais",
      "Il/Elle/On": "bienvenait",
      "Nous": "bienvenions",
      "Vous": "bienveniez",
      "Ils/Elle": "bienvenaient"
    },
    "Passé Composé": {
      "Je": "suis bienvenu(e)",
      "Tu": "es bienvenu(e)",
      "Il/Elle/On": "est bienvenu(e)",
      "Nous": "sommes bienvenus(es)",
      "Vous": "êtes bienvenus(es)",
      "Ils/Elle": "sont bienvenus(es)"
    },
    "Futur": {
      "Je": "bienviendrai",
      "Tu": "bienviendras",
      "Il/Elle/On": "bienviendra",
      "Nous": "bienviendrons",
      "Vous": "bienviendrez",
      "Ils/Elle": "bienviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais bienvenu(e)",
      "Tu": "étais bienvenu(e)",
      "Il/Elle/On": "était bienvenu(e)",
      "Nous": "étions bienvenus(es)",
      "Vous": "étiez bienvenus(es)",
      "Ils/Elle": "étaient bienvenus(es)"
    },
    "Futur Simple": {
      "Je": "bienviendrai",
      "Tu": "bienviendras",
      "Il/Elle/On": "bienviendra",
      "Nous": "bienviendrons",
      "Vous": "bienviendrez",
      "Ils/Elle": "bienviendront"
    },
    "Futur Antérieur": {
      "Je": "serai bienvenu(e)",
      "Tu": "seras bienvenu(e)",
      "Il/Elle/On": "sera bienvenu(e)",
      "Nous": "serons bienvenus(es)",
      "Vous": "serez bienvenus(es)",
      "Ils/Elle": "seront bienvenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "bienviendrais",
      "Tu": "bienviendrais",
      "Il/Elle/On": "bienviendrait",
      "Nous": "bienviendrions",
      "Vous": "bienviendriez",
      "Ils/Elle": "bienviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais bienvenu(e)",
      "Tu": "serais bienvenu(e)",
      "Il/Elle/On": "serait bienvenu(e)",
      "Nous": "serions bienvenus(es)",
      "Vous": "seriez bienvenus(es)",
      "Ils/Elle": "seraient bienvenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "bienvienne",
      "Tu": "bienviennes",
      "Il/Elle/On": "bienvienne",
      "Nous": "bienvenions",
      "Vous": "bienveniez",
      "Ils/Elle": "bienviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois bienvenu(e)",
      "Tu": "sois bienvenu(e)",
      "Il/Elle/On": "soit bienvenu(e)",
      "Nous": "soyons bienvenus(es)",
      "Vous": "soyez bienvenus(es)",
      "Ils/Elle": "soient bienvenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse bienvenu(e)",
      "Tu": "fusses bienvenu(e)",
      "Il/Elle/On": "fût bienvenu(e)",
      "Nous": "fussions bienvenus(es)",
      "Vous": "fussiez bienvenus(es)",
      "Ils/Elle": "fussent bienvenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "bienvinsse",
      "Tu": "bienvinsses",
      "Il/Elle/On": "bienvînt",
      "Nous": "bienvinssions",
      "Vous": "bienvinssiez",
      "Ils/Elle": "bienvinssent"
    },
    "Impératif Présent": {
      "Tu": "bienviens",
      "Nous": "bienvenons",
      "Vous": "bienvenez"
    },
    "Impératif Passé": {
      "Tu": "sois bienvenu(e)",
      "Nous": "soyons bienvenus(es)",
      "Vous": "soyez bienvenus(es)"
    },
    "Infinitif Présent": "bienvenir",
    "Infinitif Passé": "être bienvenu(e)",
    "Participe Présent": "bienvenant",
    "Participe Passé": "bienvenu(e)",
    "Gérondif Présent": "en bienvenant",
    "Gérondif Passé": "en étant bienvenu(e)"
  },
  "circonvenir": {
    "Présent": {
      "Je": "circonviens",
      "Tu": "circonviens",
      "Il/Elle/On": "circonvient",
      "Nous": "circonvenons",
      "Vous": "circonvenez",
      "Ils/Elle": "circonviennent"
    },
    "Imparfait": {
      "Je": "circonvenais",
      "Tu": "circonvenais",
      "Il/Elle/On": "circonvenait",
      "Nous": "circonvenions",
      "Vous": "circonveniez",
      "Ils/Elle": "circonvenaient"
    },
    "Passé Composé": {
      "Je": "suis circonvenu(e)",
      "Tu": "es circonvenu(e)",
      "Il/Elle/On": "est circonvenu(e)",
      "Nous": "sommes circonvenus(es)",
      "Vous": "êtes circonvenus(es)",
      "Ils/Elle": "sont circonvenus(es)"
    },
    "Futur": {
      "Je": "circonviendrai",
      "Tu": "circonviendras",
      "Il/Elle/On": "circonviendra",
      "Nous": "circonviendrons",
      "Vous": "circonviendrez",
      "Ils/Elle": "circonviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais circonvenu(e)",
      "Tu": "étais circonvenu(e)",
      "Il/Elle/On": "était circonvenu(e)",
      "Nous": "étions circonvenus(es)",
      "Vous": "étiez circonvenus(es)",
      "Ils/Elle": "étaient circonvenus(es)"
    },
    "Futur Simple": {
      "Je": "circonviendrai",
      "Tu": "circonviendras",
      "Il/Elle/On": "circonviendra",
      "Nous": "circonviendrons",
      "Vous": "circonviendrez",
      "Ils/Elle": "circonviendront"
    },
    "Futur Antérieur": {
      "Je": "serai circonvenu(e)",
      "Tu": "seras circonvenu(e)",
      "Il/Elle/On": "sera circonvenu(e)",
      "Nous": "serons circonvenus(es)",
      "Vous": "serez circonvenus(es)",
      "Ils/Elle": "seront circonvenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "circonviendrais",
      "Tu": "circonviendrais",
      "Il/Elle/On": "circonviendrait",
      "Nous": "circonviendrions",
      "Vous": "circonviendriez",
      "Ils/Elle": "circonviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais circonvenu(e)",
      "Tu": "serais circonvenu(e)",
      "Il/Elle/On": "serait circonvenu(e)",
      "Nous": "serions circonvenus(es)",
      "Vous": "seriez circonvenus(es)",
      "Ils/Elle": "seraient circonvenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "circonvienne",
      "Tu": "circonviennes",
      "Il/Elle/On": "circonvienne",
      "Nous": "circonvenions",
      "Vous": "circonveniez",
      "Ils/Elle": "circonviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois circonvenu(e)",
      "Tu": "sois circonvenu(e)",
      "Il/Elle/On": "soit circonvenu(e)",
      "Nous": "soyons circonvenus(es)",
      "Vous": "soyez circonvenus(es)",
      "Ils/Elle": "soient circonvenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse circonvenu(e)",
      "Tu": "fusses circonvenu(e)",
      "Il/Elle/On": "fût circonvenu(e)",
      "Nous": "fussions circonvenus(es)",
      "Vous": "fussiez circonvenus(es)",
      "Ils/Elle": "fussent circonvenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "circonvinsse",
      "Tu": "circonvinsses",
      "Il/Elle/On": "circonvînt",
      "Nous": "circonvinssions",
      "Vous": "circonvinssiez",
      "Ils/Elle": "circonvinssent"
    },
    "Impératif Présent": {
      "Tu": "circonviens",
      "Nous": "circonvenons",
      "Vous": "circonvenez"
    },
    "Impératif Passé": {
      "Tu": "sois circonvenu(e)",
      "Nous": "soyons circonvenus(es)",
      "Vous": "soyez circonvenus(es)"
    },
    "Infinitif Présent": "circonvenir",
    "Infinitif Passé": "être circonvenu(e)",
    "Participe Présent": "circonvenant",
    "Participe Passé": "circonvenu(e)",
    "Gérondif Présent": "en circonvenant",
    "Gérondif Passé": "en étant circonvenu(e)"
  },
  "contrevenir": {
    "Présent": {
      "Je": "contreviens",
      "Tu": "contreviens",
      "Il/Elle/On": "contrevient",
      "Nous": "contrevenons",
      "Vous": "contrevenez",
      "Ils/Elle": "contreviennent"
    },
    "Imparfait": {
      "Je": "contrevenais",
      "Tu": "contrevenais",
      "Il/Elle/On": "contrevenait",
      "Nous": "contrevenions",
      "Vous": "contreveniez",
      "Ils/Elle": "contrevenaient"
    },
    "Passé Composé": {
      "Je": "suis contrevenu(e)",
      "Tu": "es contrevenu(e)",
      "Il/Elle/On": "est contrevenu(e)",
      "Nous": "sommes contrevenus(es)",
      "Vous": "êtes contrevenus(es)",
      "Ils/Elle": "sont contrevenus(es)"
    },
    "Futur": {
      "Je": "contreviendrai",
      "Tu": "contreviendras",
      "Il/Elle/On": "contreviendra",
      "Nous": "contreviendrons",
      "Vous": "contreviendrez",
      "Ils/Elle": "contreviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais contrevenu(e)",
      "Tu": "étais contrevenu(e)",
      "Il/Elle/On": "était contrevenu(e)",
      "Nous": "étions contrevenus(es)",
      "Vous": "étiez contrevenus(es)",
      "Ils/Elle": "étaient contrevenus(es)"
    },
    "Futur Simple": {
      "Je": "contreviendrai",
      "Tu": "contreviendras",
      "Il/Elle/On": "contreviendra",
      "Nous": "contreviendrons",
      "Vous": "contreviendrez",
      "Ils/Elle": "contreviendront"
    },
    "Futur Antérieur": {
      "Je": "serai contrevenu(e)",
      "Tu": "seras contrevenu(e)",
      "Il/Elle/On": "sera contrevenu(e)",
      "Nous": "serons contrevenus(es)",
      "Vous": "serez contrevenus(es)",
      "Ils/Elle": "seront contrevenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "contreviendrais",
      "Tu": "contreviendrais",
      "Il/Elle/On": "contreviendrait",
      "Nous": "contreviendrions",
      "Vous": "contreviendriez",
      "Ils/Elle": "contreviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais contrevenu(e)",
      "Tu": "serais contrevenu(e)",
      "Il/Elle/On": "serait contrevenu(e)",
      "Nous": "serions contrevenus(es)",
      "Vous": "seriez contrevenus(es)",
      "Ils/Elle": "seraient contrevenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "contrevienne",
      "Tu": "contreviennes",
      "Il/Elle/On": "contrevienne",
      "Nous": "contrevenions",
      "Vous": "contreveniez",
      "Ils/Elle": "contreviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois contrevenu(e)",
      "Tu": "sois contrevenu(e)",
      "Il/Elle/On": "soit contrevenu(e)",
      "Nous": "soyons contrevenus(es)",
      "Vous": "soyez contrevenus(es)",
      "Ils/Elle": "soient contrevenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse contrevenu(e)",
      "Tu": "fusses contrevenu(e)",
      "Il/Elle/On": "fût contrevenu(e)",
      "Nous": "fussions contrevenus(es)",
      "Vous": "fussiez contrevenus(es)",
      "Ils/Elle": "fussent contrevenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "contrevinsse",
      "Tu": "contrevinsses",
      "Il/Elle/On": "contrevînt",
      "Nous": "contrevinssions",
      "Vous": "contrevinssiez",
      "Ils/Elle": "contrevinssent"
    },
    "Impératif Présent": {
      "Tu": "contreviens",
      "Nous": "contrevenons",
      "Vous": "contrevenez"
    },
    "Impératif Passé": {
      "Tu": "sois contrevenu(e)",
      "Nous": "soyons contrevenus(es)",
      "Vous": "soyez contrevenus(es)"
    },
    "Infinitif Présent": "contrevenir",
    "Infinitif Passé": "être contrevenu(e)",
    "Participe Présent": "contrevenant",
    "Participe Passé": "contrevenu(e)",
    "Gérondif Présent": "en contrevenant",
    "Gérondif Passé": "en étant contrevenu(e)"
  },
  "convenir": {
    "Présent": {
      "Je": "conviens",
      "Tu": "conviens",
      "Il/Elle/On": "convient",
      "Nous": "convenons",
      "Vous": "convenez",
      "Ils/Elle": "conviennent"
    },
    "Imparfait": {
      "Je": "convenais",
      "Tu": "convenais",
      "Il/Elle/On": "convenait",
      "Nous": "convenions",
      "Vous": "conveniez",
      "Ils/Elle": "convenaient"
    },
    "Passé Composé": {
      "Je": "suis convenu(e)",
      "Tu": "es convenu(e)",
      "Il/Elle/On": "est convenu(e)",
      "Nous": "sommes convenus(es)",
      "Vous": "êtes convenus(es)",
      "Ils/Elle": "sont convenus(es)"
    },
    "Futur": {
      "Je": "conviendrai",
      "Tu": "conviendras",
      "Il/Elle/On": "conviendra",
      "Nous": "conviendrons",
      "Vous": "conviendrez",
      "Ils/Elle": "conviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais convenu(e)",
      "Tu": "étais convenu(e)",
      "Il/Elle/On": "était convenu(e)",
      "Nous": "étions convenus(es)",
      "Vous": "étiez convenus(es)",
      "Ils/Elle": "étaient convenus(es)"
    },
    "Futur Simple": {
      "Je": "conviendrai",
      "Tu": "conviendras",
      "Il/Elle/On": "conviendra",
      "Nous": "conviendrons",
      "Vous": "conviendrez",
      "Ils/Elle": "conviendront"
    },
    "Futur Antérieur": {
      "Je": "serai convenu(e)",
      "Tu": "seras convenu(e)",
      "Il/Elle/On": "sera convenu(e)",
      "Nous": "serons convenus(es)",
      "Vous": "serez convenus(es)",
      "Ils/Elle": "seront convenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "conviendrais",
      "Tu": "conviendrais",
      "Il/Elle/On": "conviendrait",
      "Nous": "conviendrions",
      "Vous": "conviendriez",
      "Ils/Elle": "conviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais convenu(e)",
      "Tu": "serais convenu(e)",
      "Il/Elle/On": "serait convenu(e)",
      "Nous": "serions convenus(es)",
      "Vous": "seriez convenus(es)",
      "Ils/Elle": "seraient convenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "conviene",
      "Tu": "conviennes",
      "Il/Elle/On": "conviene",
      "Nous": "convenions",
      "Vous": "conveniez",
      "Ils/Elle": "conviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois convenu(e)",
      "Tu": "sois convenu(e)",
      "Il/Elle/On": "soit convenu(e)",
      "Nous": "soyons convenus(es)",
      "Vous": "soyez convenus(es)",
      "Ils/Elle": "soient convenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse convenu(e)",
      "Tu": "fusses convenu(e)",
      "Il/Elle/On": "fût convenu(e)",
      "Nous": "fussions convenus(es)",
      "Vous": "fussiez convenus(es)",
      "Ils/Elle": "fussent convenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "convinsse",
      "Tu": "convinsse",
      "Il/Elle/On": "convînt",
      "Nous": "convinsse",
      "Vous": "convinsse",
      "Ils/Elle": "convissent"
    },
    "Impératif Présent": {
      "Tu": "conviens",
      "Nous": "convenons",
      "Vous": "convenez"
    },
    "Impératif Passé": {
      "Tu": "sois convenu(e)",
      "Nous": "soyons convenus(es)",
      "Vous": "soyez convenus(es)"
    },
    "Infinitif Présent": "convenir",
    "Infinitif Passé": "être convenu(e)",
    "Participe Présent": "convenant",
    "Participe Passé": "convenu(e)",
    "Gérondif Présent": "en convenant",
    "Gérondif Passé": "en étant convenu(e)"
  },
  "devenir": {
    "Présent": {
      "Je": "deviens",
      "Tu": "deviens",
      "Il/Elle/On": "devient",
      "Nous": "devenons",
      "Vous": "devenez",
      "Ils/Elle": "deviennent"
    },
    "Imparfait": {
      "Je": "devenais",
      "Tu": "devenais",
      "Il/Elle/On": "devenait",
      "Nous": "devenions",
      "Vous": "deveniez",
      "Ils/Elle": "devenaient"
    },
    "Passé Composé": {
      "Je": "suis devenu(e)",
      "Tu": "es devenu(e)",
      "Il/Elle/On": "est devenu(e)",
      "Nous": "sommes devenus(es)",
      "Vous": "êtes devenus(es)",
      "Ils/Elle": "sont devenus(es)"
    },
    "Futur": {
      "Je": "deviendrai",
      "Tu": "deviendras",
      "Il/Elle/On": "deviendra",
      "Nous": "deviendrons",
      "Vous": "deviendrez",
      "Ils/Elle": "deviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais devenu(e)",
      "Tu": "étais devenu(e)",
      "Il/Elle/On": "était devenu(e)",
      "Nous": "étions devenus(es)",
      "Vous": "étiez devenus(es)",
      "Ils/Elle": "étaient devenus(es)"
    },
    "Futur Simple": {
      "Je": "deviendrai",
      "Tu": "deviendras",
      "Il/Elle/On": "deviendra",
      "Nous": "deviendrons",
      "Vous": "deviendrez",
      "Ils/Elle": "deviendront"
    },
    "Futur Antérieur": {
      "Je": "serai devenu(e)",
      "Tu": "seras devenu(e)",
      "Il/Elle/On": "sera devenu(e)",
      "Nous": "serons devenus(es)",
      "Vous": "serez devenus(es)",
      "Ils/Elle": "seront devenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "deviendrais",
      "Tu": "deviendrais",
      "Il/Elle/On": "deviendrait",
      "Nous": "deviendrions",
      "Vous": "deviendriez",
      "Ils/Elle": "deviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais devenu(e)",
      "Tu": "serais devenu(e)",
      "Il/Elle/On": "serait devenu(e)",
      "Nous": "serions devenus(es)",
      "Vous": "seriez devenus(es)",
      "Ils/Elle": "seraient devenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "devienne",
      "Tu": "deviennes",
      "Il/Elle/On": "devienne",
      "Nous": "devenions",
      "Vous": "deveniez",
      "Ils/Elle": "deviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois devenu(e)",
      "Tu": "sois devenu(e)",
      "Il/Elle/On": "soit devenu(e)",
      "Nous": "soyons devenus(es)",
      "Vous": "soyez devenus(es)",
      "Ils/Elle": "soient devenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse devenu(e)",
      "Tu": "fusses devenu(e)",
      "Il/Elle/On": "fût devenu(e)",
      "Nous": "fussions devenus(es)",
      "Vous": "fussiez devenus(es)",
      "Ils/Elle": "fussent devenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "devinsse",
      "Tu": "devinsse",
      "Il/Elle/On": "devînt",
      "Nous": "devinsse",
      "Vous": "devinsse",
      "Ils/Elle": "devinssent"
    },
    "Impératif Présent": {
      "Tu": "deviens",
      "Nous": "devenons",
      "Vous": "devenez"
    },
    "Impératif Passé": {
      "Tu": "sois devenu(e)",
      "Nous": "soyons devenus(es)",
      "Vous": "soyez devenus(es)"
    },
    "Infinitif Présent": "devenir",
    "Infinitif Passé": "être devenu(e)",
    "Participe Présent": "devenant",
    "Participe Passé": "devenu(e)",
    "Gérondif Présent": "en devenant",
    "Gérondif Passé": "en étant devenu(e)"
  },
  "venir": {
    "Présent": {
      "Je": "viens",
      "Tu": "viens",
      "Il/Elle/On": "vient",
      "Nous": "venons",
      "Vous": "venez",
      "Ils/Elle": "viennent"
    },
    "Imparfait": {
      "Je": "venais",
      "Tu": "venais",
      "Il/Elle/On": "venait",
      "Nous": "venions",
      "Vous": "veniez",
      "Ils/Elle": "venaient"
    },
    "Passé Composé": {
      "Je": "suis venu(e)",
      "Tu": "es venu(e)",
      "Il/Elle/On": "est venu(e)",
      "Nous": "sommes venus(es)",
      "Vous": "êtes venus(es)",
      "Ils/Elle": "sont venus(es)"
    },
    "Futur": {
      "Je": "viendrai",
      "Tu": "viendras",
      "Il/Elle/On": "viendra",
      "Nous": "viendrons",
      "Vous": "viendrez",
      "Ils/Elle": "viendront"
    },
    "Plus-que-parfait": {
      "Je": "étais venu(e)",
      "Tu": "étais venu(e)",
      "Il/Elle/On": "était venu(e)",
      "Nous": "étions venus(es)",
      "Vous": "étiez venus(es)",
      "Ils/Elle": "étaient venus(es)"
    },
    "Futur Simple": {
      "Je": "viendrai",
      "Tu": "viendras",
      "Il/Elle/On": "viendra",
      "Nous": "viendrons",
      "Vous": "viendrez",
      "Ils/Elle": "viendront"
    },
    "Futur Antérieur": {
      "Je": "serai venu(e)",
      "Tu": "seras venu(e)",
      "Il/Elle/On": "sera venu(e)",
      "Nous": "serons venus(es)",
      "Vous": "serez venus(es)",
      "Ils/Elle": "seront venus(es)"
    },
    "Conditionnel Présent": {
      "Je": "viendrais",
      "Tu": "viendrais",
      "Il/Elle/On": "viendrait",
      "Nous": "viendrions",
      "Vous": "viendriez",
      "Ils/Elle": "viendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais venu(e)",
      "Tu": "serais venu(e)",
      "Il/Elle/On": "serait venu(e)",
      "Nous": "serions venus(es)",
      "Vous": "seriez venus(es)",
      "Ils/Elle": "seraient venus(es)"
    },
    "Subjonctif Présent": {
      "Je": "vienne",
      "Tu": "viennes",
      "Il/Elle/On": "vienne",
      "Nous": "venions",
      "Vous": "veniez",
      "Ils/Elle": "viennent"
    },
    "Subjonctif Passé": {
      "Je": "sois venu(e)",
      "Tu": "sois venu(e)",
      "Il/Elle/On": "soit venu(e)",
      "Nous": "soyons venus(es)",
      "Vous": "soyez venus(es)",
      "Ils/Elle": "soient venus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse venu(e)",
      "Tu": "fusses venu(e)",
      "Il/Elle/On": "fût venu(e)",
      "Nous": "fussions venus(es)",
      "Vous": "fussiez venus(es)",
      "Ils/Elle": "fussent venus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "vinsse",
      "Tu": "vinsse",
      "Il/Elle/On": "vînt",
      "Nous": "vinsse",
      "Vous": "vinsse",
      "Ils/Elle": "vinssent"
    },
    "Impératif Présent": {
      "Tu": "viens",
      "Nous": "venons",
      "Vous": "venez"
    },
    "Impératif Passé": {
      "Tu": "sois venu(e)",
      "Nous": "soyons venus(es)",
      "Vous": "soyez venus(es)"
    },
    "Infinitif Présent": "venir",
    "Infinitif Passé": "être venu(e)",
    "Participe Présent": "venant",
    "Participe Passé": "venu(e)",
    "Gérondif Présent": "en venant",
    "Gérondif Passé": "en étant venu(e)"
  },
  "intervenir": {
    "Présent": {
      "Je": "interviens",
      "Tu": "interviens",
      "Il/Elle/On": "intervient",
      "Nous": "intervenons",
      "Vous": "intervenez",
      "Ils/Elle": "interviennent"
    },
    "Imparfait": {
      "Je": "intervenais",
      "Tu": "intervenais",
      "Il/Elle/On": "intervenait",
      "Nous": "intervenions",
      "Vous": "interveniez",
      "Ils/Elle": "intervenaient"
    },
    "Passé Composé": {
      "Je": "suis intervenu(e)",
      "Tu": "es intervenu(e)",
      "Il/Elle/On": "est intervenu(e)",
      "Nous": "sommes intervenus(es)",
      "Vous": "êtes intervenus(es)",
      "Ils/Elle": "sont intervenus(es)"
    },
    "Futur": {
      "Je": "interviendrai",
      "Tu": "interviendras",
      "Il/Elle/On": "interviendra",
      "Nous": "interviendrons",
      "Vous": "interviendrez",
      "Ils/Elle": "interviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais intervenu(e)",
      "Tu": "étais intervenu(e)",
      "Il/Elle/On": "était intervenu(e)",
      "Nous": "étions intervenus(es)",
      "Vous": "étiez intervenus(es)",
      "Ils/Elle": "étaient intervenus(es)"
    },
    "Futur Simple": {
      "Je": "interviendrai",
      "Tu": "interviendras",
      "Il/Elle/On": "interviendra",
      "Nous": "interviendrons",
      "Vous": "interviendrez",
      "Ils/Elle": "interviendront"
    },
    "Futur Antérieur": {
      "Je": "serai intervenu(e)",
      "Tu": "seras intervenu(e)",
      "Il/Elle/On": "sera intervenu(e)",
      "Nous": "serons intervenus(es)",
      "Vous": "serez intervenus(es)",
      "Ils/Elle": "seront intervenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "interviendrais",
      "Tu": "interviendrais",
      "Il/Elle/On": "interviendrait",
      "Nous": "interviendrions",
      "Vous": "interviendriez",
      "Ils/Elle": "interviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais intervenu(e)",
      "Tu": "serais intervenu(e)",
      "Il/Elle/On": "serait intervenu(e)",
      "Nous": "serions intervenus(es)",
      "Vous": "seriez intervenus(es)",
      "Ils/Elle": "seraient intervenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "intervienne",
      "Tu": "interviennes",
      "Il/Elle/On": "intervienne",
      "Nous": "intervenions",
      "Vous": "interveniez",
      "Ils/Elle": "interviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois intervenu(e)",
      "Tu": "sois intervenu(e)",
      "Il/Elle/On": "soit intervenu(e)",
      "Nous": "soyons intervenus(es)",
      "Vous": "soyez intervenus(es)",
      "Ils/Elle": "soient intervenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse intervenu(e)",
      "Tu": "fusses intervenu(e)",
      "Il/Elle/On": "fût intervenu(e)",
      "Nous": "fussions intervenus(es)",
      "Vous": "fussiez intervenus(es)",
      "Ils/Elle": "fussent intervenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "intervinsse",
      "Tu": "intervinsses",
      "Il/Elle/On": "intervînt",
      "Nous": "intervinssions",
      "Vous": "intervinssiez",
      "Ils/Elle": "intervinssent"
    },
    "Impératif Présent": {
      "Tu": "interviens",
      "Nous": "intervenons",
      "Vous": "intervenez"
    },
    "Impératif Passé": {
      "Tu": "sois intervenu(e)",
      "Nous": "soyons intervenus(es)",
      "Vous": "soyez intervenus(es)"
    },
    "Infinitif Présent": "intervenir",
    "Infinitif Passé": "être intervenu(e)",
    "Participe Présent": "intervenant",
    "Participe Passé": {
      "Masculin Singulier": "intervenu",
      "Masculin Pluriel": "intervenus",
      "Féminin Singulier": "intervenue",
      "Féminin Pluriel": "intervenues"
    },
    "Gérondif Présent": "en intervenant",
    "Gérondif Passé": {
      "Masculin Singulier": "en étant intervenu",
      "Masculin Pluriel": "en étant intervenus",
      "Féminin Singulier": "en étant intervenue",
      "Féminin Pluriel": "en étant intervenues"
    }
},
"obvenir": {
    "Présent": {
      "Je": "obviens",
      "Tu": "obviens",
      "Il/Elle/On": "obvient",
      "Nous": "obvenons",
      "Vous": "obvenez",
      "Ils/Elle": "obviennent"
    },
    "Imparfait": {
      "Je": "obvenais",
      "Tu": "obvenais",
      "Il/Elle/On": "obvenait",
      "Nous": "obvenions",
      "Vous": "obveniez",
      "Ils/Elle": "obvenaient"
    },
    "Passé Composé": {
      "Je": "suis obvenu(e)",
      "Tu": "es obvenu(e)",
      "Il/Elle/On": "est obvenu(e)",
      "Nous": "sommes obvenus(es)",
      "Vous": "êtes obvenus(es)",
      "Ils/Elle": "sont obvenus(es)"
    },
    "Futur": {
      "Je": "obviendrai",
      "Tu": "obviendras",
      "Il/Elle/On": "obtiendra",
      "Nous": "obviendrons",
      "Vous": "obviendrez",
      "Ils/Elle": "obtiendront"
    },
    "Plus-que-parfait": {
      "Je": "étais obvenu(e)",
      "Tu": "étais obvenu(e)",
      "Il/Elle/On": "était obvenu(e)",
      "Nous": "étions obvenus(es)",
      "Vous": "étiez obvenus(es)",
      "Ils/Elle": "étaient obvenus(es)"
    },
    "Futur Simple": {
      "Je": "obviendrai",
      "Tu": "obviendras",
      "Il/Elle/On": "obtiendra",
      "Nous": "obviendrons",
      "Vous": "obviendrez",
      "Ils/Elle": "obtiendront"
    },
    "Futur Antérieur": {
      "Je": "serai obvenu(e)",
      "Tu": "seras obvenu(e)",
      "Il/Elle/On": "sera obvenu(e)",
      "Nous": "serons obvenus(es)",
      "Vous": "serez obvenus(es)",
      "Ils/Elle": "seront obvenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "obviendrais",
      "Tu": "obviendrais",
      "Il/Elle/On": "obviendrait",
      "Nous": "obviendrions",
      "Vous": "obviendriez",
      "Ils/Elle": "obviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais obvenu(e)",
      "Tu": "serais obvenu(e)",
      "Il/Elle/On": "serait obvenu(e)",
      "Nous": "serions obvenus(es)",
      "Vous": "seriez obvenus(es)",
      "Ils/Elle": "seraient obvenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "obvienne",
      "Tu": "obviennes",
      "Il/Elle/On": "obvienne",
      "Nous": "obvenions",
      "Vous": "obveniez",
      "Ils/Elle": "obviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois obvenu(e)",
      "Tu": "sois obvenu(e)",
      "Il/Elle/On": "soit obvenu(e)",
      "Nous": "soyons obvenus(es)",
      "Vous": "soyez obvenus(es)",
      "Ils/Elle": "soient obvenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse obvenu(e)",
      "Tu": "fusses obvenu(e)",
      "Il/Elle/On": "fût obvenu(e)",
      "Nous": "fussions obvenus(es)",
      "Vous": "fussiez obvenus(es)",
      "Ils/Elle": "fussent obvenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "obvinisse",
      "Tu": "obvinisses",
      "Il/Elle/On": "obvînt",
      "Nous": "obvinissions",
      "Vous": "obvinissiez",
      "Ils/Elle": "obvinissent"
    },
    "Impératif Présent": {
      "Tu": "obviens",
      "Nous": "obvenons",
      "Vous": "obvenez"
    },
    "Impératif Passé": {
      "Tu": "sois obvenu(e)",
      "Nous": "soyons obvenus(es)",
      "Vous": "soyez obvenus(es)"
    },
    "Infinitif Présent": "obvenir",
    "Infinitif Passé": "être obvenu(e)",
    "Participe Présent": "obvenant",
    "Participe Passé": {
      "Masculin Singulier": "obvenu",
      "Masculin Pluriel": "obvenus",
      "Féminin Singulier": "obvenue",
      "Féminin Pluriel": "obvenues"
    },
    "Gérondif Présent": "en obvenant",
    "Gérondif Passé": {
      "Masculin Singulier": "en étant obvenu",
      "Masculin Pluriel": "en étant obvenus",
      "Féminin Singulier": "en étant obvenue",
      "Féminin Pluriel": "en étant obvenues"
    }
},
"parvenir": {
    "Présent": {
      "Je": "parviens",
      "Tu": "parviens",
      "Il/Elle/On": "parvient",
      "Nous": "parvenons",
      "Vous": "parvenez",
      "Ils/Elle": "parviennent"
    },
    "Imparfait": {
      "Je": "parvenais",
      "Tu": "parvenais",
      "Il/Elle/On": "parvenait",
      "Nous": "parvenions",
      "Vous": "parveniez",
      "Ils/Elle": "parvenaient"
    },
    "Passé Composé": {
      "Je": "suis parvenu(e)",
      "Tu": "es parvenu(e)",
      "Il/Elle/On": "est parvenu(e)",
      "Nous": "sommes parvenus(es)",
      "Vous": "êtes parvenus(es)",
      "Ils/Elle": "sont parvenus(es)"
    },
    "Futur": {
      "Je": "parviendrai",
      "Tu": "parviendras",
      "Il/Elle/On": "parviendra",
      "Nous": "parviendrons",
      "Vous": "parviendrez",
      "Ils/Elle": "parviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais parvenu(e)",
      "Tu": "étais parvenu(e)",
      "Il/Elle/On": "était parvenu(e)",
      "Nous": "étions parvenus(es)",
      "Vous": "étiez parvenus(es)",
      "Ils/Elle": "étaient parvenus(es)"
    },
    "Futur Simple": {
      "Je": "parviendrai",
      "Tu": "parviendras",
      "Il/Elle/On": "parviendra",
      "Nous": "parviendrons",
      "Vous": "parviendrez",
      "Ils/Elle": "parviendront"
    },
    "Futur Antérieur": {
      "Je": "serai parvenu(e)",
      "Tu": "seras parvenu(e)",
      "Il/Elle/On": "sera parvenu(e)",
      "Nous": "serons parvenus(es)",
      "Vous": "serez parvenus(es)",
      "Ils/Elle": "seront parvenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "parviendrais",
      "Tu": "parviendrais",
      "Il/Elle/On": "parviendrait",
      "Nous": "parviendrions",
      "Vous": "parviendriez",
      "Ils/Elle": "parviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais parvenu(e)",
      "Tu": "serais parvenu(e)",
      "Il/Elle/On": "serait parvenu(e)",
      "Nous": "serions parvenus(es)",
      "Vous": "seriez parvenus(es)",
      "Ils/Elle": "seraient parvenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "parvienne",
      "Tu": "parviennes",
      "Il/Elle/On": "parvienne",
      "Nous": "parvenions",
      "Vous": "parveniez",
      "Ils/Elle": "parviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois parvenu(e)",
      "Tu": "sois parvenu(e)",
      "Il/Elle/On": "soit parvenu(e)",
      "Nous": "soyons parvenus(es)",
      "Vous": "soyez parvenus(es)",
      "Ils/Elle": "soient parvenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse parvenu(e)",
      "Tu": "fusses parvenu(e)",
      "Il/Elle/On": "fût parvenu(e)",
      "Nous": "fussions parvenus(es)",
      "Vous": "fussiez parvenus(es)",
      "Ils/Elle": "fussent parvenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "parvinsse",
      "Tu": "parvinsses",
      "Il/Elle/On": "parvînt",
      "Nous": "parvinssions",
      "Vous": "parvinssiez",
      "Ils/Elle": "parvinssent"
    },
    "Impératif Présent": {
      "Tu": "parviens",
      "Nous": "parvenons",
      "Vous": "parvenez"
    },
    "Impératif Passé": {
      "Tu": "sois parvenu(e)",
      "Nous": "soyons parvenus(es)",
      "Vous": "soyez parvenus(es)"
    },
    "Infinitif Présent": "parvenir",
    "Infinitif Passé": "être parvenu(e)",
    "Participe Présent": "parvenant",
    "Participe Passé": {
      "Masculin Singulier": "parvenu",
      "Masculin Pluriel": "parvenus",
      "Féminin Singulier": "parvenue",
      "Féminin Pluriel": "parvenues"
    },
    "Gérondif Présent": "en parvenant",
    "Gérondif Passé": {
      "Masculin Singulier": "en étant parvenu",
      "Masculin Pluriel": "en étant parvenus",
      "Féminin Singulier": "en étant parvenue",
      "Féminin Pluriel": "en étant parvenues"
    }
},
"prévenir": {
    "Présent": {
      "Je": "préviens",
      "Tu": "préviens",
      "Il/Elle/On": "prévient",
      "Nous": "prévenons",
      "Vous": "prévenez",
      "Ils/Elle": "préviennent"
    },
    "Imparfait": {
      "Je": "prévenais",
      "Tu": "prévenais",
      "Il/Elle/On": "prévenait",
      "Nous": "prévenions",
      "Vous": "préveniez",
      "Ils/Elle": "prévenaient"
    },
    "Passé Composé": {
      "Je": "ai prévenu(e)",
      "Tu": "as prévenu(e)",
      "Il/Elle/On": "a prévenu(e)",
      "Nous": "avons prévenu(e)s",
      "Vous": "avez prévenu(e)s",
      "Ils/Elle": "ont prévenu(e)s"
    },
    "Futur": {
      "Je": "préviendrai",
      "Tu": "préviendras",
      "Il/Elle/On": "préviendra",
      "Nous": "préviendrons",
      "Vous": "préviendrez",
      "Ils/Elle": "préviendront"
    },
    "Plus-que-parfait": {
      "Je": "avais prévenu(e)",
      "Tu": "avais prévenu(e)",
      "Il/Elle/On": "avait prévenu(e)",
      "Nous": "avions prévenu(e)s",
      "Vous": "aviez prévenu(e)s",
      "Ils/Elle": "avaient prévenu(e)s"
    },
    "Futur Simple": {
      "Je": "préviendrai",
      "Tu": "préviendras",
      "Il/Elle/On": "préviendra",
      "Nous": "préviendrons",
      "Vous": "préviendrez",
      "Ils/Elle": "préviendront"
    },
    "Futur Antérieur": {
      "Je": "aurai prévenu(e)",
      "Tu": "auras prévenu(e)",
      "Il/Elle/On": "aura prévenu(e)",
      "Nous": "aurons prévenu(e)s",
      "Vous": "aurez prévenu(e)s",
      "Ils/Elle": "auront prévenu(e)s"
    },
    "Conditionnel Présent": {
      "Je": "préviendrais",
      "Tu": "préviendrais",
      "Il/Elle/On": "préviendrait",
      "Nous": "préviendrions",
      "Vous": "préviendriez",
      "Ils/Elle": "préviendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais prévenu(e)",
      "Tu": "aurais prévenu(e)",
      "Il/Elle/On": "aurait prévenu(e)",
      "Nous": "aurions prévenu(e)s",
      "Vous": "auriez prévenu(e)s",
      "Ils/Elle": "auraient prévenu(e)s"
    },
    "Subjonctif Présent": {
      "Je": "prévienne",
      "Tu": "préviennes",
      "Il/Elle/On": "prévienne",
      "Nous": "prévenions",
      "Vous": "préveniez",
      "Ils/Elle": "préviennent"
    },
    "Subjonctif Passé": {
      "Je": "aie prévenu(e)",
      "Tu": "aies prévenu(e)",
      "Il/Elle/On": "ait prévenu(e)",
      "Nous": "ayons prévenu(e)s",
      "Vous": "ayez prévenu(e)s",
      "Ils/Elle": "aient prévenu(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse prévenu(e)",
      "Tu": "eusses prévenu(e)",
      "Il/Elle/On": "eût prévenu(e)",
      "Nous": "eussions prévenu(e)s",
      "Vous": "eussiez prévenu(e)s",
      "Ils/Elle": "eussent prévenu(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "prévinsse",
      "Tu": "prévinsses",
      "Il/Elle/On": "prévînt",
      "Nous": "prévinssions",
      "Vous": "prévinssiez",
      "Ils/Elle": "prévinssent"
    },
    "Impératif Présent": {
      "Tu": "préviens",
      "Nous": "prévenons",
      "Vous": "prévenez"
    },
    "Impératif Passé": {
      "Tu": "aie prévenu(e)",
      "Nous": "ayons prévenu(e)s",
      "Vous": "ayez prévenu(e)s"
    },
    "Infinitif Présent": "prévenir",
    "Infinitif Passé": "avoir prévenu(e)",
    "Participe Présent": "prévenant",
    "Participe Passé": {
      "Masculin Singulier": "prévenu",
      "Masculin Pluriel": "prévenus",
      "Féminin Singulier": "prévenue",
      "Féminin Pluriel": "prévenues"
    },
    "Gérondif Présent": "en prévenant",
    "Gérondif Passé": {
      "Masculin Singulier": "en ayant prévenu",
      "Masculin Pluriel": "en ayant prévenus",
      "Féminin Singulier": "en ayant prévenue",
      "Féminin Pluriel": "en ayant prévenues"
    }
},
"provenir": {
    "Présent": {
      "Je": "provien",
      "Tu": "provien",
      "Il/Elle/On": "provient",
      "Nous": "provenons",
      "Vous": "provenez",
      "Ils/Elle": "proviennent"
    },
    "Imparfait": {
      "Je": "provenais",
      "Tu": "provenais",
      "Il/Elle/On": "provenait",
      "Nous": "provenions",
      "Vous": "proveniez",
      "Ils/Elle": "provenaient"
    },
    "Passé Composé": {
      "Je": "ai provenu(e)",
      "Tu": "as provenu(e)",
      "Il/Elle/On": "a provenu(e)",
      "Nous": "avons provenu(e)s",
      "Vous": "avez provenu(e)s",
      "Ils/Elle": "ont provenu(e)s"
    },
    "Futur": {
      "Je": "proviendrai",
      "Tu": "proviendras",
      "Il/Elle/On": "proviendra",
      "Nous": "proviendrons",
      "Vous": "proviendrez",
      "Ils/Elle": "proviendront"
    },
    "Plus-que-parfait": {
      "Je": "avais provenu(e)",
      "Tu": "avais provenu(e)",
      "Il/Elle/On": "avait provenu(e)",
      "Nous": "avions provenu(e)s",
      "Vous": "aviez provenu(e)s",
      "Ils/Elle": "avaient provenu(e)s"
    },
    "Futur Simple": {
      "Je": "proviendrai",
      "Tu": "proviendras",
      "Il/Elle/On": "proviendra",
      "Nous": "proviendrons",
      "Vous": "proviendrez",
      "Ils/Elle": "proviendront"
    },
    "Futur Antérieur": {
      "Je": "aurai provenu(e)",
      "Tu": "auras provenu(e)",
      "Il/Elle/On": "aura provenu(e)",
      "Nous": "aurons provenu(e)s",
      "Vous": "aurez provenu(e)s",
      "Ils/Elle": "auront provenu(e)s"
    },
    "Conditionnel Présent": {
      "Je": "proviendrais",
      "Tu": "proviendrais",
      "Il/Elle/On": "proviendrait",
      "Nous": "proviendrions",
      "Vous": "proviendriez",
      "Ils/Elle": "proviendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais provenu(e)",
      "Tu": "aurais provenu(e)",
      "Il/Elle/On": "aurait provenu(e)",
      "Nous": "aurions provenu(e)s",
      "Vous": "auriez provenu(e)s",
      "Ils/Elle": "auraient provenu(e)s"
    },
    "Subjonctif Présent": {
      "Je": "provienne",
      "Tu": "proviennes",
      "Il/Elle/On": "provienne",
      "Nous": "provenions",
      "Vous": "proveniez",
      "Ils/Elle": "proviennent"
    },
    "Subjonctif Passé": {
      "Je": "aie provenu(e)",
      "Tu": "aies provenu(e)",
      "Il/Elle/On": "ait provenu(e)",
      "Nous": "ayons provenu(e)s",
      "Vous": "ayez provenu(e)s",
      "Ils/Elle": "aient provenu(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse provenu(e)",
      "Tu": "eusses provenu(e)",
      "Il/Elle/On": "eût provenu(e)",
      "Nous": "eussions provenu(e)s",
      "Vous": "eussiez provenu(e)s",
      "Ils/Elle": "eussent provenu(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "provinss",
      "Tu": "provinsses",
      "Il/Elle/On": "provint",
      "Nous": "provinssions",
      "Vous": "provinssiez",
      "Ils/Elle": "provinssent"
    },
    "Impératif Présent": {
      "Tu": "provien",
      "Nous": "provenons",
      "Vous": "provenez"
    },
    "Impératif Passé": {
      "Tu": "aie provenu(e)",
      "Nous": "ayons provenu(e)s",
      "Vous": "ayez provenu(e)s"
    },
    "Infinitif Présent": "provenir",
    "Infinitif Passé": "avoir provenu(e)",
    "Participe Présent": "provenant",
    "Participe Passé": {
      "Masculin Singulier": "provenu",
      "Masculin Pluriel": "provenus",
      "Féminin Singulier": "provenue",
      "Féminin Pluriel": "provenues"
    },
    "Gérondif Présent": "en provenant",
    "Gérondif Passé": {
      "Masculin Singulier": "en ayant provenu",
      "Masculin Pluriel": "en ayant provenus",
      "Féminin Singulier": "en ayant provenue",
      "Féminin Pluriel": "en ayant provenues"
    }
},
"redevenir": {
    "Présent": {
      "Je": "redeviens",
      "Tu": "redeviens",
      "Il/Elle/On": "redevient",
      "Nous": "redevenons",
      "Vous": "redevenez",
      "Ils/Elle": "redeviennent"
    },
    "Imparfait": {
      "Je": "redevenais",
      "Tu": "redevenais",
      "Il/Elle/On": "redevenait",
      "Nous": "redevenions",
      "Vous": "redeveniez",
      "Ils/Elle": "redevenaient"
    },
    "Passé Composé": {
      "Je": "suis redevenu(e)",
      "Tu": "es redevenu(e)",
      "Il/Elle/On": "est redevenu(e)",
      "Nous": "sommes redevenus(es)",
      "Vous": "êtes redevenus(es)",
      "Ils/Elle": "sont redevenus(es)"
    },
    "Futur": {
      "Je": "redeviendrai",
      "Tu": "redeviendras",
      "Il/Elle/On": "redeviendra",
      "Nous": "redeviendrons",
      "Vous": "redeviendrez",
      "Ils/Elle": "redeviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais redevenu(e)",
      "Tu": "étais redevenu(e)",
      "Il/Elle/On": "était redevenu(e)",
      "Nous": "étions redevenus(es)",
      "Vous": "étiez redevenus(es)",
      "Ils/Elle": "étaient redevenus(es)"
    },
    "Futur Simple": {
      "Je": "redeviendrai",
      "Tu": "redeviendras",
      "Il/Elle/On": "redeviendra",
      "Nous": "redeviendrons",
      "Vous": "redeviendrez",
      "Ils/Elle": "redeviendront"
    },
    "Futur Antérieur": {
      "Je": "serai redevenu(e)",
      "Tu": "seras redevenu(e)",
      "Il/Elle/On": "sera redevenu(e)",
      "Nous": "serons redevenus(es)",
      "Vous": "serez redevenus(es)",
      "Ils/Elle": "seront redevenus(es)"
    },
    "Conditionnel Présent": {
      "Je": "redeviendrais",
      "Tu": "redeviendrais",
      "Il/Elle/On": "redeviendrait",
      "Nous": "redeviendrions",
      "Vous": "redeviendriez",
      "Ils/Elle": "redeviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais redevenu(e)",
      "Tu": "serais redevenu(e)",
      "Il/Elle/On": "serait redevenu(e)",
      "Nous": "serions redevenus(es)",
      "Vous": "seriez redevenus(es)",
      "Ils/Elle": "seraient redevenus(es)"
    },
    "Subjonctif Présent": {
      "Je": "redevienne",
      "Tu": "redeviennes",
      "Il/Elle/On": "redevienne",
      "Nous": "redevenions",
      "Vous": "redeveniez",
      "Ils/Elle": "redeviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois redevenu(e)",
      "Tu": "sois redevenu(e)",
      "Il/Elle/On": "soit redevenu(e)",
      "Nous": "soyons redevenus(es)",
      "Vous": "soyez redevenus(es)",
      "Ils/Elle": "soient redevenus(es)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse redevenu(e)",
      "Tu": "fusses redevenu(e)",
      "Il/Elle/On": "fût redevenu(e)",
      "Nous": "fussions redevenus(es)",
      "Vous": "fussiez redevenus(es)",
      "Ils/Elle": "fussent redevenus(es)"
    },
    "Subjonctif Imparfait": {
      "Je": "redevinsse",
      "Tu": "redevinsses",
      "Il/Elle/On": "redevînt",
      "Nous": "redevinssions",
      "Vous": "redevinssiez",
      "Ils/Elle": "redevinssent"
    },
    "Impératif Présent": {
      "Tu": "redeviens",
      "Nous": "redevenons",
      "Vous": "redevenez"
    },
    "Impératif Passé": {
      "Tu": "sois redevenu(e)",
      "Nous": "soyons redevenus(es)",
      "Vous": "soyez redevenus(es)"
    },
    "Infinitif Présent": "redevenir",
    "Infinitif Passé": "être redevenu(e)",
    "Participe Présent": "redevenant",
    "Participe Passé": {
      "Masculin Singulier": "redevenu",
      "Masculin Pluriel": "redevenus",
      "Féminin Singulier": "redevenue",
      "Féminin Pluriel": "redevenues"
    },
    "Gérondif Présent": "en redevenant",
    "Gérondif Passé": {
      "Masculin Singulier": "en étant redevenu",
      "Masculin Pluriel": "en étant redevenus",
      "Féminin Singulier": "en étant redevenue",
      "Féminin Pluriel": "en étant redevenues"
    }
},
"ressouvenir": {
    "Présent": {
      "Je": "ressouviens",
      "Tu": "ressouviens",
      "Il/Elle/On": "ressouvient",
      "Nous": "ressouvenons",
      "Vous": "ressouvenez",
      "Ils/Elle": "ressouviennent"
    },
    "Imparfait": {
      "Je": "ressouvenais",
      "Tu": "ressouvenais",
      "Il/Elle/On": "ressouvenait",
      "Nous": "ressouvenions",
      "Vous": "ressouveniez",
      "Ils/Elle": "ressouvenaient"
    },
    "Passé Composé": {
      "Je": "ai ressouvenu",
      "Tu": "as ressouvenu",
      "Il/Elle/On": "a ressouvenu",
      "Nous": "avons ressouvenu",
      "Vous": "avez ressouvenu",
      "Ils/Elle": "ont ressouvenu"
    },
    "Futur": {
      "Je": "ressouviendrai",
      "Tu": "ressouviendras",
      "Il/Elle/On": "ressouviendra",
      "Nous": "ressouviendrons",
      "Vous": "ressouviendrez",
      "Ils/Elle": "ressouviendront"
    },
    "Plus-que-parfait": {
      "Je": "avais ressouvenu",
      "Tu": "avais ressouvenu",
      "Il/Elle/On": "avait ressouvenu",
      "Nous": "avions ressouvenu",
      "Vous": "aviez ressouvenu",
      "Ils/Elle": "avaient ressouvenu"
    },
    "Futur Simple": {
      "Je": "ressouviendrai",
      "Tu": "ressouviendras",
      "Il/Elle/On": "ressouviendra",
      "Nous": "ressouviendrons",
      "Vous": "ressouviendrez",
      "Ils/Elle": "ressouviendront"
    },
    "Futur Antérieur": {
      "Je": "aurai ressouvenu",
      "Tu": "auras ressouvenu",
      "Il/Elle/On": "aura ressouvenu",
      "Nous": "aurons ressouvenu",
      "Vous": "aurez ressouvenu",
      "Ils/Elle": "auront ressouvenu"
    },
    "Conditionnel Présent": {
      "Je": "ressouviendrais",
      "Tu": "ressouviendrais",
      "Il/Elle/On": "ressouviendrait",
      "Nous": "ressouviendrions",
      "Vous": "ressouviendriez",
      "Ils/Elle": "ressouviendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais ressouvenu",
      "Tu": "aurais ressouvenu",
      "Il/Elle/On": "aurait ressouvenu",
      "Nous": "aurions ressouvenu",
      "Vous": "auriez ressouvenu",
      "Ils/Elle": "auraient ressouvenu"
    },
    "Subjonctif Présent": {
      "Je": "ressouvienne",
      "Tu": "ressouviennes",
      "Il/Elle/On": "ressouvienne",
      "Nous": "ressouvenions",
      "Vous": "ressouveniez",
      "Ils/Elle": "ressouvient"
    },
    "Subjonctif Passé": {
      "Je": "aie ressouvenu",
      "Tu": "aies ressouvenu",
      "Il/Elle/On": "ait ressouvenu",
      "Nous": "ayons ressouvenu",
      "Vous": "ayez ressouvenu",
      "Ils/Elle": "aient ressouvenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse ressouvenu",
      "Tu": "eusses ressouvenu",
      "Il/Elle/On": "eût ressouvenu",
      "Nous": "eussions ressouvenu",
      "Vous": "eussiez ressouvenu",
      "Ils/Elle": "eussent ressouvenu"
    },
    "Subjonctif Imparfait": {
      "Je": "ressouvenisse",
      "Tu": "ressouvenisses",
      "Il/Elle/On": "ressouvenît",
      "Nous": "ressouvenissions",
      "Vous": "ressouvenissiez",
      "Ils/Elle": "ressouvenissent"
    },
    "Impératif Présent": {
      "Tu": "ressouviens",
      "Nous": "ressouvenons",
      "Vous": "ressouvenez"
    },
    "Impératif Passé": {
      "Tu": "aie ressouvenu",
      "Nous": "ayons ressouvenu",
      "Vous": "ayez ressouvenu"
    },
    "Infinitif Présent": "ressouvenir",
    "Infinitif Passé": "avoir ressouvenu",
    "Participe Présent": "ressouvenant",
    "Participe Passé": "ressouvenu",
    "Gérondif Présent": "en ressouvenant",
    "Gérondif Passé": "en ayant ressouvenu"
},
"revenir": {
    "Présent": {
      "Je": "reviens",
      "Tu": "reviens",
      "Il/Elle/On": "revient",
      "Nous": "revenons",
      "Vous": "revenez",
      "Ils/Elle": "reviennent"
    },
    "Imparfait": {
      "Je": "revenais",
      "Tu": "revenais",
      "Il/Elle/On": "revenait",
      "Nous": "revenions",
      "Vous": "reveniez",
      "Ils/Elle": "revenaient"
    },
    "Passé Composé": {
      "Je": "suis revenu",
      "Tu": "es revenu",
      "Il/Elle/On": "est revenu",
      "Nous": "sommes revenus",
      "Vous": "êtes revenus",
      "Ils/Elle": "sont revenus"
    },
    "Futur": {
      "Je": "reviendrai",
      "Tu": "reviendras",
      "Il/Elle/On": "reviendra",
      "Nous": "reviendrons",
      "Vous": "reviendrez",
      "Ils/Elle": "reviendront"
    },
    "Plus-que-parfait": {
      "Je": "étais revenu",
      "Tu": "étais revenu",
      "Il/Elle/On": "était revenu",
      "Nous": "étions revenus",
      "Vous": "étiez revenus",
      "Ils/Elle": "étaient revenus"
    },
    "Futur Simple": {
      "Je": "reviendrai",
      "Tu": "reviendras",
      "Il/Elle/On": "reviendra",
      "Nous": "reviendrons",
      "Vous": "reviendrez",
      "Ils/Elle": "reviendront"
    },
    "Futur Antérieur": {
      "Je": "serai revenu",
      "Tu": "seras revenu",
      "Il/Elle/On": "sera revenu",
      "Nous": "serons revenus",
      "Vous": "serez revenus",
      "Ils/Elle": "seront revenus"
    },
    "Conditionnel Présent": {
      "Je": "reviendrais",
      "Tu": "reviendrais",
      "Il/Elle/On": "reviendrait",
      "Nous": "reviendrions",
      "Vous": "reviendriez",
      "Ils/Elle": "reviendraient"
    },
    "Conditionnel Passé": {
      "Je": "serais revenu",
      "Tu": "serais revenu",
      "Il/Elle/On": "serait revenu",
      "Nous": "serions revenus",
      "Vous": "seriez revenus",
      "Ils/Elle": "seraient revenus"
    },
    "Subjonctif Présent": {
      "Je": "revienne",
      "Tu": "reviennes",
      "Il/Elle/On": "revienne",
      "Nous": "revenions",
      "Vous": "reveniez",
      "Ils/Elle": "reviennent"
    },
    "Subjonctif Passé": {
      "Je": "sois revenu",
      "Tu": "sois revenu",
      "Il/Elle/On": "soit revenu",
      "Nous": "soyons revenus",
      "Vous": "soyez revenus",
      "Ils/Elle": "soient revenus"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse revenu",
      "Tu": "fusses revenu",
      "Il/Elle/On": "fût revenu",
      "Nous": "fussions revenus",
      "Vous": "fussiez revenus",
      "Ils/Elle": "fussent revenus"
    },
    "Subjonctif Imparfait": {
      "Je": "revinsse",
      "Tu": "revinsses",
      "Il/Elle/On": "revînt",
      "Nous": "revinssions",
      "Vous": "revinssiez",
      "Ils/Elle": "revinssent"
    },
    "Impératif Présent": {
      "Tu": "reviens",
      "Nous": "revenons",
      "Vous": "revenez"
    },
    "Impératif Passé": {
      "Tu": "sois revenu",
      "Nous": "soyons revenus",
      "Vous": "soyez revenus"
    },
    "Infinitif Présent": "revenir",
    "Infinitif Passé": "être revenu",
    "Participe Présent": "revenant",
    "Participe Passé": "revenu",
    "Gérondif Présent": "en revenant",
    "Gérondif Passé": "en étant revenu"
},
"souvenir": {
    "Présent": {
      "Je": "me souviens",
      "Tu": "te souviens",
      "Il/Elle/On": "se souvient",
      "Nous": "nous souvenons",
      "Vous": "vous souvenez",
      "Ils/Elle": "se souviennent"
    },
    "Imparfait": {
      "Je": "me souvenais",
      "Tu": "te souvenais",
      "Il/Elle/On": "se souvenait",
      "Nous": "nous souvenions",
      "Vous": "vous souveniez",
      "Ils/Elle": "se souvenaient"
    },
    "Passé Composé": {
      "Je": "me suis souvenu(e)",
      "Tu": "t'es souvenu(e)",
      "Il/Elle/On": "s'est souvenu(e)",
      "Nous": "nous sommes souvenus(e)",
      "Vous": "vous êtes souvenus(e)",
      "Ils/Elle": "se sont souvenus(e)"
    },
    "Futur": {
      "Je": "me souviendrai",
      "Tu": "te souviendras",
      "Il/Elle/On": "se souviendra",
      "Nous": "nous souviendrons",
      "Vous": "vous souviendrez",
      "Ils/Elle": "se souviendront"
    },
    "Plus-que-parfait": {
      "Je": "m'étais souvenu(e)",
      "Tu": "t'étais souvenu(e)",
      "Il/Elle/On": "s'était souvenu(e)",
      "Nous": "nous étions souvenus(e)",
      "Vous": "vous étiez souvenus(e)",
      "Ils/Elle": "s'étaient souvenus(e)"
    },
    "Futur Simple": {
      "Je": "me souviendrai",
      "Tu": "te souviendras",
      "Il/Elle/On": "se souviendra",
      "Nous": "nous souviendrons",
      "Vous": "vous souviendrez",
      "Ils/Elle": "se souviendront"
    },
    "Futur Antérieur": {
      "Je": "me serai souvenu(e)",
      "Tu": "te seras souvenu(e)",
      "Il/Elle/On": "se sera souvenu(e)",
      "Nous": "nous serons souvenus(e)",
      "Vous": "vous serez souvenus(e)",
      "Ils/Elle": "se seront souvenus(e)"
    },
    "Conditionnel Présent": {
      "Je": "me souviendrais",
      "Tu": "te souviendrais",
      "Il/Elle/On": "se souviendrait",
      "Nous": "nous souviendrions",
      "Vous": "vous souviendriez",
      "Ils/Elle": "se souviendraient"
    },
    "Conditionnel Passé": {
      "Je": "me serais souvenu(e)",
      "Tu": "te serais souvenu(e)",
      "Il/Elle/On": "se serait souvenu(e)",
      "Nous": "nous serions souvenus(e)",
      "Vous": "vous seriez souvenus(e)",
      "Ils/Elle": "se seraient souvenus(e)"
    },
    "Subjonctif Présent": {
      "Je": "me souvienne",
      "Tu": "te souviennes",
      "Il/Elle/On": "se souvienne",
      "Nous": "nous souvenions",
      "Vous": "vous souveniez",
      "Ils/Elle": "se souviennent"
    },
    "Subjonctif Passé": {
      "Je": "me sois souvenu(e)",
      "Tu": "te sois souvenu(e)",
      "Il/Elle/On": "se soit souvenu(e)",
      "Nous": "nous soyons souvenus(e)",
      "Vous": "vous soyez souvenus(e)",
      "Ils/Elle": "se soient souvenus(e)"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "me fusse souvenu(e)",
      "Tu": "te fusses souvenu(e)",
      "Il/Elle/On": "se fût souvenu(e)",
      "Nous": "nous fussions souvenus(e)",
      "Vous": "vous fussiez souvenus(e)",
      "Ils/Elle": "se fussent souvenus(e)"
    },
    "Subjonctif Imparfait": {
      "Je": "me souvinsse",
      "Tu": "te souvinsses",
      "Il/Elle/On": "se souvînt",
      "Nous": "nous souvinssions",
      "Vous": "vous souvinssiez",
      "Ils/Elle": "se souvinssent"
    },
    "Impératif Présent": {
      "Tu": "souviens-toi",
      "Nous": "souvenons-nous",
      "Vous": "souvenez-vous"
    },
    "Impératif Passé": {
      "Tu": "sois souvenu(e)",
      "Nous": "soyons souvenus(e)",
      "Vous": "soyez souvenus(e)"
    },
    "Infinitif Présent": "se souvenir",
    "Infinitif Passé": "s'être souvenu(e)",
    "Participe Présent": "se souvenant",
    "Participe Passé": "souvenu(e)",
    "Gérondif Présent": "en se souvenant",
    "Gérondif Passé": "en s'étant souvenu(e)"
  },
  "subvenir": {
    "Présent": {
      "Je": "subviens",
      "Tu": "subviens",
      "Il/Elle/On": "subvient",
      "Nous": "subvenons",
      "Vous": "subvenez",
      "Ils/Elle": "subviennent"
    },
    "Imparfait": {
      "Je": "subvenais",
      "Tu": "subvenais",
      "Il/Elle/On": "subvenait",
      "Nous": "subvenions",
      "Vous": "subveniez",
      "Ils/Elle": "subvenaient"
    },
    "Passé Composé": {
      "Je": "ai subvenu",
      "Tu": "as subvenu",
      "Il/Elle/On": "a subvenu",
      "Nous": "avons subvenu",
      "Vous": "avez subvenu",
      "Ils/Elle": "ont subvenu"
    },
    "Futur": {
      "Je": "subviendrai",
      "Tu": "subviendras",
      "Il/Elle/On": "subviendra",
      "Nous": "subviendrons",
      "Vous": "subviendrez",
      "Ils/Elle": "subviendront"
    },
    "Plus-que-parfait": {
      "Je": "avais subvenu",
      "Tu": "avais subvenu",
      "Il/Elle/On": "avait subvenu",
      "Nous": "avions subvenu",
      "Vous": "aviez subvenu",
      "Ils/Elle": "avaient subvenu"
    },
    "Futur Simple": {
      "Je": "subviendrai",
      "Tu": "subviendras",
      "Il/Elle/On": "subviendra",
      "Nous": "subviendrons",
      "Vous": "subviendrez",
      "Ils/Elle": "subviendront"
    },
    "Futur Antérieur": {
      "Je": "aurai subvenu",
      "Tu": "auras subvenu",
      "Il/Elle/On": "aura subvenu",
      "Nous": "aurons subvenu",
      "Vous": "aurez subvenu",
      "Ils/Elle": "auront subvenu"
    },
    "Conditionnel Présent": {
      "Je": "subviendrais",
      "Tu": "subviendrais",
      "Il/Elle/On": "subviendrait",
      "Nous": "subviendrions",
      "Vous": "subviendriez",
      "Ils/Elle": "subviendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais subvenu",
      "Tu": "aurais subvenu",
      "Il/Elle/On": "aurait subvenu",
      "Nous": "aurions subvenu",
      "Vous": "auriez subvenu",
      "Ils/Elle": "auraient subvenu"
    },
    "Subjonctif Présent": {
      "Je": "subvienne",
      "Tu": "subviennes",
      "Il/Elle/On": "subvienne",
      "Nous": "subvenions",
      "Vous": "subveniez",
      "Ils/Elle": "subviennent"
    },
    "Subjonctif Passé": {
      "Je": "aie subvenu",
      "Tu": "aies subvenu",
      "Il/Elle/On": "ait subvenu",
      "Nous": "ayons subvenu",
      "Vous": "ayez subvenu",
      "Ils/Elle": "aient subvenu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse subvenu",
      "Tu": "eusses subvenu",
      "Il/Elle/On": "eût subvenu",
      "Nous": "eussions subvenu",
      "Vous": "eussiez subvenu",
      "Ils/Elle": "eussent subvenu"
    },
    "Subjonctif Imparfait": {
      "Je": "subvinssse",
      "Tu": "subvinsses",
      "Il/Elle/On": "subvînt",
      "Nous": "subvinssions",
      "Vous": "subvinssiez",
      "Ils/Elle": "subvinssent"
    },
    "Impératif Présent": {
      "Tu": "subviens",
      "Nous": "subvenons",
      "Vous": "subvenez"
    },
    "Impératif Passé": {
      "Tu": "aie subvenu",
      "Nous": "ayons subvenu",
      "Vous": "ayez subvenu"
    },
    "Infinitif Présent": "subvenir",
    "Infinitif Passé": "avoir subvenu",
    "Participe Présent": "subvenant",
    "Participe Passé": "subvenu",
    "Gérondif Présent": "en subvenant",
    "Gérondif Passé": "en ayant subvenu"
  },
  "survenir": {
    "Présent": {
      "Je": "surviens",
      "Tu": "surviens",
      "Il/Elle/On": "survient",
      "Nous": "survenons",
      "Vous": "survenez",
      "Ils/Elle": "surviennent"
    },
    "Imparfait": {
      "Je": "survenais",
      "Tu": "survenais",
      "Il/Elle/On": "survenait",
      "Nous": "survenions",
      "Vous": "surveniez",
      "Ils/Elle": "survenaient"
    },
    "Passé Composé": {
      "Je": "ai survécu",
      "Tu": "as survécu",
      "Il/Elle/On": "a survécu",
      "Nous": "avons survécu",
      "Vous": "avez survécu",
      "Ils/Elle": "ont survécu"
    },
    "Futur": {
      "Je": "surviendrai",
      "Tu": "surviendras",
      "Il/Elle/On": "surviendra",
      "Nous": "surviendrons",
      "Vous": "surviendrez",
      "Ils/Elle": "surviendront"
    },
    "Plus-que-parfait": {
      "Je": "avais survécu",
      "Tu": "avais survécu",
      "Il/Elle/On": "avait survécu",
      "Nous": "avions survécu",
      "Vous": "aviez survécu",
      "Ils/Elle": "avaient survécu"
    },
    "Futur Simple": {
      "Je": "surviendrai",
      "Tu": "surviendras",
      "Il/Elle/On": "surviendra",
      "Nous": "surviendrons",
      "Vous": "surviendrez",
      "Ils/Elle": "surviendront"
    },
    "Futur Antérieur": {
      "Je": "aurai survécu",
      "Tu": "auras survécu",
      "Il/Elle/On": "aura survécu",
      "Nous": "aurons survécu",
      "Vous": "aurez survécu",
      "Ils/Elle": "auront survécu"
    },
    "Conditionnel Présent": {
      "Je": "surviendrais",
      "Tu": "surviendrais",
      "Il/Elle/On": "surviendrait",
      "Nous": "surviendrions",
      "Vous": "surviendriez",
      "Ils/Elle": "surviendraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais survécu",
      "Tu": "aurais survécu",
      "Il/Elle/On": "aurait survécu",
      "Nous": "aurions survécu",
      "Vous": "auriez survécu",
      "Ils/Elle": "auraient survécu"
    },
    "Subjonctif Présent": {
      "Je": "survienne",
      "Tu": "surviennes",
      "Il/Elle/On": "survienne",
      "Nous": "survenions",
      "Vous": "surveniez",
      "Ils/Elle": "surviennent"
    },
    "Subjonctif Passé": {
      "Je": "aie survécu",
      "Tu": "aies survécu",
      "Il/Elle/On": "ait survécu",
      "Nous": "ayons survécu",
      "Vous": "ayez survécu",
      "Ils/Elle": "aient survécu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse survécu",
      "Tu": "eusses survécu",
      "Il/Elle/On": "eût survécu",
      "Nous": "eussions survécu",
      "Vous": "eussiez survécu",
      "Ils/Elle": "eussent survécu"
    },
    "Subjonctif Imparfait": {
      "Je": "survinsse",
      "Tu": "survinsses",
      "Il/Elle/On": "survînt",
      "Nous": "survinssions",
      "Vous": "survinssiez",
      "Ils/Elle": "survinssent"
    },
    "Impératif Présent": {
      "Tu": "surviens",
      "Nous": "survenons",
      "Vous": "survenez"
    },
    "Impératif Passé": {
      "Tu": "aie survécu",
      "Nous": "ayons survécu",
      "Vous": "ayez survécu"
    },
    "Infinitif Présent": "survenir",
    "Infinitif Passé": "avoir survécu",
    "Participe Présent": "survenant",
    "Participe Passé": "survécu",
    "Gérondif Présent": "en survenant",
    "Gérondif Passé": "en ayant survécu"
  },
  "acquérir": {
    "Présent": {
      "Je": "acquiers",
      "Tu": "acquiers",
      "Il/Elle/On": "acquiert",
      "Nous": "acquérons",
      "Vous": "acquérez",
      "Ils/Elle": "acquièrent"
    },
    "Imparfait": {
      "Je": "acquérais",
      "Tu": "acquérais",
      "Il/Elle/On": "acquérait",
      "Nous": "acquérions",
      "Vous": "acquériez",
      "Ils/Elle": "acquéraient"
    },
    "Passé Composé": {
      "Je": "ai acquis",
      "Tu": "as acquis",
      "Il/Elle/On": "a acquis",
      "Nous": "avons acquis",
      "Vous": "avez acquis",
      "Ils/Elle": "ont acquis"
    },
    "Futur": {
      "Je": "acquerrai",
      "Tu": "acquerras",
      "Il/Elle/On": "acquerra",
      "Nous": "acquerrons",
      "Vous": "acquerr ez",
      "Ils/Elle": "acquerront"
    },
    "Plus-que-parfait": {
      "Je": "avais acquis",
      "Tu": "avais acquis",
      "Il/Elle/On": "avait acquis",
      "Nous": "avions acquis",
      "Vous": "aviez acquis",
      "Ils/Elle": "avaient acquis"
    },
    "Futur Simple": {
      "Je": "acquerrai",
      "Tu": "acquerras",
      "Il/Elle/On": "acquerra",
      "Nous": "acquerrons",
      "Vous": "acquerr ez",
      "Ils/Elle": "acquerront"
    },
    "Futur Antérieur": {
      "Je": "aurai acquis",
      "Tu": "auras acquis",
      "Il/Elle/On": "aura acquis",
      "Nous": "aurons acquis",
      "Vous": "aurez acquis",
      "Ils/Elle": "auront acquis"
    },
    "Conditionnel Présent": {
      "Je": "acquerrais",
      "Tu": "acquerrais",
      "Il/Elle/On": "acquerrait",
      "Nous": "acquerrions",
      "Vous": "acquerriez",
      "Ils/Elle": "acquerraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais acquis",
      "Tu": "aurais acquis",
      "Il/Elle/On": "aurait acquis",
      "Nous": "aurions acquis",
      "Vous": "auriez acquis",
      "Ils/Elle": "auraient acquis"
    },
    "Subjonctif Présent": {
      "Je": "acquière",
      "Tu": "acquières",
      "Il/Elle/On": "acquière",
      "Nous": "acquérions",
      "Vous": "acquériez",
      "Ils/Elle": "acquièrent"
    },
    "Subjonctif Passé": {
      "Je": "aie acquis",
      "Tu": "aies acquis",
      "Il/Elle/On": "ait acquis",
      "Nous": "ayons acquis",
      "Vous": "ayez acquis",
      "Ils/Elle": "aient acquis"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse acquis",
      "Tu": "eusses acquis",
      "Il/Elle/On": "eût acquis",
      "Nous": "eussions acquis",
      "Vous": "eussiez acquis",
      "Ils/Elle": "eussent acquis"
    },
    "Subjonctif Imparfait": {
      "Je": "acquîsse",
      "Tu": "acquisses",
      "Il/Elle/On": "acquît",
      "Nous": "acquissions",
      "Vous": "acquissiez",
      "Ils/Elle": "acquissent"
    },
    "Impératif Présent": {
      "Tu": "acquiers",
      "Nous": "acquérons",
      "Vous": "acquérez"
    },
    "Impératif Passé": {
      "Tu": "aie acquis",
      "Nous": "ayons acquis",
      "Vous": "ayez acquis"
    },
    "Infinitif Présent": "acquérir",
    "Infinitif Passé": "avoir acquis",
    "Participe Présent": "acquérant",
    "Participe Passé": "acquis",
    "Gérondif Présent": "en acquérant",
    "Gérondif Passé": "en ayant acquis"
  },
  "enquérir": {
    "Présent": {
      "Je": "m'enquiers",
      "Tu": "t'enquiers",
      "Il/Elle/On": "s'enquiert",
      "Nous": "nous enquérons",
      "Vous": "vous enquérez",
      "Ils/Elle": "s'enquièrent"
    },
    "Imparfait": {
      "Je": "m'enquérais",
      "Tu": "t'enquérais",
      "Il/Elle/On": "s'enquérait",
      "Nous": "nous enquérions",
      "Vous": "vous enquériez",
      "Ils/Elle": "s'enquéraient"
    },
    "Passé Composé": {
      "Je": "me suis enquéri(e)",
      "Tu": "t'es enquéri(e)",
      "Il/Elle/On": "s'est enquéri(e)",
      "Nous": "nous sommes enquéri(e)s",
      "Vous": "vous êtes enquéri(e)s",
      "Ils/Elle": "se sont enquéri(e)s"
    },
    "Futur": {
      "Je": "m'enquerrai",
      "Tu": "t'enquerras",
      "Il/Elle/On": "s'enquerra",
      "Nous": "nous enquerrons",
      "Vous": "vous enquerr ez",
      "Ils/Elle": "s'enquerront"
    },
    "Plus-que-parfait": {
      "Je": "m'étais enquéri(e)",
      "Tu": "t'étais enquéri(e)",
      "Il/Elle/On": "s'était enquéri(e)",
      "Nous": "nous étions enquéri(e)s",
      "Vous": "vous étiez enquéri(e)s",
      "Ils/Elle": "s'étaient enquéri(e)s"
    },
    "Futur Simple": {
      "Je": "m'enquerrai",
      "Tu": "t'enquerras",
      "Il/Elle/On": "s'enquerra",
      "Nous": "nous enquerrons",
      "Vous": "vous enquerr ez",
      "Ils/Elle": "s'enquerront"
    },
    "Futur Antérieur": {
      "Je": "me serai enquéri(e)",
      "Tu": "te seras enquéri(e)",
      "Il/Elle/On": "se sera enquéri(e)",
      "Nous": "nous serons enquéri(e)s",
      "Vous": "vous serez enquéri(e)s",
      "Ils/Elle": "se seront enquéri(e)s"
    },
    "Conditionnel Présent": {
      "Je": "m'enquerrais",
      "Tu": "t'enquerrais",
      "Il/Elle/On": "s'enquerrait",
      "Nous": "nous enquerrions",
      "Vous": "vous enquerr ez",
      "Ils/Elle": "s'enquerraient"
    },
    "Conditionnel Passé": {
      "Je": "me serais enquéri(e)",
      "Tu": "te serais enquéri(e)",
      "Il/Elle/On": "se serait enquéri(e)",
      "Nous": "nous serions enquéri(e)s",
      "Vous": "vous seriez enquéri(e)s",
      "Ils/Elle": "se seraient enquéri(e)s"
    },
    "Subjonctif Présent": {
      "Je": "m'enquière",
      "Tu": "t'enquières",
      "Il/Elle/On": "s'enquière",
      "Nous": "nous enquérions",
      "Vous": "vous enquériez",
      "Ils/Elle": "s'enquièrent"
    },
    "Subjonctif Passé": {
      "Je": "me sois enquéri(e)",
      "Tu": "te sois enquéri(e)",
      "Il/Elle/On": "se soit enquéri(e)",
      "Nous": "nous soyons enquéri(e)s",
      "Vous": "vous soyez enquéri(e)s",
      "Ils/Elle": "se soient enquéri(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "me fusse enquéri(e)",
      "Tu": "te fusses enquéri(e)",
      "Il/Elle/On": "se fût enquéri(e)",
      "Nous": "nous fussions enquéri(e)s",
      "Vous": "vous fussiez enquéri(e)s",
      "Ils/Elle": "se fussent enquéri(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "m'enquisse",
      "Tu": "t'enquisses",
      "Il/Elle/On": "s'enquît",
      "Nous": "nous enquissions",
      "Vous": "vous enquissiez",
      "Ils/Elle": "s'enquissent"
    },
    "Impératif Présent": {
      "Tu": "m'enquiers",
      "Nous": "nous enquérons",
      "Vous": "vous enquérez"
    },
    "Impératif Passé": {
      "Tu": "me sois enquéri(e)",
      "Nous": "nous soyons enquéri(e)s",
      "Vous": "vous soyez enquéri(e)s"
    },
    "Infinitif Présent": "s'enquérir",
    "Infinitif Passé": "s'être enquéri(e)",
    "Participe Présent": "s'enquérant",
    "Participe Passé": "enquéri(e)",
    "Gérondif Présent": "en s'enquérant",
    "Gérondif Passé": "en s'étant enquéri(e)"
  },
  "quérir": {
    "Présent": {
      "Je": "quiers",
      "Tu": "quiers",
      "Il/Elle/On": "quiert",
      "Nous": "quérons",
      "Vous": "quérez",
      "Ils/Elle": "quièrent"
    },
    "Imparfait": {
      "Je": "quérais",
      "Tu": "quérais",
      "Il/Elle/On": "quérait",
      "Nous": "quérions",
      "Vous": "quériez",
      "Ils/Elle": "quéraient"
    },
    "Passé Composé": {
      "Je": "ai quéri",
      "Tu": "as quéri",
      "Il/Elle/On": "a quéri",
      "Nous": "avons quéri",
      "Vous": "avez quéri",
      "Ils/Elle": "ont quéri"
    },
    "Futur": {
      "Je": "quérirai",
      "Tu": "quériras",
      "Il/Elle/On": "quérira",
      "Nous": "quérirons",
      "Vous": "quérirez",
      "Ils/Elle": "quériront"
    },
    "Plus-que-parfait": {
      "Je": "avais quéri",
      "Tu": "avais quéri",
      "Il/Elle/On": "avait quéri",
      "Nous": "avions quéri",
      "Vous": "aviez quéri",
      "Ils/Elle": "avaient quéri"
    },
    "Futur Simple": {
      "Je": "quérirai",
      "Tu": "quériras",
      "Il/Elle/On": "quérira",
      "Nous": "quérirons",
      "Vous": "quérirez",
      "Ils/Elle": "quériront"
    },
    "Futur Antérieur": {
      "Je": "aurai quéri",
      "Tu": "auras quéri",
      "Il/Elle/On": "aura quéri",
      "Nous": "aurons quéri",
      "Vous": "aurez quéri",
      "Ils/Elle": "auront quéri"
    },
    "Conditionnel Présent": {
      "Je": "quérirais",
      "Tu": "quérirais",
      "Il/Elle/On": "quérirait",
      "Nous": "quéririons",
      "Vous": "quéririez",
      "Ils/Elle": "quériraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais quéri",
      "Tu": "aurais quéri",
      "Il/Elle/On": "aurait quéri",
      "Nous": "aurions quéri",
      "Vous": "auriez quéri",
      "Ils/Elle": "auraient quéri"
    },
    "Subjonctif Présent": {
      "Je": "quière",
      "Tu": "quières",
      "Il/Elle/On": "quière",
      "Nous": "quiérions",
      "Vous": "quiériez",
      "Ils/Elle": "quièrent"
    },
    "Subjonctif Passé": {
      "Je": "aie quéri",
      "Tu": "aies quéri",
      "Il/Elle/On": "ait quéri",
      "Nous": "ayons quéri",
      "Vous": "ayez quéri",
      "Ils/Elle": "aient quéri"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse quéri",
      "Tu": "eusses quéri",
      "Il/Elle/On": "eût quéri",
      "Nous": "eussions quéri",
      "Vous": "eussiez quéri",
      "Ils/Elle": "eussent quéri"
    },
    "Subjonctif Imparfait": {
      "Je": "quérusse",
      "Tu": "quérusses",
      "Il/Elle/On": "quérût",
      "Nous": "quérussions",
      "Vous": "quérussiez",
      "Ils/Elle": "quérussent"
    },
    "Impératif Présent": {
      "Tu": "quiers",
      "Nous": "quérons",
      "Vous": "quérez"
    },
    "Impératif Passé": {
      "Tu": "aie quéri",
      "Nous": "ayons quéri",
      "Vous": "ayez quéri"
    },
    "Infinitif Présent": "quérir",
    "Infinitif Passé": "avoir quéri",
    "Participe Présent": "quére",
    "Participe Passé": "quéri",
    "Gérondif Présent": "en quére",
    "Gérondif Passé": "en ayant quéri"
  },
  "reconquérir": {
    "Présent": {
      "Je": "reconquiers",
      "Tu": "reconquiers",
      "Il/Elle/On": "reconquiert",
      "Nous": "reconquérons",
      "Vous": "reconquérez",
      "Ils/Elle": "reconquièrent"
    },
    "Imparfait": {
      "Je": "reconquérais",
      "Tu": "reconquérais",
      "Il/Elle/On": "reconquérait",
      "Nous": "reconquérions",
      "Vous": "reconquériez",
      "Ils/Elle": "reconquéraient"
    },
    "Passé Composé": {
      "Je": "ai reconquis",
      "Tu": "as reconquis",
      "Il/Elle/On": "a reconquis",
      "Nous": "avons reconquis",
      "Vous": "avez reconquis",
      "Ils/Elle": "ont reconquis"
    },
    "Futur": {
      "Je": "reconquerrai",
      "Tu": "reconquerras",
      "Il/Elle/On": "reconquerra",
      "Nous": "reconquerrons",
      "Vous": "reconquerrez",
      "Ils/Elle": "reconquerront"
    },
    "Plus-que-parfait": {
      "Je": "avais reconquis",
      "Tu": "avais reconquis",
      "Il/Elle/On": "avait reconquis",
      "Nous": "avions reconquis",
      "Vous": "aviez reconquis",
      "Ils/Elle": "avaient reconquis"
    },
    "Futur Simple": {
      "Je": "reconquerrai",
      "Tu": "reconquerras",
      "Il/Elle/On": "reconquerra",
      "Nous": "reconquerrons",
      "Vous": "reconquerrez",
      "Ils/Elle": "reconquerront"
    },
    "Futur Antérieur": {
      "Je": "aurai reconquis",
      "Tu": "auras reconquis",
      "Il/Elle/On": "aura reconquis",
      "Nous": "aurons reconquis",
      "Vous": "aurez reconquis",
      "Ils/Elle": "auront reconquis"
    },
    "Conditionnel Présent": {
      "Je": "reconquerrais",
      "Tu": "reconquerrais",
      "Il/Elle/On": "reconquerrait",
      "Nous": "reconquerions",
      "Vous": "reconqueriez",
      "Ils/Elle": "reconquerraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais reconquis",
      "Tu": "aurais reconquis",
      "Il/Elle/On": "aurait reconquis",
      "Nous": "aurions reconquis",
      "Vous": "auriez reconquis",
      "Ils/Elle": "auraient reconquis"
    },
    "Subjonctif Présent": {
      "Je": "reconquière",
      "Tu": "reconquières",
      "Il/Elle/On": "reconquière",
      "Nous": "reconquérions",
      "Vous": "reconquériez",
      "Ils/Elle": "reconquièrent"
    },
    "Subjonctif Passé": {
      "Je": "aie reconquis",
      "Tu": "aies reconquis",
      "Il/Elle/On": "ait reconquis",
      "Nous": "ayons reconquis",
      "Vous": "ayez reconquis",
      "Ils/Elle": "aient reconquis"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse reconquis",
      "Tu": "eusses reconquis",
      "Il/Elle/On": "eût reconquis",
      "Nous": "eussions reconquis",
      "Vous": "eussiez reconquis",
      "Ils/Elle": "eussent reconquis"
    },
    "Subjonctif Imparfait": {
      "Je": "reconquisse",
      "Tu": "reconquisses",
      "Il/Elle/On": "reconquît",
      "Nous": "reconquissions",
      "Vous": "reconquissiez",
      "Ils/Elle": "reconquissent"
    },
    "Impératif Présent": {
      "Tu": "reconquiers",
      "Nous": "reconquérons",
      "Vous": "reconquérez"
    },
    "Impératif Passé": {
      "Tu": "aie reconquis",
      "Nous": "ayons reconquis",
      "Vous": "ayez reconquis"
    },
    "Infinitif Présent": "reconquérir",
    "Infinitif Passé": "avoir reconquis",
    "Participe Présent": "reconquérant",
    "Participe Passé": "reconquis",
    "Gérondif Présent": "en reconquérant",
    "Gérondif Passé": "en ayant reconquis"
},
"requérir": {
    "Présent": {
      "Je": "requiers",
      "Tu": "requiers",
      "Il/Elle/On": "requiert",
      "Nous": "requérons",
      "Vous": "requérez",
      "Ils/Elle": "requièrent"
    },
    "Imparfait": {
      "Je": "requérais",
      "Tu": "requérais",
      "Il/Elle/On": "requérait",
      "Nous": "requérions",
      "Vous": "requériez",
      "Ils/Elle": "requéraient"
    },
    "Passé Composé": {
      "Je": "ai requis",
      "Tu": "as requis",
      "Il/Elle/On": "a requis",
      "Nous": "avons requis",
      "Vous": "avez requis",
      "Ils/Elle": "ont requis"
    },
    "Futur": {
      "Je": "requerrai",
      "Tu": "requerras",
      "Il/Elle/On": "requerra",
      "Nous": "requerrons",
      "Vous": "requerrez",
      "Ils/Elle": "requerront"
    },
    "Plus-que-parfait": {
      "Je": "avais requis",
      "Tu": "avais requis",
      "Il/Elle/On": "avait requis",
      "Nous": "avions requis",
      "Vous": "aviez requis",
      "Ils/Elle": "avaient requis"
    },
    "Futur Simple": {
      "Je": "requerrai",
      "Tu": "requerras",
      "Il/Elle/On": "requerra",
      "Nous": "requerrons",
      "Vous": "requerrez",
      "Ils/Elle": "requerront"
    },
    "Futur Antérieur": {
      "Je": "aurai requis",
      "Tu": "auras requis",
      "Il/Elle/On": "aura requis",
      "Nous": "aurons requis",
      "Vous": "aurez requis",
      "Ils/Elle": "auront requis"
    },
    "Conditionnel Présent": {
      "Je": "requerrais",
      "Tu": "requerrais",
      "Il/Elle/On": "requerrait",
      "Nous": "requerrions",
      "Vous": "requérriez",
      "Ils/Elle": "requerraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais requis",
      "Tu": "aurais requis",
      "Il/Elle/On": "aurait requis",
      "Nous": "aurions requis",
      "Vous": "auriez requis",
      "Ils/Elle": "auraient requis"
    },
    "Subjonctif Présent": {
      "Je": "requière",
      "Tu": "requières",
      "Il/Elle/On": "requière",
      "Nous": "requérions",
      "Vous": "requériez",
      "Ils/Elle": "requièrent"
    },
    "Subjonctif Passé": {
      "Je": "aie requis",
      "Tu": "aies requis",
      "Il/Elle/On": "ait requis",
      "Nous": "ayons requis",
      "Vous": "ayez requis",
      "Ils/Elle": "aient requis"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse requis",
      "Tu": "eusses requis",
      "Il/Elle/On": "eût requis",
      "Nous": "eussions requis",
      "Vous": "eussiez requis",
      "Ils/Elle": "eussent requis"
    },
    "Subjonctif Imparfait": {
      "Je": "requisse",
      "Tu": "requisses",
      "Il/Elle/On": "requît",
      "Nous": "requissions",
      "Vous": "requissiez",
      "Ils/Elle": "requissent"
    },
    "Impératif Présent": {
      "Tu": "requiers",
      "Nous": "requérons",
      "Vous": "requérez"
    },
    "Impératif Passé": {
      "Tu": "aie requis",
      "Nous": "ayons requis",
      "Vous": "ayez requis"
    },
    "Infinitif Présent": "requérir",
    "Infinitif Passé": "avoir requis",
    "Participe Présent": "requérant",
    "Participe Passé": "requis",
    "Gérondif Présent": "en requérant",
    "Gérondif Passé": "en ayant requis"
},
"sentir": {
    "Présent": {
      "Je": "sens",
      "Tu": "sens",
      "Il/Elle/On": "sent",
      "Nous": "sentons",
      "Vous": "sentez",
      "Ils/Elle": "sentent"
    },
    "Imparfait": {
      "Je": "sentais",
      "Tu": "sentais",
      "Il/Elle/On": "sentait",
      "Nous": "sentions",
      "Vous": "sentiez",
      "Ils/Elle": "sentaient"
    },
    "Passé Composé": {
      "Je": "ai senti",
      "Tu": "as senti",
      "Il/Elle/On": "a senti",
      "Nous": "avons senti",
      "Vous": "avez senti",
      "Ils/Elle": "ont senti"
    },
    "Futur": {
      "Je": "sentirai",
      "Tu": "sentiras",
      "Il/Elle/On": "sentira",
      "Nous": "sentirons",
      "Vous": "sentirez",
      "Ils/Elle": "sentiront"
    },
    "Plus-que-parfait": {
      "Je": "avais senti",
      "Tu": "avais senti",
      "Il/Elle/On": "avait senti",
      "Nous": "avions senti",
      "Vous": "aviez senti",
      "Ils/Elle": "avaient senti"
    },
    "Futur Simple": {
      "Je": "sentirai",
      "Tu": "sentiras",
      "Il/Elle/On": "sentira",
      "Nous": "sentirons",
      "Vous": "sentirez",
      "Ils/Elle": "sentiront"
    },
    "Futur Antérieur": {
      "Je": "aurai senti",
      "Tu": "auras senti",
      "Il/Elle/On": "aura senti",
      "Nous": "aurons senti",
      "Vous": "aurez senti",
      "Ils/Elle": "auront senti"
    },
    "Conditionnel Présent": {
      "Je": "sentirais",
      "Tu": "sentirais",
      "Il/Elle/On": "sentirait",
      "Nous": "sentirions",
      "Vous": "sentiriez",
      "Ils/Elle": "sentiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais senti",
      "Tu": "aurais senti",
      "Il/Elle/On": "aurait senti",
      "Nous": "aurions senti",
      "Vous": "auriez senti",
      "Ils/Elle": "auraient senti"
    },
    "Subjonctif Présent": {
      "Je": "sente",
      "Tu": "sentes",
      "Il/Elle/On": "sente",
      "Nous": "sentions",
      "Vous": "sentiez",
      "Ils/Elle": "sentent"
    },
    "Subjonctif Passé": {
      "Je": "aie senti",
      "Tu": "aies senti",
      "Il/Elle/On": "ait senti",
      "Nous": "ayons senti",
      "Vous": "ayez senti",
      "Ils/Elle": "aient senti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse senti",
      "Tu": "eusses senti",
      "Il/Elle/On": "eût senti",
      "Nous": "eussions senti",
      "Vous": "eussiez senti",
      "Ils/Elle": "eussent senti"
    },
    "Subjonctif Imparfait": {
      "Je": "sentisse",
      "Tu": "sentisses",
      "Il/Elle/On": "sentît",
      "Nous": "sentissions",
      "Vous": "sentissiez",
      "Ils/Elle": "sentissent"
    },
    "Impératif Présent": {
      "Tu": "sens",
      "Nous": "sentons",
      "Vous": "sentez"
    },
    "Impératif Passé": {
      "Tu": "aie senti",
      "Nous": "ayons senti",
      "Vous": "ayez senti"
    },
    "Infinitif Présent": "sentir",
    "Infinitif Passé": "avoir senti",
    "Participe Présent": "sentant",
    "Participe Passé": "senti",
    "Gérondif Présent": "en sentant",
    "Gérondif Passé": "en ayant senti"
},
"consentir": {
    "Présent": {
      "Je": "consens",
      "Tu": "consens",
      "Il/Elle/On": "consent",
      "Nous": "consentons",
      "Vous": "consentez",
      "Ils/Elle": "consentent"
    },
    "Imparfait": {
      "Je": "consentais",
      "Tu": "consentais",
      "Il/Elle/On": "consentait",
      "Nous": "consentions",
      "Vous": "consentiez",
      "Ils/Elle": "consentaient"
    },
    "Passé Composé": {
      "Je": "ai consenti",
      "Tu": "as consenti",
      "Il/Elle/On": "a consenti",
      "Nous": "avons consenti",
      "Vous": "avez consenti",
      "Ils/Elle": "ont consenti"
    },
    "Futur": {
      "Je": "consentirai",
      "Tu": "consentiras",
      "Il/Elle/On": "consentira",
      "Nous": "consentirons",
      "Vous": "consentirez",
      "Ils/Elle": "consentiront"
    },
    "Plus-que-parfait": {
      "Je": "avais consenti",
      "Tu": "avais consenti",
      "Il/Elle/On": "avait consenti",
      "Nous": "avions consenti",
      "Vous": "aviez consenti",
      "Ils/Elle": "avaient consenti"
    },
    "Futur Simple": {
      "Je": "consentirai",
      "Tu": "consentiras",
      "Il/Elle/On": "consentira",
      "Nous": "consentirons",
      "Vous": "consentirez",
      "Ils/Elle": "consentiront"
    },
    "Futur Antérieur": {
      "Je": "aurai consenti",
      "Tu": "auras consenti",
      "Il/Elle/On": "aura consenti",
      "Nous": "aurons consenti",
      "Vous": "aurez consenti",
      "Ils/Elle": "auront consenti"
    },
    "Conditionnel Présent": {
      "Je": "consentirais",
      "Tu": "consentirais",
      "Il/Elle/On": "consentirait",
      "Nous": "consentirions",
      "Vous": "consentiriez",
      "Ils/Elle": "consentiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais consenti",
      "Tu": "aurais consenti",
      "Il/Elle/On": "aurait consenti",
      "Nous": "aurions consenti",
      "Vous": "auriez consenti",
      "Ils/Elle": "auraient consenti"
    },
    "Subjonctif Présent": {
      "Je": "consente",
      "Tu": "consentes",
      "Il/Elle/On": "consente",
      "Nous": "consentions",
      "Vous": "consentiez",
      "Ils/Elle": "consentent"
    },
    "Subjonctif Passé": {
      "Je": "aie consenti",
      "Tu": "aies consenti",
      "Il/Elle/On": "ait consenti",
      "Nous": "ayons consenti",
      "Vous": "ayez consenti",
      "Ils/Elle": "aient consenti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse consenti",
      "Tu": "eusses consenti",
      "Il/Elle/On": "eût consenti",
      "Nous": "eussions consenti",
      "Vous": "eussiez consenti",
      "Ils/Elle": "eussent consenti"
    },
    "Subjonctif Imparfait": {
      "Je": "consentisse",
      "Tu": "consentisses",
      "Il/Elle/On": "consentît",
      "Nous": "consentissions",
      "Vous": "consentissiez",
      "Ils/Elle": "consentissent"
    },
    "Impératif Présent": {
      "Tu": "consens",
      "Nous": "consentons",
      "Vous": "consentez"
    },
    "Impératif Passé": {
      "Tu": "aie consenti",
      "Nous": "ayons consenti",
      "Vous": "ayez consenti"
    },
    "Infinitif Présent": "consentir",
    "Infinitif Passé": "avoir consenti",
    "Participe Présent": "consentant",
    "Participe Passé": "consenti",
    "Gérondif Présent": "en consentant",
    "Gérondif Passé": "en ayant consenti"
},
"pressentir": {
    "Présent": {
      "Je": "pressens",
      "Tu": "pressens",
      "Il/Elle/On": "pressent",
      "Nous": "pressentons",
      "Vous": "pressentez",
      "Ils/Elle": "pressentent"
    },
    "Imparfait": {
      "Je": "pressentais",
      "Tu": "pressentais",
      "Il/Elle/On": "pressentait",
      "Nous": "pressentions",
      "Vous": "pressentiez",
      "Ils/Elle": "pressentaient"
    },
    "Passé Composé": {
      "Je": "ai pressenti",
      "Tu": "as pressenti",
      "Il/Elle/On": "a pressenti",
      "Nous": "avons pressenti",
      "Vous": "avez pressenti",
      "Ils/Elle": "ont pressenti"
    },
    "Futur": {
      "Je": "pressentirai",
      "Tu": "pressentiras",
      "Il/Elle/On": "pressentira",
      "Nous": "pressentirons",
      "Vous": "pressentirez",
      "Ils/Elle": "pressentiront"
    },
    "Plus-que-parfait": {
      "Je": "avais pressenti",
      "Tu": "avais pressenti",
      "Il/Elle/On": "avait pressenti",
      "Nous": "avions pressenti",
      "Vous": "aviez pressenti",
      "Ils/Elle": "avaient pressenti"
    },
    "Futur Simple": {
      "Je": "pressentirai",
      "Tu": "pressentiras",
      "Il/Elle/On": "pressentira",
      "Nous": "pressentirons",
      "Vous": "pressentirez",
      "Ils/Elle": "pressentiront"
    },
    "Futur Antérieur": {
      "Je": "aurai pressenti",
      "Tu": "auras pressenti",
      "Il/Elle/On": "aura pressenti",
      "Nous": "aurons pressenti",
      "Vous": "aurez pressenti",
      "Ils/Elle": "auront pressenti"
    },
    "Conditionnel Présent": {
      "Je": "pressentirais",
      "Tu": "pressentirais",
      "Il/Elle/On": "pressentirait",
      "Nous": "pressentirions",
      "Vous": "pressentiriez",
      "Ils/Elle": "pressentiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais pressenti",
      "Tu": "aurais pressenti",
      "Il/Elle/On": "aurait pressenti",
      "Nous": "aurions pressenti",
      "Vous": "auriez pressenti",
      "Ils/Elle": "auraient pressenti"
    },
    "Subjonctif Présent": {
      "Je": "pressente",
      "Tu": "pressentes",
      "Il/Elle/On": "pressente",
      "Nous": "pressentions",
      "Vous": "pressentiez",
      "Ils/Elle": "pressentent"
    },
    "Subjonctif Passé": {
      "Je": "aie pressenti",
      "Tu": "aies pressenti",
      "Il/Elle/On": "ait pressenti",
      "Nous": "ayons pressenti",
      "Vous": "ayez pressenti",
      "Ils/Elle": "aient pressenti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse pressenti",
      "Tu": "eusses pressenti",
      "Il/Elle/On": "eût pressenti",
      "Nous": "eussions pressenti",
      "Vous": "eussiez pressenti",
      "Ils/Elle": "eussent pressenti"
    },
    "Subjonctif Imparfait": {
      "Je": "pressentisse",
      "Tu": "pressentisses",
      "Il/Elle/On": "pressentît",
      "Nous": "pressentions",
      "Vous": "pressentissiez",
      "Ils/Elle": "pressentissent"
    },
    "Impératif Présent": {
      "Tu": "pressens",
      "Nous": "pressentons",
      "Vous": "pressentez"
    },
    "Impératif Passé": {
      "Tu": "aie pressenti",
      "Nous": "ayons pressenti",
      "Vous": "ayez pressenti"
    },
    "Infinitif Présent": "pressentir",
    "Infinitif Passé": "avoir pressenti",
    "Participe Présent": "pressentant",
    "Participe Passé": "pressenti",
    "Gérondif Présent": "en pressentant",
    "Gérondif Passé": "en ayant pressenti"
},
 "ressentir": {
    "Présent": {
      "Je": "ressens",
      "Tu": "ressens",
      "Il/Elle/On": "ressent",
      "Nous": "ressentons",
      "Vous": "ressentez",
      "Ils/Elle": "ressentent"
    },
    "Imparfait": {
      "Je": "ressentais",
      "Tu": "ressentais",
      "Il/Elle/On": "ressentait",
      "Nous": "ressentions",
      "Vous": "ressentiez",
      "Ils/Elle": "ressentaient"
    },
    "Passé Composé": {
      "Je": "ai ressenti",
      "Tu": "as ressenti",
      "Il/Elle/On": "a ressenti",
      "Nous": "avons ressenti",
      "Vous": "avez ressenti",
      "Ils/Elle": "ont ressenti"
    },
    "Futur": {
      "Je": "ressentirai",
      "Tu": "ressentiras",
      "Il/Elle/On": "ressentira",
      "Nous": "ressentirons",
      "Vous": "ressentirez",
      "Ils/Elle": "ressentiront"
    },
    "Plus-que-parfait": {
      "Je": "avais ressenti",
      "Tu": "avais ressenti",
      "Il/Elle/On": "avait ressenti",
      "Nous": "avions ressenti",
      "Vous": "aviez ressenti",
      "Ils/Elle": "avaient ressenti"
    },
    "Futur Simple": {
      "Je": "ressentirai",
      "Tu": "ressentiras",
      "Il/Elle/On": "ressentira",
      "Nous": "ressentirons",
      "Vous": "ressentirez",
      "Ils/Elle": "ressentiront"
    },
    "Futur Antérieur": {
      "Je": "aurai ressenti",
      "Tu": "auras ressenti",
      "Il/Elle/On": "aura ressenti",
      "Nous": "aurons ressenti",
      "Vous": "aurez ressenti",
      "Ils/Elle": "auront ressenti"
    },
    "Conditionnel Présent": {
      "Je": "ressentirais",
      "Tu": "ressentirais",
      "Il/Elle/On": "ressentirait",
      "Nous": "ressentirions",
      "Vous": "ressentiriez",
      "Ils/Elle": "ressentiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais ressenti",
      "Tu": "aurais ressenti",
      "Il/Elle/On": "aurait ressenti",
      "Nous": "aurions ressenti",
      "Vous": "auriez ressenti",
      "Ils/Elle": "auraient ressenti"
    },
    "Subjonctif Présent": {
      "Je": "ressente",
      "Tu": "ressentes",
      "Il/Elle/On": "ressente",
      "Nous": "ressentions",
      "Vous": "ressentiez",
      "Ils/Elle": "ressentent"
    },
    "Subjonctif Passé": {
      "Je": "aie ressenti",
      "Tu": "aies ressenti",
      "Il/Elle/On": "ait ressenti",
      "Nous": "ayons ressenti",
      "Vous": "ayez ressenti",
      "Ils/Elle": "aient ressenti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse ressenti",
      "Tu": "eusses ressenti",
      "Il/Elle/On": "eût ressenti",
      "Nous": "eussions ressenti",
      "Vous": "eussiez ressenti",
      "Ils/Elle": "eussent ressenti"
    },
    "Subjonctif Imparfait": {
      "Je": "ressentisse",
      "Tu": "ressentisses",
      "Il/Elle/On": "ressentît",
      "Nous": "ressentissions",
      "Vous": "ressentissiez",
      "Ils/Elle": "ressentissent"
    },
    "Impératif Présent": {
      "Tu": "ressens",
      "Nous": "ressentons",
      "Vous": "ressentez"
    },
    "Impératif Passé": {
      "Tu": "aie ressenti",
      "Nous": "ayons ressenti",
      "Vous": "ayez ressenti"
    },
    "Infinitif Présent": "ressentir",
    "Infinitif Passé": "avoir ressenti",
    "Participe Présent": "ressentant",
    "Participe Passé": "ressenti",
    "Gérondif Présent": "en ressentant",
    "Gérondif Passé": "en ayant ressenti"
 },
 "mentir": {
    "Présent": {
      "Je": "mens",
      "Tu": "mens",
      "Il/Elle/On": "ment",
      "Nous": "mentons",
      "Vous": "mentez",
      "Ils/Elle": "mentent"
    },
    "Imparfait": {
      "Je": "mentais",
      "Tu": "mentais",
      "Il/Elle/On": "mentait",
      "Nous": "mentions",
      "Vous": "mentiez",
      "Ils/Elle": "mentaient"
    },
    "Passé Composé": {
      "Je": "ai menti",
      "Tu": "as menti",
      "Il/Elle/On": "a menti",
      "Nous": "avons menti",
      "Vous": "avez menti",
      "Ils/Elle": "ont menti"
    },
    "Futur": {
      "Je": "mentirai",
      "Tu": "mentiras",
      "Il/Elle/On": "mentira",
      "Nous": "mentirons",
      "Vous": "mentirez",
      "Ils/Elle": "mentiront"
    },
    "Plus-que-parfait": {
      "Je": "avais menti",
      "Tu": "avais menti",
      "Il/Elle/On": "avait menti",
      "Nous": "avions menti",
      "Vous": "aviez menti",
      "Ils/Elle": "avaient menti"
    },
    "Futur Simple": {
      "Je": "mentirai",
      "Tu": "mentiras",
      "Il/Elle/On": "mentira",
      "Nous": "mentirons",
      "Vous": "mentirez",
      "Ils/Elle": "mentiront"
    },
    "Futur Antérieur": {
      "Je": "aurai menti",
      "Tu": "auras menti",
      "Il/Elle/On": "aura menti",
      "Nous": "aurons menti",
      "Vous": "aurez menti",
      "Ils/Elle": "auront menti"
    },
    "Conditionnel Présent": {
      "Je": "mentirais",
      "Tu": "mentirais",
      "Il/Elle/On": "mentirait",
      "Nous": "mentirions",
      "Vous": "mentiriez",
      "Ils/Elle": "mentiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais menti",
      "Tu": "aurais menti",
      "Il/Elle/On": "aurait menti",
      "Nous": "aurions menti",
      "Vous": "auriez menti",
      "Ils/Elle": "auraient menti"
    },
    "Subjonctif Présent": {
      "Je": "mente",
      "Tu": "mentes",
      "Il/Elle/On": "mente",
      "Nous": "mentions",
      "Vous": "mentiez",
      "Ils/Elle": "mentent"
    },
    "Subjonctif Passé": {
      "Je": "aie menti",
      "Tu": "aies menti",
      "Il/Elle/On": "ait menti",
      "Nous": "ayons menti",
      "Vous": "ayez menti",
      "Ils/Elle": "aient menti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse menti",
      "Tu": "eusses menti",
      "Il/Elle/On": "eût menti",
      "Nous": "eussions menti",
      "Vous": "eussiez menti",
      "Ils/Elle": "eussent menti"
    },
    "Subjonctif Imparfait": {
      "Je": "mentisse",
      "Tu": "mentisses",
      "Il/Elle/On": "mentît",
      "Nous": "mentissions",
      "Vous": "mentissiez",
      "Ils/Elle": "mentissent"
    },
    "Impératif Présent": {
      "Tu": "mens",
      "Nous": "mentons",
      "Vous": "mentez"
    },
    "Impératif Passé": {
      "Tu": "aie menti",
      "Nous": "ayons menti",
      "Vous": "ayez menti"
    },
    "Infinitif Présent": "mentir",
    "Infinitif Passé": "avoir menti",
    "Participe Présent": "mentant",
    "Participe Passé": "menti",
    "Gérondif Présent": "en mentant",
    "Gérondif Passé": "en ayant menti"
  },
  "démentir": {
    "Présent": {
      "Je": "démens",
      "Tu": "démens",
      "Il/Elle/On": "dément",
      "Nous": "démentons",
      "Vous": "démentez",
      "Ils/Elle": "démentent"
    },
    "Imparfait": {
      "Je": "démentais",
      "Tu": "démentais",
      "Il/Elle/On": "démentait",
      "Nous": "démentions",
      "Vous": "démentiez",
      "Ils/Elle": "démentaient"
    },
    "Passé Composé": {
      "Je": "ai démenti",
      "Tu": "as démenti",
      "Il/Elle/On": "a démenti",
      "Nous": "avons démenti",
      "Vous": "avez démenti",
      "Ils/Elle": "ont démenti"
    },
    "Futur": {
      "Je": "démentirai",
      "Tu": "démentiras",
      "Il/Elle/On": "démentira",
      "Nous": "démentirons",
      "Vous": "démentirez",
      "Ils/Elle": "démentiront"
    },
    "Plus-que-parfait": {
      "Je": "avais démenti",
      "Tu": "avais démenti",
      "Il/Elle/On": "avait démenti",
      "Nous": "avions démenti",
      "Vous": "aviez démenti",
      "Ils/Elle": "avaient démenti"
    },
    "Futur Simple": {
      "Je": "démentirai",
      "Tu": "démentiras",
      "Il/Elle/On": "démentira",
      "Nous": "démentirons",
      "Vous": "démentirez",
      "Ils/Elle": "démentiront"
    },
    "Futur Antérieur": {
      "Je": "aurai démenti",
      "Tu": "auras démenti",
      "Il/Elle/On": "aura démenti",
      "Nous": "aurons démenti",
      "Vous": "aurez démenti",
      "Ils/Elle": "auront démenti"
    },
    "Conditionnel Présent": {
      "Je": "démentirais",
      "Tu": "démentirais",
      "Il/Elle/On": "démentirait",
      "Nous": "démentirions",
      "Vous": "démentiriez",
      "Ils/Elle": "démentiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais démenti",
      "Tu": "aurais démenti",
      "Il/Elle/On": "aurait démenti",
      "Nous": "aurions démenti",
      "Vous": "auriez démenti",
      "Ils/Elle": "auraient démenti"
    },
    "Subjonctif Présent": {
      "Je": "démente",
      "Tu": "démentes",
      "Il/Elle/On": "démente",
      "Nous": "démentions",
      "Vous": "démentiez",
      "Ils/Elle": "démentent"
    },
    "Subjonctif Passé": {
      "Je": "aie démenti",
      "Tu": "aies démenti",
      "Il/Elle/On": "ait démenti",
      "Nous": "ayons démenti",
      "Vous": "ayez démenti",
      "Ils/Elle": "aient démenti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse démenti",
      "Tu": "eusses démenti",
      "Il/Elle/On": "eût démenti",
      "Nous": "eussions démenti",
      "Vous": "eussiez démenti",
      "Ils/Elle": "eussent démenti"
    },
    "Subjonctif Imparfait": {
      "Je": "démentisse",
      "Tu": "démentisses",
      "Il/Elle/On": "démentît",
      "Nous": "démentissions",
      "Vous": "démentissiez",
      "Ils/Elle": "démentissent"
    },
    "Impératif Présent": {
      "Tu": "démens",
      "Nous": "démentons",
      "Vous": "démentez"
    },
    "Impératif Passé": {
      "Tu": "aie démenti",
      "Nous": "ayons démenti",
      "Vous": "ayez démenti"
    },
    "Infinitif Présent": "démentir",
    "Infinitif Passé": "avoir démenti",
    "Participe Présent": "démentant",
    "Participe Passé": "démenti",
    "Gérondif Présent": "en démentant",
    "Gérondif Passé": "en ayant démenti"
  },
  "partir": {
    "Présent": {
      "Je": "pars",
      "Tu": "pars",
      "Il/Elle/On": "part",
      "Nous": "partons",
      "Vous": "partez",
      "Ils/Elle": "partent"
    },
    "Imparfait": {
      "Je": "partais",
      "Tu": "partais",
      "Il/Elle/On": "partait",
      "Nous": "partions",
      "Vous": "partiez",
      "Ils/Elle": "partaient"
    },
    "Passé Composé": {
      "Je": "suis parti(e)",
      "Tu": "es parti(e)",
      "Il/Elle/On": "est parti(e)",
      "Nous": "sommes parti(e)s",
      "Vous": "êtes parti(e)(s)",
      "Ils/Elle": "sont parti(e)s"
    },
    "Futur": {
      "Je": "partirai",
      "Tu": "partiras",
      "Il/Elle/On": "partira",
      "Nous": "partirons",
      "Vous": "partirez",
      "Ils/Elle": "partiront"
    },
    "Plus-que-parfait": {
      "Je": "étais parti(e)",
      "Tu": "étais parti(e)",
      "Il/Elle/On": "était parti(e)",
      "Nous": "étions parti(e)s",
      "Vous": "étiez parti(e)(s)",
      "Ils/Elle": "étaient parti(e)s"
    },
    "Futur Simple": {
      "Je": "partirai",
      "Tu": "partiras",
      "Il/Elle/On": "partira",
      "Nous": "partirons",
      "Vous": "partirez",
      "Ils/Elle": "partiront"
    },
    "Futur Antérieur": {
      "Je": "serai parti(e)",
      "Tu": "seras parti(e)",
      "Il/Elle/On": "sera parti(e)",
      "Nous": "serons parti(e)s",
      "Vous": "serez parti(e)(s)",
      "Ils/Elle": "seront parti(e)s"
    },
    "Conditionnel Présent": {
      "Je": "partirais",
      "Tu": "partirais",
      "Il/Elle/On": "partirait",
      "Nous": "partirions",
      "Vous": "partiriez",
      "Ils/Elle": "partiraient"
    },
    "Conditionnel Passé": {
      "Je": "serais parti(e)",
      "Tu": "serais parti(e)",
      "Il/Elle/On": "serait parti(e)",
      "Nous": "serions parti(e)s",
      "Vous": "seriez parti(e)(s)",
      "Ils/Elle": "seraient parti(e)s"
    },
    "Subjonctif Présent": {
      "Je": "parte",
      "Tu": "partes",
      "Il/Elle/On": "parte",
      "Nous": "partions",
      "Vous": "partiez",
      "Ils/Elle": "partent"
    },
    "Subjonctif Passé": {
      "Je": "sois parti(e)",
      "Tu": "sois parti(e)",
      "Il/Elle/On": "soit parti(e)",
      "Nous": "soyons parti(e)s",
      "Vous": "soyez parti(e)(s)",
      "Ils/Elle": "soient parti(e)s"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "fusse parti(e)",
      "Tu": "fusses parti(e)",
      "Il/Elle/On": "fût parti(e)",
      "Nous": "fussions parti(e)s",
      "Vous": "fussiez parti(e)(s)",
      "Ils/Elle": "fussent parti(e)s"
    },
    "Subjonctif Imparfait": {
      "Je": "partisse",
      "Tu": "partisses",
      "Il/Elle/On": "partît",
      "Nous": "partissions",
      "Vous": "partissiez",
      "Ils/Elle": "partissent"
    },
    "Impératif Présent": {
      "Tu": "pars",
      "Nous": "partons",
      "Vous": "partez"
    },
    "Impératif Passé": {
      "Tu": "sois parti(e)",
      "Nous": "soyons parti(e)s",
      "Vous": "soyez parti(e)(s)"
    },
    "Infinitif Présent": "partir",
    "Infinitif Passé": "être parti(e)",
    "Participe Présent": "partant",
    "Participe Passé": "parti(e)",
    "Gérondif Présent": "en partant",
    "Gérondif Passé": "en étant parti(e)"
  },
  "départir": {
    "Présent": {
      "Je": "dépars",
      "Tu": "dépars",
      "Il/Elle/On": "départ",
      "Nous": "départons",
      "Vous": "départez",
      "Ils/Elle": "départent"
    },
    "Imparfait": {
      "Je": "départais",
      "Tu": "départais",
      "Il/Elle/On": "départait",
      "Nous": "départions",
      "Vous": "départiez",
      "Ils/Elle": "départaient"
    },
    "Passé Composé": {
      "Je": "ai départi",
      "Tu": "as départi",
      "Il/Elle/On": "a départi",
      "Nous": "avons départi",
      "Vous": "avez départi",
      "Ils/Elle": "ont départi"
    },
    "Futur": {
      "Je": "départirai",
      "Tu": "départiras",
      "Il/Elle/On": "départira",
      "Nous": "départirons",
      "Vous": "départirez",
      "Ils/Elle": "départiront"
    },
    "Plus-que-parfait": {
      "Je": "avais départi",
      "Tu": "avais départi",
      "Il/Elle/On": "avait départi",
      "Nous": "avions départi",
      "Vous": "aviez départi",
      "Ils/Elle": "avaient départi"
    },
    "Futur Simple": {
      "Je": "départirai",
      "Tu": "départiras",
      "Il/Elle/On": "départira",
      "Nous": "départirons",
      "Vous": "départirez",
      "Ils/Elle": "départiront"
    },
    "Futur Antérieur": {
      "Je": "aurai départi",
      "Tu": "auras départi",
      "Il/Elle/On": "aura départi",
      "Nous": "aurons départi",
      "Vous": "aurez départi",
      "Ils/Elle": "auront départi"
    },
    "Conditionnel Présent": {
      "Je": "départirais",
      "Tu": "départirais",
      "Il/Elle/On": "départirait",
      "Nous": "départirions",
      "Vous": "départiriez",
      "Ils/Elle": "départiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais départi",
      "Tu": "aurais départi",
      "Il/Elle/On": "aurait départi",
      "Nous": "aurions départi",
      "Vous": "auriez départi",
      "Ils/Elle": "auraient départi"
    },
    "Subjonctif Présent": {
      "Je": "départe",
      "Tu": "départes",
      "Il/Elle/On": "départe",
      "Nous": "départions",
      "Vous": "départiez",
      "Ils/Elle": "départent"
    },
    "Subjonctif Passé": {
      "Je": "aie départi",
      "Tu": "aies départi",
      "Il/Elle/On": "ait départi",
      "Nous": "ayons départi",
      "Vous": "ayez départi",
      "Ils/Elle": "aient départi"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse départi",
      "Tu": "eusses départi",
      "Il/Elle/On": "eût départi",
      "Nous": "eussions départi",
      "Vous": "eussiez départi",
      "Ils/Elle": "eussent départi"
    },
    "Subjonctif Imparfait": {
      "Je": "départisse",
      "Tu": "départisses",
      "Il/Elle/On": "départît",
      "Nous": "départissions",
      "Vous": "départissiez",
      "Ils/Elle": "départissent"
    },
    "Impératif Présent": {
      "Tu": "dépars",
      "Nous": "départons",
      "Vous": "départez"
    },
    "Impératif Passé": {
      "Tu": "aie départi",
      "Nous": "ayons départi",
      "Vous": "ayez départi"
    },
    "Infinitif Présent": "départir",
    "Infinitif Passé": "avoir départi",
    "Participe Présent": "départant",
    "Participe Passé": "départi",
    "Gérondif Présent": "en départant",
    "Gérondif Passé": "en ayant départi"
},
"repartir": {
    "Présent": {
      "Je": "repars",
      "Tu": "repars",
      "Il/Elle/On": "repart",
      "Nous": "repartons",
      "Vous": "repartez",
      "Ils/Elle": "repartent"
    },
    "Imparfait": {
      "Je": "repartais",
      "Tu": "repartais",
      "Il/Elle/On": "repartait",
      "Nous": "repartions",
      "Vous": "repartiez",
      "Ils/Elle": "repartaient"
    },
    "Passé Composé": {
      "Je": "ai reparti",
      "Tu": "as reparti",
      "Il/Elle/On": "a reparti",
      "Nous": "avons reparti",
      "Vous": "avez reparti",
      "Ils/Elle": "ont reparti"
    },
    "Futur": {
      "Je": "repartirai",
      "Tu": "repartiras",
      "Il/Elle/On": "repartira",
      "Nous": "repartirons",
      "Vous": "repartirez",
      "Ils/Elle": "repartiront"
    },
    "Plus-que-parfait": {
      "Je": "avais reparti",
      "Tu": "avais reparti",
      "Il/Elle/On": "avait reparti",
      "Nous": "avions reparti",
      "Vous": "aviez reparti",
      "Ils/Elle": "avaient reparti"
    },
    "Futur Simple": {
      "Je": "repartirai",
      "Tu": "repartiras",
      "Il/Elle/On": "repartira",
      "Nous": "repartirons",
      "Vous": "repartirez",
      "Ils/Elle": "repartiront"
    },
    "Futur Antérieur": {
      "Je": "aurai reparti",
      "Tu": "auras reparti",
      "Il/Elle/On": "aura reparti",
      "Nous": "aurons reparti",
      "Vous": "aurez reparti",
      "Ils/Elle": "auront reparti"
    },
    "Conditionnel Présent": {
      "Je": "repartirais",
      "Tu": "repartirais",
      "Il/Elle/On": "repartirait",
      "Nous": "repartirions",
      "Vous": "repartiriez",
      "Ils/Elle": "repartiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais reparti",
      "Tu": "aurais reparti",
      "Il/Elle/On": "aurait reparti",
      "Nous": "aurions reparti",
      "Vous": "auriez reparti",
      "Ils/Elle": "auraient reparti"
    },
    "Subjonctif Présent": {
      "Je": "reparte",
      "Tu": "repartes",
      "Il/Elle/On": "reparte",
      "Nous": "repartions",
      "Vous": "repartiez",
      "Ils/Elle": "repartent"
    },
    "Subjonctif Passé": {
      "Je": "aie reparti",
      "Tu": "aies reparti",
      "Il/Elle/On": "ait reparti",
      "Nous": "ayons reparti",
      "Vous": "ayez reparti",
      "Ils/Elle": "aient reparti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse reparti",
      "Tu": "eusses reparti",
      "Il/Elle/On": "eût reparti",
      "Nous": "eussions reparti",
      "Vous": "eussiez reparti",
      "Ils/Elle": "eussent reparti"
    },
    "Subjonctif Imparfait": {
      "Je": "repartisse",
      "Tu": "repartisses",
      "Il/Elle/On": "repartît",
      "Nous": "repartissions",
      "Vous": "repartissiez",
      "Ils/Elle": "repartissent"
    },
    "Impératif Présent": {
      "Tu": "repars",
      "Nous": "repartons",
      "Vous": "repartez"
    },
    "Impératif Passé": {
      "Tu": "aie reparti",
      "Nous": "ayons reparti",
      "Vous": "ayez reparti"
    },
    "Infinitif Présent": "repartir",
    "Infinitif Passé": "avoir reparti",
    "Participe Présent": "repartant",
    "Participe Passé": "reparti",
    "Gérondif Présent": "en repartant",
    "Gérondif Passé": "en ayant reparti"
},
"repentir": {
    "Présent": {
      "Je": "me repens",
      "Tu": "te repens",
      "Il/Elle/On": "se repent",
      "Nous": "nous repentons",
      "Vous": "vous repentez",
      "Ils/Elle": "se repentent"
    },
    "Imparfait": {
      "Je": "me repentais",
      "Tu": "te repentais",
      "Il/Elle/On": "se repentait",
      "Nous": "nous repentions",
      "Vous": "vous repenties",
      "Ils/Elle": "se repentaient"
    },
    "Passé Composé": {
      "Je": "me suis repenti",
      "Tu": "t'es repenti",
      "Il/Elle/On": "s'est repenti",
      "Nous": "nous sommes repentis",
      "Vous": "vous êtes repentis",
      "Ils/Elle": "se sont repentis"
    },
    "Futur": {
      "Je": "me repentirai",
      "Tu": "te repentiras",
      "Il/Elle/On": "se repentira",
      "Nous": "nous repentirons",
      "Vous": "vous repentirez",
      "Ils/Elle": "se repentiront"
    },
    "Plus-que-parfait": {
      "Je": "m'étais repenti",
      "Tu": "t'étais repenti",
      "Il/Elle/On": "s'était repenti",
      "Nous": "nous étions repentis",
      "Vous": "vous étiez repentis",
      "Ils/Elle": "s'étaient repentis"
    },
    "Futur Simple": {
      "Je": "me repentirai",
      "Tu": "te repentiras",
      "Il/Elle/On": "se repentira",
      "Nous": "nous repentirons",
      "Vous": "vous repentirez",
      "Ils/Elle": "se repentiront"
    },
    "Futur Antérieur": {
      "Je": "me serai repenti",
      "Tu": "te seras repenti",
      "Il/Elle/On": "se sera repenti",
      "Nous": "nous serons repentis",
      "Vous": "vous serez repentis",
      "Ils/Elle": "se seront repentis"
    },
    "Conditionnel Présent": {
      "Je": "me repentirais",
      "Tu": "te repentirais",
      "Il/Elle/On": "se repentirait",
      "Nous": "nous repentirions",
      "Vous": "vous repentiriez",
      "Ils/Elle": "se repentiraient"
    },
    "Conditionnel Passé": {
      "Je": "me serais repenti",
      "Tu": "te serais repenti",
      "Il/Elle/On": "se serait repenti",
      "Nous": "nous serions repentis",
      "Vous": "vous seriez repentis",
      "Ils/Elle": "se seraient repenties"
    },
    "Subjonctif Présent": {
      "Je": "me repente",
      "Tu": "te repentes",
      "Il/Elle/On": "se repente",
      "Nous": "nous repentions",
      "Vous": "vous repenties",
      "Ils/Elle": "se repentent"
    },
    "Subjonctif Passé": {
      "Je": "me sois repenti",
      "Tu": "te sois repenti",
      "Il/Elle/On": "se soit repenti",
      "Nous": "nous soyons repentis",
      "Vous": "vous soyez repentis",
      "Ils/Elle": "se soient repentis"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "me fusse repenti",
      "Tu": "te fusses repenti",
      "Il/Elle/On": "se fût repenti",
      "Nous": "nous fussions repentis",
      "Vous": "vous fussiez repentis",
      "Ils/Elle": "se fussent repentis"
    },
    "Subjonctif Imparfait": {
      "Je": "me repentisse",
      "Tu": "te repentisses",
      "Il/Elle/On": "se repentît",
      "Nous": "nous repentissions",
      "Vous": "vous repentissiez",
      "Ils/Elle": "se repentissent"
    },
    "Impératif Présent": {
      "Tu": "repens-toi",
      "Nous": "repentons-nous",
      "Vous": "repentez-vous"
    },
    "Impératif Passé": {
      "Tu": "sois repenti",
      "Nous": "soyons repentis",
      "Vous": "soyez repentis"
    },
    "Infinitif Présent": "se repentir",
    "Infinitif Passé": "s'être repenti",
    "Participe Présent": "se repentant",
    "Participe Passé": "repenti",
    "Gérondif Présent": "en se repentant",
    "Gérondif Passé": "en s'étant repenti"
},
"départir": {
    "Présent": {
      "Je": "dépars",
      "Tu": "dépars",
      "Il/Elle/On": "départ",
      "Nous": "départons",
      "Vous": "départez",
      "Ils/Elle": "départent"
    },
    "Imparfait": {
      "Je": "départais",
      "Tu": "départais",
      "Il/Elle/On": "départait",
      "Nous": "départions",
      "Vous": "départiez",
      "Ils/Elle": "départaient"
    },
    "Passé Composé": {
      "Je": "ai départi",
      "Tu": "as départi",
      "Il/Elle/On": "a départi",
      "Nous": "avons départi",
      "Vous": "avez départi",
      "Ils/Elle": "ont départi"
    },
    "Futur": {
      "Je": "départirai",
      "Tu": "départiras",
      "Il/Elle/On": "départira",
      "Nous": "départirons",
      "Vous": "départirez",
      "Ils/Elle": "départiront"
    },
    "Plus-que-parfait": {
      "Je": "avais départi",
      "Tu": "avais départi",
      "Il/Elle/On": "avait départi",
      "Nous": "avions départi",
      "Vous": "aviez départi",
      "Ils/Elle": "avaient départi"
    },
    "Futur Simple": {
      "Je": "départirai",
      "Tu": "départiras",
      "Il/Elle/On": "départira",
      "Nous": "départirons",
      "Vous": "départirez",
      "Ils/Elle": "départiront"
    },
    "Futur Antérieur": {
      "Je": "aurai départi",
      "Tu": "auras départi",
      "Il/Elle/On": "aura départi",
      "Nous": "aurons départi",
      "Vous": "aurez départi",
      "Ils/Elle": "auront départi"
    },
    "Conditionnel Présent": {
      "Je": "départirais",
      "Tu": "départirais",
      "Il/Elle/On": "départirait",
      "Nous": "départirions",
      "Vous": "départiriez",
      "Ils/Elle": "départiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais départi",
      "Tu": "aurais départi",
      "Il/Elle/On": "aurait départi",
      "Nous": "aurions départi",
      "Vous": "auriez départi",
      "Ils/Elle": "auraient départi"
    },
    "Subjonctif Présent": {
      "Je": "départe",
      "Tu": "départes",
      "Il/Elle/On": "départe",
      "Nous": "départions",
      "Vous": "départiez",
      "Ils/Elle": "départent"
    },
    "Subjonctif Passé": {
      "Je": "aie départi",
      "Tu": "aies départi",
      "Il/Elle/On": "ait départi",
      "Nous": "ayons départi",
      "Vous": "ayez départi",
      "Ils/Elle": "aient départi"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse départi",
      "Tu": "eusses départi",
      "Il/Elle/On": "eût départi",
      "Nous": "eussions départi",
      "Vous": "eussiez départi",
      "Ils/Elle": "eussent départi"
    },
    "Subjonctif Imparfait": {
      "Je": "départisse",
      "Tu": "départisses",
      "Il/Elle/On": "départît",
      "Nous": "départissions",
      "Vous": "départissiez",
      "Ils/Elle": "départissent"
    },
    "Impératif Présent": {
      "Tu": "dépars",
      "Nous": "départons",
      "Vous": "départez"
    },
    "Impératif Passé": {
      "Tu": "aie départi",
      "Nous": "ayons départi",
      "Vous": "ayez départi"
    },
    "Infinitif Présent": "départir",
    "Infinitif Passé": "avoir départi",
    "Participe Présent": "départant",
    "Participe Passé": "départi",
    "Gérondif Présent": "en départant",
    "Gérondif Passé": "en ayant départi"
},
"repartir": {
    "Présent": {
      "Je": "repars",
      "Tu": "repars",
      "Il/Elle/On": "repart",
      "Nous": "repartons",
      "Vous": "repartez",
      "Ils/Elle": "repartent"
    },
    "Imparfait": {
      "Je": "repartais",
      "Tu": "repartais",
      "Il/Elle/On": "repartait",
      "Nous": "repartions",
      "Vous": "repartiez",
      "Ils/Elle": "repartaient"
    },
    "Passé Composé": {
      "Je": "ai reparti",
      "Tu": "as reparti",
      "Il/Elle/On": "a reparti",
      "Nous": "avons reparti",
      "Vous": "avez reparti",
      "Ils/Elle": "ont reparti"
    },
    "Futur": {
      "Je": "repartirai",
      "Tu": "repartiras",
      "Il/Elle/On": "repartira",
      "Nous": "repartirons",
      "Vous": "repartirez",
      "Ils/Elle": "repartiront"
    },
    "Plus-que-parfait": {
      "Je": "avais reparti",
      "Tu": "avais reparti",
      "Il/Elle/On": "avait reparti",
      "Nous": "avions reparti",
      "Vous": "aviez reparti",
      "Ils/Elle": "avaient reparti"
    },
    "Futur Simple": {
      "Je": "repartirai",
      "Tu": "repartiras",
      "Il/Elle/On": "repartira",
      "Nous": "repartirons",
      "Vous": "repartirez",
      "Ils/Elle": "repartiront"
    },
    "Futur Antérieur": {
      "Je": "aurai reparti",
      "Tu": "auras reparti",
      "Il/Elle/On": "aura reparti",
      "Nous": "aurons reparti",
      "Vous": "aurez reparti",
      "Ils/Elle": "auront reparti"
    },
    "Conditionnel Présent": {
      "Je": "repartirais",
      "Tu": "repartirais",
      "Il/Elle/On": "repartirait",
      "Nous": "repartirions",
      "Vous": "repartiriez",
      "Ils/Elle": "repartiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais reparti",
      "Tu": "aurais reparti",
      "Il/Elle/On": "aurait reparti",
      "Nous": "aurions reparti",
      "Vous": "auriez reparti",
      "Ils/Elle": "auraient reparti"
    },
    "Subjonctif Présent": {
      "Je": "reparte",
      "Tu": "repartes",
      "Il/Elle/On": "reparte",
      "Nous": "repartions",
      "Vous": "repartiez",
      "Ils/Elle": "repartent"
    },
    "Subjonctif Passé": {
      "Je": "aie reparti",
      "Tu": "aies reparti",
      "Il/Elle/On": "ait reparti",
      "Nous": "ayons reparti",
      "Vous": "ayez reparti",
      "Ils/Elle": "aient reparti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse reparti",
      "Tu": "eusses reparti",
      "Il/Elle/On": "eût reparti",
      "Nous": "eussions reparti",
      "Vous": "eussiez reparti",
      "Ils/Elle": "eussent reparti"
    },
    "Subjonctif Imparfait": {
      "Je": "repartisse",
      "Tu": "repartisses",
      "Il/Elle/On": "repartît",
      "Nous": "repartissions",
      "Vous": "repartissiez",
      "Ils/Elle": "repartissent"
    },
    "Impératif Présent": {
      "Tu": "repars",
      "Nous": "repartons",
      "Vous": "repartez"
    },
    "Impératif Passé": {
      "Tu": "aie reparti",
      "Nous": "ayons reparti",
      "Vous": "ayez reparti"
    },
    "Infinitif Présent": "repartir",
    "Infinitif Passé": "avoir reparti",
    "Participe Présent": "repartant",
    "Participe Passé": "reparti",
    "Gérondif Présent": "en repartant",
    "Gérondif Passé": "en ayant reparti"
},
"repentir": {
    "Présent": {
      "Je": "me repens",
      "Tu": "te repens",
      "Il/Elle/On": "se repent",
      "Nous": "nous repentons",
      "Vous": "vous repentez",
      "Ils/Elle": "se repentent"
    },
    "Imparfait": {
      "Je": "me repentais",
      "Tu": "te repentais",
      "Il/Elle/On": "se repentait",
      "Nous": "nous repentions",
      "Vous": "vous repenties",
      "Ils/Elle": "se repentaient"
    },
    "Passé Composé": {
      "Je": "me suis repenti",
      "Tu": "t'es repenti",
      "Il/Elle/On": "s'est repenti",
      "Nous": "nous sommes repentis",
      "Vous": "vous êtes repentis",
      "Ils/Elle": "se sont repentis"
    },
    "Futur": {
      "Je": "me repentirai",
      "Tu": "te repentiras",
      "Il/Elle/On": "se repentira",
      "Nous": "nous repentirons",
      "Vous": "vous repentirez",
      "Ils/Elle": "se repentiront"
    },
    "Plus-que-parfait": {
      "Je": "m'étais repenti",
      "Tu": "t'étais repenti",
      "Il/Elle/On": "s'était repenti",
      "Nous": "nous étions repentis",
      "Vous": "vous étiez repentis",
      "Ils/Elle": "s'étaient repentis"
    },
    "Futur Simple": {
      "Je": "me repentirai",
      "Tu": "te repentiras",
      "Il/Elle/On": "se repentira",
      "Nous": "nous repentirons",
      "Vous": "vous repentirez",
      "Ils/Elle": "se repentiront"
    },
    "Futur Antérieur": {
      "Je": "me serai repenti",
      "Tu": "te seras repenti",
      "Il/Elle/On": "se sera repenti",
      "Nous": "nous serons repentis",
      "Vous": "vous serez repentis",
      "Ils/Elle": "se seront repentis"
    },
    "Conditionnel Présent": {
      "Je": "me repentirais",
      "Tu": "te repentirais",
      "Il/Elle/On": "se repentirait",
      "Nous": "nous repentirions",
      "Vous": "vous repentiriez",
      "Ils/Elle": "se repentiraient"
    },
    "Conditionnel Passé": {
      "Je": "me serais repenti",
      "Tu": "te serais repenti",
      "Il/Elle/On": "se serait repenti",
      "Nous": "nous serions repentis",
      "Vous": "vous seriez repentis",
      "Ils/Elle": "se seraient repenties"
    },
    "Subjonctif Présent": {
      "Je": "me repente",
      "Tu": "te repentes",
      "Il/Elle/On": "se repente",
      "Nous": "nous repentions",
      "Vous": "vous repenties",
      "Ils/Elle": "se repentent"
    },
    "Subjonctif Passé": {
      "Je": "me sois repenti",
      "Tu": "te sois repenti",
      "Il/Elle/On": "se soit repenti",
      "Nous": "nous soyons repentis",
      "Vous": "vous soyez repentis",
      "Ils/Elle": "se soient repentis"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "me fusse repenti",
      "Tu": "te fusses repenti",
      "Il/Elle/On": "se fût repenti",
      "Nous": "nous fussions repentis",
      "Vous": "vous fussiez repentis",
      "Ils/Elle": "se fussent repentis"
    },
    "Subjonctif Imparfait": {
      "Je": "me repentisse",
      "Tu": "te repentisses",
      "Il/Elle/On": "se repentît",
      "Nous": "nous repentissions",
      "Vous": "vous repentissiez",
      "Ils/Elle": "se repentissent"
    },
    "Impératif Présent": {
      "Tu": "repens-toi",
      "Nous": "repentons-nous",
      "Vous": "repentez-vous"
    },
    "Impératif Passé": {
      "Tu": "sois repenti",
      "Nous": "soyons repentis",
      "Vous": "soyez repentis"
    },
    "Infinitif Présent": "se repentir",
    "Infinitif Passé": "s'être repenti",
    "Participe Présent": "se repentant",
    "Participe Passé": "repenti",
    "Gérondif Présent": "en se repentant",
    "Gérondif Passé": "en s'étant repenti"
},
"sortir": {
    "Présent": {
      "Je": "sors",
      "Tu": "sors",
      "Il/Elle/On": "sort",
      "Nous": "sortons",
      "Vous": "sortez",
      "Ils/Elle": "sortent"
    },
    "Imparfait": {
      "Je": "sortais",
      "Tu": "sortais",
      "Il/Elle/On": "sortait",
      "Nous": "sortions",
      "Vous": "sortiez",
      "Ils/Elle": "sortaient"
    },
    "Passé Composé": {
      "Je": "ai sorti",
      "Tu": "as sorti",
      "Il/Elle/On": "a sorti",
      "Nous": "avons sorti",
      "Vous": "avez sorti",
      "Ils/Elle": "ont sorti"
    },
    "Futur": {
      "Je": "sortirai",
      "Tu": "sortiras",
      "Il/Elle/On": "sortira",
      "Nous": "sortirons",
      "Vous": "sortirez",
      "Ils/Elle": "sortiront"
    },
    "Plus-que-parfait": {
      "Je": "avais sorti",
      "Tu": "avais sorti",
      "Il/Elle/On": "avait sorti",
      "Nous": "avions sorti",
      "Vous": "aviez sorti",
      "Ils/Elle": "avaient sorti"
    },
    "Futur Simple": {
      "Je": "sortirai",
      "Tu": "sortiras",
      "Il/Elle/On": "sortira",
      "Nous": "sortirons",
      "Vous": "sortirez",
      "Ils/Elle": "sortiront"
    },
    "Futur Antérieur": {
      "Je": "aurai sorti",
      "Tu": "auras sorti",
      "Il/Elle/On": "aura sorti",
      "Nous": "aurons sorti",
      "Vous": "aurez sorti",
      "Ils/Elle": "auront sorti"
    },
    "Conditionnel Présent": {
      "Je": "sortirais",
      "Tu": "sortirais",
      "Il/Elle/On": "sortirait",
      "Nous": "sortirions",
      "Vous": "sortiriez",
      "Ils/Elle": "sortiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais sorti",
      "Tu": "aurais sorti",
      "Il/Elle/On": "aurait sorti",
      "Nous": "aurions sorti",
      "Vous": "auriez sorti",
      "Ils/Elle": "auraient sorti"
    },
    "Subjonctif Présent": {
      "Je": "sorte",
      "Tu": "sortes",
      "Il/Elle/On": "sorte",
      "Nous": "sortions",
      "Vous": "sortiez",
      "Ils/Elle": "sortent"
    },
    "Subjonctif Passé": {
      "Je": "aie sorti",
      "Tu": "aies sorti",
      "Il/Elle/On": "ait sorti",
      "Nous": "ayons sorti",
      "Vous": "ayez sorti",
      "Ils/Elle": "aient sorti"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse sorti",
      "Tu": "eusses sorti",
      "Il/Elle/On": "eût sorti",
      "Nous": "eussions sorti",
      "Vous": "eussiez sorti",
      "Ils/Elle": "eussent sorti"
    },
    "Subjonctif Imparfait": {
      "Je": "sortisse",
      "Tu": "sortisses",
      "Il/Elle/On": "sortît",
      "Nous": "sortissions",
      "Vous": "sortissiez",
      "Ils/Elle": "sortissent"
    },
    "Impératif Présent": {
      "Tu": "sors",
      "Nous": "sortons",
      "Vous": "sortez"
    },
    "Impératif Passé": {
      "Tu": "aie sorti",
      "Nous": "ayons sorti",
      "Vous": "ayez sorti"
    },
    "Infinitif Présent": "sortir",
    "Infinitif Passé": "avoir sorti",
    "Participe Présent": "sortant",
    "Participe Passé": "sorti",
    "Gérondif Présent": "en sortant",
    "Gérondif Passé": "en ayant sorti"
},
"ressortir": {
    "Présent": {
      "Je": "ressors",
      "Tu": "ressors",
      "Il/Elle/On": "ressort",
      "Nous": "ressortons",
      "Vous": "ressortez",
      "Ils/Elle": "ressortent"
    },
    "Imparfait": {
      "Je": "ressortais",
      "Tu": "ressortais",
      "Il/Elle/On": "ressortait",
      "Nous": "ressortions",
      "Vous": "ressortiez",
      "Ils/Elle": "ressortaient"
    },
    "Passé Composé": {
      "Je": "ai ressori",
      "Tu": "as ressori",
      "Il/Elle/On": "a ressori",
      "Nous": "avons ressori",
      "Vous": "avez ressori",
      "Ils/Elle": "ont ressori"
    },
    "Futur": {
      "Je": "ressortirai",
      "Tu": "ressortiras",
      "Il/Elle/On": "ressortira",
      "Nous": "ressortirons",
      "Vous": "ressortirez",
      "Ils/Elle": "ressortiront"
    },
    "Plus-que-parfait": {
      "Je": "avais ressori",
      "Tu": "avais ressori",
      "Il/Elle/On": "avait ressori",
      "Nous": "avions ressori",
      "Vous": "aviez ressori",
      "Ils/Elle": "avaient ressori"
    },
    "Futur Simple": {
      "Je": "ressortirai",
      "Tu": "ressortiras",
      "Il/Elle/On": "ressortira",
      "Nous": "ressortirons",
      "Vous": "ressortirez",
      "Ils/Elle": "ressortiront"
    },
    "Futur Antérieur": {
      "Je": "aurai ressori",
      "Tu": "auras ressori",
      "Il/Elle/On": "aura ressori",
      "Nous": "aurons ressori",
      "Vous": "aurez ressori",
      "Ils/Elle": "auront ressori"
    },
    "Conditionnel Présent": {
      "Je": "ressortirais",
      "Tu": "ressortirais",
      "Il/Elle/On": "ressortirait",
      "Nous": "ressortirions",
      "Vous": "ressortiriez",
      "Ils/Elle": "ressortiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais ressori",
      "Tu": "aurais ressori",
      "Il/Elle/On": "aurait ressori",
      "Nous": "aurions ressori",
      "Vous": "auriez ressori",
      "Ils/Elle": "auraient ressori"
    },
    "Subjonctif Présent": {
      "Je": "ressorte",
      "Tu": "ressortes",
      "Il/Elle/On": "ressorte",
      "Nous": "ressortions",
      "Vous": "ressortiez",
      "Ils/Elle": "ressortent"
    },
    "Subjonctif Passé": {
      "Je": "aie ressori",
      "Tu": "aies ressori",
      "Il/Elle/On": "ait ressori",
      "Nous": "ayons ressori",
      "Vous": "ayez ressori",
      "Ils/Elle": "aient ressori"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse ressori",
      "Tu": "eusses ressori",
      "Il/Elle/On": "eût ressori",
      "Nous": "eussions ressori",
      "Vous": "eussiez ressori",
      "Ils/Elle": "eussent ressori"
    },
    "Subjonctif Imparfait": {
      "Je": "ressortisse",
      "Tu": "ressortisses",
      "Il/Elle/On": "ressortît",
      "Nous": "ressortissions",
      "Vous": "ressortissiez",
      "Ils/Elle": "ressortissent"
    },
    "Impératif Présent": {
      "Tu": "ressors",
      "Nous": "ressortons",
      "Vous": "ressortez"
    },
    "Impératif Passé": {
      "Tu": "aie ressori",
      "Nous": "ayons ressori",
      "Vous": "ayez ressori"
    },
    "Infinitif Présent": "ressortir",
    "Infinitif Passé": "avoir ressori",
    "Participe Présent": "ressortant",
    "Participe Passé": "ressori",
    "Gérondif Présent": "en ressortant",
    "Gérondif Passé": "en ayant ressori"
},
"vêtir": {
    "Présent": {
      "Je": "vêts",
      "Tu": "vêts",
      "Il/Elle/On": "vêt",
      "Nous": "vêtons",
      "Vous": "vêtez",
      "Ils/Elle": "vêtent"
    },
    "Imparfait": {
      "Je": "vêtais",
      "Tu": "vêtais",
      "Il/Elle/On": "vêtait",
      "Nous": "vêtions",
      "Vous": "vêtiez",
      "Ils/Elle": "vêtaient"
    },
    "Passé Composé": {
      "Je": "ai vêtu",
      "Tu": "as vêtu",
      "Il/Elle/On": "a vêtu",
      "Nous": "avons vêtu",
      "Vous": "avez vêtu",
      "Ils/Elle": "ont vêtu"
    },
    "Futur": {
      "Je": "vêtirai",
      "Tu": "vêtiras",
      "Il/Elle/On": "vêtira",
      "Nous": "vêtirons",
      "Vous": "vêtirez",
      "Ils/Elle": "vêtiront"
    },
    "Plus-que-parfait": {
      "Je": "avais vêtu",
      "Tu": "avais vêtu",
      "Il/Elle/On": "avait vêtu",
      "Nous": "avions vêtu",
      "Vous": "aviez vêtu",
      "Ils/Elle": "avaient vêtu"
    },
    "Futur Simple": {
      "Je": "vêtirai",
      "Tu": "vêtiras",
      "Il/Elle/On": "vêtira",
      "Nous": "vêtirons",
      "Vous": "vêtirez",
      "Ils/Elle": "vêtiront"
    },
    "Futur Antérieur": {
      "Je": "aurai vêtu",
      "Tu": "auras vêtu",
      "Il/Elle/On": "aura vêtu",
      "Nous": "aurons vêtu",
      "Vous": "aurez vêtu",
      "Ils/Elle": "auront vêtu"
    },
    "Conditionnel Présent": {
      "Je": "vêtirais",
      "Tu": "vêtirais",
      "Il/Elle/On": "vêtirait",
      "Nous": "vêtirions",
      "Vous": "vêtiriez",
      "Ils/Elle": "vêtiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais vêtu",
      "Tu": "aurais vêtu",
      "Il/Elle/On": "aurait vêtu",
      "Nous": "aurions vêtu",
      "Vous": "auriez vêtu",
      "Ils/Elle": "auraient vêtu"
    },
    "Subjonctif Présent": {
      "Je": "vête",
      "Tu": "vêtes",
      "Il/Elle/On": "vête",
      "Nous": "vêtions",
      "Vous": "vêtiez",
      "Ils/Elle": "vêtent"
    },
    "Subjonctif Passé": {
      "Je": "aie vêtu",
      "Tu": "aies vêtu",
      "Il/Elle/On": "ait vêtu",
      "Nous": "ayons vêtu",
      "Vous": "ayez vêtu",
      "Ils/Elle": "aient vêtu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse vêtu",
      "Tu": "eusses vêtu",
      "Il/Elle/On": "eût vêtu",
      "Nous": "eussions vêtu",
      "Vous": "eussiez vêtu",
      "Ils/Elle": "eussent vêtu"
    },
    "Subjonctif Imparfait": {
      "Je": "vêtisse",
      "Tu": "vêtisses",
      "Il/Elle/On": "vêtît",
      "Nous": "vêtissions",
      "Vous": "vêtissiez",
      "Ils/Elle": "vêtissent"
    },
    "Impératif Présent": {
      "Tu": "vêts",
      "Nous": "vêtons",
      "Vous": "vêtez"
    },
    "Impératif Passé": {
      "Tu": "aie vêtu",
      "Nous": "ayons vêtu",
      "Vous": "ayez vêtu"
    },
    "Infinitif Présent": "vêtir",
    "Infinitif Passé": "avoir vêtu",
    "Participe Présent": "vêtant",
    "Participe Passé": "vêtu",
    "Gérondif Présent": "en vêtant",
    "Gérondif Passé": "en ayant vêtu"
},
"dévetir": {
    "Présent": {
      "Je": "dévêts",
      "Tu": "dévêts",
      "Il/Elle/On": "dévêt",
      "Nous": "dévetons",
      "Vous": "dévetiez",
      "Ils/Elle": "dévêtent"
    },
    "Imparfait": {
      "Je": "dévetais",
      "Tu": "dévetais",
      "Il/Elle/On": "dévetait",
      "Nous": "dévetions",
      "Vous": "dévetiez",
      "Ils/Elle": "dévetaient"
    },
    "Passé Composé": {
      "Je": "ai dévêtu",
      "Tu": "as dévêtu",
      "Il/Elle/On": "a dévêtu",
      "Nous": "avons dévêtu",
      "Vous": "avez dévêtu",
      "Ils/Elle": "ont dévêtu"
    },
    "Futur": {
      "Je": "dévetirai",
      "Tu": "dévetiras",
      "Il/Elle/On": "dévetira",
      "Nous": "dévetirons",
      "Vous": "dévetirez",
      "Ils/Elle": "dévetiront"
    },
    "Plus-que-parfait": {
      "Je": "avais dévêtu",
      "Tu": "avais dévêtu",
      "Il/Elle/On": "avait dévêtu",
      "Nous": "avions dévêtu",
      "Vous": "aviez dévêtu",
      "Ils/Elle": "avaient dévêtu"
    },
    "Futur Simple": {
      "Je": "dévetirai",
      "Tu": "dévetiras",
      "Il/Elle/On": "dévetira",
      "Nous": "dévetirons",
      "Vous": "dévetirez",
      "Ils/Elle": "dévetiront"
    },
    "Futur Antérieur": {
      "Je": "aurai dévêtu",
      "Tu": "auras dévêtu",
      "Il/Elle/On": "aura dévêtu",
      "Nous": "aurons dévêtu",
      "Vous": "aurez dévêtu",
      "Ils/Elle": "auront dévêtu"
    },
    "Conditionnel Présent": {
      "Je": "dévetirais",
      "Tu": "dévetirais",
      "Il/Elle/On": "dévetirait",
      "Nous": "dévetirions",
      "Vous": "dévetiriez",
      "Ils/Elle": "dévetiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais dévêtu",
      "Tu": "aurais dévêtu",
      "Il/Elle/On": "aurait dévêtu",
      "Nous": "aurions dévêtu",
      "Vous": "auriez dévêtu",
      "Ils/Elle": "auraient dévêtu"
    },
    "Subjonctif Présent": {
      "Je": "dévête",
      "Tu": "dévêtes",
      "Il/Elle/On": "dévête",
      "Nous": "dévetions",
      "Vous": "dévetiez",
      "Ils/Elle": "dévêtent"
    },
    "Subjonctif Passé": {
      "Je": "aie dévêtu",
      "Tu": "aies dévêtu",
      "Il/Elle/On": "ait dévêtu",
      "Nous": "ayons dévêtu",
      "Vous": "ayez dévêtu",
      "Ils/Elle": "aient dévêtu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse dévêtu",
      "Tu": "eusses dévêtu",
      "Il/Elle/On": "eût dévêtu",
      "Nous": "eussions dévêtu",
      "Vous": "eussiez dévêtu",
      "Ils/Elle": "eussent dévêtu"
    },
    "Subjonctif Imparfait": {
      "Je": "dévêtisse",
      "Tu": "dévêtisses",
      "Il/Elle/On": "dévêtît",
      "Nous": "dévêtissions",
      "Vous": "dévêtissiez",
      "Ils/Elle": "dévêtissent"
    },
    "Impératif Présent": {
      "Tu": "dévêts",
      "Nous": "dévetons",
      "Vous": "dévetez"
    },
    "Impératif Passé": {
      "Tu": "aie dévêtu",
      "Nous": "ayons dévêtu",
      "Vous": "ayez dévêtu"
    },
    "Infinitif Présent": "dévêtir",
    "Infinitif Passé": "avoir dévêtu",
    "Participe Présent": "dévêtant",
    "Participe Passé": "dévêtu",
    "Gérondif Présent": "en dévêtant",
    "Gérondif Passé": "en ayant dévêtu"
},
"revêtir": {
    "Présent": {
      "Je": "revêts",
      "Tu": "revêts",
      "Il/Elle/On": "revêt",
      "Nous": "revêtons",
      "Vous": "revêtez",
      "Ils/Elle": "revêtent"
    },
    "Imparfait": {
      "Je": "revêtais",
      "Tu": "revêtais",
      "Il/Elle/On": "revêtait",
      "Nous": "revêtions",
      "Vous": "revêtiez",
      "Ils/Elle": "revêtaient"
    },
    "Passé Composé": {
      "Je": "ai revêtu",
      "Tu": "as revêtu",
      "Il/Elle/On": "a revêtu",
      "Nous": "avons revêtu",
      "Vous": "avez revêtu",
      "Ils/Elle": "ont revêtu"
    },
    "Futur": {
      "Je": "revêtirai",
      "Tu": "revêtiras",
      "Il/Elle/On": "revêtira",
      "Nous": "revêtirons",
      "Vous": "revêtirez",
      "Ils/Elle": "revêtiront"
    },
    "Plus-que-parfait": {
      "Je": "avais revêtu",
      "Tu": "avais revêtu",
      "Il/Elle/On": "avait revêtu",
      "Nous": "avions revêtu",
      "Vous": "aviez revêtu",
      "Ils/Elle": "avaient revêtu"
    },
    "Futur Simple": {
      "Je": "revêtirai",
      "Tu": "revêtiras",
      "Il/Elle/On": "revêtira",
      "Nous": "revêtirons",
      "Vous": "revêtirez",
      "Ils/Elle": "revêtiront"
    },
    "Futur Antérieur": {
      "Je": "aurai revêtu",
      "Tu": "auras revêtu",
      "Il/Elle/On": "aura revêtu",
      "Nous": "aurons revêtu",
      "Vous": "aurez revêtu",
      "Ils/Elle": "auront revêtu"
    },
    "Conditionnel Présent": {
      "Je": "revêtirais",
      "Tu": "revêtirais",
      "Il/Elle/On": "revêtirait",
      "Nous": "revêtirions",
      "Vous": "revêtiriez",
      "Ils/Elle": "revêtiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais revêtu",
      "Tu": "aurais revêtu",
      "Il/Elle/On": "aurait revêtu",
      "Nous": "aurions revêtu",
      "Vous": "auriez revêtu",
      "Ils/Elle": "auraient revêtu"
    },
    "Subjonctif Présent": {
      "Je": "revête",
      "Tu": "revêtes",
      "Il/Elle/On": "revête",
      "Nous": "revêtions",
      "Vous": "revêtiez",
      "Ils/Elle": "revêtent"
    },
    "Subjonctif Passé": {
      "Je": "aie revêtu",
      "Tu": "aies revêtu",
      "Il/Elle/On": "ait revêtu",
      "Nous": "ayons revêtu",
      "Vous": "ayez revêtu",
      "Ils/Elle": "aient revêtu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse revêtu",
      "Tu": "eusses revêtu",
      "Il/Elle/On": "eût revêtu",
      "Nous": "eussions revêtu",
      "Vous": "eussiez revêtu",
      "Ils/Elle": "eussent revêtu"
    },
    "Subjonctif Imparfait": {
      "Je": "revêtisse",
      "Tu": "revêtisses",
      "Il/Elle/On": "revêtît",
      "Nous": "revêtissions",
      "Vous": "revêtissiez",
      "Ils/Elle": "revêtissent"
    },
    "Impératif Présent": {
      "Tu": "revêts",
      "Nous": "revêtons",
      "Vous": "revêtez"
    },
    "Impératif Passé": {
      "Tu": "aie revêtu",
      "Nous": "ayons revêtu",
      "Vous": "ayez revêtu"
    },
    "Infinitif Présent": "revêtir",
    "Infinitif Passé": "avoir revêtu",
    "Participe Présent": "revêtant",
    "Participe Passé": "revêtu",
    "Gérondif Présent": "en revêtant",
    "Gérondif Passé": "en ayant revêtu"
},
"survetir": {
    "Présent": {
      "Je": "survêts",
      "Tu": "survêts",
      "Il/Elle/On": "survêt",
      "Nous": "survetons",
      "Vous": "survetiez",
      "Ils/Elle": "survêtent"
    },
    "Imparfait": {
      "Je": "survêtais",
      "Tu": "survêtais",
      "Il/Elle/On": "survêtait",
      "Nous": "survêtions",
      "Vous": "survêtiez",
      "Ils/Elle": "survêtaient"
    },
    "Passé Composé": {
      "Je": "ai survêtu",
      "Tu": "as survêtu",
      "Il/Elle/On": "a survêtu",
      "Nous": "avons survêtu",
      "Vous": "avez survêtu",
      "Ils/Elle": "ont survêtu"
    },
    "Futur": {
      "Je": "survetirai",
      "Tu": "survetiras",
      "Il/Elle/On": "survetira",
      "Nous": "survetirons",
      "Vous": "survetirez",
      "Ils/Elle": "survetiront"
    },
    "Plus-que-parfait": {
      "Je": "avais survêtu",
      "Tu": "avais survêtu",
      "Il/Elle/On": "avait survêtu",
      "Nous": "avions survêtu",
      "Vous": "aviez survêtu",
      "Ils/Elle": "avaient survêtu"
    },
    "Futur Simple": {
      "Je": "survetirai",
      "Tu": "survetiras",
      "Il/Elle/On": "survetira",
      "Nous": "survetirons",
      "Vous": "survetirez",
      "Ils/Elle": "survetiront"
    },
    "Futur Antérieur": {
      "Je": "aurai survêtu",
      "Tu": "auras survêtu",
      "Il/Elle/On": "aura survêtu",
      "Nous": "aurons survêtu",
      "Vous": "aurez survêtu",
      "Ils/Elle": "auront survêtu"
    },
    "Conditionnel Présent": {
      "Je": "survetirais",
      "Tu": "survetirais",
      "Il/Elle/On": "survetirait",
      "Nous": "survetirions",
      "Vous": "survetiriez",
      "Ils/Elle": "survetiraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais survêtu",
      "Tu": "aurais survêtu",
      "Il/Elle/On": "aurait survêtu",
      "Nous": "aurions survêtu",
      "Vous": "auriez survêtu",
      "Ils/Elle": "auraient survêtu"
    },
    "Subjonctif Présent": {
      "Je": "survête",
      "Tu": "survêtes",
      "Il/Elle/On": "survête",
      "Nous": "survetions",
      "Vous": "survetiez",
      "Ils/Elle": "survêtent"
    },
    "Subjonctif Passé": {
      "Je": "aie survêtu",
      "Tu": "aies survêtu",
      "Il/Elle/On": "ait survêtu",
      "Nous": "ayons survêtu",
      "Vous": "ayez survêtu",
      "Ils/Elle": "aient survêtu"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse survêtu",
      "Tu": "eusses survêtu",
      "Il/Elle/On": "eût survêtu",
      "Nous": "eussions survêtu",
      "Vous": "eussiez survêtu",
      "Ils/Elle": "eussent survêtu"
    },
    "Subjonctif Imparfait": {
      "Je": "survêtisse",
      "Tu": "survêtisses",
      "Il/Elle/On": "survêtît",
      "Nous": "survêtissions",
      "Vous": "survêtissiez",
      "Ils/Elle": "survêtissent"
    },
    "Impératif Présent": {
      "Tu": "survêts",
      "Nous": "survetons",
      "Vous": "survêtez"
    },
    "Impératif Passé": {
      "Tu": "aie survêtu",
      "Nous": "ayons survêtu",
      "Vous": "ayez survêtu"
    },
    "Infinitif Présent": "survetir",
    "Infinitif Passé": "avoir survêtu",
    "Participe Présent": "survêtant",
    "Participe Passé": "survêtu",
    "Gérondif Présent": "en survêtant",
    "Gérondif Passé": "en ayant survêtu"
},
"couvrir": {
    "Présent": {
      "Je": "couvre",
      "Tu": "couvres",
      "Il/Elle/On": "couvre",
      "Nous": "couvrons",
      "Vous": "couvrez",
      "Ils/Elle": "couvrent"
    },
    "Imparfait": {
      "Je": "couvrais",
      "Tu": "couvrais",
      "Il/Elle/On": "couvrait",
      "Nous": "couvrions",
      "Vous": "couvriez",
      "Ils/Elle": "couvraient"
    },
    "Passé Composé": {
      "Je": "ai couvert",
      "Tu": "as couvert",
      "Il/Elle/On": "a couvert",
      "Nous": "avons couvert",
      "Vous": "avez couvert",
      "Ils/Elle": "ont couvert"
    },
    "Futur": {
      "Je": "couvrirai",
      "Tu": "couvriras",
      "Il/Elle/On": "couvrira",
      "Nous": "couvrirons",
      "Vous": "couvrirez",
      "Ils/Elle": "couvriront"
    },
    "Plus-que-parfait": {
      "Je": "avais couvert",
      "Tu": "avais couvert",
      "Il/Elle/On": "avait couvert",
      "Nous": "avions couvert",
      "Vous": "aviez couvert",
      "Ils/Elle": "avaient couvert"
    },
    "Futur Simple": {
      "Je": "couvrirai",
      "Tu": "couvriras",
      "Il/Elle/On": "couvrira",
      "Nous": "couvrirons",
      "Vous": "couvrirez",
      "Ils/Elle": "couvriront"
    },
    "Futur Antérieur": {
      "Je": "aurai couvert",
      "Tu": "auras couvert",
      "Il/Elle/On": "aura couvert",
      "Nous": "aurons couvert",
      "Vous": "aurez couvert",
      "Ils/Elle": "auront couvert"
    },
    "Conditionnel Présent": {
      "Je": "couvrirais",
      "Tu": "couvrirais",
      "Il/Elle/On": "couvrirait",
      "Nous": "couvririons",
      "Vous": "couvririez",
      "Ils/Elle": "couvriraient"
    },
    "Conditionnel Passé": {
      "Je": "aurais couvert",
      "Tu": "aurais couvert",
      "Il/Elle/On": "aurait couvert",
      "Nous": "aurions couvert",
      "Vous": "auriez couvert",
      "Ils/Elle": "auraient couvert"
    },
    "Subjonctif Présent": {
      "Je": "couvre",
      "Tu": "couvres",
      "Il/Elle/On": "couvre",
      "Nous": "couvrions",
      "Vous": "couvriez",
      "Ils/Elle": "couvrent"
    },
    "Subjonctif Passé": {
      "Je": "aie couvert",
      "Tu": "aies couvert",
      "Il/Elle/On": "ait couvert",
      "Nous": "ayons couvert",
      "Vous": "ayez couvert",
      "Ils/Elle": "aient couvert"
    },
    "Subjonctif Plus-que-parfait": {
      "Je": "eusse couvert",
      "Tu": "eusses couvert",
      "Il/Elle/On": "eût couvert",
      "Nous": "eussions couvert",
      "Vous": "eussiez couvert",
      "Ils/Elle": "eussent couvert"
    },
    "Subjonctif Imparfait": {
      "Je": "couvrisse",
      "Tu": "couvrisses",
      "Il/Elle/On": "couvrît",
      "Nous": "couvrissions",
      "Vous": "couvrissiez",
      "Ils/Elle": "couvrissent"
    },
    "Impératif Présent": {
      "Tu": "couvre",
      "Nous": "couvrons",
      "Vous": "couvrez"
    },
    "Impératif Passé": {
      "Tu": "aie couvert",
      "Nous": "ayons couvert",
      "Vous": "ayez couvert"
    },
    "Infinitif Présent": "couvrir",
    "Infinitif Passé": "avoir couvert",
    "Participe Présent": "couvrant",
    "Participe Passé": "couvert",
    "Gérondif Présent": "en couvrant",
    "Gérondif Passé": "en ayant couvert"
}}

    return conjugations.get(verb.lower(), {}).get(tense, None)    

def main():
    print("Hello! I am your Verb Conjugation chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        verb = user_input.lower()
        tense = input("Enter the tense (e.g., 'Indicative Present', 'Subjunctive Present'): ")
        verb_conjugation = conjugate_verbs(verb, tense)
        if verb_conjugation:
            print("Conjugation:")
            for pronoun, conjugated_verb in verb_conjugation.items():
                print(f"{pronoun} {conjugated_verb}")
        else:
            print("No conjugation data available for the given verb and tense.")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        verb = user_input.lower()
        tense = request.form.get("tense", "")

        verb_conjugation = conjugate_verbs(verb, tense)
        if verb_conjugation:
            conjugation_results = []
            for pronoun, conjugated_verb in verb_conjugation.items():
                conjugation_results.append(f"{pronoun} {conjugated_verb}")
        else:
            conjugation_results = ["No conjugation data available for the given verb and tense."]

        return render_template("index.html", conjugation_results=conjugation_results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
