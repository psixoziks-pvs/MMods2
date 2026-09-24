package ru.pnecrome;

import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.chat.Component;
import net.minecraft.network.chat.MutableComponent;
import net.minecraft.world.item.ItemStack;

import java.util.Locale;

/**
 * Части тел — один предмет pnecrome:part с NBT {owner, part}.
 * Имя предмета собирается из донора и части: «Голова крипера».
 */
public class PartItems {

    public static ItemStack make(String donorId, BodyPart part) {
        ItemStack stack = new ItemStack(PNecrome.PART.get());
        CompoundTag tag = new CompoundTag();
        tag.putString("pnecrome_owner", donorId);
        tag.putString("pnecrome_part", part.key());
        stack.setTag(tag);
        return stack;
    }

    public static boolean isPart(ItemStack stack) {
        if (stack.isEmpty()) return false;
        CompoundTag tag = stack.getTag();
        return tag != null && tag.contains("pnecrome_owner") && tag.contains("pnecrome_part");
    }

    public static String ownerOf(ItemStack stack) {
        CompoundTag tag = stack == null ? null : stack.getTag();
        return (tag == null || !tag.contains("pnecrome_owner")) ? null : tag.getString("pnecrome_owner");
    }

    public static BodyPart partOf(ItemStack stack) {
        CompoundTag tag = stack == null ? null : stack.getTag();
        if (tag == null || !tag.contains("pnecrome_part")) return null;
        return BodyPart.byKey(tag.getString("pnecrome_part"));
    }

    public static MutableComponent displayName(ItemStack stack) {
        String owner = norm(ownerOf(stack));
        BodyPart p = partOf(stack);
        String donorName = DonorNames.get(owner);
        return Component.literal((p == null ? "?" : p.ruName()) + " " + donorName);
    }

    private static String norm(String registryId) {
        if (registryId == null) return "";
        String s = registryId.toLowerCase(Locale.ROOT);
        if (s.startsWith("minecraft:")) s = s.substring("minecraft:".length());
        return s;
    }
}
