from PlayerAuras import PlayerAura, WaterAura, EarthAura, FireAura, IceAura

aura_object = PlayerAura()
aura_object = WaterAura(aura_object)
aura_object = EarthAura(aura_object)
aura_object = FireAura(aura_object)
aura_object = IceAura(aura_object)
aura_object.print_auras()
