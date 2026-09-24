package ru.pnecrome;

import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.TooltipFlag;
import net.minecraft.world.level.Level;

import java.util.List;

/** Часть тела: имя предмета зависит от NBT-донора («Голова крипера»). */
public class PartItem extends Item {

    public PartItem(Properties props) {
        super(props);
    }

    @Override
    public Component getName(ItemStack stack) {
        if (PartItems.isPart(stack)) {
            return PartItems.displayName(stack);
        }
        return super.getName(stack);
    }

    @Override
    public void appendHoverText(ItemStack stack, Level level, List<Component> tooltip, TooltipFlag flag) {
        if (PartItems.isPart(stack)) {
            tooltip.add(Component.translatable("item.pnecrome.part.tip").withStyle(ChatFormatting.GRAY));
        }
    }
}
