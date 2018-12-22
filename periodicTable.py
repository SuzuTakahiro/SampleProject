from tkinter import *
from tkinter import ttk

Atoms ={
"H":(1,"水素",1.00794),"He":(2,"ヘリウム",4.002602),"Li":(3,"リチウム",6.941),"Be":(4,"ベリリウム",9.012182),"B":(5,"ホウ素",10.811)
,"C":(6,"炭素",12.0107),"N":(7,"窒素",14.00674),"O":(8,"酸素",15.9994),"F":(9,"フッ素",18.9984032),"Ne":(10,"ネオン",20.1797),"Na":(11,"ナトリウム",22.989770)
,"Mg":(12,"マグネシウム",24.3050),"Al":(13,"アルミニウム",26.981538),"Si":(14,"ケイ素",28.0855),"P":(15,"リン",30.973761),"S":(16,"硫黄",32.066)
,"Cl":(17,"塩素",35.453),"Ar":(18,"アルゴン",39.948),"K":(19,"カリウム",39.0983),"Ca":(20,"カルシウム",40.078),"Sc":(21,"スカンジウム",44.955910),
"Ti":(22,"チタン",47.867),"V":(23,"バナジウム",50.9415),"Cr":(24,"クロム",51.9961),"Mn":(25,"マンガン",54.938049),"Fe":(26,"鉄",55.8457),
"Co":(27,"コバルト",58.933200),"Ni":(28,"ニッケル",58.6934),"Cu":(29,"銅",63.546),"Zn":(30,"亜鉛",65.409),"Ga":(31,"ガリウム",69.723)
,"Ge":(32,"ゲルマニウム",72.64),"As":(33,"ヒ素",74.92160),"Se":(34,"セレン",78.96),"Br":(35,"臭素",79.904),"Kr":(36,"クリプトン",83.798),
"Rb":(37,"ルビジウム",85.4678),"Sr":(38,"ストロンチウム",87.62),"Y":(39,"イットリウム",88.90585),"Zr":(40,"ジルコニウム",91.224)
,"Nb":(41,"ニオブ",92.90638),"Mo":(42,"モリブデン",95.94),"Tc":(43,"テクネチウム",98),"Ru":(44,"ルテニウム",101.07),
"Rh":(45,"ロジウム",102.90550),"Pd":(46,"パラジウム",106.42),"Ag":(47,"銀",107.8682),"Cd":(48,"カドミウム",112.411),
"In":(49,"インジウム",114.818),"Sn":(50,"スズ",118.710),"Sb":(51,"アンチモン",121.760),"Te":(52,"テルル",127.60)
,"I":(53,"ヨウ素",126.90447),"Xe":(54,"キセノン",131.293),"Cs":(55,"セシウム",132.90545),"Ba":(56,"バリウム",137.327)
,"La":(57,"ランタン",138.9055),"Ce":(58,"セリウム",140.116),"Pr":(59,"プラセオジム",140.90765),"Nd":(60,"ネオジム",144.24),
"Pm":(61,"プロメチウム",145),"Sm":(62,"サマリウム",150.36),"Eu":(63,"ユウロピウム",151.964),
"Gd":(64,"ガドリニウム",157.25),"Tb":(65,"テルビウム",158.92534),"Dy":(66,"ジスプロシウム",162.500),"Ho":(67,"ホルミウム",164.93032)
,"Er":(68,"エルビウム",167.93032),"Tm":(69,"ツリウム",168.93421),"Yb":(70,"イッテルビウム",173.04),"Lu":(71,"ルテチウム",174.967)
,"Hf":(72,"ハフニウム",178.49),"Ta":(73,"タンタル",180.9479),"W":(74,"タングステン",183,84),"Re":(75,"レニウム",186.207),
"Os":(76,"オスミウム",190.23),"Ir":(77,"イリジウム",192.217),"Pt":(78,"プラチナ（白金）",195.078),"Au":(79,"金",196.96655),"Hg":(80,"水銀",200.59)
,"Tl":(81,"タリウム",204.3833),"Pb":(82,"鉛",207.2),"Bi":(83,"ビスマス",208.98038),"Po":(84,"ポロニウム",209),"At":(85,"アスタチン",210)
,"Rn":(86,"ラドン",222),"Fr":(87,"フランシウム",223),"Ra":(88,"ラジウム",226),"Ac":(89,"アクチニウム",227),
"Th":(90,"トリウム",232.0381),"Pa":(91,"プロトアクチニウム",231.03588),"U":(92,"ウラン",238.02891),"Np":(93,"ネプツニウム",237)
,"Pu":(94,"プルトニウム",244),"Am":(95,"アメリシウム",243),"Cm":(96,"キュリウム",247),"Bk":(97,"バークリウム",247),
"Cf":(98,"カリホルニウム",251),"Es":(99,"アインスタイニウム",252),"Fm":(100,"フェルミウム",257,),"Md":(101,"メンデレビウム",258)
,"No":(102,"ノーベリウム",259),"Lr":(103,"ローレンシウム",262),"Rf":(104,"ラザホージウム",261),"Db":(105,"ドブニウム",262),"Sg":(106,"シーボーギウム",266)
,"Bh":(107,"ボーリウム",264),"Hs":(108,"ハッシウム",269),"Mt":(109,"マイトネリウム",268),"Ds":(110,"ダームスタチウム",271),"Rg":(111,"レントゲニウム",272)
# ,"Uub":(112,"ウンウンビウム",285),"Uut":(113,"ウンウントリウム",284),"Uuq":(114,"ウンウンアジウム",289),"Uup":(115,"ウンウンペチウム",288),"Uuh":(116,"ウンウンヘキシウム",292)
,"Uus":(117,"ウンウンヘキシウム",)
,"Cn":(112,"コペルニシウム",285),"Nh":(113,"ニホニウム",286),"Fl":(114,"フレロビウム",289),"Mc":(115,"モスコビウム",290),"Lv":(116,"リバモリウム",293)
,"Ts":(117,"テネシン",294),"Og":(118,"オガネソン",294)}
HorizontalDict=[
{1:"H",18:"He"},
{1:"Li",2:"Be",13:"B",14:"C",15:"N",16:"O",17:"F",18:"Ne"},
{1:"Na",2:"Mg",13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar"},
{1:"K",2:"Ca",3:"Sc",4:"Tl",5:"V",6:"Cr",7:"Mn",8:"Fe",
9:"Co",10:"Ni",11:"Cu",12:"Zn",13:"Ga",14:"Ge",15:"As",16:"Se",17:"Br",18:"Kr"},
{1:"Rb",2:"Sr",3:"Y",4:"Zr",5:"Nb",6:"Mo",7:"Tc",8:"Ru",
9:"Rh",10:"Pd",11:"Ag",12:"Cd",13:"In",14:"Sn",15:"Sb",16:"Te",17:"I",18:"Xe"},
{1:"Cs",2:"Ba",4:"Hf",5:"Ta",6:"W",7:"Re",8:"Os",
9:"Ir",10:"Pt",11:"Au",12:"Hg",13:"Tl",14:"Pb",15:"Bi",16:"Po",17:"At",18:"Rn"},
{1:"Fr",2:"Ra",4:"Rf",5:"Db",6:"Sg",7:"Bh",8:"Hs",
9:"Mt",10:"Ds",11:"Rg",12:"Cn",13:"Nh",14:"Fl",15:"Mc",16:"Lv",17:"Ts",18:"Og"},
{},
{4:"La",5:"Ce",6:"Pr",7:"Nd",8:"Pm",
9:"Sm",10:"Eu",11:"Gd",12:"Tb",13:"Dy",14:"Ho",15:"Er",16:"Tm",17:"Yb",18:"Lu"},
{4:"Ac",5:"Ta",6:"Pa",7:"U",8:"Np",
9:"Pu",10:"Am",11:"Cm",12:"Bk",13:"Cf",14:"Es",15:"Fm",16:"Md",17:"No",18:"Lr"}
]
class PeriodicTable(ttk.Frame):

    def __init__(self,master,number,symbol,name,mass):
        super().__init__(master,borderwidth=5)
        # self.grid(column=0, row=1, sticky=(N, W, E, S))
        self.pack(side="bottom")
        self.number =number
        self.symbol =symbol
        self.name  = name
        self.mass = mass
        self.create_widgets(number,name,mass)

    def create_widgets(self,name,number,mass):
        for vr in range(0,10):
            for hr in range(0,18):
                name = HorizontalDict[vr].get(hr+1)
                if name is None:
                    label = ttk.Label(self)
                    label.grid(column=hr,row=vr,sticky=(N, W, E, S))
                else:
                    button = ttk.Button(self,text=name)
                    button.bind("<Button-1>",self.selectAtom)
                    button.grid(column=hr,row=vr,sticky=(N, W, E, S))
    def selectAtom(self,event):
        symname =event.widget["text"]
        print(symname)
        print(Atoms.get(symname))
        number,name,mass = Atoms.get(symname)
        self.number.set(number)
        self.symbol.set(symname)
        self.name.set(name)
        self.mass.set(mass)


class PeriodicTableApp(ttk.Frame):

    def __init__(self,master):
        super().__init__(master,borderwidth=5)
        self.pack()
        self.variable()
        self.create_widgets()
    def variable(self):
        self.number = IntVar()
        self.symbol = StringVar()
        self.name = StringVar()
        self.mass = DoubleVar()



    def create_widgets(self):
        atomview = ttk.Frame(self)
        atomview.pack()

        atomNumlabel = ttk.Label(atomview,text="Number:")
        atomNumlabel.pack(side="left")
        atomNumentry = ttk.Entry(atomview,textvariable=self.number)
        atomNumentry.pack(side="left")
        atomSymlabel = ttk.Label(atomview,text="Symbol:")
        atomSymlabel.pack(side="left")
        atomSymentry = ttk.Entry(atomview,textvariable=self.symbol)
        atomSymentry.pack(side="left")
        label = ttk.Label(atomview,text="Name:")
        label.pack(side="left")
        entry = ttk.Entry(atomview,textvariable=self.name)
        entry.pack(side="left")
        volabel = ttk.Label(atomview,text="Mass:")
        volabel.pack(side="left")
        voentry = ttk.Entry(atomview,textvariable=self.mass)
        voentry.pack(side="left")

        PeriodicTable(self,self.number,self.symbol,self.name,self.mass,)





if __name__ == '__main__':
    master = Tk()
    master.title("PeriodicTable Sample")
    PeriodicTableApp(master)

    master.mainloop()
