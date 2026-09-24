package ru.pnecrome;

import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.ai.attributes.AttributeInstance;
import net.minecraft.world.entity.ai.attributes.Attributes;

/** Применение множителей подвида к атрибутам гибрида. */
public class HybridAttributes {

    public static void apply(LivingEntity e) {
        HybridDef def = Necromancy.hybridOf(e);
        if (def == null) return;
        AttributeInstance mov = e.getAttribute(Attributes.MOVEMENT_SPEED);
        if (mov != null) {
            mov.setBaseValue(ForgeHooks.defaultMoveSpeed(e) * def.speedMul);
        }
        AttributeInstance atk = e.getAttribute(Attributes.ATTACK_DAMAGE);
        if (atk != null) {
            atk.setBaseValue(ForgeHooks.defaultAttackDamage(e) * def.dmgMul);
        }
    }
}
