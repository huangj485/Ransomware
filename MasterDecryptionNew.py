import random
import RandomTextGenerator
import os
from random import randrange
import time

def decrypt(x, y, z):
        return pow(x, y, z)


d = 37749753240049213537661578326072416743319489912010955186385938033870610641276939518072074825904569593886488259345041442579317418606529962131572351589274051671687745904879048605880519847263625238759332104853160982714274974205942472959946281419448298353630793848986646214294982911701491713863294598565841655578475050912276489621795690412379660768225632012627210711681438454022595869674435358160448832661037984214817250721770214160570251576361779798762731515680038658309315974938514825894763168466233228203326703975578031553721095291367453751355151443319344256212241652386888514196483119499947651195455538685344202489404688869685209201960125367863836697296746055353981569007428852569015217767708263555120579074525449567338508616900596157817401295234991638478527190332339763058272424459505776489701702986129273512053711924485105205818655312541736368900324130721947743776125993498101849024778437775195500458480331550268070191408504129725126936589968733445211967455757991302892884129009681163045227071822058840177076942226537860955529818076857780681189094691239919247535295724433117489507200892209672328616546585908577134717528930512029710056618695540823680574464201802647515442809858722628257458032534251437322632122852850592275757937290464984086966531093065909377448001160759137118282523861149463444607092369066792901237760717243940559235491903884345386574891040628275139003428396757272129030366023951092558900876768065389202995401967839710865469745655920695762648267318073449329572364402416077926016655016834141458089582915118177410444994985325726990948995787420511431556331555006589759925928747294288300795088833803183131242022483191525351841220368552750015131525248629198132182662602157278589096277520693788630983604930116995998434581768289048347497751243334630113267392074797831976018533492853891180628830538815914242414437655926312595162831032347283578487286801078967083316396919121702450816560485856660809250524611695442083615692623367371377413023739713063496672806062152926288166438216271675761758418028526781105790479954490865124813411760650689692463841950655248177
n = 253406286806627605000279305413889990382764458707719140638141475051293476349213027265788135600256865458828104174198092904058253166364452947681743030431860444986930226709828762520085181730012927099515553431912487076118553619229217643180989393156446085137959780444641793807871586098963501224158428567674850412951604979170118232135985267085539877882536438104225085364280081118639646165200601256556523112373906214430654323522754739879267907155589671481257106969489162506362556698714068026699282369330280352018992338261544346403382097932023846819887591943134268618189253423382107196035533565775690793444286555241360544765760021965846518024056205698421823786821350632974893996521547138258276178105325869979712935655758925360510482354380248939350509954503292739011291249903774562281061137130249930739074107200855699903663230399977500755273708206293944116421237586307926793388914189888876460057042351374883490069387021285457186944006876487738978187370355514063183110841750637715629514202899464752893070429786158988905571193557370868938091659514217460042906213454707033473256394265403563872271285721575954279701688131427155203132754664563024686310968303235811502862545116012544861004387452962725189265941091476146009007952882622339740011925531428821773259127278113031956940165167721583884154912083076064429445928321066120071183139315299424722787550324494001146962770238284650526204613952940385077574700960512091932320916458077443332370209221153492097235749693225281661728135421787520848259180851609372838719289712599037043191174910869544104921095373575109453561135125891425291195065067744273563011774907163361905471330237989917601827893251363194907489102268770585302223791032496069831644291512716301592423091571568981679798323928173338170095858631274413215190009590438835754171812882903823551746082157769432708014985882540406922362728581310121786146691003697346323001269963677227732497692099532774992583651865462304845655492109706631147371932840235763935481648542919508641070966122037846118789467261386535488613308760746878912953470391405370009214311962644922048298166498697543919

toDecrypt = int(input())
decryptedKey = str(decrypt(toDecrypt, d, n))
decryptedKeyDoc = open("decryptedKey.txt", "w+")
decryptedKeyDoc.write(decryptedKey)
decryptedKeyDoc.close()
print(decryptedKey)
time.sleep(7)