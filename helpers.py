






def bbm(lvl):
    '''return multiplier that gets mutliplied by stat_lvl
        to calculate base_stat for a given champ lvl'''
    return (lvl - 1) * (0.685 + 0.0175 * lvl) 



def round_recurse(new, oldnum, recursion=0):
    if round(new, recursion) != oldnum:
        return round(new, recursion)
    round_recurse(new, oldnum, recursion + 1)
    # this can cause some weirdness when the new is rounded 
    # but the oldnum was rounded to a decimal







