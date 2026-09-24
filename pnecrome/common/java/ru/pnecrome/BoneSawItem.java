package ru.pnecrome;

import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.context.UseOnContext;
import net.minecraft.world.level.Level;

/**
 * Костяная пила. Правый клик по свежему трупу распиливает его на части тел.
 */
public class BoneSawItem extends Item {

    public BoneSawItem(Properties props) {
        super(props);
    }

    @Override
    public InteractionResult useOn(UseOnContext ctx) {
        Level level = ctx.getLevel();
        Player player = ctx.getPlayer();
        if (player == null) return InteractionResult.PASS;
        if (!level.isClientSide) {
            LivingEntity corpse = Necromancy.findNearbyCorpse(player);
            if (corpse != null) {
                Necromancy.sawCorpse(level, player, corpse);
                return InteractionResult.SUCCESS;
            }
            Messages.noCorpse(player);
        }
        return InteractionResult.sidedSuccess(level.isClientSide);
    }

    @Override
    public InteractionResult interactLivingEntity(ItemStack stack, Player player,
                                                  LivingEntity target, InteractionHand hand) {
        if (!player.level.isClientSide && Necromancy.isCorpse(target)) {
            Necromancy.sawCorpse(player.level, player, target);
            return InteractionResult.SUCCESS;
        }
        return InteractionResult.PASS;
    }
}
