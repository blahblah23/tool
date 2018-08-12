










game
    champs
        level
        stats    
        abils
            toggle vs active vs passive
            abilvl(champlvl, scheme)
            metric_scale
                type_of metric
                base & scale value
            mana cost
            health cost
        auto
            1.auto_start
                change_state(to_casting)
                notify__auto_start()
                cast_timer()
            2.wait_for_timer
            3.auto_send on cast_timer
                change_state(to_idle)
                notify__auto_send()
                auto_cooldown
                melee:::5.auto_land()
                ranged:::proj_timer()
            4.wait_for_timer
            5.auto_land() on proj_timer
                get&apply_dmg
                    # lots of code
                    # lots of code
                notify__auto_land()     #notify before/after dealing damage so that on hit effects can apply?
              6.auto_cooldown.refresh() on auto_cooldown
          state machine
              states
                  idle
                  casting
                      casttime
                  airborne
                      knockback
                      knock aside
                      knockup
                      pull
                  entangle
                      disarm
                      root/snare
                  pacify/polymorph
                      disarm
                      silence
                  blind
                  cripple
                  disarm
                  forced action
                      charm
                      fear/flee
                      taunt
                  knockdown
                  ground
                  nearsight
                  root/snared
                  silence
                  disrupt
                  sleep
                  slow
                  stasis
                  stun
                      suspension
                  suppress
                      -movement
                      -attacks
                      -abilities
                      -summs
                      -actives
                      interrupts
                          channeled abilites
                          charged abilities
    projectile travel time
    cast time
    on hit
    grievous wounds
    cooldown
    length
    items
    runes
    summs
    time
    Healing
        generic heal
        health regen
        life steal
        spell vamp
        drain effects   # deaths dance, red elixir, gunblade, ravenous hunter
    Damage
        types
            magic
            physical
            true
                pure
            Critical damage
            Pet damage
            Ability damage
            Basic attack damage
            Bleed damage/damage over time
            On-hit damage
            Splash/AoE damage
        things that change outgoing flat numbers
            penetration
            %multipliers
                blanket
                    exhaust
                    sona aria of perseverance
                    runes(coupdegrace, cut down, last stand)
                type-specific
                    vayne tumble gives %ofAD bonus


































