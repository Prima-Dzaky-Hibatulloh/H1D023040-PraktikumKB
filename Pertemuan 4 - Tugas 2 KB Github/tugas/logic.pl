% DATABASE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% FAKTA & ATURAN
hewan("Kucing").
hewan("Burung").
hewan("Ikan").
hewan("Ular").
hewan("Anjing").
hewan("Kuda").
hewan("Penyu").

gejala(berbulu, "Kucing").
gejala(berkaki_empat, "Kucing").
gejala(mengeong, "Kucing").

gejala(berbulu, "Burung").
gejala(bisa_terbang, "Burung").
gejala(bertelur, "Burung").

gejala(bertelur, "Ikan").
gejala(berenang, "Ikan").
gejala(berinsang, "Ikan").

gejala(merayap, "Ular").
gejala(bertelur, "Ular").

gejala(berbulu, "Anjing").
gejala(berkaki_empat, "Anjing").
gejala(menggonggong, "Anjing").

gejala(berkaki_empat, "Kuda").
gejala(berlari_cepat, "Kuda").

gejala(berenang, "Penyu").
gejala(bertelur, "Penyu").
gejala(bercangkang, "Penyu").

pertanyaan(berbulu, Y) :-
    Y = "Apakah hewan tersebut berbulu?".

pertanyaan(berkaki_empat, Y) :-
    Y = "Apakah hewan tersebut berkaki empat?".

pertanyaan(mengeong, Y) :-
    Y = "Apakah hewan tersebut mengeong?".

pertanyaan(bisa_terbang, Y) :-
    Y = "Apakah hewan tersebut bisa terbang?".

pertanyaan(bertelur, Y) :-
    Y = "Apakah hewan tersebut bertelur?".

pertanyaan(berenang, Y) :-
    Y = "Apakah hewan tersebut bisa berenang?".

pertanyaan(berinsang, Y) :-
    Y = "Apakah hewan tersebut bernafas dengan insang?".

pertanyaan(merayap, Y) :-
    Y = "Apakah hewan tersebut merayap?".

pertanyaan(menggonggong, Y) :-
    Y = "Apakah hewan tersebut menggonggong?".

pertanyaan(berlari_cepat, Y) :-
    Y = "Apakah hewan tersebut bisa berlari cepat?".

pertanyaan(bercangkang, Y) :-
    Y = "Apakah hewan tersebut memiliki cangkang?".

% ATURAN DIAGNOSA
cocok(Hewan) :-
    hewan(Hewan),
    forall(gejala(Gejala, Hewan), gejala_pos(Gejala)).

tidak_cocok(Hewan) :-
    hewan(Hewan),
    (gejala(G, Hewan), gejala_neg(G)).

diagnosa(Hewan) :-
    cocok(Hewan),
    \+ tidak_cocok(Hewan).

reset :-
    retractall(gejala_pos(_)),
    retractall(gejala_neg(_)).
