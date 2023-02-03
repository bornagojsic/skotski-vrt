# skotski-vrt
Bebi + Borna = jedan od AI-jeva za Škotski vrt ikad

U README ću pisat noteove tako da možes pogledati kad ti odgovara.
1. line 63 u game.py - jesi li siguran da ovo nije pass po referenci (ne stvara deepcopy). Točnije, treba provjeriti, kada brišeš pozicije u legal_moves na kojima su već detektivi (sljedećih par linija), brišu li se i elementi originalnog grafa. Ako odradim ostale stvari, to ću mozžda ja napraviti danas kroz dan.

2. Appendanje liste je dosta sporo, pa će to možda biti bottleneck (radi se svakim potezom u player.positions). No, optimizacija dolazi nakon što sve proradi.

3. line 83 u game.py - neće li ovo dati win detektivima svaki put, čak i ako su oni ostali bez karata? (jedini condition za Mr. X win je >= MAX_ROUNDS, a ovo prekida prije toga).

4. Lista starting_positions u player.py se isprazni nakon jedne igre, pa sam dodao bandaid fix da se svaki put popuni nazad kako bih morao runnati vise simulacija.

5. Napisao sam kod za simulaciju. Ako ga pokreneš i upišeš neki veliki broj, recimo 400 simulacija, vidjet ćes da će na nekoj nasumičnoj (možda 2., možda 330.) simulaciji program stati i ući u neki beskonačni loop. Logično bi bilo pretpostaviti da je to posljedica loopa u liniji 21 (što ako nema niti jednog poteza?), no probao sam staviti break condition nakon nekog broja iteracija, i problem se svejedno pojavljuje. Dakle, postoji neka specifična situacija u igri koja izaziva grešku (koja se dogodi u jednoj od cca 100 simulacija). Možda je povezano sa problemom u točki 1., ali zasad nisam siguran. 
