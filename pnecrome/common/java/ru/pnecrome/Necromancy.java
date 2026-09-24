package ru.pnecrome;

import net.minecraft.core.BlockPos;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.chat.Component;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.AABB;

import java.util.List;
import java.util.Locale;

/** Ядро некромантии: трупы, распил, приживление. */
public class Necromancy {

    public static final String TAG_CORPSE = "pnecrome_corpse";
    public static final String TAG_HYBRID = "pnecrome_hybrid";
    public static final long CORPSE_TTL_MS = 120_000L; // 2 минуты на распиловку

    /** Мёртвое, но ещё не разложившееся тело можно пилить. */
    public static boolean isCorpse(LivingEntity e) {
        return e != null && !e.isAlive() && e.getTag() != null && e.getTag().contains(TAG_CORPSE);
    }

    public static void markCorpse(LivingEntity e) {
        CompoundTag tag = new CompoundTag();
        tag.putLong("pnecrome_time", System.currentTimeMillis());
        e.getOrCreateTag().put(TAG_CORPSE, tag);
        e.setCustomName(Component.literal(corpseName(e)));
        e.setCustomNameVisible(true);
    }

    private static String corpseName(LivingEntity e) {
        return "Труп: " + DonorNames.get(vanillaId(e));
    }

    /** Распил трупа: дроп 4 частей (голова, руки, ноги, туловище). */
    public static void sawCorpse(Level level, Player player, LivingEntity corpse) {
        String donor = vanillaId(corpse);
        for (BodyPart part : BodyPart.values()) {
            ItemStack drop = PartItems.make(donor, part);
            popItem(level, corpse.blockPosition(), drop);
        }
        level.playSound(null, corpse.blockPosition(), SoundEvents.SKELETON_AMBIENT, SoundSource.PLAYERS, 0.7f, 1.4f);
        corpse.discard();
        Messages.sawn(player, Component.literal(DonorNames.get(donor)));
    }

    /** Приживление: часть донора -> живой моб => гибрид со своим именем. */
    public static boolean graft(Level level, Player player, LivingEntity victim, ItemStack partStack) {
        String donor = PartItems.ownerOf(partStack);
        BodyPart part = PartItems.partOf(partStack);
        if (donor == null || part == null) return false;
        String base = vanillaId(victim);
        if (donor.equals(base)) {
            Messages.rejected(player); // своя же голова жертве не нужна
            return false;
        }
        HybridDef proto = HybridRegistry.firstFor(donor, part);
        if (proto == null) {
            Messages.rejected(player);
            return false;
        }
        HybridDef def = new HybridDef(proto.id + "_" + strip(base), base, part.key(), donor,
                proto.nameRu, proto.nameEn, proto.hpMul, proto.speedMul, proto.dmgMul,
                proto.fireImmune, proto.description);
        applyHybrid(victim, def);
        partStack.shrink(1);
        level.playSound(null, victim.blockPosition(), SoundEvents.EVOCATION_CAST_SPELL, SoundSource.PLAYERS, 1f, 0.6f);
        Messages.grafted(player, Component.literal(def.nameRu));
        return true;
    }

    public static void applyHybrid(LivingEntity victim, HybridDef def) {
        CompoundTag st = new CompoundTag();
        st.putString("id", def.id);
        st.putString("base", def.baseId);
        st.putString("part", def.part.key());
        st.putString("donor", def.donorId);
        victim.getOrCreateTag().put(TAG_HYBRID, st);
        victim.setCustomName(Component.literal(def.nameRu));
        victim.setCustomNameVisible(true);
        double baseMax = victim.getMaxHealth();
        victim.setHealth((float) Math.max(1.0, baseMax * def.hpMul));
        HybridAttributes.apply(victim);
    }

    public static HybridDef hybridOf(LivingEntity e) {
        if (e == null || e.getTag() == null || !e.getTag().contains(TAG_HYBRID)) return null;
        CompoundTag st = e.getTag().getCompound(TAG_HYBRID);
        String base = st.getString("base");
        BodyPart part = BodyPart.byKey(st.getString("part"));
        String donor = st.getString("donor");
        if (base == null || part == null || donor == null) return null;
        HybridDef proto = HybridRegistry.firstFor(donor, part);
        if (proto == null) return null;
        return new HybridDef(st.getString("id"), base, part.key(), donor, proto.nameRu, proto.nameEn,
                proto.hpMul, proto.speedMul, proto.dmgMul, proto.fireImmune, proto.description);
    }

    public static LivingEntity findNearbyCorpse(Player player) {
        AABB box = player.getBoundingBox().inflate(3.5);
        List<LivingEntity> list = player.level.getEntitiesOfClass(LivingEntity.class, box, Necromancy::isCorpse);
        return list.isEmpty() ? null : list.get(0);
    }

    public static String vanillaId(LivingEntity e) {
        String s = ForgeHooks.entityTypeId(e);
        return s == null ? "" : s.toLowerCase(Locale.ROOT);
    }

    private static String strip(String fullId) {
        int i = fullId.indexOf(':');
        return i >= 0 ? fullId.substring(i + 1) : fullId;
    }

    public static void popItem(Level level, BlockPos pos, ItemStack stack) {
        ForgeHooks.spawnItem(level, pos, stack);
    }
}
