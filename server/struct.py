# File with various gameplay classes
from django.forms.models import model_to_dict
import MySQLdb

from server.const import *
from server.models import *

class caravan:
    path=[]
    originbase=-1
    destinationbase=-1
    faction=-1
    caravantype='none'

class constructionassist:
    path=[]
    originbase=-1
    destinationbase=-1
    faction=-1
    assisttype='none'

class unittype:
    maxhp=0
    combat=0
    category=0
    unittype=0
    light=0
    heavy=0
    natrual=0
    movement=0
    vision=0
    goldcost=0
    lumbercost=0
    oilcost=0
    mintier=0

# main class
class WarcraftServer:

    alterachome = [476, 514, 553, 554, 555, 591, 592, 593, 630, 631, 668]
    gilneashome = [20, 21, 58, 59, 60, 61, 62, 96, 97, 98, 99, 100, 101, 134, 135, 136, 137, 138, 139, 140, 172, 173,
                   174, 175, 176, 177, 178, 179, 210, 211, 212, 213, 214, 215, 216, 217, 253, 254, 255]
    silvermoonhome = [463, 464, 502, 503, 504, 540, 695, 696, 699, 700, 701, 734, 736, 738, 739, 773, 774, 775, 776,
                      777, 778, 811, 812, 813, 814, 815, 816, 849, 850, 851, 852, 853, 854, 887, 888, 889, 890, 891,
                      926, 927, 928, 929, 966, 967, 968, 1006]
    factiondictionary = {0: 'Amani', 1: 'Bleeding Hollow', 2: 'Black Tooth Grin', 3: 'Dragonmaw', 4: 'Stormreaver',
                         5: "Twilight's Hammer", 6: 'Blackrock', 7: 'Silvermoon', 8: 'Aerie Peak', 9: 'Ironforge',
                         10: 'Dalaran', 11: 'Kul Tiras', 12: 'Stromgarde', 13: 'Azeroth', 14: 'Lordaeron',
                         15: 'Gilneas', 16: 'Alterac', 17: 'Dark Iron', 18: 'Burning Blade', 19: 'Frostwolf',
                         20: 'Dalaran Rebel', 21: 'Gilnean Rebel', 22: 'Firetree', 23: 'Smolderthorn', 24: 'Shadowpine',
                         25: 'Shadowglen', 26: 'Revantusk', 27: 'Mossflayer', 28: 'Witherbark', 29: 'Vilebranch',
                         30: 'Dragon', 31: 'Demon'}
    buildablelist = ['Grunt', 'Berserker', 'Axethrower', 'Ogre', 'Catapult', 'Death Knight', 'Wave Rider', 'Turtle',
                     'Juggernaut', 'Horde Transport', 'Dragon', 'Raider', 'Shaman', 'Warlock', 'Footman', 'Archer',
                     'Knight', 'Ballista', 'Mage', 'Destroyer', 'Submarine', 'Battleship', 'Alliance Transport',
                     'Gryphon', 'Dwarf', 'Swordsman', 'Wildhammer Shaman', 'Rogue', 'Skeleton', 'Demon', 'Elemental',
                     'Mountaineer']
    categorylist = [CATEGORY_EXTERIOR_SIEGE, CATEGORY_RANGED, CATEGORY_EXPERT, CATEGORY_MELEE, CATEGORY_INTERIOR_SIEGE,
                    CATEGORY_NO_FIRE]

    def __init__(self):
        self.allfactions = []
        self.FOOD_SURPLUS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.FOOD_SURPLUS_AFTER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0]
        self.allunits = []
        self.allcurrentfaction = []
        self.allorders = []
        self.allspecialorders = []
        self.hexsidelimitchecks = []
        self.airlimitchecks = []
        self.allhexes = []
        self.allroads = []
        self.allbases = []
        self.allexpandables = []
        self.allcaravans = []
        self.allpotentialexpansionsreceived = []
        self.allbuildables = []
        self.basebuildorders = []
        self.expansionorders = []
        self.successfulexpansionorders = []
        self.alleconomicactions = []
        self.unitslegend = []
        self.baseslegend = []
        self.currentinitiative = []
        self.basenames = []
        self.unitstogainvet = []
        self.specialevents = []

        # TO BE REMOVED
        # DATABASE VARIABLES
        self.host_var = "warcraft-db.cvs4kmdmsx2d.us-east-1.rds.amazonaws.com"
        self.port_var = 3306
        self.user_var = "wcadmin"
        self.passwd_var = "sythegar"
        self.db_var = "warcraft"

        self.allstats={'Grunt':unittype(),'Berserker':unittype(),'Axethrower':unittype(),'Ogre':unittype(),'Catapult':unittype(),'Death Knight':unittype(),'Wave Rider':unittype(),'Turtle':unittype(),'Juggernaut':unittype(),
                       'Horde Transport':unittype(),'Dragon':unittype(),'Raider':unittype(),'Shaman':unittype(),'Warlock':unittype(),'Footman':unittype(),'Archer':unittype(),'Knight':unittype(),'Ballista':unittype(),
                       'Mage':unittype(),'Destroyer':unittype(),'Submarine':unittype(),'Battleship':unittype(),'Alliance Transport':unittype(),'Gryphon':unittype(),'Dwarf':unittype(),'Swordsman':unittype(),
                       'Wildhammer Shaman':unittype(),'Rogue':unittype(),'Skeleton':unittype(),'Demon':unittype(),'Elemental':unittype(),'Mountaineer':unittype(),"Zul'jin":unittype(),'Kilrogg Deadeye':unittype(),
                       'Rend Blackhand':unittype(),'Maim Blackhand':unittype(),'Zuluhed the Whacked':unittype(),"Gul'dan the Deceiver":unittype(),"Cho'gall":unittype(),'Orgrim Doomhammer':unittype(),
                       'Varok Saurfang':unittype(),'Alleria Windrunner':unittype(),'Sylvanas Windrunner':unittype(),'Kurdran Wildhammer':unittype(),'Maz Drachrip':unittype(),'Magni Bronzebeard':unittype(),
                       'Muradin Bronzebeard':unittype(),'Archmage Antonidas':unittype(),'Archmage Khadgar':unittype(),'Daelin Proudmoore':unittype(),'Derek Proudmoore':unittype(),'Thoras Trollbane':unittype(),
                       'Danath Trollbane':unittype(),'Anduin Lothar':unittype(),'Turalyon':unittype(),'Uther the Lightbringer':unittype(),'Terenas Menethil':unittype(),'Genn Greymane':unittype(),'Darius Crowley':unittype(),
                       'Aiden Perenolde':unittype(),'Lord Falconcrest':unittype(),'Dagran Thaurissan':unittype(),"Drek'thar":unittype(),'Nazgrel':unittype(),'Alexstrasza':unittype(),"Drak'thul":unittype(),'Gorfrunch Smashblade':unittype()}



    # load functions

    # TO BE REMOVED
    def load_db(self):
        return MySQLdb.connect(host=self.host_var,
                               user=self.user_var,
                               passwd=self.passwd_var,
                               db=self.db_var)

    def loadbasenames(self):
        data = Basenames.objects.all()
        for x in data:
            self.basenames.append([x.basename, x.faction, x.used])

    def loadcurrentfaction(self):
        f_data = Currentfaction.objects.all()
        self.allcurrentfaction.append(f_data[0].current_faction)

    def loadcurrentinitiative(self):
        i_data = Currentinitiative.objects.all()
        self.currentinitiative.append(i_data[0].current_initiative)

    def loadcaravans(self):
        c_data = Currentcaravans.objects.all()
        for x in c_data:
            newcaravan = caravan()
            newcaravan.path = []
            newcaravan.originbase = x.originbase
            newcaravan.destinationbase = int(x.destinationbase)
            newcaravan.faction = int(x.faction)
            newcaravan.caravantype = x.caravantype
            for k, v in model_to_dict(x).items():
                if 'col' in k:
                    if v is not None:
                        newcaravan.path.append(int(v))
            self.allcaravans.append(newcaravan)

    def get_unit_base(self, unit_type):
        unit_class = self.allstats[unit_type]
        return [unit_type, unit_class.maxhp, unit_class.combat, unit_class.category, unit_class.type,
                unit_class.light, unit_class.heavy, unit_class.natural,
                unit_class.movement, unit_class.vision]

    def loadunits(self, load_type):
        us_data = Unitstats.objects.all()
        for x in us_data:
            self.allstats[x.name].maxhp = x.max_hp
            self.allstats[x.name].combat = x.combat
            self.allstats[x.name].category = x.category
            self.allstats[x.name].type = x.type
            self.allstats[x.name].light = x.light_armor
            self.allstats[x.name].heavy = x.heavy_armor
            self.allstats[x.name].natural = x.natural_armor
            self.allstats[x.name].movement = x.movement
            self.allstats[x.name].vision = x.vision
            self.allstats[x.name].goldcost = x.gold_cost
            self.allstats[x.name].lumbercost = x.lumber_cost
            self.allstats[x.name].oilcost = x.oil_cost
            self.allstats[x.name].mintier = x.min_tier

        if load_type == 'saved':
            u_data = Saveunits.objects.all()
        else:
            u_data = Unitdata.objects.all()
        for x in u_data:
            u = self.get_unit_base(x.name)
            u += [x.faction, x.hit_points, x.location, x.tier, x.tier_1, x.tier_2, x.tier_3, x.tier_4, x.alive]
            if load_type == 'saved':
                u += [x.col_1, x.col_2, x.col_3, x.col_4, x.col_5, x.col_6, x.col_7, x.col_8, x.col_9, x.col_10,
                      x.col_11, x.col_12, x.col_13, x.col_14, x.col_15, x.col_16, x.col_17, x.col_18, x.col_19]
            else:
                for y in range(19):
                    u.append(0)
            u[UNIT_MAX_HIT_POINTS] += u[UNIT_TIER] # tier adds extra HP
            if u[UNIT_CATEGORY] != CATEGORY_NO_FIRE:
                u[UNIT_COMBAT] += (u[UNIT_TIER]*5) # remove this when we get real vets
            if x.name == 'Alexstrasza': # jim: im reworking this dragon approach
                if self.allbuildables[FACTION_DRAGONMAW][FACTION_DATA_DRAGON-1]==3: # why -1 here?
                    u[UNIT_FACTION] = FACTION_DRAGONMAW
                    u[UNIT_CATEGORY] = CATEGORY_NO_FIRE
                    u[UNIT_MOVEMENT_MAX] = 0
                    u[UNIT_MOVEMENT_REMAINING] = 0
                else:
                    u[UNIT_FACTION] = FACTION_DRAGON
                    u[UNIT_CATEGORY] = CATEGORY_RANGED
                    u[UNIT_MOVEMENT_MAX] = 2
                    u[UNIT_MOVEMENT_REMAINING] = 2
            self.allunits.append(u)

    def loadorders(self):
        o_data = Orders.objects.all()
        for x in o_data:
            new_order = list(filter(None, [x.unit, x.first_move, x.second_move, x.third_move]))
            self.allorders.append(new_order)

    def loadspecialorders(self):
        so_data = Specialorders.objects.all()
        for x in so_data:
            new_special_order = list(filter(None, [x.action, x.unit, x.data_1, x.data_2, x.data_3]))
            self.allspecialorders.append(new_special_order)

    def loadeconomicactions(self):
        e_data = Economicactions.objects.all()
        for x in e_data:
            new_e_action = []
            for k, v in model_to_dict(x).items():
                new_e_action.append(v)  # jim question: this can handle Nones, right?
            self.alleconomicactions.append(new_e_action)

    def loadbuildables(self, load_type):
        if load_type == 'saved':
            b_data = Savebuildables.objects.all()
        elif load_type == 'current':
            b_data = Currentbuildables.objects.all()
        else:
            b_data = Buildables.objects.all()
        for x in b_data:
            new_buildable = []
            for k, v in model_to_dict(x).items():
                new_buildable.append(v)
            self.allbuildables.append(new_buildable)
            if load_type == 'current':
                break  # jim question: load current is only supposed to load the first one?

    def loadmap(self, load_type):
        if load_type == 'saved':
            m_data = Savehexes.objects.all()
        else:
            m_data = Hexdata.objects.all()
        for x in m_data:
            m = []
            for k, v in model_to_dict(x).items():
                m.append(v)
            self.allhexes.append(m)

    def loadroads(self):
        r_data = Roaddata.objects.all()
        for x in r_data:
            r = []
            for k, v in model_to_dict(x).items():
                r.append(v)
            self.allroads.append(r)

    def loadfactions(self, load_type):
        if load_type == 'saved':
            f_data = Savefactions.objects.all()
        else:
            f_data = Factiondata.objects.all()
        for x in f_data:
            f = []
            for k, v in model_to_dict(x).items():
                f.append(v)
            self.allfactions.append(f)

    def loadbases(self, load_type):
        if load_type == 'saved':
            b_data = Savebases.objects.all()
        else:
            b_data = Basedata.objects.all()
        for x in b_data:
            b = []
            for k, v in model_to_dict(x).items():
                b.append(v)
            self.allbases.append(b)

    def loadcurrentunitslegend(self):
        l_data = Currentunitslegend.objects.all()
        for x in l_data:
            self.unitslegend.append(x.units_legend)

    def loadcurrentbaseslegend(self):
        l_data = Currentbaseslegend.objects.all()
        for x in l_data:
            self.baseslegend.append(x.base_legend)

    def loadspecialevents(self):
        e_data = Specialevents.objects.all()
        for x in e_data:
            self.specialevents.append([x.event, x.status])

    def resetturns():
        db = load_db()
        cur = db.cursor()
        cur.execute(
            "UPDATE turnstatus SET COL_0=0, COL_1=0, COL_2=0, COL_3=0, COL_4=0, COL_5=0, COL_6=0, COL_7=0, COL_8=0, COL_9=0, COL_10=0, COL_11=0, COL_12=0, COL_13=0, COL_14=0, COL_15=0, COL_16=0, COL_17=0, COL_18=0, COL_19=0, COL_20=0, COL_21=0, COL_22=0, COL_23=0, COL_24=0, COL_25=0, COL_26=0, COL_27=0, COL_28=0, COL_29=0, COL_30=0, COL_31=0, COL_32=0")
        cur.close()

        db.commit()
        db.close()

    def loadinitiative(self):
        db = self.load_db()
        cur = db.cursor()
        cur.execute("UPDATE currentinitiative SET CURRENT_INITIATIVE=-1")
        cur.close()

        db.commit()
        db.close()

    def resetcaravans(self):
        db = self.load_db()
        cur = db.cursor()
        cur.execute("TRUNCATE savecaravans")
        cur.close()
        db.commit()
        db.close()

    def resetorders(self):
        db = self.load_db()

        o_cur = db.cursor()
        o_cur.execute("TRUNCATE orders")
        o_cur.close()

        e_cur = db.cursor()
        e_cur.execute("TRUNCATE economicactions")
        e_cur.close()

        s_cur = db.cursor()
        s_cur.execute("TRUNCATE specialorders")
        s_cur.close()

        db.commit()
        db.close()

    def resetbasenames(self):
        db = self.load_db()
        cur = db.cursor()
        cur.execute("UPDATE basenames SET used=0")
        cur.close()

        db.commit()
        db.close()

    def resetspecialevents(self):
        db = self.load_db()
        cur = db.cursor()
        cur.execute("UPDATE specialevents SET status=0")
        cur.close()

        db.commit()
        db.close()









