



















from globals_ import *
import dmgheal
import cooldown

class R(ABS_R):

    RANGE = 1400

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._CD = cooldown.Cooldown(CHAMP  = self.CHAMP, 
                                    OWNER  = self,
                                    name   = ['cd-refresh', str(self.CHAMP) + '.Q'], 
                                    length = None)
        self._pdmg = dmgheal.PDmg(CHAMP  = self.CHAMP, 
                                  OWNER  = self, 
                                  target = None,
                                  amount = None, 
                                  tags   = {'aoe', 'ability'})

        # observer to know when someone is airborne?

    def cast(self):
        self.CD.trigger()
        self.pdmg.apply()
        self.CHAMP.Q.STACK.drop_stack()
        self.CHAMP.P.STACK.add(999)
        # suspend target for 1s, then do dmg
        # give self buff


    @property
    def CD(self):
        self._CD.length = 80 - 25 * self.lvlups 
        return self._CD
    @property
    def pdmg(self):
        self._pdmg.target = self.CHAMP.target
        self._pdmg.amount = 200 + 100 * self.lvlups + 1.5 * self.CHAMP.bonus_ad
        return self._pdmg











# R
# tgt range = 1400 
# CD = 80 - 25.0 * self.lvlups 

# active: self blinks to visible airborne enChamp nearest to cursor
# instantly generating 100 flow STACK but resetting steel tempest

# upon arrival, he suspends all nearby airborne ems for 1s, do pDmg thereafter.

# pDmg: 200 + 100.0 * self.lvlups (+ 150% ++ ad)

# for next 15s, selfs crit strikes give 50% ++ armor penetration.

# tgting         auto
# affects        ems
# dmg            phy
# type           sin-tgt
# sShield        blocked
# grounded       disabled
# minion aggro   true
# knockdown      irupted

# notes
# Rs aoe when suspending ems incrs per rank.
# R place self behind his main tgt.
# if however he blinks to em close to em turret, 
# R attempt positioning him outside turret range (wont give to nexus obelisk).

# Rs dmg and ++ armor penetration do not interact with each other.
# Rs ++ armor penetration give before lethality.

# suspended ems are immune to further displacements during Rs animation time.
# casting right after triggering displacement(s) overwrite latters dur (whether shorter/longer) to Rs animation time (durs wont STACK)
# casting right before suspended ems land make them remain airborne for Rs animation time (durs STACK)

# only self-applied displacements cant be tgted by R:
# ems displaced by neutral mons (e.g
# dragons initial knock-back) can be tgted.
# ems who displace themselves (e.g
# lets bounce!, satchel charge) cant be tgted.

# the following abilties are considered displacements and interact with R:

# aatroxs dark flight
# alistars pulverize and headbutt
# anivias crystallize (possible bug: give to both ally and em anivia)
# azirs emperors divide
# blitzcranks rocket grab and power fist
# braums glacial fissure
# chogaths rupture
# dianas moonfall
# darius' apprehend
# dravens stand aside
# fizzs chum waters
# mega gnars gnar!
# gragas' explosive cask
# hecarims devastating charge
# jannas howling gale and monsoon
# jarvan ivs demacian standard + dragon strike
# jayces thundering blow
# kalistas fates call
# lee sins dragons rage
# lulus wild growth
# malphites unstoppable force
# maokais bramble smash
# namis aqua prison and tidal wave
# nautilus' dredge line and depth charge
# oriannas command shockwave
# ornns volcanic rupture (possible bug: give to both ally and em ornn)
# poppys heroic charge and poppys steadfast presence when stopping ems mid-dash
# quinns vault
# rammus' powerball
# rakans grand entrance
# reksais unburrow
# rivens broken wings' third cast
# sejuanis arctic assault
# singeds fling
# shyvanas dragons descent
# swains ravenous flock ravenous
# syndras scatter weak
# threshs death sentence and flays active
# tristanas buster shot
# trundles pillar of ice (possible bug: give to both ally and em trundle)
# vaynes condemn
# velkozs tectonic disruption
# vis vault breaker and assault and battery
# volibears rolling thunder
# wukongs cyclone
# xin zhaos three talon strikes third hit and crescent guard
# selfs steel tempests third hit and R
# zacs elastic slingshot and lets bounce! when hitting ems
# ziggs' satchel charge when hitting ems
# zyras stranglethorns

