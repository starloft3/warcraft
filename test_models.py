# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Basedata(models.Model):
    base_name = models.CharField(db_column='BASE_NAME', max_length=30)  # Field name made lowercase.
    base_hex = models.IntegerField(db_column='BASE_HEX', blank=True, null=True)  # Field name made lowercase.
    base_faction = models.IntegerField(db_column='BASE_FACTION', blank=True, null=True)  # Field name made lowercase.
    base_tier = models.IntegerField(db_column='BASE_TIER', blank=True, null=True)  # Field name made lowercase.
    base_gold = models.IntegerField(db_column='BASE_GOLD', blank=True, null=True)  # Field name made lowercase.
    base_lumber = models.IntegerField(db_column='BASE_LUMBER', blank=True, null=True)  # Field name made lowercase.
    base_oil = models.IntegerField(db_column='BASE_OIL', blank=True, null=True)  # Field name made lowercase.
    base_alive = models.IntegerField(db_column='BASE_ALIVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'basedata'


class Basenames(models.Model):
    basename = models.CharField(primary_key=True, max_length=30)
    faction = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basenames'


class Buildables(models.Model):
    grunt = models.IntegerField(db_column='GRUNT')  # Field name made lowercase.
    berserker = models.IntegerField(db_column='BERSERKER')  # Field name made lowercase.
    axethrower = models.IntegerField(db_column='AXETHROWER')  # Field name made lowercase.
    ogre = models.IntegerField(db_column='OGRE')  # Field name made lowercase.
    catapult = models.IntegerField(db_column='CATAPULT')  # Field name made lowercase.
    death_knight = models.IntegerField(db_column='DEATH_KNIGHT')  # Field name made lowercase.
    wave_rider = models.IntegerField(db_column='WAVE_RIDER')  # Field name made lowercase.
    turtle = models.IntegerField(db_column='TURTLE')  # Field name made lowercase.
    juggernaut = models.IntegerField(db_column='JUGGERNAUT')  # Field name made lowercase.
    horde_transport = models.IntegerField(db_column='HORDE_TRANSPORT')  # Field name made lowercase.
    dragon = models.IntegerField(db_column='DRAGON')  # Field name made lowercase.
    raider = models.IntegerField(db_column='RAIDER')  # Field name made lowercase.
    shaman = models.IntegerField(db_column='SHAMAN')  # Field name made lowercase.
    warlock = models.IntegerField(db_column='WARLOCK')  # Field name made lowercase.
    footman = models.IntegerField(db_column='FOOTMAN')  # Field name made lowercase.
    archer = models.IntegerField(db_column='ARCHER')  # Field name made lowercase.
    knight = models.IntegerField(db_column='KNIGHT')  # Field name made lowercase.
    ballista = models.IntegerField(db_column='BALLISTA')  # Field name made lowercase.
    mage = models.IntegerField(db_column='MAGE')  # Field name made lowercase.
    destroyer = models.IntegerField(db_column='DESTROYER')  # Field name made lowercase.
    submarine = models.IntegerField(db_column='SUBMARINE')  # Field name made lowercase.
    battleship = models.IntegerField(db_column='BATTLESHIP')  # Field name made lowercase.
    alliance_transport = models.IntegerField(db_column='ALLIANCE_TRANSPORT')  # Field name made lowercase.
    gryphon = models.IntegerField(db_column='GRYPHON')  # Field name made lowercase.
    dwarf = models.IntegerField(db_column='DWARF')  # Field name made lowercase.
    swordsman = models.IntegerField(db_column='SWORDSMAN')  # Field name made lowercase.
    wildhammer_shaman = models.IntegerField(db_column='WILDHAMMER_SHAMAN')  # Field name made lowercase.
    rogue = models.IntegerField(db_column='ROGUE')  # Field name made lowercase.
    skeleton = models.IntegerField(db_column='SKELETON')  # Field name made lowercase.
    demon = models.IntegerField(db_column='DEMON')  # Field name made lowercase.
    elemental = models.IntegerField(db_column='ELEMENTAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'buildables'


class Currentbases(models.Model):
    base_name = models.CharField(db_column='BASE_NAME', max_length=45)  # Field name made lowercase.
    base_hex = models.IntegerField(db_column='BASE_HEX')  # Field name made lowercase.
    base_faction = models.IntegerField(db_column='BASE_FACTION')  # Field name made lowercase.
    base_tier = models.IntegerField(db_column='BASE_TIER')  # Field name made lowercase.
    base_gold = models.IntegerField(db_column='BASE_GOLD')  # Field name made lowercase.
    base_lumber = models.IntegerField(db_column='BASE_LUMBER')  # Field name made lowercase.
    base_oil = models.IntegerField(db_column='BASE_OIL')  # Field name made lowercase.
    base_alive = models.IntegerField(db_column='BASE_ALIVE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentbases'


class Currentbaseslegend(models.Model):
    base_legend = models.IntegerField(db_column='BASE_LEGEND')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentbaseslegend'


class Currentbuildables(models.Model):
    grunt = models.IntegerField(db_column='GRUNT')  # Field name made lowercase.
    berserker = models.IntegerField(db_column='BERSERKER')  # Field name made lowercase.
    axethrower = models.IntegerField(db_column='AXETHROWER')  # Field name made lowercase.
    ogre = models.IntegerField(db_column='OGRE')  # Field name made lowercase.
    catapult = models.IntegerField(db_column='CATAPULT')  # Field name made lowercase.
    death_knight = models.IntegerField(db_column='DEATH_KNIGHT')  # Field name made lowercase.
    wave_rider = models.IntegerField(db_column='WAVE_RIDER')  # Field name made lowercase.
    turtle = models.IntegerField(db_column='TURTLE')  # Field name made lowercase.
    juggernaut = models.IntegerField(db_column='JUGGERNAUT')  # Field name made lowercase.
    horde_transport = models.IntegerField(db_column='HORDE_TRANSPORT')  # Field name made lowercase.
    dragon = models.IntegerField(db_column='DRAGON')  # Field name made lowercase.
    raider = models.IntegerField(db_column='RAIDER')  # Field name made lowercase.
    shaman = models.IntegerField(db_column='SHAMAN')  # Field name made lowercase.
    warlock = models.IntegerField(db_column='WARLOCK')  # Field name made lowercase.
    footman = models.IntegerField(db_column='FOOTMAN')  # Field name made lowercase.
    archer = models.IntegerField(db_column='ARCHER')  # Field name made lowercase.
    knight = models.IntegerField(db_column='KNIGHT')  # Field name made lowercase.
    ballista = models.IntegerField(db_column='BALLISTA')  # Field name made lowercase.
    mage = models.IntegerField(db_column='MAGE')  # Field name made lowercase.
    destroyer = models.IntegerField(db_column='DESTROYER')  # Field name made lowercase.
    submarine = models.IntegerField(db_column='SUBMARINE')  # Field name made lowercase.
    battleship = models.IntegerField(db_column='BATTLESHIP')  # Field name made lowercase.
    alliance_transport = models.IntegerField(db_column='ALLIANCE_TRANSPORT')  # Field name made lowercase.
    gryphon = models.IntegerField(db_column='GRYPHON')  # Field name made lowercase.
    dwarf = models.IntegerField(db_column='DWARF')  # Field name made lowercase.
    swordsman = models.IntegerField(db_column='SWORDSMAN')  # Field name made lowercase.
    wildhammer_shaman = models.IntegerField(db_column='WILDHAMMER_SHAMAN')  # Field name made lowercase.
    rogue = models.IntegerField(db_column='ROGUE')  # Field name made lowercase.
    skeleton = models.IntegerField(db_column='SKELETON')  # Field name made lowercase.
    demon = models.IntegerField(db_column='DEMON')  # Field name made lowercase.
    elemental = models.IntegerField(db_column='ELEMENTAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentbuildables'


class Currentcaravans(models.Model):
    originbase = models.CharField(max_length=4)
    destinationbase = models.CharField(max_length=4)
    faction = models.CharField(max_length=4)
    caravantype = models.CharField(max_length=5)
    col_0 = models.CharField(max_length=5, blank=True, null=True)
    col_1 = models.CharField(max_length=5, blank=True, null=True)
    col_2 = models.CharField(max_length=5, blank=True, null=True)
    col_3 = models.CharField(max_length=5, blank=True, null=True)
    col_4 = models.CharField(max_length=5, blank=True, null=True)
    col_5 = models.CharField(max_length=5, blank=True, null=True)
    col_6 = models.CharField(max_length=5, blank=True, null=True)
    col_7 = models.CharField(max_length=5, blank=True, null=True)
    col_8 = models.CharField(max_length=5, blank=True, null=True)
    col_9 = models.CharField(max_length=5, blank=True, null=True)
    col_10 = models.CharField(max_length=5, blank=True, null=True)
    col_11 = models.CharField(max_length=5, blank=True, null=True)
    col_12 = models.CharField(max_length=5, blank=True, null=True)
    col_13 = models.CharField(max_length=5, blank=True, null=True)
    col_14 = models.CharField(max_length=5, blank=True, null=True)
    col_15 = models.CharField(max_length=5, blank=True, null=True)
    col_16 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currentcaravans'


class Currentfaction(models.Model):
    current_faction = models.IntegerField(db_column='CURRENT_FACTION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentfaction'


class Currenthexes(models.Model):
    hex_terrain = models.CharField(db_column='HEX_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_n_terrain = models.CharField(db_column='HEX_N_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_ne_terrain = models.CharField(db_column='HEX_NE_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_se_terrain = models.CharField(db_column='HEX_SE_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_s_terrain = models.CharField(db_column='HEX_S_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_sw_terrain = models.CharField(db_column='HEX_SW_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_nw_terrain = models.CharField(db_column='HEX_NW_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_building = models.IntegerField(db_column='HEX_BUILDING')  # Field name made lowercase.
    hex_oil = models.IntegerField(db_column='HEX_OIL')  # Field name made lowercase.
    hex_farm = models.IntegerField(db_column='HEX_FARM')  # Field name made lowercase.
    hex_mill = models.IntegerField(db_column='HEX_MILL')  # Field name made lowercase.
    hex_rig = models.IntegerField(db_column='HEX_RIG')  # Field name made lowercase.
    hex_gold = models.IntegerField(db_column='HEX_GOLD')  # Field name made lowercase.
    hex_new_combat = models.IntegerField(db_column='HEX_NEW_COMBAT')  # Field name made lowercase.
    hex_battle_fought = models.IntegerField(db_column='HEX_BATTLE_FOUGHT')  # Field name made lowercase.
    hex_n_control = models.IntegerField(db_column='HEX_N_CONTROL')  # Field name made lowercase.
    hex_ne_control = models.IntegerField(db_column='HEX_NE_CONTROL')  # Field name made lowercase.
    hex_se_control = models.IntegerField(db_column='HEX_SE_CONTROL')  # Field name made lowercase.
    hex_s_control = models.IntegerField(db_column='HEX_S_CONTROL')  # Field name made lowercase.
    hex_sw_control = models.IntegerField(db_column='HEX_SW_CONTROL')  # Field name made lowercase.
    hex_nw_control = models.IntegerField(db_column='HEX_NW_CONTROL')  # Field name made lowercase.
    field22 = models.IntegerField(db_column='FIELD22')  # Field name made lowercase.
    hex_expansion_owner = models.IntegerField(db_column='HEX_EXPANSION_OWNER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currenthexes'


class Currentinitiative(models.Model):
    current_initiative = models.IntegerField(db_column='CURRENT_INITIATIVE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentinitiative'


class Currentunits(models.Model):
    name = models.CharField(db_column='NAME', max_length=22)  # Field name made lowercase.
    faction = models.IntegerField(db_column='FACTION', blank=True, null=True)  # Field name made lowercase.
    hit_points = models.IntegerField(db_column='HIT_POINTS', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    tier = models.IntegerField(db_column='TIER', blank=True, null=True)  # Field name made lowercase.
    tier_1 = models.CharField(db_column='TIER_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_2 = models.CharField(db_column='TIER_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_3 = models.CharField(db_column='TIER_3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_4 = models.CharField(db_column='TIER_4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    alive = models.IntegerField(db_column='ALIVE', blank=True, null=True)  # Field name made lowercase.
    col_1 = models.IntegerField(db_column='COL_1', blank=True, null=True)  # Field name made lowercase.
    col_2 = models.IntegerField(db_column='COL_2', blank=True, null=True)  # Field name made lowercase.
    col_3 = models.IntegerField(db_column='COL_3', blank=True, null=True)  # Field name made lowercase.
    col_4 = models.IntegerField(db_column='COL_4', blank=True, null=True)  # Field name made lowercase.
    col_5 = models.IntegerField(db_column='COL_5', blank=True, null=True)  # Field name made lowercase.
    col_6 = models.IntegerField(db_column='COL_6', blank=True, null=True)  # Field name made lowercase.
    col_7 = models.IntegerField(db_column='COL_7', blank=True, null=True)  # Field name made lowercase.
    col_8 = models.IntegerField(db_column='COL_8', blank=True, null=True)  # Field name made lowercase.
    col_9 = models.IntegerField(db_column='COL_9', blank=True, null=True)  # Field name made lowercase.
    col_10 = models.IntegerField(db_column='COL_10', blank=True, null=True)  # Field name made lowercase.
    col_11 = models.IntegerField(db_column='COL_11', blank=True, null=True)  # Field name made lowercase.
    col_12 = models.IntegerField(db_column='COL_12', blank=True, null=True)  # Field name made lowercase.
    col_13 = models.IntegerField(db_column='COL_13', blank=True, null=True)  # Field name made lowercase.
    col_14 = models.IntegerField(db_column='COL_14', blank=True, null=True)  # Field name made lowercase.
    col_15 = models.IntegerField(db_column='COL_15', blank=True, null=True)  # Field name made lowercase.
    col_16 = models.IntegerField(db_column='COL_16', blank=True, null=True)  # Field name made lowercase.
    col_17 = models.IntegerField(db_column='COL_17', blank=True, null=True)  # Field name made lowercase.
    col_18 = models.IntegerField(db_column='COL_18', blank=True, null=True)  # Field name made lowercase.
    col_19 = models.IntegerField(db_column='COL_19', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentunits'


class Currentunitslegend(models.Model):
    units_legend = models.IntegerField(db_column='UNITS_LEGEND')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentunitslegend'


class Currentvision(models.Model):
    hex = models.IntegerField(db_column='HEX')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentvision'


class Economicactions(models.Model):
    action_type = models.CharField(max_length=25)
    base_hex = models.CharField(max_length=4)
    action_1 = models.CharField(max_length=15, blank=True, null=True)
    action_2 = models.CharField(max_length=15, blank=True, null=True)
    action_3 = models.CharField(max_length=15, blank=True, null=True)
    action_4 = models.CharField(max_length=15, blank=True, null=True)
    action_5 = models.CharField(max_length=15, blank=True, null=True)
    action_6 = models.CharField(max_length=15, blank=True, null=True)
    action_7 = models.CharField(max_length=15, blank=True, null=True)
    action_8 = models.CharField(max_length=15, blank=True, null=True)
    action_9 = models.CharField(max_length=15, blank=True, null=True)
    action_10 = models.CharField(max_length=15, blank=True, null=True)
    action_11 = models.CharField(max_length=15, blank=True, null=True)
    action_12 = models.CharField(max_length=15, blank=True, null=True)
    action_13 = models.CharField(max_length=15, blank=True, null=True)
    action_14 = models.CharField(max_length=15, blank=True, null=True)
    action_15 = models.CharField(max_length=15, blank=True, null=True)
    action_16 = models.CharField(max_length=15, blank=True, null=True)
    action_17 = models.CharField(max_length=15, blank=True, null=True)
    action_18 = models.CharField(max_length=15, blank=True, null=True)
    action_19 = models.CharField(max_length=15, blank=True, null=True)
    action_20 = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'economicactions'


class Factiondata(models.Model):
    amani = models.IntegerField(db_column='AMANI', primary_key=True)  # Field name made lowercase.
    bleeding_hollow = models.IntegerField(db_column='BLEEDING_HOLLOW', blank=True, null=True)  # Field name made lowercase.
    black_tooth_grin = models.IntegerField(db_column='BLACK_TOOTH_GRIN', blank=True, null=True)  # Field name made lowercase.
    dragonmaw = models.IntegerField(db_column='DRAGONMAW', blank=True, null=True)  # Field name made lowercase.
    stormreaver = models.IntegerField(db_column='STORMREAVER', blank=True, null=True)  # Field name made lowercase.
    twilights_hammer = models.IntegerField(db_column='TWILIGHTS_HAMMER', blank=True, null=True)  # Field name made lowercase.
    blackrock = models.IntegerField(db_column='BLACKROCK', blank=True, null=True)  # Field name made lowercase.
    silvermoon = models.IntegerField(db_column='SILVERMOON', blank=True, null=True)  # Field name made lowercase.
    aerie_peak = models.IntegerField(db_column='AERIE_PEAK', blank=True, null=True)  # Field name made lowercase.
    ironforge = models.IntegerField(db_column='IRONFORGE', blank=True, null=True)  # Field name made lowercase.
    dalaran = models.IntegerField(db_column='DALARAN', blank=True, null=True)  # Field name made lowercase.
    kul_tiras = models.IntegerField(db_column='KUL_TIRAS', blank=True, null=True)  # Field name made lowercase.
    stromgarde = models.IntegerField(db_column='STROMGARDE', blank=True, null=True)  # Field name made lowercase.
    azeroth = models.IntegerField(db_column='AZEROTH', blank=True, null=True)  # Field name made lowercase.
    lordaeron = models.IntegerField(db_column='LORDAERON', blank=True, null=True)  # Field name made lowercase.
    gilneas = models.IntegerField(db_column='GILNEAS', blank=True, null=True)  # Field name made lowercase.
    alterac = models.IntegerField(db_column='ALTERAC', blank=True, null=True)  # Field name made lowercase.
    dark_iron = models.IntegerField(db_column='DARK_IRON', blank=True, null=True)  # Field name made lowercase.
    burning_blade = models.IntegerField(db_column='BURNING_BLADE', blank=True, null=True)  # Field name made lowercase.
    frostwolf = models.IntegerField(db_column='FROSTWOLF', blank=True, null=True)  # Field name made lowercase.
    dalaran_rebel = models.IntegerField(db_column='DALARAN_REBEL', blank=True, null=True)  # Field name made lowercase.
    gilneas_rebel = models.IntegerField(db_column='GILNEAS_REBEL', blank=True, null=True)  # Field name made lowercase.
    firetree = models.IntegerField(db_column='FIRETREE', blank=True, null=True)  # Field name made lowercase.
    smolderthorn = models.IntegerField(db_column='SMOLDERTHORN', blank=True, null=True)  # Field name made lowercase.
    shadowpine = models.IntegerField(db_column='SHADOWPINE', blank=True, null=True)  # Field name made lowercase.
    shadowglen = models.IntegerField(db_column='SHADOWGLEN', blank=True, null=True)  # Field name made lowercase.
    revantusk = models.IntegerField(db_column='REVANTUSK', blank=True, null=True)  # Field name made lowercase.
    mossflayer = models.IntegerField(db_column='MOSSFLAYER', blank=True, null=True)  # Field name made lowercase.
    witherbark = models.IntegerField(db_column='WITHERBARK', blank=True, null=True)  # Field name made lowercase.
    vilebranch = models.IntegerField(db_column='VILEBRANCH', blank=True, null=True)  # Field name made lowercase.
    dragon = models.IntegerField(db_column='DRAGON', blank=True, null=True)  # Field name made lowercase.
    demon = models.IntegerField(db_column='DEMON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factiondata'


class Hexdata(models.Model):
    hex_terrain = models.CharField(db_column='HEX_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_n_terrain = models.CharField(db_column='HEX_N_TERRAIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hex_ne_terrain = models.CharField(db_column='HEX_NE_TERRAIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hex_se_terrain = models.CharField(db_column='HEX_SE_TERRAIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hex_s_terrain = models.CharField(db_column='HEX_S_TERRAIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hex_sw_terrain = models.CharField(db_column='HEX_SW_TERRAIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hex_nw_terrain = models.CharField(db_column='HEX_NW_TERRAIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hex_building = models.IntegerField(db_column='HEX_BUILDING', blank=True, null=True)  # Field name made lowercase.
    hex_oil = models.IntegerField(db_column='HEX_OIL', blank=True, null=True)  # Field name made lowercase.
    hex_farm = models.IntegerField(db_column='HEX_FARM', blank=True, null=True)  # Field name made lowercase.
    hex_mill = models.IntegerField(db_column='HEX_MILL', blank=True, null=True)  # Field name made lowercase.
    hex_rig = models.IntegerField(db_column='HEX_RIG', blank=True, null=True)  # Field name made lowercase.
    hex_gold = models.IntegerField(db_column='HEX_GOLD', blank=True, null=True)  # Field name made lowercase.
    hex_new_combat = models.IntegerField(db_column='HEX_NEW_COMBAT', blank=True, null=True)  # Field name made lowercase.
    hex_battle_fought = models.IntegerField(db_column='HEX_BATTLE_FOUGHT', blank=True, null=True)  # Field name made lowercase.
    hex_n_control = models.IntegerField(db_column='HEX_N_CONTROL', blank=True, null=True)  # Field name made lowercase.
    hex_ne_control = models.IntegerField(db_column='HEX_NE_CONTROL', blank=True, null=True)  # Field name made lowercase.
    hex_se_control = models.IntegerField(db_column='HEX_SE_CONTROL', blank=True, null=True)  # Field name made lowercase.
    hex_s_control = models.IntegerField(db_column='HEX_S_CONTROL', blank=True, null=True)  # Field name made lowercase.
    hex_sw_control = models.IntegerField(db_column='HEX_SW_CONTROL', blank=True, null=True)  # Field name made lowercase.
    hex_nw_control = models.IntegerField(db_column='HEX_NW_CONTROL', blank=True, null=True)  # Field name made lowercase.
    field22 = models.IntegerField(db_column='FIELD22', blank=True, null=True)  # Field name made lowercase.
    hex_expansion_owner = models.IntegerField(db_column='HEX_EXPANSION_OWNER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hexdata'


class Orders(models.Model):
    unit = models.IntegerField()
    first_move = models.IntegerField(blank=True, null=True)
    second_move = models.IntegerField(blank=True, null=True)
    third_move = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Playerdata(models.Model):
    password = models.CharField(max_length=18)
    faction = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playerdata'


class Roaddata(models.Model):
    road_hex = models.IntegerField(db_column='ROAD_HEX')  # Field name made lowercase.
    road_n = models.IntegerField(db_column='ROAD_N', blank=True, null=True)  # Field name made lowercase.
    road_ne = models.IntegerField(db_column='ROAD_NE', blank=True, null=True)  # Field name made lowercase.
    road_se = models.IntegerField(db_column='ROAD_SE', blank=True, null=True)  # Field name made lowercase.
    road_s = models.IntegerField(db_column='ROAD_S', blank=True, null=True)  # Field name made lowercase.
    road_sw = models.IntegerField(db_column='ROAD_SW', blank=True, null=True)  # Field name made lowercase.
    road_nw = models.IntegerField(db_column='ROAD_NW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roaddata'


class Savebases(models.Model):
    base_name = models.CharField(db_column='BASE_NAME', max_length=21)  # Field name made lowercase.
    base_hex = models.IntegerField(db_column='BASE_HEX', blank=True, null=True)  # Field name made lowercase.
    base_faction = models.IntegerField(db_column='BASE_FACTION', blank=True, null=True)  # Field name made lowercase.
    base_tier = models.IntegerField(db_column='BASE_TIER', blank=True, null=True)  # Field name made lowercase.
    base_gold = models.IntegerField(db_column='BASE_GOLD', blank=True, null=True)  # Field name made lowercase.
    base_lumber = models.IntegerField(db_column='BASE_LUMBER', blank=True, null=True)  # Field name made lowercase.
    base_oil = models.IntegerField(db_column='BASE_OIL', blank=True, null=True)  # Field name made lowercase.
    base_alive = models.IntegerField(db_column='BASE_ALIVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'savebases'


class Savebuildables(models.Model):
    grunt = models.IntegerField(db_column='GRUNT')  # Field name made lowercase.
    berserker = models.IntegerField(db_column='BERSERKER', blank=True, null=True)  # Field name made lowercase.
    axethrower = models.IntegerField(db_column='AXETHROWER', blank=True, null=True)  # Field name made lowercase.
    ogre = models.IntegerField(db_column='OGRE', blank=True, null=True)  # Field name made lowercase.
    catapult = models.IntegerField(db_column='CATAPULT', blank=True, null=True)  # Field name made lowercase.
    death_knight = models.IntegerField(db_column='DEATH_KNIGHT', blank=True, null=True)  # Field name made lowercase.
    wave_rider = models.IntegerField(db_column='WAVE_RIDER', blank=True, null=True)  # Field name made lowercase.
    turtle = models.IntegerField(db_column='TURTLE', blank=True, null=True)  # Field name made lowercase.
    juggernaut = models.IntegerField(db_column='JUGGERNAUT', blank=True, null=True)  # Field name made lowercase.
    horde_transport = models.IntegerField(db_column='HORDE_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    dragon = models.IntegerField(db_column='DRAGON', blank=True, null=True)  # Field name made lowercase.
    raider = models.IntegerField(db_column='RAIDER', blank=True, null=True)  # Field name made lowercase.
    shaman = models.IntegerField(db_column='SHAMAN', blank=True, null=True)  # Field name made lowercase.
    warlock = models.IntegerField(db_column='WARLOCK', blank=True, null=True)  # Field name made lowercase.
    footman = models.IntegerField(db_column='FOOTMAN', blank=True, null=True)  # Field name made lowercase.
    archer = models.IntegerField(db_column='ARCHER', blank=True, null=True)  # Field name made lowercase.
    knight = models.IntegerField(db_column='KNIGHT', blank=True, null=True)  # Field name made lowercase.
    ballista = models.IntegerField(db_column='BALLISTA', blank=True, null=True)  # Field name made lowercase.
    mage = models.IntegerField(db_column='MAGE', blank=True, null=True)  # Field name made lowercase.
    destroyer = models.IntegerField(db_column='DESTROYER', blank=True, null=True)  # Field name made lowercase.
    submarine = models.IntegerField(db_column='SUBMARINE', blank=True, null=True)  # Field name made lowercase.
    battleship = models.IntegerField(db_column='BATTLESHIP', blank=True, null=True)  # Field name made lowercase.
    alliance_transport = models.IntegerField(db_column='ALLIANCE_TRANSPORT', blank=True, null=True)  # Field name made lowercase.
    gryphon = models.IntegerField(db_column='GRYPHON', blank=True, null=True)  # Field name made lowercase.
    dwarf = models.IntegerField(db_column='DWARF', blank=True, null=True)  # Field name made lowercase.
    swordsman = models.IntegerField(db_column='SWORDSMAN', blank=True, null=True)  # Field name made lowercase.
    wildhammer_shaman = models.IntegerField(db_column='WILDHAMMER_SHAMAN', blank=True, null=True)  # Field name made lowercase.
    rogue = models.IntegerField(db_column='ROGUE', blank=True, null=True)  # Field name made lowercase.
    skeleton = models.IntegerField(db_column='SKELETON', blank=True, null=True)  # Field name made lowercase.
    demon = models.IntegerField(db_column='DEMON', blank=True, null=True)  # Field name made lowercase.
    elemental = models.IntegerField(db_column='ELEMENTAL', blank=True, null=True)  # Field name made lowercase.
    mountaineer = models.IntegerField(db_column='MOUNTAINEER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'savebuildables'


class Savecaravans(models.Model):
    originbase = models.CharField(max_length=4)
    destinationbase = models.CharField(max_length=4)
    faction = models.CharField(max_length=4)
    caravantype = models.CharField(max_length=5)
    col_0 = models.CharField(max_length=5, blank=True, null=True)
    col_1 = models.CharField(max_length=5, blank=True, null=True)
    col_2 = models.CharField(max_length=5, blank=True, null=True)
    col_3 = models.CharField(max_length=5, blank=True, null=True)
    col_4 = models.CharField(max_length=5, blank=True, null=True)
    col_5 = models.CharField(max_length=5, blank=True, null=True)
    col_6 = models.CharField(max_length=5, blank=True, null=True)
    col_7 = models.CharField(max_length=5, blank=True, null=True)
    col_8 = models.CharField(max_length=5, blank=True, null=True)
    col_9 = models.CharField(max_length=5, blank=True, null=True)
    col_10 = models.CharField(max_length=5, blank=True, null=True)
    col_11 = models.CharField(max_length=5, blank=True, null=True)
    col_12 = models.CharField(max_length=5, blank=True, null=True)
    col_13 = models.CharField(max_length=5, blank=True, null=True)
    col_14 = models.CharField(max_length=5, blank=True, null=True)
    col_15 = models.CharField(max_length=5, blank=True, null=True)
    col_16 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'savecaravans'


class Savefactions(models.Model):
    amani = models.IntegerField(db_column='AMANI')  # Field name made lowercase.
    bleeding_hollow = models.IntegerField(db_column='BLEEDING_HOLLOW', blank=True, null=True)  # Field name made lowercase.
    black_tooth_grin = models.IntegerField(db_column='BLACK_TOOTH_GRIN', blank=True, null=True)  # Field name made lowercase.
    dragonmaw = models.IntegerField(db_column='DRAGONMAW', blank=True, null=True)  # Field name made lowercase.
    stormreaver = models.IntegerField(db_column='STORMREAVER', blank=True, null=True)  # Field name made lowercase.
    twilights_hammer = models.IntegerField(db_column='TWILIGHTS_HAMMER', blank=True, null=True)  # Field name made lowercase.
    blackrock = models.IntegerField(db_column='BLACKROCK', blank=True, null=True)  # Field name made lowercase.
    silvermoon = models.IntegerField(db_column='SILVERMOON', blank=True, null=True)  # Field name made lowercase.
    aerie_peak = models.IntegerField(db_column='AERIE_PEAK', blank=True, null=True)  # Field name made lowercase.
    ironforge = models.IntegerField(db_column='IRONFORGE', blank=True, null=True)  # Field name made lowercase.
    dalaran = models.IntegerField(db_column='DALARAN', blank=True, null=True)  # Field name made lowercase.
    kul_tiras = models.IntegerField(db_column='KUL_TIRAS', blank=True, null=True)  # Field name made lowercase.
    stromgarde = models.IntegerField(db_column='STROMGARDE', blank=True, null=True)  # Field name made lowercase.
    azeroth = models.IntegerField(db_column='AZEROTH', blank=True, null=True)  # Field name made lowercase.
    lordaeron = models.IntegerField(db_column='LORDAERON', blank=True, null=True)  # Field name made lowercase.
    gilneas = models.IntegerField(db_column='GILNEAS', blank=True, null=True)  # Field name made lowercase.
    alterac = models.IntegerField(db_column='ALTERAC', blank=True, null=True)  # Field name made lowercase.
    dark_iron = models.IntegerField(db_column='DARK_IRON', blank=True, null=True)  # Field name made lowercase.
    burning_blade = models.IntegerField(db_column='BURNING_BLADE', blank=True, null=True)  # Field name made lowercase.
    frostwolf = models.IntegerField(db_column='FROSTWOLF', blank=True, null=True)  # Field name made lowercase.
    dalaran_rebel = models.IntegerField(db_column='DALARAN_REBEL', blank=True, null=True)  # Field name made lowercase.
    gilneas_rebel = models.IntegerField(db_column='GILNEAS_REBEL', blank=True, null=True)  # Field name made lowercase.
    firetree = models.IntegerField(db_column='FIRETREE', blank=True, null=True)  # Field name made lowercase.
    smolderthorn = models.IntegerField(db_column='SMOLDERTHORN', blank=True, null=True)  # Field name made lowercase.
    shadowpine = models.IntegerField(db_column='SHADOWPINE', blank=True, null=True)  # Field name made lowercase.
    shadowglen = models.IntegerField(db_column='SHADOWGLEN', blank=True, null=True)  # Field name made lowercase.
    revantusk = models.IntegerField(db_column='REVANTUSK', blank=True, null=True)  # Field name made lowercase.
    mossflayer = models.IntegerField(db_column='MOSSFLAYER', blank=True, null=True)  # Field name made lowercase.
    witherbark = models.IntegerField(db_column='WITHERBARK', blank=True, null=True)  # Field name made lowercase.
    vilebranch = models.IntegerField(db_column='VILEBRANCH', blank=True, null=True)  # Field name made lowercase.
    dragon = models.IntegerField(db_column='DRAGON', blank=True, null=True)  # Field name made lowercase.
    demon = models.IntegerField(db_column='DEMON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'savefactions'


class Savehexes(models.Model):
    hex_terrain = models.CharField(db_column='HEX_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_n_terrain = models.CharField(db_column='HEX_N_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_ne_terrain = models.CharField(db_column='HEX_NE_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_se_terrain = models.CharField(db_column='HEX_SE_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_s_terrain = models.CharField(db_column='HEX_S_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_sw_terrain = models.CharField(db_column='HEX_SW_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_nw_terrain = models.CharField(db_column='HEX_NW_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_building = models.IntegerField(db_column='HEX_BUILDING')  # Field name made lowercase.
    hex_oil = models.IntegerField(db_column='HEX_OIL')  # Field name made lowercase.
    hex_farm = models.IntegerField(db_column='HEX_FARM')  # Field name made lowercase.
    hex_mill = models.IntegerField(db_column='HEX_MILL')  # Field name made lowercase.
    hex_rig = models.IntegerField(db_column='HEX_RIG')  # Field name made lowercase.
    hex_gold = models.IntegerField(db_column='HEX_GOLD')  # Field name made lowercase.
    hex_new_combat = models.IntegerField(db_column='HEX_NEW_COMBAT')  # Field name made lowercase.
    hex_battle_fought = models.IntegerField(db_column='HEX_BATTLE_FOUGHT')  # Field name made lowercase.
    hex_n_control = models.IntegerField(db_column='HEX_N_CONTROL')  # Field name made lowercase.
    hex_ne_control = models.IntegerField(db_column='HEX_NE_CONTROL')  # Field name made lowercase.
    hex_se_control = models.IntegerField(db_column='HEX_SE_CONTROL')  # Field name made lowercase.
    hex_s_control = models.IntegerField(db_column='HEX_S_CONTROL')  # Field name made lowercase.
    hex_sw_control = models.IntegerField(db_column='HEX_SW_CONTROL')  # Field name made lowercase.
    hex_nw_control = models.IntegerField(db_column='HEX_NW_CONTROL')  # Field name made lowercase.
    field22 = models.IntegerField(db_column='FIELD22')  # Field name made lowercase.
    hex_expansion_owner = models.IntegerField(db_column='HEX_EXPANSION_OWNER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'savehexes'


class Saveunits(models.Model):
    name = models.CharField(db_column='NAME', max_length=22)  # Field name made lowercase.
    faction = models.IntegerField(db_column='FACTION', blank=True, null=True)  # Field name made lowercase.
    hit_points = models.IntegerField(db_column='HIT_POINTS', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    tier = models.IntegerField(db_column='TIER', blank=True, null=True)  # Field name made lowercase.
    tier_1 = models.CharField(db_column='TIER_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_2 = models.CharField(db_column='TIER_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_3 = models.CharField(db_column='TIER_3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_4 = models.CharField(db_column='TIER_4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    alive = models.IntegerField(db_column='ALIVE', blank=True, null=True)  # Field name made lowercase.
    col_1 = models.IntegerField(db_column='COL_1', blank=True, null=True)  # Field name made lowercase.
    col_2 = models.IntegerField(db_column='COL_2', blank=True, null=True)  # Field name made lowercase.
    col_3 = models.IntegerField(db_column='COL_3', blank=True, null=True)  # Field name made lowercase.
    col_4 = models.IntegerField(db_column='COL_4', blank=True, null=True)  # Field name made lowercase.
    col_5 = models.IntegerField(db_column='COL_5', blank=True, null=True)  # Field name made lowercase.
    col_6 = models.IntegerField(db_column='COL_6', blank=True, null=True)  # Field name made lowercase.
    col_7 = models.IntegerField(db_column='COL_7', blank=True, null=True)  # Field name made lowercase.
    col_8 = models.IntegerField(db_column='COL_8', blank=True, null=True)  # Field name made lowercase.
    col_9 = models.IntegerField(db_column='COL_9', blank=True, null=True)  # Field name made lowercase.
    col_10 = models.IntegerField(db_column='COL_10', blank=True, null=True)  # Field name made lowercase.
    col_11 = models.IntegerField(db_column='COL_11', blank=True, null=True)  # Field name made lowercase.
    col_12 = models.IntegerField(db_column='COL_12', blank=True, null=True)  # Field name made lowercase.
    col_13 = models.IntegerField(db_column='COL_13', blank=True, null=True)  # Field name made lowercase.
    col_14 = models.IntegerField(db_column='COL_14', blank=True, null=True)  # Field name made lowercase.
    col_15 = models.IntegerField(db_column='COL_15', blank=True, null=True)  # Field name made lowercase.
    col_16 = models.IntegerField(db_column='COL_16', blank=True, null=True)  # Field name made lowercase.
    col_17 = models.IntegerField(db_column='COL_17', blank=True, null=True)  # Field name made lowercase.
    col_18 = models.IntegerField(db_column='COL_18', blank=True, null=True)  # Field name made lowercase.
    col_19 = models.IntegerField(db_column='COL_19', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saveunits'


class Specialevents(models.Model):
    event = models.CharField(max_length=25, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialevents'


class Specialorders(models.Model):
    action = models.CharField(max_length=45)
    unit = models.CharField(max_length=45)
    data_1 = models.CharField(max_length=45, blank=True, null=True)
    data_2 = models.CharField(max_length=45, blank=True, null=True)
    data_3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialorders'


class Spectatorbases(models.Model):
    base_name = models.CharField(db_column='BASE_NAME', max_length=45)  # Field name made lowercase.
    base_hex = models.IntegerField(db_column='BASE_HEX')  # Field name made lowercase.
    base_faction = models.IntegerField(db_column='BASE_FACTION')  # Field name made lowercase.
    base_tier = models.IntegerField(db_column='BASE_TIER')  # Field name made lowercase.
    base_gold = models.IntegerField(db_column='BASE_GOLD')  # Field name made lowercase.
    base_lumber = models.IntegerField(db_column='BASE_LUMBER')  # Field name made lowercase.
    base_oil = models.IntegerField(db_column='BASE_OIL')  # Field name made lowercase.
    base_alive = models.IntegerField(db_column='BASE_ALIVE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectatorbases'


class Spectatorbaseslegend(models.Model):
    base_legend = models.IntegerField(db_column='BASE_LEGEND')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectatorbaseslegend'


class Spectatorbuildables(models.Model):
    grunt = models.IntegerField(db_column='GRUNT')  # Field name made lowercase.
    berserker = models.IntegerField(db_column='BERSERKER')  # Field name made lowercase.
    axethrower = models.IntegerField(db_column='AXETHROWER')  # Field name made lowercase.
    ogre = models.IntegerField(db_column='OGRE')  # Field name made lowercase.
    catapult = models.IntegerField(db_column='CATAPULT')  # Field name made lowercase.
    death_knight = models.IntegerField(db_column='DEATH_KNIGHT')  # Field name made lowercase.
    wave_rider = models.IntegerField(db_column='WAVE_RIDER')  # Field name made lowercase.
    turtle = models.IntegerField(db_column='TURTLE')  # Field name made lowercase.
    juggernaut = models.IntegerField(db_column='JUGGERNAUT')  # Field name made lowercase.
    horde_transport = models.IntegerField(db_column='HORDE_TRANSPORT')  # Field name made lowercase.
    dragon = models.IntegerField(db_column='DRAGON')  # Field name made lowercase.
    raider = models.IntegerField(db_column='RAIDER')  # Field name made lowercase.
    shaman = models.IntegerField(db_column='SHAMAN')  # Field name made lowercase.
    warlock = models.IntegerField(db_column='WARLOCK')  # Field name made lowercase.
    footman = models.IntegerField(db_column='FOOTMAN')  # Field name made lowercase.
    archer = models.IntegerField(db_column='ARCHER')  # Field name made lowercase.
    knight = models.IntegerField(db_column='KNIGHT')  # Field name made lowercase.
    ballista = models.IntegerField(db_column='BALLISTA')  # Field name made lowercase.
    mage = models.IntegerField(db_column='MAGE')  # Field name made lowercase.
    destroyer = models.IntegerField(db_column='DESTROYER')  # Field name made lowercase.
    submarine = models.IntegerField(db_column='SUBMARINE')  # Field name made lowercase.
    battleship = models.IntegerField(db_column='BATTLESHIP')  # Field name made lowercase.
    alliance_transport = models.IntegerField(db_column='ALLIANCE_TRANSPORT')  # Field name made lowercase.
    gryphon = models.IntegerField(db_column='GRYPHON')  # Field name made lowercase.
    dwarf = models.IntegerField(db_column='DWARF')  # Field name made lowercase.
    swordsman = models.IntegerField(db_column='SWORDSMAN')  # Field name made lowercase.
    wildhammer_shaman = models.IntegerField(db_column='WILDHAMMER_SHAMAN')  # Field name made lowercase.
    rogue = models.IntegerField(db_column='ROGUE')  # Field name made lowercase.
    skeleton = models.IntegerField(db_column='SKELETON')  # Field name made lowercase.
    demon = models.IntegerField(db_column='DEMON')  # Field name made lowercase.
    elemental = models.IntegerField(db_column='ELEMENTAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectatorbuildables'


class Spectatorcaravans(models.Model):
    originbase = models.CharField(max_length=4)
    destinationbase = models.CharField(max_length=4)
    faction = models.CharField(max_length=4)
    caravantype = models.CharField(max_length=5)
    col_0 = models.CharField(max_length=5, blank=True, null=True)
    col_1 = models.CharField(max_length=5, blank=True, null=True)
    col_2 = models.CharField(max_length=5, blank=True, null=True)
    col_3 = models.CharField(max_length=5, blank=True, null=True)
    col_4 = models.CharField(max_length=5, blank=True, null=True)
    col_5 = models.CharField(max_length=5, blank=True, null=True)
    col_6 = models.CharField(max_length=5, blank=True, null=True)
    col_7 = models.CharField(max_length=5, blank=True, null=True)
    col_8 = models.CharField(max_length=5, blank=True, null=True)
    col_9 = models.CharField(max_length=5, blank=True, null=True)
    col_10 = models.CharField(max_length=5, blank=True, null=True)
    col_11 = models.CharField(max_length=5, blank=True, null=True)
    col_12 = models.CharField(max_length=5, blank=True, null=True)
    col_13 = models.CharField(max_length=5, blank=True, null=True)
    col_14 = models.CharField(max_length=5, blank=True, null=True)
    col_15 = models.CharField(max_length=5, blank=True, null=True)
    col_16 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spectatorcaravans'


class Spectatorhexes(models.Model):
    hex_terrain = models.CharField(db_column='HEX_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_n_terrain = models.CharField(db_column='HEX_N_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_ne_terrain = models.CharField(db_column='HEX_NE_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_se_terrain = models.CharField(db_column='HEX_SE_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_s_terrain = models.CharField(db_column='HEX_S_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_sw_terrain = models.CharField(db_column='HEX_SW_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_nw_terrain = models.CharField(db_column='HEX_NW_TERRAIN', max_length=1)  # Field name made lowercase.
    hex_building = models.IntegerField(db_column='HEX_BUILDING')  # Field name made lowercase.
    hex_oil = models.IntegerField(db_column='HEX_OIL')  # Field name made lowercase.
    hex_farm = models.IntegerField(db_column='HEX_FARM')  # Field name made lowercase.
    hex_mill = models.IntegerField(db_column='HEX_MILL')  # Field name made lowercase.
    hex_rig = models.IntegerField(db_column='HEX_RIG')  # Field name made lowercase.
    hex_gold = models.IntegerField(db_column='HEX_GOLD')  # Field name made lowercase.
    hex_new_combat = models.IntegerField(db_column='HEX_NEW_COMBAT')  # Field name made lowercase.
    hex_battle_fought = models.IntegerField(db_column='HEX_BATTLE_FOUGHT')  # Field name made lowercase.
    hex_n_control = models.IntegerField(db_column='HEX_N_CONTROL')  # Field name made lowercase.
    hex_ne_control = models.IntegerField(db_column='HEX_NE_CONTROL')  # Field name made lowercase.
    hex_se_control = models.IntegerField(db_column='HEX_SE_CONTROL')  # Field name made lowercase.
    hex_s_control = models.IntegerField(db_column='HEX_S_CONTROL')  # Field name made lowercase.
    hex_sw_control = models.IntegerField(db_column='HEX_SW_CONTROL')  # Field name made lowercase.
    hex_nw_control = models.IntegerField(db_column='HEX_NW_CONTROL')  # Field name made lowercase.
    field22 = models.IntegerField(db_column='FIELD22')  # Field name made lowercase.
    hex_expansion_owner = models.IntegerField(db_column='HEX_EXPANSION_OWNER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectatorhexes'


class Spectatorunits(models.Model):
    name = models.CharField(db_column='NAME', max_length=22)  # Field name made lowercase.
    faction = models.IntegerField(db_column='FACTION', blank=True, null=True)  # Field name made lowercase.
    hit_points = models.IntegerField(db_column='HIT_POINTS', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    tier = models.IntegerField(db_column='TIER', blank=True, null=True)  # Field name made lowercase.
    tier_1 = models.CharField(db_column='TIER_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_2 = models.CharField(db_column='TIER_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_3 = models.CharField(db_column='TIER_3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_4 = models.CharField(db_column='TIER_4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    alive = models.IntegerField(db_column='ALIVE', blank=True, null=True)  # Field name made lowercase.
    col_1 = models.IntegerField(db_column='COL_1', blank=True, null=True)  # Field name made lowercase.
    col_2 = models.IntegerField(db_column='COL_2', blank=True, null=True)  # Field name made lowercase.
    col_3 = models.IntegerField(db_column='COL_3', blank=True, null=True)  # Field name made lowercase.
    col_4 = models.IntegerField(db_column='COL_4', blank=True, null=True)  # Field name made lowercase.
    col_5 = models.IntegerField(db_column='COL_5', blank=True, null=True)  # Field name made lowercase.
    col_6 = models.IntegerField(db_column='COL_6', blank=True, null=True)  # Field name made lowercase.
    col_7 = models.IntegerField(db_column='COL_7', blank=True, null=True)  # Field name made lowercase.
    col_8 = models.IntegerField(db_column='COL_8', blank=True, null=True)  # Field name made lowercase.
    col_9 = models.IntegerField(db_column='COL_9', blank=True, null=True)  # Field name made lowercase.
    col_10 = models.IntegerField(db_column='COL_10', blank=True, null=True)  # Field name made lowercase.
    col_11 = models.IntegerField(db_column='COL_11', blank=True, null=True)  # Field name made lowercase.
    col_12 = models.IntegerField(db_column='COL_12', blank=True, null=True)  # Field name made lowercase.
    col_13 = models.IntegerField(db_column='COL_13', blank=True, null=True)  # Field name made lowercase.
    col_14 = models.IntegerField(db_column='COL_14', blank=True, null=True)  # Field name made lowercase.
    col_15 = models.IntegerField(db_column='COL_15', blank=True, null=True)  # Field name made lowercase.
    col_16 = models.IntegerField(db_column='COL_16', blank=True, null=True)  # Field name made lowercase.
    col_17 = models.IntegerField(db_column='COL_17', blank=True, null=True)  # Field name made lowercase.
    col_18 = models.IntegerField(db_column='COL_18', blank=True, null=True)  # Field name made lowercase.
    col_19 = models.IntegerField(db_column='COL_19', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectatorunits'


class Spectatorunitslegend(models.Model):
    units_legend = models.IntegerField(db_column='UNITS_LEGEND')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectatorunitslegend'


class Spectatorvision(models.Model):
    hex = models.IntegerField(db_column='HEX')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spectatorvision'


class Turnstatus(models.Model):
    col_0 = models.IntegerField(db_column='COL_0')  # Field name made lowercase.
    col_1 = models.IntegerField(db_column='COL_1')  # Field name made lowercase.
    col_2 = models.IntegerField(db_column='COL_2')  # Field name made lowercase.
    col_3 = models.IntegerField(db_column='COL_3')  # Field name made lowercase.
    col_4 = models.IntegerField(db_column='COL_4')  # Field name made lowercase.
    col_5 = models.IntegerField(db_column='COL_5')  # Field name made lowercase.
    col_6 = models.IntegerField(db_column='COL_6')  # Field name made lowercase.
    col_7 = models.IntegerField(db_column='COL_7')  # Field name made lowercase.
    col_8 = models.IntegerField(db_column='COL_8')  # Field name made lowercase.
    col_9 = models.IntegerField(db_column='COL_9')  # Field name made lowercase.
    col_10 = models.IntegerField(db_column='COL_10')  # Field name made lowercase.
    col_11 = models.IntegerField(db_column='COL_11')  # Field name made lowercase.
    col_12 = models.IntegerField(db_column='COL_12')  # Field name made lowercase.
    col_13 = models.IntegerField(db_column='COL_13')  # Field name made lowercase.
    col_14 = models.IntegerField(db_column='COL_14')  # Field name made lowercase.
    col_15 = models.IntegerField(db_column='COL_15')  # Field name made lowercase.
    col_16 = models.IntegerField(db_column='COL_16')  # Field name made lowercase.
    col_17 = models.IntegerField(db_column='COL_17')  # Field name made lowercase.
    col_18 = models.IntegerField(db_column='COL_18')  # Field name made lowercase.
    col_19 = models.IntegerField(db_column='COL_19')  # Field name made lowercase.
    col_20 = models.IntegerField(db_column='COL_20')  # Field name made lowercase.
    col_21 = models.IntegerField(db_column='COL_21')  # Field name made lowercase.
    col_22 = models.IntegerField(db_column='COL_22')  # Field name made lowercase.
    col_23 = models.IntegerField(db_column='COL_23')  # Field name made lowercase.
    col_24 = models.IntegerField(db_column='COL_24')  # Field name made lowercase.
    col_25 = models.IntegerField(db_column='COL_25')  # Field name made lowercase.
    col_26 = models.IntegerField(db_column='COL_26')  # Field name made lowercase.
    col_27 = models.IntegerField(db_column='COL_27')  # Field name made lowercase.
    col_28 = models.IntegerField(db_column='COL_28')  # Field name made lowercase.
    col_29 = models.IntegerField(db_column='COL_29')  # Field name made lowercase.
    col_30 = models.IntegerField(db_column='COL_30')  # Field name made lowercase.
    col_31 = models.IntegerField(db_column='COL_31')  # Field name made lowercase.
    col_32 = models.IntegerField(db_column='COL_32', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnstatus'


class Unitdata(models.Model):
    name = models.CharField(db_column='NAME', max_length=30)  # Field name made lowercase.
    faction = models.IntegerField(db_column='FACTION', blank=True, null=True)  # Field name made lowercase.
    hit_points = models.IntegerField(db_column='HIT_POINTS', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    tier = models.IntegerField(db_column='TIER', blank=True, null=True)  # Field name made lowercase.
    tier_1 = models.CharField(db_column='TIER_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_2 = models.CharField(db_column='TIER_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_3 = models.CharField(db_column='TIER_3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tier_4 = models.CharField(db_column='TIER_4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    alive = models.IntegerField(db_column='ALIVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unitdata'


class Unitstats(models.Model):
    name = models.CharField(db_column='NAME', max_length=22)  # Field name made lowercase.
    max_hp = models.IntegerField(db_column='MAX_HP', blank=True, null=True)  # Field name made lowercase.
    combat = models.IntegerField(db_column='COMBAT', blank=True, null=True)  # Field name made lowercase.
    category = models.IntegerField(db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    light_armor = models.IntegerField(db_column='LIGHT_ARMOR', blank=True, null=True)  # Field name made lowercase.
    heavy_armor = models.IntegerField(db_column='HEAVY_ARMOR', blank=True, null=True)  # Field name made lowercase.
    natural_armor = models.IntegerField(db_column='NATURAL_ARMOR', blank=True, null=True)  # Field name made lowercase.
    movement = models.IntegerField(db_column='MOVEMENT', blank=True, null=True)  # Field name made lowercase.
    vision = models.IntegerField(db_column='VISION', blank=True, null=True)  # Field name made lowercase.
    gold_cost = models.IntegerField(db_column='GOLD_COST', blank=True, null=True)  # Field name made lowercase.
    lumber_cost = models.IntegerField(db_column='LUMBER_COST', blank=True, null=True)  # Field name made lowercase.
    oil_cost = models.IntegerField(db_column='OIL_COST', blank=True, null=True)  # Field name made lowercase.
    min_tier = models.IntegerField(db_column='MIN_TIER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unitstats'
