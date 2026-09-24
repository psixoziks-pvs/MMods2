package ru.pnecrome;

import net.minecraft.ChatFormatting;
import net.minecraft.network.chat.Component;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResultHolder;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.TooltipFlag;
import net.minecraft.world.level.Level;

import java.util.List;

/** Некрономикон — книга гибридов: список всех известных скрещиваний и их имён. */
public class NecronomiconItem extends Item {

    public NecronomiconItem(Properties props) {
        super(props);
    }

    @Override
    public void appendHoverText(ItemStack stack, Level level, List<Component> tooltip, TooltipFlag flag) {
        tooltip.add(Component.translatable("item.pnecrome.necronomicon.tip").withStyle(ChatFormatting.GRAY));
    }

    @Override
    public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand hand) {
        if (!level.isClientSide) {
            int i = 0;
            for (HybridDef def : HybridRegistry.all()) {
                if (i++ >= 10) break; // первые записи, чтобы не затапливать чат
                player.sendSystemMessage(Component.literal(def.nameRu + " (" + def.nameEn + ") — " + def.description)
                        .withStyle(ChatFormatting.DARK_PURPLE));
            }
        }
        return InteractionResultHolder.sidedSuccess(player.getItemInHand(hand), level.isClientSide);
    }
}
