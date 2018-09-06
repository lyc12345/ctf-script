#!/home/ubuntu/SageMath/sage

M = 2^521-1
A = M-3
B = 0x51953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00
E = EllipticCurve(GF(M),[A,B])

g = E(5405424750907042817849523452244787490362599682385950687385382709003948286406876796594535643748818283262121138737076141597966012285810985633370824005103944416, 984970155278863317776905647274559677791525657478616051760985477946504010716818161185200198096532903279219172158326801022992897407628359999389646296263358663)
c1 = E(552855983191477065625173490798701617711704046550323641029043197505267412733020855489986706517083352349729506878848234582442903346393633912672334490115627032, 4448288254968185929975292935301106070977300148734716422986283428819999541940872803146014484885544656926366780738305965546200127900163602523408778848349228434)
c2 = E(1172894324150563774663811643608960517627766591027738626927811162713249354115380380370221946441154957962746746084983424309132270981703866563921333244571945068, 1326862342442789403618364073625262255428404701645852537809124740716613376400513445402466174855564161338377255072099047633392029230168238302039238121549772049)

v = 9384757913109791206432099854903467361937642653999980200734089504250831957794906590642748355314391346715210803028085802723918238142980155591464724209887858
assert g*v == c1

pk = E(4892656645518573331106701586397878976390433610692116750215231364193992297525681417236426633145141081722252828121588677507009668068565040851265421535903327698, 445589854414539227925716617203051677345304928733141270115246729820043468361633813613863577404936314503047208205373086044049612015283264631681675748037596649)

plain = c2 - (pk*v)

ans = int(plain[0])
print hex(ans)[2:-1].decode('hex')
#SCTF{Ev3r_get_th4t_feelin9_of_dejavu_L0LOL}