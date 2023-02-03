# skotski-vrt
Bebi + Borna = jedan od AI-jeva za Škotski vrt ikad

U README ću pisat noteove tako da možes pogledati kad ti odgovara.
1. line 63 u game.py - jesi li siguran da ovo nije pass po referenci (ne stvara deepcopy). Točnije, treba provjeriti, kada brišeš pozicije u legal_moves na kojima su već detektivi (sljedećih par linija), brišu li se i elementi originalnog grafa. Ako odradim ostale stvari, to ću možda ja napraviti danas kroz dan.

2. Lista starting_positions u player.py se isprazni nakon jedne igre, pa sam dodao bandaid fix da se svaki put popuni nazad kako bih morao runnati vise simulacija. Taj bandaid fix izaziva da se ponekad Mister X i detektivi inicijaliziraju na istu početnu lokaciju, no to ću prepraviti kasnije, za sad mi je samo bilo bitno da mogu runnati simulaciju.

3. Napisao sam kod za simuliranje n nasumičnih igara na učitanoj mapi. Naravno, analizu vremenske efikasnosti nema smisla izvoditi na ovoliko sitnoj mapi. Kada implementiram veću mapu, provjerit ću koji su bottleneckovi (pogađam da će appendanje one liste player.positions pri svakom potezu možda biti jedan od njih?). 

4. Zašto simulacije?
Za početak, izvrstan su način da vidim ima li buggova u samoj implementaciji igre jer će se u tisućama simulacija pojaviti većina rubnih slučajevima koji izazivaju greške. Važniji je razlog, naravno, implementacija MCTS-a (bez heuristike, za početak), ali radim i na drugim RL/ML/algoritamskim metodama koje bi mogle biti dobre za ovo. Budući da sa MCTS-om već imam iskustva, a dosta je moćan,  najlakše mi je početi s tim. 

===========================================================================

1. Re: Vrlo sam siguran jer je u line 60 definiran boards koji je deepcopy

2. Re: Mozemo dodati metodu koja generira pocetne pozicije u Simulation() klasu

5. Maknuo sam inciijalizaciju boarda iz loopa u play_n_randoms u simulation.py jer se inace fileovi citaju n puta sto nije preznacajno, ali linearno raste vrijeme koje se trosi na citanje (za 100 simulacija mi je bilo 0.06s, a za 1k je bilo 0.5s)
