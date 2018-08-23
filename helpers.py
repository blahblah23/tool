






def bbm(lvl):
    '''return multiplier that gets mutliplied by stat_lvl
        to calculate base_stat for a given champ lvl'''
    return (lvl - 1) * (0.685 + 0.0175 * lvl) 





