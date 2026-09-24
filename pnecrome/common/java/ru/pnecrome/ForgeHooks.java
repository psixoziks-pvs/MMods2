package ru.pnecrome;

import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;

/** Небольшие мостики к версии-специфичному коду (VersionBridge в каждом source set версии). */
public class ForgeHooks {

    public static String entityTypeId(LivingEntity e) {
        return VersionBridge.entityTypeId(e);
    }

    public static void spawnItem(Level level, BlockPos pos, ItemStack stack) {
        VersionBridge.spawnItem(level, pos, stack);
    }

    public static double defaultMoveSpeed(LivingEntity e) {
        return VersionBridge.defaultMoveSpeed(e);
    }

    public static double defaultAttackDamage(LivingEntity e) {
        return VersionBridge.defaultAttackDamage(e);
    }
}
