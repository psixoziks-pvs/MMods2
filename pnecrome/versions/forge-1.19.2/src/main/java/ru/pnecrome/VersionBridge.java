package ru.pnecrome;

import net.minecraft.core.BlockPos;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;

/** Мостик к API Minecraft 1.19.2 (модлоадер Forge/NeoForge). */
public class VersionBridge {

    public static String entityTypeId(LivingEntity e) {
        ResourceLocation rl = net.minecraftforge.registries.ForgeRegistries.ENTITY_TYPES.getKey(e.getType());
        return rl == null ? "" : rl.toString();
    }

    public static void spawnItem(Level level, BlockPos pos, ItemStack stack) {
        double x = pos.getX() + 0.5, y = pos.getY() + 0.5, z = pos.getZ() + 0.5;
        ItemEntity it = new ItemEntity(level, x, y, z, stack);
        it.setPickUpDelay(40);
        level.addFreshEntity(it);
    }

    public static double defaultMoveSpeed(LivingEntity e) {
        Double v = e.getAttributeBaseValue(Attributes.MOVEMENT_SPEED);
        return v == null ? 0.2 : v;
    }

    public static double defaultAttackDamage(LivingEntity e) {
        Double v = e.getAttributeBaseValue(Attributes.ATTACK_DAMAGE);
        return v == null ? 2.0 : v;
    }
}
